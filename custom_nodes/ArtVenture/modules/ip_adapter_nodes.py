import os
import json
import torch
import torchvision.transforms as TT
from typing import Dict, Tuple, List
from pydantic import BaseModel

import folder_paths
import quasar.clip_vision
import quasar.controlnet
import quasar.utils
import quasar.model_management

from .utils import load_module, pil2tensor
from .utility_nodes import load_images_from_url

custom_nodes = folder_paths.get_folder_paths("custom_nodes")
ip_adapter_dir_names = ["IPAdapter", "QuasarUI_IPAdapter_plus"]

NODE_CLASS_MAPPINGS = {}
NODE_DISPLAY_NAME_MAPPINGS = {}

try:
    module_path = None

    for custom_node in custom_nodes:
        custom_node = custom_node if not os.path.islink(custom_node) else os.readlink(custom_node)
        for module_dir in ip_adapter_dir_names:
            if module_dir in os.listdir(custom_node):
                module_path = os.path.abspath(os.path.join(custom_node, module_dir))
                break

    if module_path is None:
        raise Exception("Could not find IPAdapter nodes")

    module = load_module(module_path)
    print("Loaded IPAdapter nodes from", module_path)

    nodes: Dict = getattr(module, "NODE_CLASS_MAPPINGS")
    IPAdapterApply = nodes.get("IPAdapterApply")
    IPAdapterApplyEncoded = nodes.get("IPAdapterApplyEncoded")
    IPAdapterModelLoader = nodes.get("IPAdapterModelLoader")

    # from IPAdapter_Plus
    def image_add_noise(image: torch.Tensor, noise: float):
        image = image.permute([0, 3, 1, 2])
        torch.manual_seed(0)  # use a fixed random for reproducible results
        transforms = TT.Compose(
            [
                TT.CenterCrop(min(image.shape[2], image.shape[3])),
                TT.Resize((224, 224), interpolation=TT.InterpolationMode.BICUBIC, antialias=True),
                TT.ElasticTransform(alpha=75.0, sigma=noise * 3.5),  # shuffle the image
                TT.RandomVerticalFlip(p=1.0),  # flip the image to change the geometry even more
                TT.RandomHorizontalFlip(p=1.0),
            ]
        )
        image = transforms(image.cpu())
        image = image.permute([0, 2, 3, 1])
        image = image + ((0.25 * (1 - noise) + 0.05) * torch.randn_like(image))  # add further random noise
        return image

    def zeroed_hidden_states(clip_vision, batch_size):
        image = torch.zeros([batch_size, 224, 224, 3])
        quasar.model_management.load_model_gpu(clip_vision.patcher)
        pixel_values = quasar.clip_vision.clip_preprocess(image.to(clip_vision.load_device)).float()
        outputs = clip_vision.model(pixel_values=pixel_values, intermediate_output=-2)
        # we only need the penultimate hidden states
        outputs = outputs[1].to(quasar.model_management.intermediate_device())
        return outputs

    class AV_IPAdapter(IPAdapterModelLoader, IPAdapterApply):
        @classmethod
        def INPUT_TYPES(cls):
            return {
                "required": {
                    "ip_adapter_name": (["None"] + folder_paths.get_filename_list("ipadapter"),),
                    "clip_name": (["None"] + folder_paths.get_filename_list("clip_vision"),),
                    "model": ("MODEL",),
                    "image": ("IMAGE",),
                    "weight": ("FLOAT", {"default": 1.0, "min": -1, "max": 3, "step": 0.05}),
                    "noise": ("FLOAT", {"default": 0.0, "min": 0.0, "max": 1.0, "step": 0.01}),
                },
                "optional": {
                    "ip_adapter_opt": ("IPADAPTER",),
                    "clip_vision_opt": ("CLIP_VISION",),
                    "start_at": ("FLOAT", {"default": 0.0, "min": 0.0, "max": 1.0, "step": 0.001}),
                    "end_at": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 1.0, "step": 0.001}),
                    "enabled": ("BOOLEAN", {"default": True}),
                },
            }

        RETURN_TYPES = ("MODEL", "IPADAPTER", "CLIP_VISION")
        CATEGORY = "Art Venture/IP Adapter"
        FUNCTION = "apply_ip_adapter"

        def apply_ip_adapter(
            self,
            ip_adapter_name,
            clip_name,
            model,
            image,
            weight,
            noise,
            ip_adapter_opt=None,
            clip_vision_opt=None,
            enabled=True,
            **kwargs,
        ):
            if not enabled:
                return (model, None, None)

            if ip_adapter_opt:
                ip_adapter = ip_adapter_opt
            else:
                assert ip_adapter_name != "None", "IP Adapter name must be specified"
                ip_adapter = super().load_ipadapter_model(ip_adapter_name)[0]

            if clip_vision_opt:
                clip_vision = clip_vision_opt
            else:
                assert clip_name != "None", "Clip vision name must be specified"
                clip_path = folder_paths.get_full_path("clip_vision", clip_name)
                clip_vision = quasar.clip_vision.load(clip_path)

            res: Tuple = super().apply_ipadapter(
                ip_adapter, model, weight, clip_vision=clip_vision, image=image, noise=noise, **kwargs
            )
            res += (ip_adapter, clip_vision)

            return res

    class IPAdapterImage(BaseModel):
        url: str
        weight: float

    class IPAdapterData(BaseModel):
        images: List[IPAdapterImage]

    class AV_IPAdapterEncodeFromJson:
        @classmethod
        def INPUT_TYPES(cls):
            return {
                "required": {
                    "clip_name": (["None"] + folder_paths.get_filename_list("clip_vision"),),
                    "ipadapter_plus": ("BOOLEAN", {"default": False}),
                    "noise": ("FLOAT", {"default": 0.0, "min": 0.0, "max": 1.0, "step": 0.01}),
                    "data": (
                        "STRING",
                        {
                            "placeholder": '[{"url": "http://domain/path/image.png", "weight": 1}]',
                            "multiline": True,
                            "dynamicPrompts": False,
                        },
                    ),
                },
                "optional": {
                    "clip_vision_opt": ("CLIP_VISION",),
                },
            }

        RETURN_TYPES = ("EMBEDS", "IMAGE", "CLIP_VISION", "BOOLEAN")
        RETURN_NAMES = ("embeds", "image", "clip_vision", "has_data")
        CATEGORY = "Art Venture/IP Adapter"
        FUNCTION = "encode"

        def encode(self, clip_name: str, ipadapter_plus: bool, noise: float, data: str, clip_vision_opt=None):
            data = json.loads(data or "[]")
            data: IPAdapterData = IPAdapterData(images=data)  # validate

            if len(data.images) == 0:
                images = torch.zeros((1, 64, 64, 3))
                return (None, images, None, False)

            urls = [image.url for image in data.images]
            pils, _ = load_images_from_url(urls)

            images = []
            weights = []

            for i, pil in enumerate(pils):
                weight = data.images[i].weight
                weight *= 0.1 + (weight - 0.1)
                weight = 1.19e-05 if weight <= 1.19e-05 else weight

                image = pil2tensor(pil)
                if i > 0 and image.shape[1:] != images[0].shape[1:]:
                    image = quasar.utils.common_upscale(
                        image.movedim(-1, 1), images[0].shape[2], images[0].shape[1], "bilinear", "center"
                    ).movedim(1, -1)

                images.append(image)
                weights.append(weight)

            if clip_vision_opt:
                clip_vision = clip_vision_opt
            else:
                assert clip_name != "None", "Clip vision name must be specified"
                clip_path = folder_paths.get_full_path("clip_vision", clip_name)
                clip_vision = quasar.clip_vision.load(clip_path)

            images = torch.cat(images)
            clip_embed = clip_vision.encode_image(images)
            neg_image = image_add_noise(images, noise) if noise > 0 else None

            if ipadapter_plus:
                clip_embed = clip_embed.penultimate_hidden_states
                if noise > 0:
                    clip_embed_zeroed = clip_vision.encode_image(neg_image).penultimate_hidden_states
                else:
                    clip_embed_zeroed = zeroed_hidden_states(clip_vision, images.shape[0])
            else:
                clip_embed = clip_embed.image_embeds
                if noise > 0:
                    clip_embed_zeroed = clip_vision.encode_image(neg_image).image_embeds
                else:
                    clip_embed_zeroed = torch.zeros_like(clip_embed)

            if any(e != 1.0 for e in weights):
                weights = (
                    torch.tensor(weights).unsqueeze(-1)
                    if not ipadapter_plus
                    else torch.tensor(weights).unsqueeze(-1).unsqueeze(-1)
                )
                clip_embed = clip_embed * weights

            embeds = torch.stack((clip_embed, clip_embed_zeroed))

            return (embeds, images, clip_vision, True)

    class AV_IPAdapterApplyEncoded(IPAdapterModelLoader, IPAdapterApplyEncoded):
        @classmethod
        def INPUT_TYPES(cls):
            return {
                "required": {
                    "ip_adapter_name": (["None"] + folder_paths.get_filename_list("ipadapter"),),
                    "embeds": ("EMBEDS",),
                    "model": ("MODEL",),
                    "weight": ("FLOAT", {"default": 1.0, "min": -1, "max": 3, "step": 0.05}),
                    "weight_type": (["original", "linear", "channel penalty"],),
                },
                "optional": {
                    "ip_adapter_opt": ("IPADAPTER",),
                    "attn_mask": ("MASK",),
                    "start_at": ("FLOAT", {"default": 0.0, "min": 0.0, "max": 1.0, "step": 0.001}),
                    "end_at": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 1.0, "step": 0.001}),
                    "enabled": ("BOOLEAN", {"default": True}),
                },
            }

        RETURN_TYPES = ("MODEL", "IPADAPTER")
        CATEGORY = "Art Venture/IP Adapter"
        FUNCTION = "apply_ip_adapter"

        def apply_ip_adapter(self, ip_adapter_name, model, ip_adapter_opt=None, enabled=True, **kwargs):
            if not enabled:
                return (model, None)

            if ip_adapter_opt:
                ip_adapter = ip_adapter_opt
            else:
                assert ip_adapter_name != "None", "IP Adapter name must be specified"
                ip_adapter = super().load_ipadapter_model(ip_adapter_name)[0]

            res: Tuple = super().apply_ipadapter(ip_adapter, model, **kwargs)
            res += (ip_adapter,)

            return res

    NODE_CLASS_MAPPINGS.update(
        {
            "AV_IPAdapter": AV_IPAdapter,
            "AV_IPAdapterEncodeFromJson": AV_IPAdapterEncodeFromJson,
            "AV_IPAdapterApplyEncoded": AV_IPAdapterApplyEncoded,
        }
    )
    NODE_DISPLAY_NAME_MAPPINGS.update(
        {
            "AV_IPAdapter": "IP Adapter Apply",
            "AV_IPAdapterEncodeFromJson": "IP Adapter Encoder",
            "AV_IPAdapterApplyEncoded": "IP Adapter Apply Encoded",
        }
    )

except Exception as e:
    print(e)
