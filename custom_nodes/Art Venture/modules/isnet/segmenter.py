import os
import torch
import torch.nn.functional as F
import numpy as np
from torch import nn
from torch.autograd import Variable
from torchvision import transforms
from torchvision.transforms.functional import normalize
from PIL import Image

import folder_paths
import quasar.model_management as model_management
import quasar.utils

from ..model_utils import download_model
from ..utils import pil2tensor, tensor2pil


isnet = None
gpu = model_management.get_torch_device()
cpu = torch.device("cpu")
model_dir = os.path.join(folder_paths.models_dir, "isnet")
model_url = "https://huggingface.co/NimaBoscarino/IS-Net_DIS-general-use/resolve/main/isnet-general-use.pth"
cache_size = [1024, 1024]


class GOSNormalize(object):
    def __init__(self, mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]):
        self.mean = mean
        self.std = std

    def __call__(self, image):
        image = normalize(image, self.mean, self.std)
        return image


transform = transforms.Compose([GOSNormalize([0.5, 0.5, 0.5], [1.0, 1.0, 1.0])])


def load_isnet_model(device_mode):
    global isnet
    if isnet is None:
        files = download_model(
            model_path=model_dir,
            model_url=model_url,
            ext_filter=[".pth"],
            download_name="isnet-general-use.pth",
        )

        from .models import ISNetDIS

        isnet = ISNetDIS()

        # convert to half precision
        isnet.is_fp16 = model_management.should_use_fp16()
        if isnet.is_fp16:
            isnet.half()
            for layer in isnet.modules():
                if isinstance(layer, nn.BatchNorm2d):
                    layer.float()

        state_dict = quasar.utils.load_torch_file(files[0])
        isnet.load_state_dict(state_dict)
        isnet.eval()

    if device_mode != "CPU":
        isnet = isnet.to(gpu)
    else:
        isnet = isnet.to(cpu)

    return isnet


def unload_isnet(device_mode):
    global isnet
    if isnet is not None and device_mode == "AUTO":
        isnet = isnet.to(cpu)

    model_management.soft_empty_cache()


def im_preprocess(im: torch.Tensor, size):
    im = im.clone()

    if len(im.shape) < 3:
        im = im.unsqueeze(2)
    if im.shape[2] == 1:
        im = im.repeat(1, 1, 3)

    im_tensor = torch.transpose(torch.transpose(im, 1, 2), 0, 1)
    if len(size) < 2:
        return im_tensor, im.shape[0:2]
    else:
        im_tensor = torch.unsqueeze(im_tensor, 0)
        im_tensor = F.upsample(im_tensor, size, mode="bilinear")
        im_tensor = torch.squeeze(im_tensor, 0)

    return transform(im_tensor).unsqueeze(0), im.shape[0:2]


def predict(model, image: torch.Tensor, orig_size, device):
    if model.is_fp16:
        image = image.type(torch.HalfTensor)
    else:
        image = image.type(torch.FloatTensor)

    image_v = Variable(image, requires_grad=False).to(device)
    ds_val = model(image_v)[0]  # list of 6 results

    # B x 1 x H x W    # we want the first one which is the most accurate prediction
    pred_val = ds_val[0][0, :, :, :]

    # recover the prediction spatial size to the orignal image size
    pred_val = torch.squeeze(F.upsample(torch.unsqueeze(pred_val, 0), (orig_size[0], orig_size[1]), mode="bilinear"))

    ma = torch.max(pred_val)
    mi = torch.min(pred_val)
    pred_val = (pred_val - mi) / (ma - mi)  # max = 1

    # it is the mask we need
    return (pred_val.detach().cpu().numpy() * 255).astype(np.uint8)


class ISNetSegment:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "images": ("IMAGE",),
                "threshold": ("FLOAT", {"default": 0.5, "min": 0, "max": 1, "step": 0.001}),
            },
            "optional": {"device_mode": (["AUTO", "Prefer GPU", "CPU"],), "enabled": ("BOOLEAN", {"default": True})},
        }

    RETURN_TYPES = ("IMAGE", "MASK")
    RETURN_NAMES = ("segmented", "mask")
    CATEGORY = "Art Venture/Utils"
    FUNCTION = "segment_isnet"

    def segment_isnet(self, images: torch.Tensor, threshold, device_mode="AUTO", enabled=True):
        if not enabled:
            masks = torch.zeros((len(images), 64, 64), dtype=torch.float32)
            return (images, masks)

        model = load_isnet_model(device_mode)
        device = gpu if device_mode != "CPU" else cpu

        try:
            segments = []
            masks = []
            for image in images:
                im, im_orig_size = im_preprocess(image, cache_size)
                mask = predict(model, im, im_orig_size, device)
                mask = mask / 255.0
                mask = np.clip(mask > threshold, 0, 1).astype(np.float32)
                mask = torch.from_numpy(mask).float()
                masks.append(mask)

                mask = tensor2pil(mask).convert("L")
                cropped = tensor2pil(image).convert("RGB")
                cropped.putalpha(mask)
                segments.append(pil2tensor(cropped))

            return (torch.cat(segments, dim=0), torch.stack(masks))
        finally:
            unload_isnet(device_mode)
