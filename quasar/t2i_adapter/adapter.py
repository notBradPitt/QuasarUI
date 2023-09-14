import torch
import torch.nn as nn
from collections import OrderedDict
def XqmPajboESpTdLShIQpHOQZiwGoVuVAj(ipYTWVOPDpfJXeTFApPIgldytQSaUFdk, *DukiculvUpjhZIVvaGinshRSKLSTgVVl, **kwargs):
    if ipYTWVOPDpfJXeTFApPIgldytQSaUFdk == 1:
        return nn.Conv1d(*DukiculvUpjhZIVvaGinshRSKLSTgVVl, **kwargs)
    elif ipYTWVOPDpfJXeTFApPIgldytQSaUFdk == 2:
        return nn.LcFcvNeYCKrBHlNkoWrkqdbxdkNCJBBK(*DukiculvUpjhZIVvaGinshRSKLSTgVVl, **kwargs)
    elif ipYTWVOPDpfJXeTFApPIgldytQSaUFdk == 3:
        return nn.Conv3d(*DukiculvUpjhZIVvaGinshRSKLSTgVVl, **kwargs)
    raise ValueError(f"unsupported dimensions: {dims}")
def ppDrxhPctQxMusBvKAntWykhHyNnAUtv(ipYTWVOPDpfJXeTFApPIgldytQSaUFdk, *DukiculvUpjhZIVvaGinshRSKLSTgVVl, **kwargs):
    if ipYTWVOPDpfJXeTFApPIgldytQSaUFdk == 1:
        return nn.AvgPool1d(*DukiculvUpjhZIVvaGinshRSKLSTgVVl, **kwargs)
    elif ipYTWVOPDpfJXeTFApPIgldytQSaUFdk == 2:
        return nn.AvgPool2d(*DukiculvUpjhZIVvaGinshRSKLSTgVVl, **kwargs)
    elif ipYTWVOPDpfJXeTFApPIgldytQSaUFdk == 3:
        return nn.AvgPool3d(*DukiculvUpjhZIVvaGinshRSKLSTgVVl, **kwargs)
    raise ValueError(f"unsupported dimensions: {dims}")
class LpwKTfRyOAITGEdvwhtCdMnNRMEQUkUG(nn.Module):
    def __init__(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, channels, BMidABgMadzWxSilVoOpGtdqLSQhQAjN, ipYTWVOPDpfJXeTFApPIgldytQSaUFdk=2, DjnmEmFIylXDvTfeYtLbwRKPMHUXFjho=None, sdxdTSjnkAOjlGmltQHvLiHRDstMzpAP=1):
        super().__init__()
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.channels = channels
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.DjnmEmFIylXDvTfeYtLbwRKPMHUXFjho = DjnmEmFIylXDvTfeYtLbwRKPMHUXFjho or channels
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.BMidABgMadzWxSilVoOpGtdqLSQhQAjN = BMidABgMadzWxSilVoOpGtdqLSQhQAjN
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.ipYTWVOPDpfJXeTFApPIgldytQSaUFdk = ipYTWVOPDpfJXeTFApPIgldytQSaUFdk
        NTEWXstfzqNXGESmGkQNFWBaQsGAPlGd = 2 if ipYTWVOPDpfJXeTFApPIgldytQSaUFdk != 3 else (1, 2, 2)
        if BMidABgMadzWxSilVoOpGtdqLSQhQAjN:
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.bjtPzNLsLxvykINbAtlMwKlGJQooJtzI = XqmPajboESpTdLShIQpHOQZiwGoVuVAj(
                ipYTWVOPDpfJXeTFApPIgldytQSaUFdk, rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.channels, rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.DjnmEmFIylXDvTfeYtLbwRKPMHUXFjho, 3, NTEWXstfzqNXGESmGkQNFWBaQsGAPlGd=NTEWXstfzqNXGESmGkQNFWBaQsGAPlGd, sdxdTSjnkAOjlGmltQHvLiHRDstMzpAP=sdxdTSjnkAOjlGmltQHvLiHRDstMzpAP
            )
        else:
            assert rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.channels == rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.DjnmEmFIylXDvTfeYtLbwRKPMHUXFjho
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.bjtPzNLsLxvykINbAtlMwKlGJQooJtzI = ppDrxhPctQxMusBvKAntWykhHyNnAUtv(ipYTWVOPDpfJXeTFApPIgldytQSaUFdk, aBEJjpEOpoRJYkulwSmukddEYErxRnAG=NTEWXstfzqNXGESmGkQNFWBaQsGAPlGd, NTEWXstfzqNXGESmGkQNFWBaQsGAPlGd=NTEWXstfzqNXGESmGkQNFWBaQsGAPlGd)
    def lqBgIcSWZYylbCPjXksJWDguuSOqoPCJ(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, NECAaWUrFGIXcLimrerEYmxYIykQBfXb):
        assert NECAaWUrFGIXcLimrerEYmxYIykQBfXb.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[1] == rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.channels
        if not rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.BMidABgMadzWxSilVoOpGtdqLSQhQAjN:
            sdxdTSjnkAOjlGmltQHvLiHRDstMzpAP = [NECAaWUrFGIXcLimrerEYmxYIykQBfXb.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[2] % 2, NECAaWUrFGIXcLimrerEYmxYIykQBfXb.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[3] % 2]
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.bjtPzNLsLxvykINbAtlMwKlGJQooJtzI.sdxdTSjnkAOjlGmltQHvLiHRDstMzpAP = sdxdTSjnkAOjlGmltQHvLiHRDstMzpAP
        NECAaWUrFGIXcLimrerEYmxYIykQBfXb = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.bjtPzNLsLxvykINbAtlMwKlGJQooJtzI(NECAaWUrFGIXcLimrerEYmxYIykQBfXb)
        return NECAaWUrFGIXcLimrerEYmxYIykQBfXb
class ompzonOkvRsHNKHceWNmvSNXZeCTwgaf(nn.Module):
    def __init__(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, in_c, out_c, PKmeubCqZPUpSfmqJozYuvYsQsIMTIOn, gcxqXDVvHPuehBbNpJwzTveeqNWyZNze=3, sk=False, BMidABgMadzWxSilVoOpGtdqLSQhQAjN=True):
        super().__init__()
        fsKtHQnFsZEFuvvsSCubTXMmuFUlFFAH = gcxqXDVvHPuehBbNpJwzTveeqNWyZNze // 2
        if in_c != out_c or sk == False:
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.UgSPfpdOjavOkuRHVjJRYOswzqgseqrc = nn.LcFcvNeYCKrBHlNkoWrkqdbxdkNCJBBK(in_c, out_c, gcxqXDVvHPuehBbNpJwzTveeqNWyZNze, 1, fsKtHQnFsZEFuvvsSCubTXMmuFUlFFAH)
        else:
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.UgSPfpdOjavOkuRHVjJRYOswzqgseqrc = None
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.block1 = nn.LcFcvNeYCKrBHlNkoWrkqdbxdkNCJBBK(out_c, out_c, 3, 1, 1)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.act = nn.ReLU()
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.block2 = nn.LcFcvNeYCKrBHlNkoWrkqdbxdkNCJBBK(out_c, out_c, gcxqXDVvHPuehBbNpJwzTveeqNWyZNze, 1, fsKtHQnFsZEFuvvsSCubTXMmuFUlFFAH)
        if sk == False:
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.skep = nn.LcFcvNeYCKrBHlNkoWrkqdbxdkNCJBBK(in_c, out_c, gcxqXDVvHPuehBbNpJwzTveeqNWyZNze, 1, fsKtHQnFsZEFuvvsSCubTXMmuFUlFFAH)
        else:
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.skep = None
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.PKmeubCqZPUpSfmqJozYuvYsQsIMTIOn = PKmeubCqZPUpSfmqJozYuvYsQsIMTIOn
        if rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.PKmeubCqZPUpSfmqJozYuvYsQsIMTIOn == True:
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.down_opt = LpwKTfRyOAITGEdvwhtCdMnNRMEQUkUG(in_c, BMidABgMadzWxSilVoOpGtdqLSQhQAjN=BMidABgMadzWxSilVoOpGtdqLSQhQAjN)
    def lqBgIcSWZYylbCPjXksJWDguuSOqoPCJ(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, NECAaWUrFGIXcLimrerEYmxYIykQBfXb):
        if rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.PKmeubCqZPUpSfmqJozYuvYsQsIMTIOn == True:
            NECAaWUrFGIXcLimrerEYmxYIykQBfXb = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.down_opt(NECAaWUrFGIXcLimrerEYmxYIykQBfXb)
        if rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.UgSPfpdOjavOkuRHVjJRYOswzqgseqrc is not None:  
            NECAaWUrFGIXcLimrerEYmxYIykQBfXb = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.UgSPfpdOjavOkuRHVjJRYOswzqgseqrc(NECAaWUrFGIXcLimrerEYmxYIykQBfXb)
        xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.block1(NECAaWUrFGIXcLimrerEYmxYIykQBfXb)
        xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.act(xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab)
        xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.block2(xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab)
        if rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.skep is not None:
            return xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab + rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.skep(NECAaWUrFGIXcLimrerEYmxYIykQBfXb)
        else:
            return xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab + NECAaWUrFGIXcLimrerEYmxYIykQBfXb
class ZPOXjvfzXIIyNqBeetwWBnTgzptlxmjU(nn.Module):
    def __init__(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, channels=[320, 640, 1280, 1280], nums_rb=3, lZFDQGrsxjmuPKhiBycouNmmtdgourGD=64, gcxqXDVvHPuehBbNpJwzTveeqNWyZNze=3, sk=False, BMidABgMadzWxSilVoOpGtdqLSQhQAjN=True, woDONBBxfEKwjIgxrZSxOuFkXiNJfLMx=True):
        super(ZPOXjvfzXIIyNqBeetwWBnTgzptlxmjU, rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS).__init__()
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.RxZmotBdOdFtUFLUWizeTJiDqLkJiiCu = 8
        gLwBNMSScKJaUfpftZbMpEYHNHQVdEEL = []
        PrhKctKEjepzbMQXcQBqMwDXNKyZnODL = [3, 2, 1]
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.woDONBBxfEKwjIgxrZSxOuFkXiNJfLMx = woDONBBxfEKwjIgxrZSxOuFkXiNJfLMx
        if rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.woDONBBxfEKwjIgxrZSxOuFkXiNJfLMx:
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.RxZmotBdOdFtUFLUWizeTJiDqLkJiiCu = 16
            gLwBNMSScKJaUfpftZbMpEYHNHQVdEEL = [1]
            PrhKctKEjepzbMQXcQBqMwDXNKyZnODL = [2]
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.input_channels = lZFDQGrsxjmuPKhiBycouNmmtdgourGD // (rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.RxZmotBdOdFtUFLUWizeTJiDqLkJiiCu * rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.RxZmotBdOdFtUFLUWizeTJiDqLkJiiCu)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.unshuffle = nn.PixelUnshuffle(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.RxZmotBdOdFtUFLUWizeTJiDqLkJiiCu)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.channels = channels
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.nums_rb = nums_rb
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.body = []
        for HCXmerBqIMuTscBONzTGKYapYSxWTYHo in range(len(channels)):
            for VyjoFEMsihtolZHiuwJuxJKmDsIroAsQ in range(nums_rb):
                if (HCXmerBqIMuTscBONzTGKYapYSxWTYHo in PrhKctKEjepzbMQXcQBqMwDXNKyZnODL) and (VyjoFEMsihtolZHiuwJuxJKmDsIroAsQ == 0):
                    rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.body.append(
                        ompzonOkvRsHNKHceWNmvSNXZeCTwgaf(channels[HCXmerBqIMuTscBONzTGKYapYSxWTYHo - 1], channels[HCXmerBqIMuTscBONzTGKYapYSxWTYHo], PKmeubCqZPUpSfmqJozYuvYsQsIMTIOn=True, gcxqXDVvHPuehBbNpJwzTveeqNWyZNze=gcxqXDVvHPuehBbNpJwzTveeqNWyZNze, sk=sk, BMidABgMadzWxSilVoOpGtdqLSQhQAjN=BMidABgMadzWxSilVoOpGtdqLSQhQAjN))
                elif (HCXmerBqIMuTscBONzTGKYapYSxWTYHo in gLwBNMSScKJaUfpftZbMpEYHNHQVdEEL) and (VyjoFEMsihtolZHiuwJuxJKmDsIroAsQ == 0):
                    rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.body.append(
                        ompzonOkvRsHNKHceWNmvSNXZeCTwgaf(channels[HCXmerBqIMuTscBONzTGKYapYSxWTYHo - 1], channels[HCXmerBqIMuTscBONzTGKYapYSxWTYHo], PKmeubCqZPUpSfmqJozYuvYsQsIMTIOn=False, gcxqXDVvHPuehBbNpJwzTveeqNWyZNze=gcxqXDVvHPuehBbNpJwzTveeqNWyZNze, sk=sk, BMidABgMadzWxSilVoOpGtdqLSQhQAjN=BMidABgMadzWxSilVoOpGtdqLSQhQAjN))
                else:
                    rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.body.append(
                        ompzonOkvRsHNKHceWNmvSNXZeCTwgaf(channels[HCXmerBqIMuTscBONzTGKYapYSxWTYHo], channels[HCXmerBqIMuTscBONzTGKYapYSxWTYHo], PKmeubCqZPUpSfmqJozYuvYsQsIMTIOn=False, gcxqXDVvHPuehBbNpJwzTveeqNWyZNze=gcxqXDVvHPuehBbNpJwzTveeqNWyZNze, sk=sk, BMidABgMadzWxSilVoOpGtdqLSQhQAjN=BMidABgMadzWxSilVoOpGtdqLSQhQAjN))
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.body = nn.ModuleList(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.body)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.conv_in = nn.LcFcvNeYCKrBHlNkoWrkqdbxdkNCJBBK(lZFDQGrsxjmuPKhiBycouNmmtdgourGD, channels[0], 3, 1, 1)
    def lqBgIcSWZYylbCPjXksJWDguuSOqoPCJ(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, NECAaWUrFGIXcLimrerEYmxYIykQBfXb):
        NECAaWUrFGIXcLimrerEYmxYIykQBfXb = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.unshuffle(NECAaWUrFGIXcLimrerEYmxYIykQBfXb)
        pCLwRAgBLFqTliMnElfbAlRRHMihRlVI = []
        NECAaWUrFGIXcLimrerEYmxYIykQBfXb = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.conv_in(NECAaWUrFGIXcLimrerEYmxYIykQBfXb)
        for HCXmerBqIMuTscBONzTGKYapYSxWTYHo in range(len(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.channels)):
            for VyjoFEMsihtolZHiuwJuxJKmDsIroAsQ in range(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.nums_rb):
                bgiQlPcatFmgYxScjGTjbwHMfYvijboo = HCXmerBqIMuTscBONzTGKYapYSxWTYHo * rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.nums_rb + VyjoFEMsihtolZHiuwJuxJKmDsIroAsQ
                NECAaWUrFGIXcLimrerEYmxYIykQBfXb = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.body[bgiQlPcatFmgYxScjGTjbwHMfYvijboo](NECAaWUrFGIXcLimrerEYmxYIykQBfXb)
            if rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.woDONBBxfEKwjIgxrZSxOuFkXiNJfLMx:
                pCLwRAgBLFqTliMnElfbAlRRHMihRlVI.append(None)
                if HCXmerBqIMuTscBONzTGKYapYSxWTYHo == 0:
                    pCLwRAgBLFqTliMnElfbAlRRHMihRlVI.append(None)
                    pCLwRAgBLFqTliMnElfbAlRRHMihRlVI.append(None)
                if HCXmerBqIMuTscBONzTGKYapYSxWTYHo == 2:
                    pCLwRAgBLFqTliMnElfbAlRRHMihRlVI.append(None)
            else:
                pCLwRAgBLFqTliMnElfbAlRRHMihRlVI.append(None)
                pCLwRAgBLFqTliMnElfbAlRRHMihRlVI.append(None)
            pCLwRAgBLFqTliMnElfbAlRRHMihRlVI.append(NECAaWUrFGIXcLimrerEYmxYIykQBfXb)
        return pCLwRAgBLFqTliMnElfbAlRRHMihRlVI
class SeaDiaiECtgJbgiExWzpSnrizTosOUam(nn.SeaDiaiECtgJbgiExWzpSnrizTosOUam):
    def lqBgIcSWZYylbCPjXksJWDguuSOqoPCJ(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, NECAaWUrFGIXcLimrerEYmxYIykQBfXb: torch.Tensor):
        vaQUhMcmnNspgfwIgYwSuzRUigaVCUxS = NECAaWUrFGIXcLimrerEYmxYIykQBfXb.DDRQlhrNSGpwTrokWitkZipdfbAqBFxv
        wTKTCkxEtYuHmqLlpcdxLANFEoxUnsLR = super().lqBgIcSWZYylbCPjXksJWDguuSOqoPCJ(NECAaWUrFGIXcLimrerEYmxYIykQBfXb.type(torch.float32))
        return wTKTCkxEtYuHmqLlpcdxLANFEoxUnsLR.type(vaQUhMcmnNspgfwIgYwSuzRUigaVCUxS)
class GeNhupzNiimxezSARlAnOPrGdhhSOnHB(nn.Module):
    def lqBgIcSWZYylbCPjXksJWDguuSOqoPCJ(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, NECAaWUrFGIXcLimrerEYmxYIykQBfXb: torch.Tensor):
        return NECAaWUrFGIXcLimrerEYmxYIykQBfXb * torch.sigmoid(1.702 * NECAaWUrFGIXcLimrerEYmxYIykQBfXb)
class GgoSrIzZPOGjMeOFIrXVdnpbVQukOSbe(nn.Module):
    def __init__(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, d_model: int, n_head: int, attn_mask: torch.Tensor = None):
        super().__init__()
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.tUmudCfKVwpeKVqJPkVQAwLriIrTDLbW = nn.MultiheadAttention(d_model, n_head)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.ln_1 = SeaDiaiECtgJbgiExWzpSnrizTosOUam(d_model)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.mlp = nn.Sequential(
            OrderedDict([("c_fc", nn.DhMcMyEvvzmWIEJojbQeGHlzfZKiPzHO(d_model, d_model * 4)), ("gelu", GeNhupzNiimxezSARlAnOPrGdhhSOnHB()),
                         ("c_proj", nn.DhMcMyEvvzmWIEJojbQeGHlzfZKiPzHO(d_model * 4, d_model))]))
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.ln_2 = SeaDiaiECtgJbgiExWzpSnrizTosOUam(d_model)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.attn_mask = attn_mask
    def psnGIaaNNBTQhtdDvLAOAncJBcOCafNn(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, NECAaWUrFGIXcLimrerEYmxYIykQBfXb: torch.Tensor):
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.attn_mask = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.attn_mask.sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ(DDRQlhrNSGpwTrokWitkZipdfbAqBFxv=NECAaWUrFGIXcLimrerEYmxYIykQBfXb.DDRQlhrNSGpwTrokWitkZipdfbAqBFxv, fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc=NECAaWUrFGIXcLimrerEYmxYIykQBfXb.fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc) if rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.attn_mask is not None else None
        return rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.tUmudCfKVwpeKVqJPkVQAwLriIrTDLbW(NECAaWUrFGIXcLimrerEYmxYIykQBfXb, NECAaWUrFGIXcLimrerEYmxYIykQBfXb, NECAaWUrFGIXcLimrerEYmxYIykQBfXb, need_weights=False, attn_mask=rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.attn_mask)[0]
    def lqBgIcSWZYylbCPjXksJWDguuSOqoPCJ(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, NECAaWUrFGIXcLimrerEYmxYIykQBfXb: torch.Tensor):
        NECAaWUrFGIXcLimrerEYmxYIykQBfXb = NECAaWUrFGIXcLimrerEYmxYIykQBfXb + rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.psnGIaaNNBTQhtdDvLAOAncJBcOCafNn(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.ln_1(NECAaWUrFGIXcLimrerEYmxYIykQBfXb))
        NECAaWUrFGIXcLimrerEYmxYIykQBfXb = NECAaWUrFGIXcLimrerEYmxYIykQBfXb + rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.mlp(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.ln_2(NECAaWUrFGIXcLimrerEYmxYIykQBfXb))
        return NECAaWUrFGIXcLimrerEYmxYIykQBfXb
class lxWVPNdaxUbpuzwEAZgGWGeTDDPkAoFY(nn.Module):
    def __init__(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, QfeoFYGsEQNWblsqXsRKWQpzeXgWujaz=1024, FEAAZHeTRQEJCsYHCOEPpfOenpVZIhNT=768, num_head=8, n_layes=3, num_token=4):
        super().__init__()
        xmbXivThLFnawFPAJvIDBztziWsaDyEE = QfeoFYGsEQNWblsqXsRKWQpzeXgWujaz ** -0.5
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.transformer_layes = nn.Sequential(*[GgoSrIzZPOGjMeOFIrXVdnpbVQukOSbe(QfeoFYGsEQNWblsqXsRKWQpzeXgWujaz, num_head) for _ in range(n_layes)])
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.num_token = num_token
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.fstVyJPPUlPlRjSxVKdBhpDfMHdhuUMc = nn.Parameter(torch.randn(1, num_token, QfeoFYGsEQNWblsqXsRKWQpzeXgWujaz) * xmbXivThLFnawFPAJvIDBztziWsaDyEE)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.ln_post = SeaDiaiECtgJbgiExWzpSnrizTosOUam(QfeoFYGsEQNWblsqXsRKWQpzeXgWujaz)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.ln_pre = SeaDiaiECtgJbgiExWzpSnrizTosOUam(QfeoFYGsEQNWblsqXsRKWQpzeXgWujaz)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.proj = nn.Parameter(xmbXivThLFnawFPAJvIDBztziWsaDyEE * torch.randn(QfeoFYGsEQNWblsqXsRKWQpzeXgWujaz, FEAAZHeTRQEJCsYHCOEPpfOenpVZIhNT))
    def lqBgIcSWZYylbCPjXksJWDguuSOqoPCJ(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, NECAaWUrFGIXcLimrerEYmxYIykQBfXb):
        fstVyJPPUlPlRjSxVKdBhpDfMHdhuUMc = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.fstVyJPPUlPlRjSxVKdBhpDfMHdhuUMc + torch.zeros(
            (NECAaWUrFGIXcLimrerEYmxYIykQBfXb.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[0], rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.num_token, rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.fstVyJPPUlPlRjSxVKdBhpDfMHdhuUMc.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[-1]), fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc=NECAaWUrFGIXcLimrerEYmxYIykQBfXb.fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc)
        NECAaWUrFGIXcLimrerEYmxYIykQBfXb = torch.cat([NECAaWUrFGIXcLimrerEYmxYIykQBfXb, fstVyJPPUlPlRjSxVKdBhpDfMHdhuUMc], yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk=1)
        NECAaWUrFGIXcLimrerEYmxYIykQBfXb = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.ln_pre(NECAaWUrFGIXcLimrerEYmxYIykQBfXb)
        NECAaWUrFGIXcLimrerEYmxYIykQBfXb = NECAaWUrFGIXcLimrerEYmxYIykQBfXb.permute(1, 0, 2)  
        NECAaWUrFGIXcLimrerEYmxYIykQBfXb = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.transformer_layes(NECAaWUrFGIXcLimrerEYmxYIykQBfXb)
        NECAaWUrFGIXcLimrerEYmxYIykQBfXb = NECAaWUrFGIXcLimrerEYmxYIykQBfXb.permute(1, 0, 2)  
        NECAaWUrFGIXcLimrerEYmxYIykQBfXb = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.ln_post(NECAaWUrFGIXcLimrerEYmxYIykQBfXb[:, -rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.num_token:, :])
        NECAaWUrFGIXcLimrerEYmxYIykQBfXb = NECAaWUrFGIXcLimrerEYmxYIykQBfXb @ rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.proj
        return NECAaWUrFGIXcLimrerEYmxYIykQBfXb
class gvWdzESafylvwQVqXYlgZdSnBxZpueCs(nn.Module):
    def __init__(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, in_c):
        super().__init__()
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.block1 = nn.LcFcvNeYCKrBHlNkoWrkqdbxdkNCJBBK(in_c, in_c, 3, 1, 1)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.act = nn.ReLU()
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.block2 = nn.LcFcvNeYCKrBHlNkoWrkqdbxdkNCJBBK(in_c, in_c, 3, 1, 1)
    def lqBgIcSWZYylbCPjXksJWDguuSOqoPCJ(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, NECAaWUrFGIXcLimrerEYmxYIykQBfXb):
        xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.block1(NECAaWUrFGIXcLimrerEYmxYIykQBfXb)
        xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.act(xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab)
        xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.block2(xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab)
        return xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab + NECAaWUrFGIXcLimrerEYmxYIykQBfXb
class oomommsZHQWMxaNIGlGepiPZHgBeyHcx(nn.Module):
    def __init__(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, in_c, inter_c, out_c, nums_rb, PKmeubCqZPUpSfmqJozYuvYsQsIMTIOn=False):
        super().__init__()
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.UgSPfpdOjavOkuRHVjJRYOswzqgseqrc = nn.LcFcvNeYCKrBHlNkoWrkqdbxdkNCJBBK(in_c, inter_c, 1, 1, 0)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.body = []
        for _ in range(nums_rb):
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.body.append(gvWdzESafylvwQVqXYlgZdSnBxZpueCs(inter_c))
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.body = nn.Sequential(*rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.body)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.out_conv = nn.LcFcvNeYCKrBHlNkoWrkqdbxdkNCJBBK(inter_c, out_c, 1, 1, 0)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.PKmeubCqZPUpSfmqJozYuvYsQsIMTIOn = PKmeubCqZPUpSfmqJozYuvYsQsIMTIOn
        if rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.PKmeubCqZPUpSfmqJozYuvYsQsIMTIOn == True:
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.down_opt = LpwKTfRyOAITGEdvwhtCdMnNRMEQUkUG(in_c, BMidABgMadzWxSilVoOpGtdqLSQhQAjN=False)
    def lqBgIcSWZYylbCPjXksJWDguuSOqoPCJ(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, NECAaWUrFGIXcLimrerEYmxYIykQBfXb):
        if rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.PKmeubCqZPUpSfmqJozYuvYsQsIMTIOn == True:
            NECAaWUrFGIXcLimrerEYmxYIykQBfXb = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.down_opt(NECAaWUrFGIXcLimrerEYmxYIykQBfXb)
        NECAaWUrFGIXcLimrerEYmxYIykQBfXb = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.UgSPfpdOjavOkuRHVjJRYOswzqgseqrc(NECAaWUrFGIXcLimrerEYmxYIykQBfXb)
        NECAaWUrFGIXcLimrerEYmxYIykQBfXb = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.body(NECAaWUrFGIXcLimrerEYmxYIykQBfXb)
        NECAaWUrFGIXcLimrerEYmxYIykQBfXb = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.out_conv(NECAaWUrFGIXcLimrerEYmxYIykQBfXb)
        return NECAaWUrFGIXcLimrerEYmxYIykQBfXb
class qgeSgitlrURgBLleGvUEMOpdoielgAYL(nn.Module):
    def __init__(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, channels=[320, 640, 1280, 1280], nums_rb=3, lZFDQGrsxjmuPKhiBycouNmmtdgourGD=64):
        super(qgeSgitlrURgBLleGvUEMOpdoielgAYL, rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS).__init__()
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.RxZmotBdOdFtUFLUWizeTJiDqLkJiiCu = 8
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.unshuffle = nn.PixelUnshuffle(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.RxZmotBdOdFtUFLUWizeTJiDqLkJiiCu)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.input_channels = lZFDQGrsxjmuPKhiBycouNmmtdgourGD // (rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.RxZmotBdOdFtUFLUWizeTJiDqLkJiiCu * rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.RxZmotBdOdFtUFLUWizeTJiDqLkJiiCu)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.channels = channels
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.nums_rb = nums_rb
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.body = []
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.woDONBBxfEKwjIgxrZSxOuFkXiNJfLMx = False
        for HCXmerBqIMuTscBONzTGKYapYSxWTYHo in range(len(channels)):
            if HCXmerBqIMuTscBONzTGKYapYSxWTYHo == 0:
                rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.body.append(oomommsZHQWMxaNIGlGepiPZHgBeyHcx(in_c=lZFDQGrsxjmuPKhiBycouNmmtdgourGD, inter_c=channels[HCXmerBqIMuTscBONzTGKYapYSxWTYHo]//4, out_c=channels[HCXmerBqIMuTscBONzTGKYapYSxWTYHo], nums_rb=nums_rb, PKmeubCqZPUpSfmqJozYuvYsQsIMTIOn=False))
            else:
                rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.body.append(oomommsZHQWMxaNIGlGepiPZHgBeyHcx(in_c=channels[HCXmerBqIMuTscBONzTGKYapYSxWTYHo-1], inter_c=channels[HCXmerBqIMuTscBONzTGKYapYSxWTYHo]//4, out_c=channels[HCXmerBqIMuTscBONzTGKYapYSxWTYHo], nums_rb=nums_rb, PKmeubCqZPUpSfmqJozYuvYsQsIMTIOn=True))
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.body = nn.ModuleList(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.body)
    def lqBgIcSWZYylbCPjXksJWDguuSOqoPCJ(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, NECAaWUrFGIXcLimrerEYmxYIykQBfXb):
        NECAaWUrFGIXcLimrerEYmxYIykQBfXb = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.unshuffle(NECAaWUrFGIXcLimrerEYmxYIykQBfXb)
        pCLwRAgBLFqTliMnElfbAlRRHMihRlVI = []
        for HCXmerBqIMuTscBONzTGKYapYSxWTYHo in range(len(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.channels)):
            NECAaWUrFGIXcLimrerEYmxYIykQBfXb = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.body[HCXmerBqIMuTscBONzTGKYapYSxWTYHo](NECAaWUrFGIXcLimrerEYmxYIykQBfXb)
            pCLwRAgBLFqTliMnElfbAlRRHMihRlVI.append(None)
            pCLwRAgBLFqTliMnElfbAlRRHMihRlVI.append(None)
            pCLwRAgBLFqTliMnElfbAlRRHMihRlVI.append(NECAaWUrFGIXcLimrerEYmxYIykQBfXb)
        return pCLwRAgBLFqTliMnElfbAlRRHMihRlVI
