import copy
from typing import Union

from einops import rearrange
from torch import Tensor
import torch.nn.functional as F
import torch

import quasar.model_management
import quasar.utils
from quasar.model_patcher import ModelPatcher
from quasar.model_base import BaseModel

from .ad_settings import AnimateDiffSettings, AdjustPE, AdjustWeight
from .context import ContextOptions, ContextOptions, ContextOptionsGroup
from .motion_module_ad import AnimateDiffModel, AnimateDiffFormat, EncoderOnlyAnimateDiffModel, has_mid_block, normalize_ad_state_dict
from .logger import logger
from .utils_motion import ADKeyframe, ADKeyframeGroup, MotionCompatibilityError, get_combined_multival, ade_broadcast_image_to, normalize_min_max
from .motion_lora import MotionLoraInfo, MotionLoraList
from .utils_model import get_motion_lora_path, get_motion_model_path, get_sd_model_type
from .sample_settings import SampleSettings, SeedNoiseGeneration


# some motion_model casts here might fail if model becomes metatensor or is not castable;
# should not really matter if it fails, so ignore raised Exceptions
class ModelPatcherAndInjector(ModelPatcher):
    def __init__(self, m: ModelPatcher):
        # replicate ModelPatcher.clone() to initialize ModelPatcherAndInjector
        super().__init__(m.model, m.load_device, m.offload_device, m.size, m.current_device, weight_inplace_update=m.weight_inplace_update)
        self.patches = {}
        for k in m.patches:
            self.patches[k] = m.patches[k][:]
        if hasattr(m, "patches_uuid"):
            self.patches_uuid = m.patches_uuid

        self.object_patches = m.object_patches.copy()
        self.model_options = copy.deepcopy(m.model_options)
        self.model_keys = m.model_keys
        if hasattr(m, "backup"):
            self.backup = m.backup
        if hasattr(m, "object_patches_backup"):
            self.object_patches_backup = m.object_patches_backup


        # injection stuff
        self.motion_injection_params: InjectionParams = None
        self.sample_settings: SampleSettings = SampleSettings()
        self.motion_models: MotionModelGroup = None
    
    def model_patches_to(self, device):
        super().model_patches_to(device)
        if self.motion_models is not None:
            for motion_model in self.motion_models.models:
                try:
                    motion_model.model.to(device)
                except Exception:
                    pass

    def patch_model(self, device_to=None, patch_weights=True):
        # first, perform model patching
        if patch_weights: # TODO: keep only 'else' portion when don't need to worry about past quasar versions
            patched_model = super().patch_model(device_to)
        else:
            patched_model = super().patch_model(device_to, patch_weights)
        # finally, perform motion model injection
        self.inject_model(device_to=device_to)
        return patched_model

    def unpatch_model(self, device_to=None, unpatch_weights=True):
        # first, eject motion model from unet
        self.eject_model(device_to=device_to)
        # finally, do normal model unpatching
        if unpatch_weights: # TODO: keep only 'else' portion when don't need to worry about past quasar versions
            return super().unpatch_model(device_to)
        else:
            return super().unpatch_model(device_to, unpatch_weights)

    def inject_model(self, device_to=None):
        if self.motion_models is not None:
            for motion_model in self.motion_models.models:
                motion_model.model.inject(self)
                try:
                    motion_model.model.to(device_to)
                except Exception:
                    pass

    def eject_model(self, device_to=None):
        if self.motion_models is not None:
            for motion_model in self.motion_models.models:
                motion_model.model.eject(self)
                try:
                    motion_model.model.to(device_to)
                except Exception:
                    pass

    def clone(self):
        cloned = ModelPatcherAndInjector(self)
        cloned.motion_models = self.motion_models.clone() if self.motion_models else self.motion_models
        cloned.sample_settings = self.sample_settings
        cloned.motion_injection_params = self.motion_injection_params.clone() if self.motion_injection_params else self.motion_injection_params
        return cloned


class MotionModelPatcher(ModelPatcher):
    # Mostly here so that type hints work in IDEs
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.model: AnimateDiffModel = self.model
        self.timestep_percent_range = (0.0, 1.0)
        self.timestep_range: tuple[float, float] = None
        self.keyframes: ADKeyframeGroup = ADKeyframeGroup()

        self.scale_multival = None
        self.effect_multival = None

        # AnimateLCM-I2V
        self.orig_ref_drift: float = None
        self.orig_insertion_weights: list[float] = None
        self.orig_apply_ref_when_disabled = False
        self.orig_img_latents: Tensor = None
        self.img_features: list[int, Tensor] = None  # temporary
        self.img_latents_shape: tuple = None

        # temporary variables
        self.current_used_steps = 0
        self.current_keyframe: ADKeyframe = None
        self.current_index = -1
        self.current_scale: Union[float, Tensor] = None
        self.current_effect: Union[float, Tensor] = None
        self.combined_scale: Union[float, Tensor] = None
        self.combined_effect: Union[float, Tensor] = None
        self.was_within_range = False
        self.prev_sub_idxs = None
        self.prev_batched_number = None

    def patch_model(self, *args, **kwargs):
        # patch as normal; used to need to do prepare_weights call to work with lowvram, but no longer needed
        # will consider removing this override at some point since it does nothing at the moment
        patched_model = super().patch_model(*args, **kwargs)
        return patched_model

    def pre_run(self, model: ModelPatcherAndInjector):
        self.cleanup()
        self.model.set_scale(self.scale_multival)
        self.model.set_effect(self.effect_multival)
        if self.model.img_encoder is not None:
            self.model.img_encoder.set_ref_drift(self.orig_ref_drift)
            self.model.img_encoder.set_insertion_weights(self.orig_insertion_weights)

    def initialize_timesteps(self, model: BaseModel):
        self.timestep_range = (model.model_sampling.percent_to_sigma(self.timestep_percent_range[0]),
                               model.model_sampling.percent_to_sigma(self.timestep_percent_range[1]))
        if self.keyframes is not None:
            for keyframe in self.keyframes.keyframes:
                keyframe.start_t = model.model_sampling.percent_to_sigma(keyframe.start_percent)

    def prepare_current_keyframe(self, t: Tensor):
        curr_t: float = t[0]
        prev_index = self.current_index
        # if met guaranteed steps, look for next keyframe in case need to switch
        if self.current_keyframe is None or self.current_used_steps >= self.current_keyframe.guarantee_steps:
            # if has next index, loop through and see if need to switch
            if self.keyframes.has_index(self.current_index+1):
                for i in range(self.current_index+1, len(self.keyframes)):
                    eval_kf = self.keyframes[i]
                    # check if start_t is greater or equal to curr_t
                    # NOTE: t is in terms of sigmas, not percent, so bigger number = earlier step in sampling
                    if eval_kf.start_t >= curr_t:
                        self.current_index = i
                        self.current_keyframe = eval_kf
                        self.current_used_steps = 0
                        # keep track of scale and effect multivals, accounting for inherit_missing
                        if self.current_keyframe.has_scale():
                            self.current_scale = self.current_keyframe.scale_multival
                        elif not self.current_keyframe.inherit_missing:
                            self.current_scale = None
                        if self.current_keyframe.has_effect():
                            self.current_effect = self.current_keyframe.effect_multival
                        elif not self.current_keyframe.inherit_missing:
                            self.current_effect = None
                        # if guarantee_steps greater than zero, stop searching for other keyframes
                        if self.current_keyframe.guarantee_steps > 0:
                            break
                    # if eval_kf is outside the percent range, stop looking further
                    else:
                        break
        # if index changed, apply new combined values
        if prev_index != self.current_index:
            # combine model's scale and effect with keyframe's scale and effect
            self.combined_scale = get_combined_multival(self.scale_multival, self.current_scale)
            self.combined_effect = get_combined_multival(self.effect_multival, self.current_effect)
            # apply scale and effect
            self.model.set_scale(self.combined_scale)
            self.model.set_effect(self.combined_effect)
        # apply effect - if not within range, set effect to 0, effectively turning model off
        if curr_t > self.timestep_range[0] or curr_t < self.timestep_range[1]:
            self.model.set_effect(0.0)
            self.was_within_range = False
        else:
            # if was not in range last step, apply effect to toggle AD status
            if not self.was_within_range:
                self.model.set_effect(self.combined_effect)
                self.was_within_range = True
        # update steps current keyframe is used
        self.current_used_steps += 1

    def prepare_img_features(self, x: Tensor, cond_or_uncond: list[int], ad_params: dict[str], latent_format):
        # if no img_encoder, done
        if self.model.img_encoder is None:
            return
        batched_number = len(cond_or_uncond)
        full_length = ad_params["full_length"]
        sub_idxs = ad_params["sub_idxs"]
        goal_length = x.size(0) // batched_number
        # calculate img_features if needed
        if (self.img_latents_shape is None or sub_idxs != self.prev_sub_idxs or batched_number != self.prev_batched_number
                or x.shape[2] != self.img_latents_shape[2] or x.shape[3] != self.img_latents_shape[3]):
            if sub_idxs is not None and self.orig_img_latents.size(0) >= full_length:
                img_latents = quasar.utils.common_upscale(self.orig_img_latents[sub_idxs], x.shape[3], x.shape[2], 'nearest-exact', 'center').to(x.dtype).to(x.device)
            else:
                img_latents = quasar.utils.common_upscale(self.orig_img_latents, x.shape[3], x.shape[2], 'nearest-exact', 'center').to(x.dtype).to(x.device)
            img_latents = latent_format.process_in(img_latents)
            # make sure img_latents matches goal_length
            if goal_length != img_latents.shape[0]:
                img_latents = ade_broadcast_image_to(img_latents, goal_length, batched_number)
            img_features = self.model.img_encoder(img_latents, goal_length, batched_number)
            self.model.set_img_features(img_features=img_features, apply_ref_when_disabled=self.orig_apply_ref_when_disabled)
            # cache values for next step
            self.img_latents_shape = img_latents.shape
        self.prev_sub_idxs = sub_idxs
        self.prev_batched_number = batched_number

    def cleanup(self):
        if self.model is not None:
            self.model.cleanup()
        # AnimateLCM-I2V
        del self.img_features
        self.img_features = None
        self.img_latents_shape = None
        # Default
        self.current_used_steps = 0
        self.current_keyframe = None
        self.current_index = -1
        self.current_scale = None
        self.current_effect = None
        self.combined_scale = None
        self.combined_effect = None
        self.was_within_range = False
        self.prev_sub_idxs = None
        self.prev_batched_number = None

    def clone(self):
        # normal ModelPatcher clone actions
        n = MotionModelPatcher(self.model, self.load_device, self.offload_device, self.size, self.current_device, weight_inplace_update=self.weight_inplace_update)
        n.patches = {}
        for k in self.patches:
            n.patches[k] = self.patches[k][:]
        if hasattr(n, "patches_uuid"):
            self.patches_uuid = n.patches_uuid

        n.object_patches = self.object_patches.copy()
        n.model_options = copy.deepcopy(self.model_options)
        n.model_keys = self.model_keys
        if hasattr(n, "backup"):
            self.backup = n.backup
        if hasattr(n, "object_patches_backup"):
            self.object_patches_backup = n.object_patches_backup
        # extra cloned params
        n.timestep_percent_range = self.timestep_percent_range
        n.timestep_range = self.timestep_range
        n.keyframes = self.keyframes.clone()
        n.scale_multival = self.scale_multival
        n.effect_multival = self.effect_multival
        n.orig_img_latents = self.orig_img_latents
        n.orig_ref_drift = self.orig_ref_drift
        n.orig_insertion_weights = self.orig_insertion_weights.copy() if self.orig_insertion_weights is not None else self.orig_insertion_weights
        n.orig_apply_ref_when_disabled = self.orig_apply_ref_when_disabled
        return n


class MotionModelGroup:
    def __init__(self, init_motion_model: MotionModelPatcher=None):
        self.models: list[MotionModelPatcher] = []
        if init_motion_model is not None:
            self.add(init_motion_model)

    def add(self, mm: MotionModelPatcher):
        # add to end of list
        self.models.append(mm)

    def add_to_start(self, mm: MotionModelPatcher):
        self.models.insert(0, mm)

    def __getitem__(self, index) -> MotionModelPatcher:
        return self.models[index]
    
    def is_empty(self) -> bool:
        return len(self.models) == 0
    
    def clone(self) -> 'MotionModelGroup':
        cloned = MotionModelGroup()
        for mm in self.models:
            cloned.add(mm)
        return cloned
    
    def set_sub_idxs(self, sub_idxs: list[int]):
        for motion_model in self.models:
            motion_model.model.set_sub_idxs(sub_idxs=sub_idxs)
    
    def set_view_options(self, view_options: ContextOptions):
        for motion_model in self.models:
            motion_model.model.set_view_options(view_options)

    def set_video_length(self, video_length: int, full_length: int):
        for motion_model in self.models:
            motion_model.model.set_video_length(video_length=video_length, full_length=full_length)
    
    def initialize_timesteps(self, model: BaseModel):
        for motion_model in self.models:
            motion_model.initialize_timesteps(model)

    def pre_run(self, model: ModelPatcherAndInjector):
        for motion_model in self.models:
            motion_model.pre_run(model)
    
    def cleanup(self):
        for motion_model in self.models:
            motion_model.cleanup()
    
    def prepare_current_keyframe(self, t: Tensor):
        for motion_model in self.models:
            motion_model.prepare_current_keyframe(t=t)

    def get_name_string(self, show_version=False):
        identifiers = []
        for motion_model in self.models:
            id = motion_model.model.mm_info.mm_name
            if show_version:
                id += f":{motion_model.model.mm_info.mm_version}"
            identifiers.append(id)
        return ", ".join(identifiers)


def get_vanilla_model_patcher(m: ModelPatcher) -> ModelPatcher:
    model = ModelPatcher(m.model, m.load_device, m.offload_device, m.size, m.current_device, weight_inplace_update=m.weight_inplace_update)
    model.patches = {}
    for k in m.patches:
        model.patches[k] = m.patches[k][:]

    model.object_patches = m.object_patches.copy()
    model.model_options = copy.deepcopy(m.model_options)
    model.model_keys = m.model_keys
    return model

# adapted from https://github.com/guoyww/AnimateDiff/blob/main/animatediff/utils/convert_lora_safetensor_to_diffusers.py
# Example LoRA keys:
#   down_blocks.0.motion_modules.0.temporal_transformer.transformer_blocks.0.attention_blocks.0.processor.to_q_lora.down.weight
#   down_blocks.0.motion_modules.0.temporal_transformer.transformer_blocks.0.attention_blocks.0.processor.to_q_lora.up.weight
#
# Example model keys: 
#   down_blocks.0.motion_modules.0.temporal_transformer.transformer_blocks.0.attention_blocks.0.to_q.weight
#
def load_motion_lora_as_patches(motion_model: MotionModelPatcher, lora: MotionLoraInfo) -> None:
    def get_version(has_midblock: bool):
        return "v2" if has_midblock else "v1"

    lora_path = get_motion_lora_path(lora.name)
    logger.info(f"Loading motion LoRA {lora.name}")
    state_dict = quasar.utils.load_torch_file(lora_path)

    # remove all non-temporal keys (in case model has extra stuff in it)
    for key in list(state_dict.keys()):
        if "temporal" not in key:
            del state_dict[key]
    if len(state_dict) == 0:
        raise ValueError(f"'{lora.name}' contains no temporal keys; it is not a valid motion LoRA!")

    model_has_midblock = motion_model.model.mid_block != None
    lora_has_midblock = has_mid_block(state_dict)
    logger.info(f"Applying a {get_version(lora_has_midblock)} LoRA ({lora.name}) to a { motion_model.model.mm_info.mm_version} motion model.")

    patches = {}
    # convert lora state dict to one that matches motion_module keys and tensors
    for key in state_dict:
        # if motion_module doesn't have a midblock, skip mid_block entries
        if not model_has_midblock:
            if "mid_block" in key: continue
        # only process lora down key (we will process up at the same time as down)
        if "up." in key: continue

        # get up key version of down key
        up_key = key.replace(".down.", ".up.")

        # adapt key to match motion_module key format - remove 'processor.', '_lora', 'down.', and 'up.'
        model_key = key.replace("processor.", "").replace("_lora", "").replace("down.", "").replace("up.", "")

        # motion_module keys have a '0.' after all 'to_out.' weight keys
        if "to_out.0." not in model_key:
            model_key = model_key.replace("to_out.", "to_out.0.")
        
        weight_down = state_dict[key]
        weight_up = state_dict[up_key]
        # actual weights obtained by matrix multiplication of up and down weights
        # save as a tuple, so that (Motion)ModelPatcher's calculate_weight function detects len==1, applying it correctly
        patches[model_key] = (torch.mm(
            quasar.model_management.cast_to_device(weight_up, weight_up.device, torch.float32),
            quasar.model_management.cast_to_device(weight_down, weight_down.device, torch.float32)
            ),)
    del state_dict
    # add patches to motion ModelPatcher
    motion_model.add_patches(patches=patches, strength_patch=lora.strength)


def load_motion_module_gen1(model_name: str, model: ModelPatcher, motion_lora: MotionLoraList = None, motion_model_settings: AnimateDiffSettings = None) -> MotionModelPatcher:
    model_path = get_motion_model_path(model_name)
    logger.info(f"Loading motion module {model_name}")
    mm_state_dict = quasar.utils.load_torch_file(model_path, safe_load=True)
    # TODO: check for empty state dict?
    # get normalized state_dict and motion model info
    mm_state_dict, mm_info = normalize_ad_state_dict(mm_state_dict=mm_state_dict, mm_name=model_name)
    # check that motion model is compatible with sd model
    model_sd_type = get_sd_model_type(model)
    if model_sd_type != mm_info.sd_type:
        raise MotionCompatibilityError(f"Motion module '{mm_info.mm_name}' is intended for {mm_info.sd_type} models, " \
                                       + f"but the provided model is type {model_sd_type}.")
    # apply motion model settings
    mm_state_dict = apply_mm_settings(model_dict=mm_state_dict, mm_settings=motion_model_settings)
    # initialize AnimateDiffModelWrapper
    ad_wrapper = AnimateDiffModel(mm_state_dict=mm_state_dict, mm_info=mm_info)
    ad_wrapper.to(model.model_dtype())
    ad_wrapper.to(model.offload_device)
    is_animatelcm = mm_info.mm_format==AnimateDiffFormat.ANIMATELCM
    load_result = ad_wrapper.load_state_dict(mm_state_dict, strict=not is_animatelcm)
    # TODO: report load_result of motion_module loading?
    # wrap motion_module into a ModelPatcher, to allow motion lora patches
    motion_model = MotionModelPatcher(model=ad_wrapper, load_device=model.load_device, offload_device=model.offload_device)
    # load motion_lora, if present
    if motion_lora is not None:
        for lora in motion_lora.loras:
            load_motion_lora_as_patches(motion_model, lora)
    return motion_model


def load_motion_module_gen2(model_name: str, motion_model_settings: AnimateDiffSettings = None) -> MotionModelPatcher:
    model_path = get_motion_model_path(model_name)
    logger.info(f"Loading motion module {model_name} via Gen2")
    mm_state_dict = quasar.utils.load_torch_file(model_path, safe_load=True)
    # TODO: check for empty state dict?
    # get normalized state_dict and motion model info (converts alternate AD models like HotshotXL into AD keys)
    mm_state_dict, mm_info = normalize_ad_state_dict(mm_state_dict=mm_state_dict, mm_name=model_name)
    # apply motion model settings
    mm_state_dict = apply_mm_settings(model_dict=mm_state_dict, mm_settings=motion_model_settings)
    # initialize AnimateDiffModelWrapper
    ad_wrapper = AnimateDiffModel(mm_state_dict=mm_state_dict, mm_info=mm_info)
    ad_wrapper.to(quasar.model_management.unet_dtype())
    ad_wrapper.to(quasar.model_management.unet_offload_device())
    is_animatelcm = mm_info.mm_format==AnimateDiffFormat.ANIMATELCM
    load_result = ad_wrapper.load_state_dict(mm_state_dict, strict=not is_animatelcm)
    # TODO: manually check load_results for AnimateLCM models
    if is_animatelcm:
        pass
    # TODO: report load_result of motion_module loading?
    # wrap motion_module into a ModelPatcher, to allow motion lora patches
    motion_model = MotionModelPatcher(model=ad_wrapper, load_device=quasar.model_management.get_torch_device(),
                                      offload_device=quasar.model_management.unet_offload_device())
    return motion_model


def create_fresh_motion_module(motion_model: MotionModelPatcher) -> MotionModelPatcher:
    ad_wrapper = AnimateDiffModel(mm_state_dict=motion_model.model.state_dict(), mm_info=motion_model.model.mm_info)
    ad_wrapper.to(quasar.model_management.unet_dtype())
    ad_wrapper.to(quasar.model_management.unet_offload_device())
    ad_wrapper.load_state_dict(motion_model.model.state_dict())
    return MotionModelPatcher(model=ad_wrapper, load_device=quasar.model_management.get_torch_device(),
                                      offload_device=quasar.model_management.unet_offload_device())


def create_fresh_encoder_only_model(motion_model: MotionModelPatcher) -> MotionModelPatcher:
    ad_wrapper = EncoderOnlyAnimateDiffModel(mm_state_dict=motion_model.model.state_dict(), mm_info=motion_model.model.mm_info)
    ad_wrapper.to(quasar.model_management.unet_dtype())
    ad_wrapper.to(quasar.model_management.unet_offload_device())
    ad_wrapper.load_state_dict(motion_model.model.state_dict(), strict=False)
    return MotionModelPatcher(model=ad_wrapper, load_device=quasar.model_management.get_torch_device(),
                                      offload_device=quasar.model_management.unet_offload_device()) 


def inject_img_encoder_into_model(motion_model: MotionModelPatcher, w_encoder: MotionModelPatcher):
    motion_model.model.init_img_encoder()
    motion_model.model.img_encoder.to(quasar.model_management.unet_dtype())
    motion_model.model.img_encoder.to(quasar.model_management.unet_offload_device())
    motion_model.model.img_encoder.load_state_dict(w_encoder.model.img_encoder.state_dict())


def validate_model_compatibility_gen2(model: ModelPatcher, motion_model: MotionModelPatcher):
    # check that motion model is compatible with sd model
    model_sd_type = get_sd_model_type(model)
    mm_info = motion_model.model.mm_info
    if model_sd_type != mm_info.sd_type:
        raise MotionCompatibilityError(f"Motion module '{mm_info.mm_name}' is intended for {mm_info.sd_type} models, " \
                                       + f"but the provided model is type {model_sd_type}.")


def interpolate_pe_to_length(model_dict: dict[str, Tensor], key: str, new_length: int):
    pe_shape = model_dict[key].shape
    temp_pe = rearrange(model_dict[key], "(t b) f d -> t b f d", t=1)
    temp_pe = F.interpolate(temp_pe, size=(new_length, pe_shape[-1]), mode="bilinear")
    temp_pe = rearrange(temp_pe, "t b f d -> (t b) f d", t=1)
    model_dict[key] = temp_pe
    del temp_pe


def interpolate_pe_to_length_diffs(model_dict: dict[str, Tensor], key: str, new_length: int):
    # TODO: fill out and try out
    pe_shape = model_dict[key].shape
    temp_pe = rearrange(model_dict[key], "(t b) f d -> t b f d", t=1)
    temp_pe = F.interpolate(temp_pe, size=(new_length, pe_shape[-1]), mode="bilinear")
    temp_pe = rearrange(temp_pe, "t b f d -> (t b) f d", t=1)
    model_dict[key] = temp_pe
    del temp_pe


def interpolate_pe_to_length_pingpong(model_dict: dict[str, Tensor], key: str, new_length: int):
    if model_dict[key].shape[1] < new_length:
        temp_pe = model_dict[key]
        flipped_temp_pe = torch.flip(temp_pe[:, 1:-1, :], [1])
        use_flipped = True
        preview_pe = None
        while model_dict[key].shape[1] < new_length:
            preview_pe = model_dict[key]
            model_dict[key] = torch.cat([model_dict[key], flipped_temp_pe if use_flipped else temp_pe], dim=1)
            use_flipped = not use_flipped
        del temp_pe
        del flipped_temp_pe
        del preview_pe
    model_dict[key] = model_dict[key][:, :new_length]


def freeze_mask_of_pe(model_dict: dict[str, Tensor], key: str):
    pe_portion = model_dict[key].shape[2] // 64
    first_pe = model_dict[key][:,:1,:]
    model_dict[key][:,:,pe_portion:] = first_pe[:,:,pe_portion:]
    del first_pe


def freeze_mask_of_attn(model_dict: dict[str, Tensor], key: str):
    attn_portion = model_dict[key].shape[0] // 2
    model_dict[key][:attn_portion,:attn_portion] *= 1.5


def apply_mm_settings(model_dict: dict[str, Tensor], mm_settings: AnimateDiffSettings) -> dict[str, Tensor]:
    if mm_settings is None:
        return model_dict
    if not mm_settings.has_anything_to_apply():
        return model_dict
    # first, handle PE Adjustments
    for adjust_pe in mm_settings.adjust_pe.adjusts:
        adjust_pe: AdjustPE
        if adjust_pe.has_anything_to_apply():
            already_printed = False
            for key in model_dict:
                if "attention_blocks" in key and "pos_encoder" in key:
                    # apply simple motion pe stretch, if needed
                    if adjust_pe.has_motion_pe_stretch():
                        original_length = model_dict[key].shape[1]
                        new_pe_length = original_length + adjust_pe.motion_pe_stretch
                        interpolate_pe_to_length(model_dict, key, new_length=new_pe_length)
                        if adjust_pe.print_adjustment and not already_printed:
                            logger.info(f"[Adjust PE]: PE Stretch from {original_length} to {new_pe_length}.")
                    # apply pe_idx_offset, if needed
                    if adjust_pe.has_initial_pe_idx_offset():
                        original_length = model_dict[key].shape[1]
                        model_dict[key] = model_dict[key][:, adjust_pe.initial_pe_idx_offset:]
                        if adjust_pe.print_adjustment and not already_printed:
                            logger.info(f"[Adjust PE]: Offsetting PEs by {adjust_pe.initial_pe_idx_offset}; PE length to shortens from {original_length} to {model_dict[key].shape[1]}.")
                    # apply has_cap_initial_pe_length, if needed
                    if adjust_pe.has_cap_initial_pe_length():
                        original_length = model_dict[key].shape[1]
                        model_dict[key] = model_dict[key][:, :adjust_pe.cap_initial_pe_length]
                        if adjust_pe.print_adjustment and not already_printed:
                            logger.info(f"[Adjust PE]: Capping PEs (initial) from {original_length} to {model_dict[key].shape[1]}.")
                    # apply interpolate_pe_to_length, if needed
                    if adjust_pe.has_interpolate_pe_to_length():
                        original_length = model_dict[key].shape[1]
                        interpolate_pe_to_length(model_dict, key, new_length=adjust_pe.interpolate_pe_to_length)
                        if adjust_pe.print_adjustment and not already_printed:
                            logger.info(f"[Adjust PE]: Interpolating PE length from {original_length} to {model_dict[key].shape[1]}.")
                    # apply final_pe_idx_offset, if needed
                    if adjust_pe.has_final_pe_idx_offset():
                        original_length = model_dict[key].shape[1]
                        model_dict[key] = model_dict[key][:, adjust_pe.final_pe_idx_offset:]
                        if adjust_pe.print_adjustment and not already_printed:
                            logger.info(f"[Adjust PE]: Capping PEs (final) from {original_length} to {model_dict[key].shape[1]}.")
                    already_printed = True
    # finally, handle Weight Adjustments
    for adjust_w in mm_settings.adjust_weight.adjusts:
        adjust_w: AdjustWeight
        if adjust_w.has_anything_to_apply():
            adjust_w.mark_attrs_as_unprinted()
            for key in model_dict:
                # apply global weight adjustments, if needed
                adjust_w.perform_applicable_ops(attr=AdjustWeight.ATTR_ALL, model_dict=model_dict, key=key)
                if "attention_blocks" in key:
                    # apply pe change, if needed
                    if "pos_encoder" in key:
                        adjust_w.perform_applicable_ops(attr=AdjustWeight.ATTR_PE, model_dict=model_dict, key=key)
                    else:
                        # apply attn change, if needed
                        adjust_w.perform_applicable_ops(attr=AdjustWeight.ATTR_ATTN, model_dict=model_dict, key=key)
                        # apply specific attn changes, if needed
                        # apply attn_q change, if needed
                        if "to_q" in key:
                            adjust_w.perform_applicable_ops(attr=AdjustWeight.ATTR_ATTN_Q, model_dict=model_dict, key=key)
                        # apply attn_q change, if needed
                        elif "to_k" in key:
                            adjust_w.perform_applicable_ops(attr=AdjustWeight.ATTR_ATTN_K, model_dict=model_dict, key=key)
                        # apply attn_q change, if needed
                        elif "to_v" in key:
                            adjust_w.perform_applicable_ops(attr=AdjustWeight.ATTR_ATTN_V, model_dict=model_dict, key=key)
                        # apply to_out changes, if needed
                        elif "to_out" in key:
                            if key.strip().endswith("weight"):
                                adjust_w.perform_applicable_ops(attr=AdjustWeight.ATTR_ATTN_OUT_WEIGHT, model_dict=model_dict, key=key)
                            elif key.strip().endswith("bias"):
                                adjust_w.perform_applicable_ops(attr=AdjustWeight.ATTR_ATTN_OUT_BIAS, model_dict=model_dict, key=key)
                else:
                    adjust_w.perform_applicable_ops(attr=AdjustWeight.ATTR_OTHER, model_dict=model_dict, key=key)
    return model_dict


class InjectionParams:
    def __init__(self, unlimited_area_hack: bool=False, apply_mm_groupnorm_hack: bool=True, model_name: str="",
                 apply_v2_properly: bool=True) -> None:
        self.full_length = None
        self.unlimited_area_hack = unlimited_area_hack
        self.apply_mm_groupnorm_hack = apply_mm_groupnorm_hack
        self.model_name = model_name
        self.apply_v2_properly = apply_v2_properly
        self.context_options: ContextOptionsGroup = ContextOptionsGroup.default()
        self.motion_model_settings = AnimateDiffSettings() # Gen1
        self.sub_idxs = None  # value should NOT be included in clone, so it will auto reset
    
    def set_noise_extra_args(self, noise_extra_args: dict):
        noise_extra_args["context_options"] = self.context_options.clone()

    def set_context(self, context_options: ContextOptionsGroup):
        self.context_options = context_options.clone() if context_options else ContextOptionsGroup.default()
    
    def is_using_sliding_context(self) -> bool:
        return self.context_options.context_length is not None

    def set_motion_model_settings(self, motion_model_settings: AnimateDiffSettings): # Gen1
        if motion_model_settings is None:
            self.motion_model_settings = AnimateDiffSettings()
        else:
            self.motion_model_settings = motion_model_settings

    def reset_context(self):
        self.context_options = ContextOptionsGroup.default()
    
    def clone(self) -> 'InjectionParams':
        new_params = InjectionParams(
            self.unlimited_area_hack, self.apply_mm_groupnorm_hack,
            self.model_name, apply_v2_properly=self.apply_v2_properly,
            )
        new_params.full_length = self.full_length
        new_params.set_context(self.context_options)
        new_params.set_motion_model_settings(self.motion_model_settings) # Gen1
        return new_params
