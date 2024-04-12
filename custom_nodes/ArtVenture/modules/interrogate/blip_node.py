import os

import torch
from torchvision import transforms
from torchvision.transforms.functional import InterpolationMode

import folder_paths
from quasar.model_management import text_encoder_device, text_encoder_offload_device, soft_empty_cache

from ..model_utils import download_model
from ..utils import tensor2pil

blips = {}
blip_size = 384
gpu = text_encoder_device()
cpu = text_encoder_offload_device()
model_url = (
    "https://storage.googleapis.com/sfr-vision-language-research/BLIP/models/model_base_caption_capfilt_large.pth"
)
model_dir = os.path.join(folder_paths.models_dir, "blip")

folder_paths.folder_names_and_paths["blip"] = (
    [model_dir],
    folder_paths.supported_pt_extensions,
)


def packages(versions=False):
    import subprocess
    import sys

    return [
        (r.decode().split("==")[0] if not versions else r.decode())
        for r in subprocess.check_output([sys.executable, "-m", "pip", "freeze"]).split()
    ]


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


def load_blip(model_name):
    if model_name not in blips:
        blip_path = folder_paths.get_full_path("blip", model_name)

        from .models.blip import blip_decoder

        current_dir = os.path.dirname(os.path.realpath(__file__))
        med_config = os.path.join(current_dir, "configs", "med_config.json")
        blip = blip_decoder(
            pretrained=blip_path,
            image_size=blip_size,
            vit="base",
            med_config=med_config,
        )
        blip.eval()
        blips[model_name] = blip

    return blips[model_name]


def unload_blip():
    global blips
    if blips is not None and blips.is_auto_mode:
        blips = blips.to(cpu)

    soft_empty_cache()


def join_caption(caption, prefix, suffix):
    if prefix:
        caption = prefix + ", " + caption
    if suffix:
        caption = caption + ", " + suffix
    return caption


def blip_caption(model, image, min_length, max_length):
    image = tensor2pil(image)

    if "transformers==4.26.1" in packages(True):
        print("Using Legacy `transformImaage()`")
        tensor = transformImage_legacy(image)
    else:
        tensor = transformImage(image)

    with torch.no_grad():
        caption = model.generate(
            tensor,
            sample=False,
            num_beams=1,
            min_length=min_length,
            max_length=max_length,
        )
        return caption[0]


class BlipLoader:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "model_name": (folder_paths.get_filename_list("blip"),),
            },
        }

    RETURN_TYPES = ("BLIP_MODEL",)
    FUNCTION = "load_blip"
    CATEGORY = "Art Venture/Captioning"

    def load_blip(self, model_name):
        model = load_blip(model_name)
        return (model,)


class BlipCaption:
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
                "blip_model": ("BLIP_MODEL",),
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("caption",)
    OUTPUT_IS_LIST = (True,)
    FUNCTION = "blip_caption"
    CATEGORY = "Art Venture/Captioning"

    def blip_caption(
        self, image, min_length, max_length, device_mode="AUTO", prefix="", suffix="", enabled=True, blip_model=None
    ):
        if not enabled:
            return (join_caption("", prefix, suffix),)

        if blip_model is None:
            ckpts = folder_paths.get_filename_list("blip")
            if len(ckpts) == 0:
                ckpts = download_model(
                    model_path=model_dir,
                    model_url=model_url,
                    ext_filter=[".pth"],
                    download_name="model_base_caption_capfilt_large.pth",
                )
            blip_model = load_blip(ckpts[0])

        device = gpu if device_mode != "CPU" else cpu
        blip_model = blip_model.to(device)

        try:
            captions = []

            with torch.no_grad():
                for img in image:
                    img = tensor2pil(img)
                    tensor = transformImage(img)
                    caption = blip_model.generate(
                        tensor,
                        sample=False,
                        num_beams=1,
                        min_length=min_length,
                        max_length=max_length,
                    )

                    caption = join_caption(caption[0], prefix, suffix)
                    captions.append(caption)

            return (captions,)
        except:
            raise
        finally:
            if device_mode == "AUTO":
                blip_model = blip_model.to(cpu)
