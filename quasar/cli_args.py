import argparse
import enum
import quasar.options
class TThmoUAXlrSuGJKbRtTwrhvihcAqADzp(argparse.Action):
    def __init__(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, **kwargs):
        ljnptQvQTcjCRoKUsgERGUPmIIPsOuKZ = kwargs.pop("type", None)
        if ljnptQvQTcjCRoKUsgERGUPmIIPsOuKZ is None:
            raise ValueError("type must be assigned an Enum when using EnumAction")
        if not issubclass(ljnptQvQTcjCRoKUsgERGUPmIIPsOuKZ, enum.Enum):
            raise TypeError("type must be an Enum when using EnumAction")
        tmujDLxgYaCDFcisPjJrwuVqCDvwpMHt = tuple(dgvKdkEDrMSdkCaRxfkDNVbaXWUetgtO.value for dgvKdkEDrMSdkCaRxfkDNVbaXWUetgtO in ljnptQvQTcjCRoKUsgERGUPmIIPsOuKZ)
        kwargs.setdefault("choices", tmujDLxgYaCDFcisPjJrwuVqCDvwpMHt)
        kwargs.setdefault("metavar", f"[{','.join(list(tmujDLxgYaCDFcisPjJrwuVqCDvwpMHt))}]")
        super(TThmoUAXlrSuGJKbRtTwrhvihcAqADzp, rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS).__init__(**kwargs)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS._enum = ljnptQvQTcjCRoKUsgERGUPmIIPsOuKZ
    def __call__(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, igCtajZqjJempyRtCXGEtbeTNbPBhKtk, namespace, values, option_string=None):
        value = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS._enum(values)
        setattr(namespace, rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.dest, value)
igCtajZqjJempyRtCXGEtbeTNbPBhKtk = argparse.ArgumentParser()
igCtajZqjJempyRtCXGEtbeTNbPBhKtk.add_argument("--listen", type=str, default="127.0.0.1", metavar="IP", nargs="?", const="0.0.0.0", help="Specify the IP address to listen on (default: 127.0.0.1). If --listen is provided without an argument, it defaults to 0.0.0.0. (listens on all)")
igCtajZqjJempyRtCXGEtbeTNbPBhKtk.add_argument("--port", type=int, default=8188, help="Set the listen port.")
igCtajZqjJempyRtCXGEtbeTNbPBhKtk.add_argument("--enable-cors-header", type=str, default=None, metavar="ORIGIN", nargs="?", const="*", help="Enable CORS (Cross-Origin Resource Sharing) with optional origin or allow all with default '*'.")
igCtajZqjJempyRtCXGEtbeTNbPBhKtk.add_argument("--extra-model-paths-config", type=str, default=None, metavar="PATH", nargs='+', action='append', help="Load one or more extra_model_paths.yaml files.")
igCtajZqjJempyRtCXGEtbeTNbPBhKtk.add_argument("--output-directory", type=str, default=None, help="Set the QuasarUI output directory.")
igCtajZqjJempyRtCXGEtbeTNbPBhKtk.add_argument("--temp-directory", type=str, default=None, help="Set the QuasarUI temp directory (default is in the QuasarUI directory).")
igCtajZqjJempyRtCXGEtbeTNbPBhKtk.add_argument("--auto-launch", action="store_true", help="Automatically launch QuasarUI in the default browser.")
igCtajZqjJempyRtCXGEtbeTNbPBhKtk.add_argument("--disable-auto-launch", action="store_true", help="Disable auto launching the browser.")
igCtajZqjJempyRtCXGEtbeTNbPBhKtk.add_argument("--cuda-device", type=int, default=None, metavar="DEVICE_ID", help="Set the id of the cuda device this instance will use.")
EGhDDjhJsCMHQJIcLIsYHmaiZFJPPFoc = igCtajZqjJempyRtCXGEtbeTNbPBhKtk.add_mutually_exclusive_group()
EGhDDjhJsCMHQJIcLIsYHmaiZFJPPFoc.add_argument("--cuda-malloc", action="store_true", help="Enable cudaMallocAsync (enabled by default for torch 2.0 and up).")
EGhDDjhJsCMHQJIcLIsYHmaiZFJPPFoc.add_argument("--disable-cuda-malloc", action="store_true", help="Disable cudaMallocAsync.")
igCtajZqjJempyRtCXGEtbeTNbPBhKtk.add_argument("--dont-upcast-attention", action="store_true", help="Disable upcasting of attention. Can boost speed but increase the chances of black images.")
cTTdkyAOSlCSMZZvycSuswPqGDmVUGOs = igCtajZqjJempyRtCXGEtbeTNbPBhKtk.add_mutually_exclusive_group()
cTTdkyAOSlCSMZZvycSuswPqGDmVUGOs.add_argument("--force-fp32", action="store_true", help="Force fp32 (If this makes your GPU work better please report it).")
cTTdkyAOSlCSMZZvycSuswPqGDmVUGOs.add_argument("--force-fp16", action="store_true", help="Force fp16.")
cBlpKEpxYUBSDEGQAFHZEznpGpNYIlhg = igCtajZqjJempyRtCXGEtbeTNbPBhKtk.add_mutually_exclusive_group()
cBlpKEpxYUBSDEGQAFHZEznpGpNYIlhg.add_argument("--fp16-vae", action="store_true", help="Run the VAE in fp16, might cause black images.")
cBlpKEpxYUBSDEGQAFHZEznpGpNYIlhg.add_argument("--fp32-vae", action="store_true", help="Run the VAE in full precision fp32.")
cBlpKEpxYUBSDEGQAFHZEznpGpNYIlhg.add_argument("--bf16-vae", action="store_true", help="Run the VAE in bf16.")
igCtajZqjJempyRtCXGEtbeTNbPBhKtk.add_argument("--directml", type=int, nargs="?", metavar="DIRECTML_DEVICE", const=-1, help="Use torch-directml.")
igCtajZqjJempyRtCXGEtbeTNbPBhKtk.add_argument("--disable-ipex-optimize", action="store_true", help="Disables ipex.optimize when loading models with Intel GPUs.")
class ySfrcxMpeHyRDGXqWhEgkCOiWqyynQSR(enum.Enum):
    OnCKbmhTlJDZXLhZJCnKrONVSVqAexhw = "none"
    gGqBvGsqLMhGxhhibPMtLUoFnsICxLOm = "auto"
    ckUOIVYknbJNjaizvaRkdiudkcoNGhss = "latent2rgb"
    CFXvAYULVpQFvvdJNHbevhEXAaaPZtnO = "taesd"
igCtajZqjJempyRtCXGEtbeTNbPBhKtk.add_argument("--preview-method", type=ySfrcxMpeHyRDGXqWhEgkCOiWqyynQSR, default=ySfrcxMpeHyRDGXqWhEgkCOiWqyynQSR.OnCKbmhTlJDZXLhZJCnKrONVSVqAexhw, help="Default preview method for sampler nodes.", action=TThmoUAXlrSuGJKbRtTwrhvihcAqADzp)
foFcmhoKSYCznluNanJTWzrZFCOsjxqI = igCtajZqjJempyRtCXGEtbeTNbPBhKtk.add_mutually_exclusive_group()
foFcmhoKSYCznluNanJTWzrZFCOsjxqI.add_argument("--use-split-cross-attention", action="store_true", help="Use the split cross attention optimization. Ignored when xformers is used.")
foFcmhoKSYCznluNanJTWzrZFCOsjxqI.add_argument("--use-quad-cross-attention", action="store_true", help="Use the sub-quadratic cross attention optimization . Ignored when xformers is used.")
foFcmhoKSYCznluNanJTWzrZFCOsjxqI.add_argument("--use-pytorch-cross-attention", action="store_true", help="Use the new pytorch 2.0 cross attention function.")
igCtajZqjJempyRtCXGEtbeTNbPBhKtk.add_argument("--disable-xformers", action="store_true", help="Disable xformers.")
NVWLOsvJRjTdkYXQqGyobNAHrwnSAPzp = igCtajZqjJempyRtCXGEtbeTNbPBhKtk.add_mutually_exclusive_group()
NVWLOsvJRjTdkYXQqGyobNAHrwnSAPzp.add_argument("--gpu-only", action="store_true", help="Store and run everything (text encoders/CLIP models, etc... on the GPU).")
NVWLOsvJRjTdkYXQqGyobNAHrwnSAPzp.add_argument("--highvram", action="store_true", help="By default models will be unloaded to CPU memory after being used. This option keeps them in GPU memory.")
NVWLOsvJRjTdkYXQqGyobNAHrwnSAPzp.add_argument("--normalvram", action="store_true", help="Used to force normal vram use if lowvram gets automatically enabled.")
NVWLOsvJRjTdkYXQqGyobNAHrwnSAPzp.add_argument("--lowvram", action="store_true", help="Split the unet in parts to use less vram.")
NVWLOsvJRjTdkYXQqGyobNAHrwnSAPzp.add_argument("--novram", action="store_true", help="When lowvram isn'XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz enough.")
NVWLOsvJRjTdkYXQqGyobNAHrwnSAPzp.add_argument("--cpu", action="store_true", help="To use the CPU for everything (slow).")
igCtajZqjJempyRtCXGEtbeTNbPBhKtk.add_argument("--disable-smart-memory", action="store_true", help="Force QuasarUI to agressively offload to regular ram instead of keeping models in vram when it can.")
igCtajZqjJempyRtCXGEtbeTNbPBhKtk.add_argument("--dont-print-server", action="store_true", help="Don'XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz print REDIKAYZymAzMirxFmomyJtEGktwcqlE pwTxzdNTJGMWEFORftJTEtPYMMiKwDuP.")
igCtajZqjJempyRtCXGEtbeTNbPBhKtk.add_argument("--quick-test-for-ci", action="store_true", help="Quick test for CI.")
igCtajZqjJempyRtCXGEtbeTNbPBhKtk.add_argument("--windows-standalone-build", action="store_true", help="Windows standalone build: Enable convenient things that most people using the standalone windows build will probably enjoy (like auto opening the page on startup).")
igCtajZqjJempyRtCXGEtbeTNbPBhKtk.add_argument("--disable-metadata", action="store_true", help="Disable saving prompt metadata in files.")
if quasar.options.eOxNNTvHPWJLMAndNXyDYEInLePDkdvs:
    DukiculvUpjhZIVvaGinshRSKLSTgVVl = igCtajZqjJempyRtCXGEtbeTNbPBhKtk.parse_args()
else:
    DukiculvUpjhZIVvaGinshRSKLSTgVVl = igCtajZqjJempyRtCXGEtbeTNbPBhKtk.parse_args([])
if DukiculvUpjhZIVvaGinshRSKLSTgVVl.windows_standalone_build:
    DukiculvUpjhZIVvaGinshRSKLSTgVVl.auto_launch = True
if DukiculvUpjhZIVvaGinshRSKLSTgVVl.disable_auto_launch:
    DukiculvUpjhZIVvaGinshRSKLSTgVVl.auto_launch = False
