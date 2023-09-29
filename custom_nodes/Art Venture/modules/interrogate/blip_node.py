import os

import torch
from torchvision import transforms
from torchvision.transforms.functional import InterpolationMode

import folder_paths
from quasar.model_management import text_encoder_device, text_encoder_offload_device, soft_empty_cache

from ..model_utils import download_model
from ..utils import is_junction, tensor2pil

blip = None
blip_size = 384
gpu = text_encoder_device()
cpu = text_encoder_offload_device()
BLIP_MODEL_URL = (
    "https://storage.googleapis.com/sfr-vision-language-research/BLIP/models/model_base_caption_capfilt_large.pth"
)


def packages(versions=False):
    import subprocess
    import sys

    return [
        (r.decode().split("==")[0] if not versions else r.decode())
        for r in subprocess.check_output([sys.executable, "-m", "pip", "freeze"]).split()
    ]


def transformImage_legacy(input_image):
    raw_image = input_image.convert("RGB")
    raw_image = raw_image.resize((blip_size, blip_size))
    transform = transforms.Compose(
        [
            transforms.Resize(raw_image.size, interpolation=InterpolationMode.BICUBIC),
            transforms.ToTensor(),
            transforms.Normalize(
                (0.48145466, 0.4578275, 0.40821073),
                (0.26862954, 0.26130258, 0.27577711),
            ),
        ]
    )
    image = transform(raw_image).unsqueeze(0).to(gpu)
    return image


def transformImage(input_image):
    raw_image = input_image.convert("RGB")
    raw_image = raw_image.resize((blip_size, blip_size))
    transform = transforms.Compose(
        [
            transforms.Resize(raw_image.size, interpolation=InterpolationMode.BICUBIC),
            transforms.ToTensor(),
            transforms.Normalize(
                (0.48145466, 0.4578275, 0.40821073),
                (0.26862954, 0.26130258, 0.27577711),
            ),
        ]
    )
    image = transform(raw_image).unsqueeze(0).to(gpu)
    return image.view(1, -1, blip_size, blip_size)  # Change the shape of the output tensor


def load_blip(device_mode):
    global blip
    if blip is None:
        blip_dir = os.path.join(folder_paths.models_dir, "blip")
        if not os.path.exists(blip_dir) and not is_junction(blip_dir):
            os.makedirs(blip_dir, exist_ok=True)

        files = download_model(
            model_path=blip_dir,
            model_url=BLIP_MODEL_URL,
            ext_filter=[".pth"],
            download_name="model_base_caption_capfilt_large.pth",
        )

        from .models.blip import blip_decoder

        current_dir = os.path.dirname(os.path.realpath(__file__))
        med_config = os.path.join(current_dir, "configs", "med_config.json")
        blip = blip_decoder(
            pretrained=files[0],
            image_size=blip_size,
            vit="base",
            med_config=med_config,
        )
        blip.eval()

    if device_mode != "CPU":
        blip = blip.to(gpu)

    blip.is_auto_mode = device_mode == "AUTO"

    return blip


def unload_blip():
    global blip
    if blip is not None and blip.is_auto_mode:
        blip = blip.to(cpu)

    soft_empty_cache()


def join_caption(caption, prefix, suffix):
    if prefix:
        caption = prefix + ", " + caption
    if suffix:
        caption = caption + ", " + suffix
    return caption


class BlipCaption:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "image": ("IMAGE",),
                "min_length": (
                    "INT",
                    {
                        "default": 24,
                        "min": 0,  # minimum value
                        "max": 200,  # maximum value
                        "step": 1,  # slider's step
                    },
                ),
                "max_length": (
                    "INT",
                    {
                        "default": 48,
                        "min": 0,  # minimum value
                        "max": 200,  # maximum value
                        "step": 1,  # slider's step
                    },
                ),
            },
            "optional": {
                "device_mode": (["AUTO", "Prefer GPU", "CPU"],),
                "prefix": ("STRING", {"default": ""}),
                "suffix": ("STRING", {"default": ""}),
                "enabled": ("BOOLEAN", {"default": True}),
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("caption",)

    FUNCTION = "blip_caption"

    CATEGORY = "Art Venture/Utils"

    def blip_caption(self, image, min_length, max_length, device_mode="AUTO", prefix="", suffix="", enabled=True):
        if not enabled:
            return (join_caption("", prefix, suffix),)

        model = load_blip(device_mode)
        image = tensor2pil(image)

        if "transformers==4.26.1" in packages(True):
            print("Using Legacy `transformImaage()`")
            tensor = transformImage_legacy(image)
        else:
            tensor = transformImage(image)

        try:
            with torch.no_grad():
                caption = model.generate(
                    tensor,
                    sample=False,
                    num_beams=1,
                    min_length=min_length,
                    max_length=max_length,
                )
            return (join_caption(caption[0], prefix, suffix),)
        except:
            raise
        finally:
            unload_blip()
