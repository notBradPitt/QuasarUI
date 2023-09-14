import importlib
import torch
from torch import optim
import numpy as np
from inspect import isfunction
from PIL import Image, ImageDraw, ImageFont
def HfllaoODQNAKLTFWiQpHMEGjWMiEKOvy(wh, RFDsQwESUjeJfiPgSSVsMLLYlHaZhFoO, vqDBJgidQufnKyAltPYRqiKGjmztArDJ=10):
    b = len(RFDsQwESUjeJfiPgSSVsMLLYlHaZhFoO)
    RwuLgHmuydINdRclYbcjRQYllIegGWNX = list()
    for yxxYrwQLMMSWucQsTsVtSHMcRYQfLskE in range(b):
        RjbpXqoMyPZAmgptHWPBEETbLVFTnfjy = Image.new("RGB", wh, color="white")
        qpZZNNWjkKaSzyJyrXqnlfLLYpjqkOPj = ImageDraw.Draw(RjbpXqoMyPZAmgptHWPBEETbLVFTnfjy)
        dsatOIhgAcHwIQkhZlecQmrscRHtlKWQ = ImageFont.truetype('data/DejaVuSans.ttf', vqDBJgidQufnKyAltPYRqiKGjmztArDJ=vqDBJgidQufnKyAltPYRqiKGjmztArDJ)
        SPKuTOwasLAlPwlgOWdrcoOQjpyXyMLo = int(40 * (wh[0] / 256))
        ZryGmWpYRAUrHkedIjWPTTdrhKyjktLU = "\n".join(RFDsQwESUjeJfiPgSSVsMLLYlHaZhFoO[yxxYrwQLMMSWucQsTsVtSHMcRYQfLskE][tUuYqnLjDXuftYgMagGpmrobxWgfcbgq:tUuYqnLjDXuftYgMagGpmrobxWgfcbgq + SPKuTOwasLAlPwlgOWdrcoOQjpyXyMLo] for tUuYqnLjDXuftYgMagGpmrobxWgfcbgq in range(0, len(RFDsQwESUjeJfiPgSSVsMLLYlHaZhFoO[yxxYrwQLMMSWucQsTsVtSHMcRYQfLskE]), SPKuTOwasLAlPwlgOWdrcoOQjpyXyMLo))
        try:
            qpZZNNWjkKaSzyJyrXqnlfLLYpjqkOPj.text((0, 0), ZryGmWpYRAUrHkedIjWPTTdrhKyjktLU, fill="black", dsatOIhgAcHwIQkhZlecQmrscRHtlKWQ=dsatOIhgAcHwIQkhZlecQmrscRHtlKWQ)
        except UnicodeEncodeError:
            print("Cant encode string for logging. Skipping.")
        RjbpXqoMyPZAmgptHWPBEETbLVFTnfjy = np.array(RjbpXqoMyPZAmgptHWPBEETbLVFTnfjy).transpose(2, 0, 1) / 127.5 - 1.0
        RwuLgHmuydINdRclYbcjRQYllIegGWNX.append(RjbpXqoMyPZAmgptHWPBEETbLVFTnfjy)
    RwuLgHmuydINdRclYbcjRQYllIegGWNX = np.stack(RwuLgHmuydINdRclYbcjRQYllIegGWNX)
    RwuLgHmuydINdRclYbcjRQYllIegGWNX = torch.xPmCFphFKpGMpIsczaSKHmMgRPZzJwla(RwuLgHmuydINdRclYbcjRQYllIegGWNX)
    return RwuLgHmuydINdRclYbcjRQYllIegGWNX
def ZzwbNPhUuXXssxbTuYyHPoxTrklsirLS(NECAaWUrFGIXcLimrerEYmxYIykQBfXb):
    if not isinstance(NECAaWUrFGIXcLimrerEYmxYIykQBfXb, torch.Tensor):
        return False
    return (len(NECAaWUrFGIXcLimrerEYmxYIykQBfXb.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg) == 4) and (NECAaWUrFGIXcLimrerEYmxYIykQBfXb.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[1] > 3)
def gAKoXnrVLIlIxvWCILBMTLkCdBWswcJy(NECAaWUrFGIXcLimrerEYmxYIykQBfXb):
    if not isinstance(NECAaWUrFGIXcLimrerEYmxYIykQBfXb,torch.Tensor):
        return False
    return (len(NECAaWUrFGIXcLimrerEYmxYIykQBfXb.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg) == 4) and (NECAaWUrFGIXcLimrerEYmxYIykQBfXb.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[1] == 3 or NECAaWUrFGIXcLimrerEYmxYIykQBfXb.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[1] == 1)
def CzuSRmujwDQnNtuxpiDhURIOWmCdbjjH(NECAaWUrFGIXcLimrerEYmxYIykQBfXb):
    return NECAaWUrFGIXcLimrerEYmxYIykQBfXb is not None
def zKvTEPbGDoRBsQSYYaddQKLTFDorvdms(iQelECAceWgpMwNVKVNfqYXiZvxEyNPn, TXGwYXNLgQsYzfHHpRBDJGFCFZEClzIo):
    if CzuSRmujwDQnNtuxpiDhURIOWmCdbjjH(iQelECAceWgpMwNVKVNfqYXiZvxEyNPn):
        return iQelECAceWgpMwNVKVNfqYXiZvxEyNPn
    return TXGwYXNLgQsYzfHHpRBDJGFCFZEClzIo() if isfunction(TXGwYXNLgQsYzfHHpRBDJGFCFZEClzIo) else TXGwYXNLgQsYzfHHpRBDJGFCFZEClzIo
def LQBGcVjMdfNQYPLmVRRnitgdXFeFXNHl(xPmCFphFKpGMpIsczaSKHmMgRPZzJwla):
    return xPmCFphFKpGMpIsczaSKHmMgRPZzJwla.mean(yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk=list(range(1, len(xPmCFphFKpGMpIsczaSKHmMgRPZzJwla.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg))))
def puFyScOxbCoaJpDyPPCuBECupHqupNWc(VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM, aFZoJwWpCnqyOJdcAMLlqOHxDgjPTNCS=False):
    qyAeWGjwkAKXKqNJnPEFUWsaxokgrMHt = sum(HutkrxeXIuRQKOhCWHkiwqLGAsJjUSKj.numel() for HutkrxeXIuRQKOhCWHkiwqLGAsJjUSKj in VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM.parameters())
    if aFZoJwWpCnqyOJdcAMLlqOHxDgjPTNCS:
        print(f"{model.__class__.__name__} has {total_params*1.e-6:.2f} M params.")
    return qyAeWGjwkAKXKqNJnPEFUWsaxokgrMHt
def EGpJWSXQbHSqfmcMzBaJeJAuDkDlnmrK(hNBxbvKCDbRukyaGMnSKVERydVUZJyCM):
    if not "target" in hNBxbvKCDbRukyaGMnSKVERydVUZJyCM:
        if hNBxbvKCDbRukyaGMnSKVERydVUZJyCM == '__is_first_stage__':
            return None
        elif hNBxbvKCDbRukyaGMnSKVERydVUZJyCM == "__is_unconditional__":
            return None
        raise KeyError("Expected key `target` to instantiate.")
    return tKEmVJXddieUvwAAwLUzsRfqAMEptvQj(hNBxbvKCDbRukyaGMnSKVERydVUZJyCM["target"])(**hNBxbvKCDbRukyaGMnSKVERydVUZJyCM.get("params", dict()))
def tKEmVJXddieUvwAAwLUzsRfqAMEptvQj(string, reload=False):
    FRIBQCDfDDxIonplwxvPCicvOmmOgYPC, qImTjFfovKitSMWzOmePbprJitutCVKi = string.rsplit(".", 1)
    if reload:
        module_imp = importlib.import_module(module)
        importlib.reload(module_imp)
    return getattr(importlib.import_module(module, package=None), cls)
class yAZCiIvpBfsXHJlhDcwbveVaGrmswZaZ(optim.Optimizer):
    def __init__(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, params, BbjvYJKNzsfQZuahPgdyaFZrYmxOIhRT=1.dgvKdkEDrMSdkCaRxfkDNVbaXWUetgtO-3, aGiatFWLVusbPGSDloFtejqscKjAwtLv=(0.9, 0.999), VVqkfbMIOFDgzhOKKnJVcuOffzzrOGPv=1.dgvKdkEDrMSdkCaRxfkDNVbaXWUetgtO-8,  
                 IXIijmgGcHCScFjClwljTOXTswNkiIkK=1.dgvKdkEDrMSdkCaRxfkDNVbaXWUetgtO-2, CYYsnkfcHEJHHedghOjEJLrmJvXYOCpq=False, bGiLySteHgQEfhoICMWhUyeWhlsZpzRt=0.9999,   
                 NrlrYzsfxnatCeZgJtAuRDendjKXEJSe=1., param_names=()):
        if not 0.0 <= BbjvYJKNzsfQZuahPgdyaFZrYmxOIhRT:
            raise ValueError("Invalid learning rate: {}".format(BbjvYJKNzsfQZuahPgdyaFZrYmxOIhRT))
        if not 0.0 <= VVqkfbMIOFDgzhOKKnJVcuOffzzrOGPv:
            raise ValueError("Invalid epsilon value: {}".format(VVqkfbMIOFDgzhOKKnJVcuOffzzrOGPv))
        if not 0.0 <= aGiatFWLVusbPGSDloFtejqscKjAwtLv[0] < 1.0:
            raise ValueError("Invalid beta parameter at index 0: {}".format(aGiatFWLVusbPGSDloFtejqscKjAwtLv[0]))
        if not 0.0 <= aGiatFWLVusbPGSDloFtejqscKjAwtLv[1] < 1.0:
            raise ValueError("Invalid beta parameter at index 1: {}".format(aGiatFWLVusbPGSDloFtejqscKjAwtLv[1]))
        if not 0.0 <= IXIijmgGcHCScFjClwljTOXTswNkiIkK:
            raise ValueError("Invalid weight_decay value: {}".format(IXIijmgGcHCScFjClwljTOXTswNkiIkK))
        if not 0.0 <= bGiLySteHgQEfhoICMWhUyeWhlsZpzRt <= 1.0:
            raise ValueError("Invalid ema_decay value: {}".format(bGiLySteHgQEfhoICMWhUyeWhlsZpzRt))
        fUGzhhpzBvumAHKYDXHkrPjpAiRgKnhT = dict(BbjvYJKNzsfQZuahPgdyaFZrYmxOIhRT=BbjvYJKNzsfQZuahPgdyaFZrYmxOIhRT, aGiatFWLVusbPGSDloFtejqscKjAwtLv=aGiatFWLVusbPGSDloFtejqscKjAwtLv, VVqkfbMIOFDgzhOKKnJVcuOffzzrOGPv=VVqkfbMIOFDgzhOKKnJVcuOffzzrOGPv,
                        IXIijmgGcHCScFjClwljTOXTswNkiIkK=IXIijmgGcHCScFjClwljTOXTswNkiIkK, CYYsnkfcHEJHHedghOjEJLrmJvXYOCpq=CYYsnkfcHEJHHedghOjEJLrmJvXYOCpq, bGiLySteHgQEfhoICMWhUyeWhlsZpzRt=bGiLySteHgQEfhoICMWhUyeWhlsZpzRt,
                        NrlrYzsfxnatCeZgJtAuRDendjKXEJSe=NrlrYzsfxnatCeZgJtAuRDendjKXEJSe, param_names=param_names)
        super().__init__(params, fUGzhhpzBvumAHKYDXHkrPjpAiRgKnhT)
    def __setstate__(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, bPsjVMuBAjrfyzAMRkMvJyUnABuWbsuC):
        super().__setstate__(bPsjVMuBAjrfyzAMRkMvJyUnABuWbsuC)
        for EBSqSRjSGRxQZGLBDNBFhqftXyLrzJTb in rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.param_groups:
            EBSqSRjSGRxQZGLBDNBFhqftXyLrzJTb.setdefault('amsgrad', False)
    @torch.no_grad()
    def UHmIQCHeLkozPfaktIdEHKdpTVYzCLhe(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, closure=None):
        GtnkLyvfmiRPrwSQJfyYiKxybcBdUius = None
        if closure is not None:
            with torch.enable_grad():
                GtnkLyvfmiRPrwSQJfyYiKxybcBdUius = closure()
        for EBSqSRjSGRxQZGLBDNBFhqftXyLrzJTb in rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.param_groups:
            bybhcpArvRzuIwvVHWjzxQjfTIapYOKm = []
            bOFdibOgqCMNbvTQUiuVVicZmEqbrdNB = []
            ZrFREbKujjZSPTrJDDApFqcMQeuOJAYP = []
            fPlNpLiZCjYHHiARCfcJLAztwwrqHqmJ = []
            hjZLKUEttdNnuGCCjpmYMygqEMkYzGfL = []
            JoDiNJsyRroFDjjzJcZmIUbnNJhbtrAh = []
            ErclQDWBdutFEBDpJYbDQnUPbdBRnwXZ = []
            wObOQIGrcWpNHKiKhNlzZIRlVFPkTngy = []
            CYYsnkfcHEJHHedghOjEJLrmJvXYOCpq = EBSqSRjSGRxQZGLBDNBFhqftXyLrzJTb['amsgrad']
            oYseJQnKRrTJdWpDXdxdcssdaXeoymtK, snGqTEACPtQXAwoRnofkmvtqYYLLadiM = EBSqSRjSGRxQZGLBDNBFhqftXyLrzJTb['betas']
            bGiLySteHgQEfhoICMWhUyeWhlsZpzRt = EBSqSRjSGRxQZGLBDNBFhqftXyLrzJTb['ema_decay']
            NrlrYzsfxnatCeZgJtAuRDendjKXEJSe = EBSqSRjSGRxQZGLBDNBFhqftXyLrzJTb['ema_power']
            for HutkrxeXIuRQKOhCWHkiwqLGAsJjUSKj in EBSqSRjSGRxQZGLBDNBFhqftXyLrzJTb['params']:
                if HutkrxeXIuRQKOhCWHkiwqLGAsJjUSKj.grad is None:
                    continue
                bybhcpArvRzuIwvVHWjzxQjfTIapYOKm.append(HutkrxeXIuRQKOhCWHkiwqLGAsJjUSKj)
                if HutkrxeXIuRQKOhCWHkiwqLGAsJjUSKj.grad.is_sparse:
                    raise RuntimeError('AdamW does not support sparse gradients')
                bOFdibOgqCMNbvTQUiuVVicZmEqbrdNB.append(HutkrxeXIuRQKOhCWHkiwqLGAsJjUSKj.grad)
                bPsjVMuBAjrfyzAMRkMvJyUnABuWbsuC = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.bPsjVMuBAjrfyzAMRkMvJyUnABuWbsuC[HutkrxeXIuRQKOhCWHkiwqLGAsJjUSKj]
                if len(bPsjVMuBAjrfyzAMRkMvJyUnABuWbsuC) == 0:
                    bPsjVMuBAjrfyzAMRkMvJyUnABuWbsuC['step'] = 0
                    bPsjVMuBAjrfyzAMRkMvJyUnABuWbsuC['exp_avg'] = torch.zeros_like(HutkrxeXIuRQKOhCWHkiwqLGAsJjUSKj, memory_format=torch.preserve_format)
                    bPsjVMuBAjrfyzAMRkMvJyUnABuWbsuC['exp_avg_sq'] = torch.zeros_like(HutkrxeXIuRQKOhCWHkiwqLGAsJjUSKj, memory_format=torch.preserve_format)
                    if CYYsnkfcHEJHHedghOjEJLrmJvXYOCpq:
                        bPsjVMuBAjrfyzAMRkMvJyUnABuWbsuC['max_exp_avg_sq'] = torch.zeros_like(HutkrxeXIuRQKOhCWHkiwqLGAsJjUSKj, memory_format=torch.preserve_format)
                    bPsjVMuBAjrfyzAMRkMvJyUnABuWbsuC['param_exp_avg'] = HutkrxeXIuRQKOhCWHkiwqLGAsJjUSKj.detach().float().tEcQvpBwXwdqvKxRTLEBROBUyPoodldL()
                ZrFREbKujjZSPTrJDDApFqcMQeuOJAYP.append(bPsjVMuBAjrfyzAMRkMvJyUnABuWbsuC['exp_avg'])
                fPlNpLiZCjYHHiARCfcJLAztwwrqHqmJ.append(bPsjVMuBAjrfyzAMRkMvJyUnABuWbsuC['exp_avg_sq'])
                hjZLKUEttdNnuGCCjpmYMygqEMkYzGfL.append(bPsjVMuBAjrfyzAMRkMvJyUnABuWbsuC['param_exp_avg'])
                if CYYsnkfcHEJHHedghOjEJLrmJvXYOCpq:
                    ErclQDWBdutFEBDpJYbDQnUPbdBRnwXZ.append(bPsjVMuBAjrfyzAMRkMvJyUnABuWbsuC['max_exp_avg_sq'])
                bPsjVMuBAjrfyzAMRkMvJyUnABuWbsuC['step'] += 1
                wObOQIGrcWpNHKiKhNlzZIRlVFPkTngy.append(bPsjVMuBAjrfyzAMRkMvJyUnABuWbsuC['step'])
            optim._functional.adamw(bybhcpArvRzuIwvVHWjzxQjfTIapYOKm,
                    bOFdibOgqCMNbvTQUiuVVicZmEqbrdNB,
                    ZrFREbKujjZSPTrJDDApFqcMQeuOJAYP,
                    fPlNpLiZCjYHHiARCfcJLAztwwrqHqmJ,
                    ErclQDWBdutFEBDpJYbDQnUPbdBRnwXZ,
                    wObOQIGrcWpNHKiKhNlzZIRlVFPkTngy,
                    CYYsnkfcHEJHHedghOjEJLrmJvXYOCpq=CYYsnkfcHEJHHedghOjEJLrmJvXYOCpq,
                    oYseJQnKRrTJdWpDXdxdcssdaXeoymtK=oYseJQnKRrTJdWpDXdxdcssdaXeoymtK,
                    snGqTEACPtQXAwoRnofkmvtqYYLLadiM=snGqTEACPtQXAwoRnofkmvtqYYLLadiM,
                    BbjvYJKNzsfQZuahPgdyaFZrYmxOIhRT=EBSqSRjSGRxQZGLBDNBFhqftXyLrzJTb['lr'],
                    IXIijmgGcHCScFjClwljTOXTswNkiIkK=EBSqSRjSGRxQZGLBDNBFhqftXyLrzJTb['weight_decay'],
                    VVqkfbMIOFDgzhOKKnJVcuOffzzrOGPv=EBSqSRjSGRxQZGLBDNBFhqftXyLrzJTb['eps'],
                    csoiAhSrFEjktbqzvBQFmDenJgChHPAc=False)
            zPyUviprizEpwLutzFZnHQUggdALhEXJ = min(bGiLySteHgQEfhoICMWhUyeWhlsZpzRt, 1 - bPsjVMuBAjrfyzAMRkMvJyUnABuWbsuC['step'] ** -NrlrYzsfxnatCeZgJtAuRDendjKXEJSe)
            for wqONwpPqzusAImUvAyPmoTAxAbxfcvHV, YhvBCQJfNGSjusfvTIxOkaEXefbpyTVW in zip(bybhcpArvRzuIwvVHWjzxQjfTIapYOKm, hjZLKUEttdNnuGCCjpmYMygqEMkYzGfL):
                YhvBCQJfNGSjusfvTIxOkaEXefbpyTVW.mul_(zPyUviprizEpwLutzFZnHQUggdALhEXJ).add_(wqONwpPqzusAImUvAyPmoTAxAbxfcvHV.float(), uigKGapaQVcFiOjEiWwRAHjjkAWxsqck=1 - zPyUviprizEpwLutzFZnHQUggdALhEXJ)
        return loss