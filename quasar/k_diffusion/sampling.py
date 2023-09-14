import math
from scipy import integrate
import torch
from torch import nn
import torchsde
from tqdm.auto import trange, tqdm
from . import utils
def yzfXtlbWultmkvsrGijiuFyhqWQceWau(NECAaWUrFGIXcLimrerEYmxYIykQBfXb):
    return torch.cat([NECAaWUrFGIXcLimrerEYmxYIykQBfXb, NECAaWUrFGIXcLimrerEYmxYIykQBfXb.new_zeros([1])])
def TvpwQRUBaSfOAvxhavXqmWqPsgPQgUoi(zXHJFiFFvWqeQIAxyaTGMUgoRaHrYzjK, FrgHMQrwGwxjLFZFaZndQasXgRhPXZyj, SjuBswrlxdwXAwbvIiTMrngJfAEFYXwe, rho=7., fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc='cpu'):
    CXURldOtbDrlqtwyOXRPAdpXYbntOGUT = torch.linspace(0, 1, zXHJFiFFvWqeQIAxyaTGMUgoRaHrYzjK, fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc=fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc)
    prEhLQZgexCgVJysAYGrbGyTHjWEkGxM = FrgHMQrwGwxjLFZFaZndQasXgRhPXZyj ** (1 / rho)
    VrErRHnHSBFbSXockeOQkfffgOvGkwop = SjuBswrlxdwXAwbvIiTMrngJfAEFYXwe ** (1 / rho)
    ywkdEDhpSPXHYARENdFhpYnCzsLhiORy = (VrErRHnHSBFbSXockeOQkfffgOvGkwop + CXURldOtbDrlqtwyOXRPAdpXYbntOGUT * (prEhLQZgexCgVJysAYGrbGyTHjWEkGxM - VrErRHnHSBFbSXockeOQkfffgOvGkwop)) ** rho
    return yzfXtlbWultmkvsrGijiuFyhqWQceWau(ywkdEDhpSPXHYARENdFhpYnCzsLhiORy).sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ(fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc)
def kZdRKjkrWOFbCmesgdCsylgvVPWpBhfp(zXHJFiFFvWqeQIAxyaTGMUgoRaHrYzjK, FrgHMQrwGwxjLFZFaZndQasXgRhPXZyj, SjuBswrlxdwXAwbvIiTMrngJfAEFYXwe, fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc='cpu'):
    ywkdEDhpSPXHYARENdFhpYnCzsLhiORy = torch.linspace(math.DJwhOGBaLcOjmXnuwXMXOyhMtknqkKXL(SjuBswrlxdwXAwbvIiTMrngJfAEFYXwe), math.DJwhOGBaLcOjmXnuwXMXOyhMtknqkKXL(FrgHMQrwGwxjLFZFaZndQasXgRhPXZyj), zXHJFiFFvWqeQIAxyaTGMUgoRaHrYzjK, fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc=fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc).exp()
    return yzfXtlbWultmkvsrGijiuFyhqWQceWau(ywkdEDhpSPXHYARENdFhpYnCzsLhiORy)
def ycbvozqOJgwREIGJdDouyDrTvoOXuofF(zXHJFiFFvWqeQIAxyaTGMUgoRaHrYzjK, FrgHMQrwGwxjLFZFaZndQasXgRhPXZyj, SjuBswrlxdwXAwbvIiTMrngJfAEFYXwe, rho=1., fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc='cpu'):
    CXURldOtbDrlqtwyOXRPAdpXYbntOGUT = torch.linspace(1, 0, zXHJFiFFvWqeQIAxyaTGMUgoRaHrYzjK, fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc=fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc) ** rho
    ywkdEDhpSPXHYARENdFhpYnCzsLhiORy = torch.exp(CXURldOtbDrlqtwyOXRPAdpXYbntOGUT * (math.DJwhOGBaLcOjmXnuwXMXOyhMtknqkKXL(SjuBswrlxdwXAwbvIiTMrngJfAEFYXwe) - math.DJwhOGBaLcOjmXnuwXMXOyhMtknqkKXL(FrgHMQrwGwxjLFZFaZndQasXgRhPXZyj)) + math.DJwhOGBaLcOjmXnuwXMXOyhMtknqkKXL(FrgHMQrwGwxjLFZFaZndQasXgRhPXZyj))
    return yzfXtlbWultmkvsrGijiuFyhqWQceWau(ywkdEDhpSPXHYARENdFhpYnCzsLhiORy)
def rUvmOjeAZtwfFLESPIWsdHTNvLzklbtn(zXHJFiFFvWqeQIAxyaTGMUgoRaHrYzjK, beta_d=19.9, beta_min=0.1, eps_s=1e-3, fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc='cpu'):
    XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz = torch.linspace(1, eps_s, zXHJFiFFvWqeQIAxyaTGMUgoRaHrYzjK, fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc=fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc)
    ywkdEDhpSPXHYARENdFhpYnCzsLhiORy = torch.sqrt(torch.exp(beta_d * XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz ** 2 / 2 + beta_min * XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz) - 1)
    return yzfXtlbWultmkvsrGijiuFyhqWQceWau(ywkdEDhpSPXHYARENdFhpYnCzsLhiORy)
def wWkWWmmaMWzBivoGthogCOrDaHJcXRQg(NECAaWUrFGIXcLimrerEYmxYIykQBfXb, njuvAJFseAnTpNXMmovFtOzaohoePSQs, ODAZKuAsCnodIahYkmGtylGzWplGUuPD):
    return (NECAaWUrFGIXcLimrerEYmxYIykQBfXb - ODAZKuAsCnodIahYkmGtylGzWplGUuPD) / utils.CMxxOxdPTSrjIzfwUpFYdWOyWfmNnQNF(njuvAJFseAnTpNXMmovFtOzaohoePSQs, NECAaWUrFGIXcLimrerEYmxYIykQBfXb.ndim)
def EQrWJtFJAcWXVjwSXclhNFDOxYkkGfcF(sigma_from, sigma_to, YifKHCfIbeEsuQSFLLpJatOOrlBeQSoO=1.):
    if not YifKHCfIbeEsuQSFLLpJatOOrlBeQSoO:
        return sigma_to, 0.
    jfsUMkPasnZkDrBlHrfavWZhDulLllvc = min(sigma_to, YifKHCfIbeEsuQSFLLpJatOOrlBeQSoO * (sigma_to ** 2 * (sigma_from ** 2 - sigma_to ** 2) / sigma_from ** 2) ** 0.5)
    FEJQVZkfSRZklwwzvlTqxcIUgPGYvkPs = (sigma_to ** 2 - jfsUMkPasnZkDrBlHrfavWZhDulLllvc ** 2) ** 0.5
    return FEJQVZkfSRZklwwzvlTqxcIUgPGYvkPs, jfsUMkPasnZkDrBlHrfavWZhDulLllvc
def IIWZsliZaKlVluovJAtCbQFoHHPJmJDG(NECAaWUrFGIXcLimrerEYmxYIykQBfXb):
    return lambda njuvAJFseAnTpNXMmovFtOzaohoePSQs, sigma_next: torch.randn_like(NECAaWUrFGIXcLimrerEYmxYIykQBfXb)
class ioRBGeZVPXlLSIJciWlohlwLtaxCmFgk:
    def __init__(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, NECAaWUrFGIXcLimrerEYmxYIykQBfXb, WFuXrjgnWyCysWFupUPTADHAPjELsNbG, MStccjMYPXYbPLBRJuuGIaVGkOvnhCnE, qWZgfPzZGdBXrbWzvrSHUmcFFjBFiMVr=None, **kwargs):
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.cpu_tree = True
        if "cpu" in kwargs:
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.cpu_tree = kwargs.pop("cpu")
        WFuXrjgnWyCysWFupUPTADHAPjELsNbG, MStccjMYPXYbPLBRJuuGIaVGkOvnhCnE, rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.HBMNcZPXMGfIKnBsvnouXucWvkUmgWwq = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.sort(WFuXrjgnWyCysWFupUPTADHAPjELsNbG, MStccjMYPXYbPLBRJuuGIaVGkOvnhCnE)
        ynDVQlyZvavwayPPgASoQNtQlVCbisLC = kwargs.get('w0', torch.zeros_like(NECAaWUrFGIXcLimrerEYmxYIykQBfXb))
        if qWZgfPzZGdBXrbWzvrSHUmcFFjBFiMVr is None:
            qWZgfPzZGdBXrbWzvrSHUmcFFjBFiMVr = torch.randint(0, 2 ** 63 - 1, []).ygFiYnqtfEqFJmbillPxtHRxsUoFqqJk()
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.batched = True
        try:
            assert len(qWZgfPzZGdBXrbWzvrSHUmcFFjBFiMVr) == NECAaWUrFGIXcLimrerEYmxYIykQBfXb.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[0]
            ynDVQlyZvavwayPPgASoQNtQlVCbisLC = ynDVQlyZvavwayPPgASoQNtQlVCbisLC[0]
        except TypeError:
            qWZgfPzZGdBXrbWzvrSHUmcFFjBFiMVr = [qWZgfPzZGdBXrbWzvrSHUmcFFjBFiMVr]
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.batched = False
        if rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.cpu_tree:
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.trees = [torchsde.BrownianTree(WFuXrjgnWyCysWFupUPTADHAPjELsNbG.cpu(), ynDVQlyZvavwayPPgASoQNtQlVCbisLC.cpu(), MStccjMYPXYbPLBRJuuGIaVGkOvnhCnE.cpu(), entropy=uPePujIqMVDrwNvZQxJajkuaQFAcacjA, **kwargs) for uPePujIqMVDrwNvZQxJajkuaQFAcacjA in qWZgfPzZGdBXrbWzvrSHUmcFFjBFiMVr]
        else:
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.trees = [torchsde.BrownianTree(WFuXrjgnWyCysWFupUPTADHAPjELsNbG, ynDVQlyZvavwayPPgASoQNtQlVCbisLC, MStccjMYPXYbPLBRJuuGIaVGkOvnhCnE, entropy=uPePujIqMVDrwNvZQxJajkuaQFAcacjA, **kwargs) for uPePujIqMVDrwNvZQxJajkuaQFAcacjA in qWZgfPzZGdBXrbWzvrSHUmcFFjBFiMVr]
    @staticmethod
    def sort(GlZreLQjBCiBptpFgmbsMbhjFlMgPVav, b):
        return (GlZreLQjBCiBptpFgmbsMbhjFlMgPVav, b, 1) if GlZreLQjBCiBptpFgmbsMbhjFlMgPVav < b else (b, GlZreLQjBCiBptpFgmbsMbhjFlMgPVav, -1)
    def __call__(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, WFuXrjgnWyCysWFupUPTADHAPjELsNbG, MStccjMYPXYbPLBRJuuGIaVGkOvnhCnE):
        WFuXrjgnWyCysWFupUPTADHAPjELsNbG, MStccjMYPXYbPLBRJuuGIaVGkOvnhCnE, HBMNcZPXMGfIKnBsvnouXucWvkUmgWwq = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.sort(WFuXrjgnWyCysWFupUPTADHAPjELsNbG, MStccjMYPXYbPLBRJuuGIaVGkOvnhCnE)
        if rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.cpu_tree:
            AeIrbRXDkpZlClJGwzMknCltTQQdmhvu = torch.stack([QsZEAmfflOadhVePZXNfHzYmVeuBjJin(WFuXrjgnWyCysWFupUPTADHAPjELsNbG.cpu().float(), MStccjMYPXYbPLBRJuuGIaVGkOvnhCnE.cpu().float()).sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ(WFuXrjgnWyCysWFupUPTADHAPjELsNbG.DDRQlhrNSGpwTrokWitkZipdfbAqBFxv).sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ(WFuXrjgnWyCysWFupUPTADHAPjELsNbG.fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc) for QsZEAmfflOadhVePZXNfHzYmVeuBjJin in rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.trees]) * (rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.HBMNcZPXMGfIKnBsvnouXucWvkUmgWwq * HBMNcZPXMGfIKnBsvnouXucWvkUmgWwq)
        else:
            AeIrbRXDkpZlClJGwzMknCltTQQdmhvu = torch.stack([QsZEAmfflOadhVePZXNfHzYmVeuBjJin(WFuXrjgnWyCysWFupUPTADHAPjELsNbG, MStccjMYPXYbPLBRJuuGIaVGkOvnhCnE) for QsZEAmfflOadhVePZXNfHzYmVeuBjJin in rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.trees]) * (rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.HBMNcZPXMGfIKnBsvnouXucWvkUmgWwq * HBMNcZPXMGfIKnBsvnouXucWvkUmgWwq)
        return AeIrbRXDkpZlClJGwzMknCltTQQdmhvu if rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.batched else AeIrbRXDkpZlClJGwzMknCltTQQdmhvu[0]
class NKEocvhZhGGzDdsiFFqWYmrsPdkyJdwN:
    def __init__(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, NECAaWUrFGIXcLimrerEYmxYIykQBfXb, FrgHMQrwGwxjLFZFaZndQasXgRhPXZyj, SjuBswrlxdwXAwbvIiTMrngJfAEFYXwe, qWZgfPzZGdBXrbWzvrSHUmcFFjBFiMVr=None, transform=lambda NECAaWUrFGIXcLimrerEYmxYIykQBfXb: NECAaWUrFGIXcLimrerEYmxYIykQBfXb, cpu=False):
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.transform = transform
        WFuXrjgnWyCysWFupUPTADHAPjELsNbG, MStccjMYPXYbPLBRJuuGIaVGkOvnhCnE = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.transform(torch.as_tensor(FrgHMQrwGwxjLFZFaZndQasXgRhPXZyj)), rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.transform(torch.as_tensor(SjuBswrlxdwXAwbvIiTMrngJfAEFYXwe))
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.QsZEAmfflOadhVePZXNfHzYmVeuBjJin = ioRBGeZVPXlLSIJciWlohlwLtaxCmFgk(NECAaWUrFGIXcLimrerEYmxYIykQBfXb, WFuXrjgnWyCysWFupUPTADHAPjELsNbG, MStccjMYPXYbPLBRJuuGIaVGkOvnhCnE, qWZgfPzZGdBXrbWzvrSHUmcFFjBFiMVr, cpu=cpu)
    def __call__(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, njuvAJFseAnTpNXMmovFtOzaohoePSQs, sigma_next):
        WFuXrjgnWyCysWFupUPTADHAPjELsNbG, MStccjMYPXYbPLBRJuuGIaVGkOvnhCnE = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.transform(torch.as_tensor(njuvAJFseAnTpNXMmovFtOzaohoePSQs)), rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.transform(torch.as_tensor(sigma_next))
        return rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.QsZEAmfflOadhVePZXNfHzYmVeuBjJin(WFuXrjgnWyCysWFupUPTADHAPjELsNbG, MStccjMYPXYbPLBRJuuGIaVGkOvnhCnE) / (MStccjMYPXYbPLBRJuuGIaVGkOvnhCnE - WFuXrjgnWyCysWFupUPTADHAPjELsNbG).abs().sqrt()
@torch.no_grad()
def PuAgvJfRmvFlidRHqKvHBEoHrWNmVjiR(VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM, NECAaWUrFGIXcLimrerEYmxYIykQBfXb, ywkdEDhpSPXHYARENdFhpYnCzsLhiORy, TlJxtGydipTPezrPlUrxTKACQdhKNgvw=None, FJsaFpOBdvpFlEdxOzBgjwcWBUfetQGF=None, disable=None, s_churn=0., s_tmin=0., s_tmax=float('inf'), s_noise=1.):
    TlJxtGydipTPezrPlUrxTKACQdhKNgvw = {} if TlJxtGydipTPezrPlUrxTKACQdhKNgvw is None else TlJxtGydipTPezrPlUrxTKACQdhKNgvw
    moQRitRqIYEATNnahksUxyKeQfVQohNA = NECAaWUrFGIXcLimrerEYmxYIykQBfXb.new_ones([NECAaWUrFGIXcLimrerEYmxYIykQBfXb.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[0]])
    for HCXmerBqIMuTscBONzTGKYapYSxWTYHo in trange(len(ywkdEDhpSPXHYARENdFhpYnCzsLhiORy) - 1, disable=disable):
        bGXhNdiqkuBftSpmdmGnluqLPlFxVFXz = min(s_churn / (len(ywkdEDhpSPXHYARENdFhpYnCzsLhiORy) - 1), 2 ** 0.5 - 1) if s_tmin <= ywkdEDhpSPXHYARENdFhpYnCzsLhiORy[HCXmerBqIMuTscBONzTGKYapYSxWTYHo] <= s_tmax else 0.
        CAWDKXGBXpOWdbjQrpDTbrPyowjCdaIn = ywkdEDhpSPXHYARENdFhpYnCzsLhiORy[HCXmerBqIMuTscBONzTGKYapYSxWTYHo] * (bGXhNdiqkuBftSpmdmGnluqLPlFxVFXz + 1)
        if bGXhNdiqkuBftSpmdmGnluqLPlFxVFXz > 0:
            VVqkfbMIOFDgzhOKKnJVcuOffzzrOGPv = torch.randn_like(NECAaWUrFGIXcLimrerEYmxYIykQBfXb) * s_noise
            NECAaWUrFGIXcLimrerEYmxYIykQBfXb = NECAaWUrFGIXcLimrerEYmxYIykQBfXb + VVqkfbMIOFDgzhOKKnJVcuOffzzrOGPv * (CAWDKXGBXpOWdbjQrpDTbrPyowjCdaIn ** 2 - ywkdEDhpSPXHYARENdFhpYnCzsLhiORy[HCXmerBqIMuTscBONzTGKYapYSxWTYHo] ** 2) ** 0.5
        ODAZKuAsCnodIahYkmGtylGzWplGUuPD = VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM(NECAaWUrFGIXcLimrerEYmxYIykQBfXb, CAWDKXGBXpOWdbjQrpDTbrPyowjCdaIn * moQRitRqIYEATNnahksUxyKeQfVQohNA, **TlJxtGydipTPezrPlUrxTKACQdhKNgvw)
        TXGwYXNLgQsYzfHHpRBDJGFCFZEClzIo = wWkWWmmaMWzBivoGthogCOrDaHJcXRQg(NECAaWUrFGIXcLimrerEYmxYIykQBfXb, CAWDKXGBXpOWdbjQrpDTbrPyowjCdaIn, ODAZKuAsCnodIahYkmGtylGzWplGUuPD)
        if FJsaFpOBdvpFlEdxOzBgjwcWBUfetQGF is not None:
            FJsaFpOBdvpFlEdxOzBgjwcWBUfetQGF({'x': NECAaWUrFGIXcLimrerEYmxYIykQBfXb, 'i': HCXmerBqIMuTscBONzTGKYapYSxWTYHo, 'sigma': ywkdEDhpSPXHYARENdFhpYnCzsLhiORy[HCXmerBqIMuTscBONzTGKYapYSxWTYHo], 'sigma_hat': CAWDKXGBXpOWdbjQrpDTbrPyowjCdaIn, 'denoised': ODAZKuAsCnodIahYkmGtylGzWplGUuPD})
        rYtAWlTfuJKXWhYOjYFOlRbQzowyoxFG = ywkdEDhpSPXHYARENdFhpYnCzsLhiORy[HCXmerBqIMuTscBONzTGKYapYSxWTYHo + 1] - CAWDKXGBXpOWdbjQrpDTbrPyowjCdaIn
        NECAaWUrFGIXcLimrerEYmxYIykQBfXb = NECAaWUrFGIXcLimrerEYmxYIykQBfXb + TXGwYXNLgQsYzfHHpRBDJGFCFZEClzIo * rYtAWlTfuJKXWhYOjYFOlRbQzowyoxFG
    return NECAaWUrFGIXcLimrerEYmxYIykQBfXb
@torch.no_grad()
def SQPTsGeeXwABUFqJMVihgEHyuTpiYIUo(VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM, NECAaWUrFGIXcLimrerEYmxYIykQBfXb, ywkdEDhpSPXHYARENdFhpYnCzsLhiORy, TlJxtGydipTPezrPlUrxTKACQdhKNgvw=None, FJsaFpOBdvpFlEdxOzBgjwcWBUfetQGF=None, disable=None, YifKHCfIbeEsuQSFLLpJatOOrlBeQSoO=1., s_noise=1., ubyoEoHoKfVYweiaMPbKnyuENzoZHLei=None):
    TlJxtGydipTPezrPlUrxTKACQdhKNgvw = {} if TlJxtGydipTPezrPlUrxTKACQdhKNgvw is None else TlJxtGydipTPezrPlUrxTKACQdhKNgvw
    ubyoEoHoKfVYweiaMPbKnyuENzoZHLei = IIWZsliZaKlVluovJAtCbQFoHHPJmJDG(NECAaWUrFGIXcLimrerEYmxYIykQBfXb) if ubyoEoHoKfVYweiaMPbKnyuENzoZHLei is None else ubyoEoHoKfVYweiaMPbKnyuENzoZHLei
    moQRitRqIYEATNnahksUxyKeQfVQohNA = NECAaWUrFGIXcLimrerEYmxYIykQBfXb.new_ones([NECAaWUrFGIXcLimrerEYmxYIykQBfXb.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[0]])
    for HCXmerBqIMuTscBONzTGKYapYSxWTYHo in trange(len(ywkdEDhpSPXHYARENdFhpYnCzsLhiORy) - 1, disable=disable):
        ODAZKuAsCnodIahYkmGtylGzWplGUuPD = VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM(NECAaWUrFGIXcLimrerEYmxYIykQBfXb, ywkdEDhpSPXHYARENdFhpYnCzsLhiORy[HCXmerBqIMuTscBONzTGKYapYSxWTYHo] * moQRitRqIYEATNnahksUxyKeQfVQohNA, **TlJxtGydipTPezrPlUrxTKACQdhKNgvw)
        FEJQVZkfSRZklwwzvlTqxcIUgPGYvkPs, jfsUMkPasnZkDrBlHrfavWZhDulLllvc = EQrWJtFJAcWXVjwSXclhNFDOxYkkGfcF(ywkdEDhpSPXHYARENdFhpYnCzsLhiORy[HCXmerBqIMuTscBONzTGKYapYSxWTYHo], ywkdEDhpSPXHYARENdFhpYnCzsLhiORy[HCXmerBqIMuTscBONzTGKYapYSxWTYHo + 1], YifKHCfIbeEsuQSFLLpJatOOrlBeQSoO=YifKHCfIbeEsuQSFLLpJatOOrlBeQSoO)
        if FJsaFpOBdvpFlEdxOzBgjwcWBUfetQGF is not None:
            FJsaFpOBdvpFlEdxOzBgjwcWBUfetQGF({'x': NECAaWUrFGIXcLimrerEYmxYIykQBfXb, 'i': HCXmerBqIMuTscBONzTGKYapYSxWTYHo, 'sigma': ywkdEDhpSPXHYARENdFhpYnCzsLhiORy[HCXmerBqIMuTscBONzTGKYapYSxWTYHo], 'sigma_hat': ywkdEDhpSPXHYARENdFhpYnCzsLhiORy[HCXmerBqIMuTscBONzTGKYapYSxWTYHo], 'denoised': ODAZKuAsCnodIahYkmGtylGzWplGUuPD})
        TXGwYXNLgQsYzfHHpRBDJGFCFZEClzIo = wWkWWmmaMWzBivoGthogCOrDaHJcXRQg(NECAaWUrFGIXcLimrerEYmxYIykQBfXb, ywkdEDhpSPXHYARENdFhpYnCzsLhiORy[HCXmerBqIMuTscBONzTGKYapYSxWTYHo], ODAZKuAsCnodIahYkmGtylGzWplGUuPD)
        rYtAWlTfuJKXWhYOjYFOlRbQzowyoxFG = FEJQVZkfSRZklwwzvlTqxcIUgPGYvkPs - ywkdEDhpSPXHYARENdFhpYnCzsLhiORy[HCXmerBqIMuTscBONzTGKYapYSxWTYHo]
        NECAaWUrFGIXcLimrerEYmxYIykQBfXb = NECAaWUrFGIXcLimrerEYmxYIykQBfXb + TXGwYXNLgQsYzfHHpRBDJGFCFZEClzIo * rYtAWlTfuJKXWhYOjYFOlRbQzowyoxFG
        if ywkdEDhpSPXHYARENdFhpYnCzsLhiORy[HCXmerBqIMuTscBONzTGKYapYSxWTYHo + 1] > 0:
            NECAaWUrFGIXcLimrerEYmxYIykQBfXb = NECAaWUrFGIXcLimrerEYmxYIykQBfXb + ubyoEoHoKfVYweiaMPbKnyuENzoZHLei(ywkdEDhpSPXHYARENdFhpYnCzsLhiORy[HCXmerBqIMuTscBONzTGKYapYSxWTYHo], ywkdEDhpSPXHYARENdFhpYnCzsLhiORy[HCXmerBqIMuTscBONzTGKYapYSxWTYHo + 1]) * s_noise * jfsUMkPasnZkDrBlHrfavWZhDulLllvc
    return NECAaWUrFGIXcLimrerEYmxYIykQBfXb
@torch.no_grad()
def oDLEZdqtdUxCVvBkOgnAmKbPeSQUHsAY(VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM, NECAaWUrFGIXcLimrerEYmxYIykQBfXb, ywkdEDhpSPXHYARENdFhpYnCzsLhiORy, TlJxtGydipTPezrPlUrxTKACQdhKNgvw=None, FJsaFpOBdvpFlEdxOzBgjwcWBUfetQGF=None, disable=None, s_churn=0., s_tmin=0., s_tmax=float('inf'), s_noise=1.):
    TlJxtGydipTPezrPlUrxTKACQdhKNgvw = {} if TlJxtGydipTPezrPlUrxTKACQdhKNgvw is None else TlJxtGydipTPezrPlUrxTKACQdhKNgvw
    moQRitRqIYEATNnahksUxyKeQfVQohNA = NECAaWUrFGIXcLimrerEYmxYIykQBfXb.new_ones([NECAaWUrFGIXcLimrerEYmxYIykQBfXb.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[0]])
    for HCXmerBqIMuTscBONzTGKYapYSxWTYHo in trange(len(ywkdEDhpSPXHYARENdFhpYnCzsLhiORy) - 1, disable=disable):
        bGXhNdiqkuBftSpmdmGnluqLPlFxVFXz = min(s_churn / (len(ywkdEDhpSPXHYARENdFhpYnCzsLhiORy) - 1), 2 ** 0.5 - 1) if s_tmin <= ywkdEDhpSPXHYARENdFhpYnCzsLhiORy[HCXmerBqIMuTscBONzTGKYapYSxWTYHo] <= s_tmax else 0.
        CAWDKXGBXpOWdbjQrpDTbrPyowjCdaIn = ywkdEDhpSPXHYARENdFhpYnCzsLhiORy[HCXmerBqIMuTscBONzTGKYapYSxWTYHo] * (bGXhNdiqkuBftSpmdmGnluqLPlFxVFXz + 1)
        if bGXhNdiqkuBftSpmdmGnluqLPlFxVFXz > 0:
            VVqkfbMIOFDgzhOKKnJVcuOffzzrOGPv = torch.randn_like(NECAaWUrFGIXcLimrerEYmxYIykQBfXb) * s_noise
            NECAaWUrFGIXcLimrerEYmxYIykQBfXb = NECAaWUrFGIXcLimrerEYmxYIykQBfXb + VVqkfbMIOFDgzhOKKnJVcuOffzzrOGPv * (CAWDKXGBXpOWdbjQrpDTbrPyowjCdaIn ** 2 - ywkdEDhpSPXHYARENdFhpYnCzsLhiORy[HCXmerBqIMuTscBONzTGKYapYSxWTYHo] ** 2) ** 0.5
        ODAZKuAsCnodIahYkmGtylGzWplGUuPD = VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM(NECAaWUrFGIXcLimrerEYmxYIykQBfXb, CAWDKXGBXpOWdbjQrpDTbrPyowjCdaIn * moQRitRqIYEATNnahksUxyKeQfVQohNA, **TlJxtGydipTPezrPlUrxTKACQdhKNgvw)
        TXGwYXNLgQsYzfHHpRBDJGFCFZEClzIo = wWkWWmmaMWzBivoGthogCOrDaHJcXRQg(NECAaWUrFGIXcLimrerEYmxYIykQBfXb, CAWDKXGBXpOWdbjQrpDTbrPyowjCdaIn, ODAZKuAsCnodIahYkmGtylGzWplGUuPD)
        if FJsaFpOBdvpFlEdxOzBgjwcWBUfetQGF is not None:
            FJsaFpOBdvpFlEdxOzBgjwcWBUfetQGF({'x': NECAaWUrFGIXcLimrerEYmxYIykQBfXb, 'i': HCXmerBqIMuTscBONzTGKYapYSxWTYHo, 'sigma': ywkdEDhpSPXHYARENdFhpYnCzsLhiORy[HCXmerBqIMuTscBONzTGKYapYSxWTYHo], 'sigma_hat': CAWDKXGBXpOWdbjQrpDTbrPyowjCdaIn, 'denoised': ODAZKuAsCnodIahYkmGtylGzWplGUuPD})
        rYtAWlTfuJKXWhYOjYFOlRbQzowyoxFG = ywkdEDhpSPXHYARENdFhpYnCzsLhiORy[HCXmerBqIMuTscBONzTGKYapYSxWTYHo + 1] - CAWDKXGBXpOWdbjQrpDTbrPyowjCdaIn
        if ywkdEDhpSPXHYARENdFhpYnCzsLhiORy[HCXmerBqIMuTscBONzTGKYapYSxWTYHo + 1] == 0:
            NECAaWUrFGIXcLimrerEYmxYIykQBfXb = NECAaWUrFGIXcLimrerEYmxYIykQBfXb + TXGwYXNLgQsYzfHHpRBDJGFCFZEClzIo * rYtAWlTfuJKXWhYOjYFOlRbQzowyoxFG
        else:
            kFbeKlGwETjnrOUnINvTygvTLgayPoOr = NECAaWUrFGIXcLimrerEYmxYIykQBfXb + TXGwYXNLgQsYzfHHpRBDJGFCFZEClzIo * rYtAWlTfuJKXWhYOjYFOlRbQzowyoxFG
            BcIfZkiygxWOtTynEqPPtsxtqUsZCGOr = VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM(kFbeKlGwETjnrOUnINvTygvTLgayPoOr, ywkdEDhpSPXHYARENdFhpYnCzsLhiORy[HCXmerBqIMuTscBONzTGKYapYSxWTYHo + 1] * moQRitRqIYEATNnahksUxyKeQfVQohNA, **TlJxtGydipTPezrPlUrxTKACQdhKNgvw)
            FuAUWHkMfOeTSBLwrSFWPYoaINWdNNuS = wWkWWmmaMWzBivoGthogCOrDaHJcXRQg(kFbeKlGwETjnrOUnINvTygvTLgayPoOr, ywkdEDhpSPXHYARENdFhpYnCzsLhiORy[HCXmerBqIMuTscBONzTGKYapYSxWTYHo + 1], BcIfZkiygxWOtTynEqPPtsxtqUsZCGOr)
            MuSoyWCWnTgQTlACEFqeERUJEMYSXsqG = (TXGwYXNLgQsYzfHHpRBDJGFCFZEClzIo + FuAUWHkMfOeTSBLwrSFWPYoaINWdNNuS) / 2
            NECAaWUrFGIXcLimrerEYmxYIykQBfXb = NECAaWUrFGIXcLimrerEYmxYIykQBfXb + MuSoyWCWnTgQTlACEFqeERUJEMYSXsqG * rYtAWlTfuJKXWhYOjYFOlRbQzowyoxFG
    return NECAaWUrFGIXcLimrerEYmxYIykQBfXb
@torch.no_grad()
def jbTLkXhMkVoqNMkBmVuXgtBIfDUQzwLK(VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM, NECAaWUrFGIXcLimrerEYmxYIykQBfXb, ywkdEDhpSPXHYARENdFhpYnCzsLhiORy, TlJxtGydipTPezrPlUrxTKACQdhKNgvw=None, FJsaFpOBdvpFlEdxOzBgjwcWBUfetQGF=None, disable=None, s_churn=0., s_tmin=0., s_tmax=float('inf'), s_noise=1.):
    TlJxtGydipTPezrPlUrxTKACQdhKNgvw = {} if TlJxtGydipTPezrPlUrxTKACQdhKNgvw is None else TlJxtGydipTPezrPlUrxTKACQdhKNgvw
    moQRitRqIYEATNnahksUxyKeQfVQohNA = NECAaWUrFGIXcLimrerEYmxYIykQBfXb.new_ones([NECAaWUrFGIXcLimrerEYmxYIykQBfXb.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[0]])
    for HCXmerBqIMuTscBONzTGKYapYSxWTYHo in trange(len(ywkdEDhpSPXHYARENdFhpYnCzsLhiORy) - 1, disable=disable):
        bGXhNdiqkuBftSpmdmGnluqLPlFxVFXz = min(s_churn / (len(ywkdEDhpSPXHYARENdFhpYnCzsLhiORy) - 1), 2 ** 0.5 - 1) if s_tmin <= ywkdEDhpSPXHYARENdFhpYnCzsLhiORy[HCXmerBqIMuTscBONzTGKYapYSxWTYHo] <= s_tmax else 0.
        CAWDKXGBXpOWdbjQrpDTbrPyowjCdaIn = ywkdEDhpSPXHYARENdFhpYnCzsLhiORy[HCXmerBqIMuTscBONzTGKYapYSxWTYHo] * (bGXhNdiqkuBftSpmdmGnluqLPlFxVFXz + 1)
        if bGXhNdiqkuBftSpmdmGnluqLPlFxVFXz > 0:
            VVqkfbMIOFDgzhOKKnJVcuOffzzrOGPv = torch.randn_like(NECAaWUrFGIXcLimrerEYmxYIykQBfXb) * s_noise
            NECAaWUrFGIXcLimrerEYmxYIykQBfXb = NECAaWUrFGIXcLimrerEYmxYIykQBfXb + VVqkfbMIOFDgzhOKKnJVcuOffzzrOGPv * (CAWDKXGBXpOWdbjQrpDTbrPyowjCdaIn ** 2 - ywkdEDhpSPXHYARENdFhpYnCzsLhiORy[HCXmerBqIMuTscBONzTGKYapYSxWTYHo] ** 2) ** 0.5
        ODAZKuAsCnodIahYkmGtylGzWplGUuPD = VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM(NECAaWUrFGIXcLimrerEYmxYIykQBfXb, CAWDKXGBXpOWdbjQrpDTbrPyowjCdaIn * moQRitRqIYEATNnahksUxyKeQfVQohNA, **TlJxtGydipTPezrPlUrxTKACQdhKNgvw)
        TXGwYXNLgQsYzfHHpRBDJGFCFZEClzIo = wWkWWmmaMWzBivoGthogCOrDaHJcXRQg(NECAaWUrFGIXcLimrerEYmxYIykQBfXb, CAWDKXGBXpOWdbjQrpDTbrPyowjCdaIn, ODAZKuAsCnodIahYkmGtylGzWplGUuPD)
        if FJsaFpOBdvpFlEdxOzBgjwcWBUfetQGF is not None:
            FJsaFpOBdvpFlEdxOzBgjwcWBUfetQGF({'x': NECAaWUrFGIXcLimrerEYmxYIykQBfXb, 'i': HCXmerBqIMuTscBONzTGKYapYSxWTYHo, 'sigma': ywkdEDhpSPXHYARENdFhpYnCzsLhiORy[HCXmerBqIMuTscBONzTGKYapYSxWTYHo], 'sigma_hat': CAWDKXGBXpOWdbjQrpDTbrPyowjCdaIn, 'denoised': ODAZKuAsCnodIahYkmGtylGzWplGUuPD})
        if ywkdEDhpSPXHYARENdFhpYnCzsLhiORy[HCXmerBqIMuTscBONzTGKYapYSxWTYHo + 1] == 0:
            rYtAWlTfuJKXWhYOjYFOlRbQzowyoxFG = ywkdEDhpSPXHYARENdFhpYnCzsLhiORy[HCXmerBqIMuTscBONzTGKYapYSxWTYHo + 1] - CAWDKXGBXpOWdbjQrpDTbrPyowjCdaIn
            NECAaWUrFGIXcLimrerEYmxYIykQBfXb = NECAaWUrFGIXcLimrerEYmxYIykQBfXb + TXGwYXNLgQsYzfHHpRBDJGFCFZEClzIo * rYtAWlTfuJKXWhYOjYFOlRbQzowyoxFG
        else:
            sahmwjoyHOScdLmiUoocJhfMmYjSxaJw = CAWDKXGBXpOWdbjQrpDTbrPyowjCdaIn.DJwhOGBaLcOjmXnuwXMXOyhMtknqkKXL().lerp(ywkdEDhpSPXHYARENdFhpYnCzsLhiORy[HCXmerBqIMuTscBONzTGKYapYSxWTYHo + 1].DJwhOGBaLcOjmXnuwXMXOyhMtknqkKXL(), 0.5).exp()
            mYbwFoBzIzNaKtZLNPrZfYAiiXtKgqCB = sahmwjoyHOScdLmiUoocJhfMmYjSxaJw - CAWDKXGBXpOWdbjQrpDTbrPyowjCdaIn
            sarzybouETpGLDMDvAKZxFsvbnqCanvR = ywkdEDhpSPXHYARENdFhpYnCzsLhiORy[HCXmerBqIMuTscBONzTGKYapYSxWTYHo + 1] - CAWDKXGBXpOWdbjQrpDTbrPyowjCdaIn
            kFbeKlGwETjnrOUnINvTygvTLgayPoOr = NECAaWUrFGIXcLimrerEYmxYIykQBfXb + TXGwYXNLgQsYzfHHpRBDJGFCFZEClzIo * mYbwFoBzIzNaKtZLNPrZfYAiiXtKgqCB
            BcIfZkiygxWOtTynEqPPtsxtqUsZCGOr = VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM(kFbeKlGwETjnrOUnINvTygvTLgayPoOr, sahmwjoyHOScdLmiUoocJhfMmYjSxaJw * moQRitRqIYEATNnahksUxyKeQfVQohNA, **TlJxtGydipTPezrPlUrxTKACQdhKNgvw)
            FuAUWHkMfOeTSBLwrSFWPYoaINWdNNuS = wWkWWmmaMWzBivoGthogCOrDaHJcXRQg(kFbeKlGwETjnrOUnINvTygvTLgayPoOr, sahmwjoyHOScdLmiUoocJhfMmYjSxaJw, BcIfZkiygxWOtTynEqPPtsxtqUsZCGOr)
            NECAaWUrFGIXcLimrerEYmxYIykQBfXb = NECAaWUrFGIXcLimrerEYmxYIykQBfXb + FuAUWHkMfOeTSBLwrSFWPYoaINWdNNuS * sarzybouETpGLDMDvAKZxFsvbnqCanvR
    return NECAaWUrFGIXcLimrerEYmxYIykQBfXb
@torch.no_grad()
def OwSxHXEpwAmJifuVJnvsHyagIcNmBqVk(VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM, NECAaWUrFGIXcLimrerEYmxYIykQBfXb, ywkdEDhpSPXHYARENdFhpYnCzsLhiORy, TlJxtGydipTPezrPlUrxTKACQdhKNgvw=None, FJsaFpOBdvpFlEdxOzBgjwcWBUfetQGF=None, disable=None, YifKHCfIbeEsuQSFLLpJatOOrlBeQSoO=1., s_noise=1., ubyoEoHoKfVYweiaMPbKnyuENzoZHLei=None):
    TlJxtGydipTPezrPlUrxTKACQdhKNgvw = {} if TlJxtGydipTPezrPlUrxTKACQdhKNgvw is None else TlJxtGydipTPezrPlUrxTKACQdhKNgvw
    ubyoEoHoKfVYweiaMPbKnyuENzoZHLei = IIWZsliZaKlVluovJAtCbQFoHHPJmJDG(NECAaWUrFGIXcLimrerEYmxYIykQBfXb) if ubyoEoHoKfVYweiaMPbKnyuENzoZHLei is None else ubyoEoHoKfVYweiaMPbKnyuENzoZHLei
    moQRitRqIYEATNnahksUxyKeQfVQohNA = NECAaWUrFGIXcLimrerEYmxYIykQBfXb.new_ones([NECAaWUrFGIXcLimrerEYmxYIykQBfXb.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[0]])
    for HCXmerBqIMuTscBONzTGKYapYSxWTYHo in trange(len(ywkdEDhpSPXHYARENdFhpYnCzsLhiORy) - 1, disable=disable):
        ODAZKuAsCnodIahYkmGtylGzWplGUuPD = VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM(NECAaWUrFGIXcLimrerEYmxYIykQBfXb, ywkdEDhpSPXHYARENdFhpYnCzsLhiORy[HCXmerBqIMuTscBONzTGKYapYSxWTYHo] * moQRitRqIYEATNnahksUxyKeQfVQohNA, **TlJxtGydipTPezrPlUrxTKACQdhKNgvw)
        FEJQVZkfSRZklwwzvlTqxcIUgPGYvkPs, jfsUMkPasnZkDrBlHrfavWZhDulLllvc = EQrWJtFJAcWXVjwSXclhNFDOxYkkGfcF(ywkdEDhpSPXHYARENdFhpYnCzsLhiORy[HCXmerBqIMuTscBONzTGKYapYSxWTYHo], ywkdEDhpSPXHYARENdFhpYnCzsLhiORy[HCXmerBqIMuTscBONzTGKYapYSxWTYHo + 1], YifKHCfIbeEsuQSFLLpJatOOrlBeQSoO=YifKHCfIbeEsuQSFLLpJatOOrlBeQSoO)
        if FJsaFpOBdvpFlEdxOzBgjwcWBUfetQGF is not None:
            FJsaFpOBdvpFlEdxOzBgjwcWBUfetQGF({'x': NECAaWUrFGIXcLimrerEYmxYIykQBfXb, 'i': HCXmerBqIMuTscBONzTGKYapYSxWTYHo, 'sigma': ywkdEDhpSPXHYARENdFhpYnCzsLhiORy[HCXmerBqIMuTscBONzTGKYapYSxWTYHo], 'sigma_hat': ywkdEDhpSPXHYARENdFhpYnCzsLhiORy[HCXmerBqIMuTscBONzTGKYapYSxWTYHo], 'denoised': ODAZKuAsCnodIahYkmGtylGzWplGUuPD})
        TXGwYXNLgQsYzfHHpRBDJGFCFZEClzIo = wWkWWmmaMWzBivoGthogCOrDaHJcXRQg(NECAaWUrFGIXcLimrerEYmxYIykQBfXb, ywkdEDhpSPXHYARENdFhpYnCzsLhiORy[HCXmerBqIMuTscBONzTGKYapYSxWTYHo], ODAZKuAsCnodIahYkmGtylGzWplGUuPD)
        if FEJQVZkfSRZklwwzvlTqxcIUgPGYvkPs == 0:
            rYtAWlTfuJKXWhYOjYFOlRbQzowyoxFG = FEJQVZkfSRZklwwzvlTqxcIUgPGYvkPs - ywkdEDhpSPXHYARENdFhpYnCzsLhiORy[HCXmerBqIMuTscBONzTGKYapYSxWTYHo]
            NECAaWUrFGIXcLimrerEYmxYIykQBfXb = NECAaWUrFGIXcLimrerEYmxYIykQBfXb + TXGwYXNLgQsYzfHHpRBDJGFCFZEClzIo * rYtAWlTfuJKXWhYOjYFOlRbQzowyoxFG
        else:
            sahmwjoyHOScdLmiUoocJhfMmYjSxaJw = ywkdEDhpSPXHYARENdFhpYnCzsLhiORy[HCXmerBqIMuTscBONzTGKYapYSxWTYHo].DJwhOGBaLcOjmXnuwXMXOyhMtknqkKXL().lerp(FEJQVZkfSRZklwwzvlTqxcIUgPGYvkPs.DJwhOGBaLcOjmXnuwXMXOyhMtknqkKXL(), 0.5).exp()
            mYbwFoBzIzNaKtZLNPrZfYAiiXtKgqCB = sahmwjoyHOScdLmiUoocJhfMmYjSxaJw - ywkdEDhpSPXHYARENdFhpYnCzsLhiORy[HCXmerBqIMuTscBONzTGKYapYSxWTYHo]
            sarzybouETpGLDMDvAKZxFsvbnqCanvR = FEJQVZkfSRZklwwzvlTqxcIUgPGYvkPs - ywkdEDhpSPXHYARENdFhpYnCzsLhiORy[HCXmerBqIMuTscBONzTGKYapYSxWTYHo]
            kFbeKlGwETjnrOUnINvTygvTLgayPoOr = NECAaWUrFGIXcLimrerEYmxYIykQBfXb + TXGwYXNLgQsYzfHHpRBDJGFCFZEClzIo * mYbwFoBzIzNaKtZLNPrZfYAiiXtKgqCB
            BcIfZkiygxWOtTynEqPPtsxtqUsZCGOr = VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM(kFbeKlGwETjnrOUnINvTygvTLgayPoOr, sahmwjoyHOScdLmiUoocJhfMmYjSxaJw * moQRitRqIYEATNnahksUxyKeQfVQohNA, **TlJxtGydipTPezrPlUrxTKACQdhKNgvw)
            FuAUWHkMfOeTSBLwrSFWPYoaINWdNNuS = wWkWWmmaMWzBivoGthogCOrDaHJcXRQg(kFbeKlGwETjnrOUnINvTygvTLgayPoOr, sahmwjoyHOScdLmiUoocJhfMmYjSxaJw, BcIfZkiygxWOtTynEqPPtsxtqUsZCGOr)
            NECAaWUrFGIXcLimrerEYmxYIykQBfXb = NECAaWUrFGIXcLimrerEYmxYIykQBfXb + FuAUWHkMfOeTSBLwrSFWPYoaINWdNNuS * sarzybouETpGLDMDvAKZxFsvbnqCanvR
            NECAaWUrFGIXcLimrerEYmxYIykQBfXb = NECAaWUrFGIXcLimrerEYmxYIykQBfXb + ubyoEoHoKfVYweiaMPbKnyuENzoZHLei(ywkdEDhpSPXHYARENdFhpYnCzsLhiORy[HCXmerBqIMuTscBONzTGKYapYSxWTYHo], ywkdEDhpSPXHYARENdFhpYnCzsLhiORy[HCXmerBqIMuTscBONzTGKYapYSxWTYHo + 1]) * s_noise * jfsUMkPasnZkDrBlHrfavWZhDulLllvc
    return NECAaWUrFGIXcLimrerEYmxYIykQBfXb
def YBBNVCgficcesWKBpkrWWRHRnnFStZwy(wXwbcvVCQXFmEpNuIRIfbkuOtOpqgUXt, XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz, HCXmerBqIMuTscBONzTGKYapYSxWTYHo, VyjoFEMsihtolZHiuwJuxJKmDsIroAsQ):
    if wXwbcvVCQXFmEpNuIRIfbkuOtOpqgUXt - 1 > HCXmerBqIMuTscBONzTGKYapYSxWTYHo:
        raise ValueError(f'Order {order} too high for step {i}')
    def UBHGiEJRIvAIIxVhgWpzHaosMoApMUPf(tau):
        AxEOibCbRjeUvRwvVNaXLXCBIIzXUnBD = 1.
        for EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm in range(wXwbcvVCQXFmEpNuIRIfbkuOtOpqgUXt):
            if VyjoFEMsihtolZHiuwJuxJKmDsIroAsQ == EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm:
                continue
            AxEOibCbRjeUvRwvVNaXLXCBIIzXUnBD *= (tau - XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz[HCXmerBqIMuTscBONzTGKYapYSxWTYHo - EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm]) / (XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz[HCXmerBqIMuTscBONzTGKYapYSxWTYHo - VyjoFEMsihtolZHiuwJuxJKmDsIroAsQ] - XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz[HCXmerBqIMuTscBONzTGKYapYSxWTYHo - EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm])
        return AxEOibCbRjeUvRwvVNaXLXCBIIzXUnBD
    return integrate.quad(UBHGiEJRIvAIIxVhgWpzHaosMoApMUPf, XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz[HCXmerBqIMuTscBONzTGKYapYSxWTYHo], XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz[HCXmerBqIMuTscBONzTGKYapYSxWTYHo + 1], epsrel=1e-4)[0]
@torch.no_grad()
def YvLQeBPrMuGdZhfqmuFjJMaHFEhvIcMP(VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM, NECAaWUrFGIXcLimrerEYmxYIykQBfXb, ywkdEDhpSPXHYARENdFhpYnCzsLhiORy, TlJxtGydipTPezrPlUrxTKACQdhKNgvw=None, FJsaFpOBdvpFlEdxOzBgjwcWBUfetQGF=None, disable=None, wXwbcvVCQXFmEpNuIRIfbkuOtOpqgUXt=4):
    TlJxtGydipTPezrPlUrxTKACQdhKNgvw = {} if TlJxtGydipTPezrPlUrxTKACQdhKNgvw is None else TlJxtGydipTPezrPlUrxTKACQdhKNgvw
    moQRitRqIYEATNnahksUxyKeQfVQohNA = NECAaWUrFGIXcLimrerEYmxYIykQBfXb.new_ones([NECAaWUrFGIXcLimrerEYmxYIykQBfXb.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[0]])
    dTmYgTUgufMcGyMnnJowIAZqeHEGwVLa = ywkdEDhpSPXHYARENdFhpYnCzsLhiORy.detach().cpu().numpy()
    bKTOPCkNnYlTtvyGohgLIoPMQbrflxmi = []
    for HCXmerBqIMuTscBONzTGKYapYSxWTYHo in trange(len(ywkdEDhpSPXHYARENdFhpYnCzsLhiORy) - 1, disable=disable):
        ODAZKuAsCnodIahYkmGtylGzWplGUuPD = VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM(NECAaWUrFGIXcLimrerEYmxYIykQBfXb, ywkdEDhpSPXHYARENdFhpYnCzsLhiORy[HCXmerBqIMuTscBONzTGKYapYSxWTYHo] * moQRitRqIYEATNnahksUxyKeQfVQohNA, **TlJxtGydipTPezrPlUrxTKACQdhKNgvw)
        TXGwYXNLgQsYzfHHpRBDJGFCFZEClzIo = wWkWWmmaMWzBivoGthogCOrDaHJcXRQg(NECAaWUrFGIXcLimrerEYmxYIykQBfXb, ywkdEDhpSPXHYARENdFhpYnCzsLhiORy[HCXmerBqIMuTscBONzTGKYapYSxWTYHo], ODAZKuAsCnodIahYkmGtylGzWplGUuPD)
        bKTOPCkNnYlTtvyGohgLIoPMQbrflxmi.append(TXGwYXNLgQsYzfHHpRBDJGFCFZEClzIo)
        if len(bKTOPCkNnYlTtvyGohgLIoPMQbrflxmi) > wXwbcvVCQXFmEpNuIRIfbkuOtOpqgUXt:
            bKTOPCkNnYlTtvyGohgLIoPMQbrflxmi.pop(0)
        if FJsaFpOBdvpFlEdxOzBgjwcWBUfetQGF is not None:
            FJsaFpOBdvpFlEdxOzBgjwcWBUfetQGF({'x': NECAaWUrFGIXcLimrerEYmxYIykQBfXb, 'i': HCXmerBqIMuTscBONzTGKYapYSxWTYHo, 'sigma': ywkdEDhpSPXHYARENdFhpYnCzsLhiORy[HCXmerBqIMuTscBONzTGKYapYSxWTYHo], 'sigma_hat': ywkdEDhpSPXHYARENdFhpYnCzsLhiORy[HCXmerBqIMuTscBONzTGKYapYSxWTYHo], 'denoised': ODAZKuAsCnodIahYkmGtylGzWplGUuPD})
        ZWrQpYxChvwQShHmclFqrKsTNDRcHBIk = min(HCXmerBqIMuTscBONzTGKYapYSxWTYHo + 1, wXwbcvVCQXFmEpNuIRIfbkuOtOpqgUXt)
        OABLyDuHThLdYuHnvRIPeoSNESXgbYMG = [YBBNVCgficcesWKBpkrWWRHRnnFStZwy(ZWrQpYxChvwQShHmclFqrKsTNDRcHBIk, dTmYgTUgufMcGyMnnJowIAZqeHEGwVLa, HCXmerBqIMuTscBONzTGKYapYSxWTYHo, VyjoFEMsihtolZHiuwJuxJKmDsIroAsQ) for VyjoFEMsihtolZHiuwJuxJKmDsIroAsQ in range(ZWrQpYxChvwQShHmclFqrKsTNDRcHBIk)]
        NECAaWUrFGIXcLimrerEYmxYIykQBfXb = NECAaWUrFGIXcLimrerEYmxYIykQBfXb + sum(RTeeCveGNqxbJtPYwNiYCFTAFzNZRiqQ * TXGwYXNLgQsYzfHHpRBDJGFCFZEClzIo for RTeeCveGNqxbJtPYwNiYCFTAFzNZRiqQ, TXGwYXNLgQsYzfHHpRBDJGFCFZEClzIo in zip(OABLyDuHThLdYuHnvRIPeoSNESXgbYMG, reversed(bKTOPCkNnYlTtvyGohgLIoPMQbrflxmi)))
    return NECAaWUrFGIXcLimrerEYmxYIykQBfXb
class NGiNYzQhmKjeBZLsqcKpxYURBZmYqGcq:
    def __init__(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab, pcoeff, icoeff, dcoeff, wXwbcvVCQXFmEpNuIRIfbkuOtOpqgUXt=1, accept_safety=0.81, VVqkfbMIOFDgzhOKKnJVcuOffzzrOGPv=1e-8):
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab = xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.b1 = (pcoeff + icoeff + dcoeff) / wXwbcvVCQXFmEpNuIRIfbkuOtOpqgUXt
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.b2 = -(pcoeff + 2 * dcoeff) / wXwbcvVCQXFmEpNuIRIfbkuOtOpqgUXt
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.b3 = dcoeff / wXwbcvVCQXFmEpNuIRIfbkuOtOpqgUXt
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.accept_safety = accept_safety
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.VVqkfbMIOFDgzhOKKnJVcuOffzzrOGPv = VVqkfbMIOFDgzhOKKnJVcuOffzzrOGPv
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.errs = []
    def bTftPQpbuUjUgSfCZgPydPPxdiarPmWa(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, NECAaWUrFGIXcLimrerEYmxYIykQBfXb):
        return 1 + math.atan(NECAaWUrFGIXcLimrerEYmxYIykQBfXb - 1)
    def foIIHvoqqRevvKxdeHdyKcKTgnrvvWhQ(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, PqgBmIFFlGqAiqwTGPXLJksdyclTftXN):
        JcmCprFGEoXFxRBzgvhXNLyFdLBEwPSU = 1 / (float(PqgBmIFFlGqAiqwTGPXLJksdyclTftXN) + rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.VVqkfbMIOFDgzhOKKnJVcuOffzzrOGPv)
        if not rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.errs:
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.errs = [JcmCprFGEoXFxRBzgvhXNLyFdLBEwPSU, JcmCprFGEoXFxRBzgvhXNLyFdLBEwPSU, JcmCprFGEoXFxRBzgvhXNLyFdLBEwPSU]
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.errs[0] = JcmCprFGEoXFxRBzgvhXNLyFdLBEwPSU
        ZOCdfHhxSDyKGnmTCFXPxBveAfxLOShd = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.errs[0] ** rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.b1 * rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.errs[1] ** rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.b2 * rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.errs[2] ** rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.b3
        ZOCdfHhxSDyKGnmTCFXPxBveAfxLOShd = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.bTftPQpbuUjUgSfCZgPydPPxdiarPmWa(ZOCdfHhxSDyKGnmTCFXPxBveAfxLOShd)
        zhHKdMSPADgJhezBAcOeeNCoGFcRRkLr = ZOCdfHhxSDyKGnmTCFXPxBveAfxLOShd >= rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.accept_safety
        if zhHKdMSPADgJhezBAcOeeNCoGFcRRkLr:
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.errs[2] = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.errs[1]
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.errs[1] = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.errs[0]
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab *= ZOCdfHhxSDyKGnmTCFXPxBveAfxLOShd
        return zhHKdMSPADgJhezBAcOeeNCoGFcRRkLr
class emYxrxANFTrWWjWadwfDMSCYZnhrRDgT(nn.Module):
    def __init__(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM, TlJxtGydipTPezrPlUrxTKACQdhKNgvw=None, eps_callback=None, info_callback=None):
        super().__init__()
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM = VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.TlJxtGydipTPezrPlUrxTKACQdhKNgvw = {} if TlJxtGydipTPezrPlUrxTKACQdhKNgvw is None else TlJxtGydipTPezrPlUrxTKACQdhKNgvw
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.eps_callback = eps_callback
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.info_callback = info_callback
    def XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, njuvAJFseAnTpNXMmovFtOzaohoePSQs):
        return -njuvAJFseAnTpNXMmovFtOzaohoePSQs.DJwhOGBaLcOjmXnuwXMXOyhMtknqkKXL()
    def njuvAJFseAnTpNXMmovFtOzaohoePSQs(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz):
        return XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz.neg().exp()
    def VVqkfbMIOFDgzhOKKnJVcuOffzzrOGPv(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, UrPSefbjpQyNJmSeYnIHVGjeyEquRrNC, nyrzKxQtioheHIZujafABgijbCjrWhBU, NECAaWUrFGIXcLimrerEYmxYIykQBfXb, XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz, *DukiculvUpjhZIVvaGinshRSKLSTgVVl, **kwargs):
        if nyrzKxQtioheHIZujafABgijbCjrWhBU in UrPSefbjpQyNJmSeYnIHVGjeyEquRrNC:
            return UrPSefbjpQyNJmSeYnIHVGjeyEquRrNC[nyrzKxQtioheHIZujafABgijbCjrWhBU], UrPSefbjpQyNJmSeYnIHVGjeyEquRrNC
        njuvAJFseAnTpNXMmovFtOzaohoePSQs = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.njuvAJFseAnTpNXMmovFtOzaohoePSQs(XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz) * NECAaWUrFGIXcLimrerEYmxYIykQBfXb.new_ones([NECAaWUrFGIXcLimrerEYmxYIykQBfXb.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[0]])
        VVqkfbMIOFDgzhOKKnJVcuOffzzrOGPv = (NECAaWUrFGIXcLimrerEYmxYIykQBfXb - rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM(NECAaWUrFGIXcLimrerEYmxYIykQBfXb, njuvAJFseAnTpNXMmovFtOzaohoePSQs, *DukiculvUpjhZIVvaGinshRSKLSTgVVl, **rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.TlJxtGydipTPezrPlUrxTKACQdhKNgvw, **kwargs)) / rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.njuvAJFseAnTpNXMmovFtOzaohoePSQs(XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz)
        if rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.eps_callback is not None:
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.eps_callback()
        return VVqkfbMIOFDgzhOKKnJVcuOffzzrOGPv, {nyrzKxQtioheHIZujafABgijbCjrWhBU: VVqkfbMIOFDgzhOKKnJVcuOffzzrOGPv, **UrPSefbjpQyNJmSeYnIHVGjeyEquRrNC}
    def HzAMZAoLeVYawAUWyrrBxXuvUjreQOsk(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, NECAaWUrFGIXcLimrerEYmxYIykQBfXb, XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz, FeAWRnaTBNovNhgenUWGiCkgCADxZPHQ, UrPSefbjpQyNJmSeYnIHVGjeyEquRrNC=None):
        UrPSefbjpQyNJmSeYnIHVGjeyEquRrNC = {} if UrPSefbjpQyNJmSeYnIHVGjeyEquRrNC is None else UrPSefbjpQyNJmSeYnIHVGjeyEquRrNC
        xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab = FeAWRnaTBNovNhgenUWGiCkgCADxZPHQ - XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz
        VVqkfbMIOFDgzhOKKnJVcuOffzzrOGPv, UrPSefbjpQyNJmSeYnIHVGjeyEquRrNC = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.VVqkfbMIOFDgzhOKKnJVcuOffzzrOGPv(UrPSefbjpQyNJmSeYnIHVGjeyEquRrNC, 'eps', NECAaWUrFGIXcLimrerEYmxYIykQBfXb, XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz)
        OwtjieWMGnaJvwZEZbRZsGQyWjGUyGdi = NECAaWUrFGIXcLimrerEYmxYIykQBfXb - rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.njuvAJFseAnTpNXMmovFtOzaohoePSQs(FeAWRnaTBNovNhgenUWGiCkgCADxZPHQ) * xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab.expm1() * VVqkfbMIOFDgzhOKKnJVcuOffzzrOGPv
        return OwtjieWMGnaJvwZEZbRZsGQyWjGUyGdi, UrPSefbjpQyNJmSeYnIHVGjeyEquRrNC
    def FXhawJAqlnkeQxauLnmajSilxvyhqXYh(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, NECAaWUrFGIXcLimrerEYmxYIykQBfXb, XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz, FeAWRnaTBNovNhgenUWGiCkgCADxZPHQ, apACmNWgYmlQTXHPQlhMzlFpreaoNbwW=1 / 2, UrPSefbjpQyNJmSeYnIHVGjeyEquRrNC=None):
        UrPSefbjpQyNJmSeYnIHVGjeyEquRrNC = {} if UrPSefbjpQyNJmSeYnIHVGjeyEquRrNC is None else UrPSefbjpQyNJmSeYnIHVGjeyEquRrNC
        xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab = FeAWRnaTBNovNhgenUWGiCkgCADxZPHQ - XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz
        VVqkfbMIOFDgzhOKKnJVcuOffzzrOGPv, UrPSefbjpQyNJmSeYnIHVGjeyEquRrNC = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.VVqkfbMIOFDgzhOKKnJVcuOffzzrOGPv(UrPSefbjpQyNJmSeYnIHVGjeyEquRrNC, 'eps', NECAaWUrFGIXcLimrerEYmxYIykQBfXb, XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz)
        XauksjEFAUvtInEaALXIwUhurkUuooOF = XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz + apACmNWgYmlQTXHPQlhMzlFpreaoNbwW * xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab
        ddkdPIaRKoONDDOjzqCLBzqWRUfKAuZP = NECAaWUrFGIXcLimrerEYmxYIykQBfXb - rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.njuvAJFseAnTpNXMmovFtOzaohoePSQs(XauksjEFAUvtInEaALXIwUhurkUuooOF) * (apACmNWgYmlQTXHPQlhMzlFpreaoNbwW * xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab).expm1() * VVqkfbMIOFDgzhOKKnJVcuOffzzrOGPv
        HWCcAjtdJVaPoTurNyGCUZfzCVQoWpYg, UrPSefbjpQyNJmSeYnIHVGjeyEquRrNC = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.VVqkfbMIOFDgzhOKKnJVcuOffzzrOGPv(UrPSefbjpQyNJmSeYnIHVGjeyEquRrNC, 'eps_r1', ddkdPIaRKoONDDOjzqCLBzqWRUfKAuZP, XauksjEFAUvtInEaALXIwUhurkUuooOF)
        kFbeKlGwETjnrOUnINvTygvTLgayPoOr = NECAaWUrFGIXcLimrerEYmxYIykQBfXb - rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.njuvAJFseAnTpNXMmovFtOzaohoePSQs(FeAWRnaTBNovNhgenUWGiCkgCADxZPHQ) * xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab.expm1() * VVqkfbMIOFDgzhOKKnJVcuOffzzrOGPv - rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.njuvAJFseAnTpNXMmovFtOzaohoePSQs(FeAWRnaTBNovNhgenUWGiCkgCADxZPHQ) / (2 * apACmNWgYmlQTXHPQlhMzlFpreaoNbwW) * xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab.expm1() * (HWCcAjtdJVaPoTurNyGCUZfzCVQoWpYg - VVqkfbMIOFDgzhOKKnJVcuOffzzrOGPv)
        return kFbeKlGwETjnrOUnINvTygvTLgayPoOr, UrPSefbjpQyNJmSeYnIHVGjeyEquRrNC
    def IuzFllPzUxmiJphaHtQbBaxJViSVJqPW(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, NECAaWUrFGIXcLimrerEYmxYIykQBfXb, XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz, FeAWRnaTBNovNhgenUWGiCkgCADxZPHQ, apACmNWgYmlQTXHPQlhMzlFpreaoNbwW=1 / 3, jUXrpBDWrfGGiwtyaMexgPCaBaIoLdEZ=2 / 3, UrPSefbjpQyNJmSeYnIHVGjeyEquRrNC=None):
        UrPSefbjpQyNJmSeYnIHVGjeyEquRrNC = {} if UrPSefbjpQyNJmSeYnIHVGjeyEquRrNC is None else UrPSefbjpQyNJmSeYnIHVGjeyEquRrNC
        xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab = FeAWRnaTBNovNhgenUWGiCkgCADxZPHQ - XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz
        VVqkfbMIOFDgzhOKKnJVcuOffzzrOGPv, UrPSefbjpQyNJmSeYnIHVGjeyEquRrNC = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.VVqkfbMIOFDgzhOKKnJVcuOffzzrOGPv(UrPSefbjpQyNJmSeYnIHVGjeyEquRrNC, 'eps', NECAaWUrFGIXcLimrerEYmxYIykQBfXb, XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz)
        XauksjEFAUvtInEaALXIwUhurkUuooOF = XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz + apACmNWgYmlQTXHPQlhMzlFpreaoNbwW * xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab
        orjPyVtdqCXZbZZCrekqzXxPBGSWSqJa = XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz + jUXrpBDWrfGGiwtyaMexgPCaBaIoLdEZ * xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab
        ddkdPIaRKoONDDOjzqCLBzqWRUfKAuZP = NECAaWUrFGIXcLimrerEYmxYIykQBfXb - rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.njuvAJFseAnTpNXMmovFtOzaohoePSQs(XauksjEFAUvtInEaALXIwUhurkUuooOF) * (apACmNWgYmlQTXHPQlhMzlFpreaoNbwW * xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab).expm1() * VVqkfbMIOFDgzhOKKnJVcuOffzzrOGPv
        HWCcAjtdJVaPoTurNyGCUZfzCVQoWpYg, UrPSefbjpQyNJmSeYnIHVGjeyEquRrNC = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.VVqkfbMIOFDgzhOKKnJVcuOffzzrOGPv(UrPSefbjpQyNJmSeYnIHVGjeyEquRrNC, 'eps_r1', ddkdPIaRKoONDDOjzqCLBzqWRUfKAuZP, XauksjEFAUvtInEaALXIwUhurkUuooOF)
        YaoLKXMxYolQSjUTSVHMwSWbGqmmhIZH = NECAaWUrFGIXcLimrerEYmxYIykQBfXb - rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.njuvAJFseAnTpNXMmovFtOzaohoePSQs(orjPyVtdqCXZbZZCrekqzXxPBGSWSqJa) * (jUXrpBDWrfGGiwtyaMexgPCaBaIoLdEZ * xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab).expm1() * VVqkfbMIOFDgzhOKKnJVcuOffzzrOGPv - rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.njuvAJFseAnTpNXMmovFtOzaohoePSQs(orjPyVtdqCXZbZZCrekqzXxPBGSWSqJa) * (jUXrpBDWrfGGiwtyaMexgPCaBaIoLdEZ / apACmNWgYmlQTXHPQlhMzlFpreaoNbwW) * ((jUXrpBDWrfGGiwtyaMexgPCaBaIoLdEZ * xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab).expm1() / (jUXrpBDWrfGGiwtyaMexgPCaBaIoLdEZ * xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab) - 1) * (HWCcAjtdJVaPoTurNyGCUZfzCVQoWpYg - VVqkfbMIOFDgzhOKKnJVcuOffzzrOGPv)
        fXFfHKElHcEsNlXUBanhIhLYlnyBgYYW, UrPSefbjpQyNJmSeYnIHVGjeyEquRrNC = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.VVqkfbMIOFDgzhOKKnJVcuOffzzrOGPv(UrPSefbjpQyNJmSeYnIHVGjeyEquRrNC, 'eps_r2', YaoLKXMxYolQSjUTSVHMwSWbGqmmhIZH, orjPyVtdqCXZbZZCrekqzXxPBGSWSqJa)
        zTbhjDcmYDmcunfncCyQqpmFtTMHAqGh = NECAaWUrFGIXcLimrerEYmxYIykQBfXb - rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.njuvAJFseAnTpNXMmovFtOzaohoePSQs(FeAWRnaTBNovNhgenUWGiCkgCADxZPHQ) * xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab.expm1() * VVqkfbMIOFDgzhOKKnJVcuOffzzrOGPv - rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.njuvAJFseAnTpNXMmovFtOzaohoePSQs(FeAWRnaTBNovNhgenUWGiCkgCADxZPHQ) / jUXrpBDWrfGGiwtyaMexgPCaBaIoLdEZ * (xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab.expm1() / xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab - 1) * (fXFfHKElHcEsNlXUBanhIhLYlnyBgYYW - VVqkfbMIOFDgzhOKKnJVcuOffzzrOGPv)
        return zTbhjDcmYDmcunfncCyQqpmFtTMHAqGh, UrPSefbjpQyNJmSeYnIHVGjeyEquRrNC
    def WriULhEyEihtMQlEXBgXiTsCMmqSinrF(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, NECAaWUrFGIXcLimrerEYmxYIykQBfXb, t_start, t_end, mqjdnLvRIQanefOEDvuxdBhWzpDCvXGA, YifKHCfIbeEsuQSFLLpJatOOrlBeQSoO=0., s_noise=1., ubyoEoHoKfVYweiaMPbKnyuENzoZHLei=None):
        ubyoEoHoKfVYweiaMPbKnyuENzoZHLei = IIWZsliZaKlVluovJAtCbQFoHHPJmJDG(NECAaWUrFGIXcLimrerEYmxYIykQBfXb) if ubyoEoHoKfVYweiaMPbKnyuENzoZHLei is None else ubyoEoHoKfVYweiaMPbKnyuENzoZHLei
        if not t_end > t_start and YifKHCfIbeEsuQSFLLpJatOOrlBeQSoO:
            raise ValueError('eta must be 0 for reverse sampling')
        FTosLGldclAzaiNbwuLMIEtXfrZQpTnU = math.floor(mqjdnLvRIQanefOEDvuxdBhWzpDCvXGA / 3) + 1
        cZfLNeHGLvPreutnrDmWGGyKvtymQVKM = torch.linspace(t_start, t_end, FTosLGldclAzaiNbwuLMIEtXfrZQpTnU + 1, fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc=NECAaWUrFGIXcLimrerEYmxYIykQBfXb.fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc)
        if mqjdnLvRIQanefOEDvuxdBhWzpDCvXGA % 3 == 0:
            CfVKhsKPtOaiLDSyReEIATrYxiCnFRUx = [3] * (FTosLGldclAzaiNbwuLMIEtXfrZQpTnU - 2) + [2, 1]
        else:
            CfVKhsKPtOaiLDSyReEIATrYxiCnFRUx = [3] * (FTosLGldclAzaiNbwuLMIEtXfrZQpTnU - 1) + [mqjdnLvRIQanefOEDvuxdBhWzpDCvXGA % 3]
        for HCXmerBqIMuTscBONzTGKYapYSxWTYHo in range(len(CfVKhsKPtOaiLDSyReEIATrYxiCnFRUx)):
            UrPSefbjpQyNJmSeYnIHVGjeyEquRrNC = {}
            XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz, FeAWRnaTBNovNhgenUWGiCkgCADxZPHQ = cZfLNeHGLvPreutnrDmWGGyKvtymQVKM[HCXmerBqIMuTscBONzTGKYapYSxWTYHo], cZfLNeHGLvPreutnrDmWGGyKvtymQVKM[HCXmerBqIMuTscBONzTGKYapYSxWTYHo + 1]
            if YifKHCfIbeEsuQSFLLpJatOOrlBeQSoO:
                ylGhUFMpxPbtUUTfCZpemVkdanRhWmHa, WWLDnvOujbcGZhDStZqEqAbBZaJQZkVg = EQrWJtFJAcWXVjwSXclhNFDOxYkkGfcF(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.njuvAJFseAnTpNXMmovFtOzaohoePSQs(XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz), rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.njuvAJFseAnTpNXMmovFtOzaohoePSQs(FeAWRnaTBNovNhgenUWGiCkgCADxZPHQ), YifKHCfIbeEsuQSFLLpJatOOrlBeQSoO)
                bYVlspJHAQeYetnvmXskpqNYdxqYkhnk = torch.minimum(t_end, rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz(ylGhUFMpxPbtUUTfCZpemVkdanRhWmHa))
                WWLDnvOujbcGZhDStZqEqAbBZaJQZkVg = (rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.njuvAJFseAnTpNXMmovFtOzaohoePSQs(FeAWRnaTBNovNhgenUWGiCkgCADxZPHQ) ** 2 - rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.njuvAJFseAnTpNXMmovFtOzaohoePSQs(bYVlspJHAQeYetnvmXskpqNYdxqYkhnk) ** 2) ** 0.5
            else:
                bYVlspJHAQeYetnvmXskpqNYdxqYkhnk, WWLDnvOujbcGZhDStZqEqAbBZaJQZkVg = FeAWRnaTBNovNhgenUWGiCkgCADxZPHQ, 0.
            VVqkfbMIOFDgzhOKKnJVcuOffzzrOGPv, UrPSefbjpQyNJmSeYnIHVGjeyEquRrNC = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.VVqkfbMIOFDgzhOKKnJVcuOffzzrOGPv(UrPSefbjpQyNJmSeYnIHVGjeyEquRrNC, 'eps', NECAaWUrFGIXcLimrerEYmxYIykQBfXb, XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz)
            ODAZKuAsCnodIahYkmGtylGzWplGUuPD = NECAaWUrFGIXcLimrerEYmxYIykQBfXb - rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.njuvAJFseAnTpNXMmovFtOzaohoePSQs(XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz) * VVqkfbMIOFDgzhOKKnJVcuOffzzrOGPv
            if rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.info_callback is not None:
                rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.info_callback({'x': NECAaWUrFGIXcLimrerEYmxYIykQBfXb, 'i': HCXmerBqIMuTscBONzTGKYapYSxWTYHo, 't': cZfLNeHGLvPreutnrDmWGGyKvtymQVKM[HCXmerBqIMuTscBONzTGKYapYSxWTYHo], 't_up': XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz, 'denoised': ODAZKuAsCnodIahYkmGtylGzWplGUuPD})
            if CfVKhsKPtOaiLDSyReEIATrYxiCnFRUx[HCXmerBqIMuTscBONzTGKYapYSxWTYHo] == 1:
                NECAaWUrFGIXcLimrerEYmxYIykQBfXb, UrPSefbjpQyNJmSeYnIHVGjeyEquRrNC = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.HzAMZAoLeVYawAUWyrrBxXuvUjreQOsk(NECAaWUrFGIXcLimrerEYmxYIykQBfXb, XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz, bYVlspJHAQeYetnvmXskpqNYdxqYkhnk, UrPSefbjpQyNJmSeYnIHVGjeyEquRrNC=UrPSefbjpQyNJmSeYnIHVGjeyEquRrNC)
            elif CfVKhsKPtOaiLDSyReEIATrYxiCnFRUx[HCXmerBqIMuTscBONzTGKYapYSxWTYHo] == 2:
                NECAaWUrFGIXcLimrerEYmxYIykQBfXb, UrPSefbjpQyNJmSeYnIHVGjeyEquRrNC = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.FXhawJAqlnkeQxauLnmajSilxvyhqXYh(NECAaWUrFGIXcLimrerEYmxYIykQBfXb, XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz, bYVlspJHAQeYetnvmXskpqNYdxqYkhnk, UrPSefbjpQyNJmSeYnIHVGjeyEquRrNC=UrPSefbjpQyNJmSeYnIHVGjeyEquRrNC)
            else:
                NECAaWUrFGIXcLimrerEYmxYIykQBfXb, UrPSefbjpQyNJmSeYnIHVGjeyEquRrNC = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.IuzFllPzUxmiJphaHtQbBaxJViSVJqPW(NECAaWUrFGIXcLimrerEYmxYIykQBfXb, XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz, bYVlspJHAQeYetnvmXskpqNYdxqYkhnk, UrPSefbjpQyNJmSeYnIHVGjeyEquRrNC=UrPSefbjpQyNJmSeYnIHVGjeyEquRrNC)
            NECAaWUrFGIXcLimrerEYmxYIykQBfXb = NECAaWUrFGIXcLimrerEYmxYIykQBfXb + WWLDnvOujbcGZhDStZqEqAbBZaJQZkVg * s_noise * ubyoEoHoKfVYweiaMPbKnyuENzoZHLei(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.njuvAJFseAnTpNXMmovFtOzaohoePSQs(XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz), rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.njuvAJFseAnTpNXMmovFtOzaohoePSQs(FeAWRnaTBNovNhgenUWGiCkgCADxZPHQ))
        return NECAaWUrFGIXcLimrerEYmxYIykQBfXb
    def lieinrspmvpJdGRvWmbDEsTLywcStiXK(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, NECAaWUrFGIXcLimrerEYmxYIykQBfXb, t_start, t_end, wXwbcvVCQXFmEpNuIRIfbkuOtOpqgUXt=3, lrGjvYpKmgOnrVeFRaijRVZHIZNddmlD=0.05, fFzyGDwsUOSTBngTGiKDqIYKKikweEzG=0.0078, nHhdfLfCCuIPTnfLwRoJKgcxTtMzAVNY=0.05, pcoeff=0., icoeff=1., dcoeff=0., accept_safety=0.81, YifKHCfIbeEsuQSFLLpJatOOrlBeQSoO=0., s_noise=1., ubyoEoHoKfVYweiaMPbKnyuENzoZHLei=None):
        ubyoEoHoKfVYweiaMPbKnyuENzoZHLei = IIWZsliZaKlVluovJAtCbQFoHHPJmJDG(NECAaWUrFGIXcLimrerEYmxYIykQBfXb) if ubyoEoHoKfVYweiaMPbKnyuENzoZHLei is None else ubyoEoHoKfVYweiaMPbKnyuENzoZHLei
        if wXwbcvVCQXFmEpNuIRIfbkuOtOpqgUXt not in {2, 3}:
            raise ValueError('order should be 2 or 3')
        lqBgIcSWZYylbCPjXksJWDguuSOqoPCJ = t_end > t_start
        if not lqBgIcSWZYylbCPjXksJWDguuSOqoPCJ and YifKHCfIbeEsuQSFLLpJatOOrlBeQSoO:
            raise ValueError('eta must be 0 for reverse sampling')
        nHhdfLfCCuIPTnfLwRoJKgcxTtMzAVNY = abs(nHhdfLfCCuIPTnfLwRoJKgcxTtMzAVNY) * (1 if lqBgIcSWZYylbCPjXksJWDguuSOqoPCJ else -1)
        fFzyGDwsUOSTBngTGiKDqIYKKikweEzG = torch.xPmCFphFKpGMpIsczaSKHmMgRPZzJwla(fFzyGDwsUOSTBngTGiKDqIYKKikweEzG)
        lrGjvYpKmgOnrVeFRaijRVZHIZNddmlD = torch.xPmCFphFKpGMpIsczaSKHmMgRPZzJwla(lrGjvYpKmgOnrVeFRaijRVZHIZNddmlD)
        uPePujIqMVDrwNvZQxJajkuaQFAcacjA = t_start
        sIfmGCKFYSuAcKGivnHeSsHXHFOsVWBD = NECAaWUrFGIXcLimrerEYmxYIykQBfXb
        zhHKdMSPADgJhezBAcOeeNCoGFcRRkLr = True
        McbnBzBcpYLemnDFrpdXetrbuBSescLC = NGiNYzQhmKjeBZLsqcKpxYURBZmYqGcq(nHhdfLfCCuIPTnfLwRoJKgcxTtMzAVNY, pcoeff, icoeff, dcoeff, 1.5 if YifKHCfIbeEsuQSFLLpJatOOrlBeQSoO else wXwbcvVCQXFmEpNuIRIfbkuOtOpqgUXt, accept_safety)
        dkvGBiZkeLIFANNbVKlbQzLVBVedCkgi = {'steps': 0, 'nfe': 0, 'n_accept': 0, 'n_reject': 0}
        while uPePujIqMVDrwNvZQxJajkuaQFAcacjA < t_end - 1e-5 if lqBgIcSWZYylbCPjXksJWDguuSOqoPCJ else uPePujIqMVDrwNvZQxJajkuaQFAcacjA > t_end + 1e-5:
            UrPSefbjpQyNJmSeYnIHVGjeyEquRrNC = {}
            XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz = torch.minimum(t_end, uPePujIqMVDrwNvZQxJajkuaQFAcacjA + McbnBzBcpYLemnDFrpdXetrbuBSescLC.xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab) if lqBgIcSWZYylbCPjXksJWDguuSOqoPCJ else torch.maximum(t_end, uPePujIqMVDrwNvZQxJajkuaQFAcacjA + McbnBzBcpYLemnDFrpdXetrbuBSescLC.xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab)
            if YifKHCfIbeEsuQSFLLpJatOOrlBeQSoO:
                ylGhUFMpxPbtUUTfCZpemVkdanRhWmHa, WWLDnvOujbcGZhDStZqEqAbBZaJQZkVg = EQrWJtFJAcWXVjwSXclhNFDOxYkkGfcF(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.njuvAJFseAnTpNXMmovFtOzaohoePSQs(uPePujIqMVDrwNvZQxJajkuaQFAcacjA), rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.njuvAJFseAnTpNXMmovFtOzaohoePSQs(XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz), YifKHCfIbeEsuQSFLLpJatOOrlBeQSoO)
                MdTfxGpERcHJkTQkcfFIbAXTjXrLmeZb = torch.minimum(t_end, rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz(ylGhUFMpxPbtUUTfCZpemVkdanRhWmHa))
                WWLDnvOujbcGZhDStZqEqAbBZaJQZkVg = (rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.njuvAJFseAnTpNXMmovFtOzaohoePSQs(XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz) ** 2 - rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.njuvAJFseAnTpNXMmovFtOzaohoePSQs(MdTfxGpERcHJkTQkcfFIbAXTjXrLmeZb) ** 2) ** 0.5
            else:
                MdTfxGpERcHJkTQkcfFIbAXTjXrLmeZb, WWLDnvOujbcGZhDStZqEqAbBZaJQZkVg = XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz, 0.
            VVqkfbMIOFDgzhOKKnJVcuOffzzrOGPv, UrPSefbjpQyNJmSeYnIHVGjeyEquRrNC = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.VVqkfbMIOFDgzhOKKnJVcuOffzzrOGPv(UrPSefbjpQyNJmSeYnIHVGjeyEquRrNC, 'eps', NECAaWUrFGIXcLimrerEYmxYIykQBfXb, uPePujIqMVDrwNvZQxJajkuaQFAcacjA)
            ODAZKuAsCnodIahYkmGtylGzWplGUuPD = NECAaWUrFGIXcLimrerEYmxYIykQBfXb - rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.njuvAJFseAnTpNXMmovFtOzaohoePSQs(uPePujIqMVDrwNvZQxJajkuaQFAcacjA) * VVqkfbMIOFDgzhOKKnJVcuOffzzrOGPv
            if wXwbcvVCQXFmEpNuIRIfbkuOtOpqgUXt == 2:
                GfrchFcsKktrRpeJWVjvVinDZCjHJpVJ, UrPSefbjpQyNJmSeYnIHVGjeyEquRrNC = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.HzAMZAoLeVYawAUWyrrBxXuvUjreQOsk(NECAaWUrFGIXcLimrerEYmxYIykQBfXb, uPePujIqMVDrwNvZQxJajkuaQFAcacjA, MdTfxGpERcHJkTQkcfFIbAXTjXrLmeZb, UrPSefbjpQyNJmSeYnIHVGjeyEquRrNC=UrPSefbjpQyNJmSeYnIHVGjeyEquRrNC)
                PhsXoEtTtWgfBRlQjqyjFjLXYhIIULtH, UrPSefbjpQyNJmSeYnIHVGjeyEquRrNC = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.FXhawJAqlnkeQxauLnmajSilxvyhqXYh(NECAaWUrFGIXcLimrerEYmxYIykQBfXb, uPePujIqMVDrwNvZQxJajkuaQFAcacjA, MdTfxGpERcHJkTQkcfFIbAXTjXrLmeZb, UrPSefbjpQyNJmSeYnIHVGjeyEquRrNC=UrPSefbjpQyNJmSeYnIHVGjeyEquRrNC)
            else:
                GfrchFcsKktrRpeJWVjvVinDZCjHJpVJ, UrPSefbjpQyNJmSeYnIHVGjeyEquRrNC = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.FXhawJAqlnkeQxauLnmajSilxvyhqXYh(NECAaWUrFGIXcLimrerEYmxYIykQBfXb, uPePujIqMVDrwNvZQxJajkuaQFAcacjA, MdTfxGpERcHJkTQkcfFIbAXTjXrLmeZb, apACmNWgYmlQTXHPQlhMzlFpreaoNbwW=1 / 3, UrPSefbjpQyNJmSeYnIHVGjeyEquRrNC=UrPSefbjpQyNJmSeYnIHVGjeyEquRrNC)
                PhsXoEtTtWgfBRlQjqyjFjLXYhIIULtH, UrPSefbjpQyNJmSeYnIHVGjeyEquRrNC = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.IuzFllPzUxmiJphaHtQbBaxJViSVJqPW(NECAaWUrFGIXcLimrerEYmxYIykQBfXb, uPePujIqMVDrwNvZQxJajkuaQFAcacjA, MdTfxGpERcHJkTQkcfFIbAXTjXrLmeZb, UrPSefbjpQyNJmSeYnIHVGjeyEquRrNC=UrPSefbjpQyNJmSeYnIHVGjeyEquRrNC)
            MOjnRhezkNHoQzGPojAUpkgsQLDRoDNC = torch.maximum(fFzyGDwsUOSTBngTGiKDqIYKKikweEzG, lrGjvYpKmgOnrVeFRaijRVZHIZNddmlD * torch.maximum(GfrchFcsKktrRpeJWVjvVinDZCjHJpVJ.abs(), sIfmGCKFYSuAcKGivnHeSsHXHFOsVWBD.abs()))
            PqgBmIFFlGqAiqwTGPXLJksdyclTftXN = torch.linalg.norm((GfrchFcsKktrRpeJWVjvVinDZCjHJpVJ - PhsXoEtTtWgfBRlQjqyjFjLXYhIIULtH) / MOjnRhezkNHoQzGPojAUpkgsQLDRoDNC) / NECAaWUrFGIXcLimrerEYmxYIykQBfXb.numel() ** 0.5
            zhHKdMSPADgJhezBAcOeeNCoGFcRRkLr = McbnBzBcpYLemnDFrpdXetrbuBSescLC.foIIHvoqqRevvKxdeHdyKcKTgnrvvWhQ(PqgBmIFFlGqAiqwTGPXLJksdyclTftXN)
            if zhHKdMSPADgJhezBAcOeeNCoGFcRRkLr:
                sIfmGCKFYSuAcKGivnHeSsHXHFOsVWBD = GfrchFcsKktrRpeJWVjvVinDZCjHJpVJ
                NECAaWUrFGIXcLimrerEYmxYIykQBfXb = PhsXoEtTtWgfBRlQjqyjFjLXYhIIULtH + WWLDnvOujbcGZhDStZqEqAbBZaJQZkVg * s_noise * ubyoEoHoKfVYweiaMPbKnyuENzoZHLei(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.njuvAJFseAnTpNXMmovFtOzaohoePSQs(uPePujIqMVDrwNvZQxJajkuaQFAcacjA), rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.njuvAJFseAnTpNXMmovFtOzaohoePSQs(XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz))
                uPePujIqMVDrwNvZQxJajkuaQFAcacjA = XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz
                dkvGBiZkeLIFANNbVKlbQzLVBVedCkgi['n_accept'] += 1
            else:
                dkvGBiZkeLIFANNbVKlbQzLVBVedCkgi['n_reject'] += 1
            dkvGBiZkeLIFANNbVKlbQzLVBVedCkgi['nfe'] += wXwbcvVCQXFmEpNuIRIfbkuOtOpqgUXt
            dkvGBiZkeLIFANNbVKlbQzLVBVedCkgi['steps'] += 1
            if rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.info_callback is not None:
                rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.info_callback({'x': NECAaWUrFGIXcLimrerEYmxYIykQBfXb, 'i': dkvGBiZkeLIFANNbVKlbQzLVBVedCkgi['steps'] - 1, 't': uPePujIqMVDrwNvZQxJajkuaQFAcacjA, 't_up': uPePujIqMVDrwNvZQxJajkuaQFAcacjA, 'denoised': ODAZKuAsCnodIahYkmGtylGzWplGUuPD, 'error': PqgBmIFFlGqAiqwTGPXLJksdyclTftXN, 'h': McbnBzBcpYLemnDFrpdXetrbuBSescLC.xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab, **dkvGBiZkeLIFANNbVKlbQzLVBVedCkgi})
        return NECAaWUrFGIXcLimrerEYmxYIykQBfXb, dkvGBiZkeLIFANNbVKlbQzLVBVedCkgi
@torch.no_grad()
def VDQOtTmmMUGwedygxOrBSZdviYnhtBDM(VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM, NECAaWUrFGIXcLimrerEYmxYIykQBfXb, FrgHMQrwGwxjLFZFaZndQasXgRhPXZyj, SjuBswrlxdwXAwbvIiTMrngJfAEFYXwe, zXHJFiFFvWqeQIAxyaTGMUgoRaHrYzjK, TlJxtGydipTPezrPlUrxTKACQdhKNgvw=None, FJsaFpOBdvpFlEdxOzBgjwcWBUfetQGF=None, disable=None, YifKHCfIbeEsuQSFLLpJatOOrlBeQSoO=0., s_noise=1., ubyoEoHoKfVYweiaMPbKnyuENzoZHLei=None):
    if FrgHMQrwGwxjLFZFaZndQasXgRhPXZyj <= 0 or SjuBswrlxdwXAwbvIiTMrngJfAEFYXwe <= 0:
        raise ValueError('sigma_min and sigma_max must not be 0')
    with tqdm(total=zXHJFiFFvWqeQIAxyaTGMUgoRaHrYzjK, disable=disable) as ehYcJDzojxbXZiwqMPlEiTyCBgASsEBo:
        coRBQpFSAigrvAFvKpXVhaSBGcYwgXUm = emYxrxANFTrWWjWadwfDMSCYZnhrRDgT(VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM, TlJxtGydipTPezrPlUrxTKACQdhKNgvw, eps_callback=ehYcJDzojxbXZiwqMPlEiTyCBgASsEBo.update)
        if FJsaFpOBdvpFlEdxOzBgjwcWBUfetQGF is not None:
            coRBQpFSAigrvAFvKpXVhaSBGcYwgXUm.info_callback = lambda dkvGBiZkeLIFANNbVKlbQzLVBVedCkgi: FJsaFpOBdvpFlEdxOzBgjwcWBUfetQGF({'sigma': coRBQpFSAigrvAFvKpXVhaSBGcYwgXUm.njuvAJFseAnTpNXMmovFtOzaohoePSQs(dkvGBiZkeLIFANNbVKlbQzLVBVedCkgi['t']), 'sigma_hat': coRBQpFSAigrvAFvKpXVhaSBGcYwgXUm.njuvAJFseAnTpNXMmovFtOzaohoePSQs(dkvGBiZkeLIFANNbVKlbQzLVBVedCkgi['t_up']), **dkvGBiZkeLIFANNbVKlbQzLVBVedCkgi})
        return coRBQpFSAigrvAFvKpXVhaSBGcYwgXUm.WriULhEyEihtMQlEXBgXiTsCMmqSinrF(NECAaWUrFGIXcLimrerEYmxYIykQBfXb, coRBQpFSAigrvAFvKpXVhaSBGcYwgXUm.XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz(torch.xPmCFphFKpGMpIsczaSKHmMgRPZzJwla(SjuBswrlxdwXAwbvIiTMrngJfAEFYXwe)), coRBQpFSAigrvAFvKpXVhaSBGcYwgXUm.XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz(torch.xPmCFphFKpGMpIsczaSKHmMgRPZzJwla(FrgHMQrwGwxjLFZFaZndQasXgRhPXZyj)), zXHJFiFFvWqeQIAxyaTGMUgoRaHrYzjK, YifKHCfIbeEsuQSFLLpJatOOrlBeQSoO, s_noise, ubyoEoHoKfVYweiaMPbKnyuENzoZHLei)
@torch.no_grad()
def BvWGQUPePgVskvYZnjYrTTFssOiSKdhE(VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM, NECAaWUrFGIXcLimrerEYmxYIykQBfXb, FrgHMQrwGwxjLFZFaZndQasXgRhPXZyj, SjuBswrlxdwXAwbvIiTMrngJfAEFYXwe, TlJxtGydipTPezrPlUrxTKACQdhKNgvw=None, FJsaFpOBdvpFlEdxOzBgjwcWBUfetQGF=None, disable=None, wXwbcvVCQXFmEpNuIRIfbkuOtOpqgUXt=3, lrGjvYpKmgOnrVeFRaijRVZHIZNddmlD=0.05, fFzyGDwsUOSTBngTGiKDqIYKKikweEzG=0.0078, nHhdfLfCCuIPTnfLwRoJKgcxTtMzAVNY=0.05, pcoeff=0., icoeff=1., dcoeff=0., accept_safety=0.81, YifKHCfIbeEsuQSFLLpJatOOrlBeQSoO=0., s_noise=1., ubyoEoHoKfVYweiaMPbKnyuENzoZHLei=None, return_info=False):
    if FrgHMQrwGwxjLFZFaZndQasXgRhPXZyj <= 0 or SjuBswrlxdwXAwbvIiTMrngJfAEFYXwe <= 0:
        raise ValueError('sigma_min and sigma_max must not be 0')
    with tqdm(disable=disable) as ehYcJDzojxbXZiwqMPlEiTyCBgASsEBo:
        coRBQpFSAigrvAFvKpXVhaSBGcYwgXUm = emYxrxANFTrWWjWadwfDMSCYZnhrRDgT(VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM, TlJxtGydipTPezrPlUrxTKACQdhKNgvw, eps_callback=ehYcJDzojxbXZiwqMPlEiTyCBgASsEBo.update)
        if FJsaFpOBdvpFlEdxOzBgjwcWBUfetQGF is not None:
            coRBQpFSAigrvAFvKpXVhaSBGcYwgXUm.info_callback = lambda dkvGBiZkeLIFANNbVKlbQzLVBVedCkgi: FJsaFpOBdvpFlEdxOzBgjwcWBUfetQGF({'sigma': coRBQpFSAigrvAFvKpXVhaSBGcYwgXUm.njuvAJFseAnTpNXMmovFtOzaohoePSQs(dkvGBiZkeLIFANNbVKlbQzLVBVedCkgi['t']), 'sigma_hat': coRBQpFSAigrvAFvKpXVhaSBGcYwgXUm.njuvAJFseAnTpNXMmovFtOzaohoePSQs(dkvGBiZkeLIFANNbVKlbQzLVBVedCkgi['t_up']), **dkvGBiZkeLIFANNbVKlbQzLVBVedCkgi})
        NECAaWUrFGIXcLimrerEYmxYIykQBfXb, dkvGBiZkeLIFANNbVKlbQzLVBVedCkgi = coRBQpFSAigrvAFvKpXVhaSBGcYwgXUm.lieinrspmvpJdGRvWmbDEsTLywcStiXK(NECAaWUrFGIXcLimrerEYmxYIykQBfXb, coRBQpFSAigrvAFvKpXVhaSBGcYwgXUm.XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz(torch.xPmCFphFKpGMpIsczaSKHmMgRPZzJwla(SjuBswrlxdwXAwbvIiTMrngJfAEFYXwe)), coRBQpFSAigrvAFvKpXVhaSBGcYwgXUm.XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz(torch.xPmCFphFKpGMpIsczaSKHmMgRPZzJwla(FrgHMQrwGwxjLFZFaZndQasXgRhPXZyj)), wXwbcvVCQXFmEpNuIRIfbkuOtOpqgUXt, lrGjvYpKmgOnrVeFRaijRVZHIZNddmlD, fFzyGDwsUOSTBngTGiKDqIYKKikweEzG, nHhdfLfCCuIPTnfLwRoJKgcxTtMzAVNY, pcoeff, icoeff, dcoeff, accept_safety, YifKHCfIbeEsuQSFLLpJatOOrlBeQSoO, s_noise, ubyoEoHoKfVYweiaMPbKnyuENzoZHLei)
    if return_info:
        return NECAaWUrFGIXcLimrerEYmxYIykQBfXb, dkvGBiZkeLIFANNbVKlbQzLVBVedCkgi
    return NECAaWUrFGIXcLimrerEYmxYIykQBfXb
@torch.no_grad()
def LeKQzbzjntcGKZLmyypVGMKVoXUMuzVl(VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM, NECAaWUrFGIXcLimrerEYmxYIykQBfXb, ywkdEDhpSPXHYARENdFhpYnCzsLhiORy, TlJxtGydipTPezrPlUrxTKACQdhKNgvw=None, FJsaFpOBdvpFlEdxOzBgjwcWBUfetQGF=None, disable=None, YifKHCfIbeEsuQSFLLpJatOOrlBeQSoO=1., s_noise=1., ubyoEoHoKfVYweiaMPbKnyuENzoZHLei=None):
    TlJxtGydipTPezrPlUrxTKACQdhKNgvw = {} if TlJxtGydipTPezrPlUrxTKACQdhKNgvw is None else TlJxtGydipTPezrPlUrxTKACQdhKNgvw
    ubyoEoHoKfVYweiaMPbKnyuENzoZHLei = IIWZsliZaKlVluovJAtCbQFoHHPJmJDG(NECAaWUrFGIXcLimrerEYmxYIykQBfXb) if ubyoEoHoKfVYweiaMPbKnyuENzoZHLei is None else ubyoEoHoKfVYweiaMPbKnyuENzoZHLei
    moQRitRqIYEATNnahksUxyKeQfVQohNA = NECAaWUrFGIXcLimrerEYmxYIykQBfXb.new_ones([NECAaWUrFGIXcLimrerEYmxYIykQBfXb.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[0]])
    iJNMljKhHywaTvselSjXSJkeAobJUZjA = lambda XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz: XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz.neg().exp()
    ocNKgMRHAumlFztHlKLWFgphgoqSohMJ = lambda njuvAJFseAnTpNXMmovFtOzaohoePSQs: njuvAJFseAnTpNXMmovFtOzaohoePSQs.DJwhOGBaLcOjmXnuwXMXOyhMtknqkKXL().neg()
    for HCXmerBqIMuTscBONzTGKYapYSxWTYHo in trange(len(ywkdEDhpSPXHYARENdFhpYnCzsLhiORy) - 1, disable=disable):
        ODAZKuAsCnodIahYkmGtylGzWplGUuPD = VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM(NECAaWUrFGIXcLimrerEYmxYIykQBfXb, ywkdEDhpSPXHYARENdFhpYnCzsLhiORy[HCXmerBqIMuTscBONzTGKYapYSxWTYHo] * moQRitRqIYEATNnahksUxyKeQfVQohNA, **TlJxtGydipTPezrPlUrxTKACQdhKNgvw)
        FEJQVZkfSRZklwwzvlTqxcIUgPGYvkPs, jfsUMkPasnZkDrBlHrfavWZhDulLllvc = EQrWJtFJAcWXVjwSXclhNFDOxYkkGfcF(ywkdEDhpSPXHYARENdFhpYnCzsLhiORy[HCXmerBqIMuTscBONzTGKYapYSxWTYHo], ywkdEDhpSPXHYARENdFhpYnCzsLhiORy[HCXmerBqIMuTscBONzTGKYapYSxWTYHo + 1], YifKHCfIbeEsuQSFLLpJatOOrlBeQSoO=YifKHCfIbeEsuQSFLLpJatOOrlBeQSoO)
        if FJsaFpOBdvpFlEdxOzBgjwcWBUfetQGF is not None:
            FJsaFpOBdvpFlEdxOzBgjwcWBUfetQGF({'x': NECAaWUrFGIXcLimrerEYmxYIykQBfXb, 'i': HCXmerBqIMuTscBONzTGKYapYSxWTYHo, 'sigma': ywkdEDhpSPXHYARENdFhpYnCzsLhiORy[HCXmerBqIMuTscBONzTGKYapYSxWTYHo], 'sigma_hat': ywkdEDhpSPXHYARENdFhpYnCzsLhiORy[HCXmerBqIMuTscBONzTGKYapYSxWTYHo], 'denoised': ODAZKuAsCnodIahYkmGtylGzWplGUuPD})
        if FEJQVZkfSRZklwwzvlTqxcIUgPGYvkPs == 0:
            TXGwYXNLgQsYzfHHpRBDJGFCFZEClzIo = wWkWWmmaMWzBivoGthogCOrDaHJcXRQg(NECAaWUrFGIXcLimrerEYmxYIykQBfXb, ywkdEDhpSPXHYARENdFhpYnCzsLhiORy[HCXmerBqIMuTscBONzTGKYapYSxWTYHo], ODAZKuAsCnodIahYkmGtylGzWplGUuPD)
            rYtAWlTfuJKXWhYOjYFOlRbQzowyoxFG = FEJQVZkfSRZklwwzvlTqxcIUgPGYvkPs - ywkdEDhpSPXHYARENdFhpYnCzsLhiORy[HCXmerBqIMuTscBONzTGKYapYSxWTYHo]
            NECAaWUrFGIXcLimrerEYmxYIykQBfXb = NECAaWUrFGIXcLimrerEYmxYIykQBfXb + TXGwYXNLgQsYzfHHpRBDJGFCFZEClzIo * rYtAWlTfuJKXWhYOjYFOlRbQzowyoxFG
        else:
            XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz, FeAWRnaTBNovNhgenUWGiCkgCADxZPHQ = ocNKgMRHAumlFztHlKLWFgphgoqSohMJ(ywkdEDhpSPXHYARENdFhpYnCzsLhiORy[HCXmerBqIMuTscBONzTGKYapYSxWTYHo]), ocNKgMRHAumlFztHlKLWFgphgoqSohMJ(FEJQVZkfSRZklwwzvlTqxcIUgPGYvkPs)
            r = 1 / 2
            xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab = FeAWRnaTBNovNhgenUWGiCkgCADxZPHQ - XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz
            uPePujIqMVDrwNvZQxJajkuaQFAcacjA = XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz + r * xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab
            kFbeKlGwETjnrOUnINvTygvTLgayPoOr = (iJNMljKhHywaTvselSjXSJkeAobJUZjA(uPePujIqMVDrwNvZQxJajkuaQFAcacjA) / iJNMljKhHywaTvselSjXSJkeAobJUZjA(XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz)) * NECAaWUrFGIXcLimrerEYmxYIykQBfXb - (-xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab * r).expm1() * ODAZKuAsCnodIahYkmGtylGzWplGUuPD
            BcIfZkiygxWOtTynEqPPtsxtqUsZCGOr = VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM(kFbeKlGwETjnrOUnINvTygvTLgayPoOr, iJNMljKhHywaTvselSjXSJkeAobJUZjA(uPePujIqMVDrwNvZQxJajkuaQFAcacjA) * moQRitRqIYEATNnahksUxyKeQfVQohNA, **TlJxtGydipTPezrPlUrxTKACQdhKNgvw)
            NECAaWUrFGIXcLimrerEYmxYIykQBfXb = (iJNMljKhHywaTvselSjXSJkeAobJUZjA(FeAWRnaTBNovNhgenUWGiCkgCADxZPHQ) / iJNMljKhHywaTvselSjXSJkeAobJUZjA(XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz)) * NECAaWUrFGIXcLimrerEYmxYIykQBfXb - (-xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab).expm1() * BcIfZkiygxWOtTynEqPPtsxtqUsZCGOr
        if ywkdEDhpSPXHYARENdFhpYnCzsLhiORy[HCXmerBqIMuTscBONzTGKYapYSxWTYHo + 1] > 0:
            NECAaWUrFGIXcLimrerEYmxYIykQBfXb = NECAaWUrFGIXcLimrerEYmxYIykQBfXb + ubyoEoHoKfVYweiaMPbKnyuENzoZHLei(ywkdEDhpSPXHYARENdFhpYnCzsLhiORy[HCXmerBqIMuTscBONzTGKYapYSxWTYHo], ywkdEDhpSPXHYARENdFhpYnCzsLhiORy[HCXmerBqIMuTscBONzTGKYapYSxWTYHo + 1]) * s_noise * jfsUMkPasnZkDrBlHrfavWZhDulLllvc
    return NECAaWUrFGIXcLimrerEYmxYIykQBfXb
@torch.no_grad()
def QRikJcRGHxTxaPvSvOzHyOJrgVxpnJnw(VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM, NECAaWUrFGIXcLimrerEYmxYIykQBfXb, ywkdEDhpSPXHYARENdFhpYnCzsLhiORy, TlJxtGydipTPezrPlUrxTKACQdhKNgvw=None, FJsaFpOBdvpFlEdxOzBgjwcWBUfetQGF=None, disable=None, YifKHCfIbeEsuQSFLLpJatOOrlBeQSoO=1., s_noise=1., ubyoEoHoKfVYweiaMPbKnyuENzoZHLei=None, r=1 / 2):
    FrgHMQrwGwxjLFZFaZndQasXgRhPXZyj, SjuBswrlxdwXAwbvIiTMrngJfAEFYXwe = ywkdEDhpSPXHYARENdFhpYnCzsLhiORy[ywkdEDhpSPXHYARENdFhpYnCzsLhiORy > 0].min(), ywkdEDhpSPXHYARENdFhpYnCzsLhiORy.max()
    qWZgfPzZGdBXrbWzvrSHUmcFFjBFiMVr = TlJxtGydipTPezrPlUrxTKACQdhKNgvw.get("seed", None)
    ubyoEoHoKfVYweiaMPbKnyuENzoZHLei = NKEocvhZhGGzDdsiFFqWYmrsPdkyJdwN(NECAaWUrFGIXcLimrerEYmxYIykQBfXb, FrgHMQrwGwxjLFZFaZndQasXgRhPXZyj, SjuBswrlxdwXAwbvIiTMrngJfAEFYXwe, qWZgfPzZGdBXrbWzvrSHUmcFFjBFiMVr=qWZgfPzZGdBXrbWzvrSHUmcFFjBFiMVr, cpu=True) if ubyoEoHoKfVYweiaMPbKnyuENzoZHLei is None else ubyoEoHoKfVYweiaMPbKnyuENzoZHLei
    TlJxtGydipTPezrPlUrxTKACQdhKNgvw = {} if TlJxtGydipTPezrPlUrxTKACQdhKNgvw is None else TlJxtGydipTPezrPlUrxTKACQdhKNgvw
    moQRitRqIYEATNnahksUxyKeQfVQohNA = NECAaWUrFGIXcLimrerEYmxYIykQBfXb.new_ones([NECAaWUrFGIXcLimrerEYmxYIykQBfXb.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[0]])
    iJNMljKhHywaTvselSjXSJkeAobJUZjA = lambda XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz: XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz.neg().exp()
    ocNKgMRHAumlFztHlKLWFgphgoqSohMJ = lambda njuvAJFseAnTpNXMmovFtOzaohoePSQs: njuvAJFseAnTpNXMmovFtOzaohoePSQs.DJwhOGBaLcOjmXnuwXMXOyhMtknqkKXL().neg()
    for HCXmerBqIMuTscBONzTGKYapYSxWTYHo in trange(len(ywkdEDhpSPXHYARENdFhpYnCzsLhiORy) - 1, disable=disable):
        ODAZKuAsCnodIahYkmGtylGzWplGUuPD = VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM(NECAaWUrFGIXcLimrerEYmxYIykQBfXb, ywkdEDhpSPXHYARENdFhpYnCzsLhiORy[HCXmerBqIMuTscBONzTGKYapYSxWTYHo] * moQRitRqIYEATNnahksUxyKeQfVQohNA, **TlJxtGydipTPezrPlUrxTKACQdhKNgvw)
        if FJsaFpOBdvpFlEdxOzBgjwcWBUfetQGF is not None:
            FJsaFpOBdvpFlEdxOzBgjwcWBUfetQGF({'x': NECAaWUrFGIXcLimrerEYmxYIykQBfXb, 'i': HCXmerBqIMuTscBONzTGKYapYSxWTYHo, 'sigma': ywkdEDhpSPXHYARENdFhpYnCzsLhiORy[HCXmerBqIMuTscBONzTGKYapYSxWTYHo], 'sigma_hat': ywkdEDhpSPXHYARENdFhpYnCzsLhiORy[HCXmerBqIMuTscBONzTGKYapYSxWTYHo], 'denoised': ODAZKuAsCnodIahYkmGtylGzWplGUuPD})
        if ywkdEDhpSPXHYARENdFhpYnCzsLhiORy[HCXmerBqIMuTscBONzTGKYapYSxWTYHo + 1] == 0:
            TXGwYXNLgQsYzfHHpRBDJGFCFZEClzIo = wWkWWmmaMWzBivoGthogCOrDaHJcXRQg(NECAaWUrFGIXcLimrerEYmxYIykQBfXb, ywkdEDhpSPXHYARENdFhpYnCzsLhiORy[HCXmerBqIMuTscBONzTGKYapYSxWTYHo], ODAZKuAsCnodIahYkmGtylGzWplGUuPD)
            rYtAWlTfuJKXWhYOjYFOlRbQzowyoxFG = ywkdEDhpSPXHYARENdFhpYnCzsLhiORy[HCXmerBqIMuTscBONzTGKYapYSxWTYHo + 1] - ywkdEDhpSPXHYARENdFhpYnCzsLhiORy[HCXmerBqIMuTscBONzTGKYapYSxWTYHo]
            NECAaWUrFGIXcLimrerEYmxYIykQBfXb = NECAaWUrFGIXcLimrerEYmxYIykQBfXb + TXGwYXNLgQsYzfHHpRBDJGFCFZEClzIo * rYtAWlTfuJKXWhYOjYFOlRbQzowyoxFG
        else:
            XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz, FeAWRnaTBNovNhgenUWGiCkgCADxZPHQ = ocNKgMRHAumlFztHlKLWFgphgoqSohMJ(ywkdEDhpSPXHYARENdFhpYnCzsLhiORy[HCXmerBqIMuTscBONzTGKYapYSxWTYHo]), ocNKgMRHAumlFztHlKLWFgphgoqSohMJ(ywkdEDhpSPXHYARENdFhpYnCzsLhiORy[HCXmerBqIMuTscBONzTGKYapYSxWTYHo + 1])
            xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab = FeAWRnaTBNovNhgenUWGiCkgCADxZPHQ - XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz
            uPePujIqMVDrwNvZQxJajkuaQFAcacjA = XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz + xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab * r
            dUdwyQTZywwzpMBUEMfJcciKbLwgFwkk = 1 / (2 * r)
            ylGhUFMpxPbtUUTfCZpemVkdanRhWmHa, WWLDnvOujbcGZhDStZqEqAbBZaJQZkVg = EQrWJtFJAcWXVjwSXclhNFDOxYkkGfcF(iJNMljKhHywaTvselSjXSJkeAobJUZjA(XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz), iJNMljKhHywaTvselSjXSJkeAobJUZjA(uPePujIqMVDrwNvZQxJajkuaQFAcacjA), YifKHCfIbeEsuQSFLLpJatOOrlBeQSoO)
            xGbtxSIyjuzSTkrGzwzrSnToNOCqXWiE = ocNKgMRHAumlFztHlKLWFgphgoqSohMJ(ylGhUFMpxPbtUUTfCZpemVkdanRhWmHa)
            kFbeKlGwETjnrOUnINvTygvTLgayPoOr = (iJNMljKhHywaTvselSjXSJkeAobJUZjA(xGbtxSIyjuzSTkrGzwzrSnToNOCqXWiE) / iJNMljKhHywaTvselSjXSJkeAobJUZjA(XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz)) * NECAaWUrFGIXcLimrerEYmxYIykQBfXb - (XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz - xGbtxSIyjuzSTkrGzwzrSnToNOCqXWiE).expm1() * ODAZKuAsCnodIahYkmGtylGzWplGUuPD
            kFbeKlGwETjnrOUnINvTygvTLgayPoOr = kFbeKlGwETjnrOUnINvTygvTLgayPoOr + ubyoEoHoKfVYweiaMPbKnyuENzoZHLei(iJNMljKhHywaTvselSjXSJkeAobJUZjA(XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz), iJNMljKhHywaTvselSjXSJkeAobJUZjA(uPePujIqMVDrwNvZQxJajkuaQFAcacjA)) * s_noise * WWLDnvOujbcGZhDStZqEqAbBZaJQZkVg
            BcIfZkiygxWOtTynEqPPtsxtqUsZCGOr = VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM(kFbeKlGwETjnrOUnINvTygvTLgayPoOr, iJNMljKhHywaTvselSjXSJkeAobJUZjA(uPePujIqMVDrwNvZQxJajkuaQFAcacjA) * moQRitRqIYEATNnahksUxyKeQfVQohNA, **TlJxtGydipTPezrPlUrxTKACQdhKNgvw)
            ylGhUFMpxPbtUUTfCZpemVkdanRhWmHa, WWLDnvOujbcGZhDStZqEqAbBZaJQZkVg = EQrWJtFJAcWXVjwSXclhNFDOxYkkGfcF(iJNMljKhHywaTvselSjXSJkeAobJUZjA(XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz), iJNMljKhHywaTvselSjXSJkeAobJUZjA(FeAWRnaTBNovNhgenUWGiCkgCADxZPHQ), YifKHCfIbeEsuQSFLLpJatOOrlBeQSoO)
            bYVlspJHAQeYetnvmXskpqNYdxqYkhnk = ocNKgMRHAumlFztHlKLWFgphgoqSohMJ(ylGhUFMpxPbtUUTfCZpemVkdanRhWmHa)
            rKSZfrRIFKbTvDlLGiZPNMcxKfBZimzE = (1 - dUdwyQTZywwzpMBUEMfJcciKbLwgFwkk) * ODAZKuAsCnodIahYkmGtylGzWplGUuPD + dUdwyQTZywwzpMBUEMfJcciKbLwgFwkk * BcIfZkiygxWOtTynEqPPtsxtqUsZCGOr
            NECAaWUrFGIXcLimrerEYmxYIykQBfXb = (iJNMljKhHywaTvselSjXSJkeAobJUZjA(bYVlspJHAQeYetnvmXskpqNYdxqYkhnk) / iJNMljKhHywaTvselSjXSJkeAobJUZjA(XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz)) * NECAaWUrFGIXcLimrerEYmxYIykQBfXb - (XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz - bYVlspJHAQeYetnvmXskpqNYdxqYkhnk).expm1() * rKSZfrRIFKbTvDlLGiZPNMcxKfBZimzE
            NECAaWUrFGIXcLimrerEYmxYIykQBfXb = NECAaWUrFGIXcLimrerEYmxYIykQBfXb + ubyoEoHoKfVYweiaMPbKnyuENzoZHLei(iJNMljKhHywaTvselSjXSJkeAobJUZjA(XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz), iJNMljKhHywaTvselSjXSJkeAobJUZjA(FeAWRnaTBNovNhgenUWGiCkgCADxZPHQ)) * s_noise * WWLDnvOujbcGZhDStZqEqAbBZaJQZkVg
    return NECAaWUrFGIXcLimrerEYmxYIykQBfXb
@torch.no_grad()
def mLCrRcghkbEZotZzvMYNlReioZaoihIc(VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM, NECAaWUrFGIXcLimrerEYmxYIykQBfXb, ywkdEDhpSPXHYARENdFhpYnCzsLhiORy, TlJxtGydipTPezrPlUrxTKACQdhKNgvw=None, FJsaFpOBdvpFlEdxOzBgjwcWBUfetQGF=None, disable=None):
    TlJxtGydipTPezrPlUrxTKACQdhKNgvw = {} if TlJxtGydipTPezrPlUrxTKACQdhKNgvw is None else TlJxtGydipTPezrPlUrxTKACQdhKNgvw
    moQRitRqIYEATNnahksUxyKeQfVQohNA = NECAaWUrFGIXcLimrerEYmxYIykQBfXb.new_ones([NECAaWUrFGIXcLimrerEYmxYIykQBfXb.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[0]])
    iJNMljKhHywaTvselSjXSJkeAobJUZjA = lambda XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz: XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz.neg().exp()
    ocNKgMRHAumlFztHlKLWFgphgoqSohMJ = lambda njuvAJFseAnTpNXMmovFtOzaohoePSQs: njuvAJFseAnTpNXMmovFtOzaohoePSQs.DJwhOGBaLcOjmXnuwXMXOyhMtknqkKXL().neg()
    ueXXLHoJXnpFxRYcHYZiKwSNTImJksbs = None
    for HCXmerBqIMuTscBONzTGKYapYSxWTYHo in trange(len(ywkdEDhpSPXHYARENdFhpYnCzsLhiORy) - 1, disable=disable):
        ODAZKuAsCnodIahYkmGtylGzWplGUuPD = VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM(NECAaWUrFGIXcLimrerEYmxYIykQBfXb, ywkdEDhpSPXHYARENdFhpYnCzsLhiORy[HCXmerBqIMuTscBONzTGKYapYSxWTYHo] * moQRitRqIYEATNnahksUxyKeQfVQohNA, **TlJxtGydipTPezrPlUrxTKACQdhKNgvw)
        if FJsaFpOBdvpFlEdxOzBgjwcWBUfetQGF is not None:
            FJsaFpOBdvpFlEdxOzBgjwcWBUfetQGF({'x': NECAaWUrFGIXcLimrerEYmxYIykQBfXb, 'i': HCXmerBqIMuTscBONzTGKYapYSxWTYHo, 'sigma': ywkdEDhpSPXHYARENdFhpYnCzsLhiORy[HCXmerBqIMuTscBONzTGKYapYSxWTYHo], 'sigma_hat': ywkdEDhpSPXHYARENdFhpYnCzsLhiORy[HCXmerBqIMuTscBONzTGKYapYSxWTYHo], 'denoised': ODAZKuAsCnodIahYkmGtylGzWplGUuPD})
        XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz, FeAWRnaTBNovNhgenUWGiCkgCADxZPHQ = ocNKgMRHAumlFztHlKLWFgphgoqSohMJ(ywkdEDhpSPXHYARENdFhpYnCzsLhiORy[HCXmerBqIMuTscBONzTGKYapYSxWTYHo]), ocNKgMRHAumlFztHlKLWFgphgoqSohMJ(ywkdEDhpSPXHYARENdFhpYnCzsLhiORy[HCXmerBqIMuTscBONzTGKYapYSxWTYHo + 1])
        xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab = FeAWRnaTBNovNhgenUWGiCkgCADxZPHQ - XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz
        if ueXXLHoJXnpFxRYcHYZiKwSNTImJksbs is None or ywkdEDhpSPXHYARENdFhpYnCzsLhiORy[HCXmerBqIMuTscBONzTGKYapYSxWTYHo + 1] == 0:
            NECAaWUrFGIXcLimrerEYmxYIykQBfXb = (iJNMljKhHywaTvselSjXSJkeAobJUZjA(FeAWRnaTBNovNhgenUWGiCkgCADxZPHQ) / iJNMljKhHywaTvselSjXSJkeAobJUZjA(XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz)) * NECAaWUrFGIXcLimrerEYmxYIykQBfXb - (-xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab).expm1() * ODAZKuAsCnodIahYkmGtylGzWplGUuPD
        else:
            CxMMXaDxrhzaisSNzJudfgSUMPNkfkZs = XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz - ocNKgMRHAumlFztHlKLWFgphgoqSohMJ(ywkdEDhpSPXHYARENdFhpYnCzsLhiORy[HCXmerBqIMuTscBONzTGKYapYSxWTYHo - 1])
            r = CxMMXaDxrhzaisSNzJudfgSUMPNkfkZs / xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab
            rKSZfrRIFKbTvDlLGiZPNMcxKfBZimzE = (1 + 1 / (2 * r)) * ODAZKuAsCnodIahYkmGtylGzWplGUuPD - (1 / (2 * r)) * ueXXLHoJXnpFxRYcHYZiKwSNTImJksbs
            NECAaWUrFGIXcLimrerEYmxYIykQBfXb = (iJNMljKhHywaTvselSjXSJkeAobJUZjA(FeAWRnaTBNovNhgenUWGiCkgCADxZPHQ) / iJNMljKhHywaTvselSjXSJkeAobJUZjA(XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz)) * NECAaWUrFGIXcLimrerEYmxYIykQBfXb - (-xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab).expm1() * rKSZfrRIFKbTvDlLGiZPNMcxKfBZimzE
        ueXXLHoJXnpFxRYcHYZiKwSNTImJksbs = ODAZKuAsCnodIahYkmGtylGzWplGUuPD
    return NECAaWUrFGIXcLimrerEYmxYIykQBfXb
@torch.no_grad()
def uNmHMVmlZIfozpWtWtfnPVRUoUgjiFfI(VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM, NECAaWUrFGIXcLimrerEYmxYIykQBfXb, ywkdEDhpSPXHYARENdFhpYnCzsLhiORy, TlJxtGydipTPezrPlUrxTKACQdhKNgvw=None, FJsaFpOBdvpFlEdxOzBgjwcWBUfetQGF=None, disable=None, YifKHCfIbeEsuQSFLLpJatOOrlBeQSoO=1., s_noise=1., ubyoEoHoKfVYweiaMPbKnyuENzoZHLei=None, clbgFKGfOFaPvTRBXwoouOOLgsSYaJzB='midpoint'):
    if clbgFKGfOFaPvTRBXwoouOOLgsSYaJzB not in {'heun', 'midpoint'}:
        raise ValueError('solver_type must be \'heun\' or \'midpoint\'')
    qWZgfPzZGdBXrbWzvrSHUmcFFjBFiMVr = TlJxtGydipTPezrPlUrxTKACQdhKNgvw.get("seed", None)
    FrgHMQrwGwxjLFZFaZndQasXgRhPXZyj, SjuBswrlxdwXAwbvIiTMrngJfAEFYXwe = ywkdEDhpSPXHYARENdFhpYnCzsLhiORy[ywkdEDhpSPXHYARENdFhpYnCzsLhiORy > 0].min(), ywkdEDhpSPXHYARENdFhpYnCzsLhiORy.max()
    ubyoEoHoKfVYweiaMPbKnyuENzoZHLei = NKEocvhZhGGzDdsiFFqWYmrsPdkyJdwN(NECAaWUrFGIXcLimrerEYmxYIykQBfXb, FrgHMQrwGwxjLFZFaZndQasXgRhPXZyj, SjuBswrlxdwXAwbvIiTMrngJfAEFYXwe, qWZgfPzZGdBXrbWzvrSHUmcFFjBFiMVr=qWZgfPzZGdBXrbWzvrSHUmcFFjBFiMVr, cpu=True) if ubyoEoHoKfVYweiaMPbKnyuENzoZHLei is None else ubyoEoHoKfVYweiaMPbKnyuENzoZHLei
    TlJxtGydipTPezrPlUrxTKACQdhKNgvw = {} if TlJxtGydipTPezrPlUrxTKACQdhKNgvw is None else TlJxtGydipTPezrPlUrxTKACQdhKNgvw
    moQRitRqIYEATNnahksUxyKeQfVQohNA = NECAaWUrFGIXcLimrerEYmxYIykQBfXb.new_ones([NECAaWUrFGIXcLimrerEYmxYIykQBfXb.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[0]])
    ueXXLHoJXnpFxRYcHYZiKwSNTImJksbs = None
    CxMMXaDxrhzaisSNzJudfgSUMPNkfkZs = None
    xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab = None
    for HCXmerBqIMuTscBONzTGKYapYSxWTYHo in trange(len(ywkdEDhpSPXHYARENdFhpYnCzsLhiORy) - 1, disable=disable):
        ODAZKuAsCnodIahYkmGtylGzWplGUuPD = VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM(NECAaWUrFGIXcLimrerEYmxYIykQBfXb, ywkdEDhpSPXHYARENdFhpYnCzsLhiORy[HCXmerBqIMuTscBONzTGKYapYSxWTYHo] * moQRitRqIYEATNnahksUxyKeQfVQohNA, **TlJxtGydipTPezrPlUrxTKACQdhKNgvw)
        if FJsaFpOBdvpFlEdxOzBgjwcWBUfetQGF is not None:
            FJsaFpOBdvpFlEdxOzBgjwcWBUfetQGF({'x': NECAaWUrFGIXcLimrerEYmxYIykQBfXb, 'i': HCXmerBqIMuTscBONzTGKYapYSxWTYHo, 'sigma': ywkdEDhpSPXHYARENdFhpYnCzsLhiORy[HCXmerBqIMuTscBONzTGKYapYSxWTYHo], 'sigma_hat': ywkdEDhpSPXHYARENdFhpYnCzsLhiORy[HCXmerBqIMuTscBONzTGKYapYSxWTYHo], 'denoised': ODAZKuAsCnodIahYkmGtylGzWplGUuPD})
        if ywkdEDhpSPXHYARENdFhpYnCzsLhiORy[HCXmerBqIMuTscBONzTGKYapYSxWTYHo + 1] == 0:
            NECAaWUrFGIXcLimrerEYmxYIykQBfXb = ODAZKuAsCnodIahYkmGtylGzWplGUuPD
        else:
            XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz, uPePujIqMVDrwNvZQxJajkuaQFAcacjA = -ywkdEDhpSPXHYARENdFhpYnCzsLhiORy[HCXmerBqIMuTscBONzTGKYapYSxWTYHo].DJwhOGBaLcOjmXnuwXMXOyhMtknqkKXL(), -ywkdEDhpSPXHYARENdFhpYnCzsLhiORy[HCXmerBqIMuTscBONzTGKYapYSxWTYHo + 1].DJwhOGBaLcOjmXnuwXMXOyhMtknqkKXL()
            xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab = uPePujIqMVDrwNvZQxJajkuaQFAcacjA - XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz
            vsjyXOaGpNISukdnqLpXahdvkXFTgQDj = YifKHCfIbeEsuQSFLLpJatOOrlBeQSoO * xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab
            NECAaWUrFGIXcLimrerEYmxYIykQBfXb = ywkdEDhpSPXHYARENdFhpYnCzsLhiORy[HCXmerBqIMuTscBONzTGKYapYSxWTYHo + 1] / ywkdEDhpSPXHYARENdFhpYnCzsLhiORy[HCXmerBqIMuTscBONzTGKYapYSxWTYHo] * (-vsjyXOaGpNISukdnqLpXahdvkXFTgQDj).exp() * NECAaWUrFGIXcLimrerEYmxYIykQBfXb + (-xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab - vsjyXOaGpNISukdnqLpXahdvkXFTgQDj).expm1().neg() * ODAZKuAsCnodIahYkmGtylGzWplGUuPD
            if ueXXLHoJXnpFxRYcHYZiKwSNTImJksbs is not None:
                r = CxMMXaDxrhzaisSNzJudfgSUMPNkfkZs / xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab
                if clbgFKGfOFaPvTRBXwoouOOLgsSYaJzB == 'heun':
                    NECAaWUrFGIXcLimrerEYmxYIykQBfXb = NECAaWUrFGIXcLimrerEYmxYIykQBfXb + ((-xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab - vsjyXOaGpNISukdnqLpXahdvkXFTgQDj).expm1().neg() / (-xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab - vsjyXOaGpNISukdnqLpXahdvkXFTgQDj) + 1) * (1 / r) * (ODAZKuAsCnodIahYkmGtylGzWplGUuPD - ueXXLHoJXnpFxRYcHYZiKwSNTImJksbs)
                elif clbgFKGfOFaPvTRBXwoouOOLgsSYaJzB == 'midpoint':
                    NECAaWUrFGIXcLimrerEYmxYIykQBfXb = NECAaWUrFGIXcLimrerEYmxYIykQBfXb + 0.5 * (-xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab - vsjyXOaGpNISukdnqLpXahdvkXFTgQDj).expm1().neg() * (1 / r) * (ODAZKuAsCnodIahYkmGtylGzWplGUuPD - ueXXLHoJXnpFxRYcHYZiKwSNTImJksbs)
            if YifKHCfIbeEsuQSFLLpJatOOrlBeQSoO:
                NECAaWUrFGIXcLimrerEYmxYIykQBfXb = NECAaWUrFGIXcLimrerEYmxYIykQBfXb + ubyoEoHoKfVYweiaMPbKnyuENzoZHLei(ywkdEDhpSPXHYARENdFhpYnCzsLhiORy[HCXmerBqIMuTscBONzTGKYapYSxWTYHo], ywkdEDhpSPXHYARENdFhpYnCzsLhiORy[HCXmerBqIMuTscBONzTGKYapYSxWTYHo + 1]) * ywkdEDhpSPXHYARENdFhpYnCzsLhiORy[HCXmerBqIMuTscBONzTGKYapYSxWTYHo + 1] * (-2 * vsjyXOaGpNISukdnqLpXahdvkXFTgQDj).expm1().neg().sqrt() * s_noise
        ueXXLHoJXnpFxRYcHYZiKwSNTImJksbs = ODAZKuAsCnodIahYkmGtylGzWplGUuPD
        CxMMXaDxrhzaisSNzJudfgSUMPNkfkZs = xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab
    return NECAaWUrFGIXcLimrerEYmxYIykQBfXb
@torch.no_grad()
def GsPANuUcgsjHGkTyeIQySWJIyyoltTqj(VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM, NECAaWUrFGIXcLimrerEYmxYIykQBfXb, ywkdEDhpSPXHYARENdFhpYnCzsLhiORy, TlJxtGydipTPezrPlUrxTKACQdhKNgvw=None, FJsaFpOBdvpFlEdxOzBgjwcWBUfetQGF=None, disable=None, YifKHCfIbeEsuQSFLLpJatOOrlBeQSoO=1., s_noise=1., ubyoEoHoKfVYweiaMPbKnyuENzoZHLei=None):
    qWZgfPzZGdBXrbWzvrSHUmcFFjBFiMVr = TlJxtGydipTPezrPlUrxTKACQdhKNgvw.get("seed", None)
    FrgHMQrwGwxjLFZFaZndQasXgRhPXZyj, SjuBswrlxdwXAwbvIiTMrngJfAEFYXwe = ywkdEDhpSPXHYARENdFhpYnCzsLhiORy[ywkdEDhpSPXHYARENdFhpYnCzsLhiORy > 0].min(), ywkdEDhpSPXHYARENdFhpYnCzsLhiORy.max()
    ubyoEoHoKfVYweiaMPbKnyuENzoZHLei = NKEocvhZhGGzDdsiFFqWYmrsPdkyJdwN(NECAaWUrFGIXcLimrerEYmxYIykQBfXb, FrgHMQrwGwxjLFZFaZndQasXgRhPXZyj, SjuBswrlxdwXAwbvIiTMrngJfAEFYXwe, qWZgfPzZGdBXrbWzvrSHUmcFFjBFiMVr=qWZgfPzZGdBXrbWzvrSHUmcFFjBFiMVr, cpu=True) if ubyoEoHoKfVYweiaMPbKnyuENzoZHLei is None else ubyoEoHoKfVYweiaMPbKnyuENzoZHLei
    TlJxtGydipTPezrPlUrxTKACQdhKNgvw = {} if TlJxtGydipTPezrPlUrxTKACQdhKNgvw is None else TlJxtGydipTPezrPlUrxTKACQdhKNgvw
    moQRitRqIYEATNnahksUxyKeQfVQohNA = NECAaWUrFGIXcLimrerEYmxYIykQBfXb.new_ones([NECAaWUrFGIXcLimrerEYmxYIykQBfXb.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[0]])
    SIAhnrRYZKAdFiRAoAIjMieqUGNFPJks, BcIfZkiygxWOtTynEqPPtsxtqUsZCGOr = None, None
    xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab, WWYRPNkUKTAWHUatYWDtFEQZUJYCgYhA, odURDvLMVCAWjoNhpFhQPFcQPfPXPepU = None, None, None
    for HCXmerBqIMuTscBONzTGKYapYSxWTYHo in trange(len(ywkdEDhpSPXHYARENdFhpYnCzsLhiORy) - 1, disable=disable):
        ODAZKuAsCnodIahYkmGtylGzWplGUuPD = VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM(NECAaWUrFGIXcLimrerEYmxYIykQBfXb, ywkdEDhpSPXHYARENdFhpYnCzsLhiORy[HCXmerBqIMuTscBONzTGKYapYSxWTYHo] * moQRitRqIYEATNnahksUxyKeQfVQohNA, **TlJxtGydipTPezrPlUrxTKACQdhKNgvw)
        if FJsaFpOBdvpFlEdxOzBgjwcWBUfetQGF is not None:
            FJsaFpOBdvpFlEdxOzBgjwcWBUfetQGF({'x': NECAaWUrFGIXcLimrerEYmxYIykQBfXb, 'i': HCXmerBqIMuTscBONzTGKYapYSxWTYHo, 'sigma': ywkdEDhpSPXHYARENdFhpYnCzsLhiORy[HCXmerBqIMuTscBONzTGKYapYSxWTYHo], 'sigma_hat': ywkdEDhpSPXHYARENdFhpYnCzsLhiORy[HCXmerBqIMuTscBONzTGKYapYSxWTYHo], 'denoised': ODAZKuAsCnodIahYkmGtylGzWplGUuPD})
        if ywkdEDhpSPXHYARENdFhpYnCzsLhiORy[HCXmerBqIMuTscBONzTGKYapYSxWTYHo + 1] == 0:
            NECAaWUrFGIXcLimrerEYmxYIykQBfXb = ODAZKuAsCnodIahYkmGtylGzWplGUuPD
        else:
            XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz, uPePujIqMVDrwNvZQxJajkuaQFAcacjA = -ywkdEDhpSPXHYARENdFhpYnCzsLhiORy[HCXmerBqIMuTscBONzTGKYapYSxWTYHo].DJwhOGBaLcOjmXnuwXMXOyhMtknqkKXL(), -ywkdEDhpSPXHYARENdFhpYnCzsLhiORy[HCXmerBqIMuTscBONzTGKYapYSxWTYHo + 1].DJwhOGBaLcOjmXnuwXMXOyhMtknqkKXL()
            xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab = uPePujIqMVDrwNvZQxJajkuaQFAcacjA - XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz
            HvMtcLMkYOgBajunBiNciNYZrgUexevn = xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab * (YifKHCfIbeEsuQSFLLpJatOOrlBeQSoO + 1)
            NECAaWUrFGIXcLimrerEYmxYIykQBfXb = torch.exp(-HvMtcLMkYOgBajunBiNciNYZrgUexevn) * NECAaWUrFGIXcLimrerEYmxYIykQBfXb + (-HvMtcLMkYOgBajunBiNciNYZrgUexevn).expm1().neg() * ODAZKuAsCnodIahYkmGtylGzWplGUuPD
            if odURDvLMVCAWjoNhpFhQPFcQPfPXPepU is not None:
                aNnhgvGSzDOfunNUFPhsrxktbnXzLhMl = WWYRPNkUKTAWHUatYWDtFEQZUJYCgYhA / xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab
                apACmNWgYmlQTXHPQlhMzlFpreaoNbwW = odURDvLMVCAWjoNhpFhQPFcQPfPXPepU / xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab
                BuOKAoOadeFDehIzNrjhsKWYpzeDxJvv = (ODAZKuAsCnodIahYkmGtylGzWplGUuPD - SIAhnrRYZKAdFiRAoAIjMieqUGNFPJks) / aNnhgvGSzDOfunNUFPhsrxktbnXzLhMl
                pLnXFBBVVTvPLoFwyFPIDmkVDLfvHXLU = (SIAhnrRYZKAdFiRAoAIjMieqUGNFPJks - BcIfZkiygxWOtTynEqPPtsxtqUsZCGOr) / apACmNWgYmlQTXHPQlhMzlFpreaoNbwW
                tbuZnqNEmikCJaKNSLmSqWpMDYVUBzXX = BuOKAoOadeFDehIzNrjhsKWYpzeDxJvv + (BuOKAoOadeFDehIzNrjhsKWYpzeDxJvv - pLnXFBBVVTvPLoFwyFPIDmkVDLfvHXLU) * aNnhgvGSzDOfunNUFPhsrxktbnXzLhMl / (aNnhgvGSzDOfunNUFPhsrxktbnXzLhMl + apACmNWgYmlQTXHPQlhMzlFpreaoNbwW)
                qmVBooQzqysdVWXJerZDBEhryENmpgND = (BuOKAoOadeFDehIzNrjhsKWYpzeDxJvv - pLnXFBBVVTvPLoFwyFPIDmkVDLfvHXLU) / (aNnhgvGSzDOfunNUFPhsrxktbnXzLhMl + apACmNWgYmlQTXHPQlhMzlFpreaoNbwW)
                sSoPaxtPkFmuEwlZOSGoifpOhiJjZods = HvMtcLMkYOgBajunBiNciNYZrgUexevn.neg().expm1() / HvMtcLMkYOgBajunBiNciNYZrgUexevn + 1
                vQCArAadlVzodMvevsCjAxlkZoNodHrO = sSoPaxtPkFmuEwlZOSGoifpOhiJjZods / HvMtcLMkYOgBajunBiNciNYZrgUexevn - 0.5
                NECAaWUrFGIXcLimrerEYmxYIykQBfXb = NECAaWUrFGIXcLimrerEYmxYIykQBfXb + sSoPaxtPkFmuEwlZOSGoifpOhiJjZods * tbuZnqNEmikCJaKNSLmSqWpMDYVUBzXX - vQCArAadlVzodMvevsCjAxlkZoNodHrO * qmVBooQzqysdVWXJerZDBEhryENmpgND
            elif WWYRPNkUKTAWHUatYWDtFEQZUJYCgYhA is not None:
                r = WWYRPNkUKTAWHUatYWDtFEQZUJYCgYhA / xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab
                TXGwYXNLgQsYzfHHpRBDJGFCFZEClzIo = (ODAZKuAsCnodIahYkmGtylGzWplGUuPD - SIAhnrRYZKAdFiRAoAIjMieqUGNFPJks) / r
                sSoPaxtPkFmuEwlZOSGoifpOhiJjZods = HvMtcLMkYOgBajunBiNciNYZrgUexevn.neg().expm1() / HvMtcLMkYOgBajunBiNciNYZrgUexevn + 1
                NECAaWUrFGIXcLimrerEYmxYIykQBfXb = NECAaWUrFGIXcLimrerEYmxYIykQBfXb + sSoPaxtPkFmuEwlZOSGoifpOhiJjZods * TXGwYXNLgQsYzfHHpRBDJGFCFZEClzIo
            if YifKHCfIbeEsuQSFLLpJatOOrlBeQSoO:
                NECAaWUrFGIXcLimrerEYmxYIykQBfXb = NECAaWUrFGIXcLimrerEYmxYIykQBfXb + ubyoEoHoKfVYweiaMPbKnyuENzoZHLei(ywkdEDhpSPXHYARENdFhpYnCzsLhiORy[HCXmerBqIMuTscBONzTGKYapYSxWTYHo], ywkdEDhpSPXHYARENdFhpYnCzsLhiORy[HCXmerBqIMuTscBONzTGKYapYSxWTYHo + 1]) * ywkdEDhpSPXHYARENdFhpYnCzsLhiORy[HCXmerBqIMuTscBONzTGKYapYSxWTYHo + 1] * (-2 * xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab * YifKHCfIbeEsuQSFLLpJatOOrlBeQSoO).expm1().neg().sqrt() * s_noise
        SIAhnrRYZKAdFiRAoAIjMieqUGNFPJks, BcIfZkiygxWOtTynEqPPtsxtqUsZCGOr = ODAZKuAsCnodIahYkmGtylGzWplGUuPD, SIAhnrRYZKAdFiRAoAIjMieqUGNFPJks
        WWYRPNkUKTAWHUatYWDtFEQZUJYCgYhA, odURDvLMVCAWjoNhpFhQPFcQPfPXPepU = xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab, WWYRPNkUKTAWHUatYWDtFEQZUJYCgYhA
    return NECAaWUrFGIXcLimrerEYmxYIykQBfXb
@torch.no_grad()
def ajpILspJdcYSCWKOpWipfPxtgCkReUEz(VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM, NECAaWUrFGIXcLimrerEYmxYIykQBfXb, ywkdEDhpSPXHYARENdFhpYnCzsLhiORy, TlJxtGydipTPezrPlUrxTKACQdhKNgvw=None, FJsaFpOBdvpFlEdxOzBgjwcWBUfetQGF=None, disable=None, YifKHCfIbeEsuQSFLLpJatOOrlBeQSoO=1., s_noise=1., ubyoEoHoKfVYweiaMPbKnyuENzoZHLei=None):
    FrgHMQrwGwxjLFZFaZndQasXgRhPXZyj, SjuBswrlxdwXAwbvIiTMrngJfAEFYXwe = ywkdEDhpSPXHYARENdFhpYnCzsLhiORy[ywkdEDhpSPXHYARENdFhpYnCzsLhiORy > 0].min(), ywkdEDhpSPXHYARENdFhpYnCzsLhiORy.max()
    ubyoEoHoKfVYweiaMPbKnyuENzoZHLei = NKEocvhZhGGzDdsiFFqWYmrsPdkyJdwN(NECAaWUrFGIXcLimrerEYmxYIykQBfXb, FrgHMQrwGwxjLFZFaZndQasXgRhPXZyj, SjuBswrlxdwXAwbvIiTMrngJfAEFYXwe, qWZgfPzZGdBXrbWzvrSHUmcFFjBFiMVr=TlJxtGydipTPezrPlUrxTKACQdhKNgvw.get("seed", None), cpu=False) if ubyoEoHoKfVYweiaMPbKnyuENzoZHLei is None else ubyoEoHoKfVYweiaMPbKnyuENzoZHLei
    return GsPANuUcgsjHGkTyeIQySWJIyyoltTqj(VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM, NECAaWUrFGIXcLimrerEYmxYIykQBfXb, ywkdEDhpSPXHYARENdFhpYnCzsLhiORy, TlJxtGydipTPezrPlUrxTKACQdhKNgvw=TlJxtGydipTPezrPlUrxTKACQdhKNgvw, FJsaFpOBdvpFlEdxOzBgjwcWBUfetQGF=FJsaFpOBdvpFlEdxOzBgjwcWBUfetQGF, disable=disable, YifKHCfIbeEsuQSFLLpJatOOrlBeQSoO=YifKHCfIbeEsuQSFLLpJatOOrlBeQSoO, s_noise=s_noise, ubyoEoHoKfVYweiaMPbKnyuENzoZHLei=ubyoEoHoKfVYweiaMPbKnyuENzoZHLei)
@torch.no_grad()
def PaJXRHhJlLsQTOEUIYargwwHoGufrEiR(VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM, NECAaWUrFGIXcLimrerEYmxYIykQBfXb, ywkdEDhpSPXHYARENdFhpYnCzsLhiORy, TlJxtGydipTPezrPlUrxTKACQdhKNgvw=None, FJsaFpOBdvpFlEdxOzBgjwcWBUfetQGF=None, disable=None, YifKHCfIbeEsuQSFLLpJatOOrlBeQSoO=1., s_noise=1., ubyoEoHoKfVYweiaMPbKnyuENzoZHLei=None, clbgFKGfOFaPvTRBXwoouOOLgsSYaJzB='midpoint'):
    FrgHMQrwGwxjLFZFaZndQasXgRhPXZyj, SjuBswrlxdwXAwbvIiTMrngJfAEFYXwe = ywkdEDhpSPXHYARENdFhpYnCzsLhiORy[ywkdEDhpSPXHYARENdFhpYnCzsLhiORy > 0].min(), ywkdEDhpSPXHYARENdFhpYnCzsLhiORy.max()
    ubyoEoHoKfVYweiaMPbKnyuENzoZHLei = NKEocvhZhGGzDdsiFFqWYmrsPdkyJdwN(NECAaWUrFGIXcLimrerEYmxYIykQBfXb, FrgHMQrwGwxjLFZFaZndQasXgRhPXZyj, SjuBswrlxdwXAwbvIiTMrngJfAEFYXwe, qWZgfPzZGdBXrbWzvrSHUmcFFjBFiMVr=TlJxtGydipTPezrPlUrxTKACQdhKNgvw.get("seed", None), cpu=False) if ubyoEoHoKfVYweiaMPbKnyuENzoZHLei is None else ubyoEoHoKfVYweiaMPbKnyuENzoZHLei
    return uNmHMVmlZIfozpWtWtfnPVRUoUgjiFfI(VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM, NECAaWUrFGIXcLimrerEYmxYIykQBfXb, ywkdEDhpSPXHYARENdFhpYnCzsLhiORy, TlJxtGydipTPezrPlUrxTKACQdhKNgvw=TlJxtGydipTPezrPlUrxTKACQdhKNgvw, FJsaFpOBdvpFlEdxOzBgjwcWBUfetQGF=FJsaFpOBdvpFlEdxOzBgjwcWBUfetQGF, disable=disable, YifKHCfIbeEsuQSFLLpJatOOrlBeQSoO=YifKHCfIbeEsuQSFLLpJatOOrlBeQSoO, s_noise=s_noise, ubyoEoHoKfVYweiaMPbKnyuENzoZHLei=ubyoEoHoKfVYweiaMPbKnyuENzoZHLei, clbgFKGfOFaPvTRBXwoouOOLgsSYaJzB=clbgFKGfOFaPvTRBXwoouOOLgsSYaJzB)
@torch.no_grad()
def RtidtItaVjCLMmrjlxMnBZYmZgltTGen(VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM, NECAaWUrFGIXcLimrerEYmxYIykQBfXb, ywkdEDhpSPXHYARENdFhpYnCzsLhiORy, TlJxtGydipTPezrPlUrxTKACQdhKNgvw=None, FJsaFpOBdvpFlEdxOzBgjwcWBUfetQGF=None, disable=None, YifKHCfIbeEsuQSFLLpJatOOrlBeQSoO=1., s_noise=1., ubyoEoHoKfVYweiaMPbKnyuENzoZHLei=None, r=1 / 2):
    FrgHMQrwGwxjLFZFaZndQasXgRhPXZyj, SjuBswrlxdwXAwbvIiTMrngJfAEFYXwe = ywkdEDhpSPXHYARENdFhpYnCzsLhiORy[ywkdEDhpSPXHYARENdFhpYnCzsLhiORy > 0].min(), ywkdEDhpSPXHYARENdFhpYnCzsLhiORy.max()
    ubyoEoHoKfVYweiaMPbKnyuENzoZHLei = NKEocvhZhGGzDdsiFFqWYmrsPdkyJdwN(NECAaWUrFGIXcLimrerEYmxYIykQBfXb, FrgHMQrwGwxjLFZFaZndQasXgRhPXZyj, SjuBswrlxdwXAwbvIiTMrngJfAEFYXwe, qWZgfPzZGdBXrbWzvrSHUmcFFjBFiMVr=TlJxtGydipTPezrPlUrxTKACQdhKNgvw.get("seed", None), cpu=False) if ubyoEoHoKfVYweiaMPbKnyuENzoZHLei is None else ubyoEoHoKfVYweiaMPbKnyuENzoZHLei
    return QRikJcRGHxTxaPvSvOzHyOJrgVxpnJnw(VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM, NECAaWUrFGIXcLimrerEYmxYIykQBfXb, ywkdEDhpSPXHYARENdFhpYnCzsLhiORy, TlJxtGydipTPezrPlUrxTKACQdhKNgvw=TlJxtGydipTPezrPlUrxTKACQdhKNgvw, FJsaFpOBdvpFlEdxOzBgjwcWBUfetQGF=FJsaFpOBdvpFlEdxOzBgjwcWBUfetQGF, disable=disable, YifKHCfIbeEsuQSFLLpJatOOrlBeQSoO=YifKHCfIbeEsuQSFLLpJatOOrlBeQSoO, s_noise=s_noise, ubyoEoHoKfVYweiaMPbKnyuENzoZHLei=ubyoEoHoKfVYweiaMPbKnyuENzoZHLei, r=r)
