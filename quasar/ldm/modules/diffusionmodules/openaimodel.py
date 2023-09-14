from abc import abstractmethod
import math
import numpy as np
import torch as th
import torch.nn as nn
import torch.nn.functional as F
from .util import (
    vcSlHLxBcVodHmZrzACHLEJuENMXjWTG,
    ppDrxhPctQxMusBvKAntWykhHyNnAUtv,
    TVrUNiPGCtAmXFOUoqodGJnRgbvoldNA,
    DvCWYnpMIBQxXcLuPCRaTuuQvPYPGGWh,
    gjzRLJpCqzjvjCYIlAGlFiFZIQLazZsd,
)
from ..attention import CvuNifYqMqjsNqfVaEEpwROqJiOUCfhu
from quasar.ldm.util import exists
import quasar.ops
class LGJrzWOmnMkUAuAZdNrpyxhOgAHLcaqg(nn.Module):
    @abstractmethod
    def lqBgIcSWZYylbCPjXksJWDguuSOqoPCJ(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, NECAaWUrFGIXcLimrerEYmxYIykQBfXb, cbvuxLJlTEiYpJEoytPnUgMhAcRHRwIE):
class ETGhHLqpqtlhedBMHvqXdpnYyyTCWDrS(nn.Sequential, LGJrzWOmnMkUAuAZdNrpyxhOgAHLcaqg):
    def lqBgIcSWZYylbCPjXksJWDguuSOqoPCJ(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, NECAaWUrFGIXcLimrerEYmxYIykQBfXb, cbvuxLJlTEiYpJEoytPnUgMhAcRHRwIE, tRdCjhUPYVVxnSEkGmJIHWRitDXRXSZS=None, transformer_options={}, onnoKTSBXtsNokVdhRRVzlkVGMUUuaBt=None):
        for rmOubEJgfxmJuwTevhKPPVPDYGHXWRFZ in rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS:
            if isinstance(rmOubEJgfxmJuwTevhKPPVPDYGHXWRFZ, LGJrzWOmnMkUAuAZdNrpyxhOgAHLcaqg):
                NECAaWUrFGIXcLimrerEYmxYIykQBfXb = rmOubEJgfxmJuwTevhKPPVPDYGHXWRFZ(NECAaWUrFGIXcLimrerEYmxYIykQBfXb, cbvuxLJlTEiYpJEoytPnUgMhAcRHRwIE)
            elif isinstance(rmOubEJgfxmJuwTevhKPPVPDYGHXWRFZ, CvuNifYqMqjsNqfVaEEpwROqJiOUCfhu):
                NECAaWUrFGIXcLimrerEYmxYIykQBfXb = rmOubEJgfxmJuwTevhKPPVPDYGHXWRFZ(NECAaWUrFGIXcLimrerEYmxYIykQBfXb, tRdCjhUPYVVxnSEkGmJIHWRitDXRXSZS, transformer_options)
            elif isinstance(rmOubEJgfxmJuwTevhKPPVPDYGHXWRFZ, kjruhryvXAQxnjJDeOXqTJbBrTkRFQSk):
                NECAaWUrFGIXcLimrerEYmxYIykQBfXb = rmOubEJgfxmJuwTevhKPPVPDYGHXWRFZ(NECAaWUrFGIXcLimrerEYmxYIykQBfXb, onnoKTSBXtsNokVdhRRVzlkVGMUUuaBt=onnoKTSBXtsNokVdhRRVzlkVGMUUuaBt)
            else:
                NECAaWUrFGIXcLimrerEYmxYIykQBfXb = rmOubEJgfxmJuwTevhKPPVPDYGHXWRFZ(NECAaWUrFGIXcLimrerEYmxYIykQBfXb)
        return NECAaWUrFGIXcLimrerEYmxYIykQBfXb
def lgcRKzdVlZLqUAtcHVZRPLwLobDmukAq(cZfLNeHGLvPreutnrDmWGGyKvtymQVKM, NECAaWUrFGIXcLimrerEYmxYIykQBfXb, cbvuxLJlTEiYpJEoytPnUgMhAcRHRwIE, tRdCjhUPYVVxnSEkGmJIHWRitDXRXSZS=None, transformer_options={}, onnoKTSBXtsNokVdhRRVzlkVGMUUuaBt=None):
    for rmOubEJgfxmJuwTevhKPPVPDYGHXWRFZ in cZfLNeHGLvPreutnrDmWGGyKvtymQVKM:
        if isinstance(rmOubEJgfxmJuwTevhKPPVPDYGHXWRFZ, LGJrzWOmnMkUAuAZdNrpyxhOgAHLcaqg):
            NECAaWUrFGIXcLimrerEYmxYIykQBfXb = rmOubEJgfxmJuwTevhKPPVPDYGHXWRFZ(NECAaWUrFGIXcLimrerEYmxYIykQBfXb, cbvuxLJlTEiYpJEoytPnUgMhAcRHRwIE)
        elif isinstance(rmOubEJgfxmJuwTevhKPPVPDYGHXWRFZ, CvuNifYqMqjsNqfVaEEpwROqJiOUCfhu):
            NECAaWUrFGIXcLimrerEYmxYIykQBfXb = rmOubEJgfxmJuwTevhKPPVPDYGHXWRFZ(NECAaWUrFGIXcLimrerEYmxYIykQBfXb, tRdCjhUPYVVxnSEkGmJIHWRitDXRXSZS, transformer_options)
            transformer_options["current_index"] += 1
        elif isinstance(rmOubEJgfxmJuwTevhKPPVPDYGHXWRFZ, kjruhryvXAQxnjJDeOXqTJbBrTkRFQSk):
            NECAaWUrFGIXcLimrerEYmxYIykQBfXb = rmOubEJgfxmJuwTevhKPPVPDYGHXWRFZ(NECAaWUrFGIXcLimrerEYmxYIykQBfXb, onnoKTSBXtsNokVdhRRVzlkVGMUUuaBt=onnoKTSBXtsNokVdhRRVzlkVGMUUuaBt)
        else:
            NECAaWUrFGIXcLimrerEYmxYIykQBfXb = rmOubEJgfxmJuwTevhKPPVPDYGHXWRFZ(NECAaWUrFGIXcLimrerEYmxYIykQBfXb)
    return NECAaWUrFGIXcLimrerEYmxYIykQBfXb
class kjruhryvXAQxnjJDeOXqTJbBrTkRFQSk(nn.Module):
    def __init__(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, channels, BMidABgMadzWxSilVoOpGtdqLSQhQAjN, ipYTWVOPDpfJXeTFApPIgldytQSaUFdk=2, DjnmEmFIylXDvTfeYtLbwRKPMHUXFjho=None, sdxdTSjnkAOjlGmltQHvLiHRDstMzpAP=1, DDRQlhrNSGpwTrokWitkZipdfbAqBFxv=None, fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc=None, xwIQGNbJnSVpLrBBfhMLBchFpoolNzOe=quasar.ops):
        super().__init__()
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.channels = channels
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.DjnmEmFIylXDvTfeYtLbwRKPMHUXFjho = DjnmEmFIylXDvTfeYtLbwRKPMHUXFjho or channels
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.BMidABgMadzWxSilVoOpGtdqLSQhQAjN = BMidABgMadzWxSilVoOpGtdqLSQhQAjN
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.ipYTWVOPDpfJXeTFApPIgldytQSaUFdk = ipYTWVOPDpfJXeTFApPIgldytQSaUFdk
        if BMidABgMadzWxSilVoOpGtdqLSQhQAjN:
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.VRzIOXLfdDszfSOpzuKgtjeGGtXuyctm = xwIQGNbJnSVpLrBBfhMLBchFpoolNzOe.XqmPajboESpTdLShIQpHOQZiwGoVuVAj(ipYTWVOPDpfJXeTFApPIgldytQSaUFdk, rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.channels, rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.DjnmEmFIylXDvTfeYtLbwRKPMHUXFjho, 3, sdxdTSjnkAOjlGmltQHvLiHRDstMzpAP=sdxdTSjnkAOjlGmltQHvLiHRDstMzpAP, DDRQlhrNSGpwTrokWitkZipdfbAqBFxv=DDRQlhrNSGpwTrokWitkZipdfbAqBFxv, fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc=fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc)
    def lqBgIcSWZYylbCPjXksJWDguuSOqoPCJ(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, NECAaWUrFGIXcLimrerEYmxYIykQBfXb, onnoKTSBXtsNokVdhRRVzlkVGMUUuaBt=None):
        assert NECAaWUrFGIXcLimrerEYmxYIykQBfXb.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[1] == rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.channels
        if rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.ipYTWVOPDpfJXeTFApPIgldytQSaUFdk == 3:
            BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg = [NECAaWUrFGIXcLimrerEYmxYIykQBfXb.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[2], NECAaWUrFGIXcLimrerEYmxYIykQBfXb.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[3] * 2, NECAaWUrFGIXcLimrerEYmxYIykQBfXb.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[4] * 2]
            if onnoKTSBXtsNokVdhRRVzlkVGMUUuaBt is not None:
                BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[1] = onnoKTSBXtsNokVdhRRVzlkVGMUUuaBt[3]
                BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[2] = onnoKTSBXtsNokVdhRRVzlkVGMUUuaBt[4]
        else:
            BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg = [NECAaWUrFGIXcLimrerEYmxYIykQBfXb.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[2] * 2, NECAaWUrFGIXcLimrerEYmxYIykQBfXb.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[3] * 2]
            if onnoKTSBXtsNokVdhRRVzlkVGMUUuaBt is not None:
                BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[0] = onnoKTSBXtsNokVdhRRVzlkVGMUUuaBt[2]
                BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[1] = onnoKTSBXtsNokVdhRRVzlkVGMUUuaBt[3]
        NECAaWUrFGIXcLimrerEYmxYIykQBfXb = F.interpolate(NECAaWUrFGIXcLimrerEYmxYIykQBfXb, vqDBJgidQufnKyAltPYRqiKGjmztArDJ=BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg, bPTwwoDdWiuYqhtrDEHoDbHGiYcwcsQC="nearest")
        if rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.BMidABgMadzWxSilVoOpGtdqLSQhQAjN:
            NECAaWUrFGIXcLimrerEYmxYIykQBfXb = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.VRzIOXLfdDszfSOpzuKgtjeGGtXuyctm(NECAaWUrFGIXcLimrerEYmxYIykQBfXb)
        return NECAaWUrFGIXcLimrerEYmxYIykQBfXb
class LpwKTfRyOAITGEdvwhtCdMnNRMEQUkUG(nn.Module):
    def __init__(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, channels, BMidABgMadzWxSilVoOpGtdqLSQhQAjN, ipYTWVOPDpfJXeTFApPIgldytQSaUFdk=2, DjnmEmFIylXDvTfeYtLbwRKPMHUXFjho=None, sdxdTSjnkAOjlGmltQHvLiHRDstMzpAP=1, DDRQlhrNSGpwTrokWitkZipdfbAqBFxv=None, fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc=None, xwIQGNbJnSVpLrBBfhMLBchFpoolNzOe=quasar.ops):
        super().__init__()
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.channels = channels
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.DjnmEmFIylXDvTfeYtLbwRKPMHUXFjho = DjnmEmFIylXDvTfeYtLbwRKPMHUXFjho or channels
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.BMidABgMadzWxSilVoOpGtdqLSQhQAjN = BMidABgMadzWxSilVoOpGtdqLSQhQAjN
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.ipYTWVOPDpfJXeTFApPIgldytQSaUFdk = ipYTWVOPDpfJXeTFApPIgldytQSaUFdk
        NTEWXstfzqNXGESmGkQNFWBaQsGAPlGd = 2 if ipYTWVOPDpfJXeTFApPIgldytQSaUFdk != 3 else (1, 2, 2)
        if BMidABgMadzWxSilVoOpGtdqLSQhQAjN:
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.bjtPzNLsLxvykINbAtlMwKlGJQooJtzI = xwIQGNbJnSVpLrBBfhMLBchFpoolNzOe.XqmPajboESpTdLShIQpHOQZiwGoVuVAj(
                ipYTWVOPDpfJXeTFApPIgldytQSaUFdk, rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.channels, rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.DjnmEmFIylXDvTfeYtLbwRKPMHUXFjho, 3, NTEWXstfzqNXGESmGkQNFWBaQsGAPlGd=NTEWXstfzqNXGESmGkQNFWBaQsGAPlGd, sdxdTSjnkAOjlGmltQHvLiHRDstMzpAP=sdxdTSjnkAOjlGmltQHvLiHRDstMzpAP, DDRQlhrNSGpwTrokWitkZipdfbAqBFxv=DDRQlhrNSGpwTrokWitkZipdfbAqBFxv, fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc=fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc
            )
        else:
            assert rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.channels == rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.DjnmEmFIylXDvTfeYtLbwRKPMHUXFjho
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.bjtPzNLsLxvykINbAtlMwKlGJQooJtzI = ppDrxhPctQxMusBvKAntWykhHyNnAUtv(ipYTWVOPDpfJXeTFApPIgldytQSaUFdk, aBEJjpEOpoRJYkulwSmukddEYErxRnAG=NTEWXstfzqNXGESmGkQNFWBaQsGAPlGd, NTEWXstfzqNXGESmGkQNFWBaQsGAPlGd=NTEWXstfzqNXGESmGkQNFWBaQsGAPlGd)
    def lqBgIcSWZYylbCPjXksJWDguuSOqoPCJ(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, NECAaWUrFGIXcLimrerEYmxYIykQBfXb):
        assert NECAaWUrFGIXcLimrerEYmxYIykQBfXb.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[1] == rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.channels
        return rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.bjtPzNLsLxvykINbAtlMwKlGJQooJtzI(NECAaWUrFGIXcLimrerEYmxYIykQBfXb)
class WyEaQvHmxeWCTWupmPIsgcbcMkcKnPVN(LGJrzWOmnMkUAuAZdNrpyxhOgAHLcaqg):
    def __init__(
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS,
        channels,
        emb_channels,
        kcIxGCXrUvsLPSfmGoULGFzAthVmTXcA,
        DjnmEmFIylXDvTfeYtLbwRKPMHUXFjho=None,
        BMidABgMadzWxSilVoOpGtdqLSQhQAjN=False,
        ihazehElCCwCXjMBaNMdYMBnXEUKZiVD=False,
        ipYTWVOPDpfJXeTFApPIgldytQSaUFdk=2,
        TkHgGRFhDYRqyKuFvQRlKbpOBXUaEDVU=False,
        kvJZslyswPMVzCnLtIoKrkpdfusdzxSS=False,
        PKmeubCqZPUpSfmqJozYuvYsQsIMTIOn=False,
        DDRQlhrNSGpwTrokWitkZipdfbAqBFxv=None,
        fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc=None,
        xwIQGNbJnSVpLrBBfhMLBchFpoolNzOe=quasar.ops
    ):
        super().__init__()
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.channels = channels
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.emb_channels = emb_channels
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.kcIxGCXrUvsLPSfmGoULGFzAthVmTXcA = kcIxGCXrUvsLPSfmGoULGFzAthVmTXcA
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.DjnmEmFIylXDvTfeYtLbwRKPMHUXFjho = DjnmEmFIylXDvTfeYtLbwRKPMHUXFjho or channels
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.BMidABgMadzWxSilVoOpGtdqLSQhQAjN = BMidABgMadzWxSilVoOpGtdqLSQhQAjN
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.TkHgGRFhDYRqyKuFvQRlKbpOBXUaEDVU = TkHgGRFhDYRqyKuFvQRlKbpOBXUaEDVU
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.ihazehElCCwCXjMBaNMdYMBnXEUKZiVD = ihazehElCCwCXjMBaNMdYMBnXEUKZiVD
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.in_layers = nn.Sequential(
            nn.GroupNorm(32, channels, DDRQlhrNSGpwTrokWitkZipdfbAqBFxv=DDRQlhrNSGpwTrokWitkZipdfbAqBFxv, fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc=fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc),
            nn.XHAfRvdQzGhVBUIWzxCQjrhAiQInnRoY(),
            xwIQGNbJnSVpLrBBfhMLBchFpoolNzOe.XqmPajboESpTdLShIQpHOQZiwGoVuVAj(ipYTWVOPDpfJXeTFApPIgldytQSaUFdk, channels, rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.DjnmEmFIylXDvTfeYtLbwRKPMHUXFjho, 3, sdxdTSjnkAOjlGmltQHvLiHRDstMzpAP=1, DDRQlhrNSGpwTrokWitkZipdfbAqBFxv=DDRQlhrNSGpwTrokWitkZipdfbAqBFxv, fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc=fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc),
        )
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.updown = kvJZslyswPMVzCnLtIoKrkpdfusdzxSS or PKmeubCqZPUpSfmqJozYuvYsQsIMTIOn
        if kvJZslyswPMVzCnLtIoKrkpdfusdzxSS:
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.h_upd = kjruhryvXAQxnjJDeOXqTJbBrTkRFQSk(channels, False, ipYTWVOPDpfJXeTFApPIgldytQSaUFdk, DDRQlhrNSGpwTrokWitkZipdfbAqBFxv=DDRQlhrNSGpwTrokWitkZipdfbAqBFxv, fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc=fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc)
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.x_upd = kjruhryvXAQxnjJDeOXqTJbBrTkRFQSk(channels, False, ipYTWVOPDpfJXeTFApPIgldytQSaUFdk, DDRQlhrNSGpwTrokWitkZipdfbAqBFxv=DDRQlhrNSGpwTrokWitkZipdfbAqBFxv, fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc=fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc)
        elif PKmeubCqZPUpSfmqJozYuvYsQsIMTIOn:
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.h_upd = LpwKTfRyOAITGEdvwhtCdMnNRMEQUkUG(channels, False, ipYTWVOPDpfJXeTFApPIgldytQSaUFdk, DDRQlhrNSGpwTrokWitkZipdfbAqBFxv=DDRQlhrNSGpwTrokWitkZipdfbAqBFxv, fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc=fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc)
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.x_upd = LpwKTfRyOAITGEdvwhtCdMnNRMEQUkUG(channels, False, ipYTWVOPDpfJXeTFApPIgldytQSaUFdk, DDRQlhrNSGpwTrokWitkZipdfbAqBFxv=DDRQlhrNSGpwTrokWitkZipdfbAqBFxv, fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc=fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc)
        else:
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.h_upd = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.x_upd = nn.Identity()
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.emb_layers = nn.Sequential(
            nn.XHAfRvdQzGhVBUIWzxCQjrhAiQInnRoY(),
            xwIQGNbJnSVpLrBBfhMLBchFpoolNzOe.DhMcMyEvvzmWIEJojbQeGHlzfZKiPzHO(
                emb_channels,
                2 * rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.DjnmEmFIylXDvTfeYtLbwRKPMHUXFjho if ihazehElCCwCXjMBaNMdYMBnXEUKZiVD else rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.DjnmEmFIylXDvTfeYtLbwRKPMHUXFjho, DDRQlhrNSGpwTrokWitkZipdfbAqBFxv=DDRQlhrNSGpwTrokWitkZipdfbAqBFxv, fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc=fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc
            ),
        )
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.out_layers = nn.Sequential(
            nn.GroupNorm(32, rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.DjnmEmFIylXDvTfeYtLbwRKPMHUXFjho, DDRQlhrNSGpwTrokWitkZipdfbAqBFxv=DDRQlhrNSGpwTrokWitkZipdfbAqBFxv, fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc=fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc),
            nn.XHAfRvdQzGhVBUIWzxCQjrhAiQInnRoY(),
            nn.Dropout(HutkrxeXIuRQKOhCWHkiwqLGAsJjUSKj=kcIxGCXrUvsLPSfmGoULGFzAthVmTXcA),
            TVrUNiPGCtAmXFOUoqodGJnRgbvoldNA(
                xwIQGNbJnSVpLrBBfhMLBchFpoolNzOe.XqmPajboESpTdLShIQpHOQZiwGoVuVAj(ipYTWVOPDpfJXeTFApPIgldytQSaUFdk, rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.DjnmEmFIylXDvTfeYtLbwRKPMHUXFjho, rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.DjnmEmFIylXDvTfeYtLbwRKPMHUXFjho, 3, sdxdTSjnkAOjlGmltQHvLiHRDstMzpAP=1, DDRQlhrNSGpwTrokWitkZipdfbAqBFxv=DDRQlhrNSGpwTrokWitkZipdfbAqBFxv, fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc=fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc)
            ),
        )
        if rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.DjnmEmFIylXDvTfeYtLbwRKPMHUXFjho == channels:
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.skip_connection = nn.Identity()
        elif BMidABgMadzWxSilVoOpGtdqLSQhQAjN:
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.skip_connection = xwIQGNbJnSVpLrBBfhMLBchFpoolNzOe.XqmPajboESpTdLShIQpHOQZiwGoVuVAj(
                ipYTWVOPDpfJXeTFApPIgldytQSaUFdk, channels, rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.DjnmEmFIylXDvTfeYtLbwRKPMHUXFjho, 3, sdxdTSjnkAOjlGmltQHvLiHRDstMzpAP=1, DDRQlhrNSGpwTrokWitkZipdfbAqBFxv=DDRQlhrNSGpwTrokWitkZipdfbAqBFxv, fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc=fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc
            )
        else:
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.skip_connection = xwIQGNbJnSVpLrBBfhMLBchFpoolNzOe.XqmPajboESpTdLShIQpHOQZiwGoVuVAj(ipYTWVOPDpfJXeTFApPIgldytQSaUFdk, channels, rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.DjnmEmFIylXDvTfeYtLbwRKPMHUXFjho, 1, DDRQlhrNSGpwTrokWitkZipdfbAqBFxv=DDRQlhrNSGpwTrokWitkZipdfbAqBFxv, fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc=fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc)
    def lqBgIcSWZYylbCPjXksJWDguuSOqoPCJ(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, NECAaWUrFGIXcLimrerEYmxYIykQBfXb, cbvuxLJlTEiYpJEoytPnUgMhAcRHRwIE):
        return vcSlHLxBcVodHmZrzACHLEJuENMXjWTG(
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.NFbNMrWYGAqPnzmlcfuXjOSWmXVgbZMT, (NECAaWUrFGIXcLimrerEYmxYIykQBfXb, cbvuxLJlTEiYpJEoytPnUgMhAcRHRwIE), rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.parameters(), rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.TkHgGRFhDYRqyKuFvQRlKbpOBXUaEDVU
        )
    def NFbNMrWYGAqPnzmlcfuXjOSWmXVgbZMT(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, NECAaWUrFGIXcLimrerEYmxYIykQBfXb, cbvuxLJlTEiYpJEoytPnUgMhAcRHRwIE):
        if rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.updown:
            aXXGTekuTrsJXqWmaHIENjhRmydXLEIV, UgSPfpdOjavOkuRHVjJRYOswzqgseqrc = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.in_layers[:-1], rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.in_layers[-1]
            xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab = aXXGTekuTrsJXqWmaHIENjhRmydXLEIV(NECAaWUrFGIXcLimrerEYmxYIykQBfXb)
            xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.h_upd(xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab)
            NECAaWUrFGIXcLimrerEYmxYIykQBfXb = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.x_upd(NECAaWUrFGIXcLimrerEYmxYIykQBfXb)
            xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab = UgSPfpdOjavOkuRHVjJRYOswzqgseqrc(xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab)
        else:
            xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.in_layers(NECAaWUrFGIXcLimrerEYmxYIykQBfXb)
        HuwDLjbvJalYrDiOrBQJwuDjfQqhlhyg = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.emb_layers(cbvuxLJlTEiYpJEoytPnUgMhAcRHRwIE).type(xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab.DDRQlhrNSGpwTrokWitkZipdfbAqBFxv)
        while len(HuwDLjbvJalYrDiOrBQJwuDjfQqhlhyg.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg) < len(xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg):
            HuwDLjbvJalYrDiOrBQJwuDjfQqhlhyg = HuwDLjbvJalYrDiOrBQJwuDjfQqhlhyg[..., None]
        if rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.ihazehElCCwCXjMBaNMdYMBnXEUKZiVD:
            PdrhFpDoDSQUNGYkzwiSUjANogRCAnUi, erkRHMRWOTLKJGShnBUllKAdETjNuWRz = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.out_layers[0], rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.out_layers[1:]
            xmbXivThLFnawFPAJvIDBztziWsaDyEE, eYjswTGDmElddaoiSKnLRKnPgsfIHdGc = th.ebMwMGDmpDsmyMtCQfGxUhZuVHvTpavF(HuwDLjbvJalYrDiOrBQJwuDjfQqhlhyg, 2, yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk=1)
            xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab = PdrhFpDoDSQUNGYkzwiSUjANogRCAnUi(xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab) * (1 + xmbXivThLFnawFPAJvIDBztziWsaDyEE) + eYjswTGDmElddaoiSKnLRKnPgsfIHdGc
            xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab = erkRHMRWOTLKJGShnBUllKAdETjNuWRz(xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab)
        else:
            xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab = xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab + HuwDLjbvJalYrDiOrBQJwuDjfQqhlhyg
            xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.out_layers(xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab)
        return rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.skip_connection(NECAaWUrFGIXcLimrerEYmxYIykQBfXb) + xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab
class zGGBuzFwarRcjrVdvKsXbQZONUVfKAiA(nn.Module):
    def __init__(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk):
        super().__init__()
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk = yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk
    def lqBgIcSWZYylbCPjXksJWDguuSOqoPCJ(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz):
        return gjzRLJpCqzjvjCYIlAGlFiFZIQLazZsd(XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz, rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk)
class ECDCaNzfsUCStonxUHNJYFmsGbuTLSRS(nn.Module):
    def __init__(
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS,
        image_size,
        EbKSIFxpyCpzycRDApduouVsxspHzkTj,
        rfffeowUobVqguyCFHTDeTaijHAmTODl,
        DjnmEmFIylXDvTfeYtLbwRKPMHUXFjho,
        CCAXgmpIWICHAxdXRCbCjrvfPSDecjrB,
        fnGjYHqQPjLHiqvqzJoEFfKlYjtXwlEV,
        kcIxGCXrUvsLPSfmGoULGFzAthVmTXcA=0,
        PobbJiwtnxNwnEHqwlZzMzYFDrQuLuRE=(1, 2, 4, 8),
        jOostTwESugfvAylZrJTwVKiwgHfNemg=True,
        ipYTWVOPDpfJXeTFApPIgldytQSaUFdk=2,
        zwGEeMyeAIpgIqRmKFBmqOoJjGppGEtq=None,
        TkHgGRFhDYRqyKuFvQRlKbpOBXUaEDVU=False,
        HzaWhAqAbytRDBNdzYQQeTtjNGGUstsT=False,
        keUhCSnpGKMQazMnVXBhIUZfFyfjwEWp=False,
        WbSAuusmaEgbrureofeJezeXtfsVoscC=-1,
        num_head_channels=-1,
        GCnzBkfQgSsDmjgVHcytxSaoXsdQIGVs=-1,
        ihazehElCCwCXjMBaNMdYMBnXEUKZiVD=False,
        TyTQlPjBwYgItlBuhNWOxBQglapqYRXt=False,
        VMrqJDhbxmERmCYepAXgIUzOdbkIzndx=False,
        DqIoTEigRjcjZHmcxxSAedEQXxCjwxFB=False,    
        mvciuYyNHMqmFhQqZCFnjvXvgTuOnAAU=1,              
        FEAAZHeTRQEJCsYHCOEPpfOenpVZIhNT=None,                 
        NHEiPJISrktQvbPzAsEGcwxQibSjZqpo=None,                     
        SuXQmVmiJmhBfBymkmQFoPywSBByJxgG=True,
        bxZoDuqwYERKHMJbDKvQMoOVzkYUsfEW=None,
        TRFujbnWxYpAUeZVygnndzXoFNMuTCLb=None,
        IoMJDiqQpviQNxjpYtEOuDEgFMuxDSNg=False,
        PRCmYmLASLnRTlacrSLaZCNiipiIjyAo=False,
        fXHGlYkFilBYlIntaRCCiTGrHJqNqSCm=None,
        bNRNtGADYHWmhhfDRZvMDNGtMgvwCBHd=None,
        fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc=None,
        xwIQGNbJnSVpLrBBfhMLBchFpoolNzOe=quasar.ops,
    ):
        super().__init__()
        assert DqIoTEigRjcjZHmcxxSAedEQXxCjwxFB == True, "use_spatial_transformer has to be true"
        if DqIoTEigRjcjZHmcxxSAedEQXxCjwxFB:
            assert FEAAZHeTRQEJCsYHCOEPpfOenpVZIhNT is not None, 'Fool!! You forgot to include the dimension of your cross-attention conditioning...'
        if FEAAZHeTRQEJCsYHCOEPpfOenpVZIhNT is not None:
            assert DqIoTEigRjcjZHmcxxSAedEQXxCjwxFB, 'Fool!! You forgot to use the spatial transformer for your cross-attention conditioning...'
        if GCnzBkfQgSsDmjgVHcytxSaoXsdQIGVs == -1:
            GCnzBkfQgSsDmjgVHcytxSaoXsdQIGVs = WbSAuusmaEgbrureofeJezeXtfsVoscC
        if WbSAuusmaEgbrureofeJezeXtfsVoscC == -1:
            assert num_head_channels != -1, 'Either num_heads or num_head_channels has to be set'
        if num_head_channels == -1:
            assert WbSAuusmaEgbrureofeJezeXtfsVoscC != -1, 'Either num_heads or num_head_channels has to be set'
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.image_size = image_size
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.EbKSIFxpyCpzycRDApduouVsxspHzkTj = EbKSIFxpyCpzycRDApduouVsxspHzkTj
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.rfffeowUobVqguyCFHTDeTaijHAmTODl = rfffeowUobVqguyCFHTDeTaijHAmTODl
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.DjnmEmFIylXDvTfeYtLbwRKPMHUXFjho = DjnmEmFIylXDvTfeYtLbwRKPMHUXFjho
        if isinstance(mvciuYyNHMqmFhQqZCFnjvXvgTuOnAAU, int):
            mvciuYyNHMqmFhQqZCFnjvXvgTuOnAAU = len(PobbJiwtnxNwnEHqwlZzMzYFDrQuLuRE) * [mvciuYyNHMqmFhQqZCFnjvXvgTuOnAAU]
        if bNRNtGADYHWmhhfDRZvMDNGtMgvwCBHd is None:
            bNRNtGADYHWmhhfDRZvMDNGtMgvwCBHd =  mvciuYyNHMqmFhQqZCFnjvXvgTuOnAAU[-1]
        if isinstance(CCAXgmpIWICHAxdXRCbCjrvfPSDecjrB, int):
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.CCAXgmpIWICHAxdXRCbCjrvfPSDecjrB = len(PobbJiwtnxNwnEHqwlZzMzYFDrQuLuRE) * [CCAXgmpIWICHAxdXRCbCjrvfPSDecjrB]
        else:
            if len(CCAXgmpIWICHAxdXRCbCjrvfPSDecjrB) != len(PobbJiwtnxNwnEHqwlZzMzYFDrQuLuRE):
                raise ValueError("provide num_res_blocks either as an int (globally constant) or "
                                 "as a list/tuple (per-level) with the same length as channel_mult")
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.CCAXgmpIWICHAxdXRCbCjrvfPSDecjrB = CCAXgmpIWICHAxdXRCbCjrvfPSDecjrB
        if bxZoDuqwYERKHMJbDKvQMoOVzkYUsfEW is not None:
            assert len(bxZoDuqwYERKHMJbDKvQMoOVzkYUsfEW) == len(PobbJiwtnxNwnEHqwlZzMzYFDrQuLuRE)
        if TRFujbnWxYpAUeZVygnndzXoFNMuTCLb is not None:
            assert len(TRFujbnWxYpAUeZVygnndzXoFNMuTCLb) == len(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.CCAXgmpIWICHAxdXRCbCjrvfPSDecjrB)
            assert all(map(lambda HCXmerBqIMuTscBONzTGKYapYSxWTYHo: rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.CCAXgmpIWICHAxdXRCbCjrvfPSDecjrB[HCXmerBqIMuTscBONzTGKYapYSxWTYHo] >= TRFujbnWxYpAUeZVygnndzXoFNMuTCLb[HCXmerBqIMuTscBONzTGKYapYSxWTYHo], range(len(TRFujbnWxYpAUeZVygnndzXoFNMuTCLb))))
            print(f"Constructor of UNetModel received num_attention_blocks={num_attention_blocks}. "
                  f"This option has LESS priority than attention_resolutions {attention_resolutions}, "
                  f"i.e., in cases where num_attention_blocks[i] > 0 but 2**i not in attention_resolutions, "
                  f"attention will still not be set.")
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.fnGjYHqQPjLHiqvqzJoEFfKlYjtXwlEV = fnGjYHqQPjLHiqvqzJoEFfKlYjtXwlEV
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.kcIxGCXrUvsLPSfmGoULGFzAthVmTXcA = kcIxGCXrUvsLPSfmGoULGFzAthVmTXcA
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.PobbJiwtnxNwnEHqwlZzMzYFDrQuLuRE = PobbJiwtnxNwnEHqwlZzMzYFDrQuLuRE
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.jOostTwESugfvAylZrJTwVKiwgHfNemg = jOostTwESugfvAylZrJTwVKiwgHfNemg
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.zwGEeMyeAIpgIqRmKFBmqOoJjGppGEtq = zwGEeMyeAIpgIqRmKFBmqOoJjGppGEtq
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.TkHgGRFhDYRqyKuFvQRlKbpOBXUaEDVU = TkHgGRFhDYRqyKuFvQRlKbpOBXUaEDVU
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.DDRQlhrNSGpwTrokWitkZipdfbAqBFxv = th.float16 if HzaWhAqAbytRDBNdzYQQeTtjNGGUstsT else th.float32
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.DDRQlhrNSGpwTrokWitkZipdfbAqBFxv = th.bfloat16 if keUhCSnpGKMQazMnVXBhIUZfFyfjwEWp else rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.DDRQlhrNSGpwTrokWitkZipdfbAqBFxv
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.WbSAuusmaEgbrureofeJezeXtfsVoscC = WbSAuusmaEgbrureofeJezeXtfsVoscC
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.num_head_channels = num_head_channels
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.GCnzBkfQgSsDmjgVHcytxSaoXsdQIGVs = GCnzBkfQgSsDmjgVHcytxSaoXsdQIGVs
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.predict_codebook_ids = NHEiPJISrktQvbPzAsEGcwxQibSjZqpo is not None
        TJtWhnWNhUyDzzDREHTjcgkGTiVvhEoR = rfffeowUobVqguyCFHTDeTaijHAmTODl * 4
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.time_embed = nn.Sequential(
            xwIQGNbJnSVpLrBBfhMLBchFpoolNzOe.DhMcMyEvvzmWIEJojbQeGHlzfZKiPzHO(rfffeowUobVqguyCFHTDeTaijHAmTODl, TJtWhnWNhUyDzzDREHTjcgkGTiVvhEoR, DDRQlhrNSGpwTrokWitkZipdfbAqBFxv=rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.DDRQlhrNSGpwTrokWitkZipdfbAqBFxv, fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc=fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc),
            nn.XHAfRvdQzGhVBUIWzxCQjrhAiQInnRoY(),
            xwIQGNbJnSVpLrBBfhMLBchFpoolNzOe.DhMcMyEvvzmWIEJojbQeGHlzfZKiPzHO(TJtWhnWNhUyDzzDREHTjcgkGTiVvhEoR, TJtWhnWNhUyDzzDREHTjcgkGTiVvhEoR, DDRQlhrNSGpwTrokWitkZipdfbAqBFxv=rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.DDRQlhrNSGpwTrokWitkZipdfbAqBFxv, fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc=fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc),
        )
        if rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.zwGEeMyeAIpgIqRmKFBmqOoJjGppGEtq is not None:
            if isinstance(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.zwGEeMyeAIpgIqRmKFBmqOoJjGppGEtq, int):
                rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.label_emb = nn.Embedding(zwGEeMyeAIpgIqRmKFBmqOoJjGppGEtq, TJtWhnWNhUyDzzDREHTjcgkGTiVvhEoR)
            elif rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.zwGEeMyeAIpgIqRmKFBmqOoJjGppGEtq == "continuous":
                print("setting up linear c_adm embedding layer")
                rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.label_emb = nn.DhMcMyEvvzmWIEJojbQeGHlzfZKiPzHO(1, TJtWhnWNhUyDzzDREHTjcgkGTiVvhEoR)
            elif rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.zwGEeMyeAIpgIqRmKFBmqOoJjGppGEtq == "sequential":
                assert fXHGlYkFilBYlIntaRCCiTGrHJqNqSCm is not None
                rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.label_emb = nn.Sequential(
                    nn.Sequential(
                        xwIQGNbJnSVpLrBBfhMLBchFpoolNzOe.DhMcMyEvvzmWIEJojbQeGHlzfZKiPzHO(fXHGlYkFilBYlIntaRCCiTGrHJqNqSCm, TJtWhnWNhUyDzzDREHTjcgkGTiVvhEoR, DDRQlhrNSGpwTrokWitkZipdfbAqBFxv=rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.DDRQlhrNSGpwTrokWitkZipdfbAqBFxv, fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc=fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc),
                        nn.XHAfRvdQzGhVBUIWzxCQjrhAiQInnRoY(),
                        xwIQGNbJnSVpLrBBfhMLBchFpoolNzOe.DhMcMyEvvzmWIEJojbQeGHlzfZKiPzHO(TJtWhnWNhUyDzzDREHTjcgkGTiVvhEoR, TJtWhnWNhUyDzzDREHTjcgkGTiVvhEoR, DDRQlhrNSGpwTrokWitkZipdfbAqBFxv=rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.DDRQlhrNSGpwTrokWitkZipdfbAqBFxv, fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc=fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc),
                    )
                )
            else:
                raise ValueError()
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.input_blocks = nn.ModuleList(
            [
                ETGhHLqpqtlhedBMHvqXdpnYyyTCWDrS(
                    xwIQGNbJnSVpLrBBfhMLBchFpoolNzOe.XqmPajboESpTdLShIQpHOQZiwGoVuVAj(ipYTWVOPDpfJXeTFApPIgldytQSaUFdk, EbKSIFxpyCpzycRDApduouVsxspHzkTj, rfffeowUobVqguyCFHTDeTaijHAmTODl, 3, sdxdTSjnkAOjlGmltQHvLiHRDstMzpAP=1, DDRQlhrNSGpwTrokWitkZipdfbAqBFxv=rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.DDRQlhrNSGpwTrokWitkZipdfbAqBFxv, fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc=fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc)
                )
            ]
        )
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS._feature_size = rfffeowUobVqguyCFHTDeTaijHAmTODl
        XODsQsqEQVWQmaUYhGgsqyaWoJCgGlap = [rfffeowUobVqguyCFHTDeTaijHAmTODl]
        PCiQtOeHrYsokBqtFxBbpDPnOjZourbJ = rfffeowUobVqguyCFHTDeTaijHAmTODl
        bKTOPCkNnYlTtvyGohgLIoPMQbrflxmi = 1
        for QGZhPqtOMdRtNNTWfnQtIxGkLaBzolOd, XVFRnfSDhyHpjboFTGKCmAMvovOXxqYP in enumerate(PobbJiwtnxNwnEHqwlZzMzYFDrQuLuRE):
            for QHVHwxnivSirVrVqgJLXXPIBHKHvEzbG in range(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.CCAXgmpIWICHAxdXRCbCjrvfPSDecjrB[QGZhPqtOMdRtNNTWfnQtIxGkLaBzolOd]):
                YLFvlrIxIOsplmnxmtPcOLtJTpiskWMv = [
                    WyEaQvHmxeWCTWupmPIsgcbcMkcKnPVN(
                        PCiQtOeHrYsokBqtFxBbpDPnOjZourbJ,
                        TJtWhnWNhUyDzzDREHTjcgkGTiVvhEoR,
                        kcIxGCXrUvsLPSfmGoULGFzAthVmTXcA,
                        DjnmEmFIylXDvTfeYtLbwRKPMHUXFjho=XVFRnfSDhyHpjboFTGKCmAMvovOXxqYP * rfffeowUobVqguyCFHTDeTaijHAmTODl,
                        ipYTWVOPDpfJXeTFApPIgldytQSaUFdk=ipYTWVOPDpfJXeTFApPIgldytQSaUFdk,
                        TkHgGRFhDYRqyKuFvQRlKbpOBXUaEDVU=TkHgGRFhDYRqyKuFvQRlKbpOBXUaEDVU,
                        ihazehElCCwCXjMBaNMdYMBnXEUKZiVD=ihazehElCCwCXjMBaNMdYMBnXEUKZiVD,
                        DDRQlhrNSGpwTrokWitkZipdfbAqBFxv=rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.DDRQlhrNSGpwTrokWitkZipdfbAqBFxv,
                        fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc=fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc,
                        xwIQGNbJnSVpLrBBfhMLBchFpoolNzOe=xwIQGNbJnSVpLrBBfhMLBchFpoolNzOe,
                    )
                ]
                PCiQtOeHrYsokBqtFxBbpDPnOjZourbJ = XVFRnfSDhyHpjboFTGKCmAMvovOXxqYP * rfffeowUobVqguyCFHTDeTaijHAmTODl
                if bKTOPCkNnYlTtvyGohgLIoPMQbrflxmi in fnGjYHqQPjLHiqvqzJoEFfKlYjtXwlEV:
                    if num_head_channels == -1:
                        QiYWcbRqbdDfAfhjULhYwmIlOStjgPlv = PCiQtOeHrYsokBqtFxBbpDPnOjZourbJ // WbSAuusmaEgbrureofeJezeXtfsVoscC
                    else:
                        WbSAuusmaEgbrureofeJezeXtfsVoscC = PCiQtOeHrYsokBqtFxBbpDPnOjZourbJ // num_head_channels
                        QiYWcbRqbdDfAfhjULhYwmIlOStjgPlv = num_head_channels
                    if SuXQmVmiJmhBfBymkmQFoPywSBByJxgG:
                        QiYWcbRqbdDfAfhjULhYwmIlOStjgPlv = PCiQtOeHrYsokBqtFxBbpDPnOjZourbJ // WbSAuusmaEgbrureofeJezeXtfsVoscC if DqIoTEigRjcjZHmcxxSAedEQXxCjwxFB else num_head_channels
                    if exists(bxZoDuqwYERKHMJbDKvQMoOVzkYUsfEW):
                        ScYwEbQtDNjWKaCbFCgtVUtLrqNSqQxZ = bxZoDuqwYERKHMJbDKvQMoOVzkYUsfEW[QGZhPqtOMdRtNNTWfnQtIxGkLaBzolOd]
                    else:
                        ScYwEbQtDNjWKaCbFCgtVUtLrqNSqQxZ = False
                    if not exists(TRFujbnWxYpAUeZVygnndzXoFNMuTCLb) or QHVHwxnivSirVrVqgJLXXPIBHKHvEzbG < TRFujbnWxYpAUeZVygnndzXoFNMuTCLb[QGZhPqtOMdRtNNTWfnQtIxGkLaBzolOd]:
                        YLFvlrIxIOsplmnxmtPcOLtJTpiskWMv.append(CvuNifYqMqjsNqfVaEEpwROqJiOUCfhu(
                                PCiQtOeHrYsokBqtFxBbpDPnOjZourbJ, WbSAuusmaEgbrureofeJezeXtfsVoscC, QiYWcbRqbdDfAfhjULhYwmIlOStjgPlv, JtnlCSDzHOgtbZVTfQMidKPjmOFZfzZX=mvciuYyNHMqmFhQqZCFnjvXvgTuOnAAU[QGZhPqtOMdRtNNTWfnQtIxGkLaBzolOd], FEAAZHeTRQEJCsYHCOEPpfOenpVZIhNT=FEAAZHeTRQEJCsYHCOEPpfOenpVZIhNT,
                                ylReNVtjXdQbeAwJXhTkOjiHrFPToKDa=ScYwEbQtDNjWKaCbFCgtVUtLrqNSqQxZ, use_linear=PRCmYmLASLnRTlacrSLaZCNiipiIjyAo,
                                TkHgGRFhDYRqyKuFvQRlKbpOBXUaEDVU=TkHgGRFhDYRqyKuFvQRlKbpOBXUaEDVU, DDRQlhrNSGpwTrokWitkZipdfbAqBFxv=rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.DDRQlhrNSGpwTrokWitkZipdfbAqBFxv, fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc=fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc, xwIQGNbJnSVpLrBBfhMLBchFpoolNzOe=xwIQGNbJnSVpLrBBfhMLBchFpoolNzOe
                            )
                        )
                rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.input_blocks.append(ETGhHLqpqtlhedBMHvqXdpnYyyTCWDrS(*YLFvlrIxIOsplmnxmtPcOLtJTpiskWMv))
                rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS._feature_size += PCiQtOeHrYsokBqtFxBbpDPnOjZourbJ
                XODsQsqEQVWQmaUYhGgsqyaWoJCgGlap.append(PCiQtOeHrYsokBqtFxBbpDPnOjZourbJ)
            if QGZhPqtOMdRtNNTWfnQtIxGkLaBzolOd != len(PobbJiwtnxNwnEHqwlZzMzYFDrQuLuRE) - 1:
                VAkEsdMDwAEDPzAuJymQaRUNIxlnDSEu = PCiQtOeHrYsokBqtFxBbpDPnOjZourbJ
                rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.input_blocks.append(
                    ETGhHLqpqtlhedBMHvqXdpnYyyTCWDrS(
                        WyEaQvHmxeWCTWupmPIsgcbcMkcKnPVN(
                            PCiQtOeHrYsokBqtFxBbpDPnOjZourbJ,
                            TJtWhnWNhUyDzzDREHTjcgkGTiVvhEoR,
                            kcIxGCXrUvsLPSfmGoULGFzAthVmTXcA,
                            DjnmEmFIylXDvTfeYtLbwRKPMHUXFjho=VAkEsdMDwAEDPzAuJymQaRUNIxlnDSEu,
                            ipYTWVOPDpfJXeTFApPIgldytQSaUFdk=ipYTWVOPDpfJXeTFApPIgldytQSaUFdk,
                            TkHgGRFhDYRqyKuFvQRlKbpOBXUaEDVU=TkHgGRFhDYRqyKuFvQRlKbpOBXUaEDVU,
                            ihazehElCCwCXjMBaNMdYMBnXEUKZiVD=ihazehElCCwCXjMBaNMdYMBnXEUKZiVD,
                            PKmeubCqZPUpSfmqJozYuvYsQsIMTIOn=True,
                            DDRQlhrNSGpwTrokWitkZipdfbAqBFxv=rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.DDRQlhrNSGpwTrokWitkZipdfbAqBFxv,
                            fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc=fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc,
                            xwIQGNbJnSVpLrBBfhMLBchFpoolNzOe=xwIQGNbJnSVpLrBBfhMLBchFpoolNzOe
                        )
                        if TyTQlPjBwYgItlBuhNWOxBQglapqYRXt
                        else LpwKTfRyOAITGEdvwhtCdMnNRMEQUkUG(
                            PCiQtOeHrYsokBqtFxBbpDPnOjZourbJ, jOostTwESugfvAylZrJTwVKiwgHfNemg, ipYTWVOPDpfJXeTFApPIgldytQSaUFdk=ipYTWVOPDpfJXeTFApPIgldytQSaUFdk, DjnmEmFIylXDvTfeYtLbwRKPMHUXFjho=VAkEsdMDwAEDPzAuJymQaRUNIxlnDSEu, DDRQlhrNSGpwTrokWitkZipdfbAqBFxv=rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.DDRQlhrNSGpwTrokWitkZipdfbAqBFxv, fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc=fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc, xwIQGNbJnSVpLrBBfhMLBchFpoolNzOe=xwIQGNbJnSVpLrBBfhMLBchFpoolNzOe
                        )
                    )
                )
                PCiQtOeHrYsokBqtFxBbpDPnOjZourbJ = VAkEsdMDwAEDPzAuJymQaRUNIxlnDSEu
                XODsQsqEQVWQmaUYhGgsqyaWoJCgGlap.append(PCiQtOeHrYsokBqtFxBbpDPnOjZourbJ)
                bKTOPCkNnYlTtvyGohgLIoPMQbrflxmi *= 2
                rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS._feature_size += PCiQtOeHrYsokBqtFxBbpDPnOjZourbJ
        if num_head_channels == -1:
            QiYWcbRqbdDfAfhjULhYwmIlOStjgPlv = PCiQtOeHrYsokBqtFxBbpDPnOjZourbJ // WbSAuusmaEgbrureofeJezeXtfsVoscC
        else:
            WbSAuusmaEgbrureofeJezeXtfsVoscC = PCiQtOeHrYsokBqtFxBbpDPnOjZourbJ // num_head_channels
            QiYWcbRqbdDfAfhjULhYwmIlOStjgPlv = num_head_channels
        if SuXQmVmiJmhBfBymkmQFoPywSBByJxgG:
            QiYWcbRqbdDfAfhjULhYwmIlOStjgPlv = PCiQtOeHrYsokBqtFxBbpDPnOjZourbJ // WbSAuusmaEgbrureofeJezeXtfsVoscC if DqIoTEigRjcjZHmcxxSAedEQXxCjwxFB else num_head_channels
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.middle_block = ETGhHLqpqtlhedBMHvqXdpnYyyTCWDrS(
            WyEaQvHmxeWCTWupmPIsgcbcMkcKnPVN(
                PCiQtOeHrYsokBqtFxBbpDPnOjZourbJ,
                TJtWhnWNhUyDzzDREHTjcgkGTiVvhEoR,
                kcIxGCXrUvsLPSfmGoULGFzAthVmTXcA,
                ipYTWVOPDpfJXeTFApPIgldytQSaUFdk=ipYTWVOPDpfJXeTFApPIgldytQSaUFdk,
                TkHgGRFhDYRqyKuFvQRlKbpOBXUaEDVU=TkHgGRFhDYRqyKuFvQRlKbpOBXUaEDVU,
                ihazehElCCwCXjMBaNMdYMBnXEUKZiVD=ihazehElCCwCXjMBaNMdYMBnXEUKZiVD,
                DDRQlhrNSGpwTrokWitkZipdfbAqBFxv=rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.DDRQlhrNSGpwTrokWitkZipdfbAqBFxv,
                fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc=fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc,
                xwIQGNbJnSVpLrBBfhMLBchFpoolNzOe=xwIQGNbJnSVpLrBBfhMLBchFpoolNzOe
            ),
            CvuNifYqMqjsNqfVaEEpwROqJiOUCfhu(  
                            PCiQtOeHrYsokBqtFxBbpDPnOjZourbJ, WbSAuusmaEgbrureofeJezeXtfsVoscC, QiYWcbRqbdDfAfhjULhYwmIlOStjgPlv, JtnlCSDzHOgtbZVTfQMidKPjmOFZfzZX=bNRNtGADYHWmhhfDRZvMDNGtMgvwCBHd, FEAAZHeTRQEJCsYHCOEPpfOenpVZIhNT=FEAAZHeTRQEJCsYHCOEPpfOenpVZIhNT,
                            ylReNVtjXdQbeAwJXhTkOjiHrFPToKDa=IoMJDiqQpviQNxjpYtEOuDEgFMuxDSNg, use_linear=PRCmYmLASLnRTlacrSLaZCNiipiIjyAo,
                            TkHgGRFhDYRqyKuFvQRlKbpOBXUaEDVU=TkHgGRFhDYRqyKuFvQRlKbpOBXUaEDVU, DDRQlhrNSGpwTrokWitkZipdfbAqBFxv=rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.DDRQlhrNSGpwTrokWitkZipdfbAqBFxv, fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc=fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc, xwIQGNbJnSVpLrBBfhMLBchFpoolNzOe=xwIQGNbJnSVpLrBBfhMLBchFpoolNzOe
                        ),
            WyEaQvHmxeWCTWupmPIsgcbcMkcKnPVN(
                PCiQtOeHrYsokBqtFxBbpDPnOjZourbJ,
                TJtWhnWNhUyDzzDREHTjcgkGTiVvhEoR,
                kcIxGCXrUvsLPSfmGoULGFzAthVmTXcA,
                ipYTWVOPDpfJXeTFApPIgldytQSaUFdk=ipYTWVOPDpfJXeTFApPIgldytQSaUFdk,
                TkHgGRFhDYRqyKuFvQRlKbpOBXUaEDVU=TkHgGRFhDYRqyKuFvQRlKbpOBXUaEDVU,
                ihazehElCCwCXjMBaNMdYMBnXEUKZiVD=ihazehElCCwCXjMBaNMdYMBnXEUKZiVD,
                DDRQlhrNSGpwTrokWitkZipdfbAqBFxv=rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.DDRQlhrNSGpwTrokWitkZipdfbAqBFxv,
                fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc=fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc,
                xwIQGNbJnSVpLrBBfhMLBchFpoolNzOe=xwIQGNbJnSVpLrBBfhMLBchFpoolNzOe
            ),
        )
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS._feature_size += PCiQtOeHrYsokBqtFxBbpDPnOjZourbJ
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.output_blocks = nn.ModuleList([])
        for QGZhPqtOMdRtNNTWfnQtIxGkLaBzolOd, XVFRnfSDhyHpjboFTGKCmAMvovOXxqYP in list(enumerate(PobbJiwtnxNwnEHqwlZzMzYFDrQuLuRE))[::-1]:
            for HCXmerBqIMuTscBONzTGKYapYSxWTYHo in range(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.CCAXgmpIWICHAxdXRCbCjrvfPSDecjrB[QGZhPqtOMdRtNNTWfnQtIxGkLaBzolOd] + 1):
                mjRKBOfHqIJfkEnyqyePYVkZExVPYhYK = XODsQsqEQVWQmaUYhGgsqyaWoJCgGlap.pop()
                YLFvlrIxIOsplmnxmtPcOLtJTpiskWMv = [
                    WyEaQvHmxeWCTWupmPIsgcbcMkcKnPVN(
                        PCiQtOeHrYsokBqtFxBbpDPnOjZourbJ + mjRKBOfHqIJfkEnyqyePYVkZExVPYhYK,
                        TJtWhnWNhUyDzzDREHTjcgkGTiVvhEoR,
                        kcIxGCXrUvsLPSfmGoULGFzAthVmTXcA,
                        DjnmEmFIylXDvTfeYtLbwRKPMHUXFjho=rfffeowUobVqguyCFHTDeTaijHAmTODl * XVFRnfSDhyHpjboFTGKCmAMvovOXxqYP,
                        ipYTWVOPDpfJXeTFApPIgldytQSaUFdk=ipYTWVOPDpfJXeTFApPIgldytQSaUFdk,
                        TkHgGRFhDYRqyKuFvQRlKbpOBXUaEDVU=TkHgGRFhDYRqyKuFvQRlKbpOBXUaEDVU,
                        ihazehElCCwCXjMBaNMdYMBnXEUKZiVD=ihazehElCCwCXjMBaNMdYMBnXEUKZiVD,
                        DDRQlhrNSGpwTrokWitkZipdfbAqBFxv=rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.DDRQlhrNSGpwTrokWitkZipdfbAqBFxv,
                        fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc=fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc,
                        xwIQGNbJnSVpLrBBfhMLBchFpoolNzOe=xwIQGNbJnSVpLrBBfhMLBchFpoolNzOe
                    )
                ]
                PCiQtOeHrYsokBqtFxBbpDPnOjZourbJ = rfffeowUobVqguyCFHTDeTaijHAmTODl * XVFRnfSDhyHpjboFTGKCmAMvovOXxqYP
                if bKTOPCkNnYlTtvyGohgLIoPMQbrflxmi in fnGjYHqQPjLHiqvqzJoEFfKlYjtXwlEV:
                    if num_head_channels == -1:
                        QiYWcbRqbdDfAfhjULhYwmIlOStjgPlv = PCiQtOeHrYsokBqtFxBbpDPnOjZourbJ // WbSAuusmaEgbrureofeJezeXtfsVoscC
                    else:
                        WbSAuusmaEgbrureofeJezeXtfsVoscC = PCiQtOeHrYsokBqtFxBbpDPnOjZourbJ // num_head_channels
                        QiYWcbRqbdDfAfhjULhYwmIlOStjgPlv = num_head_channels
                    if SuXQmVmiJmhBfBymkmQFoPywSBByJxgG:
                        QiYWcbRqbdDfAfhjULhYwmIlOStjgPlv = PCiQtOeHrYsokBqtFxBbpDPnOjZourbJ // WbSAuusmaEgbrureofeJezeXtfsVoscC if DqIoTEigRjcjZHmcxxSAedEQXxCjwxFB else num_head_channels
                    if exists(bxZoDuqwYERKHMJbDKvQMoOVzkYUsfEW):
                        ScYwEbQtDNjWKaCbFCgtVUtLrqNSqQxZ = bxZoDuqwYERKHMJbDKvQMoOVzkYUsfEW[QGZhPqtOMdRtNNTWfnQtIxGkLaBzolOd]
                    else:
                        ScYwEbQtDNjWKaCbFCgtVUtLrqNSqQxZ = False
                    if not exists(TRFujbnWxYpAUeZVygnndzXoFNMuTCLb) or HCXmerBqIMuTscBONzTGKYapYSxWTYHo < TRFujbnWxYpAUeZVygnndzXoFNMuTCLb[QGZhPqtOMdRtNNTWfnQtIxGkLaBzolOd]:
                        YLFvlrIxIOsplmnxmtPcOLtJTpiskWMv.append(
                            CvuNifYqMqjsNqfVaEEpwROqJiOUCfhu(
                                PCiQtOeHrYsokBqtFxBbpDPnOjZourbJ, WbSAuusmaEgbrureofeJezeXtfsVoscC, QiYWcbRqbdDfAfhjULhYwmIlOStjgPlv, JtnlCSDzHOgtbZVTfQMidKPjmOFZfzZX=mvciuYyNHMqmFhQqZCFnjvXvgTuOnAAU[QGZhPqtOMdRtNNTWfnQtIxGkLaBzolOd], FEAAZHeTRQEJCsYHCOEPpfOenpVZIhNT=FEAAZHeTRQEJCsYHCOEPpfOenpVZIhNT,
                                ylReNVtjXdQbeAwJXhTkOjiHrFPToKDa=ScYwEbQtDNjWKaCbFCgtVUtLrqNSqQxZ, use_linear=PRCmYmLASLnRTlacrSLaZCNiipiIjyAo,
                                TkHgGRFhDYRqyKuFvQRlKbpOBXUaEDVU=TkHgGRFhDYRqyKuFvQRlKbpOBXUaEDVU, DDRQlhrNSGpwTrokWitkZipdfbAqBFxv=rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.DDRQlhrNSGpwTrokWitkZipdfbAqBFxv, fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc=fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc, xwIQGNbJnSVpLrBBfhMLBchFpoolNzOe=xwIQGNbJnSVpLrBBfhMLBchFpoolNzOe
                            )
                        )
                if QGZhPqtOMdRtNNTWfnQtIxGkLaBzolOd and HCXmerBqIMuTscBONzTGKYapYSxWTYHo == rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.CCAXgmpIWICHAxdXRCbCjrvfPSDecjrB[QGZhPqtOMdRtNNTWfnQtIxGkLaBzolOd]:
                    VAkEsdMDwAEDPzAuJymQaRUNIxlnDSEu = PCiQtOeHrYsokBqtFxBbpDPnOjZourbJ
                    YLFvlrIxIOsplmnxmtPcOLtJTpiskWMv.append(
                        WyEaQvHmxeWCTWupmPIsgcbcMkcKnPVN(
                            PCiQtOeHrYsokBqtFxBbpDPnOjZourbJ,
                            TJtWhnWNhUyDzzDREHTjcgkGTiVvhEoR,
                            kcIxGCXrUvsLPSfmGoULGFzAthVmTXcA,
                            DjnmEmFIylXDvTfeYtLbwRKPMHUXFjho=VAkEsdMDwAEDPzAuJymQaRUNIxlnDSEu,
                            ipYTWVOPDpfJXeTFApPIgldytQSaUFdk=ipYTWVOPDpfJXeTFApPIgldytQSaUFdk,
                            TkHgGRFhDYRqyKuFvQRlKbpOBXUaEDVU=TkHgGRFhDYRqyKuFvQRlKbpOBXUaEDVU,
                            ihazehElCCwCXjMBaNMdYMBnXEUKZiVD=ihazehElCCwCXjMBaNMdYMBnXEUKZiVD,
                            kvJZslyswPMVzCnLtIoKrkpdfusdzxSS=True,
                            DDRQlhrNSGpwTrokWitkZipdfbAqBFxv=rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.DDRQlhrNSGpwTrokWitkZipdfbAqBFxv,
                            fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc=fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc,
                            xwIQGNbJnSVpLrBBfhMLBchFpoolNzOe=xwIQGNbJnSVpLrBBfhMLBchFpoolNzOe
                        )
                        if TyTQlPjBwYgItlBuhNWOxBQglapqYRXt
                        else kjruhryvXAQxnjJDeOXqTJbBrTkRFQSk(PCiQtOeHrYsokBqtFxBbpDPnOjZourbJ, jOostTwESugfvAylZrJTwVKiwgHfNemg, ipYTWVOPDpfJXeTFApPIgldytQSaUFdk=ipYTWVOPDpfJXeTFApPIgldytQSaUFdk, DjnmEmFIylXDvTfeYtLbwRKPMHUXFjho=VAkEsdMDwAEDPzAuJymQaRUNIxlnDSEu, DDRQlhrNSGpwTrokWitkZipdfbAqBFxv=rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.DDRQlhrNSGpwTrokWitkZipdfbAqBFxv, fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc=fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc, xwIQGNbJnSVpLrBBfhMLBchFpoolNzOe=xwIQGNbJnSVpLrBBfhMLBchFpoolNzOe)
                    )
                    bKTOPCkNnYlTtvyGohgLIoPMQbrflxmi //= 2
                rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.output_blocks.append(ETGhHLqpqtlhedBMHvqXdpnYyyTCWDrS(*YLFvlrIxIOsplmnxmtPcOLtJTpiskWMv))
                rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS._feature_size += PCiQtOeHrYsokBqtFxBbpDPnOjZourbJ
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.iqymPVpxyjOWChGwBkTemSzHJbnJdAIz = nn.Sequential(
            nn.GroupNorm(32, PCiQtOeHrYsokBqtFxBbpDPnOjZourbJ, DDRQlhrNSGpwTrokWitkZipdfbAqBFxv=rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.DDRQlhrNSGpwTrokWitkZipdfbAqBFxv, fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc=fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc),
            nn.XHAfRvdQzGhVBUIWzxCQjrhAiQInnRoY(),
            TVrUNiPGCtAmXFOUoqodGJnRgbvoldNA(xwIQGNbJnSVpLrBBfhMLBchFpoolNzOe.XqmPajboESpTdLShIQpHOQZiwGoVuVAj(ipYTWVOPDpfJXeTFApPIgldytQSaUFdk, rfffeowUobVqguyCFHTDeTaijHAmTODl, DjnmEmFIylXDvTfeYtLbwRKPMHUXFjho, 3, sdxdTSjnkAOjlGmltQHvLiHRDstMzpAP=1, DDRQlhrNSGpwTrokWitkZipdfbAqBFxv=rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.DDRQlhrNSGpwTrokWitkZipdfbAqBFxv, fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc=fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc)),
        )
        if rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.predict_codebook_ids:
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.id_predictor = nn.Sequential(
            nn.GroupNorm(32, PCiQtOeHrYsokBqtFxBbpDPnOjZourbJ, DDRQlhrNSGpwTrokWitkZipdfbAqBFxv=rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.DDRQlhrNSGpwTrokWitkZipdfbAqBFxv, fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc=fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc),
            xwIQGNbJnSVpLrBBfhMLBchFpoolNzOe.XqmPajboESpTdLShIQpHOQZiwGoVuVAj(ipYTWVOPDpfJXeTFApPIgldytQSaUFdk, rfffeowUobVqguyCFHTDeTaijHAmTODl, NHEiPJISrktQvbPzAsEGcwxQibSjZqpo, 1, DDRQlhrNSGpwTrokWitkZipdfbAqBFxv=rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.DDRQlhrNSGpwTrokWitkZipdfbAqBFxv, fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc=fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc),
        )
    def lqBgIcSWZYylbCPjXksJWDguuSOqoPCJ(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, NECAaWUrFGIXcLimrerEYmxYIykQBfXb, iaqNqpReXPEdYpNiyUIejEPLCqtbtedA=None, tRdCjhUPYVVxnSEkGmJIHWRitDXRXSZS=None, ZljqvWVaiqYAYdTFzQHSTXFDKwgstKaW=None, lxwsNGReZsRzPAGinnJJBaOYnaZlIssl=None, transformer_options={}, **kwargs):
        transformer_options["original_shape"] = list(NECAaWUrFGIXcLimrerEYmxYIykQBfXb.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg)
        transformer_options["current_index"] = 0
        assert (ZljqvWVaiqYAYdTFzQHSTXFDKwgstKaW is not None) == (
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.zwGEeMyeAIpgIqRmKFBmqOoJjGppGEtq is not None
        ), "must specify y if and only if the model is class-conditional"
        omGAnSaAXbgvwNbvtUsYicLqgJqNBgst = []
        lrHpXVKxDdNMqlsYwiglUaoDzgYScUcl = gjzRLJpCqzjvjCYIlAGlFiFZIQLazZsd(iaqNqpReXPEdYpNiyUIejEPLCqtbtedA, rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.rfffeowUobVqguyCFHTDeTaijHAmTODl, repeat_only=False).sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.DDRQlhrNSGpwTrokWitkZipdfbAqBFxv)
        cbvuxLJlTEiYpJEoytPnUgMhAcRHRwIE = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.time_embed(lrHpXVKxDdNMqlsYwiglUaoDzgYScUcl)
        if rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.zwGEeMyeAIpgIqRmKFBmqOoJjGppGEtq is not None:
            assert ZljqvWVaiqYAYdTFzQHSTXFDKwgstKaW.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[0] == NECAaWUrFGIXcLimrerEYmxYIykQBfXb.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[0]
            cbvuxLJlTEiYpJEoytPnUgMhAcRHRwIE = cbvuxLJlTEiYpJEoytPnUgMhAcRHRwIE + rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.label_emb(ZljqvWVaiqYAYdTFzQHSTXFDKwgstKaW)
        xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab = NECAaWUrFGIXcLimrerEYmxYIykQBfXb.type(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.DDRQlhrNSGpwTrokWitkZipdfbAqBFxv)
        for id, FRIBQCDfDDxIonplwxvPCicvOmmOgYPC in enumerate(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.input_blocks):
            transformer_options["block"] = ("input", id)
            xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab = lgcRKzdVlZLqUAtcHVZRPLwLobDmukAq(FRIBQCDfDDxIonplwxvPCicvOmmOgYPC, xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab, cbvuxLJlTEiYpJEoytPnUgMhAcRHRwIE, tRdCjhUPYVVxnSEkGmJIHWRitDXRXSZS, transformer_options)
            if lxwsNGReZsRzPAGinnJJBaOYnaZlIssl is not None and 'input' in lxwsNGReZsRzPAGinnJJBaOYnaZlIssl and len(lxwsNGReZsRzPAGinnJJBaOYnaZlIssl['input']) > 0:
                KlAKNBDNwzXcDoVQDPbFMpDaCXwgpTpW = lxwsNGReZsRzPAGinnJJBaOYnaZlIssl['input'].pop()
                if KlAKNBDNwzXcDoVQDPbFMpDaCXwgpTpW is not None:
                    xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab += KlAKNBDNwzXcDoVQDPbFMpDaCXwgpTpW
            omGAnSaAXbgvwNbvtUsYicLqgJqNBgst.append(xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab)
        transformer_options["block"] = ("middle", 0)
        xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab = lgcRKzdVlZLqUAtcHVZRPLwLobDmukAq(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.middle_block, xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab, cbvuxLJlTEiYpJEoytPnUgMhAcRHRwIE, tRdCjhUPYVVxnSEkGmJIHWRitDXRXSZS, transformer_options)
        if lxwsNGReZsRzPAGinnJJBaOYnaZlIssl is not None and 'middle' in lxwsNGReZsRzPAGinnJJBaOYnaZlIssl and len(lxwsNGReZsRzPAGinnJJBaOYnaZlIssl['middle']) > 0:
            KlAKNBDNwzXcDoVQDPbFMpDaCXwgpTpW = lxwsNGReZsRzPAGinnJJBaOYnaZlIssl['middle'].pop()
            if KlAKNBDNwzXcDoVQDPbFMpDaCXwgpTpW is not None:
                xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab += KlAKNBDNwzXcDoVQDPbFMpDaCXwgpTpW
        for id, FRIBQCDfDDxIonplwxvPCicvOmmOgYPC in enumerate(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.output_blocks):
            transformer_options["block"] = ("output", id)
            cyVtyoMONSPBlqSlWoufOPfgvyJAdKec = omGAnSaAXbgvwNbvtUsYicLqgJqNBgst.pop()
            if lxwsNGReZsRzPAGinnJJBaOYnaZlIssl is not None and 'output' in lxwsNGReZsRzPAGinnJJBaOYnaZlIssl and len(lxwsNGReZsRzPAGinnJJBaOYnaZlIssl['output']) > 0:
                KlAKNBDNwzXcDoVQDPbFMpDaCXwgpTpW = lxwsNGReZsRzPAGinnJJBaOYnaZlIssl['output'].pop()
                if KlAKNBDNwzXcDoVQDPbFMpDaCXwgpTpW is not None:
                    cyVtyoMONSPBlqSlWoufOPfgvyJAdKec += KlAKNBDNwzXcDoVQDPbFMpDaCXwgpTpW
            xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab = th.cat([xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab, cyVtyoMONSPBlqSlWoufOPfgvyJAdKec], yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk=1)
            del cyVtyoMONSPBlqSlWoufOPfgvyJAdKec
            if len(omGAnSaAXbgvwNbvtUsYicLqgJqNBgst) > 0:
                onnoKTSBXtsNokVdhRRVzlkVGMUUuaBt = omGAnSaAXbgvwNbvtUsYicLqgJqNBgst[-1].BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg
            else:
                onnoKTSBXtsNokVdhRRVzlkVGMUUuaBt = None
            xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab = lgcRKzdVlZLqUAtcHVZRPLwLobDmukAq(FRIBQCDfDDxIonplwxvPCicvOmmOgYPC, xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab, cbvuxLJlTEiYpJEoytPnUgMhAcRHRwIE, tRdCjhUPYVVxnSEkGmJIHWRitDXRXSZS, transformer_options, onnoKTSBXtsNokVdhRRVzlkVGMUUuaBt)
        xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab = xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab.type(NECAaWUrFGIXcLimrerEYmxYIykQBfXb.DDRQlhrNSGpwTrokWitkZipdfbAqBFxv)
        if rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.predict_codebook_ids:
            return rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.id_predictor(xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab)
        else:
            return rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.iqymPVpxyjOWChGwBkTemSzHJbnJdAIz(xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab)
