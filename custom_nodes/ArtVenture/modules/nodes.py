import os
import io
import json
import torch
from typing import Dict

from PIL import Image
from PIL.PngImagePlugin import PngInfo
import numpy as np

import folder_paths
import quasar.sd
from nodes import LoraLoader, VAELoader
from quasar_extras.nodes_model_merging import CheckpointSave

from .logger import logger

from .utility_nodes import (
    NODE_CLASS_MAPPINGS as UTIL_NODE_CLASS_MAPPINGS,
    NODE_DISPLAY_NAME_MAPPINGS as UTIL_NODE_DISPLAY_NAME_MAPPINGS,
)
from .sdxl_prompt_styler import (
    NODE_CLASS_MAPPINGS as SDXL_STYLER_NODE_CLASS_MAPPINGS,
    NODE_DISPLAY_NAME_MAPPINGS as SDXL_STYLER_NODE_DISPLAY_NAME_MAPPINGS,
)
from .interrogate import (
    NODE_CLASS_MAPPINGS as INTERROGATE_NODE_CLASS_MAPPINGS,
    NODE_DISPLAY_NAME_MAPPINGS as INTERROGATE_NODE_DISPLAY_NAME_MAPPINGS,
)
from .fooocus import (
    NODE_CLASS_MAPPINGS as FOOOCUS_NODE_CLASS_MAPPINGS,
    NODE_DISPLAY_NAME_MAPPINGS as FOOOCUS_NODE_DISPLAY_NAME_MAPPINGS,
)
from .postprocessing import (
    NODE_CLASS_MAPPINGS as PP_NODE_CLASS_MAPPINGS,
    NODE_DISPLAY_NAME_MAPPINGS as PP_NODE_DISPLAY_NAME_MAPPINGS,
)
from .controlnet import (
    NODE_CLASS_MAPPINGS as CONTROLNET_NODE_CLASS_MAPPINGS,
    NODE_DISPLAY_NAME_MAPPINGS as CONTROLNET_NODE_DISPLAY_NAME_MAPPINGS,
)
from .animatediff import (
    NODE_CLASS_MAPPINGS as ANIMATEDIFF_NODE_CLASS_MAPPINGS,
    NODE_DISPLAY_NAME_MAPPINGS as ANIMATEDIFF_NODE_DISPLAY_NAME_MAPPINGS,
)
from .ip_adapter_nodes import (
    NODE_CLASS_MAPPINGS as IP_ADAPTER_NODE_CLASS_MAPPINGS,
    NODE_DISPLAY_NAME_MAPPINGS as IP_ADAPTER_NODE_DISPLAY_NAME_MAPPINGS,
)
from .isnet import (
    NODE_CLASS_MAPPINGS as ISNET_NODE_CLASS_MAPPINGS,
    NODE_DISPLAY_NAME_MAPPINGS as ISNET_NODE_DISPLAY_NAME_MAPPINGS,
)
from .inpaint import (
    NODE_CLASS_MAPPINGS as INPAINT_NODE_CLASS_MAPPINGS,
    NODE_DISPLAY_NAME_MAPPINGS as INPAINT_NODE_DISPLAY_NAME_MAPPINGS,
)
from .video import (
    NODE_CLASS_MAPPINGS as VIDEO_NODE_CLASS_MAPPINGS,
    NODE_DISPLAY_NAME_MAPPINGS as VIDEO_NODE_DISPLAY_NAME_MAPPINGS,
)

from .model_utils import load_file_from_url

lora_cloud_front_url = "https://cdn.artventure.ai"


class AVVAELoader(VAELoader):
    @classmethod
    def INPUT_TYPES(s):
        inputs = VAELoader.INPUT_TYPES()
        inputs["optional"] = {"vae_override": ("STRING", {"default": "None"})}
        return inputs

    CATEGORY = "Art Venture/Loaders"

    def load_vae(self, vae_name, vae_override="None"):
        if vae_override != "None":
            if vae_override not in folder_paths.get_filename_list("vae"):
                print(f"Warning: Not found VAE model {vae_override}. Use {vae_name} instead.")
            else:
                vae_name = vae_override

        return super().load_vae(vae_name)


class AVLoraLoader(LoraLoader):
    @classmethod
    def INPUT_TYPES(s):
        inputs = LoraLoader.INPUT_TYPES()
        inputs["optional"] = {
            "lora_override": ("STRING", {"default": "None"}),
            "enabled": ("BOOLEAN", {"default": True}),
        }
        return inputs

    CATEGORY = "Art Venture/Loaders"

    def load_lora(self, model, clip, lora_name, *args, lora_override="None", enabled=True, **kwargs):
        if not enabled:
            return (model, clip)

        if lora_override != "None":
            if lora_override not in folder_paths.get_filename_list("loras"):
                print(f"Warning: Not found Lora model {lora_override}. Use {lora_name} instead.")
            else:
                lora_name = lora_override

        return super().load_lora(model, clip, lora_name, *args, **kwargs)


class AVLoraListStacker:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "data": ("STRING", {"default": "", "multiline": True, "dynamicPrompts": False}),
            },
            "optional": {"base_url": ("STRING", {"default": lora_cloud_front_url}), "lora_stack": ("LORA_STACK",)},
        }

    RETURN_TYPES = ("LORA_STACK",)
    FUNCTION = "load_list_lora"
    CATEGORY = "Art Venture/Loaders"

    def parse_lora_list(self, data: str, base_url: str):
        # data is a list of lora model (lora_name, strength_model, strength_clip, url) in json format
        # trim data
        data = data.strip()
        if data == "" or data == "[]" or data is None:
            return []

        print(f"Loading lora list: {data}")

        lora_list = json.loads(data)
        if len(lora_list) == 0:
            return []

        available_loras = folder_paths.get_filename_list("loras")
        model_path = os.path.join(folder_paths.models_dir, "loras")

        lora_params = []
        for lora in lora_list:
            lora_name = lora["name"]
            strength_model = lora["strength"]
            strength_clip = lora["strength"]
            lora_url = lora.get("url", None)

            if strength_model == 0 and strength_clip == 0:
                continue

            if lora_name not in available_loras:
                lora_url = lora_url or f"{base_url}/models/loras/{lora_name}"
                load_file_from_url(lora_url, model_dir=model_path, file_name=lora_name)

            lora_params.append((lora_name, strength_model, strength_clip))

        return lora_params

    def load_list_lora(self, data, base_url=lora_cloud_front_url, lora_stack=None):
        loras = self.parse_lora_list(data, base_url=base_url)

        if lora_stack is not None:
            loras.extend([l for l in lora_stack if l[0] != "None"])

        return (loras,)


class AVLoraListLoader(AVLoraListStacker):
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "model": ("MODEL",),
                "clip": ("CLIP",),
                "data": ("STRING", {"default": "", "multiline": True, "dynamicPrompts": False}),
            },
            "optional": {"base_url": ("STRING", {"default": lora_cloud_front_url})},
        }

    RETURN_TYPES = ("MODEL", "CLIP")

    def load_list_lora(self, model, clip, data, base_url=lora_cloud_front_url):
        lora_params = self.parse_lora_list(data, base_url=base_url)

        if len(lora_params) == 0:
            return (model, clip)

        def recursive_load_lora(lora_params, model, clip, id, folder_paths):
            if len(lora_params) == 0:
                return model, clip

            lora_name, strength_model, strength_clip = lora_params[0]

            lora_path = folder_paths.get_full_path("loras", lora_name)
            lora_model, lora_clip = quasar.sd.load_lora_for_models(
                model, clip, quasar.utils.load_torch_file(lora_path), strength_model, strength_clip
            )

            # Call the function again with the new lora_model and lora_clip and the remaining tuples
            return recursive_load_lora(lora_params[1:], lora_model, lora_clip, id, folder_paths)

        lora_model, lora_clip = recursive_load_lora(lora_params, model, clip, id, folder_paths)

        return (lora_model, lora_clip)


class AVCheckpointModelsToParametersPipe:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "ckpt_name": (folder_paths.get_filename_list("checkpoints"),),
            },
            "optional": {
                "pipe": ("PIPE",),
                "secondary_ckpt_name": (["None"] + folder_paths.get_filename_list("checkpoints"),),
                "vae_name": (["None"] + folder_paths.get_filename_list("vae"),),
                "upscaler_name": (["None"] + folder_paths.get_filename_list("upscale_models"),),
                "secondary_upscaler_name": (["None"] + folder_paths.get_filename_list("upscale_models"),),
                "lora_1_name": (["None"] + folder_paths.get_filename_list("loras"),),
                "lora_2_name": (["None"] + folder_paths.get_filename_list("loras"),),
                "lora_3_name": (["None"] + folder_paths.get_filename_list("loras"),),
            },
        }

    RETURN_TYPES = ("PIPE",)
    CATEGORY = "Art Venture/Parameters"
    FUNCTION = "checkpoint_models_to_parameter_pipe"

    def checkpoint_models_to_parameter_pipe(
        self,
        ckpt_name,
        pipe: Dict = {},
        secondary_ckpt_name="None",
        vae_name="None",
        upscaler_name="None",
        secondary_upscaler_name="None",
        lora_1_name="None",
        lora_2_name="None",
        lora_3_name="None",
    ):
        pipe["ckpt_name"] = ckpt_name if ckpt_name != "None" else None
        pipe["secondary_ckpt_name"] = secondary_ckpt_name if secondary_ckpt_name != "None" else None
        pipe["vae_name"] = vae_name if vae_name != "None" else None
        pipe["upscaler_name"] = upscaler_name if upscaler_name != "None" else None
        pipe["secondary_upscaler_name"] = secondary_upscaler_name if secondary_upscaler_name != "None" else None
        pipe["lora_1_name"] = lora_1_name if lora_1_name != "None" else None
        pipe["lora_2_name"] = lora_2_name if lora_2_name != "None" else None
        pipe["lora_3_name"] = lora_3_name if lora_3_name != "None" else None
        return (pipe,)


class AVPromptsToParametersPipe:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "positive": ("STRING", {"multiline": True, "default": "Positive"}),
                "negative": ("STRING", {"multiline": True, "default": "Negative"}),
            },
            "optional": {
                "pipe": ("PIPE",),
                "image": ("IMAGE",),
                "mask": ("MASK",),
            },
        }

    RETURN_TYPES = ("PIPE",)
    CATEGORY = "Art Venture/Parameters"
    FUNCTION = "prompt_to_parameter_pipe"

    def prompt_to_parameter_pipe(self, positive, negative, pipe: Dict = {}, image=None, mask=None):
        pipe["positive"] = positive
        pipe["negative"] = negative
        pipe["image"] = image
        pipe["mask"] = mask
        return (pipe,)


class AVParametersPipeToCheckpointModels:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "pipe": ("PIPE",),
            },
        }

    RETURN_TYPES = (
        "PIPE",
        "CHECKPOINT_NAME",
        "CHECKPOINT_NAME",
        "VAE_NAME",
        "UPSCALER_NAME",
        "UPSCALER_NAME",
        "LORA_NAME",
        "LORA_NAME",
        "LORA_NAME",
    )
    RETURN_NAMES = (
        "pipe",
        "ckpt_name",
        "secondary_ckpt_name",
        "vae_name",
        "upscaler_name",
        "secondary_upscaler_name",
        "lora_1_name",
        "lora_2_name",
        "lora_3_name",
    )
    CATEGORY = "Art Venture/Parameters"
    FUNCTION = "parameter_pipe_to_checkpoint_models"

    def parameter_pipe_to_checkpoint_models(self, pipe: Dict = {}):
        ckpt_name = pipe.get("ckpt_name", None)
        secondary_ckpt_name = pipe.get("secondary_ckpt_name", None)
        vae_name = pipe.get("vae_name", None)
        upscaler_name = pipe.get("upscaler_name", None)
        secondary_upscaler_name = pipe.get("secondary_upscaler_name", None)
        lora_1_name = pipe.get("lora_1_name", None)
        lora_2_name = pipe.get("lora_2_name", None)
        lora_3_name = pipe.get("lora_3_name", None)

        return (
            pipe,
            ckpt_name,
            secondary_ckpt_name,
            vae_name,
            upscaler_name,
            secondary_upscaler_name,
            lora_1_name,
            lora_2_name,
            lora_3_name,
        )


class AVParametersPipeToPrompts:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "pipe": ("PIPE",),
            },
        }

    RETURN_TYPES = (
        "PIPE",
        "STRING",
        "STRING",
        "IMAGE",
        "MASK",
    )
    RETURN_NAMES = (
        "pipe",
        "positive",
        "negative",
        "image",
        "mask",
    )
    CATEGORY = "Art Venture/Parameters"
    FUNCTION = "parameter_pipe_to_prompt"

    def parameter_pipe_to_prompt(self, pipe: Dict = {}):
        positive = pipe.get("positive", None)
        negative = pipe.get("negative", None)
        image = pipe.get("image", None)
        mask = pipe.get("mask", None)

        return (
            pipe,
            positive,
            negative,
            image,
            mask,
        )


class AVCheckpointMerge:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "model1": ("MODEL",),
                "model2": ("MODEL",),
                "model1_weight": ("FLOAT", {"default": 1.0, "min": -1.0, "max": 1.0, "step": 0.01}),
                "model2_weight": ("FLOAT", {"default": 1.0, "min": -1.0, "max": 1.0, "step": 0.01}),
            }
        }

    RETURN_TYPES = ("MODEL",)
    FUNCTION = "merge"

    CATEGORY = "Art Venture/Model Merging"

    def merge(self, model1, model2, model1_weight, model2_weight):
        m = model1.clone()
        k1 = model1.get_key_patches("diffusion_model.")
        k2 = model2.get_key_patches("diffusion_model.")
        for k in k1:
            if k in k2:
                a = k1[k][0]
                b = k2[k][0]

                if a.shape != b.shape and a.shape[0:1] + a.shape[2:] == b.shape[0:1] + b.shape[2:]:
                    if a.shape[1] == 4 and b.shape[1] == 9:
                        raise RuntimeError(
                            "When merging inpainting model with a normal one, model1 must be the inpainting model."
                        )
                    if a.shape[1] == 4 and b.shape[1] == 8:
                        raise RuntimeError(
                            "When merging instruct-pix2pix model with a normal one, model1 must be the instruct-pix2pix model."
                        )

                    c = torch.zeros_like(a)
                    c[:, 0:4, :, :] = b
                    b = c

                m.add_patches({k: (b,)}, model2_weight, model1_weight)
            else:
                logger.warn(f"Key {k} not found in model2")
                m.add_patches({k: k1[k]}, -1.0, 1.0)  # zero out

        return (m,)


class AVCheckpointSave(CheckpointSave):
    CATEGORY = "Art Venture/Model Merging"

    @classmethod
    def INPUT_TYPES(s):
        inputs = CheckpointSave.INPUT_TYPES()
        inputs["optional"] = {
            "dtype": (["float16", "float32"], {"default": "float16"}),
        }

        return inputs

    def save(self, *args, dtype="float16", **kwargs):
        quasar_save_checkpoint = quasar.sd.save_checkpoint

        if dtype == "float16":

            def save_checkpoint(output_path, model, clip, vae, metadata=None):
                model.model.half()
                return quasar_save_checkpoint(output_path, model, clip, vae, metadata)

            quasar.sd.save_checkpoint = save_checkpoint

        try:
            return super().save(*args, **kwargs)
        finally:
            quasar.sd.save_checkpoint = quasar_save_checkpoint


NODE_CLASS_MAPPINGS = {
    "AV_CheckpointModelsToParametersPipe": AVCheckpointModelsToParametersPipe,
    "AV_PromptsToParametersPipe": AVPromptsToParametersPipe,
    "AV_ParametersPipeToCheckpointModels": AVParametersPipeToCheckpointModels,
    "AV_ParametersPipeToPrompts": AVParametersPipeToPrompts,
    "AV_VAELoader": AVVAELoader,
    "AV_LoraLoader": AVLoraLoader,
    "AV_LoraListLoader": AVLoraListLoader,
    "AV_LoraListStacker": AVLoraListStacker,
    "AV_CheckpointMerge": AVCheckpointMerge,
    "AV_CheckpointSave": AVCheckpointSave,
}
NODE_DISPLAY_NAME_MAPPINGS = {
    "AV_CheckpointModelsToParametersPipe": "Checkpoint Models to Pipe",
    "AV_PromptsToParametersPipe": "Prompts to Pipe",
    "AV_ParametersPipeToCheckpointModels": "Pipe to Checkpoint Models",
    "AV_ParametersPipeToPrompts": "Pipe to Prompts",
    "AV_VAELoader": "VAE Loader",
    "AV_LoraLoader": "Lora Loader",
    "AV_LoraListLoader": "Lora List Loader",
    "AV_LoraListStacker": "Lora List Stacker",
    "AV_CheckpointMerge": "Checkpoint Merge",
    "AV_CheckpointSave": "Checkpoint Save",
}


NODE_CLASS_MAPPINGS.update(UTIL_NODE_CLASS_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(UTIL_NODE_DISPLAY_NAME_MAPPINGS)

NODE_CLASS_MAPPINGS.update(SDXL_STYLER_NODE_CLASS_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(SDXL_STYLER_NODE_DISPLAY_NAME_MAPPINGS)

NODE_CLASS_MAPPINGS.update(INTERROGATE_NODE_CLASS_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(INTERROGATE_NODE_DISPLAY_NAME_MAPPINGS)

NODE_CLASS_MAPPINGS.update(FOOOCUS_NODE_CLASS_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(FOOOCUS_NODE_DISPLAY_NAME_MAPPINGS)

NODE_CLASS_MAPPINGS.update(PP_NODE_CLASS_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(PP_NODE_DISPLAY_NAME_MAPPINGS)

NODE_CLASS_MAPPINGS.update(CONTROLNET_NODE_CLASS_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(CONTROLNET_NODE_DISPLAY_NAME_MAPPINGS)

NODE_CLASS_MAPPINGS.update(ANIMATEDIFF_NODE_CLASS_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(ANIMATEDIFF_NODE_DISPLAY_NAME_MAPPINGS)

NODE_CLASS_MAPPINGS.update(IP_ADAPTER_NODE_CLASS_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(IP_ADAPTER_NODE_DISPLAY_NAME_MAPPINGS)

NODE_CLASS_MAPPINGS.update(ISNET_NODE_CLASS_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(ISNET_NODE_DISPLAY_NAME_MAPPINGS)

NODE_CLASS_MAPPINGS.update(INPAINT_NODE_CLASS_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(INPAINT_NODE_DISPLAY_NAME_MAPPINGS)

NODE_CLASS_MAPPINGS.update(VIDEO_NODE_CLASS_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(VIDEO_NODE_DISPLAY_NAME_MAPPINGS)
