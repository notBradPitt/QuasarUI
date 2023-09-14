import psutil
from enum import Enum
from quasar.cli_args import DukiculvUpjhZIVvaGinshRSKLSTgVVl
import quasar.utils
import torch
import sys
class bsSIGhSsMwfAaUYcCeSPPMJpGwJitrWP(Enum):
    UFZDvMQkHyQtFgyaiLMMYzebzwjzKbnN = 0    
    sZuTEjYlLsSpGlAgsvokhLKtJWGXtBSt = 1     
    VVfVZDrXgnSkeTCCsEZSDrsgdvoNXCjZ = 2
    xmfoFlkMIlumPovjAHlmdldLqjMICkUt = 3
    UgFpkYwkZWeRlPVDTDYbfGJbKZebAxwU = 4
    fUORddVDjBLaHdhUZCahKFgidvhsDIPi = 5      
class ZnzMTovtbNqIZyGLmHCGwrCzxBPhBddd(Enum):
    cgDhUViYUOcOuMDteCWBWTptzTvpxlxZ = 0
    amvcnbTgIfYErScizhLPObRvsCqqoxLu = 1
    hNmmVuyKkHcBszNhVyKhRBcIvpDkVwUd = 2
XWcfUReeNuYAHgWXiaGMksnQlevFLcTW = bsSIGhSsMwfAaUYcCeSPPMJpGwJitrWP.xmfoFlkMIlumPovjAHlmdldLqjMICkUt
LJPIyadMglCGcXCbArwGhXyoJxFGdhyB = bsSIGhSsMwfAaUYcCeSPPMJpGwJitrWP.xmfoFlkMIlumPovjAHlmdldLqjMICkUt
juiVBlpYUtLrUBmtDEGztlteWPsvLbZQ = ZnzMTovtbNqIZyGLmHCGwrCzxBPhBddd.cgDhUViYUOcOuMDteCWBWTptzTvpxlxZ
veKSzIFEKTXWuBNHlaLkijsXuLHLIqID = 0
uenKiAwaCaBygEScZqNFFJcCmPIQjOxl = True
IOVuQmaDimDpoaWsackoJZhURAqJgGHp = False
ZnhsFYXiDrJhDvSRdTZbdswNjfAVNkiY = False
if DukiculvUpjhZIVvaGinshRSKLSTgVVl.directml is not None:
    import torch_directml
    ZnhsFYXiDrJhDvSRdTZbdswNjfAVNkiY = True
    rOAXCYCqopGIxRiDeWhjPHWOJKKoPMfT = DukiculvUpjhZIVvaGinshRSKLSTgVVl.directml
    if rOAXCYCqopGIxRiDeWhjPHWOJKKoPMfT < 0:
        sUHCqHCSbRpERmfmIenceBcDyeETWvqj = torch_directml.fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc()
    else:
        sUHCqHCSbRpERmfmIenceBcDyeETWvqj = torch_directml.fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc(rOAXCYCqopGIxRiDeWhjPHWOJKKoPMfT)
    print("Using directml with device:", torch_directml.LKGttefzMHbQsSCFJjKbAWGhbIpBWTal(rOAXCYCqopGIxRiDeWhjPHWOJKKoPMfT))
    uenKiAwaCaBygEScZqNFFJcCmPIQjOxl = False 
try:
    import intel_extension_for_pytorch as ipex
    if torch.xpu.is_available():
        IOVuQmaDimDpoaWsackoJZhURAqJgGHp = True
except:
    pass
try:
    if torch.backends.mps.is_available():
        juiVBlpYUtLrUBmtDEGztlteWPsvLbZQ = ZnzMTovtbNqIZyGLmHCGwrCzxBPhBddd.hNmmVuyKkHcBszNhVyKhRBcIvpDkVwUd
        import torch.mps
except:
    pass
if DukiculvUpjhZIVvaGinshRSKLSTgVVl.cpu:
    juiVBlpYUtLrUBmtDEGztlteWPsvLbZQ = ZnzMTovtbNqIZyGLmHCGwrCzxBPhBddd.amvcnbTgIfYErScizhLPObRvsCqqoxLu
def KwVMPUvXTcrLXlMbtZUohDhciWKSVHEE():
    global juiVBlpYUtLrUBmtDEGztlteWPsvLbZQ
    global IOVuQmaDimDpoaWsackoJZhURAqJgGHp
    if juiVBlpYUtLrUBmtDEGztlteWPsvLbZQ == ZnzMTovtbNqIZyGLmHCGwrCzxBPhBddd.cgDhUViYUOcOuMDteCWBWTptzTvpxlxZ:
        if IOVuQmaDimDpoaWsackoJZhURAqJgGHp:
            return True
    return False
def aIQypJefEzoiiobeXriYBEHMJwDTvZWS():
    global ZnhsFYXiDrJhDvSRdTZbdswNjfAVNkiY
    global juiVBlpYUtLrUBmtDEGztlteWPsvLbZQ
    if ZnhsFYXiDrJhDvSRdTZbdswNjfAVNkiY:
        global sUHCqHCSbRpERmfmIenceBcDyeETWvqj
        return sUHCqHCSbRpERmfmIenceBcDyeETWvqj
    if juiVBlpYUtLrUBmtDEGztlteWPsvLbZQ == ZnzMTovtbNqIZyGLmHCGwrCzxBPhBddd.hNmmVuyKkHcBszNhVyKhRBcIvpDkVwUd:
        return torch.fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc("mps")
    if juiVBlpYUtLrUBmtDEGztlteWPsvLbZQ == ZnzMTovtbNqIZyGLmHCGwrCzxBPhBddd.amvcnbTgIfYErScizhLPObRvsCqqoxLu:
        return torch.fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc("cpu")
    else:
        if KwVMPUvXTcrLXlMbtZUohDhciWKSVHEE():
            return torch.fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc("xpu")
        else:
            return torch.fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc(torch.cuda.current_device())
def vJrdZOBBaEUjLkobsDWKZVCBOAICHZyg(ZclsJeyZNkbLbpqNgnNOPEMMNHesUkIE=None, torch_total_too=False):
    global ZnhsFYXiDrJhDvSRdTZbdswNjfAVNkiY
    if ZclsJeyZNkbLbpqNgnNOPEMMNHesUkIE is None:
        ZclsJeyZNkbLbpqNgnNOPEMMNHesUkIE = aIQypJefEzoiiobeXriYBEHMJwDTvZWS()
    if hasattr(ZclsJeyZNkbLbpqNgnNOPEMMNHesUkIE, 'type') and (ZclsJeyZNkbLbpqNgnNOPEMMNHesUkIE.type == 'cpu' or ZclsJeyZNkbLbpqNgnNOPEMMNHesUkIE.type == 'mps'):
        pOnYuedIKRPotKGLeyhBElrmAyUTLfmv = psutil.virtual_memory().total
        vMpioSWBxKjOQrgisIamMlxKJVjYOaHf = pOnYuedIKRPotKGLeyhBElrmAyUTLfmv
    else:
        if ZnhsFYXiDrJhDvSRdTZbdswNjfAVNkiY:
            pOnYuedIKRPotKGLeyhBElrmAyUTLfmv = 1024 * 1024 * 1024 
            vMpioSWBxKjOQrgisIamMlxKJVjYOaHf = pOnYuedIKRPotKGLeyhBElrmAyUTLfmv
        elif KwVMPUvXTcrLXlMbtZUohDhciWKSVHEE():
            jnfIHeLvMhRAslhkREQLmMNJsXQjQGQh = torch.xpu.memory_stats(ZclsJeyZNkbLbpqNgnNOPEMMNHesUkIE)
            tclmftGFRtKnFiydynBHNEmEqcODJwxu = jnfIHeLvMhRAslhkREQLmMNJsXQjQGQh['reserved_bytes.all.current']
            pOnYuedIKRPotKGLeyhBElrmAyUTLfmv = torch.xpu.get_device_properties(ZclsJeyZNkbLbpqNgnNOPEMMNHesUkIE).total_memory
            vMpioSWBxKjOQrgisIamMlxKJVjYOaHf = tclmftGFRtKnFiydynBHNEmEqcODJwxu
        else:
            jnfIHeLvMhRAslhkREQLmMNJsXQjQGQh = torch.cuda.memory_stats(ZclsJeyZNkbLbpqNgnNOPEMMNHesUkIE)
            tclmftGFRtKnFiydynBHNEmEqcODJwxu = jnfIHeLvMhRAslhkREQLmMNJsXQjQGQh['reserved_bytes.all.current']
            _, xyODYNYecjUPUhoYbggALGqCgPeoExzF = torch.cuda.mem_get_info(ZclsJeyZNkbLbpqNgnNOPEMMNHesUkIE)
            vMpioSWBxKjOQrgisIamMlxKJVjYOaHf = tclmftGFRtKnFiydynBHNEmEqcODJwxu
            pOnYuedIKRPotKGLeyhBElrmAyUTLfmv = xyODYNYecjUPUhoYbggALGqCgPeoExzF
    if torch_total_too:
        return (pOnYuedIKRPotKGLeyhBElrmAyUTLfmv, vMpioSWBxKjOQrgisIamMlxKJVjYOaHf)
    else:
        return pOnYuedIKRPotKGLeyhBElrmAyUTLfmv
veKSzIFEKTXWuBNHlaLkijsXuLHLIqID = vJrdZOBBaEUjLkobsDWKZVCBOAICHZyg(aIQypJefEzoiiobeXriYBEHMJwDTvZWS()) / (1024 * 1024)
OVMYylabuSsLfTJDTHAaNxBUHEzJIuun = psutil.virtual_memory().total / (1024 * 1024)
print("Total VRAM {:0.0f} MB, total RAM {:0.0f} MB".format(veKSzIFEKTXWuBNHlaLkijsXuLHLIqID, OVMYylabuSsLfTJDTHAaNxBUHEzJIuun))
if not DukiculvUpjhZIVvaGinshRSKLSTgVVl.normalvram and not DukiculvUpjhZIVvaGinshRSKLSTgVVl.cpu:
    if uenKiAwaCaBygEScZqNFFJcCmPIQjOxl and veKSzIFEKTXWuBNHlaLkijsXuLHLIqID <= 4096:
        print("Trying to enable lowvram mode because your GPU seems to have 4GB or less. If you don'XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz want this use: --normalvram")
        LJPIyadMglCGcXCbArwGhXyoJxFGdhyB = bsSIGhSsMwfAaUYcCeSPPMJpGwJitrWP.VVfVZDrXgnSkeTCCsEZSDrsgdvoNXCjZ
try:
    uiFxRFoacIkrFnuAQlLvqBYROTajCRaW = torch.cuda.OutOfMemoryError
except:
    uiFxRFoacIkrFnuAQlLvqBYROTajCRaW = Exception
eRNchFEQjWOMOILGbPEmvchpGnDSszsx = ""
JVsRrAvxuVrkOSZJAuikfuJHUFpwCjOl = True
if DukiculvUpjhZIVvaGinshRSKLSTgVVl.disable_xformers:
    vcboklnCXZjBmAHPGChuylVSoiqHJRJr = False
else:
    try:
        import xformers
        import xformers.ops
        vcboklnCXZjBmAHPGChuylVSoiqHJRJr = True
        try:
            eRNchFEQjWOMOILGbPEmvchpGnDSszsx = xformers.AXCokaVjpCbdWwYKPYgzJCgAIrWdXrxQ.__version__
            print("xformers version:", eRNchFEQjWOMOILGbPEmvchpGnDSszsx)
            if eRNchFEQjWOMOILGbPEmvchpGnDSszsx.startswith("0.0.18"):
                print()
                print("WARNING: This version of xformers has a major bug where you will get black images when generating high resolution images.")
                print("Please downgrade or upgrade xformers to a different version.")
                print()
                JVsRrAvxuVrkOSZJAuikfuJHUFpwCjOl = False
        except:
            pass
    except:
        vcboklnCXZjBmAHPGChuylVSoiqHJRJr = False
def DVqffYgSzWmxuhVYAcPeksRgsBxTPaac():
    global juiVBlpYUtLrUBmtDEGztlteWPsvLbZQ
    if juiVBlpYUtLrUBmtDEGztlteWPsvLbZQ == ZnzMTovtbNqIZyGLmHCGwrCzxBPhBddd.cgDhUViYUOcOuMDteCWBWTptzTvpxlxZ:
        if torch.AXCokaVjpCbdWwYKPYgzJCgAIrWdXrxQ.cuda:
            return True
    return False
DZvIzvjAkqkpJkswFRHqtaZvinqJTGYp = DukiculvUpjhZIVvaGinshRSKLSTgVVl.use_pytorch_cross_attention
qCowljuzAdxdgKVbAjBcdFMhaoJzUJWF = torch.float32
try:
    if DVqffYgSzWmxuhVYAcPeksRgsBxTPaac():
        ZPClPSxxFNAMrlYlFwDWDrhqqTDPMQnh = torch.AXCokaVjpCbdWwYKPYgzJCgAIrWdXrxQ.__version__
        if int(ZPClPSxxFNAMrlYlFwDWDrhqqTDPMQnh[0]) >= 2:
            if DZvIzvjAkqkpJkswFRHqtaZvinqJTGYp == False and vcboklnCXZjBmAHPGChuylVSoiqHJRJr == False and DukiculvUpjhZIVvaGinshRSKLSTgVVl.use_split_cross_attention == False and DukiculvUpjhZIVvaGinshRSKLSTgVVl.use_quad_cross_attention == False:
                DZvIzvjAkqkpJkswFRHqtaZvinqJTGYp = True
            if torch.cuda.is_bf16_supported():
                qCowljuzAdxdgKVbAjBcdFMhaoJzUJWF = torch.bfloat16
except:
    pass
if KwVMPUvXTcrLXlMbtZUohDhciWKSVHEE():
    qCowljuzAdxdgKVbAjBcdFMhaoJzUJWF = torch.bfloat16
if DukiculvUpjhZIVvaGinshRSKLSTgVVl.fp16_vae:
    qCowljuzAdxdgKVbAjBcdFMhaoJzUJWF = torch.float16
elif DukiculvUpjhZIVvaGinshRSKLSTgVVl.bf16_vae:
    qCowljuzAdxdgKVbAjBcdFMhaoJzUJWF = torch.bfloat16
elif DukiculvUpjhZIVvaGinshRSKLSTgVVl.fp32_vae:
    qCowljuzAdxdgKVbAjBcdFMhaoJzUJWF = torch.float32
if DZvIzvjAkqkpJkswFRHqtaZvinqJTGYp:
    torch.backends.cuda.enable_math_sdp(True)
    torch.backends.cuda.enable_flash_sdp(True)
    torch.backends.cuda.enable_mem_efficient_sdp(True)
    vcboklnCXZjBmAHPGChuylVSoiqHJRJr = False
if DukiculvUpjhZIVvaGinshRSKLSTgVVl.lowvram:
    LJPIyadMglCGcXCbArwGhXyoJxFGdhyB = bsSIGhSsMwfAaUYcCeSPPMJpGwJitrWP.VVfVZDrXgnSkeTCCsEZSDrsgdvoNXCjZ
    uenKiAwaCaBygEScZqNFFJcCmPIQjOxl = True
elif DukiculvUpjhZIVvaGinshRSKLSTgVVl.novram:
    LJPIyadMglCGcXCbArwGhXyoJxFGdhyB = bsSIGhSsMwfAaUYcCeSPPMJpGwJitrWP.sZuTEjYlLsSpGlAgsvokhLKtJWGXtBSt
elif DukiculvUpjhZIVvaGinshRSKLSTgVVl.highvram or DukiculvUpjhZIVvaGinshRSKLSTgVVl.gpu_only:
    XWcfUReeNuYAHgWXiaGMksnQlevFLcTW = bsSIGhSsMwfAaUYcCeSPPMJpGwJitrWP.UgFpkYwkZWeRlPVDTDYbfGJbKZebAxwU
lCuoOVqdrEfSVpWTEosmhRdVLdBiqWjv = False
YdSuSQhzpUBLjGBadREIsEKqDLsEYINV = False
if DukiculvUpjhZIVvaGinshRSKLSTgVVl.force_fp32:
    print("Forcing FP32, if this improves things please report it.")
    lCuoOVqdrEfSVpWTEosmhRdVLdBiqWjv = True
if DukiculvUpjhZIVvaGinshRSKLSTgVVl.force_fp16:
    print("Forcing FP16.")
    YdSuSQhzpUBLjGBadREIsEKqDLsEYINV = True
if uenKiAwaCaBygEScZqNFFJcCmPIQjOxl:
    try:
        import accelerate
        if LJPIyadMglCGcXCbArwGhXyoJxFGdhyB in (bsSIGhSsMwfAaUYcCeSPPMJpGwJitrWP.VVfVZDrXgnSkeTCCsEZSDrsgdvoNXCjZ, bsSIGhSsMwfAaUYcCeSPPMJpGwJitrWP.sZuTEjYlLsSpGlAgsvokhLKtJWGXtBSt):
            XWcfUReeNuYAHgWXiaGMksnQlevFLcTW = LJPIyadMglCGcXCbArwGhXyoJxFGdhyB
    except Exception as dgvKdkEDrMSdkCaRxfkDNVbaXWUetgtO:
        import traceback
        print(traceback.format_exc())
        print("ERROR: LOW VRAM MODE NEEDS accelerate.")
        uenKiAwaCaBygEScZqNFFJcCmPIQjOxl = False
if juiVBlpYUtLrUBmtDEGztlteWPsvLbZQ != ZnzMTovtbNqIZyGLmHCGwrCzxBPhBddd.cgDhUViYUOcOuMDteCWBWTptzTvpxlxZ:
    XWcfUReeNuYAHgWXiaGMksnQlevFLcTW = bsSIGhSsMwfAaUYcCeSPPMJpGwJitrWP.UFZDvMQkHyQtFgyaiLMMYzebzwjzKbnN
if juiVBlpYUtLrUBmtDEGztlteWPsvLbZQ == ZnzMTovtbNqIZyGLmHCGwrCzxBPhBddd.hNmmVuyKkHcBszNhVyKhRBcIvpDkVwUd:
    XWcfUReeNuYAHgWXiaGMksnQlevFLcTW = bsSIGhSsMwfAaUYcCeSPPMJpGwJitrWP.fUORddVDjBLaHdhUZCahKFgidvhsDIPi
print(f"Set vram state to: {vram_state.name}")
NjIEdxRqdpqXlUcDlXRnvqpbxQblNfhR = DukiculvUpjhZIVvaGinshRSKLSTgVVl.disable_smart_memory
if NjIEdxRqdpqXlUcDlXRnvqpbxQblNfhR:
    print("Disabling smart memory management")
def CIUMTWevcFrsyhsNplwosYXuEZxYMCyJ(fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc):
    if hasattr(fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc, 'type'):
        if fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc.type == "cuda":
            try:
                hVHRBRuqcIiMHSgcToHpoKDoVGBTqaDF = torch.cuda.get_allocator_backend()
            except:
                hVHRBRuqcIiMHSgcToHpoKDoVGBTqaDF = ""
            return "{} {} : {}".format(fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc, torch.cuda.get_device_name(fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc), hVHRBRuqcIiMHSgcToHpoKDoVGBTqaDF)
        else:
            return "{}".format(fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc.type)
    elif KwVMPUvXTcrLXlMbtZUohDhciWKSVHEE():
        return "{} {}".format(fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc, torch.xpu.get_device_name(fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc))
    else:
        return "CUDA {}: {}".format(fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc, torch.cuda.get_device_name(fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc))
try:
    print("Device:", CIUMTWevcFrsyhsNplwosYXuEZxYMCyJ(aIQypJefEzoiiobeXriYBEHMJwDTvZWS()))
except:
    print("Could not pick default device.")
print("VAE dtype:", qCowljuzAdxdgKVbAjBcdFMhaoJzUJWF)
FfkeYsDSxglNPQNTExpnnOwBEXWBaUly = []
class FfbXlBqXzExOIBrKBYDHAPLLLbxJXNmn:
    def __init__(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM):
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM = VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.model_accelerated = False
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc = VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM.load_device
    def AMIceNNlHUikbbcFMVQYJJUvVsvzXHLM(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS):
        return rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM.ymWRjcVVevoMjPXqCNiaROKjJDVRxVuV()
    def MQQtGLLsyroAcMAWroBCfCzRdISZtAns(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc):
        if fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc == rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM.current_device:
            return 0
        else:
            return rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.AMIceNNlHUikbbcFMVQYJJUvVsvzXHLM()
    def EIyhhhygqxldOESswsKbqPZzmKJaZZAy(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, tDBLIWwBGFohuhaQQPiONjckHLCZrnys=0):
        APCyVYcCZTRmHvFLJJgTqjyloWYqwQIg = None
        if tDBLIWwBGFohuhaQQPiONjckHLCZrnys == 0:
            APCyVYcCZTRmHvFLJJgTqjyloWYqwQIg = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM.RDTOrwmBjfxGxlZjvgtcnLQViOIXZSlc(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM.RDTOrwmBjfxGxlZjvgtcnLQViOIXZSlc(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM.LnVirSCOJainsBkOCuBFzVkpVqINXQDh())
        try:
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.real_model = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM.QbcJNaFyswYsDxKtpcxHQUBPsPaTuJFs(device_to=APCyVYcCZTRmHvFLJJgTqjyloWYqwQIg) 
        except Exception as dgvKdkEDrMSdkCaRxfkDNVbaXWUetgtO:
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM.IPVijuJuWpDdBNNaJrYLjziBbaCAwYlc(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM.SlzENmVKreawuuvgrVSmYHZXOypOtbgl)
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.JxSLzJAiqMKUkNJmPjXqPfYEUoOfxhic()
            raise dgvKdkEDrMSdkCaRxfkDNVbaXWUetgtO
        if tDBLIWwBGFohuhaQQPiONjckHLCZrnys > 0:
            print("loading in lowvram mode", tDBLIWwBGFohuhaQQPiONjckHLCZrnys/(1024 * 1024))
            HqRsyLUujJHpnCSDMCsQhdJbIegGHwGT = accelerate.infer_auto_device_map(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.real_model, max_memory={0: "{}MiB".format(tDBLIWwBGFohuhaQQPiONjckHLCZrnys // (1024 * 1024)), "cpu": "16GiB"})
            accelerate.dispatch_model(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.real_model, HqRsyLUujJHpnCSDMCsQhdJbIegGHwGT=HqRsyLUujJHpnCSDMCsQhdJbIegGHwGT, main_device=rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc)
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.model_accelerated = True
        if KwVMPUvXTcrLXlMbtZUohDhciWKSVHEE() and not DukiculvUpjhZIVvaGinshRSKLSTgVVl.disable_ipex_optimize:
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.real_model = torch.xpu.optimize(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.real_model.eval(), inplace=True, auto_kernel_selection=True, graph_mode=True)
        return rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.real_model
    def JxSLzJAiqMKUkNJmPjXqPfYEUoOfxhic(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS):
        if rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.model_accelerated:
            accelerate.hooks.remove_hook_from_submodules(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.real_model)
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.model_accelerated = False
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM.IPVijuJuWpDdBNNaJrYLjziBbaCAwYlc(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM.SlzENmVKreawuuvgrVSmYHZXOypOtbgl)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM.RDTOrwmBjfxGxlZjvgtcnLQViOIXZSlc(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM.SlzENmVKreawuuvgrVSmYHZXOypOtbgl)
    def __eq__(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, other):
        return rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM is other.VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM
def BhZEdLwSnzaDJwUfESecuJfraxpORxNr():
    return (1024 * 1024 * 1024)
def tBKfYbOgStwAHAAAacRAmyKTgbFKBaRV(VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM):
    malLBWIDASxmsaybIieZrAScTgrYitEw = []
    for HCXmerBqIMuTscBONzTGKYapYSxWTYHo in range(len(FfkeYsDSxglNPQNTExpnnOwBEXWBaUly)):
        if VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM.hlsUPEbCDylvHBJIhHotpulFhpPyOFlW(FfkeYsDSxglNPQNTExpnnOwBEXWBaUly[HCXmerBqIMuTscBONzTGKYapYSxWTYHo].VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM):
            malLBWIDASxmsaybIieZrAScTgrYitEw = [HCXmerBqIMuTscBONzTGKYapYSxWTYHo] + malLBWIDASxmsaybIieZrAScTgrYitEw
    for HCXmerBqIMuTscBONzTGKYapYSxWTYHo in malLBWIDASxmsaybIieZrAScTgrYitEw:
        print("unload clone", HCXmerBqIMuTscBONzTGKYapYSxWTYHo)
        FfkeYsDSxglNPQNTExpnnOwBEXWBaUly.pop(HCXmerBqIMuTscBONzTGKYapYSxWTYHo).JxSLzJAiqMKUkNJmPjXqPfYEUoOfxhic()
def ewXbUsuAHcVJiRjpgfinHdaPAjSTrzud(memory_required, fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc, keep_loaded=[]):
    kLwkHghjFhLFLxlzmvgTrccqSwVTJxjE = False
    for HCXmerBqIMuTscBONzTGKYapYSxWTYHo in range(len(FfkeYsDSxglNPQNTExpnnOwBEXWBaUly) -1, -1, -1):
        if not NjIEdxRqdpqXlUcDlXRnvqpbxQblNfhR:
            if pEiuPTHzmozHhNpBwWGAaONYuNGSpuqI(fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc) > memory_required:
                break
        aabRFCTveTbJRpDAvKtyLupehsGxrhzo = FfkeYsDSxglNPQNTExpnnOwBEXWBaUly[HCXmerBqIMuTscBONzTGKYapYSxWTYHo]
        if aabRFCTveTbJRpDAvKtyLupehsGxrhzo.fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc == fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc:
            if aabRFCTveTbJRpDAvKtyLupehsGxrhzo not in keep_loaded:
                FTosLGldclAzaiNbwuLMIEtXfrZQpTnU = FfkeYsDSxglNPQNTExpnnOwBEXWBaUly.pop(HCXmerBqIMuTscBONzTGKYapYSxWTYHo)
                FTosLGldclAzaiNbwuLMIEtXfrZQpTnU.JxSLzJAiqMKUkNJmPjXqPfYEUoOfxhic()
                del FTosLGldclAzaiNbwuLMIEtXfrZQpTnU
                kLwkHghjFhLFLxlzmvgTrccqSwVTJxjE = True
    if kLwkHghjFhLFLxlzmvgTrccqSwVTJxjE:
        sIeWDNiYvNWPLHobyjQHaTvlWZnazsHi()
def hePDtJntacOxTjWwcIlTXDXxmfFUQfAv(models, memory_required=0):
    global XWcfUReeNuYAHgWXiaGMksnQlevFLcTW
    UUeNmHFjiQneVUrtuVohCNrZuwVSBMwU = BhZEdLwSnzaDJwUfESecuJfraxpORxNr()
    TfqgUQfWXdgBSgLRImcDRraFZVBPvcrm = max(UUeNmHFjiQneVUrtuVohCNrZuwVSBMwU, memory_required)
    lzhSOHhRZjuoYIjVoFUCdpBRfHPXFMHG = []
    eBdcMwLRfjvyvypYAKnhRuKNFiUTFfKU = []
    for NECAaWUrFGIXcLimrerEYmxYIykQBfXb in models:
        gWMlsETwCGEtQCScMJUfCpbQDgoVkgTJ = FfbXlBqXzExOIBrKBYDHAPLLLbxJXNmn(NECAaWUrFGIXcLimrerEYmxYIykQBfXb)
        if gWMlsETwCGEtQCScMJUfCpbQDgoVkgTJ in FfkeYsDSxglNPQNTExpnnOwBEXWBaUly:
            index = FfkeYsDSxglNPQNTExpnnOwBEXWBaUly.index(gWMlsETwCGEtQCScMJUfCpbQDgoVkgTJ)
            FfkeYsDSxglNPQNTExpnnOwBEXWBaUly.insert(0, FfkeYsDSxglNPQNTExpnnOwBEXWBaUly.pop(index))
            eBdcMwLRfjvyvypYAKnhRuKNFiUTFfKU.append(gWMlsETwCGEtQCScMJUfCpbQDgoVkgTJ)
        else:
            lzhSOHhRZjuoYIjVoFUCdpBRfHPXFMHG.append(gWMlsETwCGEtQCScMJUfCpbQDgoVkgTJ)
    if len(lzhSOHhRZjuoYIjVoFUCdpBRfHPXFMHG) == 0:
        erJCGJYZvjbZGXOEIGerBgbEFXzxkqrA = set(map(lambda GlZreLQjBCiBptpFgmbsMbhjFlMgPVav: GlZreLQjBCiBptpFgmbsMbhjFlMgPVav.fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc, eBdcMwLRfjvyvypYAKnhRuKNFiUTFfKU))
        for TXGwYXNLgQsYzfHHpRBDJGFCFZEClzIo in erJCGJYZvjbZGXOEIGerBgbEFXzxkqrA:
            if TXGwYXNLgQsYzfHHpRBDJGFCFZEClzIo != torch.fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc("cpu"):
                ewXbUsuAHcVJiRjpgfinHdaPAjSTrzud(TfqgUQfWXdgBSgLRImcDRraFZVBPvcrm, TXGwYXNLgQsYzfHHpRBDJGFCFZEClzIo, eBdcMwLRfjvyvypYAKnhRuKNFiUTFfKU)
        return
    print("loading new")
    FoUrwyqDTyFueQmwmIQernGktGVEkvwi = {}
    for gWMlsETwCGEtQCScMJUfCpbQDgoVkgTJ in lzhSOHhRZjuoYIjVoFUCdpBRfHPXFMHG:
        tBKfYbOgStwAHAAAacRAmyKTgbFKBaRV(gWMlsETwCGEtQCScMJUfCpbQDgoVkgTJ.VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM)
        FoUrwyqDTyFueQmwmIQernGktGVEkvwi[gWMlsETwCGEtQCScMJUfCpbQDgoVkgTJ.fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc] = FoUrwyqDTyFueQmwmIQernGktGVEkvwi.get(gWMlsETwCGEtQCScMJUfCpbQDgoVkgTJ.fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc, 0) + gWMlsETwCGEtQCScMJUfCpbQDgoVkgTJ.MQQtGLLsyroAcMAWroBCfCzRdISZtAns(gWMlsETwCGEtQCScMJUfCpbQDgoVkgTJ.fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc)
    for fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc in FoUrwyqDTyFueQmwmIQernGktGVEkvwi:
        if fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc != torch.fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc("cpu"):
            ewXbUsuAHcVJiRjpgfinHdaPAjSTrzud(FoUrwyqDTyFueQmwmIQernGktGVEkvwi[fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc] * 1.3 + TfqgUQfWXdgBSgLRImcDRraFZVBPvcrm, fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc, eBdcMwLRfjvyvypYAKnhRuKNFiUTFfKU)
    for gWMlsETwCGEtQCScMJUfCpbQDgoVkgTJ in lzhSOHhRZjuoYIjVoFUCdpBRfHPXFMHG:
        VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM = gWMlsETwCGEtQCScMJUfCpbQDgoVkgTJ.VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM
        qxChBbXgmHGvShWfrlkAlcJfGoosKGEU = VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM.load_device
        if ioAiXxCftMnqgaPIIDsVtFGXZzkoBTeS(qxChBbXgmHGvShWfrlkAlcJfGoosKGEU):
            wwegoDAYvCMyEVzJyKsZSJLrJpAJSwMU = bsSIGhSsMwfAaUYcCeSPPMJpGwJitrWP.UFZDvMQkHyQtFgyaiLMMYzebzwjzKbnN
        else:
            wwegoDAYvCMyEVzJyKsZSJLrJpAJSwMU = XWcfUReeNuYAHgWXiaGMksnQlevFLcTW
        tDBLIWwBGFohuhaQQPiONjckHLCZrnys = 0
        if uenKiAwaCaBygEScZqNFFJcCmPIQjOxl and (wwegoDAYvCMyEVzJyKsZSJLrJpAJSwMU == bsSIGhSsMwfAaUYcCeSPPMJpGwJitrWP.VVfVZDrXgnSkeTCCsEZSDrsgdvoNXCjZ or wwegoDAYvCMyEVzJyKsZSJLrJpAJSwMU == bsSIGhSsMwfAaUYcCeSPPMJpGwJitrWP.xmfoFlkMIlumPovjAHlmdldLqjMICkUt):
            ymWRjcVVevoMjPXqCNiaROKjJDVRxVuV = gWMlsETwCGEtQCScMJUfCpbQDgoVkgTJ.MQQtGLLsyroAcMAWroBCfCzRdISZtAns(qxChBbXgmHGvShWfrlkAlcJfGoosKGEU)
            xllbafDFdXuZQfvbPcIaHikKQYibetEj = pEiuPTHzmozHhNpBwWGAaONYuNGSpuqI(qxChBbXgmHGvShWfrlkAlcJfGoosKGEU)
            tDBLIWwBGFohuhaQQPiONjckHLCZrnys = int(max(256 * (1024 * 1024), (xllbafDFdXuZQfvbPcIaHikKQYibetEj - 1024 * (1024 * 1024)) / 1.3 ))
            if ymWRjcVVevoMjPXqCNiaROKjJDVRxVuV > (xllbafDFdXuZQfvbPcIaHikKQYibetEj - UUeNmHFjiQneVUrtuVohCNrZuwVSBMwU): 
                wwegoDAYvCMyEVzJyKsZSJLrJpAJSwMU = bsSIGhSsMwfAaUYcCeSPPMJpGwJitrWP.VVfVZDrXgnSkeTCCsEZSDrsgdvoNXCjZ
            else:
                tDBLIWwBGFohuhaQQPiONjckHLCZrnys = 0
        if wwegoDAYvCMyEVzJyKsZSJLrJpAJSwMU == bsSIGhSsMwfAaUYcCeSPPMJpGwJitrWP.sZuTEjYlLsSpGlAgsvokhLKtJWGXtBSt:
            tDBLIWwBGFohuhaQQPiONjckHLCZrnys = 256 * 1024 * 1024
        SDFdGXgNPWXQtDcfwAWRDdOuUlYtuPmn = gWMlsETwCGEtQCScMJUfCpbQDgoVkgTJ.EIyhhhygqxldOESswsKbqPZzmKJaZZAy(tDBLIWwBGFohuhaQQPiONjckHLCZrnys)
        FfkeYsDSxglNPQNTExpnnOwBEXWBaUly.insert(0, gWMlsETwCGEtQCScMJUfCpbQDgoVkgTJ)
    return
def kXOGaMSSvphjyezwWWyYPLRGDFntsRVH(VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM):
    return hePDtJntacOxTjWwcIlTXDXxmfFUQfAv([VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM])
def swGRFPugxSKWuFFSumUDzRojyZMqyytZ():
    HZgFvSCHHvndfkOsuWOqyKgtGBOkAfAZ = []
    for HCXmerBqIMuTscBONzTGKYapYSxWTYHo in range(len(FfkeYsDSxglNPQNTExpnnOwBEXWBaUly)):
        print(sys.getrefcount(FfkeYsDSxglNPQNTExpnnOwBEXWBaUly[HCXmerBqIMuTscBONzTGKYapYSxWTYHo].VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM))
        if sys.getrefcount(FfkeYsDSxglNPQNTExpnnOwBEXWBaUly[HCXmerBqIMuTscBONzTGKYapYSxWTYHo].VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM) <= 2:
            HZgFvSCHHvndfkOsuWOqyKgtGBOkAfAZ = [HCXmerBqIMuTscBONzTGKYapYSxWTYHo] + HZgFvSCHHvndfkOsuWOqyKgtGBOkAfAZ
    for HCXmerBqIMuTscBONzTGKYapYSxWTYHo in HZgFvSCHHvndfkOsuWOqyKgtGBOkAfAZ:
        NECAaWUrFGIXcLimrerEYmxYIykQBfXb = FfkeYsDSxglNPQNTExpnnOwBEXWBaUly.pop(HCXmerBqIMuTscBONzTGKYapYSxWTYHo)
        NECAaWUrFGIXcLimrerEYmxYIykQBfXb.JxSLzJAiqMKUkNJmPjXqPfYEUoOfxhic()
        del NECAaWUrFGIXcLimrerEYmxYIykQBfXb
def YtdGBnIPnrvLkEwWTnnTACWnmoKQkWef(DDRQlhrNSGpwTrokWitkZipdfbAqBFxv):
    YtdGBnIPnrvLkEwWTnnTACWnmoKQkWef = 4
    if DDRQlhrNSGpwTrokWitkZipdfbAqBFxv == torch.float16 or DDRQlhrNSGpwTrokWitkZipdfbAqBFxv == torch.bfloat16:
        YtdGBnIPnrvLkEwWTnnTACWnmoKQkWef = 2
    return YtdGBnIPnrvLkEwWTnnTACWnmoKQkWef
def NPYgJTJBLTgTpVRGASjizjQOHZYHkGwk():
    if XWcfUReeNuYAHgWXiaGMksnQlevFLcTW == bsSIGhSsMwfAaUYcCeSPPMJpGwJitrWP.UgFpkYwkZWeRlPVDTDYbfGJbKZebAxwU:
        return aIQypJefEzoiiobeXriYBEHMJwDTvZWS()
    else:
        return torch.fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc("cpu")
def BwkFoHezUkMdKklCWJzPKpCSLQiPHevU(parameters, DDRQlhrNSGpwTrokWitkZipdfbAqBFxv):
    qxChBbXgmHGvShWfrlkAlcJfGoosKGEU = aIQypJefEzoiiobeXriYBEHMJwDTvZWS()
    if XWcfUReeNuYAHgWXiaGMksnQlevFLcTW == bsSIGhSsMwfAaUYcCeSPPMJpGwJitrWP.UgFpkYwkZWeRlPVDTDYbfGJbKZebAxwU:
        return qxChBbXgmHGvShWfrlkAlcJfGoosKGEU
    vEthuWaYJODGuiLIhVoxiboQwhYEFQTC = torch.fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc("cpu")
    if NjIEdxRqdpqXlUcDlXRnvqpbxQblNfhR:
        return vEthuWaYJODGuiLIhVoxiboQwhYEFQTC
    ymWRjcVVevoMjPXqCNiaROKjJDVRxVuV = YtdGBnIPnrvLkEwWTnnTACWnmoKQkWef(DDRQlhrNSGpwTrokWitkZipdfbAqBFxv) * parameters
    TzPJJUtOrNSCDAUBlGOZDiuVffcoAOOT = pEiuPTHzmozHhNpBwWGAaONYuNGSpuqI(qxChBbXgmHGvShWfrlkAlcJfGoosKGEU)
    FHkzgnCZhlsbsReoOBOIbOPRTlIcbzyP = pEiuPTHzmozHhNpBwWGAaONYuNGSpuqI(vEthuWaYJODGuiLIhVoxiboQwhYEFQTC)
    if TzPJJUtOrNSCDAUBlGOZDiuVffcoAOOT > FHkzgnCZhlsbsReoOBOIbOPRTlIcbzyP and ymWRjcVVevoMjPXqCNiaROKjJDVRxVuV < TzPJJUtOrNSCDAUBlGOZDiuVffcoAOOT:
        return qxChBbXgmHGvShWfrlkAlcJfGoosKGEU
    else:
        return vEthuWaYJODGuiLIhVoxiboQwhYEFQTC
def dqLuwFxiusOelmbvAEJTDqSGYtVhBvgP():
    if DukiculvUpjhZIVvaGinshRSKLSTgVVl.gpu_only:
        return aIQypJefEzoiiobeXriYBEHMJwDTvZWS()
    else:
        return torch.fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc("cpu")
def sJVlxAzjdIdFAWAuvdyJGHtFVXvPbtas():
    if DukiculvUpjhZIVvaGinshRSKLSTgVVl.gpu_only:
        return aIQypJefEzoiiobeXriYBEHMJwDTvZWS()
    elif XWcfUReeNuYAHgWXiaGMksnQlevFLcTW == bsSIGhSsMwfAaUYcCeSPPMJpGwJitrWP.UgFpkYwkZWeRlPVDTDYbfGJbKZebAxwU or XWcfUReeNuYAHgWXiaGMksnQlevFLcTW == bsSIGhSsMwfAaUYcCeSPPMJpGwJitrWP.xmfoFlkMIlumPovjAHlmdldLqjMICkUt:
        if LlPEFQdsyRQPhjrfArraPsqqOdqUiGhQ(prioritize_performance=False):
            return aIQypJefEzoiiobeXriYBEHMJwDTvZWS()
        else:
            return torch.fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc("cpu")
    else:
        return torch.fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc("cpu")
def zuJfaIVUVTEmsdCoRWVPlHBmxypRJNsM():
    return aIQypJefEzoiiobeXriYBEHMJwDTvZWS()
def rbjCHbLylizwDImHfhIiyuDrPiLxESxv():
    if DukiculvUpjhZIVvaGinshRSKLSTgVVl.gpu_only:
        return aIQypJefEzoiiobeXriYBEHMJwDTvZWS()
    else:
        return torch.fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc("cpu")
def ZqDDNItYkrDACxJojECjSvkCxXbdyHhx():
    global qCowljuzAdxdgKVbAjBcdFMhaoJzUJWF
    return qCowljuzAdxdgKVbAjBcdFMhaoJzUJWF
def wnvxDevQWKlbjTSkvEgnuqaeEwzNgHXB(ZclsJeyZNkbLbpqNgnNOPEMMNHesUkIE):
    if hasattr(ZclsJeyZNkbLbpqNgnNOPEMMNHesUkIE, 'type'):
        return ZclsJeyZNkbLbpqNgnNOPEMMNHesUkIE.type
    return "cuda"
def fpzqQPwQsgljpVXCeYPLnjVJExRYKmpM():
    global ZnhsFYXiDrJhDvSRdTZbdswNjfAVNkiY
    global juiVBlpYUtLrUBmtDEGztlteWPsvLbZQ
    if juiVBlpYUtLrUBmtDEGztlteWPsvLbZQ != ZnzMTovtbNqIZyGLmHCGwrCzxBPhBddd.cgDhUViYUOcOuMDteCWBWTptzTvpxlxZ:
        return False
    if KwVMPUvXTcrLXlMbtZUohDhciWKSVHEE():
        return False
    if ZnhsFYXiDrJhDvSRdTZbdswNjfAVNkiY:
        return False
    return vcboklnCXZjBmAHPGChuylVSoiqHJRJr
def tifElOLkamgDCGAybMmNngkxKANHIbzS():
    ClvYjtcXylmicwCwVQPykJTWmcwImVEP = fpzqQPwQsgljpVXCeYPLnjVJExRYKmpM()
    if not ClvYjtcXylmicwCwVQPykJTWmcwImVEP:
        return False
    return JVsRrAvxuVrkOSZJAuikfuJHUFpwCjOl
def kQDSfcrSuHTuIBtYUKBNyIxOCqzlxNlm():
    global DZvIzvjAkqkpJkswFRHqtaZvinqJTGYp
    return DZvIzvjAkqkpJkswFRHqtaZvinqJTGYp
def LmHUtOnHEobaJRMzJJQyCSrAdMSLaYpO():
    global DZvIzvjAkqkpJkswFRHqtaZvinqJTGYp
    if DZvIzvjAkqkpJkswFRHqtaZvinqJTGYp:
        if DVqffYgSzWmxuhVYAcPeksRgsBxTPaac(): 
            return True
    return False
def pEiuPTHzmozHhNpBwWGAaONYuNGSpuqI(ZclsJeyZNkbLbpqNgnNOPEMMNHesUkIE=None, torch_free_too=False):
    global ZnhsFYXiDrJhDvSRdTZbdswNjfAVNkiY
    if ZclsJeyZNkbLbpqNgnNOPEMMNHesUkIE is None:
        ZclsJeyZNkbLbpqNgnNOPEMMNHesUkIE = aIQypJefEzoiiobeXriYBEHMJwDTvZWS()
    if hasattr(ZclsJeyZNkbLbpqNgnNOPEMMNHesUkIE, 'type') and (ZclsJeyZNkbLbpqNgnNOPEMMNHesUkIE.type == 'cpu' or ZclsJeyZNkbLbpqNgnNOPEMMNHesUkIE.type == 'mps'):
        GPfGQFkmkbPdFypYtapiuNmsHHdeiLUL = psutil.virtual_memory().available
        AGGPItzIimskEiuQBFJsAxXDSPwlOIrM = GPfGQFkmkbPdFypYtapiuNmsHHdeiLUL
    else:
        if ZnhsFYXiDrJhDvSRdTZbdswNjfAVNkiY:
            GPfGQFkmkbPdFypYtapiuNmsHHdeiLUL = 1024 * 1024 * 1024 
            AGGPItzIimskEiuQBFJsAxXDSPwlOIrM = GPfGQFkmkbPdFypYtapiuNmsHHdeiLUL
        elif KwVMPUvXTcrLXlMbtZUohDhciWKSVHEE():
            jnfIHeLvMhRAslhkREQLmMNJsXQjQGQh = torch.xpu.memory_stats(ZclsJeyZNkbLbpqNgnNOPEMMNHesUkIE)
            uSOBDJEyVeWZeclOGZGRFLcMdGPcgkrg = jnfIHeLvMhRAslhkREQLmMNJsXQjQGQh['active_bytes.all.current']
            NlACvCKDuohzrqdGJVQwtGYoIFWtXkeL = jnfIHeLvMhRAslhkREQLmMNJsXQjQGQh['allocated_bytes.all.current']
            tclmftGFRtKnFiydynBHNEmEqcODJwxu = jnfIHeLvMhRAslhkREQLmMNJsXQjQGQh['reserved_bytes.all.current']
            AGGPItzIimskEiuQBFJsAxXDSPwlOIrM = tclmftGFRtKnFiydynBHNEmEqcODJwxu - uSOBDJEyVeWZeclOGZGRFLcMdGPcgkrg
            GPfGQFkmkbPdFypYtapiuNmsHHdeiLUL = torch.xpu.get_device_properties(ZclsJeyZNkbLbpqNgnNOPEMMNHesUkIE).total_memory - NlACvCKDuohzrqdGJVQwtGYoIFWtXkeL
        else:
            jnfIHeLvMhRAslhkREQLmMNJsXQjQGQh = torch.cuda.memory_stats(ZclsJeyZNkbLbpqNgnNOPEMMNHesUkIE)
            uSOBDJEyVeWZeclOGZGRFLcMdGPcgkrg = jnfIHeLvMhRAslhkREQLmMNJsXQjQGQh['active_bytes.all.current']
            tclmftGFRtKnFiydynBHNEmEqcODJwxu = jnfIHeLvMhRAslhkREQLmMNJsXQjQGQh['reserved_bytes.all.current']
            bLdRlCbdaeBYOyHpjSfQFxRMMEURpZTX, _ = torch.cuda.mem_get_info(ZclsJeyZNkbLbpqNgnNOPEMMNHesUkIE)
            AGGPItzIimskEiuQBFJsAxXDSPwlOIrM = tclmftGFRtKnFiydynBHNEmEqcODJwxu - uSOBDJEyVeWZeclOGZGRFLcMdGPcgkrg
            GPfGQFkmkbPdFypYtapiuNmsHHdeiLUL = bLdRlCbdaeBYOyHpjSfQFxRMMEURpZTX + AGGPItzIimskEiuQBFJsAxXDSPwlOIrM
    if torch_free_too:
        return (GPfGQFkmkbPdFypYtapiuNmsHHdeiLUL, AGGPItzIimskEiuQBFJsAxXDSPwlOIrM)
    else:
        return GPfGQFkmkbPdFypYtapiuNmsHHdeiLUL
def lxwarqEuDMRDmYdMwbHDlziRlGulMSMD(PwhgTrGNWmGcxauFNPvZUzwrMxrcaDHR):
    if fpzqQPwQsgljpVXCeYPLnjVJExRYKmpM() or LmHUtOnHEobaJRMzJJQyCSrAdMSLaYpO():
        return (PwhgTrGNWmGcxauFNPvZUzwrMxrcaDHR / 20) * (1024 * 1024)
    else:
        return (((PwhgTrGNWmGcxauFNPvZUzwrMxrcaDHR * 0.6) / 0.9) + 1024) * (1024 * 1024)
def ftPVzCnUTasFvGiQpnGOOcDKmxXmWOAb():
    global XWcfUReeNuYAHgWXiaGMksnQlevFLcTW
    if XWcfUReeNuYAHgWXiaGMksnQlevFLcTW == bsSIGhSsMwfAaUYcCeSPPMJpGwJitrWP.sZuTEjYlLsSpGlAgsvokhLKtJWGXtBSt:
        return 0
    IXTWcznOcZKXpZEMTEEOHcQTIWQVdnyI = pEiuPTHzmozHhNpBwWGAaONYuNGSpuqI() / (1024 * 1024)
    if fpzqQPwQsgljpVXCeYPLnjVJExRYKmpM() or LmHUtOnHEobaJRMzJJQyCSrAdMSLaYpO():
        PwhgTrGNWmGcxauFNPvZUzwrMxrcaDHR = 20 * IXTWcznOcZKXpZEMTEEOHcQTIWQVdnyI
    else:
        PwhgTrGNWmGcxauFNPvZUzwrMxrcaDHR = ((IXTWcznOcZKXpZEMTEEOHcQTIWQVdnyI - 1024) * 0.9) / (0.6)
    return int(max(PwhgTrGNWmGcxauFNPvZUzwrMxrcaDHR, 0))
def YLsTZtHbHfkBglTAIMHWtMKYRdphevCa():
    global juiVBlpYUtLrUBmtDEGztlteWPsvLbZQ
    return juiVBlpYUtLrUBmtDEGztlteWPsvLbZQ == ZnzMTovtbNqIZyGLmHCGwrCzxBPhBddd.amvcnbTgIfYErScizhLPObRvsCqqoxLu
def SAwmFeRpGeYWXQgcdsAGvsnMQYGkubrw():
    global juiVBlpYUtLrUBmtDEGztlteWPsvLbZQ
    return juiVBlpYUtLrUBmtDEGztlteWPsvLbZQ == ZnzMTovtbNqIZyGLmHCGwrCzxBPhBddd.hNmmVuyKkHcBszNhVyKhRBcIvpDkVwUd
def ioAiXxCftMnqgaPIIDsVtFGXZzkoBTeS(fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc):
    if hasattr(fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc, 'type'):
        if (fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc.type == 'cpu'):
            return True
    return False
def QwMlZFtdFFPZWYeJfMWWfpZthldmgRri(fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc):
    if hasattr(fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc, 'type'):
        if (fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc.type == 'mps'):
            return True
    return False
def LlPEFQdsyRQPhjrfArraPsqqOdqUiGhQ(fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc=None, PdGWiWNrDwHLuxVqHGwwISTXDvUzkDgP=0, prioritize_performance=True):
    global ZnhsFYXiDrJhDvSRdTZbdswNjfAVNkiY
    if fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc is not None:
        if ioAiXxCftMnqgaPIIDsVtFGXZzkoBTeS(fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc):
            return False
    if YdSuSQhzpUBLjGBadREIsEKqDLsEYINV:
        return True
    if fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc is not None: 
        if QwMlZFtdFFPZWYeJfMWWfpZthldmgRri(fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc):
            return False
    if lCuoOVqdrEfSVpWTEosmhRdVLdBiqWjv:
        return False
    if ZnhsFYXiDrJhDvSRdTZbdswNjfAVNkiY:
        return False
    if YLsTZtHbHfkBglTAIMHWtMKYRdphevCa() or SAwmFeRpGeYWXQgcdsAGvsnMQYGkubrw():
        return False 
    if KwVMPUvXTcrLXlMbtZUohDhciWKSVHEE():
        return True
    if torch.cuda.is_bf16_supported():
        return True
    cQvoHpxzlKBypKSOHIlIcyjpjLnzphFe = torch.cuda.get_device_properties("cuda")
    if cQvoHpxzlKBypKSOHIlIcyjpjLnzphFe.major < 6:
        return False
    TybTfjccLYlRrmjrblOlIJZQgUgZmlBM = False
    OiNVyiywgURbgOHSjdnIYNDIIaJjOJre = ["1080", "1070", "titan x", "p3000", "p3200", "p4000", "p4200", "p5000", "p5200", "p6000", "1060", "1050"]
    for NECAaWUrFGIXcLimrerEYmxYIykQBfXb in OiNVyiywgURbgOHSjdnIYNDIIaJjOJre:
        if NECAaWUrFGIXcLimrerEYmxYIykQBfXb in cQvoHpxzlKBypKSOHIlIcyjpjLnzphFe.pSfJNVvqLWVlUeHdpahCTGSrSPJYAnEQ.lower():
            TybTfjccLYlRrmjrblOlIJZQgUgZmlBM = True
    if TybTfjccLYlRrmjrblOlIJZQgUgZmlBM:
        sGVNGqMDbfOiItaBylfOUWpFtkYLRfBF = (pEiuPTHzmozHhNpBwWGAaONYuNGSpuqI() * 0.9 - BhZEdLwSnzaDJwUfESecuJfraxpORxNr())
        if (not prioritize_performance) or PdGWiWNrDwHLuxVqHGwwISTXDvUzkDgP * 4 > sGVNGqMDbfOiItaBylfOUWpFtkYLRfBF:
            return True
    if cQvoHpxzlKBypKSOHIlIcyjpjLnzphFe.major < 7:
        return False
    BXOksMoCymLVRejnmYFCcWFrzgWLVtuJ = ["1660", "1650", "1630", "T500", "T550", "T600", "MX550", "MX450", "CMP 30HX"]
    for NECAaWUrFGIXcLimrerEYmxYIykQBfXb in BXOksMoCymLVRejnmYFCcWFrzgWLVtuJ:
        if NECAaWUrFGIXcLimrerEYmxYIykQBfXb in cQvoHpxzlKBypKSOHIlIcyjpjLnzphFe.pSfJNVvqLWVlUeHdpahCTGSrSPJYAnEQ:
            return False
    return True
def sIeWDNiYvNWPLHobyjQHaTvlWZnazsHi(force=False):
    global juiVBlpYUtLrUBmtDEGztlteWPsvLbZQ
    if juiVBlpYUtLrUBmtDEGztlteWPsvLbZQ == ZnzMTovtbNqIZyGLmHCGwrCzxBPhBddd.hNmmVuyKkHcBszNhVyKhRBcIvpDkVwUd:
        torch.mps.empty_cache()
    elif KwVMPUvXTcrLXlMbtZUohDhciWKSVHEE():
        torch.xpu.empty_cache()
    elif torch.cuda.is_available():
        if force or DVqffYgSzWmxuhVYAcPeksRgsBxTPaac(): 
            torch.cuda.empty_cache()
            torch.cuda.ipc_collect()
def fJSttSHgRmTiJkiWezuwVxBkdvWTIAvw(RXBOtvKSHQkBvdKDbckmnlphvVygYURP, VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM, nyrzKxQtioheHIZujafABgijbCjrWhBU):
    if RXBOtvKSHQkBvdKDbckmnlphvVygYURP.fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc == torch.fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc("meta"): 
        LzoAloNRhZjLeevNrYoyQqisMYXZbMuT = nyrzKxQtioheHIZujafABgijbCjrWhBU.split('.')              
        bjtPzNLsLxvykINbAtlMwKlGJQooJtzI = quasar.utils.get_attr(VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM, '.'.join(LzoAloNRhZjLeevNrYoyQqisMYXZbMuT[:-1]))
        RXBOtvKSHQkBvdKDbckmnlphvVygYURP = bjtPzNLsLxvykINbAtlMwKlGJQooJtzI._hf_hook.weights_map[LzoAloNRhZjLeevNrYoyQqisMYXZbMuT[-1]]
    return RXBOtvKSHQkBvdKDbckmnlphvVygYURP
import threading
class FcmhbKAfUbwHtuUFKflJjsPfbobaJqvP(Exception):
    pass
TcCBqXJWePLEWaLVEhNmoSuPlxBFLrqe = threading.RLock()
NIMMAjqKpMwgFfFMJGlJLJdwCPLKOQTM = False
def ggsUtIbLrBjTjYoMQwfUAZvlFgfjRNAK(value=True):
    global NIMMAjqKpMwgFfFMJGlJLJdwCPLKOQTM
    global TcCBqXJWePLEWaLVEhNmoSuPlxBFLrqe
    with TcCBqXJWePLEWaLVEhNmoSuPlxBFLrqe:
        NIMMAjqKpMwgFfFMJGlJLJdwCPLKOQTM = value
def YWJBrEdoGByBmOQFMXiRByRmSfnooCWg():
    global NIMMAjqKpMwgFfFMJGlJLJdwCPLKOQTM
    global TcCBqXJWePLEWaLVEhNmoSuPlxBFLrqe
    with TcCBqXJWePLEWaLVEhNmoSuPlxBFLrqe:
        return NIMMAjqKpMwgFfFMJGlJLJdwCPLKOQTM
def cufzYbsmvfzVPCacJuRroKjPAHWqOusW():
    global NIMMAjqKpMwgFfFMJGlJLJdwCPLKOQTM
    global TcCBqXJWePLEWaLVEhNmoSuPlxBFLrqe
    with TcCBqXJWePLEWaLVEhNmoSuPlxBFLrqe:
        if NIMMAjqKpMwgFfFMJGlJLJdwCPLKOQTM:
            NIMMAjqKpMwgFfFMJGlJLJdwCPLKOQTM = False
            raise FcmhbKAfUbwHtuUFKflJjsPfbobaJqvP()
