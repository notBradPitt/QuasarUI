import math
import torch
import torch.nn as nn
import numpy as np
from einops import rearrange
from typing import Optional, Any
from ..attention import jfuIbfkFdWANZYpHZjuHkfnjaHCwdire
from quasar import model_management
import quasar.ops
if model_management.tifElOLkamgDCGAybMmNngkxKANHIbzS():
    import xformers
    import xformers.ops
def FBGIyMBfRymrmsEWcEPIkRwuaTeBVITr(iaqNqpReXPEdYpNiyUIejEPLCqtbtedA, embedding_dim):
    assert len(iaqNqpReXPEdYpNiyUIejEPLCqtbtedA.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg) == 1
    kUDyPzYUnjCMRilJYWZZFlqgXgunyVDA = embedding_dim // 2
    cbvuxLJlTEiYpJEoytPnUgMhAcRHRwIE = math.DJwhOGBaLcOjmXnuwXMXOyhMtknqkKXL(10000) / (kUDyPzYUnjCMRilJYWZZFlqgXgunyVDA - 1)
    cbvuxLJlTEiYpJEoytPnUgMhAcRHRwIE = torch.exp(torch.arange(kUDyPzYUnjCMRilJYWZZFlqgXgunyVDA, DDRQlhrNSGpwTrokWitkZipdfbAqBFxv=torch.float32) * -cbvuxLJlTEiYpJEoytPnUgMhAcRHRwIE)
    cbvuxLJlTEiYpJEoytPnUgMhAcRHRwIE = cbvuxLJlTEiYpJEoytPnUgMhAcRHRwIE.sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ(fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc=iaqNqpReXPEdYpNiyUIejEPLCqtbtedA.fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc)
    cbvuxLJlTEiYpJEoytPnUgMhAcRHRwIE = iaqNqpReXPEdYpNiyUIejEPLCqtbtedA.float()[:, None] * cbvuxLJlTEiYpJEoytPnUgMhAcRHRwIE[None, :]
    cbvuxLJlTEiYpJEoytPnUgMhAcRHRwIE = torch.cat([torch.sin(cbvuxLJlTEiYpJEoytPnUgMhAcRHRwIE), torch.cos(cbvuxLJlTEiYpJEoytPnUgMhAcRHRwIE)], yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk=1)
    if embedding_dim % 2 == 1:  
        cbvuxLJlTEiYpJEoytPnUgMhAcRHRwIE = torch.nn.functional.rdKUTGbMBZTNIXamcnkpRlWsmbXvStaN(cbvuxLJlTEiYpJEoytPnUgMhAcRHRwIE, (0,1,0,0))
    return cbvuxLJlTEiYpJEoytPnUgMhAcRHRwIE
def liYZHxYGwkXhuYdMFrAtaIVIwKaEIKPp(NECAaWUrFGIXcLimrerEYmxYIykQBfXb):
    return NECAaWUrFGIXcLimrerEYmxYIykQBfXb*torch.sigmoid(NECAaWUrFGIXcLimrerEYmxYIykQBfXb)
def HSnGePyLrgZhiiSoMOwJmgVPBjIpItDD(EbKSIFxpyCpzycRDApduouVsxspHzkTj, num_groups=32):
    return torch.nn.GroupNorm(num_groups=num_groups, num_channels=EbKSIFxpyCpzycRDApduouVsxspHzkTj, VVqkfbMIOFDgzhOKKnJVcuOffzzrOGPv=1e-6, affine=True)
class kjruhryvXAQxnjJDeOXqTJbBrTkRFQSk(nn.Module):
    def __init__(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, EbKSIFxpyCpzycRDApduouVsxspHzkTj, with_conv):
        super().__init__()
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.with_conv = with_conv
        if rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.with_conv:
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.VRzIOXLfdDszfSOpzuKgtjeGGtXuyctm = quasar.ops.LcFcvNeYCKrBHlNkoWrkqdbxdkNCJBBK(EbKSIFxpyCpzycRDApduouVsxspHzkTj,
                                        EbKSIFxpyCpzycRDApduouVsxspHzkTj,
                                        aBEJjpEOpoRJYkulwSmukddEYErxRnAG=3,
                                        NTEWXstfzqNXGESmGkQNFWBaQsGAPlGd=1,
                                        sdxdTSjnkAOjlGmltQHvLiHRDstMzpAP=1)
    def lqBgIcSWZYylbCPjXksJWDguuSOqoPCJ(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, NECAaWUrFGIXcLimrerEYmxYIykQBfXb):
        try:
            NECAaWUrFGIXcLimrerEYmxYIykQBfXb = torch.nn.functional.interpolate(NECAaWUrFGIXcLimrerEYmxYIykQBfXb, scale_factor=2.0, bPTwwoDdWiuYqhtrDEHoDbHGiYcwcsQC="nearest")
        except: 
            b, cjHIelcAqVoHWdLcgzuZiBumKNTVADsY, xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab, AeIrbRXDkpZlClJGwzMknCltTQQdmhvu = NECAaWUrFGIXcLimrerEYmxYIykQBfXb.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg
            iqymPVpxyjOWChGwBkTemSzHJbnJdAIz = torch.empty((b, cjHIelcAqVoHWdLcgzuZiBumKNTVADsY, xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab*2, AeIrbRXDkpZlClJGwzMknCltTQQdmhvu*2), DDRQlhrNSGpwTrokWitkZipdfbAqBFxv=NECAaWUrFGIXcLimrerEYmxYIykQBfXb.DDRQlhrNSGpwTrokWitkZipdfbAqBFxv, layout=NECAaWUrFGIXcLimrerEYmxYIykQBfXb.layout, fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc=NECAaWUrFGIXcLimrerEYmxYIykQBfXb.fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc)
            split = 8
            QBYRnCrsHIHjuDAPBxgVhibLQMjOwjJW = iqymPVpxyjOWChGwBkTemSzHJbnJdAIz.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[1] // split
            for HCXmerBqIMuTscBONzTGKYapYSxWTYHo in range(0, iqymPVpxyjOWChGwBkTemSzHJbnJdAIz.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[1], QBYRnCrsHIHjuDAPBxgVhibLQMjOwjJW):
                iqymPVpxyjOWChGwBkTemSzHJbnJdAIz[:,HCXmerBqIMuTscBONzTGKYapYSxWTYHo:HCXmerBqIMuTscBONzTGKYapYSxWTYHo+QBYRnCrsHIHjuDAPBxgVhibLQMjOwjJW] = torch.nn.functional.interpolate(NECAaWUrFGIXcLimrerEYmxYIykQBfXb[:,HCXmerBqIMuTscBONzTGKYapYSxWTYHo:HCXmerBqIMuTscBONzTGKYapYSxWTYHo+QBYRnCrsHIHjuDAPBxgVhibLQMjOwjJW].sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ(torch.float32), scale_factor=2.0, bPTwwoDdWiuYqhtrDEHoDbHGiYcwcsQC="nearest").sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ(NECAaWUrFGIXcLimrerEYmxYIykQBfXb.DDRQlhrNSGpwTrokWitkZipdfbAqBFxv)
            del NECAaWUrFGIXcLimrerEYmxYIykQBfXb
            NECAaWUrFGIXcLimrerEYmxYIykQBfXb = iqymPVpxyjOWChGwBkTemSzHJbnJdAIz
        if rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.with_conv:
            NECAaWUrFGIXcLimrerEYmxYIykQBfXb = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.VRzIOXLfdDszfSOpzuKgtjeGGtXuyctm(NECAaWUrFGIXcLimrerEYmxYIykQBfXb)
        return NECAaWUrFGIXcLimrerEYmxYIykQBfXb
class LpwKTfRyOAITGEdvwhtCdMnNRMEQUkUG(nn.Module):
    def __init__(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, EbKSIFxpyCpzycRDApduouVsxspHzkTj, with_conv):
        super().__init__()
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.with_conv = with_conv
        if rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.with_conv:
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.VRzIOXLfdDszfSOpzuKgtjeGGtXuyctm = quasar.ops.LcFcvNeYCKrBHlNkoWrkqdbxdkNCJBBK(EbKSIFxpyCpzycRDApduouVsxspHzkTj,
                                        EbKSIFxpyCpzycRDApduouVsxspHzkTj,
                                        aBEJjpEOpoRJYkulwSmukddEYErxRnAG=3,
                                        NTEWXstfzqNXGESmGkQNFWBaQsGAPlGd=2,
                                        sdxdTSjnkAOjlGmltQHvLiHRDstMzpAP=0)
    def lqBgIcSWZYylbCPjXksJWDguuSOqoPCJ(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, NECAaWUrFGIXcLimrerEYmxYIykQBfXb):
        if rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.with_conv:
            rdKUTGbMBZTNIXamcnkpRlWsmbXvStaN = (0,1,0,1)
            NECAaWUrFGIXcLimrerEYmxYIykQBfXb = torch.nn.functional.rdKUTGbMBZTNIXamcnkpRlWsmbXvStaN(NECAaWUrFGIXcLimrerEYmxYIykQBfXb, rdKUTGbMBZTNIXamcnkpRlWsmbXvStaN, bPTwwoDdWiuYqhtrDEHoDbHGiYcwcsQC="constant", GXNVXDlnsSLzkmussBPoJXgJwuXIiwsc=0)
            NECAaWUrFGIXcLimrerEYmxYIykQBfXb = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.VRzIOXLfdDszfSOpzuKgtjeGGtXuyctm(NECAaWUrFGIXcLimrerEYmxYIykQBfXb)
        else:
            NECAaWUrFGIXcLimrerEYmxYIykQBfXb = torch.nn.functional.avg_pool2d(NECAaWUrFGIXcLimrerEYmxYIykQBfXb, aBEJjpEOpoRJYkulwSmukddEYErxRnAG=2, NTEWXstfzqNXGESmGkQNFWBaQsGAPlGd=2)
        return NECAaWUrFGIXcLimrerEYmxYIykQBfXb
class ompzonOkvRsHNKHceWNmvSNXZeCTwgaf(nn.Module):
    def __init__(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, *, EbKSIFxpyCpzycRDApduouVsxspHzkTj, DjnmEmFIylXDvTfeYtLbwRKPMHUXFjho=None, conv_shortcut=False,
                 kcIxGCXrUvsLPSfmGoULGFzAthVmTXcA, hMSVpTuyPHmoxFcPWurjMXzUcTNEpKNm=512):
        super().__init__()
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.EbKSIFxpyCpzycRDApduouVsxspHzkTj = EbKSIFxpyCpzycRDApduouVsxspHzkTj
        DjnmEmFIylXDvTfeYtLbwRKPMHUXFjho = EbKSIFxpyCpzycRDApduouVsxspHzkTj if DjnmEmFIylXDvTfeYtLbwRKPMHUXFjho is None else DjnmEmFIylXDvTfeYtLbwRKPMHUXFjho
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.DjnmEmFIylXDvTfeYtLbwRKPMHUXFjho = DjnmEmFIylXDvTfeYtLbwRKPMHUXFjho
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.use_conv_shortcut = conv_shortcut
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.swish = torch.nn.XHAfRvdQzGhVBUIWzxCQjrhAiQInnRoY(inplace=True)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.norm1 = HSnGePyLrgZhiiSoMOwJmgVPBjIpItDD(EbKSIFxpyCpzycRDApduouVsxspHzkTj)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.conv1 = quasar.ops.LcFcvNeYCKrBHlNkoWrkqdbxdkNCJBBK(EbKSIFxpyCpzycRDApduouVsxspHzkTj,
                                     DjnmEmFIylXDvTfeYtLbwRKPMHUXFjho,
                                     aBEJjpEOpoRJYkulwSmukddEYErxRnAG=3,
                                     NTEWXstfzqNXGESmGkQNFWBaQsGAPlGd=1,
                                     sdxdTSjnkAOjlGmltQHvLiHRDstMzpAP=1)
        if hMSVpTuyPHmoxFcPWurjMXzUcTNEpKNm > 0:
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.temb_proj = quasar.ops.DhMcMyEvvzmWIEJojbQeGHlzfZKiPzHO(hMSVpTuyPHmoxFcPWurjMXzUcTNEpKNm,
                                             DjnmEmFIylXDvTfeYtLbwRKPMHUXFjho)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.norm2 = HSnGePyLrgZhiiSoMOwJmgVPBjIpItDD(DjnmEmFIylXDvTfeYtLbwRKPMHUXFjho)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.kcIxGCXrUvsLPSfmGoULGFzAthVmTXcA = torch.nn.Dropout(kcIxGCXrUvsLPSfmGoULGFzAthVmTXcA, inplace=True)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.conv2 = quasar.ops.LcFcvNeYCKrBHlNkoWrkqdbxdkNCJBBK(DjnmEmFIylXDvTfeYtLbwRKPMHUXFjho,
                                     DjnmEmFIylXDvTfeYtLbwRKPMHUXFjho,
                                     aBEJjpEOpoRJYkulwSmukddEYErxRnAG=3,
                                     NTEWXstfzqNXGESmGkQNFWBaQsGAPlGd=1,
                                     sdxdTSjnkAOjlGmltQHvLiHRDstMzpAP=1)
        if rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.EbKSIFxpyCpzycRDApduouVsxspHzkTj != rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.DjnmEmFIylXDvTfeYtLbwRKPMHUXFjho:
            if rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.use_conv_shortcut:
                rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.conv_shortcut = quasar.ops.LcFcvNeYCKrBHlNkoWrkqdbxdkNCJBBK(EbKSIFxpyCpzycRDApduouVsxspHzkTj,
                                                     DjnmEmFIylXDvTfeYtLbwRKPMHUXFjho,
                                                     aBEJjpEOpoRJYkulwSmukddEYErxRnAG=3,
                                                     NTEWXstfzqNXGESmGkQNFWBaQsGAPlGd=1,
                                                     sdxdTSjnkAOjlGmltQHvLiHRDstMzpAP=1)
            else:
                rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.nin_shortcut = quasar.ops.LcFcvNeYCKrBHlNkoWrkqdbxdkNCJBBK(EbKSIFxpyCpzycRDApduouVsxspHzkTj,
                                                    DjnmEmFIylXDvTfeYtLbwRKPMHUXFjho,
                                                    aBEJjpEOpoRJYkulwSmukddEYErxRnAG=1,
                                                    NTEWXstfzqNXGESmGkQNFWBaQsGAPlGd=1,
                                                    sdxdTSjnkAOjlGmltQHvLiHRDstMzpAP=0)
    def lqBgIcSWZYylbCPjXksJWDguuSOqoPCJ(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, NECAaWUrFGIXcLimrerEYmxYIykQBfXb, sXAWsqVPxctAEwLmvNZmqxpDglMjciIT):
        xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab = NECAaWUrFGIXcLimrerEYmxYIykQBfXb
        xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.norm1(xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab)
        xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.swish(xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab)
        xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.conv1(xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab)
        if sXAWsqVPxctAEwLmvNZmqxpDglMjciIT is not None:
            xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab = xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab + rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.temb_proj(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.swish(sXAWsqVPxctAEwLmvNZmqxpDglMjciIT))[:,:,None,None]
        xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.norm2(xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab)
        xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.swish(xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab)
        xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.kcIxGCXrUvsLPSfmGoULGFzAthVmTXcA(xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab)
        xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.conv2(xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab)
        if rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.EbKSIFxpyCpzycRDApduouVsxspHzkTj != rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.DjnmEmFIylXDvTfeYtLbwRKPMHUXFjho:
            if rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.use_conv_shortcut:
                NECAaWUrFGIXcLimrerEYmxYIykQBfXb = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.conv_shortcut(NECAaWUrFGIXcLimrerEYmxYIykQBfXb)
            else:
                NECAaWUrFGIXcLimrerEYmxYIykQBfXb = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.nin_shortcut(NECAaWUrFGIXcLimrerEYmxYIykQBfXb)
        return NECAaWUrFGIXcLimrerEYmxYIykQBfXb+xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab
def NocniVfiTbOkToiCFFQzSIFScSqfKTeX(mxaMgfLZUDPObiqkdCgHnnARjBNVGQnh, EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm, powGafreWfwlSAqPpTpUhFgpFVqCPavl):
    apACmNWgYmlQTXHPQlhMzlFpreaoNbwW = torch.zeros_like(EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm, fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc=mxaMgfLZUDPObiqkdCgHnnARjBNVGQnh.fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc)
    xmbXivThLFnawFPAJvIDBztziWsaDyEE = (int(mxaMgfLZUDPObiqkdCgHnnARjBNVGQnh.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[-1])**(-0.5))
    GPfGQFkmkbPdFypYtapiuNmsHHdeiLUL = model_management.pEiuPTHzmozHhNpBwWGAaONYuNGSpuqI(mxaMgfLZUDPObiqkdCgHnnARjBNVGQnh.fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc)
    phzLQGCUmzLbVFGkMTvzdkdzRosviliv = 1024 ** 3
    zFHMWWyGvdkMWuoMhXMvojVdQBgrBFJN = mxaMgfLZUDPObiqkdCgHnnARjBNVGQnh.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[0] * mxaMgfLZUDPObiqkdCgHnnARjBNVGQnh.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[1] * EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[2] * mxaMgfLZUDPObiqkdCgHnnARjBNVGQnh.element_size()
    uagghsEwpSSqmsjyWKQSfwSRZBLmwawS = 3 if mxaMgfLZUDPObiqkdCgHnnARjBNVGQnh.element_size() == 2 else 2.5
    tTsKDmbmbyaWMYgSLHQnRfOIRMuZWWXp = zFHMWWyGvdkMWuoMhXMvojVdQBgrBFJN * uagghsEwpSSqmsjyWKQSfwSRZBLmwawS
    TMepbhrhtxHODfHDPkWDjgPPPikciJwm = 1
    if tTsKDmbmbyaWMYgSLHQnRfOIRMuZWWXp > GPfGQFkmkbPdFypYtapiuNmsHHdeiLUL:
        TMepbhrhtxHODfHDPkWDjgPPPikciJwm = 2**(math.ceil(math.DJwhOGBaLcOjmXnuwXMXOyhMtknqkKXL(tTsKDmbmbyaWMYgSLHQnRfOIRMuZWWXp / GPfGQFkmkbPdFypYtapiuNmsHHdeiLUL, 2)))
    while True:
        try:
            foSXFEftRhafROZSdfioWvUHDRtUeRyD = mxaMgfLZUDPObiqkdCgHnnARjBNVGQnh.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[1] // TMepbhrhtxHODfHDPkWDjgPPPikciJwm if (mxaMgfLZUDPObiqkdCgHnnARjBNVGQnh.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[1] % TMepbhrhtxHODfHDPkWDjgPPPikciJwm) == 0 else mxaMgfLZUDPObiqkdCgHnnARjBNVGQnh.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[1]
            for HCXmerBqIMuTscBONzTGKYapYSxWTYHo in range(0, mxaMgfLZUDPObiqkdCgHnnARjBNVGQnh.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[1], foSXFEftRhafROZSdfioWvUHDRtUeRyD):
                lGLYgANCchGMWZfAOSVuiBulTGaEVaQM = HCXmerBqIMuTscBONzTGKYapYSxWTYHo + foSXFEftRhafROZSdfioWvUHDRtUeRyD
                XauksjEFAUvtInEaALXIwUhurkUuooOF = torch.bmm(mxaMgfLZUDPObiqkdCgHnnARjBNVGQnh[:, HCXmerBqIMuTscBONzTGKYapYSxWTYHo:lGLYgANCchGMWZfAOSVuiBulTGaEVaQM], EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm) * xmbXivThLFnawFPAJvIDBztziWsaDyEE
                orjPyVtdqCXZbZZCrekqzXxPBGSWSqJa = torch.nn.functional.softmax(XauksjEFAUvtInEaALXIwUhurkUuooOF, yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk=2).permute(0,2,1)
                del XauksjEFAUvtInEaALXIwUhurkUuooOF
                apACmNWgYmlQTXHPQlhMzlFpreaoNbwW[:, :, HCXmerBqIMuTscBONzTGKYapYSxWTYHo:lGLYgANCchGMWZfAOSVuiBulTGaEVaQM] = torch.bmm(powGafreWfwlSAqPpTpUhFgpFVqCPavl, orjPyVtdqCXZbZZCrekqzXxPBGSWSqJa)
                del orjPyVtdqCXZbZZCrekqzXxPBGSWSqJa
            break
        except model_management.uiFxRFoacIkrFnuAQlLvqBYROTajCRaW as dgvKdkEDrMSdkCaRxfkDNVbaXWUetgtO:
            model_management.sIeWDNiYvNWPLHobyjQHaTvlWZnazsHi(True)
            TMepbhrhtxHODfHDPkWDjgPPPikciJwm *= 2
            if TMepbhrhtxHODfHDPkWDjgPPPikciJwm > 128:
                raise dgvKdkEDrMSdkCaRxfkDNVbaXWUetgtO
            print("out of memory error, increasing steps and trying again", TMepbhrhtxHODfHDPkWDjgPPPikciJwm)
    return apACmNWgYmlQTXHPQlhMzlFpreaoNbwW
class eHXBSfnHAaGpWFgNmODAIYNswTKSTBje(nn.Module):
    def __init__(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, EbKSIFxpyCpzycRDApduouVsxspHzkTj):
        super().__init__()
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.EbKSIFxpyCpzycRDApduouVsxspHzkTj = EbKSIFxpyCpzycRDApduouVsxspHzkTj
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.norm = HSnGePyLrgZhiiSoMOwJmgVPBjIpItDD(EbKSIFxpyCpzycRDApduouVsxspHzkTj)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.mxaMgfLZUDPObiqkdCgHnnARjBNVGQnh = quasar.ops.LcFcvNeYCKrBHlNkoWrkqdbxdkNCJBBK(EbKSIFxpyCpzycRDApduouVsxspHzkTj,
                                 EbKSIFxpyCpzycRDApduouVsxspHzkTj,
                                 aBEJjpEOpoRJYkulwSmukddEYErxRnAG=1,
                                 NTEWXstfzqNXGESmGkQNFWBaQsGAPlGd=1,
                                 sdxdTSjnkAOjlGmltQHvLiHRDstMzpAP=0)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm = quasar.ops.LcFcvNeYCKrBHlNkoWrkqdbxdkNCJBBK(EbKSIFxpyCpzycRDApduouVsxspHzkTj,
                                 EbKSIFxpyCpzycRDApduouVsxspHzkTj,
                                 aBEJjpEOpoRJYkulwSmukddEYErxRnAG=1,
                                 NTEWXstfzqNXGESmGkQNFWBaQsGAPlGd=1,
                                 sdxdTSjnkAOjlGmltQHvLiHRDstMzpAP=0)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.powGafreWfwlSAqPpTpUhFgpFVqCPavl = quasar.ops.LcFcvNeYCKrBHlNkoWrkqdbxdkNCJBBK(EbKSIFxpyCpzycRDApduouVsxspHzkTj,
                                 EbKSIFxpyCpzycRDApduouVsxspHzkTj,
                                 aBEJjpEOpoRJYkulwSmukddEYErxRnAG=1,
                                 NTEWXstfzqNXGESmGkQNFWBaQsGAPlGd=1,
                                 sdxdTSjnkAOjlGmltQHvLiHRDstMzpAP=0)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.proj_out = quasar.ops.LcFcvNeYCKrBHlNkoWrkqdbxdkNCJBBK(EbKSIFxpyCpzycRDApduouVsxspHzkTj,
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
        mxaMgfLZUDPObiqkdCgHnnARjBNVGQnh = mxaMgfLZUDPObiqkdCgHnnARjBNVGQnh.reshape(b,cjHIelcAqVoHWdLcgzuZiBumKNTVADsY,xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab*AeIrbRXDkpZlClJGwzMknCltTQQdmhvu)
        mxaMgfLZUDPObiqkdCgHnnARjBNVGQnh = mxaMgfLZUDPObiqkdCgHnnARjBNVGQnh.permute(0,2,1)   
        EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm = EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm.reshape(b,cjHIelcAqVoHWdLcgzuZiBumKNTVADsY,xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab*AeIrbRXDkpZlClJGwzMknCltTQQdmhvu) 
        powGafreWfwlSAqPpTpUhFgpFVqCPavl = powGafreWfwlSAqPpTpUhFgpFVqCPavl.reshape(b,cjHIelcAqVoHWdLcgzuZiBumKNTVADsY,xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab*AeIrbRXDkpZlClJGwzMknCltTQQdmhvu)
        apACmNWgYmlQTXHPQlhMzlFpreaoNbwW = NocniVfiTbOkToiCFFQzSIFScSqfKTeX(mxaMgfLZUDPObiqkdCgHnnARjBNVGQnh, EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm, powGafreWfwlSAqPpTpUhFgpFVqCPavl)
        vCjLIHrnXRniEvZiWnGuQBAcFdDANZRw = apACmNWgYmlQTXHPQlhMzlFpreaoNbwW.reshape(b,cjHIelcAqVoHWdLcgzuZiBumKNTVADsY,xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab,AeIrbRXDkpZlClJGwzMknCltTQQdmhvu)
        del apACmNWgYmlQTXHPQlhMzlFpreaoNbwW
        vCjLIHrnXRniEvZiWnGuQBAcFdDANZRw = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.proj_out(vCjLIHrnXRniEvZiWnGuQBAcFdDANZRw)
        return NECAaWUrFGIXcLimrerEYmxYIykQBfXb+vCjLIHrnXRniEvZiWnGuQBAcFdDANZRw
class ldnyNYWgddBWpHIfAwydTddRkkFRiqhj(nn.Module):
    def __init__(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, EbKSIFxpyCpzycRDApduouVsxspHzkTj):
        super().__init__()
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.EbKSIFxpyCpzycRDApduouVsxspHzkTj = EbKSIFxpyCpzycRDApduouVsxspHzkTj
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.norm = HSnGePyLrgZhiiSoMOwJmgVPBjIpItDD(EbKSIFxpyCpzycRDApduouVsxspHzkTj)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.mxaMgfLZUDPObiqkdCgHnnARjBNVGQnh = quasar.ops.LcFcvNeYCKrBHlNkoWrkqdbxdkNCJBBK(EbKSIFxpyCpzycRDApduouVsxspHzkTj,
                                 EbKSIFxpyCpzycRDApduouVsxspHzkTj,
                                 aBEJjpEOpoRJYkulwSmukddEYErxRnAG=1,
                                 NTEWXstfzqNXGESmGkQNFWBaQsGAPlGd=1,
                                 sdxdTSjnkAOjlGmltQHvLiHRDstMzpAP=0)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm = quasar.ops.LcFcvNeYCKrBHlNkoWrkqdbxdkNCJBBK(EbKSIFxpyCpzycRDApduouVsxspHzkTj,
                                 EbKSIFxpyCpzycRDApduouVsxspHzkTj,
                                 aBEJjpEOpoRJYkulwSmukddEYErxRnAG=1,
                                 NTEWXstfzqNXGESmGkQNFWBaQsGAPlGd=1,
                                 sdxdTSjnkAOjlGmltQHvLiHRDstMzpAP=0)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.powGafreWfwlSAqPpTpUhFgpFVqCPavl = quasar.ops.LcFcvNeYCKrBHlNkoWrkqdbxdkNCJBBK(EbKSIFxpyCpzycRDApduouVsxspHzkTj,
                                 EbKSIFxpyCpzycRDApduouVsxspHzkTj,
                                 aBEJjpEOpoRJYkulwSmukddEYErxRnAG=1,
                                 NTEWXstfzqNXGESmGkQNFWBaQsGAPlGd=1,
                                 sdxdTSjnkAOjlGmltQHvLiHRDstMzpAP=0)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.proj_out = quasar.ops.LcFcvNeYCKrBHlNkoWrkqdbxdkNCJBBK(EbKSIFxpyCpzycRDApduouVsxspHzkTj,
                                        EbKSIFxpyCpzycRDApduouVsxspHzkTj,
                                        aBEJjpEOpoRJYkulwSmukddEYErxRnAG=1,
                                        NTEWXstfzqNXGESmGkQNFWBaQsGAPlGd=1,
                                        sdxdTSjnkAOjlGmltQHvLiHRDstMzpAP=0)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.attention_op: Optional[Any] = None
    def lqBgIcSWZYylbCPjXksJWDguuSOqoPCJ(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, NECAaWUrFGIXcLimrerEYmxYIykQBfXb):
        vCjLIHrnXRniEvZiWnGuQBAcFdDANZRw = NECAaWUrFGIXcLimrerEYmxYIykQBfXb
        vCjLIHrnXRniEvZiWnGuQBAcFdDANZRw = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.norm(vCjLIHrnXRniEvZiWnGuQBAcFdDANZRw)
        mxaMgfLZUDPObiqkdCgHnnARjBNVGQnh = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.mxaMgfLZUDPObiqkdCgHnnARjBNVGQnh(vCjLIHrnXRniEvZiWnGuQBAcFdDANZRw)
        EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm(vCjLIHrnXRniEvZiWnGuQBAcFdDANZRw)
        powGafreWfwlSAqPpTpUhFgpFVqCPavl = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.powGafreWfwlSAqPpTpUhFgpFVqCPavl(vCjLIHrnXRniEvZiWnGuQBAcFdDANZRw)
        oKoLNmqMHsUubaMUUnyDFEgClwoExDJu, AHoGYMpsqEtOaZpAamJqoHqHvnlwZSRh, gFdyNTfDqQDeXijWZEnTSFKJXHMWaEiV, vFYBIMOEtqWwjvpBeeDFaIqTrgSbzULJ = mxaMgfLZUDPObiqkdCgHnnARjBNVGQnh.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg
        mxaMgfLZUDPObiqkdCgHnnARjBNVGQnh, EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm, powGafreWfwlSAqPpTpUhFgpFVqCPavl = map(
            lambda XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz: XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz.view(oKoLNmqMHsUubaMUUnyDFEgClwoExDJu, AHoGYMpsqEtOaZpAamJqoHqHvnlwZSRh, -1).transpose(1, 2).contiguous(),
            (mxaMgfLZUDPObiqkdCgHnnARjBNVGQnh, EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm, powGafreWfwlSAqPpTpUhFgpFVqCPavl),
        )
        try:
            iqymPVpxyjOWChGwBkTemSzHJbnJdAIz = xformers.ops.memory_efficient_attention(mxaMgfLZUDPObiqkdCgHnnARjBNVGQnh, EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm, powGafreWfwlSAqPpTpUhFgpFVqCPavl, attn_bias=None, bjtPzNLsLxvykINbAtlMwKlGJQooJtzI=rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.attention_op)
            iqymPVpxyjOWChGwBkTemSzHJbnJdAIz = iqymPVpxyjOWChGwBkTemSzHJbnJdAIz.transpose(1, 2).reshape(oKoLNmqMHsUubaMUUnyDFEgClwoExDJu, AHoGYMpsqEtOaZpAamJqoHqHvnlwZSRh, gFdyNTfDqQDeXijWZEnTSFKJXHMWaEiV, vFYBIMOEtqWwjvpBeeDFaIqTrgSbzULJ)
        except NotImplementedError as dgvKdkEDrMSdkCaRxfkDNVbaXWUetgtO:
            iqymPVpxyjOWChGwBkTemSzHJbnJdAIz = NocniVfiTbOkToiCFFQzSIFScSqfKTeX(mxaMgfLZUDPObiqkdCgHnnARjBNVGQnh.view(oKoLNmqMHsUubaMUUnyDFEgClwoExDJu, -1, AHoGYMpsqEtOaZpAamJqoHqHvnlwZSRh), EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm.view(oKoLNmqMHsUubaMUUnyDFEgClwoExDJu, -1, AHoGYMpsqEtOaZpAamJqoHqHvnlwZSRh).transpose(1, 2), powGafreWfwlSAqPpTpUhFgpFVqCPavl.view(oKoLNmqMHsUubaMUUnyDFEgClwoExDJu, -1, AHoGYMpsqEtOaZpAamJqoHqHvnlwZSRh).transpose(1, 2)).reshape(oKoLNmqMHsUubaMUUnyDFEgClwoExDJu, AHoGYMpsqEtOaZpAamJqoHqHvnlwZSRh, gFdyNTfDqQDeXijWZEnTSFKJXHMWaEiV, vFYBIMOEtqWwjvpBeeDFaIqTrgSbzULJ)
        iqymPVpxyjOWChGwBkTemSzHJbnJdAIz = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.proj_out(iqymPVpxyjOWChGwBkTemSzHJbnJdAIz)
        return NECAaWUrFGIXcLimrerEYmxYIykQBfXb+iqymPVpxyjOWChGwBkTemSzHJbnJdAIz
class pCvQubQjWEJoxMrxbzCNTANcTYbnMyrc(nn.Module):
    def __init__(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, EbKSIFxpyCpzycRDApduouVsxspHzkTj):
        super().__init__()
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.EbKSIFxpyCpzycRDApduouVsxspHzkTj = EbKSIFxpyCpzycRDApduouVsxspHzkTj
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.norm = HSnGePyLrgZhiiSoMOwJmgVPBjIpItDD(EbKSIFxpyCpzycRDApduouVsxspHzkTj)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.mxaMgfLZUDPObiqkdCgHnnARjBNVGQnh = quasar.ops.LcFcvNeYCKrBHlNkoWrkqdbxdkNCJBBK(EbKSIFxpyCpzycRDApduouVsxspHzkTj,
                                 EbKSIFxpyCpzycRDApduouVsxspHzkTj,
                                 aBEJjpEOpoRJYkulwSmukddEYErxRnAG=1,
                                 NTEWXstfzqNXGESmGkQNFWBaQsGAPlGd=1,
                                 sdxdTSjnkAOjlGmltQHvLiHRDstMzpAP=0)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm = quasar.ops.LcFcvNeYCKrBHlNkoWrkqdbxdkNCJBBK(EbKSIFxpyCpzycRDApduouVsxspHzkTj,
                                 EbKSIFxpyCpzycRDApduouVsxspHzkTj,
                                 aBEJjpEOpoRJYkulwSmukddEYErxRnAG=1,
                                 NTEWXstfzqNXGESmGkQNFWBaQsGAPlGd=1,
                                 sdxdTSjnkAOjlGmltQHvLiHRDstMzpAP=0)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.powGafreWfwlSAqPpTpUhFgpFVqCPavl = quasar.ops.LcFcvNeYCKrBHlNkoWrkqdbxdkNCJBBK(EbKSIFxpyCpzycRDApduouVsxspHzkTj,
                                 EbKSIFxpyCpzycRDApduouVsxspHzkTj,
                                 aBEJjpEOpoRJYkulwSmukddEYErxRnAG=1,
                                 NTEWXstfzqNXGESmGkQNFWBaQsGAPlGd=1,
                                 sdxdTSjnkAOjlGmltQHvLiHRDstMzpAP=0)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.proj_out = quasar.ops.LcFcvNeYCKrBHlNkoWrkqdbxdkNCJBBK(EbKSIFxpyCpzycRDApduouVsxspHzkTj,
                                        EbKSIFxpyCpzycRDApduouVsxspHzkTj,
                                        aBEJjpEOpoRJYkulwSmukddEYErxRnAG=1,
                                        NTEWXstfzqNXGESmGkQNFWBaQsGAPlGd=1,
                                        sdxdTSjnkAOjlGmltQHvLiHRDstMzpAP=0)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.attention_op: Optional[Any] = None
    def lqBgIcSWZYylbCPjXksJWDguuSOqoPCJ(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, NECAaWUrFGIXcLimrerEYmxYIykQBfXb):
        vCjLIHrnXRniEvZiWnGuQBAcFdDANZRw = NECAaWUrFGIXcLimrerEYmxYIykQBfXb
        vCjLIHrnXRniEvZiWnGuQBAcFdDANZRw = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.norm(vCjLIHrnXRniEvZiWnGuQBAcFdDANZRw)
        mxaMgfLZUDPObiqkdCgHnnARjBNVGQnh = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.mxaMgfLZUDPObiqkdCgHnnARjBNVGQnh(vCjLIHrnXRniEvZiWnGuQBAcFdDANZRw)
        EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm(vCjLIHrnXRniEvZiWnGuQBAcFdDANZRw)
        powGafreWfwlSAqPpTpUhFgpFVqCPavl = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.powGafreWfwlSAqPpTpUhFgpFVqCPavl(vCjLIHrnXRniEvZiWnGuQBAcFdDANZRw)
        oKoLNmqMHsUubaMUUnyDFEgClwoExDJu, AHoGYMpsqEtOaZpAamJqoHqHvnlwZSRh, gFdyNTfDqQDeXijWZEnTSFKJXHMWaEiV, vFYBIMOEtqWwjvpBeeDFaIqTrgSbzULJ = mxaMgfLZUDPObiqkdCgHnnARjBNVGQnh.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg
        mxaMgfLZUDPObiqkdCgHnnARjBNVGQnh, EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm, powGafreWfwlSAqPpTpUhFgpFVqCPavl = map(
            lambda XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz: XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz.view(oKoLNmqMHsUubaMUUnyDFEgClwoExDJu, 1, AHoGYMpsqEtOaZpAamJqoHqHvnlwZSRh, -1).transpose(2, 3).contiguous(),
            (mxaMgfLZUDPObiqkdCgHnnARjBNVGQnh, EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm, powGafreWfwlSAqPpTpUhFgpFVqCPavl),
        )
        try:
            iqymPVpxyjOWChGwBkTemSzHJbnJdAIz = torch.nn.functional.scaled_dot_product_attention(mxaMgfLZUDPObiqkdCgHnnARjBNVGQnh, EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm, powGafreWfwlSAqPpTpUhFgpFVqCPavl, attn_mask=None, dropout_p=0.0, is_causal=False)
            iqymPVpxyjOWChGwBkTemSzHJbnJdAIz = iqymPVpxyjOWChGwBkTemSzHJbnJdAIz.transpose(2, 3).reshape(oKoLNmqMHsUubaMUUnyDFEgClwoExDJu, AHoGYMpsqEtOaZpAamJqoHqHvnlwZSRh, gFdyNTfDqQDeXijWZEnTSFKJXHMWaEiV, vFYBIMOEtqWwjvpBeeDFaIqTrgSbzULJ)
        except model_management.uiFxRFoacIkrFnuAQlLvqBYROTajCRaW as dgvKdkEDrMSdkCaRxfkDNVbaXWUetgtO:
            print("scaled_dot_product_attention OOMed: switched to slice attention")
            iqymPVpxyjOWChGwBkTemSzHJbnJdAIz = NocniVfiTbOkToiCFFQzSIFScSqfKTeX(mxaMgfLZUDPObiqkdCgHnnARjBNVGQnh.view(oKoLNmqMHsUubaMUUnyDFEgClwoExDJu, -1, AHoGYMpsqEtOaZpAamJqoHqHvnlwZSRh), EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm.view(oKoLNmqMHsUubaMUUnyDFEgClwoExDJu, -1, AHoGYMpsqEtOaZpAamJqoHqHvnlwZSRh).transpose(1, 2), powGafreWfwlSAqPpTpUhFgpFVqCPavl.view(oKoLNmqMHsUubaMUUnyDFEgClwoExDJu, -1, AHoGYMpsqEtOaZpAamJqoHqHvnlwZSRh).transpose(1, 2)).reshape(oKoLNmqMHsUubaMUUnyDFEgClwoExDJu, AHoGYMpsqEtOaZpAamJqoHqHvnlwZSRh, gFdyNTfDqQDeXijWZEnTSFKJXHMWaEiV, vFYBIMOEtqWwjvpBeeDFaIqTrgSbzULJ)
        iqymPVpxyjOWChGwBkTemSzHJbnJdAIz = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.proj_out(iqymPVpxyjOWChGwBkTemSzHJbnJdAIz)
        return NECAaWUrFGIXcLimrerEYmxYIykQBfXb+iqymPVpxyjOWChGwBkTemSzHJbnJdAIz
class fMrKutSZHikVqhjSzkLcubyqOIslrzfe(jfuIbfkFdWANZYpHZjuHkfnjaHCwdire):
    def lqBgIcSWZYylbCPjXksJWDguuSOqoPCJ(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, NECAaWUrFGIXcLimrerEYmxYIykQBfXb, tRdCjhUPYVVxnSEkGmJIHWRitDXRXSZS=None, KHpRlHOzblljQyskecSxzUuWZtneWwta=None):
        b, cjHIelcAqVoHWdLcgzuZiBumKNTVADsY, xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab, AeIrbRXDkpZlClJGwzMknCltTQQdmhvu = NECAaWUrFGIXcLimrerEYmxYIykQBfXb.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg
        NECAaWUrFGIXcLimrerEYmxYIykQBfXb = rearrange(NECAaWUrFGIXcLimrerEYmxYIykQBfXb, 'b c h w -> b (h w) c')
        iqymPVpxyjOWChGwBkTemSzHJbnJdAIz = super().lqBgIcSWZYylbCPjXksJWDguuSOqoPCJ(NECAaWUrFGIXcLimrerEYmxYIykQBfXb, tRdCjhUPYVVxnSEkGmJIHWRitDXRXSZS=tRdCjhUPYVVxnSEkGmJIHWRitDXRXSZS, KHpRlHOzblljQyskecSxzUuWZtneWwta=KHpRlHOzblljQyskecSxzUuWZtneWwta)
        iqymPVpxyjOWChGwBkTemSzHJbnJdAIz = rearrange(iqymPVpxyjOWChGwBkTemSzHJbnJdAIz, 'b (h w) c -> b c h w', xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab=xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab, AeIrbRXDkpZlClJGwzMknCltTQQdmhvu=AeIrbRXDkpZlClJGwzMknCltTQQdmhvu, cjHIelcAqVoHWdLcgzuZiBumKNTVADsY=cjHIelcAqVoHWdLcgzuZiBumKNTVADsY)
        return NECAaWUrFGIXcLimrerEYmxYIykQBfXb + iqymPVpxyjOWChGwBkTemSzHJbnJdAIz
def qXfIkuZrNfESJcZDYMxfgdGOBPOHmKaF(EbKSIFxpyCpzycRDApduouVsxspHzkTj, FFkRWmQHKPdMiLiCPdiuVVUNvNEEvZkf="vanilla", attn_kwargs=None):
    assert FFkRWmQHKPdMiLiCPdiuVVUNvNEEvZkf in ["vanilla", "vanilla-xformers", "memory-efficient-cross-attn", "linear", "none"], f'attn_type {attn_type} unknown'
    if model_management.tifElOLkamgDCGAybMmNngkxKANHIbzS() and FFkRWmQHKPdMiLiCPdiuVVUNvNEEvZkf == "vanilla":
        FFkRWmQHKPdMiLiCPdiuVVUNvNEEvZkf = "vanilla-xformers"
    if model_management.kQDSfcrSuHTuIBtYUKBNyIxOCqzlxNlm() and FFkRWmQHKPdMiLiCPdiuVVUNvNEEvZkf == "vanilla":
        FFkRWmQHKPdMiLiCPdiuVVUNvNEEvZkf = "vanilla-pytorch"
    print(f"making attention of type '{FFkRWmQHKPdMiLiCPdiuVVUNvNEEvZkf}' with {in_channels} in_channels")
    if FFkRWmQHKPdMiLiCPdiuVVUNvNEEvZkf == "vanilla":
        assert attn_kwargs is None
        return eHXBSfnHAaGpWFgNmODAIYNswTKSTBje(EbKSIFxpyCpzycRDApduouVsxspHzkTj)
    elif FFkRWmQHKPdMiLiCPdiuVVUNvNEEvZkf == "vanilla-xformers":
        print(f"building MemoryEfficientAttnBlock with {in_channels} in_channels...")
        return ldnyNYWgddBWpHIfAwydTddRkkFRiqhj(EbKSIFxpyCpzycRDApduouVsxspHzkTj)
    elif FFkRWmQHKPdMiLiCPdiuVVUNvNEEvZkf == "vanilla-pytorch":
        return pCvQubQjWEJoxMrxbzCNTANcTYbnMyrc(EbKSIFxpyCpzycRDApduouVsxspHzkTj)
    elif type == "memory-efficient-cross-attn":
        attn_kwargs["query_dim"] = EbKSIFxpyCpzycRDApduouVsxspHzkTj
        return fMrKutSZHikVqhjSzkLcubyqOIslrzfe(**attn_kwargs)
    elif FFkRWmQHKPdMiLiCPdiuVVUNvNEEvZkf == "none":
        return nn.Identity(EbKSIFxpyCpzycRDApduouVsxspHzkTj)
    else:
        raise NotImplementedError()
class NOzDEVJVmkXCBbrgeucbWnojtgGvnSHf(nn.Module):
    def __init__(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, *, PCiQtOeHrYsokBqtFxBbpDPnOjZourbJ, VAkEsdMDwAEDPzAuJymQaRUNIxlnDSEu, ch_mult=(1,2,4,8), CCAXgmpIWICHAxdXRCbCjrvfPSDecjrB,
                 SVFgWZmLHyBDIohemjJyxOqQDTKUSaYc, kcIxGCXrUvsLPSfmGoULGFzAthVmTXcA=0.0, resamp_with_conv=True, EbKSIFxpyCpzycRDApduouVsxspHzkTj,
                 BcSwNQTmUGuqaESGKyPNIfMVGtVTPcEr, CJffilbwILRpyJZXwstdSKcmbtdBZCgF=True, use_linear_attn=False, FFkRWmQHKPdMiLiCPdiuVVUNvNEEvZkf="vanilla"):
        super().__init__()
        if use_linear_attn: FFkRWmQHKPdMiLiCPdiuVVUNvNEEvZkf = "linear"
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.PCiQtOeHrYsokBqtFxBbpDPnOjZourbJ = PCiQtOeHrYsokBqtFxBbpDPnOjZourbJ
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.temb_ch = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.PCiQtOeHrYsokBqtFxBbpDPnOjZourbJ*4
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.num_resolutions = len(ch_mult)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.CCAXgmpIWICHAxdXRCbCjrvfPSDecjrB = CCAXgmpIWICHAxdXRCbCjrvfPSDecjrB
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.BcSwNQTmUGuqaESGKyPNIfMVGtVTPcEr = BcSwNQTmUGuqaESGKyPNIfMVGtVTPcEr
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.EbKSIFxpyCpzycRDApduouVsxspHzkTj = EbKSIFxpyCpzycRDApduouVsxspHzkTj
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.CJffilbwILRpyJZXwstdSKcmbtdBZCgF = CJffilbwILRpyJZXwstdSKcmbtdBZCgF
        if rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.CJffilbwILRpyJZXwstdSKcmbtdBZCgF:
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.sXAWsqVPxctAEwLmvNZmqxpDglMjciIT = nn.Module()
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.sXAWsqVPxctAEwLmvNZmqxpDglMjciIT.dense = nn.ModuleList([
                quasar.ops.DhMcMyEvvzmWIEJojbQeGHlzfZKiPzHO(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.PCiQtOeHrYsokBqtFxBbpDPnOjZourbJ,
                                rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.temb_ch),
                quasar.ops.DhMcMyEvvzmWIEJojbQeGHlzfZKiPzHO(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.temb_ch,
                                rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.temb_ch),
            ])
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.conv_in = quasar.ops.LcFcvNeYCKrBHlNkoWrkqdbxdkNCJBBK(EbKSIFxpyCpzycRDApduouVsxspHzkTj,
                                       rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.PCiQtOeHrYsokBqtFxBbpDPnOjZourbJ,
                                       aBEJjpEOpoRJYkulwSmukddEYErxRnAG=3,
                                       NTEWXstfzqNXGESmGkQNFWBaQsGAPlGd=1,
                                       sdxdTSjnkAOjlGmltQHvLiHRDstMzpAP=1)
        WPrMyJZpYZhKJnvzZBeozEExkNgnAmVY = BcSwNQTmUGuqaESGKyPNIfMVGtVTPcEr
        KpITumKUkWAggHnDiNqKSkoTtPMTnyuQ = (1,)+tuple(ch_mult)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.PKmeubCqZPUpSfmqJozYuvYsQsIMTIOn = nn.ModuleList()
        for OpFlKMYGKpWqrQclNkbQJOyQGzPHDYJu in range(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.num_resolutions):
            lPmJfojDSUTFirrgKPryiJRYyZOFajzZ = nn.ModuleList()
            tUmudCfKVwpeKVqJPkVQAwLriIrTDLbW = nn.ModuleList()
            AkBFPvJWpORRGVppZZKLviMdeWBRZNeA = PCiQtOeHrYsokBqtFxBbpDPnOjZourbJ*KpITumKUkWAggHnDiNqKSkoTtPMTnyuQ[OpFlKMYGKpWqrQclNkbQJOyQGzPHDYJu]
            SFZANSjeQRuDmejNulCUPGLUGdwWWwIa = PCiQtOeHrYsokBqtFxBbpDPnOjZourbJ*ch_mult[OpFlKMYGKpWqrQclNkbQJOyQGzPHDYJu]
            for zmRdsMNKEDpECOVrJyNRRisrgWkYZnmp in range(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.CCAXgmpIWICHAxdXRCbCjrvfPSDecjrB):
                lPmJfojDSUTFirrgKPryiJRYyZOFajzZ.append(ompzonOkvRsHNKHceWNmvSNXZeCTwgaf(EbKSIFxpyCpzycRDApduouVsxspHzkTj=AkBFPvJWpORRGVppZZKLviMdeWBRZNeA,
                                         DjnmEmFIylXDvTfeYtLbwRKPMHUXFjho=SFZANSjeQRuDmejNulCUPGLUGdwWWwIa,
                                         hMSVpTuyPHmoxFcPWurjMXzUcTNEpKNm=rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.temb_ch,
                                         kcIxGCXrUvsLPSfmGoULGFzAthVmTXcA=kcIxGCXrUvsLPSfmGoULGFzAthVmTXcA))
                AkBFPvJWpORRGVppZZKLviMdeWBRZNeA = SFZANSjeQRuDmejNulCUPGLUGdwWWwIa
                if WPrMyJZpYZhKJnvzZBeozEExkNgnAmVY in SVFgWZmLHyBDIohemjJyxOqQDTKUSaYc:
                    tUmudCfKVwpeKVqJPkVQAwLriIrTDLbW.append(qXfIkuZrNfESJcZDYMxfgdGOBPOHmKaF(AkBFPvJWpORRGVppZZKLviMdeWBRZNeA, FFkRWmQHKPdMiLiCPdiuVVUNvNEEvZkf=FFkRWmQHKPdMiLiCPdiuVVUNvNEEvZkf))
            PKmeubCqZPUpSfmqJozYuvYsQsIMTIOn = nn.Module()
            PKmeubCqZPUpSfmqJozYuvYsQsIMTIOn.lPmJfojDSUTFirrgKPryiJRYyZOFajzZ = lPmJfojDSUTFirrgKPryiJRYyZOFajzZ
            PKmeubCqZPUpSfmqJozYuvYsQsIMTIOn.tUmudCfKVwpeKVqJPkVQAwLriIrTDLbW = tUmudCfKVwpeKVqJPkVQAwLriIrTDLbW
            if OpFlKMYGKpWqrQclNkbQJOyQGzPHDYJu != rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.num_resolutions-1:
                PKmeubCqZPUpSfmqJozYuvYsQsIMTIOn.FNdFYgmARbySAmYyEvSINcVrOJlCpKfW = LpwKTfRyOAITGEdvwhtCdMnNRMEQUkUG(AkBFPvJWpORRGVppZZKLviMdeWBRZNeA, resamp_with_conv)
                WPrMyJZpYZhKJnvzZBeozEExkNgnAmVY = WPrMyJZpYZhKJnvzZBeozEExkNgnAmVY // 2
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.PKmeubCqZPUpSfmqJozYuvYsQsIMTIOn.append(PKmeubCqZPUpSfmqJozYuvYsQsIMTIOn)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.rnBVwgYeGkHoRDXjLPBaCTIXNAZYBHGr = nn.Module()
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.rnBVwgYeGkHoRDXjLPBaCTIXNAZYBHGr.block_1 = ompzonOkvRsHNKHceWNmvSNXZeCTwgaf(EbKSIFxpyCpzycRDApduouVsxspHzkTj=AkBFPvJWpORRGVppZZKLviMdeWBRZNeA,
                                       DjnmEmFIylXDvTfeYtLbwRKPMHUXFjho=AkBFPvJWpORRGVppZZKLviMdeWBRZNeA,
                                       hMSVpTuyPHmoxFcPWurjMXzUcTNEpKNm=rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.temb_ch,
                                       kcIxGCXrUvsLPSfmGoULGFzAthVmTXcA=kcIxGCXrUvsLPSfmGoULGFzAthVmTXcA)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.rnBVwgYeGkHoRDXjLPBaCTIXNAZYBHGr.attn_1 = qXfIkuZrNfESJcZDYMxfgdGOBPOHmKaF(AkBFPvJWpORRGVppZZKLviMdeWBRZNeA, FFkRWmQHKPdMiLiCPdiuVVUNvNEEvZkf=FFkRWmQHKPdMiLiCPdiuVVUNvNEEvZkf)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.rnBVwgYeGkHoRDXjLPBaCTIXNAZYBHGr.block_2 = ompzonOkvRsHNKHceWNmvSNXZeCTwgaf(EbKSIFxpyCpzycRDApduouVsxspHzkTj=AkBFPvJWpORRGVppZZKLviMdeWBRZNeA,
                                       DjnmEmFIylXDvTfeYtLbwRKPMHUXFjho=AkBFPvJWpORRGVppZZKLviMdeWBRZNeA,
                                       hMSVpTuyPHmoxFcPWurjMXzUcTNEpKNm=rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.temb_ch,
                                       kcIxGCXrUvsLPSfmGoULGFzAthVmTXcA=kcIxGCXrUvsLPSfmGoULGFzAthVmTXcA)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.kvJZslyswPMVzCnLtIoKrkpdfusdzxSS = nn.ModuleList()
        for OpFlKMYGKpWqrQclNkbQJOyQGzPHDYJu in reversed(range(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.num_resolutions)):
            lPmJfojDSUTFirrgKPryiJRYyZOFajzZ = nn.ModuleList()
            tUmudCfKVwpeKVqJPkVQAwLriIrTDLbW = nn.ModuleList()
            SFZANSjeQRuDmejNulCUPGLUGdwWWwIa = PCiQtOeHrYsokBqtFxBbpDPnOjZourbJ*ch_mult[OpFlKMYGKpWqrQclNkbQJOyQGzPHDYJu]
            ywKgRImchIHWvJXlMDzoGWEZwZuXkxOC = PCiQtOeHrYsokBqtFxBbpDPnOjZourbJ*ch_mult[OpFlKMYGKpWqrQclNkbQJOyQGzPHDYJu]
            for zmRdsMNKEDpECOVrJyNRRisrgWkYZnmp in range(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.CCAXgmpIWICHAxdXRCbCjrvfPSDecjrB+1):
                if zmRdsMNKEDpECOVrJyNRRisrgWkYZnmp == rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.CCAXgmpIWICHAxdXRCbCjrvfPSDecjrB:
                    ywKgRImchIHWvJXlMDzoGWEZwZuXkxOC = PCiQtOeHrYsokBqtFxBbpDPnOjZourbJ*KpITumKUkWAggHnDiNqKSkoTtPMTnyuQ[OpFlKMYGKpWqrQclNkbQJOyQGzPHDYJu]
                lPmJfojDSUTFirrgKPryiJRYyZOFajzZ.append(ompzonOkvRsHNKHceWNmvSNXZeCTwgaf(EbKSIFxpyCpzycRDApduouVsxspHzkTj=AkBFPvJWpORRGVppZZKLviMdeWBRZNeA+ywKgRImchIHWvJXlMDzoGWEZwZuXkxOC,
                                         DjnmEmFIylXDvTfeYtLbwRKPMHUXFjho=SFZANSjeQRuDmejNulCUPGLUGdwWWwIa,
                                         hMSVpTuyPHmoxFcPWurjMXzUcTNEpKNm=rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.temb_ch,
                                         kcIxGCXrUvsLPSfmGoULGFzAthVmTXcA=kcIxGCXrUvsLPSfmGoULGFzAthVmTXcA))
                AkBFPvJWpORRGVppZZKLviMdeWBRZNeA = SFZANSjeQRuDmejNulCUPGLUGdwWWwIa
                if WPrMyJZpYZhKJnvzZBeozEExkNgnAmVY in SVFgWZmLHyBDIohemjJyxOqQDTKUSaYc:
                    tUmudCfKVwpeKVqJPkVQAwLriIrTDLbW.append(qXfIkuZrNfESJcZDYMxfgdGOBPOHmKaF(AkBFPvJWpORRGVppZZKLviMdeWBRZNeA, FFkRWmQHKPdMiLiCPdiuVVUNvNEEvZkf=FFkRWmQHKPdMiLiCPdiuVVUNvNEEvZkf))
            kvJZslyswPMVzCnLtIoKrkpdfusdzxSS = nn.Module()
            kvJZslyswPMVzCnLtIoKrkpdfusdzxSS.lPmJfojDSUTFirrgKPryiJRYyZOFajzZ = lPmJfojDSUTFirrgKPryiJRYyZOFajzZ
            kvJZslyswPMVzCnLtIoKrkpdfusdzxSS.tUmudCfKVwpeKVqJPkVQAwLriIrTDLbW = tUmudCfKVwpeKVqJPkVQAwLriIrTDLbW
            if OpFlKMYGKpWqrQclNkbQJOyQGzPHDYJu != 0:
                kvJZslyswPMVzCnLtIoKrkpdfusdzxSS.upsample = kjruhryvXAQxnjJDeOXqTJbBrTkRFQSk(AkBFPvJWpORRGVppZZKLviMdeWBRZNeA, resamp_with_conv)
                WPrMyJZpYZhKJnvzZBeozEExkNgnAmVY = WPrMyJZpYZhKJnvzZBeozEExkNgnAmVY * 2
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.kvJZslyswPMVzCnLtIoKrkpdfusdzxSS.insert(0, kvJZslyswPMVzCnLtIoKrkpdfusdzxSS) 
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.norm_out = HSnGePyLrgZhiiSoMOwJmgVPBjIpItDD(AkBFPvJWpORRGVppZZKLviMdeWBRZNeA)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.conv_out = quasar.ops.LcFcvNeYCKrBHlNkoWrkqdbxdkNCJBBK(AkBFPvJWpORRGVppZZKLviMdeWBRZNeA,
                                        VAkEsdMDwAEDPzAuJymQaRUNIxlnDSEu,
                                        aBEJjpEOpoRJYkulwSmukddEYErxRnAG=3,
                                        NTEWXstfzqNXGESmGkQNFWBaQsGAPlGd=1,
                                        sdxdTSjnkAOjlGmltQHvLiHRDstMzpAP=1)
    def lqBgIcSWZYylbCPjXksJWDguuSOqoPCJ(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, NECAaWUrFGIXcLimrerEYmxYIykQBfXb, XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz=None, tRdCjhUPYVVxnSEkGmJIHWRitDXRXSZS=None):
        if tRdCjhUPYVVxnSEkGmJIHWRitDXRXSZS is not None:
            NECAaWUrFGIXcLimrerEYmxYIykQBfXb = torch.cat((NECAaWUrFGIXcLimrerEYmxYIykQBfXb, tRdCjhUPYVVxnSEkGmJIHWRitDXRXSZS), yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk=1)
        if rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.CJffilbwILRpyJZXwstdSKcmbtdBZCgF:
            assert XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz is not None
            sXAWsqVPxctAEwLmvNZmqxpDglMjciIT = FBGIyMBfRymrmsEWcEPIkRwuaTeBVITr(XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz, rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.PCiQtOeHrYsokBqtFxBbpDPnOjZourbJ)
            sXAWsqVPxctAEwLmvNZmqxpDglMjciIT = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.sXAWsqVPxctAEwLmvNZmqxpDglMjciIT.dense[0](sXAWsqVPxctAEwLmvNZmqxpDglMjciIT)
            sXAWsqVPxctAEwLmvNZmqxpDglMjciIT = liYZHxYGwkXhuYdMFrAtaIVIwKaEIKPp(sXAWsqVPxctAEwLmvNZmqxpDglMjciIT)
            sXAWsqVPxctAEwLmvNZmqxpDglMjciIT = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.sXAWsqVPxctAEwLmvNZmqxpDglMjciIT.dense[1](sXAWsqVPxctAEwLmvNZmqxpDglMjciIT)
        else:
            sXAWsqVPxctAEwLmvNZmqxpDglMjciIT = None
        omGAnSaAXbgvwNbvtUsYicLqgJqNBgst = [rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.conv_in(NECAaWUrFGIXcLimrerEYmxYIykQBfXb)]
        for OpFlKMYGKpWqrQclNkbQJOyQGzPHDYJu in range(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.num_resolutions):
            for zmRdsMNKEDpECOVrJyNRRisrgWkYZnmp in range(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.CCAXgmpIWICHAxdXRCbCjrvfPSDecjrB):
                xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.PKmeubCqZPUpSfmqJozYuvYsQsIMTIOn[OpFlKMYGKpWqrQclNkbQJOyQGzPHDYJu].lPmJfojDSUTFirrgKPryiJRYyZOFajzZ[zmRdsMNKEDpECOVrJyNRRisrgWkYZnmp](omGAnSaAXbgvwNbvtUsYicLqgJqNBgst[-1], sXAWsqVPxctAEwLmvNZmqxpDglMjciIT)
                if len(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.PKmeubCqZPUpSfmqJozYuvYsQsIMTIOn[OpFlKMYGKpWqrQclNkbQJOyQGzPHDYJu].tUmudCfKVwpeKVqJPkVQAwLriIrTDLbW) > 0:
                    xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.PKmeubCqZPUpSfmqJozYuvYsQsIMTIOn[OpFlKMYGKpWqrQclNkbQJOyQGzPHDYJu].tUmudCfKVwpeKVqJPkVQAwLriIrTDLbW[zmRdsMNKEDpECOVrJyNRRisrgWkYZnmp](xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab)
                omGAnSaAXbgvwNbvtUsYicLqgJqNBgst.append(xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab)
            if OpFlKMYGKpWqrQclNkbQJOyQGzPHDYJu != rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.num_resolutions-1:
                omGAnSaAXbgvwNbvtUsYicLqgJqNBgst.append(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.PKmeubCqZPUpSfmqJozYuvYsQsIMTIOn[OpFlKMYGKpWqrQclNkbQJOyQGzPHDYJu].FNdFYgmARbySAmYyEvSINcVrOJlCpKfW(omGAnSaAXbgvwNbvtUsYicLqgJqNBgst[-1]))
        xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab = omGAnSaAXbgvwNbvtUsYicLqgJqNBgst[-1]
        xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.rnBVwgYeGkHoRDXjLPBaCTIXNAZYBHGr.block_1(xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab, sXAWsqVPxctAEwLmvNZmqxpDglMjciIT)
        xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.rnBVwgYeGkHoRDXjLPBaCTIXNAZYBHGr.attn_1(xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab)
        xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.rnBVwgYeGkHoRDXjLPBaCTIXNAZYBHGr.block_2(xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab, sXAWsqVPxctAEwLmvNZmqxpDglMjciIT)
        for OpFlKMYGKpWqrQclNkbQJOyQGzPHDYJu in reversed(range(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.num_resolutions)):
            for zmRdsMNKEDpECOVrJyNRRisrgWkYZnmp in range(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.CCAXgmpIWICHAxdXRCbCjrvfPSDecjrB+1):
                xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.kvJZslyswPMVzCnLtIoKrkpdfusdzxSS[OpFlKMYGKpWqrQclNkbQJOyQGzPHDYJu].lPmJfojDSUTFirrgKPryiJRYyZOFajzZ[zmRdsMNKEDpECOVrJyNRRisrgWkYZnmp](
                    torch.cat([xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab, omGAnSaAXbgvwNbvtUsYicLqgJqNBgst.pop()], yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk=1), sXAWsqVPxctAEwLmvNZmqxpDglMjciIT)
                if len(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.kvJZslyswPMVzCnLtIoKrkpdfusdzxSS[OpFlKMYGKpWqrQclNkbQJOyQGzPHDYJu].tUmudCfKVwpeKVqJPkVQAwLriIrTDLbW) > 0:
                    xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.kvJZslyswPMVzCnLtIoKrkpdfusdzxSS[OpFlKMYGKpWqrQclNkbQJOyQGzPHDYJu].tUmudCfKVwpeKVqJPkVQAwLriIrTDLbW[zmRdsMNKEDpECOVrJyNRRisrgWkYZnmp](xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab)
            if OpFlKMYGKpWqrQclNkbQJOyQGzPHDYJu != 0:
                xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.kvJZslyswPMVzCnLtIoKrkpdfusdzxSS[OpFlKMYGKpWqrQclNkbQJOyQGzPHDYJu].upsample(xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab)
        xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.norm_out(xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab)
        xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab = liYZHxYGwkXhuYdMFrAtaIVIwKaEIKPp(xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab)
        xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.conv_out(xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab)
        return xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab
    def jAbQXzbRQmhDdUPexMZJhBfggMNexRBj(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS):
        return rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.conv_out.RXBOtvKSHQkBvdKDbckmnlphvVygYURP
class HAhRJZDsPfbaJIpLwjOXFEkHqjueFULJ(nn.Module):
    def __init__(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, *, PCiQtOeHrYsokBqtFxBbpDPnOjZourbJ, VAkEsdMDwAEDPzAuJymQaRUNIxlnDSEu, ch_mult=(1,2,4,8), CCAXgmpIWICHAxdXRCbCjrvfPSDecjrB,
                 SVFgWZmLHyBDIohemjJyxOqQDTKUSaYc, kcIxGCXrUvsLPSfmGoULGFzAthVmTXcA=0.0, resamp_with_conv=True, EbKSIFxpyCpzycRDApduouVsxspHzkTj,
                 BcSwNQTmUGuqaESGKyPNIfMVGtVTPcEr, dwRTcGdsCuBbMrwBzRJcZGczJdBPIxiA, rTIStVRWjZuwLBUuZUMVolrWVNgRvzZH=True, use_linear_attn=False, FFkRWmQHKPdMiLiCPdiuVVUNvNEEvZkf="vanilla",
                 **ignore_kwargs):
        super().__init__()
        if use_linear_attn: FFkRWmQHKPdMiLiCPdiuVVUNvNEEvZkf = "linear"
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.PCiQtOeHrYsokBqtFxBbpDPnOjZourbJ = PCiQtOeHrYsokBqtFxBbpDPnOjZourbJ
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.temb_ch = 0
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.num_resolutions = len(ch_mult)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.CCAXgmpIWICHAxdXRCbCjrvfPSDecjrB = CCAXgmpIWICHAxdXRCbCjrvfPSDecjrB
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.BcSwNQTmUGuqaESGKyPNIfMVGtVTPcEr = BcSwNQTmUGuqaESGKyPNIfMVGtVTPcEr
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.EbKSIFxpyCpzycRDApduouVsxspHzkTj = EbKSIFxpyCpzycRDApduouVsxspHzkTj
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.conv_in = quasar.ops.LcFcvNeYCKrBHlNkoWrkqdbxdkNCJBBK(EbKSIFxpyCpzycRDApduouVsxspHzkTj,
                                       rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.PCiQtOeHrYsokBqtFxBbpDPnOjZourbJ,
                                       aBEJjpEOpoRJYkulwSmukddEYErxRnAG=3,
                                       NTEWXstfzqNXGESmGkQNFWBaQsGAPlGd=1,
                                       sdxdTSjnkAOjlGmltQHvLiHRDstMzpAP=1)
        WPrMyJZpYZhKJnvzZBeozEExkNgnAmVY = BcSwNQTmUGuqaESGKyPNIfMVGtVTPcEr
        KpITumKUkWAggHnDiNqKSkoTtPMTnyuQ = (1,)+tuple(ch_mult)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.KpITumKUkWAggHnDiNqKSkoTtPMTnyuQ = KpITumKUkWAggHnDiNqKSkoTtPMTnyuQ
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.PKmeubCqZPUpSfmqJozYuvYsQsIMTIOn = nn.ModuleList()
        for OpFlKMYGKpWqrQclNkbQJOyQGzPHDYJu in range(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.num_resolutions):
            lPmJfojDSUTFirrgKPryiJRYyZOFajzZ = nn.ModuleList()
            tUmudCfKVwpeKVqJPkVQAwLriIrTDLbW = nn.ModuleList()
            AkBFPvJWpORRGVppZZKLviMdeWBRZNeA = PCiQtOeHrYsokBqtFxBbpDPnOjZourbJ*KpITumKUkWAggHnDiNqKSkoTtPMTnyuQ[OpFlKMYGKpWqrQclNkbQJOyQGzPHDYJu]
            SFZANSjeQRuDmejNulCUPGLUGdwWWwIa = PCiQtOeHrYsokBqtFxBbpDPnOjZourbJ*ch_mult[OpFlKMYGKpWqrQclNkbQJOyQGzPHDYJu]
            for zmRdsMNKEDpECOVrJyNRRisrgWkYZnmp in range(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.CCAXgmpIWICHAxdXRCbCjrvfPSDecjrB):
                lPmJfojDSUTFirrgKPryiJRYyZOFajzZ.append(ompzonOkvRsHNKHceWNmvSNXZeCTwgaf(EbKSIFxpyCpzycRDApduouVsxspHzkTj=AkBFPvJWpORRGVppZZKLviMdeWBRZNeA,
                                         DjnmEmFIylXDvTfeYtLbwRKPMHUXFjho=SFZANSjeQRuDmejNulCUPGLUGdwWWwIa,
                                         hMSVpTuyPHmoxFcPWurjMXzUcTNEpKNm=rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.temb_ch,
                                         kcIxGCXrUvsLPSfmGoULGFzAthVmTXcA=kcIxGCXrUvsLPSfmGoULGFzAthVmTXcA))
                AkBFPvJWpORRGVppZZKLviMdeWBRZNeA = SFZANSjeQRuDmejNulCUPGLUGdwWWwIa
                if WPrMyJZpYZhKJnvzZBeozEExkNgnAmVY in SVFgWZmLHyBDIohemjJyxOqQDTKUSaYc:
                    tUmudCfKVwpeKVqJPkVQAwLriIrTDLbW.append(qXfIkuZrNfESJcZDYMxfgdGOBPOHmKaF(AkBFPvJWpORRGVppZZKLviMdeWBRZNeA, FFkRWmQHKPdMiLiCPdiuVVUNvNEEvZkf=FFkRWmQHKPdMiLiCPdiuVVUNvNEEvZkf))
            PKmeubCqZPUpSfmqJozYuvYsQsIMTIOn = nn.Module()
            PKmeubCqZPUpSfmqJozYuvYsQsIMTIOn.lPmJfojDSUTFirrgKPryiJRYyZOFajzZ = lPmJfojDSUTFirrgKPryiJRYyZOFajzZ
            PKmeubCqZPUpSfmqJozYuvYsQsIMTIOn.tUmudCfKVwpeKVqJPkVQAwLriIrTDLbW = tUmudCfKVwpeKVqJPkVQAwLriIrTDLbW
            if OpFlKMYGKpWqrQclNkbQJOyQGzPHDYJu != rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.num_resolutions-1:
                PKmeubCqZPUpSfmqJozYuvYsQsIMTIOn.FNdFYgmARbySAmYyEvSINcVrOJlCpKfW = LpwKTfRyOAITGEdvwhtCdMnNRMEQUkUG(AkBFPvJWpORRGVppZZKLviMdeWBRZNeA, resamp_with_conv)
                WPrMyJZpYZhKJnvzZBeozEExkNgnAmVY = WPrMyJZpYZhKJnvzZBeozEExkNgnAmVY // 2
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.PKmeubCqZPUpSfmqJozYuvYsQsIMTIOn.append(PKmeubCqZPUpSfmqJozYuvYsQsIMTIOn)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.rnBVwgYeGkHoRDXjLPBaCTIXNAZYBHGr = nn.Module()
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.rnBVwgYeGkHoRDXjLPBaCTIXNAZYBHGr.block_1 = ompzonOkvRsHNKHceWNmvSNXZeCTwgaf(EbKSIFxpyCpzycRDApduouVsxspHzkTj=AkBFPvJWpORRGVppZZKLviMdeWBRZNeA,
                                       DjnmEmFIylXDvTfeYtLbwRKPMHUXFjho=AkBFPvJWpORRGVppZZKLviMdeWBRZNeA,
                                       hMSVpTuyPHmoxFcPWurjMXzUcTNEpKNm=rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.temb_ch,
                                       kcIxGCXrUvsLPSfmGoULGFzAthVmTXcA=kcIxGCXrUvsLPSfmGoULGFzAthVmTXcA)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.rnBVwgYeGkHoRDXjLPBaCTIXNAZYBHGr.attn_1 = qXfIkuZrNfESJcZDYMxfgdGOBPOHmKaF(AkBFPvJWpORRGVppZZKLviMdeWBRZNeA, FFkRWmQHKPdMiLiCPdiuVVUNvNEEvZkf=FFkRWmQHKPdMiLiCPdiuVVUNvNEEvZkf)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.rnBVwgYeGkHoRDXjLPBaCTIXNAZYBHGr.block_2 = ompzonOkvRsHNKHceWNmvSNXZeCTwgaf(EbKSIFxpyCpzycRDApduouVsxspHzkTj=AkBFPvJWpORRGVppZZKLviMdeWBRZNeA,
                                       DjnmEmFIylXDvTfeYtLbwRKPMHUXFjho=AkBFPvJWpORRGVppZZKLviMdeWBRZNeA,
                                       hMSVpTuyPHmoxFcPWurjMXzUcTNEpKNm=rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.temb_ch,
                                       kcIxGCXrUvsLPSfmGoULGFzAthVmTXcA=kcIxGCXrUvsLPSfmGoULGFzAthVmTXcA)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.norm_out = HSnGePyLrgZhiiSoMOwJmgVPBjIpItDD(AkBFPvJWpORRGVppZZKLviMdeWBRZNeA)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.conv_out = quasar.ops.LcFcvNeYCKrBHlNkoWrkqdbxdkNCJBBK(AkBFPvJWpORRGVppZZKLviMdeWBRZNeA,
                                        2*dwRTcGdsCuBbMrwBzRJcZGczJdBPIxiA if rTIStVRWjZuwLBUuZUMVolrWVNgRvzZH else dwRTcGdsCuBbMrwBzRJcZGczJdBPIxiA,
                                        aBEJjpEOpoRJYkulwSmukddEYErxRnAG=3,
                                        NTEWXstfzqNXGESmGkQNFWBaQsGAPlGd=1,
                                        sdxdTSjnkAOjlGmltQHvLiHRDstMzpAP=1)
    def lqBgIcSWZYylbCPjXksJWDguuSOqoPCJ(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, NECAaWUrFGIXcLimrerEYmxYIykQBfXb):
        sXAWsqVPxctAEwLmvNZmqxpDglMjciIT = None
        xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.conv_in(NECAaWUrFGIXcLimrerEYmxYIykQBfXb)
        for OpFlKMYGKpWqrQclNkbQJOyQGzPHDYJu in range(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.num_resolutions):
            for zmRdsMNKEDpECOVrJyNRRisrgWkYZnmp in range(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.CCAXgmpIWICHAxdXRCbCjrvfPSDecjrB):
                xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.PKmeubCqZPUpSfmqJozYuvYsQsIMTIOn[OpFlKMYGKpWqrQclNkbQJOyQGzPHDYJu].lPmJfojDSUTFirrgKPryiJRYyZOFajzZ[zmRdsMNKEDpECOVrJyNRRisrgWkYZnmp](xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab, sXAWsqVPxctAEwLmvNZmqxpDglMjciIT)
                if len(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.PKmeubCqZPUpSfmqJozYuvYsQsIMTIOn[OpFlKMYGKpWqrQclNkbQJOyQGzPHDYJu].tUmudCfKVwpeKVqJPkVQAwLriIrTDLbW) > 0:
                    xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.PKmeubCqZPUpSfmqJozYuvYsQsIMTIOn[OpFlKMYGKpWqrQclNkbQJOyQGzPHDYJu].tUmudCfKVwpeKVqJPkVQAwLriIrTDLbW[zmRdsMNKEDpECOVrJyNRRisrgWkYZnmp](xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab)
            if OpFlKMYGKpWqrQclNkbQJOyQGzPHDYJu != rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.num_resolutions-1:
                xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.PKmeubCqZPUpSfmqJozYuvYsQsIMTIOn[OpFlKMYGKpWqrQclNkbQJOyQGzPHDYJu].FNdFYgmARbySAmYyEvSINcVrOJlCpKfW(xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab)
        xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.rnBVwgYeGkHoRDXjLPBaCTIXNAZYBHGr.block_1(xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab, sXAWsqVPxctAEwLmvNZmqxpDglMjciIT)
        xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.rnBVwgYeGkHoRDXjLPBaCTIXNAZYBHGr.attn_1(xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab)
        xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.rnBVwgYeGkHoRDXjLPBaCTIXNAZYBHGr.block_2(xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab, sXAWsqVPxctAEwLmvNZmqxpDglMjciIT)
        xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.norm_out(xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab)
        xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab = liYZHxYGwkXhuYdMFrAtaIVIwKaEIKPp(xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab)
        xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.conv_out(xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab)
        return xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab
class KfKIubLWuMYndZytaOVMUrnTLHiwPiVV(nn.Module):
    def __init__(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, *, PCiQtOeHrYsokBqtFxBbpDPnOjZourbJ, VAkEsdMDwAEDPzAuJymQaRUNIxlnDSEu, ch_mult=(1,2,4,8), CCAXgmpIWICHAxdXRCbCjrvfPSDecjrB,
                 SVFgWZmLHyBDIohemjJyxOqQDTKUSaYc, kcIxGCXrUvsLPSfmGoULGFzAthVmTXcA=0.0, resamp_with_conv=True, EbKSIFxpyCpzycRDApduouVsxspHzkTj,
                 BcSwNQTmUGuqaESGKyPNIfMVGtVTPcEr, dwRTcGdsCuBbMrwBzRJcZGczJdBPIxiA, AkDeslgfXSBVSvrenRQZoNDfcUqMZnbc=False, tanh_out=False, use_linear_attn=False,
                 FFkRWmQHKPdMiLiCPdiuVVUNvNEEvZkf="vanilla", **ignorekwargs):
        super().__init__()
        if use_linear_attn: FFkRWmQHKPdMiLiCPdiuVVUNvNEEvZkf = "linear"
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.PCiQtOeHrYsokBqtFxBbpDPnOjZourbJ = PCiQtOeHrYsokBqtFxBbpDPnOjZourbJ
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.temb_ch = 0
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.num_resolutions = len(ch_mult)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.CCAXgmpIWICHAxdXRCbCjrvfPSDecjrB = CCAXgmpIWICHAxdXRCbCjrvfPSDecjrB
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.BcSwNQTmUGuqaESGKyPNIfMVGtVTPcEr = BcSwNQTmUGuqaESGKyPNIfMVGtVTPcEr
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.EbKSIFxpyCpzycRDApduouVsxspHzkTj = EbKSIFxpyCpzycRDApduouVsxspHzkTj
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.AkDeslgfXSBVSvrenRQZoNDfcUqMZnbc = AkDeslgfXSBVSvrenRQZoNDfcUqMZnbc
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.tanh_out = tanh_out
        KpITumKUkWAggHnDiNqKSkoTtPMTnyuQ = (1,)+tuple(ch_mult)
        AkBFPvJWpORRGVppZZKLviMdeWBRZNeA = PCiQtOeHrYsokBqtFxBbpDPnOjZourbJ*ch_mult[rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.num_resolutions-1]
        WPrMyJZpYZhKJnvzZBeozEExkNgnAmVY = BcSwNQTmUGuqaESGKyPNIfMVGtVTPcEr // 2**(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.num_resolutions-1)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.z_shape = (1,dwRTcGdsCuBbMrwBzRJcZGczJdBPIxiA,WPrMyJZpYZhKJnvzZBeozEExkNgnAmVY,WPrMyJZpYZhKJnvzZBeozEExkNgnAmVY)
        print("Working with z of shape {} = {} dimensions.".format(
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.z_shape, np.AxEOibCbRjeUvRwvVNaXLXCBIIzXUnBD(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.z_shape)))
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.conv_in = quasar.ops.LcFcvNeYCKrBHlNkoWrkqdbxdkNCJBBK(dwRTcGdsCuBbMrwBzRJcZGczJdBPIxiA,
                                       AkBFPvJWpORRGVppZZKLviMdeWBRZNeA,
                                       aBEJjpEOpoRJYkulwSmukddEYErxRnAG=3,
                                       NTEWXstfzqNXGESmGkQNFWBaQsGAPlGd=1,
                                       sdxdTSjnkAOjlGmltQHvLiHRDstMzpAP=1)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.rnBVwgYeGkHoRDXjLPBaCTIXNAZYBHGr = nn.Module()
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.rnBVwgYeGkHoRDXjLPBaCTIXNAZYBHGr.block_1 = ompzonOkvRsHNKHceWNmvSNXZeCTwgaf(EbKSIFxpyCpzycRDApduouVsxspHzkTj=AkBFPvJWpORRGVppZZKLviMdeWBRZNeA,
                                       DjnmEmFIylXDvTfeYtLbwRKPMHUXFjho=AkBFPvJWpORRGVppZZKLviMdeWBRZNeA,
                                       hMSVpTuyPHmoxFcPWurjMXzUcTNEpKNm=rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.temb_ch,
                                       kcIxGCXrUvsLPSfmGoULGFzAthVmTXcA=kcIxGCXrUvsLPSfmGoULGFzAthVmTXcA)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.rnBVwgYeGkHoRDXjLPBaCTIXNAZYBHGr.attn_1 = qXfIkuZrNfESJcZDYMxfgdGOBPOHmKaF(AkBFPvJWpORRGVppZZKLviMdeWBRZNeA, FFkRWmQHKPdMiLiCPdiuVVUNvNEEvZkf=FFkRWmQHKPdMiLiCPdiuVVUNvNEEvZkf)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.rnBVwgYeGkHoRDXjLPBaCTIXNAZYBHGr.block_2 = ompzonOkvRsHNKHceWNmvSNXZeCTwgaf(EbKSIFxpyCpzycRDApduouVsxspHzkTj=AkBFPvJWpORRGVppZZKLviMdeWBRZNeA,
                                       DjnmEmFIylXDvTfeYtLbwRKPMHUXFjho=AkBFPvJWpORRGVppZZKLviMdeWBRZNeA,
                                       hMSVpTuyPHmoxFcPWurjMXzUcTNEpKNm=rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.temb_ch,
                                       kcIxGCXrUvsLPSfmGoULGFzAthVmTXcA=kcIxGCXrUvsLPSfmGoULGFzAthVmTXcA)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.kvJZslyswPMVzCnLtIoKrkpdfusdzxSS = nn.ModuleList()
        for OpFlKMYGKpWqrQclNkbQJOyQGzPHDYJu in reversed(range(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.num_resolutions)):
            lPmJfojDSUTFirrgKPryiJRYyZOFajzZ = nn.ModuleList()
            tUmudCfKVwpeKVqJPkVQAwLriIrTDLbW = nn.ModuleList()
            SFZANSjeQRuDmejNulCUPGLUGdwWWwIa = PCiQtOeHrYsokBqtFxBbpDPnOjZourbJ*ch_mult[OpFlKMYGKpWqrQclNkbQJOyQGzPHDYJu]
            for zmRdsMNKEDpECOVrJyNRRisrgWkYZnmp in range(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.CCAXgmpIWICHAxdXRCbCjrvfPSDecjrB+1):
                lPmJfojDSUTFirrgKPryiJRYyZOFajzZ.append(ompzonOkvRsHNKHceWNmvSNXZeCTwgaf(EbKSIFxpyCpzycRDApduouVsxspHzkTj=AkBFPvJWpORRGVppZZKLviMdeWBRZNeA,
                                         DjnmEmFIylXDvTfeYtLbwRKPMHUXFjho=SFZANSjeQRuDmejNulCUPGLUGdwWWwIa,
                                         hMSVpTuyPHmoxFcPWurjMXzUcTNEpKNm=rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.temb_ch,
                                         kcIxGCXrUvsLPSfmGoULGFzAthVmTXcA=kcIxGCXrUvsLPSfmGoULGFzAthVmTXcA))
                AkBFPvJWpORRGVppZZKLviMdeWBRZNeA = SFZANSjeQRuDmejNulCUPGLUGdwWWwIa
                if WPrMyJZpYZhKJnvzZBeozEExkNgnAmVY in SVFgWZmLHyBDIohemjJyxOqQDTKUSaYc:
                    tUmudCfKVwpeKVqJPkVQAwLriIrTDLbW.append(qXfIkuZrNfESJcZDYMxfgdGOBPOHmKaF(AkBFPvJWpORRGVppZZKLviMdeWBRZNeA, FFkRWmQHKPdMiLiCPdiuVVUNvNEEvZkf=FFkRWmQHKPdMiLiCPdiuVVUNvNEEvZkf))
            kvJZslyswPMVzCnLtIoKrkpdfusdzxSS = nn.Module()
            kvJZslyswPMVzCnLtIoKrkpdfusdzxSS.lPmJfojDSUTFirrgKPryiJRYyZOFajzZ = lPmJfojDSUTFirrgKPryiJRYyZOFajzZ
            kvJZslyswPMVzCnLtIoKrkpdfusdzxSS.tUmudCfKVwpeKVqJPkVQAwLriIrTDLbW = tUmudCfKVwpeKVqJPkVQAwLriIrTDLbW
            if OpFlKMYGKpWqrQclNkbQJOyQGzPHDYJu != 0:
                kvJZslyswPMVzCnLtIoKrkpdfusdzxSS.upsample = kjruhryvXAQxnjJDeOXqTJbBrTkRFQSk(AkBFPvJWpORRGVppZZKLviMdeWBRZNeA, resamp_with_conv)
                WPrMyJZpYZhKJnvzZBeozEExkNgnAmVY = WPrMyJZpYZhKJnvzZBeozEExkNgnAmVY * 2
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.kvJZslyswPMVzCnLtIoKrkpdfusdzxSS.insert(0, kvJZslyswPMVzCnLtIoKrkpdfusdzxSS) 
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.norm_out = HSnGePyLrgZhiiSoMOwJmgVPBjIpItDD(AkBFPvJWpORRGVppZZKLviMdeWBRZNeA)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.conv_out = quasar.ops.LcFcvNeYCKrBHlNkoWrkqdbxdkNCJBBK(AkBFPvJWpORRGVppZZKLviMdeWBRZNeA,
                                        VAkEsdMDwAEDPzAuJymQaRUNIxlnDSEu,
                                        aBEJjpEOpoRJYkulwSmukddEYErxRnAG=3,
                                        NTEWXstfzqNXGESmGkQNFWBaQsGAPlGd=1,
                                        sdxdTSjnkAOjlGmltQHvLiHRDstMzpAP=1)
    def lqBgIcSWZYylbCPjXksJWDguuSOqoPCJ(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, AVjwZelSxiiANPDkDuRKTIIJYnqgQaTi):
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.last_z_shape = AVjwZelSxiiANPDkDuRKTIIJYnqgQaTi.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg
        sXAWsqVPxctAEwLmvNZmqxpDglMjciIT = None
        xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.conv_in(AVjwZelSxiiANPDkDuRKTIIJYnqgQaTi)
        xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.rnBVwgYeGkHoRDXjLPBaCTIXNAZYBHGr.block_1(xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab, sXAWsqVPxctAEwLmvNZmqxpDglMjciIT)
        xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.rnBVwgYeGkHoRDXjLPBaCTIXNAZYBHGr.attn_1(xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab)
        xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.rnBVwgYeGkHoRDXjLPBaCTIXNAZYBHGr.block_2(xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab, sXAWsqVPxctAEwLmvNZmqxpDglMjciIT)
        for OpFlKMYGKpWqrQclNkbQJOyQGzPHDYJu in reversed(range(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.num_resolutions)):
            for zmRdsMNKEDpECOVrJyNRRisrgWkYZnmp in range(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.CCAXgmpIWICHAxdXRCbCjrvfPSDecjrB+1):
                xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.kvJZslyswPMVzCnLtIoKrkpdfusdzxSS[OpFlKMYGKpWqrQclNkbQJOyQGzPHDYJu].lPmJfojDSUTFirrgKPryiJRYyZOFajzZ[zmRdsMNKEDpECOVrJyNRRisrgWkYZnmp](xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab, sXAWsqVPxctAEwLmvNZmqxpDglMjciIT)
                if len(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.kvJZslyswPMVzCnLtIoKrkpdfusdzxSS[OpFlKMYGKpWqrQclNkbQJOyQGzPHDYJu].tUmudCfKVwpeKVqJPkVQAwLriIrTDLbW) > 0:
                    xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.kvJZslyswPMVzCnLtIoKrkpdfusdzxSS[OpFlKMYGKpWqrQclNkbQJOyQGzPHDYJu].tUmudCfKVwpeKVqJPkVQAwLriIrTDLbW[zmRdsMNKEDpECOVrJyNRRisrgWkYZnmp](xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab)
            if OpFlKMYGKpWqrQclNkbQJOyQGzPHDYJu != 0:
                xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.kvJZslyswPMVzCnLtIoKrkpdfusdzxSS[OpFlKMYGKpWqrQclNkbQJOyQGzPHDYJu].upsample(xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab)
        if rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.AkDeslgfXSBVSvrenRQZoNDfcUqMZnbc:
            return xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab
        xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.norm_out(xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab)
        xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab = liYZHxYGwkXhuYdMFrAtaIVIwKaEIKPp(xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab)
        xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.conv_out(xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab)
        if rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.tanh_out:
            xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab = torch.tanh(xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab)
        return xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab
