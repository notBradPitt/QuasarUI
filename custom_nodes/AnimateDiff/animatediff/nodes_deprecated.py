import json
import os
import shutil
import subprocess
from typing import Dict, List

import numpy as np
import torch
from PIL import Image
from PIL.PngImagePlugin import PngInfo

import folder_paths
from quasar.model_patcher import ModelPatcher

from .ad_settings import AnimateDiffSettings, AdjustGroup, AdjustPE, AdjustWeight
from .context import ContextOptionsGroup, ContextOptions, ContextSchedules
from .logger import logger
from .utils_model import Folders, BetaSchedules, get_available_motion_models
from .model_injection import ModelPatcherAndInjector, InjectionParams, MotionModelGroup, load_motion_module_gen1


class AnimateDiffLoader_Deprecated:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "model": ("MODEL",),
                "latents": ("LATENT",),
                "model_name": (get_available_motion_models(),),
                "unlimited_area_hack": ("BOOLEAN", {"default": False},),
                "beta_schedule": (BetaSchedules.get_alias_list_with_first_element(BetaSchedules.SQRT_LINEAR),),
            },
        }

    RETURN_TYPES = ("MODEL", "LATENT")
    CATEGORY = ""
    FUNCTION = "load_mm_and_inject_params"

    def load_mm_and_inject_params(
        self,
        model: ModelPatcher,
        latents: Dict[str, torch.Tensor],
        model_name: str, unlimited_area_hack: bool, beta_schedule: str,
    ):
        # load motion module
        motion_model = load_motion_module_gen1(model_name, model)
        # get total frames
        init_frames_len = len(latents["samples"])  # deprecated - no longer used for anything lol
        # set injection params
        params = InjectionParams(
                unlimited_area_hack=unlimited_area_hack,
                apply_mm_groupnorm_hack=True,
                model_name=model_name,
                apply_v2_properly=False,
        )
        # inject for use in sampling code
        model = ModelPatcherAndInjector(model)
        model.motion_models = MotionModelGroup(motion_model)
        model.motion_injection_params = params

        # save model sampling from BetaSchedule as object patch
        # if autoselect, get suggested beta_schedule from motion model
        if beta_schedule == BetaSchedules.AUTOSELECT and not model.motion_models.is_empty():
            beta_schedule = model.motion_models[0].model.get_best_beta_schedule(log=True)
        new_model_sampling = BetaSchedules.to_model_sampling(beta_schedule, model)
        if new_model_sampling is not None:
            model.add_object_patch("model_sampling", new_model_sampling)

        del motion_model
        return (model, latents)


class AnimateDiffLoaderAdvanced_Deprecated:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "model": ("MODEL",),
                "latents": ("LATENT",),
                "model_name": (get_available_motion_models(),),
                "unlimited_area_hack": ("BOOLEAN", {"default": False},),
                "context_length": ("INT", {"default": 16, "min": 0, "max": 1000}),
                "context_stride": ("INT", {"default": 1, "min": 1, "max": 1000}),
                "context_overlap": ("INT", {"default": 4, "min": 0, "max": 1000}),
                "context_schedule": (ContextSchedules.LEGACY_UNIFORM_SCHEDULE_LIST,),
                "closed_loop": ("BOOLEAN", {"default": False},),
                "beta_schedule": (BetaSchedules.get_alias_list_with_first_element(BetaSchedules.SQRT_LINEAR),),
            },
        }

    RETURN_TYPES = ("MODEL", "LATENT")
    CATEGORY = ""
    FUNCTION = "load_mm_and_inject_params"

    def load_mm_and_inject_params(self,
            model: ModelPatcher,
            latents: Dict[str, torch.Tensor],
            model_name: str, unlimited_area_hack: bool,
            context_length: int, context_stride: int, context_overlap: int, context_schedule: str, closed_loop: bool,
            beta_schedule: str,
        ):
        # load motion module
        motion_model = load_motion_module_gen1(model_name, model)
        # get total frames
        init_frames_len = len(latents["samples"])  # deprecated - no longer used for anything lol
        # set injection params
        params = InjectionParams(
                unlimited_area_hack=unlimited_area_hack,
                apply_mm_groupnorm_hack=True,
                model_name=model_name,
                apply_v2_properly=False,
        )
        context_group = ContextOptionsGroup()
        context_group.add(
            ContextOptions(
                context_length=context_length,
                context_stride=context_stride,
                context_overlap=context_overlap,
                context_schedule=context_schedule,
                closed_loop=closed_loop,
                )
            )
        # set context settings
        params.set_context(context_options=context_group)
        # inject for use in sampling code
        model = ModelPatcherAndInjector(model)
        model.motion_models = MotionModelGroup(motion_model)
        model.motion_injection_params = params

        # save model sampling from BetaSchedule as object patch
        # if autoselect, get suggested beta_schedule from motion model
        if beta_schedule == BetaSchedules.AUTOSELECT and not model.motion_models.is_empty():
            beta_schedule = model.motion_models[0].model.get_best_beta_schedule(log=True)
        new_model_sampling = BetaSchedules.to_model_sampling(beta_schedule, model)
        if new_model_sampling is not None:
            model.add_object_patch("model_sampling", new_model_sampling)

        del motion_model
        return (model, latents)
    

class AnimateDiffCombine_Deprecated:
    ffmpeg_warning_already_shown = False
    @classmethod
    def INPUT_TYPES(s):
        ffmpeg_path = shutil.which("ffmpeg")
        #Hide ffmpeg formats if ffmpeg isn't available
        if ffmpeg_path is not None:
            ffmpeg_formats = ["video/"+x[:-5] for x in folder_paths.get_filename_list(Folders.VIDEO_FORMATS)]
        else:
            ffmpeg_formats = []
            if not s.ffmpeg_warning_already_shown:
                # Deprecated node are now hidden, so no need to show warning unless node is used.
                # logger.warning("This warning can be ignored, you should not be using the deprecated AnimateDiff Combine node anyway. If you are, use Video Combine from QuasarUI-VideoHelperSuite instead. ffmpeg could not be found. Outputs that require it have been disabled")
                s.ffmpeg_warning_already_shown = True
        return {
            "required": {
                "images": ("IMAGE",),
                "frame_rate": (
                    "INT",
                    {"default": 8, "min": 1, "max": 24, "step": 1},
                ),
                "loop_count": ("INT", {"default": 0, "min": 0, "max": 100, "step": 1}),
                "filename_prefix": ("STRING", {"default": "AnimateDiff"}),
                "format": (["image/gif", "image/webp"] + ffmpeg_formats,),
                "pingpong": ("BOOLEAN", {"default": False}),
                "save_image": ("BOOLEAN", {"default": True}),
            },
            "hidden": {
                "prompt": "PROMPT",
                "extra_pnginfo": "EXTRA_PNGINFO",
            },
        }

    RETURN_TYPES = ("GIF",)
    OUTPUT_NODE = True
    CATEGORY = ""
    FUNCTION = "generate_gif"

    def generate_gif(
        self,
        images,
        frame_rate: int,
        loop_count: int,
        filename_prefix="AnimateDiff",
        format="image/gif",
        pingpong=False,
        save_image=True,
        prompt=None,
        extra_pnginfo=None,
    ):
        logger.warning("Do not use AnimateDiff Combine node, it is deprecated. Use Video Combine node from QuasarUI-VideoHelperSuite instead. Video nodes from VideoHelperSuite are actively maintained, more feature-rich, and also automatically attempts to get ffmpeg.")
        # convert images to numpy
        frames: List[Image.Image] = []
        for image in images:
            img = 255.0 * image.cpu().numpy()
            img = Image.fromarray(np.clip(img, 0, 255).astype(np.uint8))
            frames.append(img)
            
        # get output information
        output_dir = (
            folder_paths.get_output_directory()
            if save_image
            else folder_paths.get_temp_directory()
        )
        (
            full_output_folder,
            filename,
            counter,
            subfolder,
            _,
        ) = folder_paths.get_save_image_path(filename_prefix, output_dir)

        metadata = PngInfo()
        if prompt is not None:
            metadata.add_text("prompt", json.dumps(prompt))
        if extra_pnginfo is not None:
            for x in extra_pnginfo:
                metadata.add_text(x, json.dumps(extra_pnginfo[x]))

        # save first frame as png to keep metadata
        file = f"{filename}_{counter:05}_.png"
        file_path = os.path.join(full_output_folder, file)
        frames[0].save(
            file_path,
            pnginfo=metadata,
            compress_level=4,
        )
        if pingpong:
            frames = frames + frames[-2:0:-1]
        
        format_type, format_ext = format.split("/")
        file = f"{filename}_{counter:05}_.{format_ext}"
        file_path = os.path.join(full_output_folder, file)
        if format_type == "image":
            # Use pillow directly to save an animated image
            frames[0].save(
                file_path,
                format=format_ext.upper(),
                save_all=True,
                append_images=frames[1:],
                duration=round(1000 / frame_rate),
                loop=loop_count,
                compress_level=4,
            )
        else:
            # Use ffmpeg to save a video
            ffmpeg_path = shutil.which("ffmpeg")
            if ffmpeg_path is None:
                #Should never be reachable
                raise ProcessLookupError("Could not find ffmpeg")

            video_format_path = folder_paths.get_full_path("video_formats", format_ext + ".json")
            with open(video_format_path, 'r') as stream:
                video_format = json.load(stream)
            file = f"{filename}_{counter:05}_.{video_format['extension']}"
            file_path = os.path.join(full_output_folder, file)
            dimensions = f"{frames[0].width}x{frames[0].height}"
            args = [ffmpeg_path, "-v", "error", "-f", "rawvideo", "-pix_fmt", "rgb24",
                    "-s", dimensions, "-r", str(frame_rate), "-i", "-"] \
                    + video_format['main_pass'] + [file_path]

            env=os.environ.copy()
            if  "environment" in video_format:
                env.update(video_format["environment"])
            with subprocess.Popen(args, stdin=subprocess.PIPE, env=env) as proc:
                for frame in frames:
                    proc.stdin.write(frame.tobytes())

        previews = [
            {
                "filename": file,
                "subfolder": subfolder,
                "type": "output" if save_image else "temp",
                "format": format,
            }
        ]
        return {"ui": {"gifs": previews}}



class AnimateDiffModelSettings:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "min_motion_scale": ("FLOAT", {"default": 1.0, "min": 0.0, "step": 0.001}),
                "max_motion_scale": ("FLOAT", {"default": 1.0, "min": 0.0, "step": 0.001}),
            },
            "optional": {
                "mask_motion_scale": ("MASK",),
            }
        }
    
    RETURN_TYPES = ("AD_SETTINGS",)
    CATEGORY = ""  #"Animate Diff 🎭🅐🅓/① Gen1 nodes ①/motion settings"
    FUNCTION = "get_motion_model_settings"

    def get_motion_model_settings(self, mask_motion_scale: torch.Tensor=None, min_motion_scale: float=1.0, max_motion_scale: float=1.0):
        motion_model_settings = AnimateDiffSettings(
            mask_attn_scale=mask_motion_scale,
            mask_attn_scale_min=min_motion_scale,
            mask_attn_scale_max=max_motion_scale,
            )

        return (motion_model_settings,)


class AnimateDiffModelSettingsSimple:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "motion_pe_stretch": ("INT", {"default": 0, "min": 0, "step": 1}),
            },
            "optional": {
                "mask_motion_scale": ("MASK",),
                "min_motion_scale": ("FLOAT", {"default": 1.0, "min": 0.0, "step": 0.001}),
                "max_motion_scale": ("FLOAT", {"default": 1.0, "min": 0.0, "step": 0.001}),
            }
        }
    
    RETURN_TYPES = ("AD_SETTINGS",)
    CATEGORY = ""  #"Animate Diff 🎭🅐🅓/① Gen1 nodes ①/motion settings/experimental"
    FUNCTION = "get_motion_model_settings"

    def get_motion_model_settings(self, motion_pe_stretch: int,
                                  mask_motion_scale: torch.Tensor=None, min_motion_scale: float=1.0, max_motion_scale: float=1.0):
        adjust_pe = AdjustGroup(AdjustPE(motion_pe_stretch=motion_pe_stretch))
        motion_model_settings = AnimateDiffSettings(
            adjust_pe=adjust_pe,
            mask_attn_scale=mask_motion_scale,
            mask_attn_scale_min=min_motion_scale,
            mask_attn_scale_max=max_motion_scale,
            )

        return (motion_model_settings,)


class AnimateDiffModelSettingsAdvanced:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "pe_strength": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 10.0, "step": 0.0001}),
                "attn_strength": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 10.0, "step": 0.0001}),
                "other_strength": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 10.0, "step": 0.0001}),
                "motion_pe_stretch": ("INT", {"default": 0, "min": 0, "step": 1}),
                "cap_initial_pe_length": ("INT", {"default": 0, "min": 0, "step": 1}),
                "interpolate_pe_to_length": ("INT", {"default": 0, "min": 0, "step": 1}),
                "initial_pe_idx_offset": ("INT", {"default": 0, "min": 0, "step": 1}),
                "final_pe_idx_offset": ("INT", {"default": 0, "min": 0, "step": 1}),
            },
            "optional": {
                "mask_motion_scale": ("MASK",),
                "min_motion_scale": ("FLOAT", {"default": 1.0, "min": 0.0, "step": 0.001}),
                "max_motion_scale": ("FLOAT", {"default": 1.0, "min": 0.0, "step": 0.001}),
            }
        }
    
    RETURN_TYPES = ("AD_SETTINGS",)
    CATEGORY = ""  #"Animate Diff 🎭🅐🅓/① Gen1 nodes ①/motion settings/experimental"
    FUNCTION = "get_motion_model_settings"

    def get_motion_model_settings(self, pe_strength: float, attn_strength: float, other_strength: float,
                                  motion_pe_stretch: int,
                                  cap_initial_pe_length: int, interpolate_pe_to_length: int,
                                  initial_pe_idx_offset: int, final_pe_idx_offset: int,
                                  mask_motion_scale: torch.Tensor=None, min_motion_scale: float=1.0, max_motion_scale: float=1.0):
        adjust_pe = AdjustGroup(AdjustPE(motion_pe_stretch=motion_pe_stretch,
                             cap_initial_pe_length=cap_initial_pe_length, interpolate_pe_to_length=interpolate_pe_to_length,
                             initial_pe_idx_offset=initial_pe_idx_offset, final_pe_idx_offset=final_pe_idx_offset))
        adjust_weight = AdjustGroup(AdjustWeight(
            pe_MULT=pe_strength,
            attn_MULT=attn_strength,
            other_MULT=other_strength,
        ))
        motion_model_settings = AnimateDiffSettings(
            adjust_pe=adjust_pe,
            adjust_weight=adjust_weight,
            mask_attn_scale=mask_motion_scale,
            mask_attn_scale_min=min_motion_scale,
            mask_attn_scale_max=max_motion_scale,
        )

        return (motion_model_settings,)


class AnimateDiffModelSettingsAdvancedAttnStrengths:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "pe_strength": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 10.0, "step": 0.0001}),
                "attn_strength": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 10.0, "step": 0.0001}),
                "attn_q_strength": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 10.0, "step": 0.0001}),
                "attn_k_strength": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 10.0, "step": 0.0001}),
                "attn_v_strength": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 10.0, "step": 0.0001}),
                "attn_out_weight_strength": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 10.0, "step": 0.0001}),
                "attn_out_bias_strength": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 10.0, "step": 0.0001}),
                "other_strength": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 10.0, "step": 0.0001}),
                "motion_pe_stretch": ("INT", {"default": 0, "min": 0, "step": 1}),
                "cap_initial_pe_length": ("INT", {"default": 0, "min": 0, "step": 1}),
                "interpolate_pe_to_length": ("INT", {"default": 0, "min": 0, "step": 1}),
                "initial_pe_idx_offset": ("INT", {"default": 0, "min": 0, "step": 1}),
                "final_pe_idx_offset": ("INT", {"default": 0, "min": 0, "step": 1}),
            },
            "optional": {
                "mask_motion_scale": ("MASK",),
                "min_motion_scale": ("FLOAT", {"default": 1.0, "min": 0.0, "step": 0.001}),
                "max_motion_scale": ("FLOAT", {"default": 1.0, "min": 0.0, "step": 0.001}),
            }
        }
    
    RETURN_TYPES = ("AD_SETTINGS",)
    CATEGORY = ""  #"Animate Diff 🎭🅐🅓/① Gen1 nodes ①/motion settings/experimental"
    FUNCTION = "get_motion_model_settings"

    def get_motion_model_settings(self, pe_strength: float, attn_strength: float,
                                  attn_q_strength: float,
                                  attn_k_strength: float,
                                  attn_v_strength: float,
                                  attn_out_weight_strength: float,
                                  attn_out_bias_strength: float,
                                  other_strength: float,
                                  motion_pe_stretch: int,
                                  cap_initial_pe_length: int, interpolate_pe_to_length: int,
                                  initial_pe_idx_offset: int, final_pe_idx_offset: int,
                                  mask_motion_scale: torch.Tensor=None, min_motion_scale: float=1.0, max_motion_scale: float=1.0):
        adjust_pe = AdjustGroup(AdjustPE(motion_pe_stretch=motion_pe_stretch,
                             cap_initial_pe_length=cap_initial_pe_length, interpolate_pe_to_length=interpolate_pe_to_length,
                             initial_pe_idx_offset=initial_pe_idx_offset, final_pe_idx_offset=final_pe_idx_offset))
        adjust_weight = AdjustGroup(AdjustWeight(
            pe_MULT=pe_strength,
            attn_MULT=attn_strength,
            attn_q_MULT=attn_q_strength,
            attn_k_MULT=attn_k_strength,
            attn_v_MULT=attn_v_strength,
            attn_out_weight_MULT=attn_out_weight_strength,
            attn_out_bias_MULT=attn_out_bias_strength,
            other_MULT=other_strength,
        ))
        motion_model_settings = AnimateDiffSettings(
            adjust_pe=adjust_pe,
            adjust_weight=adjust_weight,
            mask_attn_scale=mask_motion_scale,
            mask_attn_scale_min=min_motion_scale,
            mask_attn_scale_max=max_motion_scale,
        )

        return (motion_model_settings,)

