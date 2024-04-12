import os
import sys
import time
import torch
import numpy as np
import requests
import traceback
import importlib
import subprocess
import torch.nn.functional as F
from typing import Callable
from PIL import Image

from .logger import logger


class AnyType(str):
    def __ne__(self, __value: object) -> bool:
        return False


any_type = AnyType("*")


def ensure_package(package, install_package_name=None):
    # Try to import the package
    try:
        importlib.import_module(package)
    except ImportError:
        logger.info(f"Package {package} is not installed. Installing now...")

        if "python_embeded" in sys.executable or "python_embedded" in sys.executable:
            pip_install = [sys.executable, "-s", "-m", "pip", "install"]
        else:
            pip_install = [sys.executable, "-m", "pip", "install"]

        subprocess.check_call(pip_install + [install_package_name or package])
    else:
        print(f"Package {package} is already installed.")


# modified from https://stackoverflow.com/questions/22058048/hashing-a-file-in-python
def calculate_file_hash(filename: str, hash_every_n: int = 1):
    import hashlib

    h = hashlib.sha256()
    b = bytearray(10 * 1024 * 1024)  # read 10 megabytes at a time
    mv = memoryview(b)
    with open(filename, "rb", buffering=0) as f:
        i = 0
        # don't hash entire file, only portions of it if requested
        while n := f.readinto(mv):
            if i % hash_every_n == 0:
                h.update(mv[:n])
            i += 1
    return h.hexdigest()


def get_dict_attribute(dict_inst: dict, name_string: str, default=None):
    nested_keys = name_string.split(".")
    value = dict_inst

    for key in nested_keys:
        value = value.get(key, None)

        if value is None:
            return default

    return value


def set_dict_attribute(dict_inst: dict, name_string: str, value):
    """
    Set an attribute to a dictionary using dot notation.
    If the attribute does not already exist, it will create a nested dictionary.

    Parameters:
        - dict_inst: the dictionary instance to set the attribute
        - name_string: the attribute name in dot notation (ex: 'attributes[1].name')
        - value: the value to set for the attribute

    Returns:
        None
    """
    # Split the attribute names by dot
    name_list = name_string.split(".")

    # Traverse the dictionary and create a nested dictionary if necessary
    current_dict = dict_inst
    for name in name_list[:-1]:
        is_array = name.endswith("]")
        if is_array:
            open_bracket_index = name.index("[")
            idx = int(name[open_bracket_index + 1 : -1])
            name = name[:open_bracket_index]

        if name not in current_dict:
            current_dict[name] = [] if is_array else {}

        current_dict = current_dict[name]
        if is_array:
            while len(current_dict) <= idx:
                current_dict.append({})
            current_dict = current_dict[idx]

    # Set the final attribute to its value
    name = name_list[-1]
    if name.endswith("]"):
        open_bracket_index = name.index("[")
        idx = int(name[open_bracket_index + 1 : -1])
        name = name[:open_bracket_index]

        if name not in current_dict:
            current_dict[name] = []

        while len(current_dict[name]) <= idx:
            current_dict[name].append(None)

        current_dict[name][idx] = value
    else:
        current_dict[name] = value


def is_junction(src: str) -> bool:
    import subprocess

    child = subprocess.Popen('fsutil reparsepoint query "{}"'.format(src), stdout=subprocess.PIPE)
    streamdata = child.communicate()[0]
    rc = child.returncode
    return rc == 0


def load_module(module_path, module_name=None):
    import importlib.util

    if module_name is None:
        module_name = os.path.basename(module_path)

    if os.path.isfile(module_path):
        module_spec = importlib.util.spec_from_file_location(module_name, module_path)
    else:
        module_spec = importlib.util.spec_from_file_location(module_name, os.path.join(module_path, "__init__.py"))

    module = importlib.util.module_from_spec(module_spec)
    module_spec.loader.exec_module(module)

    return module


def pil2numpy(image: Image.Image):
    return np.array(image).astype(np.float32) / 255.0


def numpy2pil(image: np.ndarray, mode=None):
    return Image.fromarray(np.clip(255.0 * image, 0, 255).astype(np.uint8), mode)


def pil2tensor(image: Image.Image):
    return torch.from_numpy(pil2numpy(image)).unsqueeze(0)


def tensor2pil(image: torch.Tensor, mode=None):
    return numpy2pil(image.cpu().numpy().squeeze(), mode=mode)


def tensor2bytes(image: torch.Tensor) -> bytes:
    return tensor2pil(image).tobytes()
