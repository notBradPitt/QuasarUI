from inspect import isfunction
import math
import torch
import torch.nn.functional as F
from torch import nn, einsum
from einops import rearrange, kYXcbCDGZMxtOlIZeOtGMsNePlSickQL
from typing import Optional, Any
from .diffusionmodules.util import vcSlHLxBcVodHmZrzACHLEJuENMXjWTG
from .sub_quadratic_attention import wWGvJoqsrPWDPWsQTifuSjfltmBzpUdK
from quasar import model_management
if model_management.fpzqQPwQsgljpVXCeYPLnjVJExRYKmpM():
    import xformers
    import xformers.ops
from quasar.cli_args import DukiculvUpjhZIVvaGinshRSKLSTgVVl
import quasar.ops
if DukiculvUpjhZIVvaGinshRSKLSTgVVl.dont_upcast_attention:
    print("disabling upcasting of attention")
    JGhGmYoXIfioVVfVVRkJUtotlxRVouBT = "fp16"
else:
    JGhGmYoXIfioVVfVVRkJUtotlxRVouBT = "fp32"
def CzuSRmujwDQnNtuxpiDhURIOWmCdbjjH(iQelECAceWgpMwNVKVNfqYXiZvxEyNPn):
    return iQelECAceWgpMwNVKVNfqYXiZvxEyNPn is not None
def mbvxGTzHRegamxLbMgjoxyrZBBDzHvEV(arr):
    return{qRswSnOBtvyzjhnKgbIzXEJZeYxpAFNw: True for qRswSnOBtvyzjhnKgbIzXEJZeYxpAFNw in arr}.keys()
def zKvTEPbGDoRBsQSYYaddQKLTFDorvdms(iQelECAceWgpMwNVKVNfqYXiZvxEyNPn, TXGwYXNLgQsYzfHHpRBDJGFCFZEClzIo):
    if CzuSRmujwDQnNtuxpiDhURIOWmCdbjjH(iQelECAceWgpMwNVKVNfqYXiZvxEyNPn):
        return iQelECAceWgpMwNVKVNfqYXiZvxEyNPn
    return TXGwYXNLgQsYzfHHpRBDJGFCFZEClzIo
def EhnojrGhJngfjyuBMSfsPyqqacULAQoV(XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz):
    return -torch.finfo(XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz.DDRQlhrNSGpwTrokWitkZipdfbAqBFxv).max
def RKlJcdDlJMwludZrWmkyUBEDsACHKapl(xPmCFphFKpGMpIsczaSKHmMgRPZzJwla):
    yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk = xPmCFphFKpGMpIsczaSKHmMgRPZzJwla.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[-1]
    fOYIxmVRkbmqKCdAjhgqqAEkLdJvKBVd = 1 / math.sqrt(yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk)
    xPmCFphFKpGMpIsczaSKHmMgRPZzJwla.uniform_(-fOYIxmVRkbmqKCdAjhgqqAEkLdJvKBVd, fOYIxmVRkbmqKCdAjhgqqAEkLdJvKBVd)
    return xPmCFphFKpGMpIsczaSKHmMgRPZzJwla
class arWeRcSKaVoQCynVIqZcAcRgBnhxHCvR(nn.Module):
    def __init__(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, dim_in, tgbtPhzliVInSVGKVTqssTxzfwkNlUPr, DDRQlhrNSGpwTrokWitkZipdfbAqBFxv=None, fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc=None, xwIQGNbJnSVpLrBBfhMLBchFpoolNzOe=quasar.ops):
        super().__init__()
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.proj = xwIQGNbJnSVpLrBBfhMLBchFpoolNzOe.DhMcMyEvvzmWIEJojbQeGHlzfZKiPzHO(dim_in, tgbtPhzliVInSVGKVTqssTxzfwkNlUPr * 2, DDRQlhrNSGpwTrokWitkZipdfbAqBFxv=DDRQlhrNSGpwTrokWitkZipdfbAqBFxv, fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc=fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc)
    def lqBgIcSWZYylbCPjXksJWDguuSOqoPCJ(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, NECAaWUrFGIXcLimrerEYmxYIykQBfXb):
        NECAaWUrFGIXcLimrerEYmxYIykQBfXb, wnJEgZdCPmnnmkKlktStjfXXkbZbbqLH = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.proj(NECAaWUrFGIXcLimrerEYmxYIykQBfXb).ebMwMGDmpDsmyMtCQfGxUhZuVHvTpavF(2, yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk=-1)
        return NECAaWUrFGIXcLimrerEYmxYIykQBfXb * F.gelu(wnJEgZdCPmnnmkKlktStjfXXkbZbbqLH)
class nVIpLCPoeZxavETSbXIKgqMNJkfGLLVs(nn.Module):
    def __init__(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk, tgbtPhzliVInSVGKVTqssTxzfwkNlUPr=None, XVFRnfSDhyHpjboFTGKCmAMvovOXxqYP=4, glu=False, kcIxGCXrUvsLPSfmGoULGFzAthVmTXcA=0., DDRQlhrNSGpwTrokWitkZipdfbAqBFxv=None, fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc=None, xwIQGNbJnSVpLrBBfhMLBchFpoolNzOe=quasar.ops):
        super().__init__()
        mnMnCdMaVdGNkPTuQLMKyEjwOMhAgIMR = int(yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk * XVFRnfSDhyHpjboFTGKCmAMvovOXxqYP)
        tgbtPhzliVInSVGKVTqssTxzfwkNlUPr = zKvTEPbGDoRBsQSYYaddQKLTFDorvdms(tgbtPhzliVInSVGKVTqssTxzfwkNlUPr, yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk)
        sXmfwvmjHIkRpPcXiyglCLqfExhzEyXD = nn.Sequential(
            xwIQGNbJnSVpLrBBfhMLBchFpoolNzOe.DhMcMyEvvzmWIEJojbQeGHlzfZKiPzHO(yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk, mnMnCdMaVdGNkPTuQLMKyEjwOMhAgIMR, DDRQlhrNSGpwTrokWitkZipdfbAqBFxv=DDRQlhrNSGpwTrokWitkZipdfbAqBFxv, fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc=fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc),
            nn.GELU()
        ) if not glu else arWeRcSKaVoQCynVIqZcAcRgBnhxHCvR(yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk, mnMnCdMaVdGNkPTuQLMKyEjwOMhAgIMR, DDRQlhrNSGpwTrokWitkZipdfbAqBFxv=DDRQlhrNSGpwTrokWitkZipdfbAqBFxv, fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc=fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc, xwIQGNbJnSVpLrBBfhMLBchFpoolNzOe=xwIQGNbJnSVpLrBBfhMLBchFpoolNzOe)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.faINqTMSsQxdMDXBAGUozMnWtvraUbzj = nn.Sequential(
            sXmfwvmjHIkRpPcXiyglCLqfExhzEyXD,
            nn.Dropout(kcIxGCXrUvsLPSfmGoULGFzAthVmTXcA),
            xwIQGNbJnSVpLrBBfhMLBchFpoolNzOe.DhMcMyEvvzmWIEJojbQeGHlzfZKiPzHO(mnMnCdMaVdGNkPTuQLMKyEjwOMhAgIMR, tgbtPhzliVInSVGKVTqssTxzfwkNlUPr, DDRQlhrNSGpwTrokWitkZipdfbAqBFxv=DDRQlhrNSGpwTrokWitkZipdfbAqBFxv, fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc=fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc)
        )
    def lqBgIcSWZYylbCPjXksJWDguuSOqoPCJ(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, NECAaWUrFGIXcLimrerEYmxYIykQBfXb):
        return rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.faINqTMSsQxdMDXBAGUozMnWtvraUbzj(NECAaWUrFGIXcLimrerEYmxYIykQBfXb)
def TVrUNiPGCtAmXFOUoqodGJnRgbvoldNA(FRIBQCDfDDxIonplwxvPCicvOmmOgYPC):
    for HutkrxeXIuRQKOhCWHkiwqLGAsJjUSKj in FRIBQCDfDDxIonplwxvPCicvOmmOgYPC.parameters():
        HutkrxeXIuRQKOhCWHkiwqLGAsJjUSKj.detach().zero_()
    return FRIBQCDfDDxIonplwxvPCicvOmmOgYPC
def HSnGePyLrgZhiiSoMOwJmgVPBjIpItDD(EbKSIFxpyCpzycRDApduouVsxspHzkTj, DDRQlhrNSGpwTrokWitkZipdfbAqBFxv=None, fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc=None):
    return torch.nn.GroupNorm(num_groups=32, num_channels=EbKSIFxpyCpzycRDApduouVsxspHzkTj, VVqkfbMIOFDgzhOKKnJVcuOffzzrOGPv=1e-6, affine=True, DDRQlhrNSGpwTrokWitkZipdfbAqBFxv=DDRQlhrNSGpwTrokWitkZipdfbAqBFxv, fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc=fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc)
class aswjqUhyWZcYJGpzhqhoxBLqrSpNpcOM(nn.Module):
    def __init__(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, EbKSIFxpyCpzycRDApduouVsxspHzkTj):
        super().__init__()
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.EbKSIFxpyCpzycRDApduouVsxspHzkTj = EbKSIFxpyCpzycRDApduouVsxspHzkTj
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.norm = HSnGePyLrgZhiiSoMOwJmgVPBjIpItDD(EbKSIFxpyCpzycRDApduouVsxspHzkTj)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.mxaMgfLZUDPObiqkdCgHnnARjBNVGQnh = torch.nn.LcFcvNeYCKrBHlNkoWrkqdbxdkNCJBBK(EbKSIFxpyCpzycRDApduouVsxspHzkTj,
                                 EbKSIFxpyCpzycRDApduouVsxspHzkTj,
                                 aBEJjpEOpoRJYkulwSmukddEYErxRnAG=1,
                                 NTEWXstfzqNXGESmGkQNFWBaQsGAPlGd=1,
                                 sdxdTSjnkAOjlGmltQHvLiHRDstMzpAP=0)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm = torch.nn.LcFcvNeYCKrBHlNkoWrkqdbxdkNCJBBK(EbKSIFxpyCpzycRDApduouVsxspHzkTj,
                                 EbKSIFxpyCpzycRDApduouVsxspHzkTj,
                                 aBEJjpEOpoRJYkulwSmukddEYErxRnAG=1,
                                 NTEWXstfzqNXGESmGkQNFWBaQsGAPlGd=1,
                                 sdxdTSjnkAOjlGmltQHvLiHRDstMzpAP=0)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.powGafreWfwlSAqPpTpUhFgpFVqCPavl = torch.nn.LcFcvNeYCKrBHlNkoWrkqdbxdkNCJBBK(EbKSIFxpyCpzycRDApduouVsxspHzkTj,
                                 EbKSIFxpyCpzycRDApduouVsxspHzkTj,
                                 aBEJjpEOpoRJYkulwSmukddEYErxRnAG=1,
                                 NTEWXstfzqNXGESmGkQNFWBaQsGAPlGd=1,
                                 sdxdTSjnkAOjlGmltQHvLiHRDstMzpAP=0)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.proj_out = torch.nn.LcFcvNeYCKrBHlNkoWrkqdbxdkNCJBBK(EbKSIFxpyCpzycRDApduouVsxspHzkTj,
                                        EbKSIFxpyCpzycRDApduouVsxspHzkTj,
                                        aBEJjpEOpoRJYkulwSmukddEYErxRnAG=1,
                                        NTEWXstfzqNXGESmGkQNFWBaQsGAPlGd=1,
                                        sdxdTSjnkAOjlGmltQHvLiHRDstMzpAP=0)
    def lqBgIcSWZYylbCPjXksJWDguuSOqoPCJ(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, NECAaWUrFGIXcLimrerEYmxYIykQBfXb):
        vCjLIHrnXRniEvZiWnGuQBAcFdDANZRw = NECAaWUrFGIXcLimrerEYmxYIykQBfXb
        vCjLIHrnXRniEvZiWnGuQBAcFdDANZRw = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.norm(vCjLIHrnXRniEvZiWnGuQBAcFdDANZRw)
        mxaMgfLZUDPObiqkdCgHnnARjBNVGQnh = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.mxaMgfLZUDPObiqkdCgHnnARjBNVGQnh(vCjLIHrnXRniEvZiWnGuQBAcFdDANZRw)
        EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm(vCjLIHrnXRniEvZiWnGuQBAcFdDANZRw)
        powGafreWfwlSAqPpTpUhFgpFVqCPavl = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.powGafreWfwlSAqPpTpUhFgpFVqCPavl(vCjLIHrnXRniEvZiWnGuQBAcFdDANZRw)
        b,cjHIelcAqVoHWdLcgzuZiBumKNTVADsY,xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab,AeIrbRXDkpZlClJGwzMknCltTQQdmhvu = mxaMgfLZUDPObiqkdCgHnnARjBNVGQnh.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg
        mxaMgfLZUDPObiqkdCgHnnARjBNVGQnh = rearrange(mxaMgfLZUDPObiqkdCgHnnARjBNVGQnh, 'b c h w -> b (h w) c')
        EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm = rearrange(EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm, 'b c h w -> b c (h w)')
        ibrocyfndMyEZXsFuHpqYHuuJzIkZANK = torch.einsum('bij,bjk->bik', mxaMgfLZUDPObiqkdCgHnnARjBNVGQnh, EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm)
        ibrocyfndMyEZXsFuHpqYHuuJzIkZANK = ibrocyfndMyEZXsFuHpqYHuuJzIkZANK * (int(cjHIelcAqVoHWdLcgzuZiBumKNTVADsY)**(-0.5))
        ibrocyfndMyEZXsFuHpqYHuuJzIkZANK = torch.nn.functional.softmax(ibrocyfndMyEZXsFuHpqYHuuJzIkZANK, yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk=2)
        powGafreWfwlSAqPpTpUhFgpFVqCPavl = rearrange(powGafreWfwlSAqPpTpUhFgpFVqCPavl, 'b c h w -> b c (h w)')
        ibrocyfndMyEZXsFuHpqYHuuJzIkZANK = rearrange(ibrocyfndMyEZXsFuHpqYHuuJzIkZANK, 'b i j -> b j i')
        vCjLIHrnXRniEvZiWnGuQBAcFdDANZRw = torch.einsum('bij,bjk->bik', powGafreWfwlSAqPpTpUhFgpFVqCPavl, ibrocyfndMyEZXsFuHpqYHuuJzIkZANK)
        vCjLIHrnXRniEvZiWnGuQBAcFdDANZRw = rearrange(vCjLIHrnXRniEvZiWnGuQBAcFdDANZRw, 'b c (h w) -> b c h w', xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab=xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab)
        vCjLIHrnXRniEvZiWnGuQBAcFdDANZRw = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.proj_out(vCjLIHrnXRniEvZiWnGuQBAcFdDANZRw)
        return NECAaWUrFGIXcLimrerEYmxYIykQBfXb+vCjLIHrnXRniEvZiWnGuQBAcFdDANZRw
class DmzUHgaxPAiRWNJrogZnoPnKOIZhuATL(nn.Module):
    def __init__(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, ZqiCYiNfDUNCIdHmASCiuNWYfvyqQifY, FEAAZHeTRQEJCsYHCOEPpfOenpVZIhNT=None, QEnKImSSxUuBDHahcSgvZCYYpzjKVrVk=8, QiYWcbRqbdDfAfhjULhYwmIlOStjgPlv=64, kcIxGCXrUvsLPSfmGoULGFzAthVmTXcA=0., DDRQlhrNSGpwTrokWitkZipdfbAqBFxv=None, fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc=None, xwIQGNbJnSVpLrBBfhMLBchFpoolNzOe=quasar.ops):
        super().__init__()
        mnMnCdMaVdGNkPTuQLMKyEjwOMhAgIMR = QiYWcbRqbdDfAfhjULhYwmIlOStjgPlv * QEnKImSSxUuBDHahcSgvZCYYpzjKVrVk
        FEAAZHeTRQEJCsYHCOEPpfOenpVZIhNT = zKvTEPbGDoRBsQSYYaddQKLTFDorvdms(FEAAZHeTRQEJCsYHCOEPpfOenpVZIhNT, ZqiCYiNfDUNCIdHmASCiuNWYfvyqQifY)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.xmbXivThLFnawFPAJvIDBztziWsaDyEE = QiYWcbRqbdDfAfhjULhYwmIlOStjgPlv ** -0.5
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.QEnKImSSxUuBDHahcSgvZCYYpzjKVrVk = QEnKImSSxUuBDHahcSgvZCYYpzjKVrVk
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.to_q = xwIQGNbJnSVpLrBBfhMLBchFpoolNzOe.DhMcMyEvvzmWIEJojbQeGHlzfZKiPzHO(ZqiCYiNfDUNCIdHmASCiuNWYfvyqQifY, mnMnCdMaVdGNkPTuQLMKyEjwOMhAgIMR, PvdyIPYzYuxTGYQjZbTucTrRGHTQkavB=False, DDRQlhrNSGpwTrokWitkZipdfbAqBFxv=DDRQlhrNSGpwTrokWitkZipdfbAqBFxv, fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc=fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.to_k = xwIQGNbJnSVpLrBBfhMLBchFpoolNzOe.DhMcMyEvvzmWIEJojbQeGHlzfZKiPzHO(FEAAZHeTRQEJCsYHCOEPpfOenpVZIhNT, mnMnCdMaVdGNkPTuQLMKyEjwOMhAgIMR, PvdyIPYzYuxTGYQjZbTucTrRGHTQkavB=False, DDRQlhrNSGpwTrokWitkZipdfbAqBFxv=DDRQlhrNSGpwTrokWitkZipdfbAqBFxv, fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc=fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.to_v = xwIQGNbJnSVpLrBBfhMLBchFpoolNzOe.DhMcMyEvvzmWIEJojbQeGHlzfZKiPzHO(FEAAZHeTRQEJCsYHCOEPpfOenpVZIhNT, mnMnCdMaVdGNkPTuQLMKyEjwOMhAgIMR, PvdyIPYzYuxTGYQjZbTucTrRGHTQkavB=False, DDRQlhrNSGpwTrokWitkZipdfbAqBFxv=DDRQlhrNSGpwTrokWitkZipdfbAqBFxv, fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc=fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.to_out = nn.Sequential(
            xwIQGNbJnSVpLrBBfhMLBchFpoolNzOe.DhMcMyEvvzmWIEJojbQeGHlzfZKiPzHO(mnMnCdMaVdGNkPTuQLMKyEjwOMhAgIMR, ZqiCYiNfDUNCIdHmASCiuNWYfvyqQifY, DDRQlhrNSGpwTrokWitkZipdfbAqBFxv=DDRQlhrNSGpwTrokWitkZipdfbAqBFxv, fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc=fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc),
            nn.Dropout(kcIxGCXrUvsLPSfmGoULGFzAthVmTXcA)
        )
    def lqBgIcSWZYylbCPjXksJWDguuSOqoPCJ(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, NECAaWUrFGIXcLimrerEYmxYIykQBfXb, tRdCjhUPYVVxnSEkGmJIHWRitDXRXSZS=None, GXNVXDlnsSLzkmussBPoJXgJwuXIiwsc=None, KHpRlHOzblljQyskecSxzUuWZtneWwta=None):
        xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.QEnKImSSxUuBDHahcSgvZCYYpzjKVrVk
        oFxedobBnFbKeewIgTfUgblKziGvmndF = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.to_q(NECAaWUrFGIXcLimrerEYmxYIykQBfXb)
        tRdCjhUPYVVxnSEkGmJIHWRitDXRXSZS = zKvTEPbGDoRBsQSYYaddQKLTFDorvdms(tRdCjhUPYVVxnSEkGmJIHWRitDXRXSZS, NECAaWUrFGIXcLimrerEYmxYIykQBfXb)
        nyrzKxQtioheHIZujafABgijbCjrWhBU = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.to_k(tRdCjhUPYVVxnSEkGmJIHWRitDXRXSZS)
        if GXNVXDlnsSLzkmussBPoJXgJwuXIiwsc is not None:
            GXNVXDlnsSLzkmussBPoJXgJwuXIiwsc = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.to_v(GXNVXDlnsSLzkmussBPoJXgJwuXIiwsc)
        else:
            GXNVXDlnsSLzkmussBPoJXgJwuXIiwsc = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.to_v(tRdCjhUPYVVxnSEkGmJIHWRitDXRXSZS)
        del tRdCjhUPYVVxnSEkGmJIHWRitDXRXSZS, NECAaWUrFGIXcLimrerEYmxYIykQBfXb
        oFxedobBnFbKeewIgTfUgblKziGvmndF = oFxedobBnFbKeewIgTfUgblKziGvmndF.unflatten(-1, (rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.QEnKImSSxUuBDHahcSgvZCYYpzjKVrVk, -1)).transpose(1,2).flatten(end_dim=1)
        uvCuKDkdVEPRdZyyLHLiivxCEmonrfgb = nyrzKxQtioheHIZujafABgijbCjrWhBU.transpose(1,2).unflatten(1, (rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.QEnKImSSxUuBDHahcSgvZCYYpzjKVrVk, -1)).flatten(end_dim=1)
        del nyrzKxQtioheHIZujafABgijbCjrWhBU
        GXNVXDlnsSLzkmussBPoJXgJwuXIiwsc = GXNVXDlnsSLzkmussBPoJXgJwuXIiwsc.unflatten(-1, (rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.QEnKImSSxUuBDHahcSgvZCYYpzjKVrVk, -1)).transpose(1,2).flatten(end_dim=1)
        DDRQlhrNSGpwTrokWitkZipdfbAqBFxv = oFxedobBnFbKeewIgTfUgblKziGvmndF.DDRQlhrNSGpwTrokWitkZipdfbAqBFxv
        ggPIURSGXIcuVBVgCWAEVPDrcubVXMiD = JGhGmYoXIfioVVfVVRkJUtotlxRVouBT =="fp32" and oFxedobBnFbKeewIgTfUgblKziGvmndF.DDRQlhrNSGpwTrokWitkZipdfbAqBFxv != torch.float32
        if ggPIURSGXIcuVBVgCWAEVPDrcubVXMiD:
            EstpvnaBPYybxVkmTKklNAJMBdTrDDnB = torch.finfo(torch.float32).bits//8
        else:
            EstpvnaBPYybxVkmTKklNAJMBdTrDDnB = torch.finfo(oFxedobBnFbKeewIgTfUgblKziGvmndF.DDRQlhrNSGpwTrokWitkZipdfbAqBFxv).bits//8
        OxxKceEwXIPmBcVPFFUdYjDLrGLsvryX, eCRSPzKosCQhJWveukAUVqFsWrMfGOHN, _ = oFxedobBnFbKeewIgTfUgblKziGvmndF.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg
        _, _, xdRMOqMyVzbfhYwKMCvFapJiNdJvFZoS = uvCuKDkdVEPRdZyyLHLiivxCEmonrfgb.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg
        KXsfTxILJBHvhxcWkTUgoitSvWDOdZta = OxxKceEwXIPmBcVPFFUdYjDLrGLsvryX * EstpvnaBPYybxVkmTKklNAJMBdTrDDnB * eCRSPzKosCQhJWveukAUVqFsWrMfGOHN * xdRMOqMyVzbfhYwKMCvFapJiNdJvFZoS
        GPfGQFkmkbPdFypYtapiuNmsHHdeiLUL, AGGPItzIimskEiuQBFJsAxXDSPwlOIrM = model_management.pEiuPTHzmozHhNpBwWGAaONYuNGSpuqI(oFxedobBnFbKeewIgTfUgblKziGvmndF.fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc, True)
        gjvNGQPejhBIaEEfWzlJIuqIUyNoJcQG = AGGPItzIimskEiuQBFJsAxXDSPwlOIrM * 0.5 
        XAMYbWMRzvpvukEerBoKgjYJduCqwDOF = None
        if GPfGQFkmkbPdFypYtapiuNmsHHdeiLUL > 8192 * 1024 * 1024 * 1.3:
            MVufvcIUNarBDvOyEjKOuGydccXpmhsg = 1024 * 4
        elif GPfGQFkmkbPdFypYtapiuNmsHHdeiLUL > 4096 * 1024 * 1024 * 1.3:
            MVufvcIUNarBDvOyEjKOuGydccXpmhsg = 1024 * 2
        else:
            MVufvcIUNarBDvOyEjKOuGydccXpmhsg = 1024
        sAWdBzxuuAYgVIpaOdkaAUivDjAhbdgS = None
        wixmXKttlLkkejGhtQWTMGdfuBVDfAtJ = (int((gjvNGQPejhBIaEEfWzlJIuqIUyNoJcQG // (OxxKceEwXIPmBcVPFFUdYjDLrGLsvryX * EstpvnaBPYybxVkmTKklNAJMBdTrDDnB * MVufvcIUNarBDvOyEjKOuGydccXpmhsg)) * 2.0) // 1024) * 1024
        if wixmXKttlLkkejGhtQWTMGdfuBVDfAtJ < 1024:
            wixmXKttlLkkejGhtQWTMGdfuBVDfAtJ = None
        if gjvNGQPejhBIaEEfWzlJIuqIUyNoJcQG is not None and KXsfTxILJBHvhxcWkTUgoitSvWDOdZta <= gjvNGQPejhBIaEEfWzlJIuqIUyNoJcQG:
            sRpdDMYTVMeNesUzSLRWIgcClptmNebH = eCRSPzKosCQhJWveukAUVqFsWrMfGOHN
            uDTBZQdxCndcOBROTvXuOsdAOWRULsLj = xdRMOqMyVzbfhYwKMCvFapJiNdJvFZoS
        else:
            sRpdDMYTVMeNesUzSLRWIgcClptmNebH = MVufvcIUNarBDvOyEjKOuGydccXpmhsg
            uDTBZQdxCndcOBROTvXuOsdAOWRULsLj = wixmXKttlLkkejGhtQWTMGdfuBVDfAtJ
            XAMYbWMRzvpvukEerBoKgjYJduCqwDOF = sAWdBzxuuAYgVIpaOdkaAUivDjAhbdgS
        ezoPMrjrILcpzrodGByaQxxZsRTFvfqA = wWGvJoqsrPWDPWsQTifuSjfltmBzpUdK(
            oFxedobBnFbKeewIgTfUgblKziGvmndF,
            uvCuKDkdVEPRdZyyLHLiivxCEmonrfgb,
            GXNVXDlnsSLzkmussBPoJXgJwuXIiwsc,
            sRpdDMYTVMeNesUzSLRWIgcClptmNebH=sRpdDMYTVMeNesUzSLRWIgcClptmNebH,
            uDTBZQdxCndcOBROTvXuOsdAOWRULsLj=uDTBZQdxCndcOBROTvXuOsdAOWRULsLj,
            XAMYbWMRzvpvukEerBoKgjYJduCqwDOF=XAMYbWMRzvpvukEerBoKgjYJduCqwDOF,
            TkHgGRFhDYRqyKuFvQRlKbpOBXUaEDVU=rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.training,
            ggPIURSGXIcuVBVgCWAEVPDrcubVXMiD=ggPIURSGXIcuVBVgCWAEVPDrcubVXMiD,
        )
        ezoPMrjrILcpzrodGByaQxxZsRTFvfqA = ezoPMrjrILcpzrodGByaQxxZsRTFvfqA.sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ(DDRQlhrNSGpwTrokWitkZipdfbAqBFxv)
        ezoPMrjrILcpzrodGByaQxxZsRTFvfqA = ezoPMrjrILcpzrodGByaQxxZsRTFvfqA.unflatten(0, (-1, rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.QEnKImSSxUuBDHahcSgvZCYYpzjKVrVk)).transpose(1,2).flatten(start_dim=2)
        WaTqBlPmvdlyOaKYCTYqcqnxRgMqkFOj, kcIxGCXrUvsLPSfmGoULGFzAthVmTXcA = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.to_out
        ezoPMrjrILcpzrodGByaQxxZsRTFvfqA = WaTqBlPmvdlyOaKYCTYqcqnxRgMqkFOj(ezoPMrjrILcpzrodGByaQxxZsRTFvfqA)
        ezoPMrjrILcpzrodGByaQxxZsRTFvfqA = kcIxGCXrUvsLPSfmGoULGFzAthVmTXcA(ezoPMrjrILcpzrodGByaQxxZsRTFvfqA)
        return ezoPMrjrILcpzrodGByaQxxZsRTFvfqA
class NPAwEAqrUFoUkOcUyBXukXyENmexVjRW(nn.Module):
    def __init__(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, ZqiCYiNfDUNCIdHmASCiuNWYfvyqQifY, FEAAZHeTRQEJCsYHCOEPpfOenpVZIhNT=None, QEnKImSSxUuBDHahcSgvZCYYpzjKVrVk=8, QiYWcbRqbdDfAfhjULhYwmIlOStjgPlv=64, kcIxGCXrUvsLPSfmGoULGFzAthVmTXcA=0., DDRQlhrNSGpwTrokWitkZipdfbAqBFxv=None, fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc=None, xwIQGNbJnSVpLrBBfhMLBchFpoolNzOe=quasar.ops):
        super().__init__()
        mnMnCdMaVdGNkPTuQLMKyEjwOMhAgIMR = QiYWcbRqbdDfAfhjULhYwmIlOStjgPlv * QEnKImSSxUuBDHahcSgvZCYYpzjKVrVk
        FEAAZHeTRQEJCsYHCOEPpfOenpVZIhNT = zKvTEPbGDoRBsQSYYaddQKLTFDorvdms(FEAAZHeTRQEJCsYHCOEPpfOenpVZIhNT, ZqiCYiNfDUNCIdHmASCiuNWYfvyqQifY)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.xmbXivThLFnawFPAJvIDBztziWsaDyEE = QiYWcbRqbdDfAfhjULhYwmIlOStjgPlv ** -0.5
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.QEnKImSSxUuBDHahcSgvZCYYpzjKVrVk = QEnKImSSxUuBDHahcSgvZCYYpzjKVrVk
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.to_q = xwIQGNbJnSVpLrBBfhMLBchFpoolNzOe.DhMcMyEvvzmWIEJojbQeGHlzfZKiPzHO(ZqiCYiNfDUNCIdHmASCiuNWYfvyqQifY, mnMnCdMaVdGNkPTuQLMKyEjwOMhAgIMR, PvdyIPYzYuxTGYQjZbTucTrRGHTQkavB=False, DDRQlhrNSGpwTrokWitkZipdfbAqBFxv=DDRQlhrNSGpwTrokWitkZipdfbAqBFxv, fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc=fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.to_k = xwIQGNbJnSVpLrBBfhMLBchFpoolNzOe.DhMcMyEvvzmWIEJojbQeGHlzfZKiPzHO(FEAAZHeTRQEJCsYHCOEPpfOenpVZIhNT, mnMnCdMaVdGNkPTuQLMKyEjwOMhAgIMR, PvdyIPYzYuxTGYQjZbTucTrRGHTQkavB=False, DDRQlhrNSGpwTrokWitkZipdfbAqBFxv=DDRQlhrNSGpwTrokWitkZipdfbAqBFxv, fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc=fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.to_v = xwIQGNbJnSVpLrBBfhMLBchFpoolNzOe.DhMcMyEvvzmWIEJojbQeGHlzfZKiPzHO(FEAAZHeTRQEJCsYHCOEPpfOenpVZIhNT, mnMnCdMaVdGNkPTuQLMKyEjwOMhAgIMR, PvdyIPYzYuxTGYQjZbTucTrRGHTQkavB=False, DDRQlhrNSGpwTrokWitkZipdfbAqBFxv=DDRQlhrNSGpwTrokWitkZipdfbAqBFxv, fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc=fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.to_out = nn.Sequential(
            xwIQGNbJnSVpLrBBfhMLBchFpoolNzOe.DhMcMyEvvzmWIEJojbQeGHlzfZKiPzHO(mnMnCdMaVdGNkPTuQLMKyEjwOMhAgIMR, ZqiCYiNfDUNCIdHmASCiuNWYfvyqQifY, DDRQlhrNSGpwTrokWitkZipdfbAqBFxv=DDRQlhrNSGpwTrokWitkZipdfbAqBFxv, fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc=fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc),
            nn.Dropout(kcIxGCXrUvsLPSfmGoULGFzAthVmTXcA)
        )
    def lqBgIcSWZYylbCPjXksJWDguuSOqoPCJ(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, NECAaWUrFGIXcLimrerEYmxYIykQBfXb, tRdCjhUPYVVxnSEkGmJIHWRitDXRXSZS=None, GXNVXDlnsSLzkmussBPoJXgJwuXIiwsc=None, KHpRlHOzblljQyskecSxzUuWZtneWwta=None):
        xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.QEnKImSSxUuBDHahcSgvZCYYpzjKVrVk
        naEomsBBFfXCFQbEeoPZWKfGANfzcHCt = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.to_q(NECAaWUrFGIXcLimrerEYmxYIykQBfXb)
        tRdCjhUPYVVxnSEkGmJIHWRitDXRXSZS = zKvTEPbGDoRBsQSYYaddQKLTFDorvdms(tRdCjhUPYVVxnSEkGmJIHWRitDXRXSZS, NECAaWUrFGIXcLimrerEYmxYIykQBfXb)
        gHCkQmZHCJBMKEUaqadAmkHhDHcisxdV = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.to_k(tRdCjhUPYVVxnSEkGmJIHWRitDXRXSZS)
        if GXNVXDlnsSLzkmussBPoJXgJwuXIiwsc is not None:
            gHOriPzjESSuKHiMnHYjcVRXlkPrtamV = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.to_v(GXNVXDlnsSLzkmussBPoJXgJwuXIiwsc)
            del GXNVXDlnsSLzkmussBPoJXgJwuXIiwsc
        else:
            gHOriPzjESSuKHiMnHYjcVRXlkPrtamV = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.to_v(tRdCjhUPYVVxnSEkGmJIHWRitDXRXSZS)
        del tRdCjhUPYVVxnSEkGmJIHWRitDXRXSZS, NECAaWUrFGIXcLimrerEYmxYIykQBfXb
        mxaMgfLZUDPObiqkdCgHnnARjBNVGQnh, EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm, powGafreWfwlSAqPpTpUhFgpFVqCPavl = map(lambda XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz: rearrange(XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz, 'b n (h d) -> (b h) n d', xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab=xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab), (naEomsBBFfXCFQbEeoPZWKfGANfzcHCt, gHCkQmZHCJBMKEUaqadAmkHhDHcisxdV, gHOriPzjESSuKHiMnHYjcVRXlkPrtamV))
        del naEomsBBFfXCFQbEeoPZWKfGANfzcHCt, gHCkQmZHCJBMKEUaqadAmkHhDHcisxdV, gHOriPzjESSuKHiMnHYjcVRXlkPrtamV
        apACmNWgYmlQTXHPQlhMzlFpreaoNbwW = torch.zeros(mxaMgfLZUDPObiqkdCgHnnARjBNVGQnh.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[0], mxaMgfLZUDPObiqkdCgHnnARjBNVGQnh.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[1], powGafreWfwlSAqPpTpUhFgpFVqCPavl.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[2], fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc=mxaMgfLZUDPObiqkdCgHnnARjBNVGQnh.fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc, DDRQlhrNSGpwTrokWitkZipdfbAqBFxv=mxaMgfLZUDPObiqkdCgHnnARjBNVGQnh.DDRQlhrNSGpwTrokWitkZipdfbAqBFxv)
        GPfGQFkmkbPdFypYtapiuNmsHHdeiLUL = model_management.pEiuPTHzmozHhNpBwWGAaONYuNGSpuqI(mxaMgfLZUDPObiqkdCgHnnARjBNVGQnh.fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc)
        phzLQGCUmzLbVFGkMTvzdkdzRosviliv = 1024 ** 3
        zFHMWWyGvdkMWuoMhXMvojVdQBgrBFJN = mxaMgfLZUDPObiqkdCgHnnARjBNVGQnh.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[0] * mxaMgfLZUDPObiqkdCgHnnARjBNVGQnh.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[1] * EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[1] * mxaMgfLZUDPObiqkdCgHnnARjBNVGQnh.element_size()
        uagghsEwpSSqmsjyWKQSfwSRZBLmwawS = 3 if mxaMgfLZUDPObiqkdCgHnnARjBNVGQnh.element_size() == 2 else 2.5
        tTsKDmbmbyaWMYgSLHQnRfOIRMuZWWXp = zFHMWWyGvdkMWuoMhXMvojVdQBgrBFJN * uagghsEwpSSqmsjyWKQSfwSRZBLmwawS
        TMepbhrhtxHODfHDPkWDjgPPPikciJwm = 1
        if tTsKDmbmbyaWMYgSLHQnRfOIRMuZWWXp > GPfGQFkmkbPdFypYtapiuNmsHHdeiLUL:
            TMepbhrhtxHODfHDPkWDjgPPPikciJwm = 2**(math.ceil(math.DJwhOGBaLcOjmXnuwXMXOyhMtknqkKXL(tTsKDmbmbyaWMYgSLHQnRfOIRMuZWWXp / GPfGQFkmkbPdFypYtapiuNmsHHdeiLUL, 2)))
        if TMepbhrhtxHODfHDPkWDjgPPPikciJwm > 64:
            hYTYdntUiTVWcWIjglogGmmOgUDIwVIl = math.floor(math.sqrt(math.sqrt(GPfGQFkmkbPdFypYtapiuNmsHHdeiLUL / 2.5)) / 8) * 64
            raise RuntimeError(f'Not enough memory, use lower resolution (max approx. {max_res}x{max_res}). '
                               f'Need: {mem_required/64/gb:0.1f}GB free, Have:{mem_free_total/gb:0.1f}GB free')
        YcLwuVbfPTuRTuZGXPRlLPMsuGweuWbX = False
        zYwiPdMrQvYxkXLZyUdKGBlvOvNCrGfv = False
        while True:
            try:
                foSXFEftRhafROZSdfioWvUHDRtUeRyD = mxaMgfLZUDPObiqkdCgHnnARjBNVGQnh.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[1] // TMepbhrhtxHODfHDPkWDjgPPPikciJwm if (mxaMgfLZUDPObiqkdCgHnnARjBNVGQnh.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[1] % TMepbhrhtxHODfHDPkWDjgPPPikciJwm) == 0 else mxaMgfLZUDPObiqkdCgHnnARjBNVGQnh.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[1]
                for HCXmerBqIMuTscBONzTGKYapYSxWTYHo in range(0, mxaMgfLZUDPObiqkdCgHnnARjBNVGQnh.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[1], foSXFEftRhafROZSdfioWvUHDRtUeRyD):
                    lGLYgANCchGMWZfAOSVuiBulTGaEVaQM = HCXmerBqIMuTscBONzTGKYapYSxWTYHo + foSXFEftRhafROZSdfioWvUHDRtUeRyD
                    if JGhGmYoXIfioVVfVVRkJUtotlxRVouBT =="fp32":
                        with torch.autocast(ClvYjtcXylmicwCwVQPykJTWmcwImVEP=False, device_type = 'cuda'):
                            XauksjEFAUvtInEaALXIwUhurkUuooOF = einsum('b i d, b j d -> b i j', mxaMgfLZUDPObiqkdCgHnnARjBNVGQnh[:, HCXmerBqIMuTscBONzTGKYapYSxWTYHo:lGLYgANCchGMWZfAOSVuiBulTGaEVaQM].float(), EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm.float()) * rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.xmbXivThLFnawFPAJvIDBztziWsaDyEE
                    else:
                        XauksjEFAUvtInEaALXIwUhurkUuooOF = einsum('b i d, b j d -> b i j', mxaMgfLZUDPObiqkdCgHnnARjBNVGQnh[:, HCXmerBqIMuTscBONzTGKYapYSxWTYHo:lGLYgANCchGMWZfAOSVuiBulTGaEVaQM], EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm) * rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.xmbXivThLFnawFPAJvIDBztziWsaDyEE
                    YcLwuVbfPTuRTuZGXPRlLPMsuGweuWbX = True
                    orjPyVtdqCXZbZZCrekqzXxPBGSWSqJa = XauksjEFAUvtInEaALXIwUhurkUuooOF.softmax(yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk=-1).sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ(powGafreWfwlSAqPpTpUhFgpFVqCPavl.DDRQlhrNSGpwTrokWitkZipdfbAqBFxv)
                    del XauksjEFAUvtInEaALXIwUhurkUuooOF
                    apACmNWgYmlQTXHPQlhMzlFpreaoNbwW[:, HCXmerBqIMuTscBONzTGKYapYSxWTYHo:lGLYgANCchGMWZfAOSVuiBulTGaEVaQM] = einsum('b i j, b j d -> b i d', orjPyVtdqCXZbZZCrekqzXxPBGSWSqJa, powGafreWfwlSAqPpTpUhFgpFVqCPavl)
                    del orjPyVtdqCXZbZZCrekqzXxPBGSWSqJa
                break
            except model_management.uiFxRFoacIkrFnuAQlLvqBYROTajCRaW as dgvKdkEDrMSdkCaRxfkDNVbaXWUetgtO:
                if YcLwuVbfPTuRTuZGXPRlLPMsuGweuWbX == False:
                    model_management.sIeWDNiYvNWPLHobyjQHaTvlWZnazsHi(True)
                    if zYwiPdMrQvYxkXLZyUdKGBlvOvNCrGfv == False:
                        zYwiPdMrQvYxkXLZyUdKGBlvOvNCrGfv = True
                        print("out of memory error, emptying cache and trying again")
                        continue
                    TMepbhrhtxHODfHDPkWDjgPPPikciJwm *= 2
                    if TMepbhrhtxHODfHDPkWDjgPPPikciJwm > 64:
                        raise dgvKdkEDrMSdkCaRxfkDNVbaXWUetgtO
                    print("out of memory error, increasing steps and trying again", TMepbhrhtxHODfHDPkWDjgPPPikciJwm)
                else:
                    raise dgvKdkEDrMSdkCaRxfkDNVbaXWUetgtO
        del mxaMgfLZUDPObiqkdCgHnnARjBNVGQnh, EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm, powGafreWfwlSAqPpTpUhFgpFVqCPavl
        jUXrpBDWrfGGiwtyaMexgPCaBaIoLdEZ = rearrange(apACmNWgYmlQTXHPQlhMzlFpreaoNbwW, '(b h) n d -> b n (h d)', xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab=xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab)
        del apACmNWgYmlQTXHPQlhMzlFpreaoNbwW
        return rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.to_out(jUXrpBDWrfGGiwtyaMexgPCaBaIoLdEZ)
class qQrohQXiAITQznFuShydRodggjOWexBZ(nn.Module):
    def __init__(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, ZqiCYiNfDUNCIdHmASCiuNWYfvyqQifY, FEAAZHeTRQEJCsYHCOEPpfOenpVZIhNT=None, QEnKImSSxUuBDHahcSgvZCYYpzjKVrVk=8, QiYWcbRqbdDfAfhjULhYwmIlOStjgPlv=64, kcIxGCXrUvsLPSfmGoULGFzAthVmTXcA=0., DDRQlhrNSGpwTrokWitkZipdfbAqBFxv=None, fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc=None, xwIQGNbJnSVpLrBBfhMLBchFpoolNzOe=quasar.ops):
        super().__init__()
        mnMnCdMaVdGNkPTuQLMKyEjwOMhAgIMR = QiYWcbRqbdDfAfhjULhYwmIlOStjgPlv * QEnKImSSxUuBDHahcSgvZCYYpzjKVrVk
        FEAAZHeTRQEJCsYHCOEPpfOenpVZIhNT = zKvTEPbGDoRBsQSYYaddQKLTFDorvdms(FEAAZHeTRQEJCsYHCOEPpfOenpVZIhNT, ZqiCYiNfDUNCIdHmASCiuNWYfvyqQifY)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.xmbXivThLFnawFPAJvIDBztziWsaDyEE = QiYWcbRqbdDfAfhjULhYwmIlOStjgPlv ** -0.5
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.QEnKImSSxUuBDHahcSgvZCYYpzjKVrVk = QEnKImSSxUuBDHahcSgvZCYYpzjKVrVk
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.to_q = xwIQGNbJnSVpLrBBfhMLBchFpoolNzOe.DhMcMyEvvzmWIEJojbQeGHlzfZKiPzHO(ZqiCYiNfDUNCIdHmASCiuNWYfvyqQifY, mnMnCdMaVdGNkPTuQLMKyEjwOMhAgIMR, PvdyIPYzYuxTGYQjZbTucTrRGHTQkavB=False, DDRQlhrNSGpwTrokWitkZipdfbAqBFxv=DDRQlhrNSGpwTrokWitkZipdfbAqBFxv, fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc=fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.to_k = xwIQGNbJnSVpLrBBfhMLBchFpoolNzOe.DhMcMyEvvzmWIEJojbQeGHlzfZKiPzHO(FEAAZHeTRQEJCsYHCOEPpfOenpVZIhNT, mnMnCdMaVdGNkPTuQLMKyEjwOMhAgIMR, PvdyIPYzYuxTGYQjZbTucTrRGHTQkavB=False, DDRQlhrNSGpwTrokWitkZipdfbAqBFxv=DDRQlhrNSGpwTrokWitkZipdfbAqBFxv, fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc=fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.to_v = xwIQGNbJnSVpLrBBfhMLBchFpoolNzOe.DhMcMyEvvzmWIEJojbQeGHlzfZKiPzHO(FEAAZHeTRQEJCsYHCOEPpfOenpVZIhNT, mnMnCdMaVdGNkPTuQLMKyEjwOMhAgIMR, PvdyIPYzYuxTGYQjZbTucTrRGHTQkavB=False, DDRQlhrNSGpwTrokWitkZipdfbAqBFxv=DDRQlhrNSGpwTrokWitkZipdfbAqBFxv, fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc=fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.to_out = nn.Sequential(
            xwIQGNbJnSVpLrBBfhMLBchFpoolNzOe.DhMcMyEvvzmWIEJojbQeGHlzfZKiPzHO(mnMnCdMaVdGNkPTuQLMKyEjwOMhAgIMR, ZqiCYiNfDUNCIdHmASCiuNWYfvyqQifY, DDRQlhrNSGpwTrokWitkZipdfbAqBFxv=DDRQlhrNSGpwTrokWitkZipdfbAqBFxv, fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc=fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc),
            nn.Dropout(kcIxGCXrUvsLPSfmGoULGFzAthVmTXcA)
        )
    def lqBgIcSWZYylbCPjXksJWDguuSOqoPCJ(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, NECAaWUrFGIXcLimrerEYmxYIykQBfXb, tRdCjhUPYVVxnSEkGmJIHWRitDXRXSZS=None, GXNVXDlnsSLzkmussBPoJXgJwuXIiwsc=None, KHpRlHOzblljQyskecSxzUuWZtneWwta=None):
        xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.QEnKImSSxUuBDHahcSgvZCYYpzjKVrVk
        mxaMgfLZUDPObiqkdCgHnnARjBNVGQnh = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.to_q(NECAaWUrFGIXcLimrerEYmxYIykQBfXb)
        tRdCjhUPYVVxnSEkGmJIHWRitDXRXSZS = zKvTEPbGDoRBsQSYYaddQKLTFDorvdms(tRdCjhUPYVVxnSEkGmJIHWRitDXRXSZS, NECAaWUrFGIXcLimrerEYmxYIykQBfXb)
        EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.to_k(tRdCjhUPYVVxnSEkGmJIHWRitDXRXSZS)
        if GXNVXDlnsSLzkmussBPoJXgJwuXIiwsc is not None:
            powGafreWfwlSAqPpTpUhFgpFVqCPavl = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.to_v(GXNVXDlnsSLzkmussBPoJXgJwuXIiwsc)
            del GXNVXDlnsSLzkmussBPoJXgJwuXIiwsc
        else:
            powGafreWfwlSAqPpTpUhFgpFVqCPavl = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.to_v(tRdCjhUPYVVxnSEkGmJIHWRitDXRXSZS)
        mxaMgfLZUDPObiqkdCgHnnARjBNVGQnh, EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm, powGafreWfwlSAqPpTpUhFgpFVqCPavl = map(lambda XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz: rearrange(XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz, 'b n (h d) -> (b h) n d', xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab=xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab), (mxaMgfLZUDPObiqkdCgHnnARjBNVGQnh, EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm, powGafreWfwlSAqPpTpUhFgpFVqCPavl))
        if JGhGmYoXIfioVVfVVRkJUtotlxRVouBT =="fp32":
            with torch.autocast(ClvYjtcXylmicwCwVQPykJTWmcwImVEP=False, device_type = 'cuda'):
                mxaMgfLZUDPObiqkdCgHnnARjBNVGQnh, EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm = mxaMgfLZUDPObiqkdCgHnnARjBNVGQnh.float(), EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm.float()
                CBMGVWLyMSnHAKHGQSLkPoYlFwOOlDBz = einsum('b i d, b j d -> b i j', mxaMgfLZUDPObiqkdCgHnnARjBNVGQnh, EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm) * rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.xmbXivThLFnawFPAJvIDBztziWsaDyEE
        else:
            CBMGVWLyMSnHAKHGQSLkPoYlFwOOlDBz = einsum('b i d, b j d -> b i j', mxaMgfLZUDPObiqkdCgHnnARjBNVGQnh, EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm) * rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.xmbXivThLFnawFPAJvIDBztziWsaDyEE
        del mxaMgfLZUDPObiqkdCgHnnARjBNVGQnh, EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm
        if CzuSRmujwDQnNtuxpiDhURIOWmCdbjjH(KHpRlHOzblljQyskecSxzUuWZtneWwta):
            KHpRlHOzblljQyskecSxzUuWZtneWwta = rearrange(KHpRlHOzblljQyskecSxzUuWZtneWwta, 'b ... -> b (...)')
            EhnojrGhJngfjyuBMSfsPyqqacULAQoV = -torch.finfo(CBMGVWLyMSnHAKHGQSLkPoYlFwOOlDBz.DDRQlhrNSGpwTrokWitkZipdfbAqBFxv).max
            KHpRlHOzblljQyskecSxzUuWZtneWwta = kYXcbCDGZMxtOlIZeOtGMsNePlSickQL(KHpRlHOzblljQyskecSxzUuWZtneWwta, 'b j -> (b h) () j', xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab=xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab)
            CBMGVWLyMSnHAKHGQSLkPoYlFwOOlDBz.masked_fill_(~KHpRlHOzblljQyskecSxzUuWZtneWwta, EhnojrGhJngfjyuBMSfsPyqqacULAQoV)
        CBMGVWLyMSnHAKHGQSLkPoYlFwOOlDBz = CBMGVWLyMSnHAKHGQSLkPoYlFwOOlDBz.softmax(yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk=-1)
        iqymPVpxyjOWChGwBkTemSzHJbnJdAIz = einsum('b i j, b j d -> b i d', CBMGVWLyMSnHAKHGQSLkPoYlFwOOlDBz, powGafreWfwlSAqPpTpUhFgpFVqCPavl)
        iqymPVpxyjOWChGwBkTemSzHJbnJdAIz = rearrange(iqymPVpxyjOWChGwBkTemSzHJbnJdAIz, '(b h) n d -> b n (h d)', xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab=xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab)
        return rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.to_out(iqymPVpxyjOWChGwBkTemSzHJbnJdAIz)
class jfuIbfkFdWANZYpHZjuHkfnjaHCwdire(nn.Module):
    def __init__(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, ZqiCYiNfDUNCIdHmASCiuNWYfvyqQifY, FEAAZHeTRQEJCsYHCOEPpfOenpVZIhNT=None, QEnKImSSxUuBDHahcSgvZCYYpzjKVrVk=8, QiYWcbRqbdDfAfhjULhYwmIlOStjgPlv=64, kcIxGCXrUvsLPSfmGoULGFzAthVmTXcA=0.0, DDRQlhrNSGpwTrokWitkZipdfbAqBFxv=None, fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc=None, xwIQGNbJnSVpLrBBfhMLBchFpoolNzOe=quasar.ops):
        super().__init__()
        mnMnCdMaVdGNkPTuQLMKyEjwOMhAgIMR = QiYWcbRqbdDfAfhjULhYwmIlOStjgPlv * QEnKImSSxUuBDHahcSgvZCYYpzjKVrVk
        FEAAZHeTRQEJCsYHCOEPpfOenpVZIhNT = zKvTEPbGDoRBsQSYYaddQKLTFDorvdms(FEAAZHeTRQEJCsYHCOEPpfOenpVZIhNT, ZqiCYiNfDUNCIdHmASCiuNWYfvyqQifY)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.QEnKImSSxUuBDHahcSgvZCYYpzjKVrVk = QEnKImSSxUuBDHahcSgvZCYYpzjKVrVk
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.QiYWcbRqbdDfAfhjULhYwmIlOStjgPlv = QiYWcbRqbdDfAfhjULhYwmIlOStjgPlv
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.to_q = xwIQGNbJnSVpLrBBfhMLBchFpoolNzOe.DhMcMyEvvzmWIEJojbQeGHlzfZKiPzHO(ZqiCYiNfDUNCIdHmASCiuNWYfvyqQifY, mnMnCdMaVdGNkPTuQLMKyEjwOMhAgIMR, PvdyIPYzYuxTGYQjZbTucTrRGHTQkavB=False, DDRQlhrNSGpwTrokWitkZipdfbAqBFxv=DDRQlhrNSGpwTrokWitkZipdfbAqBFxv, fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc=fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.to_k = xwIQGNbJnSVpLrBBfhMLBchFpoolNzOe.DhMcMyEvvzmWIEJojbQeGHlzfZKiPzHO(FEAAZHeTRQEJCsYHCOEPpfOenpVZIhNT, mnMnCdMaVdGNkPTuQLMKyEjwOMhAgIMR, PvdyIPYzYuxTGYQjZbTucTrRGHTQkavB=False, DDRQlhrNSGpwTrokWitkZipdfbAqBFxv=DDRQlhrNSGpwTrokWitkZipdfbAqBFxv, fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc=fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.to_v = xwIQGNbJnSVpLrBBfhMLBchFpoolNzOe.DhMcMyEvvzmWIEJojbQeGHlzfZKiPzHO(FEAAZHeTRQEJCsYHCOEPpfOenpVZIhNT, mnMnCdMaVdGNkPTuQLMKyEjwOMhAgIMR, PvdyIPYzYuxTGYQjZbTucTrRGHTQkavB=False, DDRQlhrNSGpwTrokWitkZipdfbAqBFxv=DDRQlhrNSGpwTrokWitkZipdfbAqBFxv, fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc=fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.to_out = nn.Sequential(xwIQGNbJnSVpLrBBfhMLBchFpoolNzOe.DhMcMyEvvzmWIEJojbQeGHlzfZKiPzHO(mnMnCdMaVdGNkPTuQLMKyEjwOMhAgIMR, ZqiCYiNfDUNCIdHmASCiuNWYfvyqQifY, DDRQlhrNSGpwTrokWitkZipdfbAqBFxv=DDRQlhrNSGpwTrokWitkZipdfbAqBFxv, fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc=fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc), nn.Dropout(kcIxGCXrUvsLPSfmGoULGFzAthVmTXcA))
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.attention_op: Optional[Any] = None
    def lqBgIcSWZYylbCPjXksJWDguuSOqoPCJ(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, NECAaWUrFGIXcLimrerEYmxYIykQBfXb, tRdCjhUPYVVxnSEkGmJIHWRitDXRXSZS=None, GXNVXDlnsSLzkmussBPoJXgJwuXIiwsc=None, KHpRlHOzblljQyskecSxzUuWZtneWwta=None):
        mxaMgfLZUDPObiqkdCgHnnARjBNVGQnh = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.to_q(NECAaWUrFGIXcLimrerEYmxYIykQBfXb)
        tRdCjhUPYVVxnSEkGmJIHWRitDXRXSZS = zKvTEPbGDoRBsQSYYaddQKLTFDorvdms(tRdCjhUPYVVxnSEkGmJIHWRitDXRXSZS, NECAaWUrFGIXcLimrerEYmxYIykQBfXb)
        EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.to_k(tRdCjhUPYVVxnSEkGmJIHWRitDXRXSZS)
        if GXNVXDlnsSLzkmussBPoJXgJwuXIiwsc is not None:
            powGafreWfwlSAqPpTpUhFgpFVqCPavl = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.to_v(GXNVXDlnsSLzkmussBPoJXgJwuXIiwsc)
            del GXNVXDlnsSLzkmussBPoJXgJwuXIiwsc
        else:
            powGafreWfwlSAqPpTpUhFgpFVqCPavl = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.to_v(tRdCjhUPYVVxnSEkGmJIHWRitDXRXSZS)
        b, _, _ = mxaMgfLZUDPObiqkdCgHnnARjBNVGQnh.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg
        mxaMgfLZUDPObiqkdCgHnnARjBNVGQnh, EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm, powGafreWfwlSAqPpTpUhFgpFVqCPavl = map(
            lambda XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz: XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz.unsqueeze(3)
            .reshape(b, XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[1], rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.QEnKImSSxUuBDHahcSgvZCYYpzjKVrVk, rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.QiYWcbRqbdDfAfhjULhYwmIlOStjgPlv)
            .permute(0, 2, 1, 3)
            .reshape(b * rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.QEnKImSSxUuBDHahcSgvZCYYpzjKVrVk, XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[1], rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.QiYWcbRqbdDfAfhjULhYwmIlOStjgPlv)
            .contiguous(),
            (mxaMgfLZUDPObiqkdCgHnnARjBNVGQnh, EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm, powGafreWfwlSAqPpTpUhFgpFVqCPavl),
        )
        iqymPVpxyjOWChGwBkTemSzHJbnJdAIz = xformers.ops.memory_efficient_attention(mxaMgfLZUDPObiqkdCgHnnARjBNVGQnh, EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm, powGafreWfwlSAqPpTpUhFgpFVqCPavl, attn_bias=None, bjtPzNLsLxvykINbAtlMwKlGJQooJtzI=rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.attention_op)
        if CzuSRmujwDQnNtuxpiDhURIOWmCdbjjH(KHpRlHOzblljQyskecSxzUuWZtneWwta):
            raise NotImplementedError
        iqymPVpxyjOWChGwBkTemSzHJbnJdAIz = (
            iqymPVpxyjOWChGwBkTemSzHJbnJdAIz.unsqueeze(0)
            .reshape(b, rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.QEnKImSSxUuBDHahcSgvZCYYpzjKVrVk, iqymPVpxyjOWChGwBkTemSzHJbnJdAIz.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[1], rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.QiYWcbRqbdDfAfhjULhYwmIlOStjgPlv)
            .permute(0, 2, 1, 3)
            .reshape(b, iqymPVpxyjOWChGwBkTemSzHJbnJdAIz.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[1], rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.QEnKImSSxUuBDHahcSgvZCYYpzjKVrVk * rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.QiYWcbRqbdDfAfhjULhYwmIlOStjgPlv)
        )
        return rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.to_out(iqymPVpxyjOWChGwBkTemSzHJbnJdAIz)
class vZWIKOyHrbMmYJeCIbyCkrAIYbpZYpRv(nn.Module):
    def __init__(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, ZqiCYiNfDUNCIdHmASCiuNWYfvyqQifY, FEAAZHeTRQEJCsYHCOEPpfOenpVZIhNT=None, QEnKImSSxUuBDHahcSgvZCYYpzjKVrVk=8, QiYWcbRqbdDfAfhjULhYwmIlOStjgPlv=64, kcIxGCXrUvsLPSfmGoULGFzAthVmTXcA=0., DDRQlhrNSGpwTrokWitkZipdfbAqBFxv=None, fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc=None, xwIQGNbJnSVpLrBBfhMLBchFpoolNzOe=quasar.ops):
        super().__init__()
        mnMnCdMaVdGNkPTuQLMKyEjwOMhAgIMR = QiYWcbRqbdDfAfhjULhYwmIlOStjgPlv * QEnKImSSxUuBDHahcSgvZCYYpzjKVrVk
        FEAAZHeTRQEJCsYHCOEPpfOenpVZIhNT = zKvTEPbGDoRBsQSYYaddQKLTFDorvdms(FEAAZHeTRQEJCsYHCOEPpfOenpVZIhNT, ZqiCYiNfDUNCIdHmASCiuNWYfvyqQifY)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.QEnKImSSxUuBDHahcSgvZCYYpzjKVrVk = QEnKImSSxUuBDHahcSgvZCYYpzjKVrVk
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.QiYWcbRqbdDfAfhjULhYwmIlOStjgPlv = QiYWcbRqbdDfAfhjULhYwmIlOStjgPlv
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.to_q = xwIQGNbJnSVpLrBBfhMLBchFpoolNzOe.DhMcMyEvvzmWIEJojbQeGHlzfZKiPzHO(ZqiCYiNfDUNCIdHmASCiuNWYfvyqQifY, mnMnCdMaVdGNkPTuQLMKyEjwOMhAgIMR, PvdyIPYzYuxTGYQjZbTucTrRGHTQkavB=False, DDRQlhrNSGpwTrokWitkZipdfbAqBFxv=DDRQlhrNSGpwTrokWitkZipdfbAqBFxv, fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc=fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.to_k = xwIQGNbJnSVpLrBBfhMLBchFpoolNzOe.DhMcMyEvvzmWIEJojbQeGHlzfZKiPzHO(FEAAZHeTRQEJCsYHCOEPpfOenpVZIhNT, mnMnCdMaVdGNkPTuQLMKyEjwOMhAgIMR, PvdyIPYzYuxTGYQjZbTucTrRGHTQkavB=False, DDRQlhrNSGpwTrokWitkZipdfbAqBFxv=DDRQlhrNSGpwTrokWitkZipdfbAqBFxv, fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc=fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.to_v = xwIQGNbJnSVpLrBBfhMLBchFpoolNzOe.DhMcMyEvvzmWIEJojbQeGHlzfZKiPzHO(FEAAZHeTRQEJCsYHCOEPpfOenpVZIhNT, mnMnCdMaVdGNkPTuQLMKyEjwOMhAgIMR, PvdyIPYzYuxTGYQjZbTucTrRGHTQkavB=False, DDRQlhrNSGpwTrokWitkZipdfbAqBFxv=DDRQlhrNSGpwTrokWitkZipdfbAqBFxv, fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc=fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.to_out = nn.Sequential(xwIQGNbJnSVpLrBBfhMLBchFpoolNzOe.DhMcMyEvvzmWIEJojbQeGHlzfZKiPzHO(mnMnCdMaVdGNkPTuQLMKyEjwOMhAgIMR, ZqiCYiNfDUNCIdHmASCiuNWYfvyqQifY, DDRQlhrNSGpwTrokWitkZipdfbAqBFxv=DDRQlhrNSGpwTrokWitkZipdfbAqBFxv, fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc=fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc), nn.Dropout(kcIxGCXrUvsLPSfmGoULGFzAthVmTXcA))
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.attention_op: Optional[Any] = None
    def lqBgIcSWZYylbCPjXksJWDguuSOqoPCJ(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, NECAaWUrFGIXcLimrerEYmxYIykQBfXb, tRdCjhUPYVVxnSEkGmJIHWRitDXRXSZS=None, GXNVXDlnsSLzkmussBPoJXgJwuXIiwsc=None, KHpRlHOzblljQyskecSxzUuWZtneWwta=None):
        mxaMgfLZUDPObiqkdCgHnnARjBNVGQnh = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.to_q(NECAaWUrFGIXcLimrerEYmxYIykQBfXb)
        tRdCjhUPYVVxnSEkGmJIHWRitDXRXSZS = zKvTEPbGDoRBsQSYYaddQKLTFDorvdms(tRdCjhUPYVVxnSEkGmJIHWRitDXRXSZS, NECAaWUrFGIXcLimrerEYmxYIykQBfXb)
        EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.to_k(tRdCjhUPYVVxnSEkGmJIHWRitDXRXSZS)
        if GXNVXDlnsSLzkmussBPoJXgJwuXIiwsc is not None:
            powGafreWfwlSAqPpTpUhFgpFVqCPavl = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.to_v(GXNVXDlnsSLzkmussBPoJXgJwuXIiwsc)
            del GXNVXDlnsSLzkmussBPoJXgJwuXIiwsc
        else:
            powGafreWfwlSAqPpTpUhFgpFVqCPavl = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.to_v(tRdCjhUPYVVxnSEkGmJIHWRitDXRXSZS)
        b, _, _ = mxaMgfLZUDPObiqkdCgHnnARjBNVGQnh.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg
        mxaMgfLZUDPObiqkdCgHnnARjBNVGQnh, EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm, powGafreWfwlSAqPpTpUhFgpFVqCPavl = map(
            lambda XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz: XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz.view(b, -1, rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.QEnKImSSxUuBDHahcSgvZCYYpzjKVrVk, rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.QiYWcbRqbdDfAfhjULhYwmIlOStjgPlv).transpose(1, 2),
            (mxaMgfLZUDPObiqkdCgHnnARjBNVGQnh, EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm, powGafreWfwlSAqPpTpUhFgpFVqCPavl),
        )
        iqymPVpxyjOWChGwBkTemSzHJbnJdAIz = torch.nn.functional.scaled_dot_product_attention(mxaMgfLZUDPObiqkdCgHnnARjBNVGQnh, EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm, powGafreWfwlSAqPpTpUhFgpFVqCPavl, attn_mask=None, dropout_p=0.0, is_causal=False)
        if CzuSRmujwDQnNtuxpiDhURIOWmCdbjjH(KHpRlHOzblljQyskecSxzUuWZtneWwta):
            raise NotImplementedError
        iqymPVpxyjOWChGwBkTemSzHJbnJdAIz = (
            iqymPVpxyjOWChGwBkTemSzHJbnJdAIz.transpose(1, 2).reshape(b, -1, rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.QEnKImSSxUuBDHahcSgvZCYYpzjKVrVk * rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.QiYWcbRqbdDfAfhjULhYwmIlOStjgPlv)
        )
        return rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.to_out(iqymPVpxyjOWChGwBkTemSzHJbnJdAIz)
if model_management.fpzqQPwQsgljpVXCeYPLnjVJExRYKmpM():
    print("Using xformers cross attention")
    qQrohQXiAITQznFuShydRodggjOWexBZ = jfuIbfkFdWANZYpHZjuHkfnjaHCwdire
elif model_management.kQDSfcrSuHTuIBtYUKBNyIxOCqzlxNlm():
    print("Using pytorch cross attention")
    qQrohQXiAITQznFuShydRodggjOWexBZ = vZWIKOyHrbMmYJeCIbyCkrAIYbpZYpRv
else:
    if DukiculvUpjhZIVvaGinshRSKLSTgVVl.use_split_cross_attention:
        print("Using split optimization for cross attention")
        qQrohQXiAITQznFuShydRodggjOWexBZ = NPAwEAqrUFoUkOcUyBXukXyENmexVjRW
    else:
        print("Using sub quadratic optimization for cross attention, if you have memory or speed issues try using: --use-split-cross-attention")
        qQrohQXiAITQznFuShydRodggjOWexBZ = DmzUHgaxPAiRWNJrogZnoPnKOIZhuATL
class jNzzEqqHtiqYqWsjrvuVQcwKYdkrmxdM(nn.Module):
    def __init__(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk, QJCnIiVfahCOVrhUgUzEjPLvCsBDwnir, SiOpzQSDRgWVXXhLenDXhMYFnSfQmjiy, kcIxGCXrUvsLPSfmGoULGFzAthVmTXcA=0., FEAAZHeTRQEJCsYHCOEPpfOenpVZIhNT=None, gated_ff=True, vcSlHLxBcVodHmZrzACHLEJuENMXjWTG=True,
                 ylReNVtjXdQbeAwJXhTkOjiHrFPToKDa=False, DDRQlhrNSGpwTrokWitkZipdfbAqBFxv=None, fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc=None, xwIQGNbJnSVpLrBBfhMLBchFpoolNzOe=quasar.ops):
        super().__init__()
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.ylReNVtjXdQbeAwJXhTkOjiHrFPToKDa = ylReNVtjXdQbeAwJXhTkOjiHrFPToKDa
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.attn1 = qQrohQXiAITQznFuShydRodggjOWexBZ(ZqiCYiNfDUNCIdHmASCiuNWYfvyqQifY=yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk, QEnKImSSxUuBDHahcSgvZCYYpzjKVrVk=QJCnIiVfahCOVrhUgUzEjPLvCsBDwnir, QiYWcbRqbdDfAfhjULhYwmIlOStjgPlv=SiOpzQSDRgWVXXhLenDXhMYFnSfQmjiy, kcIxGCXrUvsLPSfmGoULGFzAthVmTXcA=kcIxGCXrUvsLPSfmGoULGFzAthVmTXcA,
                              FEAAZHeTRQEJCsYHCOEPpfOenpVZIhNT=FEAAZHeTRQEJCsYHCOEPpfOenpVZIhNT if rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.ylReNVtjXdQbeAwJXhTkOjiHrFPToKDa else None, DDRQlhrNSGpwTrokWitkZipdfbAqBFxv=DDRQlhrNSGpwTrokWitkZipdfbAqBFxv, fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc=fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc, xwIQGNbJnSVpLrBBfhMLBchFpoolNzOe=xwIQGNbJnSVpLrBBfhMLBchFpoolNzOe)  
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.ff = nVIpLCPoeZxavETSbXIKgqMNJkfGLLVs(yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk, kcIxGCXrUvsLPSfmGoULGFzAthVmTXcA=kcIxGCXrUvsLPSfmGoULGFzAthVmTXcA, glu=gated_ff, DDRQlhrNSGpwTrokWitkZipdfbAqBFxv=DDRQlhrNSGpwTrokWitkZipdfbAqBFxv, fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc=fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc, xwIQGNbJnSVpLrBBfhMLBchFpoolNzOe=xwIQGNbJnSVpLrBBfhMLBchFpoolNzOe)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.attn2 = qQrohQXiAITQznFuShydRodggjOWexBZ(ZqiCYiNfDUNCIdHmASCiuNWYfvyqQifY=yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk, FEAAZHeTRQEJCsYHCOEPpfOenpVZIhNT=FEAAZHeTRQEJCsYHCOEPpfOenpVZIhNT,
                              QEnKImSSxUuBDHahcSgvZCYYpzjKVrVk=QJCnIiVfahCOVrhUgUzEjPLvCsBDwnir, QiYWcbRqbdDfAfhjULhYwmIlOStjgPlv=SiOpzQSDRgWVXXhLenDXhMYFnSfQmjiy, kcIxGCXrUvsLPSfmGoULGFzAthVmTXcA=kcIxGCXrUvsLPSfmGoULGFzAthVmTXcA, DDRQlhrNSGpwTrokWitkZipdfbAqBFxv=DDRQlhrNSGpwTrokWitkZipdfbAqBFxv, fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc=fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc, xwIQGNbJnSVpLrBBfhMLBchFpoolNzOe=xwIQGNbJnSVpLrBBfhMLBchFpoolNzOe)  
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.norm1 = nn.SeaDiaiECtgJbgiExWzpSnrizTosOUam(yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk, DDRQlhrNSGpwTrokWitkZipdfbAqBFxv=DDRQlhrNSGpwTrokWitkZipdfbAqBFxv, fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc=fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.norm2 = nn.SeaDiaiECtgJbgiExWzpSnrizTosOUam(yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk, DDRQlhrNSGpwTrokWitkZipdfbAqBFxv=DDRQlhrNSGpwTrokWitkZipdfbAqBFxv, fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc=fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.norm3 = nn.SeaDiaiECtgJbgiExWzpSnrizTosOUam(yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk, DDRQlhrNSGpwTrokWitkZipdfbAqBFxv=DDRQlhrNSGpwTrokWitkZipdfbAqBFxv, fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc=fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.vcSlHLxBcVodHmZrzACHLEJuENMXjWTG = vcSlHLxBcVodHmZrzACHLEJuENMXjWTG
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.QJCnIiVfahCOVrhUgUzEjPLvCsBDwnir = QJCnIiVfahCOVrhUgUzEjPLvCsBDwnir
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.SiOpzQSDRgWVXXhLenDXhMYFnSfQmjiy = SiOpzQSDRgWVXXhLenDXhMYFnSfQmjiy
    def lqBgIcSWZYylbCPjXksJWDguuSOqoPCJ(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, NECAaWUrFGIXcLimrerEYmxYIykQBfXb, tRdCjhUPYVVxnSEkGmJIHWRitDXRXSZS=None, transformer_options={}):
        return vcSlHLxBcVodHmZrzACHLEJuENMXjWTG(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.NFbNMrWYGAqPnzmlcfuXjOSWmXVgbZMT, (NECAaWUrFGIXcLimrerEYmxYIykQBfXb, tRdCjhUPYVVxnSEkGmJIHWRitDXRXSZS, transformer_options), rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.parameters(), rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.vcSlHLxBcVodHmZrzACHLEJuENMXjWTG)
    def NFbNMrWYGAqPnzmlcfuXjOSWmXVgbZMT(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, NECAaWUrFGIXcLimrerEYmxYIykQBfXb, tRdCjhUPYVVxnSEkGmJIHWRitDXRXSZS=None, transformer_options={}):
        XlZLJsLRPiguOUrwnKgvbOtnsJeZSwPk = {}
        lPmJfojDSUTFirrgKPryiJRYyZOFajzZ = None
        ezGegSWVJhFXeteAWCHWUOVOTIwjKBBx = 0
        if "current_index" in transformer_options:
            XlZLJsLRPiguOUrwnKgvbOtnsJeZSwPk["transformer_index"] = transformer_options["current_index"]
        if "block_index" in transformer_options:
            ezGegSWVJhFXeteAWCHWUOVOTIwjKBBx = transformer_options["block_index"]
            XlZLJsLRPiguOUrwnKgvbOtnsJeZSwPk["block_index"] = ezGegSWVJhFXeteAWCHWUOVOTIwjKBBx
        if "original_shape" in transformer_options:
            XlZLJsLRPiguOUrwnKgvbOtnsJeZSwPk["original_shape"] = transformer_options["original_shape"]
        if "block" in transformer_options:
            lPmJfojDSUTFirrgKPryiJRYyZOFajzZ = transformer_options["block"]
            XlZLJsLRPiguOUrwnKgvbOtnsJeZSwPk["block"] = lPmJfojDSUTFirrgKPryiJRYyZOFajzZ
        if "patches" in transformer_options:
            AAeyWOlXaAKNsAVBbCkNXANcpWvQHrqD = transformer_options["patches"]
        else:
            AAeyWOlXaAKNsAVBbCkNXANcpWvQHrqD = {}
        XlZLJsLRPiguOUrwnKgvbOtnsJeZSwPk["n_heads"] = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.QJCnIiVfahCOVrhUgUzEjPLvCsBDwnir
        XlZLJsLRPiguOUrwnKgvbOtnsJeZSwPk["dim_head"] = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.SiOpzQSDRgWVXXhLenDXhMYFnSfQmjiy
        if "patches_replace" in transformer_options:
            sNPuszSZfftSKpNLXWQFMgJMDsneguqy = transformer_options["patches_replace"]
        else:
            sNPuszSZfftSKpNLXWQFMgJMDsneguqy = {}
        zXHJFiFFvWqeQIAxyaTGMUgoRaHrYzjK = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.norm1(NECAaWUrFGIXcLimrerEYmxYIykQBfXb)
        if rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.ylReNVtjXdQbeAwJXhTkOjiHrFPToKDa:
            vJEaSmCEryvIDAzsJkuUImZZtrAtwEwD = tRdCjhUPYVVxnSEkGmJIHWRitDXRXSZS
        else:
            vJEaSmCEryvIDAzsJkuUImZZtrAtwEwD = None
        fFZXTHFiSWCHkYKiDRrJzdslyblsSCLp = None
        if "attn1_patch" in AAeyWOlXaAKNsAVBbCkNXANcpWvQHrqD:
            YBkyOiHLPkzbgIAzSqhyviJVGfxblkPn = AAeyWOlXaAKNsAVBbCkNXANcpWvQHrqD["attn1_patch"]
            if vJEaSmCEryvIDAzsJkuUImZZtrAtwEwD is None:
                vJEaSmCEryvIDAzsJkuUImZZtrAtwEwD = zXHJFiFFvWqeQIAxyaTGMUgoRaHrYzjK
            fFZXTHFiSWCHkYKiDRrJzdslyblsSCLp = vJEaSmCEryvIDAzsJkuUImZZtrAtwEwD
            for HutkrxeXIuRQKOhCWHkiwqLGAsJjUSKj in YBkyOiHLPkzbgIAzSqhyviJVGfxblkPn:
                zXHJFiFFvWqeQIAxyaTGMUgoRaHrYzjK, vJEaSmCEryvIDAzsJkuUImZZtrAtwEwD, fFZXTHFiSWCHkYKiDRrJzdslyblsSCLp = HutkrxeXIuRQKOhCWHkiwqLGAsJjUSKj(zXHJFiFFvWqeQIAxyaTGMUgoRaHrYzjK, vJEaSmCEryvIDAzsJkuUImZZtrAtwEwD, fFZXTHFiSWCHkYKiDRrJzdslyblsSCLp, XlZLJsLRPiguOUrwnKgvbOtnsJeZSwPk)
        if lPmJfojDSUTFirrgKPryiJRYyZOFajzZ is not None:
            vakHzpQAawIsgYGJFrmOdDnHevuiTIqE = (lPmJfojDSUTFirrgKPryiJRYyZOFajzZ[0], lPmJfojDSUTFirrgKPryiJRYyZOFajzZ[1], ezGegSWVJhFXeteAWCHWUOVOTIwjKBBx)
        else:
            vakHzpQAawIsgYGJFrmOdDnHevuiTIqE = None
        XQegtNARVNEfEuZhwiahsbBlgfBCycFu = sNPuszSZfftSKpNLXWQFMgJMDsneguqy.get("attn1", {})
        jkOLsNhVqaaLGvbiIAKXCnQPncjVKORJ = vakHzpQAawIsgYGJFrmOdDnHevuiTIqE
        if jkOLsNhVqaaLGvbiIAKXCnQPncjVKORJ not in XQegtNARVNEfEuZhwiahsbBlgfBCycFu:
            jkOLsNhVqaaLGvbiIAKXCnQPncjVKORJ = lPmJfojDSUTFirrgKPryiJRYyZOFajzZ
        if jkOLsNhVqaaLGvbiIAKXCnQPncjVKORJ in XQegtNARVNEfEuZhwiahsbBlgfBCycFu:
            if vJEaSmCEryvIDAzsJkuUImZZtrAtwEwD is None:
                vJEaSmCEryvIDAzsJkuUImZZtrAtwEwD = zXHJFiFFvWqeQIAxyaTGMUgoRaHrYzjK
                fFZXTHFiSWCHkYKiDRrJzdslyblsSCLp = zXHJFiFFvWqeQIAxyaTGMUgoRaHrYzjK
            zXHJFiFFvWqeQIAxyaTGMUgoRaHrYzjK = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.attn1.to_q(zXHJFiFFvWqeQIAxyaTGMUgoRaHrYzjK)
            vJEaSmCEryvIDAzsJkuUImZZtrAtwEwD = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.attn1.to_k(vJEaSmCEryvIDAzsJkuUImZZtrAtwEwD)
            fFZXTHFiSWCHkYKiDRrJzdslyblsSCLp = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.attn1.to_v(fFZXTHFiSWCHkYKiDRrJzdslyblsSCLp)
            zXHJFiFFvWqeQIAxyaTGMUgoRaHrYzjK = XQegtNARVNEfEuZhwiahsbBlgfBCycFu[jkOLsNhVqaaLGvbiIAKXCnQPncjVKORJ](zXHJFiFFvWqeQIAxyaTGMUgoRaHrYzjK, vJEaSmCEryvIDAzsJkuUImZZtrAtwEwD, fFZXTHFiSWCHkYKiDRrJzdslyblsSCLp, XlZLJsLRPiguOUrwnKgvbOtnsJeZSwPk)
            zXHJFiFFvWqeQIAxyaTGMUgoRaHrYzjK = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.attn1.to_out(zXHJFiFFvWqeQIAxyaTGMUgoRaHrYzjK)
        else:
            zXHJFiFFvWqeQIAxyaTGMUgoRaHrYzjK = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.attn1(zXHJFiFFvWqeQIAxyaTGMUgoRaHrYzjK, tRdCjhUPYVVxnSEkGmJIHWRitDXRXSZS=vJEaSmCEryvIDAzsJkuUImZZtrAtwEwD, GXNVXDlnsSLzkmussBPoJXgJwuXIiwsc=fFZXTHFiSWCHkYKiDRrJzdslyblsSCLp)
        if "attn1_output_patch" in AAeyWOlXaAKNsAVBbCkNXANcpWvQHrqD:
            YBkyOiHLPkzbgIAzSqhyviJVGfxblkPn = AAeyWOlXaAKNsAVBbCkNXANcpWvQHrqD["attn1_output_patch"]
            for HutkrxeXIuRQKOhCWHkiwqLGAsJjUSKj in YBkyOiHLPkzbgIAzSqhyviJVGfxblkPn:
                zXHJFiFFvWqeQIAxyaTGMUgoRaHrYzjK = HutkrxeXIuRQKOhCWHkiwqLGAsJjUSKj(zXHJFiFFvWqeQIAxyaTGMUgoRaHrYzjK, XlZLJsLRPiguOUrwnKgvbOtnsJeZSwPk)
        NECAaWUrFGIXcLimrerEYmxYIykQBfXb += zXHJFiFFvWqeQIAxyaTGMUgoRaHrYzjK
        if "middle_patch" in AAeyWOlXaAKNsAVBbCkNXANcpWvQHrqD:
            YBkyOiHLPkzbgIAzSqhyviJVGfxblkPn = AAeyWOlXaAKNsAVBbCkNXANcpWvQHrqD["middle_patch"]
            for HutkrxeXIuRQKOhCWHkiwqLGAsJjUSKj in YBkyOiHLPkzbgIAzSqhyviJVGfxblkPn:
                NECAaWUrFGIXcLimrerEYmxYIykQBfXb = HutkrxeXIuRQKOhCWHkiwqLGAsJjUSKj(NECAaWUrFGIXcLimrerEYmxYIykQBfXb, XlZLJsLRPiguOUrwnKgvbOtnsJeZSwPk)
        zXHJFiFFvWqeQIAxyaTGMUgoRaHrYzjK = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.norm2(NECAaWUrFGIXcLimrerEYmxYIykQBfXb)
        yZnthARNWsqGlwpVphOXaItSPLCErhDr = tRdCjhUPYVVxnSEkGmJIHWRitDXRXSZS
        ongBEoakxtrWDjxhnijJDwygyJjgXlYn = None
        if "attn2_patch" in AAeyWOlXaAKNsAVBbCkNXANcpWvQHrqD:
            YBkyOiHLPkzbgIAzSqhyviJVGfxblkPn = AAeyWOlXaAKNsAVBbCkNXANcpWvQHrqD["attn2_patch"]
            ongBEoakxtrWDjxhnijJDwygyJjgXlYn = yZnthARNWsqGlwpVphOXaItSPLCErhDr
            for HutkrxeXIuRQKOhCWHkiwqLGAsJjUSKj in YBkyOiHLPkzbgIAzSqhyviJVGfxblkPn:
                zXHJFiFFvWqeQIAxyaTGMUgoRaHrYzjK, yZnthARNWsqGlwpVphOXaItSPLCErhDr, ongBEoakxtrWDjxhnijJDwygyJjgXlYn = HutkrxeXIuRQKOhCWHkiwqLGAsJjUSKj(zXHJFiFFvWqeQIAxyaTGMUgoRaHrYzjK, yZnthARNWsqGlwpVphOXaItSPLCErhDr, ongBEoakxtrWDjxhnijJDwygyJjgXlYn, XlZLJsLRPiguOUrwnKgvbOtnsJeZSwPk)
        nzkHAhkeYmYisQeIQHruASemmnnDzYdv = sNPuszSZfftSKpNLXWQFMgJMDsneguqy.get("attn2", {})
        ozIdsXCtynQIAqSzYzHZDkJmKjKUPFoy = vakHzpQAawIsgYGJFrmOdDnHevuiTIqE
        if ozIdsXCtynQIAqSzYzHZDkJmKjKUPFoy not in nzkHAhkeYmYisQeIQHruASemmnnDzYdv:
            ozIdsXCtynQIAqSzYzHZDkJmKjKUPFoy = lPmJfojDSUTFirrgKPryiJRYyZOFajzZ
        if ozIdsXCtynQIAqSzYzHZDkJmKjKUPFoy in nzkHAhkeYmYisQeIQHruASemmnnDzYdv:
            if ongBEoakxtrWDjxhnijJDwygyJjgXlYn is None:
                ongBEoakxtrWDjxhnijJDwygyJjgXlYn = yZnthARNWsqGlwpVphOXaItSPLCErhDr
            zXHJFiFFvWqeQIAxyaTGMUgoRaHrYzjK = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.attn2.to_q(zXHJFiFFvWqeQIAxyaTGMUgoRaHrYzjK)
            yZnthARNWsqGlwpVphOXaItSPLCErhDr = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.attn2.to_k(yZnthARNWsqGlwpVphOXaItSPLCErhDr)
            ongBEoakxtrWDjxhnijJDwygyJjgXlYn = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.attn2.to_v(ongBEoakxtrWDjxhnijJDwygyJjgXlYn)
            zXHJFiFFvWqeQIAxyaTGMUgoRaHrYzjK = nzkHAhkeYmYisQeIQHruASemmnnDzYdv[ozIdsXCtynQIAqSzYzHZDkJmKjKUPFoy](zXHJFiFFvWqeQIAxyaTGMUgoRaHrYzjK, yZnthARNWsqGlwpVphOXaItSPLCErhDr, ongBEoakxtrWDjxhnijJDwygyJjgXlYn, XlZLJsLRPiguOUrwnKgvbOtnsJeZSwPk)
            zXHJFiFFvWqeQIAxyaTGMUgoRaHrYzjK = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.attn2.to_out(zXHJFiFFvWqeQIAxyaTGMUgoRaHrYzjK)
        else:
            zXHJFiFFvWqeQIAxyaTGMUgoRaHrYzjK = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.attn2(zXHJFiFFvWqeQIAxyaTGMUgoRaHrYzjK, tRdCjhUPYVVxnSEkGmJIHWRitDXRXSZS=yZnthARNWsqGlwpVphOXaItSPLCErhDr, GXNVXDlnsSLzkmussBPoJXgJwuXIiwsc=ongBEoakxtrWDjxhnijJDwygyJjgXlYn)
        if "attn2_output_patch" in AAeyWOlXaAKNsAVBbCkNXANcpWvQHrqD:
            YBkyOiHLPkzbgIAzSqhyviJVGfxblkPn = AAeyWOlXaAKNsAVBbCkNXANcpWvQHrqD["attn2_output_patch"]
            for HutkrxeXIuRQKOhCWHkiwqLGAsJjUSKj in YBkyOiHLPkzbgIAzSqhyviJVGfxblkPn:
                zXHJFiFFvWqeQIAxyaTGMUgoRaHrYzjK = HutkrxeXIuRQKOhCWHkiwqLGAsJjUSKj(zXHJFiFFvWqeQIAxyaTGMUgoRaHrYzjK, XlZLJsLRPiguOUrwnKgvbOtnsJeZSwPk)
        NECAaWUrFGIXcLimrerEYmxYIykQBfXb += zXHJFiFFvWqeQIAxyaTGMUgoRaHrYzjK
        NECAaWUrFGIXcLimrerEYmxYIykQBfXb = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.ff(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.norm3(NECAaWUrFGIXcLimrerEYmxYIykQBfXb)) + NECAaWUrFGIXcLimrerEYmxYIykQBfXb
        return NECAaWUrFGIXcLimrerEYmxYIykQBfXb
class CvuNifYqMqjsNqfVaEEpwROqJiOUCfhu(nn.Module):
    def __init__(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, EbKSIFxpyCpzycRDApduouVsxspHzkTj, QJCnIiVfahCOVrhUgUzEjPLvCsBDwnir, SiOpzQSDRgWVXXhLenDXhMYFnSfQmjiy,
                 JtnlCSDzHOgtbZVTfQMidKPjmOFZfzZX=1, kcIxGCXrUvsLPSfmGoULGFzAthVmTXcA=0., FEAAZHeTRQEJCsYHCOEPpfOenpVZIhNT=None,
                 ylReNVtjXdQbeAwJXhTkOjiHrFPToKDa=False, use_linear=False,
                 TkHgGRFhDYRqyKuFvQRlKbpOBXUaEDVU=True, DDRQlhrNSGpwTrokWitkZipdfbAqBFxv=None, fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc=None, xwIQGNbJnSVpLrBBfhMLBchFpoolNzOe=quasar.ops):
        super().__init__()
        if CzuSRmujwDQnNtuxpiDhURIOWmCdbjjH(FEAAZHeTRQEJCsYHCOEPpfOenpVZIhNT) and not isinstance(FEAAZHeTRQEJCsYHCOEPpfOenpVZIhNT, list):
            FEAAZHeTRQEJCsYHCOEPpfOenpVZIhNT = [FEAAZHeTRQEJCsYHCOEPpfOenpVZIhNT] * JtnlCSDzHOgtbZVTfQMidKPjmOFZfzZX
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.EbKSIFxpyCpzycRDApduouVsxspHzkTj = EbKSIFxpyCpzycRDApduouVsxspHzkTj
        mnMnCdMaVdGNkPTuQLMKyEjwOMhAgIMR = QJCnIiVfahCOVrhUgUzEjPLvCsBDwnir * SiOpzQSDRgWVXXhLenDXhMYFnSfQmjiy
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.norm = HSnGePyLrgZhiiSoMOwJmgVPBjIpItDD(EbKSIFxpyCpzycRDApduouVsxspHzkTj, DDRQlhrNSGpwTrokWitkZipdfbAqBFxv=DDRQlhrNSGpwTrokWitkZipdfbAqBFxv, fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc=fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc)
        if not use_linear:
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.proj_in = xwIQGNbJnSVpLrBBfhMLBchFpoolNzOe.LcFcvNeYCKrBHlNkoWrkqdbxdkNCJBBK(EbKSIFxpyCpzycRDApduouVsxspHzkTj,
                                     mnMnCdMaVdGNkPTuQLMKyEjwOMhAgIMR,
                                     aBEJjpEOpoRJYkulwSmukddEYErxRnAG=1,
                                     NTEWXstfzqNXGESmGkQNFWBaQsGAPlGd=1,
                                     sdxdTSjnkAOjlGmltQHvLiHRDstMzpAP=0, DDRQlhrNSGpwTrokWitkZipdfbAqBFxv=DDRQlhrNSGpwTrokWitkZipdfbAqBFxv, fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc=fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc)
        else:
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.proj_in = xwIQGNbJnSVpLrBBfhMLBchFpoolNzOe.DhMcMyEvvzmWIEJojbQeGHlzfZKiPzHO(EbKSIFxpyCpzycRDApduouVsxspHzkTj, mnMnCdMaVdGNkPTuQLMKyEjwOMhAgIMR, DDRQlhrNSGpwTrokWitkZipdfbAqBFxv=DDRQlhrNSGpwTrokWitkZipdfbAqBFxv, fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc=fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.transformer_blocks = nn.ModuleList(
            [jNzzEqqHtiqYqWsjrvuVQcwKYdkrmxdM(mnMnCdMaVdGNkPTuQLMKyEjwOMhAgIMR, QJCnIiVfahCOVrhUgUzEjPLvCsBDwnir, SiOpzQSDRgWVXXhLenDXhMYFnSfQmjiy, kcIxGCXrUvsLPSfmGoULGFzAthVmTXcA=kcIxGCXrUvsLPSfmGoULGFzAthVmTXcA, FEAAZHeTRQEJCsYHCOEPpfOenpVZIhNT=FEAAZHeTRQEJCsYHCOEPpfOenpVZIhNT[TXGwYXNLgQsYzfHHpRBDJGFCFZEClzIo],
                                   ylReNVtjXdQbeAwJXhTkOjiHrFPToKDa=ylReNVtjXdQbeAwJXhTkOjiHrFPToKDa, vcSlHLxBcVodHmZrzACHLEJuENMXjWTG=TkHgGRFhDYRqyKuFvQRlKbpOBXUaEDVU, DDRQlhrNSGpwTrokWitkZipdfbAqBFxv=DDRQlhrNSGpwTrokWitkZipdfbAqBFxv, fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc=fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc, xwIQGNbJnSVpLrBBfhMLBchFpoolNzOe=xwIQGNbJnSVpLrBBfhMLBchFpoolNzOe)
                for TXGwYXNLgQsYzfHHpRBDJGFCFZEClzIo in range(JtnlCSDzHOgtbZVTfQMidKPjmOFZfzZX)]
        )
        if not use_linear:
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.proj_out = xwIQGNbJnSVpLrBBfhMLBchFpoolNzOe.LcFcvNeYCKrBHlNkoWrkqdbxdkNCJBBK(mnMnCdMaVdGNkPTuQLMKyEjwOMhAgIMR,EbKSIFxpyCpzycRDApduouVsxspHzkTj,
                                                  aBEJjpEOpoRJYkulwSmukddEYErxRnAG=1,
                                                  NTEWXstfzqNXGESmGkQNFWBaQsGAPlGd=1,
                                                  sdxdTSjnkAOjlGmltQHvLiHRDstMzpAP=0, DDRQlhrNSGpwTrokWitkZipdfbAqBFxv=DDRQlhrNSGpwTrokWitkZipdfbAqBFxv, fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc=fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc)
        else:
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.proj_out = xwIQGNbJnSVpLrBBfhMLBchFpoolNzOe.DhMcMyEvvzmWIEJojbQeGHlzfZKiPzHO(EbKSIFxpyCpzycRDApduouVsxspHzkTj, mnMnCdMaVdGNkPTuQLMKyEjwOMhAgIMR, DDRQlhrNSGpwTrokWitkZipdfbAqBFxv=DDRQlhrNSGpwTrokWitkZipdfbAqBFxv, fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc=fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.use_linear = use_linear
    def lqBgIcSWZYylbCPjXksJWDguuSOqoPCJ(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, NECAaWUrFGIXcLimrerEYmxYIykQBfXb, tRdCjhUPYVVxnSEkGmJIHWRitDXRXSZS=None, transformer_options={}):
        if not isinstance(tRdCjhUPYVVxnSEkGmJIHWRitDXRXSZS, list):
            tRdCjhUPYVVxnSEkGmJIHWRitDXRXSZS = [tRdCjhUPYVVxnSEkGmJIHWRitDXRXSZS] * len(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.transformer_blocks)
        b, cjHIelcAqVoHWdLcgzuZiBumKNTVADsY, xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab, AeIrbRXDkpZlClJGwzMknCltTQQdmhvu = NECAaWUrFGIXcLimrerEYmxYIykQBfXb.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg
        pZoNxoVtAYgcFKlLqYosAEKjqMzwRmNs = NECAaWUrFGIXcLimrerEYmxYIykQBfXb
        NECAaWUrFGIXcLimrerEYmxYIykQBfXb = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.norm(NECAaWUrFGIXcLimrerEYmxYIykQBfXb)
        if not rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.use_linear:
            NECAaWUrFGIXcLimrerEYmxYIykQBfXb = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.proj_in(NECAaWUrFGIXcLimrerEYmxYIykQBfXb)
        NECAaWUrFGIXcLimrerEYmxYIykQBfXb = rearrange(NECAaWUrFGIXcLimrerEYmxYIykQBfXb, 'b c h w -> b (h w) c').contiguous()
        if rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.use_linear:
            NECAaWUrFGIXcLimrerEYmxYIykQBfXb = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.proj_in(NECAaWUrFGIXcLimrerEYmxYIykQBfXb)
        for HCXmerBqIMuTscBONzTGKYapYSxWTYHo, lPmJfojDSUTFirrgKPryiJRYyZOFajzZ in enumerate(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.transformer_blocks):
            transformer_options["block_index"] = HCXmerBqIMuTscBONzTGKYapYSxWTYHo
            NECAaWUrFGIXcLimrerEYmxYIykQBfXb = lPmJfojDSUTFirrgKPryiJRYyZOFajzZ(NECAaWUrFGIXcLimrerEYmxYIykQBfXb, tRdCjhUPYVVxnSEkGmJIHWRitDXRXSZS=tRdCjhUPYVVxnSEkGmJIHWRitDXRXSZS[HCXmerBqIMuTscBONzTGKYapYSxWTYHo], transformer_options=transformer_options)
        if rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.use_linear:
            NECAaWUrFGIXcLimrerEYmxYIykQBfXb = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.proj_out(NECAaWUrFGIXcLimrerEYmxYIykQBfXb)
        NECAaWUrFGIXcLimrerEYmxYIykQBfXb = rearrange(NECAaWUrFGIXcLimrerEYmxYIykQBfXb, 'b (h w) c -> b c h w', xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab=xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab, AeIrbRXDkpZlClJGwzMknCltTQQdmhvu=AeIrbRXDkpZlClJGwzMknCltTQQdmhvu).contiguous()
        if not rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.use_linear:
            NECAaWUrFGIXcLimrerEYmxYIykQBfXb = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.proj_out(NECAaWUrFGIXcLimrerEYmxYIykQBfXb)
        return NECAaWUrFGIXcLimrerEYmxYIykQBfXb + pZoNxoVtAYgcFKlLqYosAEKjqMzwRmNs
