from contextlib import contextmanager
import hashlib
import math
from pathlib import Path
import shutil
import urllib
import warnings
from PIL import Image
import torch
from torch import nn, optim
from torch.utils import data
def laBtnXdTXepYzjECSDUryQSPzABKYFbB(examples, transform, gCkWoUSaMffhaFfOObjYTyhEKjQylPOz, bPTwwoDdWiuYqhtrDEHoDbHGiYcwcsQC='RGB'):
    kgLFMdERvjTWIqzUwaTgEZNsXvktcIDW = [transform(eLyJtroPthPCROYWyMphoIrGatNOOXCO.convert(bPTwwoDdWiuYqhtrDEHoDbHGiYcwcsQC)) for eLyJtroPthPCROYWyMphoIrGatNOOXCO in examples[gCkWoUSaMffhaFfOObjYTyhEKjQylPOz]]
    return {gCkWoUSaMffhaFfOObjYTyhEKjQylPOz: kgLFMdERvjTWIqzUwaTgEZNsXvktcIDW}
def CMxxOxdPTSrjIzfwUpFYdWOyWfmNnQNF(NECAaWUrFGIXcLimrerEYmxYIykQBfXb, target_dims):
    QiRZNddHeMNZMeQGOXQJGIdEqODiwlSP = target_dims - NECAaWUrFGIXcLimrerEYmxYIykQBfXb.ndim
    if QiRZNddHeMNZMeQGOXQJGIdEqODiwlSP < 0:
        raise ValueError(f'input has {x.ndim} dims but target_dims is {target_dims}, which is less')
    HthxDLxzAIsfoXjVhdkDOIkulknDYkXt = NECAaWUrFGIXcLimrerEYmxYIykQBfXb[(...,) + (None,) * QiRZNddHeMNZMeQGOXQJGIdEqODiwlSP]
    return HthxDLxzAIsfoXjVhdkDOIkulknDYkXt.detach().tEcQvpBwXwdqvKxRTLEBROBUyPoodldL() if HthxDLxzAIsfoXjVhdkDOIkulknDYkXt.fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc.type == 'mps' else HthxDLxzAIsfoXjVhdkDOIkulknDYkXt
def PwJzymvvoojavDaJkLCXUcIrPqjaJEwc(FRIBQCDfDDxIonplwxvPCicvOmmOgYPC):
    return sum(HutkrxeXIuRQKOhCWHkiwqLGAsJjUSKj.numel() for HutkrxeXIuRQKOhCWHkiwqLGAsJjUSKj in FRIBQCDfDDxIonplwxvPCicvOmmOgYPC.parameters())
def jVeqrMSEwOBLsWhruTZzfRzUWRfuZGGQ(path, url, digest=None):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists():
        with urllib.request.urlopen(url) as HQlvpyIUUfnfAqKdXyNavyxWXIZkebhk, open(path, 'wb') as f:
            shutil.copyfileobj(HQlvpyIUUfnfAqKdXyNavyxWXIZkebhk, f)
    if digest is not None:
        kpNtVjVmmsmopYNhoukvXPvVaTccjSNs = hashlib.sha256(open(path, 'rb').read()).hexdigest()
        if digest != kpNtVjVmmsmopYNhoukvXPvVaTccjSNs:
            raise OSError(f'hash of {path} (url: {url}) failed to validate')
    return path
@contextmanager
def gzsaxinHqFCHkVAPwBPjEHdKjdvuZYAQ(VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM, bPTwwoDdWiuYqhtrDEHoDbHGiYcwcsQC=True):
    dCjHnaMauOPDOhrflhhKTHvlhkmATAlA = [FRIBQCDfDDxIonplwxvPCicvOmmOgYPC.training for FRIBQCDfDDxIonplwxvPCicvOmmOgYPC in VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM.modules()]
    try:
        yield VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM.train(bPTwwoDdWiuYqhtrDEHoDbHGiYcwcsQC)
    finally:
        for HCXmerBqIMuTscBONzTGKYapYSxWTYHo, FRIBQCDfDDxIonplwxvPCicvOmmOgYPC in enumerate(VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM.modules()):
            FRIBQCDfDDxIonplwxvPCicvOmmOgYPC.training = dCjHnaMauOPDOhrflhhKTHvlhkmATAlA[HCXmerBqIMuTscBONzTGKYapYSxWTYHo]
def pYZoMJfhYvcBNIHLRMPtmFGaTUbWxWXU(VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM):
    return gzsaxinHqFCHkVAPwBPjEHdKjdvuZYAQ(VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM, False)
@torch.no_grad()
def yyWaFzdOtJjUoPbjcnMdZOoSVzjhtGQq(VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM, averaged_model, eeehCkWlicOSSZeEWMocEIpaDJxlRTfD):
    PdGWiWNrDwHLuxVqHGwwISTXDvUzkDgP = dict(VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM.named_parameters())
    ssxkwYsFbNZdTHZiEKwzxHRpdkWLnjlx = dict(averaged_model.named_parameters())
    assert PdGWiWNrDwHLuxVqHGwwISTXDvUzkDgP.keys() == ssxkwYsFbNZdTHZiEKwzxHRpdkWLnjlx.keys()
    for pSfJNVvqLWVlUeHdpahCTGSrSPJYAnEQ, wqONwpPqzusAImUvAyPmoTAxAbxfcvHV in PdGWiWNrDwHLuxVqHGwwISTXDvUzkDgP.items():
        ssxkwYsFbNZdTHZiEKwzxHRpdkWLnjlx[pSfJNVvqLWVlUeHdpahCTGSrSPJYAnEQ].mul_(eeehCkWlicOSSZeEWMocEIpaDJxlRTfD).add_(wqONwpPqzusAImUvAyPmoTAxAbxfcvHV, uigKGapaQVcFiOjEiWwRAHjjkAWxsqck=1 - eeehCkWlicOSSZeEWMocEIpaDJxlRTfD)
    qPLtxWnhxftsSAYZmlGtdyOkBwnUdwgP = dict(VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM.named_buffers())
    QaFhcdpHHReMPKHnOCfkWYARCgJItCAq = dict(averaged_model.named_buffers())
    assert qPLtxWnhxftsSAYZmlGtdyOkBwnUdwgP.keys() == QaFhcdpHHReMPKHnOCfkWYARCgJItCAq.keys()
    for pSfJNVvqLWVlUeHdpahCTGSrSPJYAnEQ, ubjDIQVqxUMutpqSGhbwVzGikBuhWDVX in qPLtxWnhxftsSAYZmlGtdyOkBwnUdwgP.items():
        QaFhcdpHHReMPKHnOCfkWYARCgJItCAq[pSfJNVvqLWVlUeHdpahCTGSrSPJYAnEQ].copy_(ubjDIQVqxUMutpqSGhbwVzGikBuhWDVX)
class AwSTvhnKDKoohhqsIfTPaXnBQsyNEElU:
    def __init__(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, inv_gamma=1., power=1., xDHXyZxnTpgTIUWmlIOPGEtWVzfhHsDh=0., xPSUMHJpcKTzcLMKKmAzyKtzHGhYpbqS=1., start_at=0,
                 AXGNHRRRaXEGosLBtJYejDSeliYPSxwB=0):
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.inv_gamma = inv_gamma
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.power = power
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.xDHXyZxnTpgTIUWmlIOPGEtWVzfhHsDh = xDHXyZxnTpgTIUWmlIOPGEtWVzfhHsDh
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.xPSUMHJpcKTzcLMKKmAzyKtzHGhYpbqS = xPSUMHJpcKTzcLMKKmAzyKtzHGhYpbqS
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.start_at = start_at
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.AXGNHRRRaXEGosLBtJYejDSeliYPSxwB = AXGNHRRRaXEGosLBtJYejDSeliYPSxwB
    def TQRgUMPjEwYAaDvSuzgvheADStCoUKzT(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS):
        return dict(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.__dict__.items())
    def OVlRwgmJvqggImaZMfxKZfQnVYfyhIsc(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, TQRgUMPjEwYAaDvSuzgvheADStCoUKzT):
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.__dict__.update(TQRgUMPjEwYAaDvSuzgvheADStCoUKzT)
    def AXaAXdtcayWeFmkjLuhWJXtMBmMnXGXY(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS):
        OrPxrXTjZphGVjJTbFubBQpTMwArXbTi = max(0, rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.AXGNHRRRaXEGosLBtJYejDSeliYPSxwB - rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.start_at)
        value = 1 - (1 + OrPxrXTjZphGVjJTbFubBQpTMwArXbTi / rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.inv_gamma) ** -rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.power
        return 0. if OrPxrXTjZphGVjJTbFubBQpTMwArXbTi < 0 else min(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.xPSUMHJpcKTzcLMKKmAzyKtzHGhYpbqS, max(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.xDHXyZxnTpgTIUWmlIOPGEtWVzfhHsDh, value))
    def UHmIQCHeLkozPfaktIdEHKdpTVYzCLhe(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS):
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.AXGNHRRRaXEGosLBtJYejDSeliYPSxwB += 1
class wVZMTmaNHfHWFkxhObGcDYJTeYoKpJGq(optim.lr_scheduler._LRScheduler):
    def __init__(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, optimizer, inv_gamma=1., power=1., BPIFlVyCbIpSBAFKbXcCgjitvQJkMYGa=0., min_lr=0.,
                 AXGNHRRRaXEGosLBtJYejDSeliYPSxwB=-1, aFZoJwWpCnqyOJdcAMLlqOHxDgjPTNCS=False):
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.inv_gamma = inv_gamma
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.power = power
        if not 0. <= BPIFlVyCbIpSBAFKbXcCgjitvQJkMYGa < 1:
            raise ValueError('Invalid value for warmup')
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.BPIFlVyCbIpSBAFKbXcCgjitvQJkMYGa = BPIFlVyCbIpSBAFKbXcCgjitvQJkMYGa
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.min_lr = min_lr
        super().__init__(optimizer, AXGNHRRRaXEGosLBtJYejDSeliYPSxwB, aFZoJwWpCnqyOJdcAMLlqOHxDgjPTNCS)
    def XyyizfZZExIQuvyyTwLRBKBGMPpWAWES(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS):
        if not rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS._get_lr_called_within_step:
            warnings.warn("To get the last learning rate computed by the scheduler, "
                          "please use `get_last_lr()`.")
        return rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.FNOuVtiQFkqRVsVuScLhhmjlgTgNSllF()
    def FNOuVtiQFkqRVsVuScLhhmjlgTgNSllF(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS):
        BPIFlVyCbIpSBAFKbXcCgjitvQJkMYGa = 1 - rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.BPIFlVyCbIpSBAFKbXcCgjitvQJkMYGa ** (rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.AXGNHRRRaXEGosLBtJYejDSeliYPSxwB + 1)
        weVkLCBWUuKbvEHWMEsdwxqqchyDuLtQ = (1 + rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.AXGNHRRRaXEGosLBtJYejDSeliYPSxwB / rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.inv_gamma) ** -rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.power
        return [BPIFlVyCbIpSBAFKbXcCgjitvQJkMYGa * max(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.min_lr, rRsDAgMBGZSloePFVncbLJtZfIHKWkhB * weVkLCBWUuKbvEHWMEsdwxqqchyDuLtQ)
                for rRsDAgMBGZSloePFVncbLJtZfIHKWkhB in rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.base_lrs]
class LjUxicYPcRAXJialJGHGHeVnVnZXGJNU(optim.lr_scheduler._LRScheduler):
    def __init__(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, optimizer, WefvdocPmjFndnQUuYmdZKYvUBnqMlwy, eeehCkWlicOSSZeEWMocEIpaDJxlRTfD=0.5, BPIFlVyCbIpSBAFKbXcCgjitvQJkMYGa=0., min_lr=0.,
                 AXGNHRRRaXEGosLBtJYejDSeliYPSxwB=-1, aFZoJwWpCnqyOJdcAMLlqOHxDgjPTNCS=False):
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.WefvdocPmjFndnQUuYmdZKYvUBnqMlwy = WefvdocPmjFndnQUuYmdZKYvUBnqMlwy
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.eeehCkWlicOSSZeEWMocEIpaDJxlRTfD = eeehCkWlicOSSZeEWMocEIpaDJxlRTfD
        if not 0. <= BPIFlVyCbIpSBAFKbXcCgjitvQJkMYGa < 1:
            raise ValueError('Invalid value for warmup')
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.BPIFlVyCbIpSBAFKbXcCgjitvQJkMYGa = BPIFlVyCbIpSBAFKbXcCgjitvQJkMYGa
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.min_lr = min_lr
        super().__init__(optimizer, AXGNHRRRaXEGosLBtJYejDSeliYPSxwB, aFZoJwWpCnqyOJdcAMLlqOHxDgjPTNCS)
    def XyyizfZZExIQuvyyTwLRBKBGMPpWAWES(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS):
        if not rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS._get_lr_called_within_step:
            warnings.warn("To get the last learning rate computed by the scheduler, "
                          "please use `get_last_lr()`.")
        return rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.FNOuVtiQFkqRVsVuScLhhmjlgTgNSllF()
    def FNOuVtiQFkqRVsVuScLhhmjlgTgNSllF(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS):
        BPIFlVyCbIpSBAFKbXcCgjitvQJkMYGa = 1 - rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.BPIFlVyCbIpSBAFKbXcCgjitvQJkMYGa ** (rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.AXGNHRRRaXEGosLBtJYejDSeliYPSxwB + 1)
        weVkLCBWUuKbvEHWMEsdwxqqchyDuLtQ = (rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.eeehCkWlicOSSZeEWMocEIpaDJxlRTfD ** (1 / rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.WefvdocPmjFndnQUuYmdZKYvUBnqMlwy)) ** rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.AXGNHRRRaXEGosLBtJYejDSeliYPSxwB
        return [BPIFlVyCbIpSBAFKbXcCgjitvQJkMYGa * max(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.min_lr, rRsDAgMBGZSloePFVncbLJtZfIHKWkhB * weVkLCBWUuKbvEHWMEsdwxqqchyDuLtQ)
                for rRsDAgMBGZSloePFVncbLJtZfIHKWkhB in rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.base_lrs]
def ebaGjDReKqpYDgmCwmxVRfQoVKIauWRy(BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg, loc=0., xmbXivThLFnawFPAJvIDBztziWsaDyEE=1., fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc='cpu', DDRQlhrNSGpwTrokWitkZipdfbAqBFxv=torch.float32):
    return (torch.randn(BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg, fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc=fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc, DDRQlhrNSGpwTrokWitkZipdfbAqBFxv=DDRQlhrNSGpwTrokWitkZipdfbAqBFxv) * xmbXivThLFnawFPAJvIDBztziWsaDyEE + loc).exp()
def jlwxKjBJEoIShLXvdTRvjZpcsIXtpdlb(BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg, loc=0., xmbXivThLFnawFPAJvIDBztziWsaDyEE=1., xDHXyZxnTpgTIUWmlIOPGEtWVzfhHsDh=0., xPSUMHJpcKTzcLMKKmAzyKtzHGhYpbqS=float('inf'), fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc='cpu', DDRQlhrNSGpwTrokWitkZipdfbAqBFxv=torch.float32):
    xDHXyZxnTpgTIUWmlIOPGEtWVzfhHsDh = torch.as_tensor(xDHXyZxnTpgTIUWmlIOPGEtWVzfhHsDh, fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc=fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc, DDRQlhrNSGpwTrokWitkZipdfbAqBFxv=torch.float64)
    xPSUMHJpcKTzcLMKKmAzyKtzHGhYpbqS = torch.as_tensor(xPSUMHJpcKTzcLMKKmAzyKtzHGhYpbqS, fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc=fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc, DDRQlhrNSGpwTrokWitkZipdfbAqBFxv=torch.float64)
    TfGSombIjizhXxBLAkPyYZuBHPEexZPJ = xDHXyZxnTpgTIUWmlIOPGEtWVzfhHsDh.DJwhOGBaLcOjmXnuwXMXOyhMtknqkKXL().sub(loc).div(xmbXivThLFnawFPAJvIDBztziWsaDyEE).sigmoid()
    jheHeTtnhZrCArnhbIatNlHriKhoFJdG = xPSUMHJpcKTzcLMKKmAzyKtzHGhYpbqS.DJwhOGBaLcOjmXnuwXMXOyhMtknqkKXL().sub(loc).div(xmbXivThLFnawFPAJvIDBztziWsaDyEE).sigmoid()
    u = torch.rand(BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg, fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc=fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc, DDRQlhrNSGpwTrokWitkZipdfbAqBFxv=torch.float64) * (jheHeTtnhZrCArnhbIatNlHriKhoFJdG - TfGSombIjizhXxBLAkPyYZuBHPEexZPJ) + TfGSombIjizhXxBLAkPyYZuBHPEexZPJ
    return u.logit().mul(xmbXivThLFnawFPAJvIDBztziWsaDyEE).add(loc).exp().sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ(DDRQlhrNSGpwTrokWitkZipdfbAqBFxv)
def WDQsMMDlusMgfibJEZvfqzNqgzNsjrzp(BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg, xDHXyZxnTpgTIUWmlIOPGEtWVzfhHsDh, xPSUMHJpcKTzcLMKKmAzyKtzHGhYpbqS, fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc='cpu', DDRQlhrNSGpwTrokWitkZipdfbAqBFxv=torch.float32):
    xDHXyZxnTpgTIUWmlIOPGEtWVzfhHsDh = math.DJwhOGBaLcOjmXnuwXMXOyhMtknqkKXL(xDHXyZxnTpgTIUWmlIOPGEtWVzfhHsDh)
    xPSUMHJpcKTzcLMKKmAzyKtzHGhYpbqS = math.DJwhOGBaLcOjmXnuwXMXOyhMtknqkKXL(xPSUMHJpcKTzcLMKKmAzyKtzHGhYpbqS)
    return (torch.rand(BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg, fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc=fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc, DDRQlhrNSGpwTrokWitkZipdfbAqBFxv=DDRQlhrNSGpwTrokWitkZipdfbAqBFxv) * (xPSUMHJpcKTzcLMKKmAzyKtzHGhYpbqS - xDHXyZxnTpgTIUWmlIOPGEtWVzfhHsDh) + xDHXyZxnTpgTIUWmlIOPGEtWVzfhHsDh).exp()
def ibsHpGTkBSbGLxcUjqsypsLfQCFJyugN(BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg, sigma_data=1., xDHXyZxnTpgTIUWmlIOPGEtWVzfhHsDh=0., xPSUMHJpcKTzcLMKKmAzyKtzHGhYpbqS=float('inf'), fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc='cpu', DDRQlhrNSGpwTrokWitkZipdfbAqBFxv=torch.float32):
    TfGSombIjizhXxBLAkPyYZuBHPEexZPJ = math.atan(xDHXyZxnTpgTIUWmlIOPGEtWVzfhHsDh / sigma_data) * 2 / math.pi
    jheHeTtnhZrCArnhbIatNlHriKhoFJdG = math.atan(xPSUMHJpcKTzcLMKKmAzyKtzHGhYpbqS / sigma_data) * 2 / math.pi
    u = torch.rand(BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg, fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc=fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc, DDRQlhrNSGpwTrokWitkZipdfbAqBFxv=DDRQlhrNSGpwTrokWitkZipdfbAqBFxv) * (jheHeTtnhZrCArnhbIatNlHriKhoFJdG - TfGSombIjizhXxBLAkPyYZuBHPEexZPJ) + TfGSombIjizhXxBLAkPyYZuBHPEexZPJ
    return torch.tan(u * math.pi / 2) * sigma_data
def UrHngImVrQBgbsPbFOPItbDTfuOccNiu(BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg, loc, scale_1, scale_2, fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc='cpu', DDRQlhrNSGpwTrokWitkZipdfbAqBFxv=torch.float32):
    zXHJFiFFvWqeQIAxyaTGMUgoRaHrYzjK = torch.randn(BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg, fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc=fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc, DDRQlhrNSGpwTrokWitkZipdfbAqBFxv=DDRQlhrNSGpwTrokWitkZipdfbAqBFxv).abs()
    u = torch.rand(BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg, fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc=fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc, DDRQlhrNSGpwTrokWitkZipdfbAqBFxv=DDRQlhrNSGpwTrokWitkZipdfbAqBFxv)
    gsppVgnZwzcHOFHFfyDORVwiLubLqAhU = zXHJFiFFvWqeQIAxyaTGMUgoRaHrYzjK * -scale_1 + loc
    NtPcliVPUMBXgRhqxAVFuGdXEuVpTJlR = zXHJFiFFvWqeQIAxyaTGMUgoRaHrYzjK * scale_2 + loc
    tZrGvOQTQKhZSRQltVuxANtJzJtnyxqW = scale_1 / (scale_1 + scale_2)
    return torch.where(u < tZrGvOQTQKhZSRQltVuxANtJzJtnyxqW, gsppVgnZwzcHOFHFfyDORVwiLubLqAhU, NtPcliVPUMBXgRhqxAVFuGdXEuVpTJlR).exp()
class KmrFxJYEcqlbyidxnRtGlzChYnCkBENx(data.Dataset):
    OqvjoLSvQwIzafOkaiyctjuYLUItNdKU = {'.jpg', '.jpeg', '.png', '.ppm', '.bmp', '.pgm', '.tif', '.tiff', '.webp'}
    def __init__(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, hpDCmssMBWJUwBayrpShjJoOSQeDdfbl, transform=None):
        super().__init__()
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.hpDCmssMBWJUwBayrpShjJoOSQeDdfbl = Path(hpDCmssMBWJUwBayrpShjJoOSQeDdfbl)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.transform = nn.Identity() if transform is None else transform
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.AOGAiLpFWYRqfvQFDHklGCBgbJMOyeLI = sorted(path for path in rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.hpDCmssMBWJUwBayrpShjJoOSQeDdfbl.rglob('*') if path.BsNMPzInPMJbfbtzWNcCZMzWMgmxchHs.lower() in rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.OqvjoLSvQwIzafOkaiyctjuYLUItNdKU)
    def __repr__(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS):
        return f'FolderOfImages(root="{rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.hpDCmssMBWJUwBayrpShjJoOSQeDdfbl}", len: {len(self)})'
    def __len__(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS):
        return len(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.AOGAiLpFWYRqfvQFDHklGCBgbJMOyeLI)
    def __getitem__(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, nyrzKxQtioheHIZujafABgijbCjrWhBU):
        path = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.AOGAiLpFWYRqfvQFDHklGCBgbJMOyeLI[nyrzKxQtioheHIZujafABgijbCjrWhBU]
        with open(path, 'rb') as f:
            eLyJtroPthPCROYWyMphoIrGatNOOXCO = Image.open(f).convert('RGB')
        eLyJtroPthPCROYWyMphoIrGatNOOXCO = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.transform(eLyJtroPthPCROYWyMphoIrGatNOOXCO)
        return eLyJtroPthPCROYWyMphoIrGatNOOXCO,
class LTcVBrefNeCoZIZODXmBOcDgCFakaESM:
    def __init__(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, VpsbOZzufynrTFUvvRofTQeRCOCIKJOM, columns):
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.VpsbOZzufynrTFUvvRofTQeRCOCIKJOM = Path(VpsbOZzufynrTFUvvRofTQeRCOCIKJOM)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.columns = columns
        if rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.VpsbOZzufynrTFUvvRofTQeRCOCIKJOM.exists():
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.GGrVUpHsMvVvEYhZgyWAlwaKJQserwts = open(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.VpsbOZzufynrTFUvvRofTQeRCOCIKJOM, 'a')
        else:
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.GGrVUpHsMvVvEYhZgyWAlwaKJQserwts = open(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.VpsbOZzufynrTFUvvRofTQeRCOCIKJOM, 'w')
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.write(*rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.columns)
    def write(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, *DukiculvUpjhZIVvaGinshRSKLSTgVVl):
        print(*DukiculvUpjhZIVvaGinshRSKLSTgVVl, sep=',', GGrVUpHsMvVvEYhZgyWAlwaKJQserwts=rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.GGrVUpHsMvVvEYhZgyWAlwaKJQserwts, flush=True)
@contextmanager
def ROJyyHZkXMegwxfnalnyvlNJWVnlizks(cudnn=None, matmul=None):
    FiMpeKbXfhxXRWrzNdCkdLHZfGbuFswV = torch.backends.cudnn.allow_tf32
    JbwJEXbPHxiGCFHgLyfkISOKcBNlwXiM = torch.backends.cuda.matmul.allow_tf32
    try:
        if cudnn is not None:
            torch.backends.cudnn.allow_tf32 = cudnn
        if matmul is not None:
            torch.backends.cuda.matmul.allow_tf32 = matmul
        yield
    finally:
        if cudnn is not None:
            torch.backends.cudnn.allow_tf32 = FiMpeKbXfhxXRWrzNdCkdLHZfGbuFswV
        if matmul is not None:
            torch.backends.cuda.matmul.allow_tf32 = JbwJEXbPHxiGCFHgLyfkISOKcBNlwXiM
