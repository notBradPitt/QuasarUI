import torch
import torch.nn.functional as F
from contextlib import contextmanager
from quasar.ldm.modules.diffusionmodules.model import HAhRJZDsPfbaJIpLwjOXFEkHqjueFULJ, KfKIubLWuMYndZytaOVMUrnTLHiwPiVV
from quasar.ldm.modules.distributions.distributions import AMWOznfcIxmGDIhDMGJCUcUBGkZOTYHR
from quasar.ldm.util import EGpJWSXQbHSqfmcMzBaJeJAuDkDlnmrK
from quasar.ldm.modules.ema import FNPzkrvGxaqvoCNOqICrVrrNcmdkiBFJ
class DOVTGYrtwHyLPmYumkCaBmiywgtpSmPp(torch.nn.Module):
    def __init__(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS,
                 ddconfig,
                 lossconfig,
                 ImrGjiFVgoYlstXoXVYKbphbCLYUVMTp,
                 CZOnlrJVXnbYFkZDmLjOAswXNMiGhxHA=None,
                 qjPwgJXXCzvQOBUsJGzFEkNxwvIKJJVY=[],
                 gCkWoUSaMffhaFfOObjYTyhEKjQylPOz="image",
                 LiydrWyeMEwwOeYAqEvauuSJCuKBQzuE=None,
                 keNXWjDJOSBPBWXLznhNwIIjgmZeoNJK=None,
                 bGiLySteHgQEfhoICMWhUyeWhlsZpzRt=None,
                 QAqHpORGawewDTMOMrBjKFdcVZyPsAsW=False
                 ):
        super().__init__()
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.QAqHpORGawewDTMOMrBjKFdcVZyPsAsW = QAqHpORGawewDTMOMrBjKFdcVZyPsAsW
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.gCkWoUSaMffhaFfOObjYTyhEKjQylPOz = gCkWoUSaMffhaFfOObjYTyhEKjQylPOz
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.encoder = HAhRJZDsPfbaJIpLwjOXFEkHqjueFULJ(**ddconfig)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.decoder = KfKIubLWuMYndZytaOVMUrnTLHiwPiVV(**ddconfig)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.GtnkLyvfmiRPrwSQJfyYiKxybcBdUius = EGpJWSXQbHSqfmcMzBaJeJAuDkDlnmrK(lossconfig)
        assert ddconfig["double_z"]
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.quant_conv = torch.nn.LcFcvNeYCKrBHlNkoWrkqdbxdkNCJBBK(2*ddconfig["z_channels"], 2*ImrGjiFVgoYlstXoXVYKbphbCLYUVMTp, 1)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.post_quant_conv = torch.nn.LcFcvNeYCKrBHlNkoWrkqdbxdkNCJBBK(ImrGjiFVgoYlstXoXVYKbphbCLYUVMTp, ddconfig["z_channels"], 1)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.ImrGjiFVgoYlstXoXVYKbphbCLYUVMTp = ImrGjiFVgoYlstXoXVYKbphbCLYUVMTp
        if LiydrWyeMEwwOeYAqEvauuSJCuKBQzuE is not None:
            assert type(LiydrWyeMEwwOeYAqEvauuSJCuKBQzuE)==int
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.BpOtVuSttURsCNYELWmrxpBkqOPYBBlj("colorize", torch.randn(3, LiydrWyeMEwwOeYAqEvauuSJCuKBQzuE, 1, 1))
        if keNXWjDJOSBPBWXLznhNwIIjgmZeoNJK is not None:
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.keNXWjDJOSBPBWXLznhNwIIjgmZeoNJK = keNXWjDJOSBPBWXLznhNwIIjgmZeoNJK
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.use_ema = bGiLySteHgQEfhoICMWhUyeWhlsZpzRt is not None
        if rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.use_ema:
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.bGiLySteHgQEfhoICMWhUyeWhlsZpzRt = bGiLySteHgQEfhoICMWhUyeWhlsZpzRt
            assert 0. < bGiLySteHgQEfhoICMWhUyeWhlsZpzRt < 1.
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.model_ema = FNPzkrvGxaqvoCNOqICrVrrNcmdkiBFJ(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, eeehCkWlicOSSZeEWMocEIpaDJxlRTfD=bGiLySteHgQEfhoICMWhUyeWhlsZpzRt)
            print(f"Keeping EMAs of {len(list(self.model_ema.buffers()))}.")
        if CZOnlrJVXnbYFkZDmLjOAswXNMiGhxHA is not None:
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.etGiBBXXdQnCKsmLvSHNGrMxDccsFXro(CZOnlrJVXnbYFkZDmLjOAswXNMiGhxHA, qjPwgJXXCzvQOBUsJGzFEkNxwvIKJJVY=qjPwgJXXCzvQOBUsJGzFEkNxwvIKJJVY)
    def etGiBBXXdQnCKsmLvSHNGrMxDccsFXro(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, hxKDuOteESNpOgdClxSsFUWnOOOOTwlR, qjPwgJXXCzvQOBUsJGzFEkNxwvIKJJVY=list()):
        if hxKDuOteESNpOgdClxSsFUWnOOOOTwlR.lower().endswith(".safetensors"):
            import safetensors.torch
            ylGhUFMpxPbtUUTfCZpemVkdanRhWmHa = safetensors.torch.load_file(hxKDuOteESNpOgdClxSsFUWnOOOOTwlR, fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc="cpu")
        else:
            ylGhUFMpxPbtUUTfCZpemVkdanRhWmHa = torch.yjjLwfEWtXKFjwwmuqReIXUDoGaUzfxz(hxKDuOteESNpOgdClxSsFUWnOOOOTwlR, map_location="cpu")["state_dict"]
        keys = list(ylGhUFMpxPbtUUTfCZpemVkdanRhWmHa.keys())
        for EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm in keys:
            for yuzyAejctbCYItZpiXKFoJIMHhxhUHhK in qjPwgJXXCzvQOBUsJGzFEkNxwvIKJJVY:
                if EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm.startswith(yuzyAejctbCYItZpiXKFoJIMHhxhUHhK):
                    print("Deleting key {} from state_dict.".format(EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm))
                    del ylGhUFMpxPbtUUTfCZpemVkdanRhWmHa[EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm]
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.OVlRwgmJvqggImaZMfxKZfQnVYfyhIsc(ylGhUFMpxPbtUUTfCZpemVkdanRhWmHa, strict=False)
        print(f"Restored from {path}")
    @contextmanager
    def HtVERntkBEKLgbBOtizqXvqivvfwyHOu(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, tRdCjhUPYVVxnSEkGmJIHWRitDXRXSZS=None):
        if rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.use_ema:
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.model_ema.RqdzCAmZioTnqOtBxyPpQMpxNZqqYqMv(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.parameters())
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.model_ema.cxEZDJIlvgwWEipGcqcszbHomLBZFKCo(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS)
            if tRdCjhUPYVVxnSEkGmJIHWRitDXRXSZS is not None:
                print(f"{context}: Switched to EMA weights")
        try:
            yield None
        finally:
            if rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.use_ema:
                rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.model_ema.ySkZIiRSiuKfRdBOssYffHcPMeZbGctR(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.parameters())
                if tRdCjhUPYVVxnSEkGmJIHWRitDXRXSZS is not None:
                    print(f"{context}: Restored training weights")
    def nQusPokGJLqIVlCginQOhiNyScGlnbeN(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, *DukiculvUpjhZIVvaGinshRSKLSTgVVl, **kwargs):
        if rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.use_ema:
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.model_ema(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS)
    def encode(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, NECAaWUrFGIXcLimrerEYmxYIykQBfXb):
        xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.encoder(NECAaWUrFGIXcLimrerEYmxYIykQBfXb)
        SESipywOUUrZAieDZvVNzzAznHiUgpCj = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.quant_conv(xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab)
        OjRLpYcpZYeMIBCxhYHVmTmJqVNMxpLi = AMWOznfcIxmGDIhDMGJCUcUBGkZOTYHR(SESipywOUUrZAieDZvVNzzAznHiUgpCj)
        return OjRLpYcpZYeMIBCxhYHVmTmJqVNMxpLi
    def DzeufPfapTAWMrnfPsMZfOIZEyGYmPHT(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, AVjwZelSxiiANPDkDuRKTIIJYnqgQaTi):
        AVjwZelSxiiANPDkDuRKTIIJYnqgQaTi = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.post_quant_conv(AVjwZelSxiiANPDkDuRKTIIJYnqgQaTi)
        LdjHqvQhhQqzoBRhgJbANjrwErsqpFIT = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.decoder(AVjwZelSxiiANPDkDuRKTIIJYnqgQaTi)
        return LdjHqvQhhQqzoBRhgJbANjrwErsqpFIT
    def lqBgIcSWZYylbCPjXksJWDguuSOqoPCJ(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, input, sample_posterior=True):
        OjRLpYcpZYeMIBCxhYHVmTmJqVNMxpLi = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.encode(input)
        if sample_posterior:
            AVjwZelSxiiANPDkDuRKTIIJYnqgQaTi = OjRLpYcpZYeMIBCxhYHVmTmJqVNMxpLi.kzeIpaLNSGyUxNmgVakyIZAkNbjmCUjd()
        else:
            AVjwZelSxiiANPDkDuRKTIIJYnqgQaTi = OjRLpYcpZYeMIBCxhYHVmTmJqVNMxpLi.bPTwwoDdWiuYqhtrDEHoDbHGiYcwcsQC()
        LdjHqvQhhQqzoBRhgJbANjrwErsqpFIT = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.DzeufPfapTAWMrnfPsMZfOIZEyGYmPHT(AVjwZelSxiiANPDkDuRKTIIJYnqgQaTi)
        return LdjHqvQhhQqzoBRhgJbANjrwErsqpFIT, OjRLpYcpZYeMIBCxhYHVmTmJqVNMxpLi
    def SKWKZHWuXTvGMlQdYYsxTxwxSOSgfKOq(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, IEfFCfCTfyvJvVHxiDPsIOnopGWoUJhP, EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm):
        NECAaWUrFGIXcLimrerEYmxYIykQBfXb = IEfFCfCTfyvJvVHxiDPsIOnopGWoUJhP[EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm]
        if len(NECAaWUrFGIXcLimrerEYmxYIykQBfXb.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg) == 3:
            NECAaWUrFGIXcLimrerEYmxYIykQBfXb = NECAaWUrFGIXcLimrerEYmxYIykQBfXb[..., None]
        NECAaWUrFGIXcLimrerEYmxYIykQBfXb = NECAaWUrFGIXcLimrerEYmxYIykQBfXb.permute(0, 3, 1, 2).sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ(memory_format=torch.contiguous_format).float()
        return NECAaWUrFGIXcLimrerEYmxYIykQBfXb
    def sewtJkbspfjukYrcyQfWQofXtOfyEWBD(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, IEfFCfCTfyvJvVHxiDPsIOnopGWoUJhP, batch_idx, optimizer_idx):
        kxdrqSDQHJnEllMOtIqUSWLnexkmvsXK = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.SKWKZHWuXTvGMlQdYYsxTxwxSOSgfKOq(IEfFCfCTfyvJvVHxiDPsIOnopGWoUJhP, rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.gCkWoUSaMffhaFfOObjYTyhEKjQylPOz)
        XLJDYnAUlwQYoAMOHHOBgYDAuuXLzzWP, OjRLpYcpZYeMIBCxhYHVmTmJqVNMxpLi = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS(kxdrqSDQHJnEllMOtIqUSWLnexkmvsXK)
        if optimizer_idx == 0:
            tGScAverNUkdUvegsTHIbmGDLqCnGGHy, dztlUILHaFCthrcIqwGcuIxviiApTumy = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.GtnkLyvfmiRPrwSQJfyYiKxybcBdUius(kxdrqSDQHJnEllMOtIqUSWLnexkmvsXK, XLJDYnAUlwQYoAMOHHOBgYDAuuXLzzWP, OjRLpYcpZYeMIBCxhYHVmTmJqVNMxpLi, optimizer_idx, rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.global_step,
                                            xLaNTzwyqfLRPRuXXAejepZyhqTxIVxV=rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.jAbQXzbRQmhDdUPexMZJhBfggMNexRBj(), split="train")
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.DJwhOGBaLcOjmXnuwXMXOyhMtknqkKXL("aeloss", tGScAverNUkdUvegsTHIbmGDLqCnGGHy, prog_bar=True, logger=True, on_step=True, on_epoch=True)
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.gnKIJiBrjxoYmsVqnAarGPJDIKaykROf(dztlUILHaFCthrcIqwGcuIxviiApTumy, prog_bar=False, logger=True, on_step=True, on_epoch=False)
            return tGScAverNUkdUvegsTHIbmGDLqCnGGHy
        if optimizer_idx == 1:
            uHLtUbiPJXruoHTPNYEuVMpRiDgeSocD, ZYvemJRBResCQGCZuSjUSBwrNHrLHizC = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.GtnkLyvfmiRPrwSQJfyYiKxybcBdUius(kxdrqSDQHJnEllMOtIqUSWLnexkmvsXK, XLJDYnAUlwQYoAMOHHOBgYDAuuXLzzWP, OjRLpYcpZYeMIBCxhYHVmTmJqVNMxpLi, optimizer_idx, rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.global_step,
                                                xLaNTzwyqfLRPRuXXAejepZyhqTxIVxV=rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.jAbQXzbRQmhDdUPexMZJhBfggMNexRBj(), split="train")
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.DJwhOGBaLcOjmXnuwXMXOyhMtknqkKXL("discloss", uHLtUbiPJXruoHTPNYEuVMpRiDgeSocD, prog_bar=True, logger=True, on_step=True, on_epoch=True)
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.gnKIJiBrjxoYmsVqnAarGPJDIKaykROf(ZYvemJRBResCQGCZuSjUSBwrNHrLHizC, prog_bar=False, logger=True, on_step=True, on_epoch=False)
            return uHLtUbiPJXruoHTPNYEuVMpRiDgeSocD
    def lpdQjapBMGmRdAiHzUmOwSNexzgDSKdq(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, IEfFCfCTfyvJvVHxiDPsIOnopGWoUJhP, batch_idx):
        gnKIJiBrjxoYmsVqnAarGPJDIKaykROf = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.nOCmQrJNUNVIXeuTlkvLfZccJOWWeKjn(IEfFCfCTfyvJvVHxiDPsIOnopGWoUJhP, batch_idx)
        with rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.HtVERntkBEKLgbBOtizqXvqivvfwyHOu():
            pEvjHoaUsWwjuASMUjXPtFcfgvkVnfZl = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.nOCmQrJNUNVIXeuTlkvLfZccJOWWeKjn(IEfFCfCTfyvJvVHxiDPsIOnopGWoUJhP, batch_idx, postfix="_ema")
        return gnKIJiBrjxoYmsVqnAarGPJDIKaykROf
    def nOCmQrJNUNVIXeuTlkvLfZccJOWWeKjn(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, IEfFCfCTfyvJvVHxiDPsIOnopGWoUJhP, batch_idx, postfix=""):
        kxdrqSDQHJnEllMOtIqUSWLnexkmvsXK = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.SKWKZHWuXTvGMlQdYYsxTxwxSOSgfKOq(IEfFCfCTfyvJvVHxiDPsIOnopGWoUJhP, rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.gCkWoUSaMffhaFfOObjYTyhEKjQylPOz)
        XLJDYnAUlwQYoAMOHHOBgYDAuuXLzzWP, OjRLpYcpZYeMIBCxhYHVmTmJqVNMxpLi = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS(kxdrqSDQHJnEllMOtIqUSWLnexkmvsXK)
        tGScAverNUkdUvegsTHIbmGDLqCnGGHy, dztlUILHaFCthrcIqwGcuIxviiApTumy = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.GtnkLyvfmiRPrwSQJfyYiKxybcBdUius(kxdrqSDQHJnEllMOtIqUSWLnexkmvsXK, XLJDYnAUlwQYoAMOHHOBgYDAuuXLzzWP, OjRLpYcpZYeMIBCxhYHVmTmJqVNMxpLi, 0, rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.global_step,
                                        xLaNTzwyqfLRPRuXXAejepZyhqTxIVxV=rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.jAbQXzbRQmhDdUPexMZJhBfggMNexRBj(), split="val"+postfix)
        uHLtUbiPJXruoHTPNYEuVMpRiDgeSocD, ZYvemJRBResCQGCZuSjUSBwrNHrLHizC = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.GtnkLyvfmiRPrwSQJfyYiKxybcBdUius(kxdrqSDQHJnEllMOtIqUSWLnexkmvsXK, XLJDYnAUlwQYoAMOHHOBgYDAuuXLzzWP, OjRLpYcpZYeMIBCxhYHVmTmJqVNMxpLi, 1, rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.global_step,
                                            xLaNTzwyqfLRPRuXXAejepZyhqTxIVxV=rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.jAbQXzbRQmhDdUPexMZJhBfggMNexRBj(), split="val"+postfix)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.DJwhOGBaLcOjmXnuwXMXOyhMtknqkKXL(f"val{postfix}/rec_loss", dztlUILHaFCthrcIqwGcuIxviiApTumy[f"val{postfix}/rec_loss"])
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.gnKIJiBrjxoYmsVqnAarGPJDIKaykROf(dztlUILHaFCthrcIqwGcuIxviiApTumy)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.gnKIJiBrjxoYmsVqnAarGPJDIKaykROf(ZYvemJRBResCQGCZuSjUSBwrNHrLHizC)
        return rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.gnKIJiBrjxoYmsVqnAarGPJDIKaykROf
    def FqJXWXMSaijDsPxupfBMGRHRrIlqoZQY(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS):
        BbjvYJKNzsfQZuahPgdyaFZrYmxOIhRT = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.learning_rate
        NpMtrrlQHvUrwYnBkBNzonjaJAiVTAoM = list(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.encoder.parameters()) + list(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.decoder.parameters()) + list(
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.quant_conv.parameters()) + list(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.post_quant_conv.parameters())
        if rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.QAqHpORGawewDTMOMrBjKFdcVZyPsAsW:
            print(f"{self.__class__.__name__}: Learning logvar")
            NpMtrrlQHvUrwYnBkBNzonjaJAiVTAoM.append(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.GtnkLyvfmiRPrwSQJfyYiKxybcBdUius.logvar)
        OxnBXUMbYZAZXtjyDkAvhoYyoylUkSmj = torch.optim.Adam(NpMtrrlQHvUrwYnBkBNzonjaJAiVTAoM,
                                  BbjvYJKNzsfQZuahPgdyaFZrYmxOIhRT=BbjvYJKNzsfQZuahPgdyaFZrYmxOIhRT, aGiatFWLVusbPGSDloFtejqscKjAwtLv=(0.5, 0.9))
        IWwdolcqPfUxdciWWPcVEvhiwOCwUgAB = torch.optim.Adam(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.GtnkLyvfmiRPrwSQJfyYiKxybcBdUius.discriminator.parameters(),
                                    BbjvYJKNzsfQZuahPgdyaFZrYmxOIhRT=BbjvYJKNzsfQZuahPgdyaFZrYmxOIhRT, aGiatFWLVusbPGSDloFtejqscKjAwtLv=(0.5, 0.9))
        return [OxnBXUMbYZAZXtjyDkAvhoYyoylUkSmj, IWwdolcqPfUxdciWWPcVEvhiwOCwUgAB], []
    def jAbQXzbRQmhDdUPexMZJhBfggMNexRBj(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS):
        return rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.decoder.conv_out.RXBOtvKSHQkBvdKDbckmnlphvVygYURP
    @torch.no_grad()
    def ulbVWlTaxtyRXWaYamLkkRWwTgtiQlUt(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, IEfFCfCTfyvJvVHxiDPsIOnopGWoUJhP, only_inputs=False, log_ema=False, **kwargs):
        DJwhOGBaLcOjmXnuwXMXOyhMtknqkKXL = dict()
        NECAaWUrFGIXcLimrerEYmxYIykQBfXb = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.SKWKZHWuXTvGMlQdYYsxTxwxSOSgfKOq(IEfFCfCTfyvJvVHxiDPsIOnopGWoUJhP, rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.gCkWoUSaMffhaFfOObjYTyhEKjQylPOz)
        NECAaWUrFGIXcLimrerEYmxYIykQBfXb = NECAaWUrFGIXcLimrerEYmxYIykQBfXb.sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc)
        if not only_inputs:
            NxeMJXyCJjNtbKKpuYGLYBhNegDLQORS, OjRLpYcpZYeMIBCxhYHVmTmJqVNMxpLi = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS(NECAaWUrFGIXcLimrerEYmxYIykQBfXb)
            if NECAaWUrFGIXcLimrerEYmxYIykQBfXb.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[1] > 3:
                assert NxeMJXyCJjNtbKKpuYGLYBhNegDLQORS.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[1] > 3
                NECAaWUrFGIXcLimrerEYmxYIykQBfXb = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.GBMBSXEWZXQguuEWINMWTKfcVfzyqeuU(NECAaWUrFGIXcLimrerEYmxYIykQBfXb)
                NxeMJXyCJjNtbKKpuYGLYBhNegDLQORS = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.GBMBSXEWZXQguuEWINMWTKfcVfzyqeuU(NxeMJXyCJjNtbKKpuYGLYBhNegDLQORS)
            DJwhOGBaLcOjmXnuwXMXOyhMtknqkKXL["samples"] = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.DzeufPfapTAWMrnfPsMZfOIZEyGYmPHT(torch.randn_like(OjRLpYcpZYeMIBCxhYHVmTmJqVNMxpLi.kzeIpaLNSGyUxNmgVakyIZAkNbjmCUjd()))
            DJwhOGBaLcOjmXnuwXMXOyhMtknqkKXL["reconstructions"] = NxeMJXyCJjNtbKKpuYGLYBhNegDLQORS
            if log_ema or rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.use_ema:
                with rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.HtVERntkBEKLgbBOtizqXvqivvfwyHOu():
                    IxVcQyeDiuxSkOemCiDLwYdrJeASInzS, XrDbDPQhclItsrLKilivufsJhQFcOiEB = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS(NECAaWUrFGIXcLimrerEYmxYIykQBfXb)
                    if NECAaWUrFGIXcLimrerEYmxYIykQBfXb.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[1] > 3:
                        assert IxVcQyeDiuxSkOemCiDLwYdrJeASInzS.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[1] > 3
                        IxVcQyeDiuxSkOemCiDLwYdrJeASInzS = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.GBMBSXEWZXQguuEWINMWTKfcVfzyqeuU(IxVcQyeDiuxSkOemCiDLwYdrJeASInzS)
                    DJwhOGBaLcOjmXnuwXMXOyhMtknqkKXL["samples_ema"] = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.DzeufPfapTAWMrnfPsMZfOIZEyGYmPHT(torch.randn_like(XrDbDPQhclItsrLKilivufsJhQFcOiEB.kzeIpaLNSGyUxNmgVakyIZAkNbjmCUjd()))
                    DJwhOGBaLcOjmXnuwXMXOyhMtknqkKXL["reconstructions_ema"] = IxVcQyeDiuxSkOemCiDLwYdrJeASInzS
        DJwhOGBaLcOjmXnuwXMXOyhMtknqkKXL["inputs"] = NECAaWUrFGIXcLimrerEYmxYIykQBfXb
        return DJwhOGBaLcOjmXnuwXMXOyhMtknqkKXL
    def GBMBSXEWZXQguuEWINMWTKfcVfzyqeuU(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, NECAaWUrFGIXcLimrerEYmxYIykQBfXb):
        assert rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.gCkWoUSaMffhaFfOObjYTyhEKjQylPOz == "segmentation"
        if not hasattr(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, "colorize"):
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.BpOtVuSttURsCNYELWmrxpBkqOPYBBlj("colorize", torch.randn(3, NECAaWUrFGIXcLimrerEYmxYIykQBfXb.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[1], 1, 1).sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ(NECAaWUrFGIXcLimrerEYmxYIykQBfXb))
        NECAaWUrFGIXcLimrerEYmxYIykQBfXb = F.conv2d(NECAaWUrFGIXcLimrerEYmxYIykQBfXb, RXBOtvKSHQkBvdKDbckmnlphvVygYURP=rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.colorize)
        NECAaWUrFGIXcLimrerEYmxYIykQBfXb = 2.*(NECAaWUrFGIXcLimrerEYmxYIykQBfXb-NECAaWUrFGIXcLimrerEYmxYIykQBfXb.min())/(NECAaWUrFGIXcLimrerEYmxYIykQBfXb.max()-NECAaWUrFGIXcLimrerEYmxYIykQBfXb.min()) - 1.
        return NECAaWUrFGIXcLimrerEYmxYIykQBfXb
class bfLnKAFHEbaOYrEaVtQEKOqahcaAozxX(torch.nn.Module):
    def __init__(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, *DukiculvUpjhZIVvaGinshRSKLSTgVVl, vq_interface=False, **kwargs):
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.vq_interface = vq_interface
        super().__init__()
    def encode(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, NECAaWUrFGIXcLimrerEYmxYIykQBfXb, *DukiculvUpjhZIVvaGinshRSKLSTgVVl, **kwargs):
        return NECAaWUrFGIXcLimrerEYmxYIykQBfXb
    def DzeufPfapTAWMrnfPsMZfOIZEyGYmPHT(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, NECAaWUrFGIXcLimrerEYmxYIykQBfXb, *DukiculvUpjhZIVvaGinshRSKLSTgVVl, **kwargs):
        return NECAaWUrFGIXcLimrerEYmxYIykQBfXb
    def igozXCsnhgCZQmnoJMlyfcgGnTBaMSfs(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, NECAaWUrFGIXcLimrerEYmxYIykQBfXb, *DukiculvUpjhZIVvaGinshRSKLSTgVVl, **kwargs):
        if rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.vq_interface:
            return NECAaWUrFGIXcLimrerEYmxYIykQBfXb, None, [None, None, None]
        return NECAaWUrFGIXcLimrerEYmxYIykQBfXb
    def lqBgIcSWZYylbCPjXksJWDguuSOqoPCJ(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, NECAaWUrFGIXcLimrerEYmxYIykQBfXb, *DukiculvUpjhZIVvaGinshRSKLSTgVVl, **kwargs):
        return NECAaWUrFGIXcLimrerEYmxYIykQBfXb
