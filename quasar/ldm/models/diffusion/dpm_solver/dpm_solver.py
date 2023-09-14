import torch
import torch.nn.functional as F
import math
from tqdm import tqdm
class ZUKRuRXMuCiOVqAkFIfwywrWzwzNDRUk:
    def __init__(
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS,
            HtnYKlBDuwwBEVdTVKsUENSQHeXnhZXs='discrete',
            aGiatFWLVusbPGSDloFtejqscKjAwtLv=None,
            IOpmYnAWyhIWgvrJQuznNWQMTUXYwThN=None,
            wRjqNHDeyGVaoJDqPvKkVbYdmOyKFqNa=0.1,
            DOWMOuqfCxxMiOgRjyDbrGcTkOsbXYro=20.,
    ):
        if HtnYKlBDuwwBEVdTVKsUENSQHeXnhZXs not in ['discrete', 'linear', 'cosine']:
            raise ValueError(
                "Unsupported noise schedule {}. The schedule needs to be 'discrete' or 'linear' or 'cosine'".format(
                    HtnYKlBDuwwBEVdTVKsUENSQHeXnhZXs))
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.HtnYKlBDuwwBEVdTVKsUENSQHeXnhZXs = HtnYKlBDuwwBEVdTVKsUENSQHeXnhZXs
        if HtnYKlBDuwwBEVdTVKsUENSQHeXnhZXs == 'discrete':
            if aGiatFWLVusbPGSDloFtejqscKjAwtLv is not None:
                YBtUErmPdnxXxIKZqzNLmrclwlYRFYrs = 0.5 * torch.DJwhOGBaLcOjmXnuwXMXOyhMtknqkKXL(1 - aGiatFWLVusbPGSDloFtejqscKjAwtLv).cumsum(yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk=0)
            else:
                assert IOpmYnAWyhIWgvrJQuznNWQMTUXYwThN is not None
                YBtUErmPdnxXxIKZqzNLmrclwlYRFYrs = 0.5 * torch.DJwhOGBaLcOjmXnuwXMXOyhMtknqkKXL(IOpmYnAWyhIWgvrJQuznNWQMTUXYwThN)
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.total_N = len(YBtUErmPdnxXxIKZqzNLmrclwlYRFYrs)
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.T = 1.
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.t_array = torch.linspace(0., 1., rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.total_N + 1)[1:].reshape((1, -1))
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.log_alpha_array = YBtUErmPdnxXxIKZqzNLmrclwlYRFYrs.reshape((1, -1,))
        else:
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.total_N = 1000
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.beta_0 = wRjqNHDeyGVaoJDqPvKkVbYdmOyKFqNa
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.beta_1 = DOWMOuqfCxxMiOgRjyDbrGcTkOsbXYro
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.zPdwEaBmJLoyWlLEECXftyIOeNavvXbe = 0.008
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.cosine_beta_max = 999.
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.cosine_t_max = math.atan(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.cosine_beta_max * (1. + rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.zPdwEaBmJLoyWlLEECXftyIOeNavvXbe) / math.pi) * 2. * (
                        1. + rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.zPdwEaBmJLoyWlLEECXftyIOeNavvXbe) / math.pi - rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.zPdwEaBmJLoyWlLEECXftyIOeNavvXbe
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.cosine_log_alpha_0 = math.DJwhOGBaLcOjmXnuwXMXOyhMtknqkKXL(math.cos(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.zPdwEaBmJLoyWlLEECXftyIOeNavvXbe / (1. + rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.zPdwEaBmJLoyWlLEECXftyIOeNavvXbe) * math.pi / 2.))
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.HtnYKlBDuwwBEVdTVKsUENSQHeXnhZXs = HtnYKlBDuwwBEVdTVKsUENSQHeXnhZXs
            if HtnYKlBDuwwBEVdTVKsUENSQHeXnhZXs == 'cosine':
                rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.T = 0.9946
            else:
                rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.T = 1.
    def rbFJZghBKIbgXbmpNDbwzjVehrMOJUAI(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz):
        if rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.HtnYKlBDuwwBEVdTVKsUENSQHeXnhZXs == 'discrete':
            return YcCWLCgdGWkdmvnGxsHCCaNMxPgfJjif(XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz.reshape((-1, 1)), rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.t_array.sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ(XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz.fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc),
                                  rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.log_alpha_array.sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ(XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz.fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc)).reshape((-1))
        elif rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.HtnYKlBDuwwBEVdTVKsUENSQHeXnhZXs == 'linear':
            return -0.25 * XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz ** 2 * (rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.beta_1 - rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.beta_0) - 0.5 * XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz * rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.beta_0
        elif rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.HtnYKlBDuwwBEVdTVKsUENSQHeXnhZXs == 'cosine':
            CfXuYTFBezuxiyscOIHaKGcmlCVcFEZJ = lambda uPePujIqMVDrwNvZQxJajkuaQFAcacjA: torch.DJwhOGBaLcOjmXnuwXMXOyhMtknqkKXL(torch.cos((uPePujIqMVDrwNvZQxJajkuaQFAcacjA + rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.zPdwEaBmJLoyWlLEECXftyIOeNavvXbe) / (1. + rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.zPdwEaBmJLoyWlLEECXftyIOeNavvXbe) * math.pi / 2.))
            mQPxqKCwqnypKeTKHMQHncgoVnRYGQoB = CfXuYTFBezuxiyscOIHaKGcmlCVcFEZJ(XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz) - rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.cosine_log_alpha_0
            return mQPxqKCwqnypKeTKHMQHncgoVnRYGQoB
    def vIxEBJoJGQoaEsxWgtAKNAwmfBFoAluV(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz):
        return torch.exp(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.rbFJZghBKIbgXbmpNDbwzjVehrMOJUAI(XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz))
    def uVXtYzlfVxHwJkqqdjvYpiPZXHJTGDgn(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz):
        return torch.sqrt(1. - torch.exp(2. * rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.rbFJZghBKIbgXbmpNDbwzjVehrMOJUAI(XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz)))
    def iLJAxGawPgVbuzyTPlMNDawbjHhwvWaG(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz):
        dVYEsJMItyLBHztFFfKqnGBmSuZKBfAQ = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.rbFJZghBKIbgXbmpNDbwzjVehrMOJUAI(XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz)
        piAmEXJbyGyOPpPiVFWXstacRzFwBCaO = 0.5 * torch.DJwhOGBaLcOjmXnuwXMXOyhMtknqkKXL(1. - torch.exp(2. * dVYEsJMItyLBHztFFfKqnGBmSuZKBfAQ))
        return dVYEsJMItyLBHztFFfKqnGBmSuZKBfAQ - piAmEXJbyGyOPpPiVFWXstacRzFwBCaO
    def wdxFGSVLvnnzjandRpvORBqdoTWJHGVq(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, lamb):
        if rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.HtnYKlBDuwwBEVdTVKsUENSQHeXnhZXs == 'linear':
            YWVfQWNLFkgyFcvNlvhXIEmOhVSQEsoA = 2. * (rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.beta_1 - rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.beta_0) * torch.logaddexp(-2. * lamb, torch.zeros((1,)).sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ(lamb))
            SLoorigJzPhJlrJAYpKOSDwDKmGeGYch = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.beta_0 ** 2 + YWVfQWNLFkgyFcvNlvhXIEmOhVSQEsoA
            return YWVfQWNLFkgyFcvNlvhXIEmOhVSQEsoA / (torch.sqrt(SLoorigJzPhJlrJAYpKOSDwDKmGeGYch) + rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.beta_0) / (rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.beta_1 - rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.beta_0)
        elif rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.HtnYKlBDuwwBEVdTVKsUENSQHeXnhZXs == 'discrete':
            log_alpha = -0.5 * torch.logaddexp(torch.zeros((1,)).sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ(lamb.fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc), -2. * lamb)
            XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz = YcCWLCgdGWkdmvnGxsHCCaNMxPgfJjif(log_alpha.reshape((-1, 1)), torch.hAHyMhlDympwYBnEsaNWPsolDQrxyovx(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.log_alpha_array.sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ(lamb.fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc), [1]),
                               torch.hAHyMhlDympwYBnEsaNWPsolDQrxyovx(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.t_array.sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ(lamb.fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc), [1]))
            return XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz.reshape((-1,))
        else:
            log_alpha = -0.5 * torch.logaddexp(-2. * lamb, torch.zeros((1,)).sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ(lamb))
            ocNKgMRHAumlFztHlKLWFgphgoqSohMJ = lambda mQPxqKCwqnypKeTKHMQHncgoVnRYGQoB: torch.arccos(torch.exp(mQPxqKCwqnypKeTKHMQHncgoVnRYGQoB + rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.cosine_log_alpha_0)) * 2. * (
                        1. + rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.zPdwEaBmJLoyWlLEECXftyIOeNavvXbe) / math.pi - rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.zPdwEaBmJLoyWlLEECXftyIOeNavvXbe
            XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz = ocNKgMRHAumlFztHlKLWFgphgoqSohMJ(log_alpha)
            return XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz
def ZYOLpUhfVlCKqyjorQDawzHnmpUuDMco(
        VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM,
        noise_schedule,
        SZAVLBSfrTycZhmQUtWaVvoZUmpPNFnx="noise",
        eyENQJAyFTcaaoUTdKKuMPYftXwUWQog={},
        pHuETgbqIiqsDXsGxOxcVUpWdCrZQXpg="uncond",
        WjZIxXvCKJjhJEOixkDhHVKnlvFrhlwx=None,
        ocqvRjqLBftHXYHwpMQOsKEyGTmEGEZr=None,
        nMskTBKMFLhxYBlOqQofJpFZPCIgbKtX=1.,
        CMaKZRMESEyFWKtajMtYlJFrasLcFaTM=None,
        qzMIffBAonPqGkjVTXVHmKVvJsfmyjgi={},
):
    def cQMIOfhFnsqvzxfDuSWaXOlohEVKCdjW(cWUcAVejbxRLAUQxLneZxdtehAPjqiEP):
        if noise_schedule.HtnYKlBDuwwBEVdTVKsUENSQHeXnhZXs == 'discrete':
            return (cWUcAVejbxRLAUQxLneZxdtehAPjqiEP - 1. / noise_schedule.total_N) * 1000.
        else:
            return cWUcAVejbxRLAUQxLneZxdtehAPjqiEP
    def gHvdFIXWnpdBABVDOyCibbWXkPBFotTD(NECAaWUrFGIXcLimrerEYmxYIykQBfXb, cWUcAVejbxRLAUQxLneZxdtehAPjqiEP, BuoWBAnnMxyvqTGoSTHbQAlvPFWHbuUf=None):
        if cWUcAVejbxRLAUQxLneZxdtehAPjqiEP.reshape((-1,)).BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[0] == 1:
            cWUcAVejbxRLAUQxLneZxdtehAPjqiEP = cWUcAVejbxRLAUQxLneZxdtehAPjqiEP.expand((NECAaWUrFGIXcLimrerEYmxYIykQBfXb.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[0]))
        TkthPTkbiaqIpNjVjJVbTRxzTfpudvHy = cQMIOfhFnsqvzxfDuSWaXOlohEVKCdjW(cWUcAVejbxRLAUQxLneZxdtehAPjqiEP)
        if BuoWBAnnMxyvqTGoSTHbQAlvPFWHbuUf is None:
            pwTxzdNTJGMWEFORftJTEtPYMMiKwDuP = VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM(NECAaWUrFGIXcLimrerEYmxYIykQBfXb, TkthPTkbiaqIpNjVjJVbTRxzTfpudvHy, **eyENQJAyFTcaaoUTdKKuMPYftXwUWQog)
        else:
            pwTxzdNTJGMWEFORftJTEtPYMMiKwDuP = VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM(NECAaWUrFGIXcLimrerEYmxYIykQBfXb, TkthPTkbiaqIpNjVjJVbTRxzTfpudvHy, BuoWBAnnMxyvqTGoSTHbQAlvPFWHbuUf, **eyENQJAyFTcaaoUTdKKuMPYftXwUWQog)
        if SZAVLBSfrTycZhmQUtWaVvoZUmpPNFnx == "noise":
            return pwTxzdNTJGMWEFORftJTEtPYMMiKwDuP
        elif SZAVLBSfrTycZhmQUtWaVvoZUmpPNFnx == "x_start":
            WJsAttAlgEhvijNBnbITSLwwTXOxBfNI, zhpCBYkwQkhgdrClReoQrMdATdSZEHOs = noise_schedule.vIxEBJoJGQoaEsxWgtAKNAwmfBFoAluV(cWUcAVejbxRLAUQxLneZxdtehAPjqiEP), noise_schedule.uVXtYzlfVxHwJkqqdjvYpiPZXHJTGDgn(cWUcAVejbxRLAUQxLneZxdtehAPjqiEP)
            ipYTWVOPDpfJXeTFApPIgldytQSaUFdk = NECAaWUrFGIXcLimrerEYmxYIykQBfXb.yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk()
            return (NECAaWUrFGIXcLimrerEYmxYIykQBfXb - PpKdefOZNalnbKKPZYEFkTizePccpchH(WJsAttAlgEhvijNBnbITSLwwTXOxBfNI, ipYTWVOPDpfJXeTFApPIgldytQSaUFdk) * pwTxzdNTJGMWEFORftJTEtPYMMiKwDuP) / PpKdefOZNalnbKKPZYEFkTizePccpchH(zhpCBYkwQkhgdrClReoQrMdATdSZEHOs, ipYTWVOPDpfJXeTFApPIgldytQSaUFdk)
        elif SZAVLBSfrTycZhmQUtWaVvoZUmpPNFnx == "v":
            WJsAttAlgEhvijNBnbITSLwwTXOxBfNI, zhpCBYkwQkhgdrClReoQrMdATdSZEHOs = noise_schedule.vIxEBJoJGQoaEsxWgtAKNAwmfBFoAluV(cWUcAVejbxRLAUQxLneZxdtehAPjqiEP), noise_schedule.uVXtYzlfVxHwJkqqdjvYpiPZXHJTGDgn(cWUcAVejbxRLAUQxLneZxdtehAPjqiEP)
            ipYTWVOPDpfJXeTFApPIgldytQSaUFdk = NECAaWUrFGIXcLimrerEYmxYIykQBfXb.yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk()
            return PpKdefOZNalnbKKPZYEFkTizePccpchH(WJsAttAlgEhvijNBnbITSLwwTXOxBfNI, ipYTWVOPDpfJXeTFApPIgldytQSaUFdk) * pwTxzdNTJGMWEFORftJTEtPYMMiKwDuP + PpKdefOZNalnbKKPZYEFkTizePccpchH(zhpCBYkwQkhgdrClReoQrMdATdSZEHOs, ipYTWVOPDpfJXeTFApPIgldytQSaUFdk) * NECAaWUrFGIXcLimrerEYmxYIykQBfXb
        elif SZAVLBSfrTycZhmQUtWaVvoZUmpPNFnx == "score":
            zhpCBYkwQkhgdrClReoQrMdATdSZEHOs = noise_schedule.uVXtYzlfVxHwJkqqdjvYpiPZXHJTGDgn(cWUcAVejbxRLAUQxLneZxdtehAPjqiEP)
            ipYTWVOPDpfJXeTFApPIgldytQSaUFdk = NECAaWUrFGIXcLimrerEYmxYIykQBfXb.yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk()
            return -PpKdefOZNalnbKKPZYEFkTizePccpchH(zhpCBYkwQkhgdrClReoQrMdATdSZEHOs, ipYTWVOPDpfJXeTFApPIgldytQSaUFdk) * pwTxzdNTJGMWEFORftJTEtPYMMiKwDuP
    def ppCwMUYceqvtJMtMlOjvhPSUpkBXVReA(NECAaWUrFGIXcLimrerEYmxYIykQBfXb, TkthPTkbiaqIpNjVjJVbTRxzTfpudvHy):
        with torch.enable_grad():
            pZoNxoVtAYgcFKlLqYosAEKjqMzwRmNs = NECAaWUrFGIXcLimrerEYmxYIykQBfXb.detach().requires_grad_(True)
            leYBEyQVOGNFjYhLrxWgefjUHtZwnRUw = CMaKZRMESEyFWKtajMtYlJFrasLcFaTM(pZoNxoVtAYgcFKlLqYosAEKjqMzwRmNs, TkthPTkbiaqIpNjVjJVbTRxzTfpudvHy, WjZIxXvCKJjhJEOixkDhHVKnlvFrhlwx, **qzMIffBAonPqGkjVTXVHmKVvJsfmyjgi)
            return torch.autograd.grad(leYBEyQVOGNFjYhLrxWgefjUHtZwnRUw.sum(), pZoNxoVtAYgcFKlLqYosAEKjqMzwRmNs)[0]
    def NRtnQQOkbUbfnbxzIRWvMfkdGBlGyoSB(NECAaWUrFGIXcLimrerEYmxYIykQBfXb, cWUcAVejbxRLAUQxLneZxdtehAPjqiEP):
        if cWUcAVejbxRLAUQxLneZxdtehAPjqiEP.reshape((-1,)).BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[0] == 1:
            cWUcAVejbxRLAUQxLneZxdtehAPjqiEP = cWUcAVejbxRLAUQxLneZxdtehAPjqiEP.expand((NECAaWUrFGIXcLimrerEYmxYIykQBfXb.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[0]))
        if pHuETgbqIiqsDXsGxOxcVUpWdCrZQXpg == "uncond":
            return gHvdFIXWnpdBABVDOyCibbWXkPBFotTD(NECAaWUrFGIXcLimrerEYmxYIykQBfXb, cWUcAVejbxRLAUQxLneZxdtehAPjqiEP)
        elif pHuETgbqIiqsDXsGxOxcVUpWdCrZQXpg == "classifier":
            assert CMaKZRMESEyFWKtajMtYlJFrasLcFaTM is not None
            TkthPTkbiaqIpNjVjJVbTRxzTfpudvHy = cQMIOfhFnsqvzxfDuSWaXOlohEVKCdjW(cWUcAVejbxRLAUQxLneZxdtehAPjqiEP)
            CGUJEsRmtLvzZgcOPhDPRVKuAfpIFlDl = ppCwMUYceqvtJMtMlOjvhPSUpkBXVReA(NECAaWUrFGIXcLimrerEYmxYIykQBfXb, TkthPTkbiaqIpNjVjJVbTRxzTfpudvHy)
            zhpCBYkwQkhgdrClReoQrMdATdSZEHOs = noise_schedule.uVXtYzlfVxHwJkqqdjvYpiPZXHJTGDgn(cWUcAVejbxRLAUQxLneZxdtehAPjqiEP)
            jCizDlbKxNNChDZcMjnDhRYUQUZdrTRD = gHvdFIXWnpdBABVDOyCibbWXkPBFotTD(NECAaWUrFGIXcLimrerEYmxYIykQBfXb, cWUcAVejbxRLAUQxLneZxdtehAPjqiEP)
            return jCizDlbKxNNChDZcMjnDhRYUQUZdrTRD - nMskTBKMFLhxYBlOqQofJpFZPCIgbKtX * PpKdefOZNalnbKKPZYEFkTizePccpchH(zhpCBYkwQkhgdrClReoQrMdATdSZEHOs, ipYTWVOPDpfJXeTFApPIgldytQSaUFdk=CGUJEsRmtLvzZgcOPhDPRVKuAfpIFlDl.yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk()) * CGUJEsRmtLvzZgcOPhDPRVKuAfpIFlDl
        elif pHuETgbqIiqsDXsGxOxcVUpWdCrZQXpg == "classifier-free":
            if nMskTBKMFLhxYBlOqQofJpFZPCIgbKtX == 1. or ocqvRjqLBftHXYHwpMQOsKEyGTmEGEZr is None:
                return gHvdFIXWnpdBABVDOyCibbWXkPBFotTD(NECAaWUrFGIXcLimrerEYmxYIykQBfXb, cWUcAVejbxRLAUQxLneZxdtehAPjqiEP, BuoWBAnnMxyvqTGoSTHbQAlvPFWHbuUf=WjZIxXvCKJjhJEOixkDhHVKnlvFrhlwx)
            else:
                pZoNxoVtAYgcFKlLqYosAEKjqMzwRmNs = torch.cat([NECAaWUrFGIXcLimrerEYmxYIykQBfXb] * 2)
                xTGvTRTnrzNeWShiGfMbhVhxqQzWXDWU = torch.cat([cWUcAVejbxRLAUQxLneZxdtehAPjqiEP] * 2)
                if isinstance(WjZIxXvCKJjhJEOixkDhHVKnlvFrhlwx, dict):
                    assert isinstance(ocqvRjqLBftHXYHwpMQOsKEyGTmEGEZr, dict)
                    dfJKHENBxSWlCdWWoJqBdANPeXpCQuEv = dict()
                    for EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm in WjZIxXvCKJjhJEOixkDhHVKnlvFrhlwx:
                        if isinstance(WjZIxXvCKJjhJEOixkDhHVKnlvFrhlwx[EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm], list):
                            dfJKHENBxSWlCdWWoJqBdANPeXpCQuEv[EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm] = [torch.cat([ocqvRjqLBftHXYHwpMQOsKEyGTmEGEZr[EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm][HCXmerBqIMuTscBONzTGKYapYSxWTYHo], WjZIxXvCKJjhJEOixkDhHVKnlvFrhlwx[EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm][HCXmerBqIMuTscBONzTGKYapYSxWTYHo]]) for HCXmerBqIMuTscBONzTGKYapYSxWTYHo in range(len(WjZIxXvCKJjhJEOixkDhHVKnlvFrhlwx[EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm]))]
                        else:
                            dfJKHENBxSWlCdWWoJqBdANPeXpCQuEv[EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm] = torch.cat([ocqvRjqLBftHXYHwpMQOsKEyGTmEGEZr[EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm], WjZIxXvCKJjhJEOixkDhHVKnlvFrhlwx[EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm]])
                else:
                    dfJKHENBxSWlCdWWoJqBdANPeXpCQuEv = torch.cat([ocqvRjqLBftHXYHwpMQOsKEyGTmEGEZr, WjZIxXvCKJjhJEOixkDhHVKnlvFrhlwx])
                IaLcqonkYZBjFcVFMuukCErRqglKFVYa, jCizDlbKxNNChDZcMjnDhRYUQUZdrTRD = gHvdFIXWnpdBABVDOyCibbWXkPBFotTD(pZoNxoVtAYgcFKlLqYosAEKjqMzwRmNs, xTGvTRTnrzNeWShiGfMbhVhxqQzWXDWU, BuoWBAnnMxyvqTGoSTHbQAlvPFWHbuUf=dfJKHENBxSWlCdWWoJqBdANPeXpCQuEv).ebMwMGDmpDsmyMtCQfGxUhZuVHvTpavF(2)
                return IaLcqonkYZBjFcVFMuukCErRqglKFVYa + nMskTBKMFLhxYBlOqQofJpFZPCIgbKtX * (jCizDlbKxNNChDZcMjnDhRYUQUZdrTRD - IaLcqonkYZBjFcVFMuukCErRqglKFVYa)
    assert SZAVLBSfrTycZhmQUtWaVvoZUmpPNFnx in ["noise", "x_start", "v"]
    assert pHuETgbqIiqsDXsGxOxcVUpWdCrZQXpg in ["uncond", "classifier", "classifier-free"]
    return NRtnQQOkbUbfnbxzIRWvMfkdGBlGyoSB
class BpJFvwrXhkvrLnVItfIVGAIbkDzXgZOo:
    def __init__(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, NRtnQQOkbUbfnbxzIRWvMfkdGBlGyoSB, noise_schedule, predict_x0=False, thresholding=False, max_val=1.):
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM = NRtnQQOkbUbfnbxzIRWvMfkdGBlGyoSB
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.noise_schedule = noise_schedule
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.predict_x0 = predict_x0
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.thresholding = thresholding
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.max_val = max_val
    def bNiIErgJWlnCGkgXsykdfDBpuYqNkmzV(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, NECAaWUrFGIXcLimrerEYmxYIykQBfXb, XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz):
        return rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM(NECAaWUrFGIXcLimrerEYmxYIykQBfXb, XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz)
    def EYuWlTpOaArJlsTpDQxQKmGmreBuNyqQ(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, NECAaWUrFGIXcLimrerEYmxYIykQBfXb, XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz):
        jCizDlbKxNNChDZcMjnDhRYUQUZdrTRD = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.bNiIErgJWlnCGkgXsykdfDBpuYqNkmzV(NECAaWUrFGIXcLimrerEYmxYIykQBfXb, XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz)
        ipYTWVOPDpfJXeTFApPIgldytQSaUFdk = NECAaWUrFGIXcLimrerEYmxYIykQBfXb.yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk()
        WJsAttAlgEhvijNBnbITSLwwTXOxBfNI, zhpCBYkwQkhgdrClReoQrMdATdSZEHOs = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.noise_schedule.vIxEBJoJGQoaEsxWgtAKNAwmfBFoAluV(XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz), rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.noise_schedule.uVXtYzlfVxHwJkqqdjvYpiPZXHJTGDgn(XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz)
        UBGvtPbFIPlcsBIwyWKuWMZeENGLMRAP = (NECAaWUrFGIXcLimrerEYmxYIykQBfXb - PpKdefOZNalnbKKPZYEFkTizePccpchH(zhpCBYkwQkhgdrClReoQrMdATdSZEHOs, ipYTWVOPDpfJXeTFApPIgldytQSaUFdk) * jCizDlbKxNNChDZcMjnDhRYUQUZdrTRD) / PpKdefOZNalnbKKPZYEFkTizePccpchH(WJsAttAlgEhvijNBnbITSLwwTXOxBfNI, ipYTWVOPDpfJXeTFApPIgldytQSaUFdk)
        if rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.thresholding:
            HutkrxeXIuRQKOhCWHkiwqLGAsJjUSKj = 0.995  
            uPePujIqMVDrwNvZQxJajkuaQFAcacjA = torch.quantile(torch.abs(UBGvtPbFIPlcsBIwyWKuWMZeENGLMRAP).reshape((UBGvtPbFIPlcsBIwyWKuWMZeENGLMRAP.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[0], -1)), HutkrxeXIuRQKOhCWHkiwqLGAsJjUSKj, yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk=1)
            uPePujIqMVDrwNvZQxJajkuaQFAcacjA = PpKdefOZNalnbKKPZYEFkTizePccpchH(torch.maximum(uPePujIqMVDrwNvZQxJajkuaQFAcacjA, rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.max_val * torch.ones_like(uPePujIqMVDrwNvZQxJajkuaQFAcacjA).sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ(uPePujIqMVDrwNvZQxJajkuaQFAcacjA.fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc)), ipYTWVOPDpfJXeTFApPIgldytQSaUFdk)
            UBGvtPbFIPlcsBIwyWKuWMZeENGLMRAP = torch.clamp(UBGvtPbFIPlcsBIwyWKuWMZeENGLMRAP, -uPePujIqMVDrwNvZQxJajkuaQFAcacjA, uPePujIqMVDrwNvZQxJajkuaQFAcacjA) / uPePujIqMVDrwNvZQxJajkuaQFAcacjA
        return UBGvtPbFIPlcsBIwyWKuWMZeENGLMRAP
    def NRtnQQOkbUbfnbxzIRWvMfkdGBlGyoSB(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, NECAaWUrFGIXcLimrerEYmxYIykQBfXb, XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz):
        if rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.predict_x0:
            return rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.EYuWlTpOaArJlsTpDQxQKmGmreBuNyqQ(NECAaWUrFGIXcLimrerEYmxYIykQBfXb, XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz)
        else:
            return rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.bNiIErgJWlnCGkgXsykdfDBpuYqNkmzV(NECAaWUrFGIXcLimrerEYmxYIykQBfXb, XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz)
    def ElndQeTbOYtRDqLuGQeraWztpYSiBrGs(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, UTnGvkbfsgLpbYIDcBiyoRRbDkNDhDWP, mHINwRyYsqlVpxxfXBXtIPLPWtuKirPb, cGnQXRSvlLSuUVfhDJjlqWnweLUeQVRQ, CkYaWzCjmffLyFAjukkxYTtrfjqQGpts, fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc):
        if UTnGvkbfsgLpbYIDcBiyoRRbDkNDhDWP == 'logSNR':
            vzOtFORKjOZFyzfvjiHnxZWEXuIHRwUl = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.noise_schedule.iLJAxGawPgVbuzyTPlMNDawbjHhwvWaG(torch.xPmCFphFKpGMpIsczaSKHmMgRPZzJwla(mHINwRyYsqlVpxxfXBXtIPLPWtuKirPb).sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ(fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc))
            rlgMzMCTGtPbLYjftQCikhppVMmPJmPh = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.noise_schedule.iLJAxGawPgVbuzyTPlMNDawbjHhwvWaG(torch.xPmCFphFKpGMpIsczaSKHmMgRPZzJwla(cGnQXRSvlLSuUVfhDJjlqWnweLUeQVRQ).sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ(fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc))
            dxaBnvuhwFFaaAfgPsYRCpvAQMDPcqzg = torch.linspace(vzOtFORKjOZFyzfvjiHnxZWEXuIHRwUl.cpu().ygFiYnqtfEqFJmbillPxtHRxsUoFqqJk(), rlgMzMCTGtPbLYjftQCikhppVMmPJmPh.cpu().ygFiYnqtfEqFJmbillPxtHRxsUoFqqJk(), CkYaWzCjmffLyFAjukkxYTtrfjqQGpts + 1).sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ(fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc)
            return rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.noise_schedule.wdxFGSVLvnnzjandRpvORBqdoTWJHGVq(dxaBnvuhwFFaaAfgPsYRCpvAQMDPcqzg)
        elif UTnGvkbfsgLpbYIDcBiyoRRbDkNDhDWP == 'time_uniform':
            return torch.linspace(mHINwRyYsqlVpxxfXBXtIPLPWtuKirPb, cGnQXRSvlLSuUVfhDJjlqWnweLUeQVRQ, CkYaWzCjmffLyFAjukkxYTtrfjqQGpts + 1).sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ(fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc)
        elif UTnGvkbfsgLpbYIDcBiyoRRbDkNDhDWP == 'time_quadratic':
            cLWsJtOZVzyWkycWpHRNpXArjvgDTWtc = 2
            XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz = torch.linspace(mHINwRyYsqlVpxxfXBXtIPLPWtuKirPb ** (1. / cLWsJtOZVzyWkycWpHRNpXArjvgDTWtc), cGnQXRSvlLSuUVfhDJjlqWnweLUeQVRQ ** (1. / cLWsJtOZVzyWkycWpHRNpXArjvgDTWtc), CkYaWzCjmffLyFAjukkxYTtrfjqQGpts + 1).pow(cLWsJtOZVzyWkycWpHRNpXArjvgDTWtc).sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ(fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc)
            return XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz
        else:
            raise ValueError(
                "Unsupported skip_type {}, need to be 'logSNR' or 'time_uniform' or 'time_quadratic'".format(UTnGvkbfsgLpbYIDcBiyoRRbDkNDhDWP))
    def OzGAVUZhZNxvvNdRVOEiOFXPHiFcoPXh(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, TMepbhrhtxHODfHDPkWDjgPPPikciJwm, wXwbcvVCQXFmEpNuIRIfbkuOtOpqgUXt, UTnGvkbfsgLpbYIDcBiyoRRbDkNDhDWP, mHINwRyYsqlVpxxfXBXtIPLPWtuKirPb, cGnQXRSvlLSuUVfhDJjlqWnweLUeQVRQ, fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc):
        if wXwbcvVCQXFmEpNuIRIfbkuOtOpqgUXt == 3:
            aNvhFlguADxtQkYwCswjOmevkulEaSVC = TMepbhrhtxHODfHDPkWDjgPPPikciJwm // 3 + 1
            if TMepbhrhtxHODfHDPkWDjgPPPikciJwm % 3 == 0:
                CfVKhsKPtOaiLDSyReEIATrYxiCnFRUx = [3, ] * (aNvhFlguADxtQkYwCswjOmevkulEaSVC - 2) + [2, 1]
            elif TMepbhrhtxHODfHDPkWDjgPPPikciJwm % 3 == 1:
                CfVKhsKPtOaiLDSyReEIATrYxiCnFRUx = [3, ] * (aNvhFlguADxtQkYwCswjOmevkulEaSVC - 1) + [1]
            else:
                CfVKhsKPtOaiLDSyReEIATrYxiCnFRUx = [3, ] * (aNvhFlguADxtQkYwCswjOmevkulEaSVC - 1) + [2]
        elif wXwbcvVCQXFmEpNuIRIfbkuOtOpqgUXt == 2:
            if TMepbhrhtxHODfHDPkWDjgPPPikciJwm % 2 == 0:
                aNvhFlguADxtQkYwCswjOmevkulEaSVC = TMepbhrhtxHODfHDPkWDjgPPPikciJwm // 2
                CfVKhsKPtOaiLDSyReEIATrYxiCnFRUx = [2, ] * aNvhFlguADxtQkYwCswjOmevkulEaSVC
            else:
                aNvhFlguADxtQkYwCswjOmevkulEaSVC = TMepbhrhtxHODfHDPkWDjgPPPikciJwm // 2 + 1
                CfVKhsKPtOaiLDSyReEIATrYxiCnFRUx = [2, ] * (aNvhFlguADxtQkYwCswjOmevkulEaSVC - 1) + [1]
        elif wXwbcvVCQXFmEpNuIRIfbkuOtOpqgUXt == 1:
            aNvhFlguADxtQkYwCswjOmevkulEaSVC = 1
            CfVKhsKPtOaiLDSyReEIATrYxiCnFRUx = [1, ] * TMepbhrhtxHODfHDPkWDjgPPPikciJwm
        else:
            raise ValueError("'order' must be '1' or '2' or '3'.")
        if UTnGvkbfsgLpbYIDcBiyoRRbDkNDhDWP == 'logSNR':
            coSeFJMSLBWMYiIkaNMRNLvdHvyQfsub = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.ElndQeTbOYtRDqLuGQeraWztpYSiBrGs(UTnGvkbfsgLpbYIDcBiyoRRbDkNDhDWP, mHINwRyYsqlVpxxfXBXtIPLPWtuKirPb, cGnQXRSvlLSuUVfhDJjlqWnweLUeQVRQ, aNvhFlguADxtQkYwCswjOmevkulEaSVC, fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc)
        else:
            coSeFJMSLBWMYiIkaNMRNLvdHvyQfsub = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.ElndQeTbOYtRDqLuGQeraWztpYSiBrGs(UTnGvkbfsgLpbYIDcBiyoRRbDkNDhDWP, mHINwRyYsqlVpxxfXBXtIPLPWtuKirPb, cGnQXRSvlLSuUVfhDJjlqWnweLUeQVRQ, TMepbhrhtxHODfHDPkWDjgPPPikciJwm, fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc)[
                torch.cumsum(torch.xPmCFphFKpGMpIsczaSKHmMgRPZzJwla([0, ] + CfVKhsKPtOaiLDSyReEIATrYxiCnFRUx)).sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ(fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc)]
        return coSeFJMSLBWMYiIkaNMRNLvdHvyQfsub, CfVKhsKPtOaiLDSyReEIATrYxiCnFRUx
    def zICaXPrVsokCiDEggpgVRYpzbYydrnAQ(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, NECAaWUrFGIXcLimrerEYmxYIykQBfXb, uPePujIqMVDrwNvZQxJajkuaQFAcacjA):
        return rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.EYuWlTpOaArJlsTpDQxQKmGmreBuNyqQ(NECAaWUrFGIXcLimrerEYmxYIykQBfXb, uPePujIqMVDrwNvZQxJajkuaQFAcacjA)
    def zePJdCbCboaUjzbpiWXxZbXDFHTzATZX(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, NECAaWUrFGIXcLimrerEYmxYIykQBfXb, uPePujIqMVDrwNvZQxJajkuaQFAcacjA, XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz, JKpyVMrnPSyIBxYqPUjWKtnFnXIMmXeu=None, vjtZlQMIzMiiNQGEDKNLZnhxTIPtimCl=False):
        jfvFkkyrHbvxGpVllCdQKVvBSNiKEJLj = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.noise_schedule
        ipYTWVOPDpfJXeTFApPIgldytQSaUFdk = NECAaWUrFGIXcLimrerEYmxYIykQBfXb.yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk()
        vhxMVZkWRybktsQdWBSYgKuXhuebDAKO, kumWCHxVTklyDOVOZlvEdFyJtcLshKec = jfvFkkyrHbvxGpVllCdQKVvBSNiKEJLj.iLJAxGawPgVbuzyTPlMNDawbjHhwvWaG(uPePujIqMVDrwNvZQxJajkuaQFAcacjA), jfvFkkyrHbvxGpVllCdQKVvBSNiKEJLj.iLJAxGawPgVbuzyTPlMNDawbjHhwvWaG(XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz)
        xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab = kumWCHxVTklyDOVOZlvEdFyJtcLshKec - vhxMVZkWRybktsQdWBSYgKuXhuebDAKO
        YLNizBEwkhwwTzMoRAXZSNCzobIasIFG, mQPxqKCwqnypKeTKHMQHncgoVnRYGQoB = jfvFkkyrHbvxGpVllCdQKVvBSNiKEJLj.rbFJZghBKIbgXbmpNDbwzjVehrMOJUAI(uPePujIqMVDrwNvZQxJajkuaQFAcacjA), jfvFkkyrHbvxGpVllCdQKVvBSNiKEJLj.rbFJZghBKIbgXbmpNDbwzjVehrMOJUAI(XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz)
        hdTNoSkElMdkMBosbtxRTPZtRzspQDxC, zhpCBYkwQkhgdrClReoQrMdATdSZEHOs = jfvFkkyrHbvxGpVllCdQKVvBSNiKEJLj.uVXtYzlfVxHwJkqqdjvYpiPZXHJTGDgn(uPePujIqMVDrwNvZQxJajkuaQFAcacjA), jfvFkkyrHbvxGpVllCdQKVvBSNiKEJLj.uVXtYzlfVxHwJkqqdjvYpiPZXHJTGDgn(XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz)
        WJsAttAlgEhvijNBnbITSLwwTXOxBfNI = torch.exp(mQPxqKCwqnypKeTKHMQHncgoVnRYGQoB)
        if rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.predict_x0:
            AgzQHYUBcAtZwocfZDsAQtNEVTrztNYP = torch.expm1(-xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab)
            if JKpyVMrnPSyIBxYqPUjWKtnFnXIMmXeu is None:
                JKpyVMrnPSyIBxYqPUjWKtnFnXIMmXeu = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.NRtnQQOkbUbfnbxzIRWvMfkdGBlGyoSB(NECAaWUrFGIXcLimrerEYmxYIykQBfXb, uPePujIqMVDrwNvZQxJajkuaQFAcacjA)
            VnmAPlKFRKPJNjSTgsTtFHxWSelTupCY = (
                    PpKdefOZNalnbKKPZYEFkTizePccpchH(zhpCBYkwQkhgdrClReoQrMdATdSZEHOs / hdTNoSkElMdkMBosbtxRTPZtRzspQDxC, ipYTWVOPDpfJXeTFApPIgldytQSaUFdk) * NECAaWUrFGIXcLimrerEYmxYIykQBfXb
                    - PpKdefOZNalnbKKPZYEFkTizePccpchH(WJsAttAlgEhvijNBnbITSLwwTXOxBfNI * AgzQHYUBcAtZwocfZDsAQtNEVTrztNYP, ipYTWVOPDpfJXeTFApPIgldytQSaUFdk) * JKpyVMrnPSyIBxYqPUjWKtnFnXIMmXeu
            )
            if vjtZlQMIzMiiNQGEDKNLZnhxTIPtimCl:
                return VnmAPlKFRKPJNjSTgsTtFHxWSelTupCY, {'model_s': JKpyVMrnPSyIBxYqPUjWKtnFnXIMmXeu}
            else:
                return VnmAPlKFRKPJNjSTgsTtFHxWSelTupCY
        else:
            AgzQHYUBcAtZwocfZDsAQtNEVTrztNYP = torch.expm1(xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab)
            if JKpyVMrnPSyIBxYqPUjWKtnFnXIMmXeu is None:
                JKpyVMrnPSyIBxYqPUjWKtnFnXIMmXeu = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.NRtnQQOkbUbfnbxzIRWvMfkdGBlGyoSB(NECAaWUrFGIXcLimrerEYmxYIykQBfXb, uPePujIqMVDrwNvZQxJajkuaQFAcacjA)
            VnmAPlKFRKPJNjSTgsTtFHxWSelTupCY = (
                    PpKdefOZNalnbKKPZYEFkTizePccpchH(torch.exp(mQPxqKCwqnypKeTKHMQHncgoVnRYGQoB - YLNizBEwkhwwTzMoRAXZSNCzobIasIFG), ipYTWVOPDpfJXeTFApPIgldytQSaUFdk) * NECAaWUrFGIXcLimrerEYmxYIykQBfXb
                    - PpKdefOZNalnbKKPZYEFkTizePccpchH(zhpCBYkwQkhgdrClReoQrMdATdSZEHOs * AgzQHYUBcAtZwocfZDsAQtNEVTrztNYP, ipYTWVOPDpfJXeTFApPIgldytQSaUFdk) * JKpyVMrnPSyIBxYqPUjWKtnFnXIMmXeu
            )
            if vjtZlQMIzMiiNQGEDKNLZnhxTIPtimCl:
                return VnmAPlKFRKPJNjSTgsTtFHxWSelTupCY, {'model_s': JKpyVMrnPSyIBxYqPUjWKtnFnXIMmXeu}
            else:
                return VnmAPlKFRKPJNjSTgsTtFHxWSelTupCY
    def cCvSYUlWQxEFngXCkZIfAYqQMynNlaPB(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, NECAaWUrFGIXcLimrerEYmxYIykQBfXb, uPePujIqMVDrwNvZQxJajkuaQFAcacjA, XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz, apACmNWgYmlQTXHPQlhMzlFpreaoNbwW=0.5, JKpyVMrnPSyIBxYqPUjWKtnFnXIMmXeu=None, vjtZlQMIzMiiNQGEDKNLZnhxTIPtimCl=False,
                                            clbgFKGfOFaPvTRBXwoouOOLgsSYaJzB='dpm_solver'):
        if clbgFKGfOFaPvTRBXwoouOOLgsSYaJzB not in ['dpm_solver', 'taylor']:
            raise ValueError("'solver_type' must be either 'dpm_solver' or 'taylor', got {}".format(clbgFKGfOFaPvTRBXwoouOOLgsSYaJzB))
        if apACmNWgYmlQTXHPQlhMzlFpreaoNbwW is None:
            apACmNWgYmlQTXHPQlhMzlFpreaoNbwW = 0.5
        jfvFkkyrHbvxGpVllCdQKVvBSNiKEJLj = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.noise_schedule
        ipYTWVOPDpfJXeTFApPIgldytQSaUFdk = NECAaWUrFGIXcLimrerEYmxYIykQBfXb.yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk()
        vhxMVZkWRybktsQdWBSYgKuXhuebDAKO, kumWCHxVTklyDOVOZlvEdFyJtcLshKec = jfvFkkyrHbvxGpVllCdQKVvBSNiKEJLj.iLJAxGawPgVbuzyTPlMNDawbjHhwvWaG(uPePujIqMVDrwNvZQxJajkuaQFAcacjA), jfvFkkyrHbvxGpVllCdQKVvBSNiKEJLj.iLJAxGawPgVbuzyTPlMNDawbjHhwvWaG(XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz)
        xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab = kumWCHxVTklyDOVOZlvEdFyJtcLshKec - vhxMVZkWRybktsQdWBSYgKuXhuebDAKO
        qmIrzgQJNFgnrrvhBvUBGJtKhFUVzszI = vhxMVZkWRybktsQdWBSYgKuXhuebDAKO + apACmNWgYmlQTXHPQlhMzlFpreaoNbwW * xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab
        XauksjEFAUvtInEaALXIwUhurkUuooOF = jfvFkkyrHbvxGpVllCdQKVvBSNiKEJLj.wdxFGSVLvnnzjandRpvORBqdoTWJHGVq(qmIrzgQJNFgnrrvhBvUBGJtKhFUVzszI)
        YLNizBEwkhwwTzMoRAXZSNCzobIasIFG, YLeGXzGjcVjvxDGyfGAGucPepbgHsKqE, mQPxqKCwqnypKeTKHMQHncgoVnRYGQoB = jfvFkkyrHbvxGpVllCdQKVvBSNiKEJLj.rbFJZghBKIbgXbmpNDbwzjVehrMOJUAI(uPePujIqMVDrwNvZQxJajkuaQFAcacjA), jfvFkkyrHbvxGpVllCdQKVvBSNiKEJLj.rbFJZghBKIbgXbmpNDbwzjVehrMOJUAI(
            XauksjEFAUvtInEaALXIwUhurkUuooOF), jfvFkkyrHbvxGpVllCdQKVvBSNiKEJLj.rbFJZghBKIbgXbmpNDbwzjVehrMOJUAI(XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz)
        hdTNoSkElMdkMBosbtxRTPZtRzspQDxC, TlgULUZaszhyUGEKkErfBSgAXIPYcRCZ, zhpCBYkwQkhgdrClReoQrMdATdSZEHOs = jfvFkkyrHbvxGpVllCdQKVvBSNiKEJLj.uVXtYzlfVxHwJkqqdjvYpiPZXHJTGDgn(uPePujIqMVDrwNvZQxJajkuaQFAcacjA), jfvFkkyrHbvxGpVllCdQKVvBSNiKEJLj.uVXtYzlfVxHwJkqqdjvYpiPZXHJTGDgn(XauksjEFAUvtInEaALXIwUhurkUuooOF), jfvFkkyrHbvxGpVllCdQKVvBSNiKEJLj.uVXtYzlfVxHwJkqqdjvYpiPZXHJTGDgn(XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz)
        EhCJvDsghNmTQVbhBOPGTzmcqijBZykL, WJsAttAlgEhvijNBnbITSLwwTXOxBfNI = torch.exp(YLeGXzGjcVjvxDGyfGAGucPepbgHsKqE), torch.exp(mQPxqKCwqnypKeTKHMQHncgoVnRYGQoB)
        if rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.predict_x0:
            KmpEUFqjzUzHgeFLOVLhmopBJNkHmXnn = torch.expm1(-apACmNWgYmlQTXHPQlhMzlFpreaoNbwW * xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab)
            AgzQHYUBcAtZwocfZDsAQtNEVTrztNYP = torch.expm1(-xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab)
            if JKpyVMrnPSyIBxYqPUjWKtnFnXIMmXeu is None:
                JKpyVMrnPSyIBxYqPUjWKtnFnXIMmXeu = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.NRtnQQOkbUbfnbxzIRWvMfkdGBlGyoSB(NECAaWUrFGIXcLimrerEYmxYIykQBfXb, uPePujIqMVDrwNvZQxJajkuaQFAcacjA)
            kgbUKBPJVlaLOrCgiKgtWPLImzSTTkUG = (
                    PpKdefOZNalnbKKPZYEFkTizePccpchH(TlgULUZaszhyUGEKkErfBSgAXIPYcRCZ / hdTNoSkElMdkMBosbtxRTPZtRzspQDxC, ipYTWVOPDpfJXeTFApPIgldytQSaUFdk) * NECAaWUrFGIXcLimrerEYmxYIykQBfXb
                    - PpKdefOZNalnbKKPZYEFkTizePccpchH(EhCJvDsghNmTQVbhBOPGTzmcqijBZykL * KmpEUFqjzUzHgeFLOVLhmopBJNkHmXnn, ipYTWVOPDpfJXeTFApPIgldytQSaUFdk) * JKpyVMrnPSyIBxYqPUjWKtnFnXIMmXeu
            )
            saflYDRhXJdQdfVZvmXntLsBUdZCNHPT = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.NRtnQQOkbUbfnbxzIRWvMfkdGBlGyoSB(kgbUKBPJVlaLOrCgiKgtWPLImzSTTkUG, XauksjEFAUvtInEaALXIwUhurkUuooOF)
            if clbgFKGfOFaPvTRBXwoouOOLgsSYaJzB == 'dpm_solver':
                VnmAPlKFRKPJNjSTgsTtFHxWSelTupCY = (
                        PpKdefOZNalnbKKPZYEFkTizePccpchH(zhpCBYkwQkhgdrClReoQrMdATdSZEHOs / hdTNoSkElMdkMBosbtxRTPZtRzspQDxC, ipYTWVOPDpfJXeTFApPIgldytQSaUFdk) * NECAaWUrFGIXcLimrerEYmxYIykQBfXb
                        - PpKdefOZNalnbKKPZYEFkTizePccpchH(WJsAttAlgEhvijNBnbITSLwwTXOxBfNI * AgzQHYUBcAtZwocfZDsAQtNEVTrztNYP, ipYTWVOPDpfJXeTFApPIgldytQSaUFdk) * JKpyVMrnPSyIBxYqPUjWKtnFnXIMmXeu
                        - (0.5 / apACmNWgYmlQTXHPQlhMzlFpreaoNbwW) * PpKdefOZNalnbKKPZYEFkTizePccpchH(WJsAttAlgEhvijNBnbITSLwwTXOxBfNI * AgzQHYUBcAtZwocfZDsAQtNEVTrztNYP, ipYTWVOPDpfJXeTFApPIgldytQSaUFdk) * (saflYDRhXJdQdfVZvmXntLsBUdZCNHPT - JKpyVMrnPSyIBxYqPUjWKtnFnXIMmXeu)
                )
            elif clbgFKGfOFaPvTRBXwoouOOLgsSYaJzB == 'taylor':
                VnmAPlKFRKPJNjSTgsTtFHxWSelTupCY = (
                        PpKdefOZNalnbKKPZYEFkTizePccpchH(zhpCBYkwQkhgdrClReoQrMdATdSZEHOs / hdTNoSkElMdkMBosbtxRTPZtRzspQDxC, ipYTWVOPDpfJXeTFApPIgldytQSaUFdk) * NECAaWUrFGIXcLimrerEYmxYIykQBfXb
                        - PpKdefOZNalnbKKPZYEFkTizePccpchH(WJsAttAlgEhvijNBnbITSLwwTXOxBfNI * AgzQHYUBcAtZwocfZDsAQtNEVTrztNYP, ipYTWVOPDpfJXeTFApPIgldytQSaUFdk) * JKpyVMrnPSyIBxYqPUjWKtnFnXIMmXeu
                        + (1. / apACmNWgYmlQTXHPQlhMzlFpreaoNbwW) * PpKdefOZNalnbKKPZYEFkTizePccpchH(WJsAttAlgEhvijNBnbITSLwwTXOxBfNI * ((torch.exp(-xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab) - 1.) / xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab + 1.), ipYTWVOPDpfJXeTFApPIgldytQSaUFdk) * (
                                    saflYDRhXJdQdfVZvmXntLsBUdZCNHPT - JKpyVMrnPSyIBxYqPUjWKtnFnXIMmXeu)
                )
        else:
            KmpEUFqjzUzHgeFLOVLhmopBJNkHmXnn = torch.expm1(apACmNWgYmlQTXHPQlhMzlFpreaoNbwW * xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab)
            AgzQHYUBcAtZwocfZDsAQtNEVTrztNYP = torch.expm1(xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab)
            if JKpyVMrnPSyIBxYqPUjWKtnFnXIMmXeu is None:
                JKpyVMrnPSyIBxYqPUjWKtnFnXIMmXeu = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.NRtnQQOkbUbfnbxzIRWvMfkdGBlGyoSB(NECAaWUrFGIXcLimrerEYmxYIykQBfXb, uPePujIqMVDrwNvZQxJajkuaQFAcacjA)
            kgbUKBPJVlaLOrCgiKgtWPLImzSTTkUG = (
                    PpKdefOZNalnbKKPZYEFkTizePccpchH(torch.exp(YLeGXzGjcVjvxDGyfGAGucPepbgHsKqE - YLNizBEwkhwwTzMoRAXZSNCzobIasIFG), ipYTWVOPDpfJXeTFApPIgldytQSaUFdk) * NECAaWUrFGIXcLimrerEYmxYIykQBfXb
                    - PpKdefOZNalnbKKPZYEFkTizePccpchH(TlgULUZaszhyUGEKkErfBSgAXIPYcRCZ * KmpEUFqjzUzHgeFLOVLhmopBJNkHmXnn, ipYTWVOPDpfJXeTFApPIgldytQSaUFdk) * JKpyVMrnPSyIBxYqPUjWKtnFnXIMmXeu
            )
            saflYDRhXJdQdfVZvmXntLsBUdZCNHPT = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.NRtnQQOkbUbfnbxzIRWvMfkdGBlGyoSB(kgbUKBPJVlaLOrCgiKgtWPLImzSTTkUG, XauksjEFAUvtInEaALXIwUhurkUuooOF)
            if clbgFKGfOFaPvTRBXwoouOOLgsSYaJzB == 'dpm_solver':
                VnmAPlKFRKPJNjSTgsTtFHxWSelTupCY = (
                        PpKdefOZNalnbKKPZYEFkTizePccpchH(torch.exp(mQPxqKCwqnypKeTKHMQHncgoVnRYGQoB - YLNizBEwkhwwTzMoRAXZSNCzobIasIFG), ipYTWVOPDpfJXeTFApPIgldytQSaUFdk) * NECAaWUrFGIXcLimrerEYmxYIykQBfXb
                        - PpKdefOZNalnbKKPZYEFkTizePccpchH(zhpCBYkwQkhgdrClReoQrMdATdSZEHOs * AgzQHYUBcAtZwocfZDsAQtNEVTrztNYP, ipYTWVOPDpfJXeTFApPIgldytQSaUFdk) * JKpyVMrnPSyIBxYqPUjWKtnFnXIMmXeu
                        - (0.5 / apACmNWgYmlQTXHPQlhMzlFpreaoNbwW) * PpKdefOZNalnbKKPZYEFkTizePccpchH(zhpCBYkwQkhgdrClReoQrMdATdSZEHOs * AgzQHYUBcAtZwocfZDsAQtNEVTrztNYP, ipYTWVOPDpfJXeTFApPIgldytQSaUFdk) * (saflYDRhXJdQdfVZvmXntLsBUdZCNHPT - JKpyVMrnPSyIBxYqPUjWKtnFnXIMmXeu)
                )
            elif clbgFKGfOFaPvTRBXwoouOOLgsSYaJzB == 'taylor':
                VnmAPlKFRKPJNjSTgsTtFHxWSelTupCY = (
                        PpKdefOZNalnbKKPZYEFkTizePccpchH(torch.exp(mQPxqKCwqnypKeTKHMQHncgoVnRYGQoB - YLNizBEwkhwwTzMoRAXZSNCzobIasIFG), ipYTWVOPDpfJXeTFApPIgldytQSaUFdk) * NECAaWUrFGIXcLimrerEYmxYIykQBfXb
                        - PpKdefOZNalnbKKPZYEFkTizePccpchH(zhpCBYkwQkhgdrClReoQrMdATdSZEHOs * AgzQHYUBcAtZwocfZDsAQtNEVTrztNYP, ipYTWVOPDpfJXeTFApPIgldytQSaUFdk) * JKpyVMrnPSyIBxYqPUjWKtnFnXIMmXeu
                        - (1. / apACmNWgYmlQTXHPQlhMzlFpreaoNbwW) * PpKdefOZNalnbKKPZYEFkTizePccpchH(zhpCBYkwQkhgdrClReoQrMdATdSZEHOs * ((torch.exp(xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab) - 1.) / xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab - 1.), ipYTWVOPDpfJXeTFApPIgldytQSaUFdk) * (saflYDRhXJdQdfVZvmXntLsBUdZCNHPT - JKpyVMrnPSyIBxYqPUjWKtnFnXIMmXeu)
                )
        if vjtZlQMIzMiiNQGEDKNLZnhxTIPtimCl:
            return VnmAPlKFRKPJNjSTgsTtFHxWSelTupCY, {'model_s': JKpyVMrnPSyIBxYqPUjWKtnFnXIMmXeu, 'model_s1': saflYDRhXJdQdfVZvmXntLsBUdZCNHPT}
        else:
            return VnmAPlKFRKPJNjSTgsTtFHxWSelTupCY
    def mHiOgvjyrWlQGUVcvEtjFlvyGnxGiITk(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, NECAaWUrFGIXcLimrerEYmxYIykQBfXb, uPePujIqMVDrwNvZQxJajkuaQFAcacjA, XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz, apACmNWgYmlQTXHPQlhMzlFpreaoNbwW=1. / 3., jUXrpBDWrfGGiwtyaMexgPCaBaIoLdEZ=2. / 3., JKpyVMrnPSyIBxYqPUjWKtnFnXIMmXeu=None, saflYDRhXJdQdfVZvmXntLsBUdZCNHPT=None,
                                           vjtZlQMIzMiiNQGEDKNLZnhxTIPtimCl=False, clbgFKGfOFaPvTRBXwoouOOLgsSYaJzB='dpm_solver'):
        if clbgFKGfOFaPvTRBXwoouOOLgsSYaJzB not in ['dpm_solver', 'taylor']:
            raise ValueError("'solver_type' must be either 'dpm_solver' or 'taylor', got {}".format(clbgFKGfOFaPvTRBXwoouOOLgsSYaJzB))
        if apACmNWgYmlQTXHPQlhMzlFpreaoNbwW is None:
            apACmNWgYmlQTXHPQlhMzlFpreaoNbwW = 1. / 3.
        if jUXrpBDWrfGGiwtyaMexgPCaBaIoLdEZ is None:
            jUXrpBDWrfGGiwtyaMexgPCaBaIoLdEZ = 2. / 3.
        jfvFkkyrHbvxGpVllCdQKVvBSNiKEJLj = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.noise_schedule
        ipYTWVOPDpfJXeTFApPIgldytQSaUFdk = NECAaWUrFGIXcLimrerEYmxYIykQBfXb.yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk()
        vhxMVZkWRybktsQdWBSYgKuXhuebDAKO, kumWCHxVTklyDOVOZlvEdFyJtcLshKec = jfvFkkyrHbvxGpVllCdQKVvBSNiKEJLj.iLJAxGawPgVbuzyTPlMNDawbjHhwvWaG(uPePujIqMVDrwNvZQxJajkuaQFAcacjA), jfvFkkyrHbvxGpVllCdQKVvBSNiKEJLj.iLJAxGawPgVbuzyTPlMNDawbjHhwvWaG(XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz)
        xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab = kumWCHxVTklyDOVOZlvEdFyJtcLshKec - vhxMVZkWRybktsQdWBSYgKuXhuebDAKO
        qmIrzgQJNFgnrrvhBvUBGJtKhFUVzszI = vhxMVZkWRybktsQdWBSYgKuXhuebDAKO + apACmNWgYmlQTXHPQlhMzlFpreaoNbwW * xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab
        YRKiVcXxGJndZBbGxNkcfOoEEPquLNBF = vhxMVZkWRybktsQdWBSYgKuXhuebDAKO + jUXrpBDWrfGGiwtyaMexgPCaBaIoLdEZ * xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab
        XauksjEFAUvtInEaALXIwUhurkUuooOF = jfvFkkyrHbvxGpVllCdQKVvBSNiKEJLj.wdxFGSVLvnnzjandRpvORBqdoTWJHGVq(qmIrzgQJNFgnrrvhBvUBGJtKhFUVzszI)
        orjPyVtdqCXZbZZCrekqzXxPBGSWSqJa = jfvFkkyrHbvxGpVllCdQKVvBSNiKEJLj.wdxFGSVLvnnzjandRpvORBqdoTWJHGVq(YRKiVcXxGJndZBbGxNkcfOoEEPquLNBF)
        YLNizBEwkhwwTzMoRAXZSNCzobIasIFG, YLeGXzGjcVjvxDGyfGAGucPepbgHsKqE, NxCIXJRNgkASiOftvSuiVgcNuCzNXNeM, mQPxqKCwqnypKeTKHMQHncgoVnRYGQoB = jfvFkkyrHbvxGpVllCdQKVvBSNiKEJLj.rbFJZghBKIbgXbmpNDbwzjVehrMOJUAI(
            uPePujIqMVDrwNvZQxJajkuaQFAcacjA), jfvFkkyrHbvxGpVllCdQKVvBSNiKEJLj.rbFJZghBKIbgXbmpNDbwzjVehrMOJUAI(XauksjEFAUvtInEaALXIwUhurkUuooOF), jfvFkkyrHbvxGpVllCdQKVvBSNiKEJLj.rbFJZghBKIbgXbmpNDbwzjVehrMOJUAI(orjPyVtdqCXZbZZCrekqzXxPBGSWSqJa), jfvFkkyrHbvxGpVllCdQKVvBSNiKEJLj.rbFJZghBKIbgXbmpNDbwzjVehrMOJUAI(XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz)
        hdTNoSkElMdkMBosbtxRTPZtRzspQDxC, TlgULUZaszhyUGEKkErfBSgAXIPYcRCZ, PxXxumiWorVmXQCEApwZvdoElIetUuUm, zhpCBYkwQkhgdrClReoQrMdATdSZEHOs = jfvFkkyrHbvxGpVllCdQKVvBSNiKEJLj.uVXtYzlfVxHwJkqqdjvYpiPZXHJTGDgn(uPePujIqMVDrwNvZQxJajkuaQFAcacjA), jfvFkkyrHbvxGpVllCdQKVvBSNiKEJLj.uVXtYzlfVxHwJkqqdjvYpiPZXHJTGDgn(XauksjEFAUvtInEaALXIwUhurkUuooOF), jfvFkkyrHbvxGpVllCdQKVvBSNiKEJLj.uVXtYzlfVxHwJkqqdjvYpiPZXHJTGDgn(
            orjPyVtdqCXZbZZCrekqzXxPBGSWSqJa), jfvFkkyrHbvxGpVllCdQKVvBSNiKEJLj.uVXtYzlfVxHwJkqqdjvYpiPZXHJTGDgn(XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz)
        EhCJvDsghNmTQVbhBOPGTzmcqijBZykL, ddYsDvsjzMtiXbianklyooNYucSluiOC, WJsAttAlgEhvijNBnbITSLwwTXOxBfNI = torch.exp(YLeGXzGjcVjvxDGyfGAGucPepbgHsKqE), torch.exp(NxCIXJRNgkASiOftvSuiVgcNuCzNXNeM), torch.exp(mQPxqKCwqnypKeTKHMQHncgoVnRYGQoB)
        if rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.predict_x0:
            KmpEUFqjzUzHgeFLOVLhmopBJNkHmXnn = torch.expm1(-apACmNWgYmlQTXHPQlhMzlFpreaoNbwW * xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab)
            XhltRrGNsHvcXZKOqIdUMmjLMkDiFkeb = torch.expm1(-jUXrpBDWrfGGiwtyaMexgPCaBaIoLdEZ * xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab)
            AgzQHYUBcAtZwocfZDsAQtNEVTrztNYP = torch.expm1(-xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab)
            mNELetnWBIcVtEBeErisIEXVmDJvNfnk = torch.expm1(-jUXrpBDWrfGGiwtyaMexgPCaBaIoLdEZ * xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab) / (jUXrpBDWrfGGiwtyaMexgPCaBaIoLdEZ * xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab) + 1.
            sSoPaxtPkFmuEwlZOSGoifpOhiJjZods = AgzQHYUBcAtZwocfZDsAQtNEVTrztNYP / xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab + 1.
            vQCArAadlVzodMvevsCjAxlkZoNodHrO = sSoPaxtPkFmuEwlZOSGoifpOhiJjZods / xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab - 0.5
            if JKpyVMrnPSyIBxYqPUjWKtnFnXIMmXeu is None:
                JKpyVMrnPSyIBxYqPUjWKtnFnXIMmXeu = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.NRtnQQOkbUbfnbxzIRWvMfkdGBlGyoSB(NECAaWUrFGIXcLimrerEYmxYIykQBfXb, uPePujIqMVDrwNvZQxJajkuaQFAcacjA)
            if saflYDRhXJdQdfVZvmXntLsBUdZCNHPT is None:
                kgbUKBPJVlaLOrCgiKgtWPLImzSTTkUG = (
                        PpKdefOZNalnbKKPZYEFkTizePccpchH(TlgULUZaszhyUGEKkErfBSgAXIPYcRCZ / hdTNoSkElMdkMBosbtxRTPZtRzspQDxC, ipYTWVOPDpfJXeTFApPIgldytQSaUFdk) * NECAaWUrFGIXcLimrerEYmxYIykQBfXb
                        - PpKdefOZNalnbKKPZYEFkTizePccpchH(EhCJvDsghNmTQVbhBOPGTzmcqijBZykL * KmpEUFqjzUzHgeFLOVLhmopBJNkHmXnn, ipYTWVOPDpfJXeTFApPIgldytQSaUFdk) * JKpyVMrnPSyIBxYqPUjWKtnFnXIMmXeu
                )
                saflYDRhXJdQdfVZvmXntLsBUdZCNHPT = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.NRtnQQOkbUbfnbxzIRWvMfkdGBlGyoSB(kgbUKBPJVlaLOrCgiKgtWPLImzSTTkUG, XauksjEFAUvtInEaALXIwUhurkUuooOF)
            mdhAgvqtBDxwnjTRwVrbYASuEwaEpfng = (
                    PpKdefOZNalnbKKPZYEFkTizePccpchH(PxXxumiWorVmXQCEApwZvdoElIetUuUm / hdTNoSkElMdkMBosbtxRTPZtRzspQDxC, ipYTWVOPDpfJXeTFApPIgldytQSaUFdk) * NECAaWUrFGIXcLimrerEYmxYIykQBfXb
                    - PpKdefOZNalnbKKPZYEFkTizePccpchH(ddYsDvsjzMtiXbianklyooNYucSluiOC * XhltRrGNsHvcXZKOqIdUMmjLMkDiFkeb, ipYTWVOPDpfJXeTFApPIgldytQSaUFdk) * JKpyVMrnPSyIBxYqPUjWKtnFnXIMmXeu
                    + jUXrpBDWrfGGiwtyaMexgPCaBaIoLdEZ / apACmNWgYmlQTXHPQlhMzlFpreaoNbwW * PpKdefOZNalnbKKPZYEFkTizePccpchH(ddYsDvsjzMtiXbianklyooNYucSluiOC * mNELetnWBIcVtEBeErisIEXVmDJvNfnk, ipYTWVOPDpfJXeTFApPIgldytQSaUFdk) * (saflYDRhXJdQdfVZvmXntLsBUdZCNHPT - JKpyVMrnPSyIBxYqPUjWKtnFnXIMmXeu)
            )
            BbGNuxsaIDpfjqVpCHbUrHcEeMCXgzAD = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.NRtnQQOkbUbfnbxzIRWvMfkdGBlGyoSB(mdhAgvqtBDxwnjTRwVrbYASuEwaEpfng, orjPyVtdqCXZbZZCrekqzXxPBGSWSqJa)
            if clbgFKGfOFaPvTRBXwoouOOLgsSYaJzB == 'dpm_solver':
                VnmAPlKFRKPJNjSTgsTtFHxWSelTupCY = (
                        PpKdefOZNalnbKKPZYEFkTizePccpchH(zhpCBYkwQkhgdrClReoQrMdATdSZEHOs / hdTNoSkElMdkMBosbtxRTPZtRzspQDxC, ipYTWVOPDpfJXeTFApPIgldytQSaUFdk) * NECAaWUrFGIXcLimrerEYmxYIykQBfXb
                        - PpKdefOZNalnbKKPZYEFkTizePccpchH(WJsAttAlgEhvijNBnbITSLwwTXOxBfNI * AgzQHYUBcAtZwocfZDsAQtNEVTrztNYP, ipYTWVOPDpfJXeTFApPIgldytQSaUFdk) * JKpyVMrnPSyIBxYqPUjWKtnFnXIMmXeu
                        + (1. / jUXrpBDWrfGGiwtyaMexgPCaBaIoLdEZ) * PpKdefOZNalnbKKPZYEFkTizePccpchH(WJsAttAlgEhvijNBnbITSLwwTXOxBfNI * sSoPaxtPkFmuEwlZOSGoifpOhiJjZods, ipYTWVOPDpfJXeTFApPIgldytQSaUFdk) * (BbGNuxsaIDpfjqVpCHbUrHcEeMCXgzAD - JKpyVMrnPSyIBxYqPUjWKtnFnXIMmXeu)
                )
            elif clbgFKGfOFaPvTRBXwoouOOLgsSYaJzB == 'taylor':
                JMGVTAnPDszEzkCSYHRWGONpUuxiYWan = (1. / apACmNWgYmlQTXHPQlhMzlFpreaoNbwW) * (saflYDRhXJdQdfVZvmXntLsBUdZCNHPT - JKpyVMrnPSyIBxYqPUjWKtnFnXIMmXeu)
                mOxpaHKKDTkUvxIlUhdDIZUVBxgVRtno = (1. / jUXrpBDWrfGGiwtyaMexgPCaBaIoLdEZ) * (BbGNuxsaIDpfjqVpCHbUrHcEeMCXgzAD - JKpyVMrnPSyIBxYqPUjWKtnFnXIMmXeu)
                tIYldbaSgeVHfQdLotGvnpAoGDTPzJJk = (jUXrpBDWrfGGiwtyaMexgPCaBaIoLdEZ * JMGVTAnPDszEzkCSYHRWGONpUuxiYWan - apACmNWgYmlQTXHPQlhMzlFpreaoNbwW * mOxpaHKKDTkUvxIlUhdDIZUVBxgVRtno) / (jUXrpBDWrfGGiwtyaMexgPCaBaIoLdEZ - apACmNWgYmlQTXHPQlhMzlFpreaoNbwW)
                SYIcqiGMboSYKxqMSlRyCphnPmizQRaq = 2. * (mOxpaHKKDTkUvxIlUhdDIZUVBxgVRtno - JMGVTAnPDszEzkCSYHRWGONpUuxiYWan) / (jUXrpBDWrfGGiwtyaMexgPCaBaIoLdEZ - apACmNWgYmlQTXHPQlhMzlFpreaoNbwW)
                VnmAPlKFRKPJNjSTgsTtFHxWSelTupCY = (
                        PpKdefOZNalnbKKPZYEFkTizePccpchH(zhpCBYkwQkhgdrClReoQrMdATdSZEHOs / hdTNoSkElMdkMBosbtxRTPZtRzspQDxC, ipYTWVOPDpfJXeTFApPIgldytQSaUFdk) * NECAaWUrFGIXcLimrerEYmxYIykQBfXb
                        - PpKdefOZNalnbKKPZYEFkTizePccpchH(WJsAttAlgEhvijNBnbITSLwwTXOxBfNI * AgzQHYUBcAtZwocfZDsAQtNEVTrztNYP, ipYTWVOPDpfJXeTFApPIgldytQSaUFdk) * JKpyVMrnPSyIBxYqPUjWKtnFnXIMmXeu
                        + PpKdefOZNalnbKKPZYEFkTizePccpchH(WJsAttAlgEhvijNBnbITSLwwTXOxBfNI * sSoPaxtPkFmuEwlZOSGoifpOhiJjZods, ipYTWVOPDpfJXeTFApPIgldytQSaUFdk) * tIYldbaSgeVHfQdLotGvnpAoGDTPzJJk
                        - PpKdefOZNalnbKKPZYEFkTizePccpchH(WJsAttAlgEhvijNBnbITSLwwTXOxBfNI * vQCArAadlVzodMvevsCjAxlkZoNodHrO, ipYTWVOPDpfJXeTFApPIgldytQSaUFdk) * SYIcqiGMboSYKxqMSlRyCphnPmizQRaq
                )
        else:
            KmpEUFqjzUzHgeFLOVLhmopBJNkHmXnn = torch.expm1(apACmNWgYmlQTXHPQlhMzlFpreaoNbwW * xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab)
            XhltRrGNsHvcXZKOqIdUMmjLMkDiFkeb = torch.expm1(jUXrpBDWrfGGiwtyaMexgPCaBaIoLdEZ * xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab)
            AgzQHYUBcAtZwocfZDsAQtNEVTrztNYP = torch.expm1(xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab)
            mNELetnWBIcVtEBeErisIEXVmDJvNfnk = torch.expm1(jUXrpBDWrfGGiwtyaMexgPCaBaIoLdEZ * xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab) / (jUXrpBDWrfGGiwtyaMexgPCaBaIoLdEZ * xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab) - 1.
            sSoPaxtPkFmuEwlZOSGoifpOhiJjZods = AgzQHYUBcAtZwocfZDsAQtNEVTrztNYP / xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab - 1.
            vQCArAadlVzodMvevsCjAxlkZoNodHrO = sSoPaxtPkFmuEwlZOSGoifpOhiJjZods / xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab - 0.5
            if JKpyVMrnPSyIBxYqPUjWKtnFnXIMmXeu is None:
                JKpyVMrnPSyIBxYqPUjWKtnFnXIMmXeu = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.NRtnQQOkbUbfnbxzIRWvMfkdGBlGyoSB(NECAaWUrFGIXcLimrerEYmxYIykQBfXb, uPePujIqMVDrwNvZQxJajkuaQFAcacjA)
            if saflYDRhXJdQdfVZvmXntLsBUdZCNHPT is None:
                kgbUKBPJVlaLOrCgiKgtWPLImzSTTkUG = (
                        PpKdefOZNalnbKKPZYEFkTizePccpchH(torch.exp(YLeGXzGjcVjvxDGyfGAGucPepbgHsKqE - YLNizBEwkhwwTzMoRAXZSNCzobIasIFG), ipYTWVOPDpfJXeTFApPIgldytQSaUFdk) * NECAaWUrFGIXcLimrerEYmxYIykQBfXb
                        - PpKdefOZNalnbKKPZYEFkTizePccpchH(TlgULUZaszhyUGEKkErfBSgAXIPYcRCZ * KmpEUFqjzUzHgeFLOVLhmopBJNkHmXnn, ipYTWVOPDpfJXeTFApPIgldytQSaUFdk) * JKpyVMrnPSyIBxYqPUjWKtnFnXIMmXeu
                )
                saflYDRhXJdQdfVZvmXntLsBUdZCNHPT = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.NRtnQQOkbUbfnbxzIRWvMfkdGBlGyoSB(kgbUKBPJVlaLOrCgiKgtWPLImzSTTkUG, XauksjEFAUvtInEaALXIwUhurkUuooOF)
            mdhAgvqtBDxwnjTRwVrbYASuEwaEpfng = (
                    PpKdefOZNalnbKKPZYEFkTizePccpchH(torch.exp(NxCIXJRNgkASiOftvSuiVgcNuCzNXNeM - YLNizBEwkhwwTzMoRAXZSNCzobIasIFG), ipYTWVOPDpfJXeTFApPIgldytQSaUFdk) * NECAaWUrFGIXcLimrerEYmxYIykQBfXb
                    - PpKdefOZNalnbKKPZYEFkTizePccpchH(PxXxumiWorVmXQCEApwZvdoElIetUuUm * XhltRrGNsHvcXZKOqIdUMmjLMkDiFkeb, ipYTWVOPDpfJXeTFApPIgldytQSaUFdk) * JKpyVMrnPSyIBxYqPUjWKtnFnXIMmXeu
                    - jUXrpBDWrfGGiwtyaMexgPCaBaIoLdEZ / apACmNWgYmlQTXHPQlhMzlFpreaoNbwW * PpKdefOZNalnbKKPZYEFkTizePccpchH(PxXxumiWorVmXQCEApwZvdoElIetUuUm * mNELetnWBIcVtEBeErisIEXVmDJvNfnk, ipYTWVOPDpfJXeTFApPIgldytQSaUFdk) * (saflYDRhXJdQdfVZvmXntLsBUdZCNHPT - JKpyVMrnPSyIBxYqPUjWKtnFnXIMmXeu)
            )
            BbGNuxsaIDpfjqVpCHbUrHcEeMCXgzAD = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.NRtnQQOkbUbfnbxzIRWvMfkdGBlGyoSB(mdhAgvqtBDxwnjTRwVrbYASuEwaEpfng, orjPyVtdqCXZbZZCrekqzXxPBGSWSqJa)
            if clbgFKGfOFaPvTRBXwoouOOLgsSYaJzB == 'dpm_solver':
                VnmAPlKFRKPJNjSTgsTtFHxWSelTupCY = (
                        PpKdefOZNalnbKKPZYEFkTizePccpchH(torch.exp(mQPxqKCwqnypKeTKHMQHncgoVnRYGQoB - YLNizBEwkhwwTzMoRAXZSNCzobIasIFG), ipYTWVOPDpfJXeTFApPIgldytQSaUFdk) * NECAaWUrFGIXcLimrerEYmxYIykQBfXb
                        - PpKdefOZNalnbKKPZYEFkTizePccpchH(zhpCBYkwQkhgdrClReoQrMdATdSZEHOs * AgzQHYUBcAtZwocfZDsAQtNEVTrztNYP, ipYTWVOPDpfJXeTFApPIgldytQSaUFdk) * JKpyVMrnPSyIBxYqPUjWKtnFnXIMmXeu
                        - (1. / jUXrpBDWrfGGiwtyaMexgPCaBaIoLdEZ) * PpKdefOZNalnbKKPZYEFkTizePccpchH(zhpCBYkwQkhgdrClReoQrMdATdSZEHOs * sSoPaxtPkFmuEwlZOSGoifpOhiJjZods, ipYTWVOPDpfJXeTFApPIgldytQSaUFdk) * (BbGNuxsaIDpfjqVpCHbUrHcEeMCXgzAD - JKpyVMrnPSyIBxYqPUjWKtnFnXIMmXeu)
                )
            elif clbgFKGfOFaPvTRBXwoouOOLgsSYaJzB == 'taylor':
                JMGVTAnPDszEzkCSYHRWGONpUuxiYWan = (1. / apACmNWgYmlQTXHPQlhMzlFpreaoNbwW) * (saflYDRhXJdQdfVZvmXntLsBUdZCNHPT - JKpyVMrnPSyIBxYqPUjWKtnFnXIMmXeu)
                mOxpaHKKDTkUvxIlUhdDIZUVBxgVRtno = (1. / jUXrpBDWrfGGiwtyaMexgPCaBaIoLdEZ) * (BbGNuxsaIDpfjqVpCHbUrHcEeMCXgzAD - JKpyVMrnPSyIBxYqPUjWKtnFnXIMmXeu)
                tIYldbaSgeVHfQdLotGvnpAoGDTPzJJk = (jUXrpBDWrfGGiwtyaMexgPCaBaIoLdEZ * JMGVTAnPDszEzkCSYHRWGONpUuxiYWan - apACmNWgYmlQTXHPQlhMzlFpreaoNbwW * mOxpaHKKDTkUvxIlUhdDIZUVBxgVRtno) / (jUXrpBDWrfGGiwtyaMexgPCaBaIoLdEZ - apACmNWgYmlQTXHPQlhMzlFpreaoNbwW)
                SYIcqiGMboSYKxqMSlRyCphnPmizQRaq = 2. * (mOxpaHKKDTkUvxIlUhdDIZUVBxgVRtno - JMGVTAnPDszEzkCSYHRWGONpUuxiYWan) / (jUXrpBDWrfGGiwtyaMexgPCaBaIoLdEZ - apACmNWgYmlQTXHPQlhMzlFpreaoNbwW)
                VnmAPlKFRKPJNjSTgsTtFHxWSelTupCY = (
                        PpKdefOZNalnbKKPZYEFkTizePccpchH(torch.exp(mQPxqKCwqnypKeTKHMQHncgoVnRYGQoB - YLNizBEwkhwwTzMoRAXZSNCzobIasIFG), ipYTWVOPDpfJXeTFApPIgldytQSaUFdk) * NECAaWUrFGIXcLimrerEYmxYIykQBfXb
                        - PpKdefOZNalnbKKPZYEFkTizePccpchH(zhpCBYkwQkhgdrClReoQrMdATdSZEHOs * AgzQHYUBcAtZwocfZDsAQtNEVTrztNYP, ipYTWVOPDpfJXeTFApPIgldytQSaUFdk) * JKpyVMrnPSyIBxYqPUjWKtnFnXIMmXeu
                        - PpKdefOZNalnbKKPZYEFkTizePccpchH(zhpCBYkwQkhgdrClReoQrMdATdSZEHOs * sSoPaxtPkFmuEwlZOSGoifpOhiJjZods, ipYTWVOPDpfJXeTFApPIgldytQSaUFdk) * tIYldbaSgeVHfQdLotGvnpAoGDTPzJJk
                        - PpKdefOZNalnbKKPZYEFkTizePccpchH(zhpCBYkwQkhgdrClReoQrMdATdSZEHOs * vQCArAadlVzodMvevsCjAxlkZoNodHrO, ipYTWVOPDpfJXeTFApPIgldytQSaUFdk) * SYIcqiGMboSYKxqMSlRyCphnPmizQRaq
                )
        if vjtZlQMIzMiiNQGEDKNLZnhxTIPtimCl:
            return VnmAPlKFRKPJNjSTgsTtFHxWSelTupCY, {'model_s': JKpyVMrnPSyIBxYqPUjWKtnFnXIMmXeu, 'model_s1': saflYDRhXJdQdfVZvmXntLsBUdZCNHPT, 'model_s2': BbGNuxsaIDpfjqVpCHbUrHcEeMCXgzAD}
        else:
            return VnmAPlKFRKPJNjSTgsTtFHxWSelTupCY
    def aCOxTfpXBERMDYYcDLWtqpDSGEkAcwGl(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, NECAaWUrFGIXcLimrerEYmxYIykQBfXb, mnAIBgWuMvXNfmUTqdOanZcqQsoFdkjZ, wqXgjkKQfegsPGuaedxSYSqZgMJKaPUG, XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz, clbgFKGfOFaPvTRBXwoouOOLgsSYaJzB="dpm_solver"):
        if clbgFKGfOFaPvTRBXwoouOOLgsSYaJzB not in ['dpm_solver', 'taylor']:
            raise ValueError("'solver_type' must be either 'dpm_solver' or 'taylor', got {}".format(clbgFKGfOFaPvTRBXwoouOOLgsSYaJzB))
        jfvFkkyrHbvxGpVllCdQKVvBSNiKEJLj = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.noise_schedule
        ipYTWVOPDpfJXeTFApPIgldytQSaUFdk = NECAaWUrFGIXcLimrerEYmxYIykQBfXb.yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk()
        mNEgXxlqCWHzzUtUhwWutQeMRvDLLrUk, dBJktmjlnYZCfkHVkiGkJCaMOYuHpDIz = mnAIBgWuMvXNfmUTqdOanZcqQsoFdkjZ
        hmGtvRJJMQtlFaEMOaHLnaqPknfiPCob, OOgDeKRaXooJQBZSMdGvFiXBhTpSOvMr = wqXgjkKQfegsPGuaedxSYSqZgMJKaPUG
        JzssbVRxFsWiHdxVebKHGwmGyMFOmLOT, JKzQCoLXfIJoXCRTovJGWkOVVSpOlUzM, kumWCHxVTklyDOVOZlvEdFyJtcLshKec = jfvFkkyrHbvxGpVllCdQKVvBSNiKEJLj.iLJAxGawPgVbuzyTPlMNDawbjHhwvWaG(hmGtvRJJMQtlFaEMOaHLnaqPknfiPCob), jfvFkkyrHbvxGpVllCdQKVvBSNiKEJLj.iLJAxGawPgVbuzyTPlMNDawbjHhwvWaG(
            OOgDeKRaXooJQBZSMdGvFiXBhTpSOvMr), jfvFkkyrHbvxGpVllCdQKVvBSNiKEJLj.iLJAxGawPgVbuzyTPlMNDawbjHhwvWaG(XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz)
        UhmyIxsZKejneuBmSKTcEPfOqBrixbXR, mQPxqKCwqnypKeTKHMQHncgoVnRYGQoB = jfvFkkyrHbvxGpVllCdQKVvBSNiKEJLj.rbFJZghBKIbgXbmpNDbwzjVehrMOJUAI(OOgDeKRaXooJQBZSMdGvFiXBhTpSOvMr), jfvFkkyrHbvxGpVllCdQKVvBSNiKEJLj.rbFJZghBKIbgXbmpNDbwzjVehrMOJUAI(XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz)
        MsMCQbDbVKbfvtxySgtTKWSDCYuGdwoI, zhpCBYkwQkhgdrClReoQrMdATdSZEHOs = jfvFkkyrHbvxGpVllCdQKVvBSNiKEJLj.uVXtYzlfVxHwJkqqdjvYpiPZXHJTGDgn(OOgDeKRaXooJQBZSMdGvFiXBhTpSOvMr), jfvFkkyrHbvxGpVllCdQKVvBSNiKEJLj.uVXtYzlfVxHwJkqqdjvYpiPZXHJTGDgn(XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz)
        WJsAttAlgEhvijNBnbITSLwwTXOxBfNI = torch.exp(mQPxqKCwqnypKeTKHMQHncgoVnRYGQoB)
        IwyeUaJKIoxsnfYHQRButOExeHcYfVvM = JKzQCoLXfIJoXCRTovJGWkOVVSpOlUzM - JzssbVRxFsWiHdxVebKHGwmGyMFOmLOT
        xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab = kumWCHxVTklyDOVOZlvEdFyJtcLshKec - JKzQCoLXfIJoXCRTovJGWkOVVSpOlUzM
        aNnhgvGSzDOfunNUFPhsrxktbnXzLhMl = IwyeUaJKIoxsnfYHQRButOExeHcYfVvM / xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab
        JMGVTAnPDszEzkCSYHRWGONpUuxiYWan = PpKdefOZNalnbKKPZYEFkTizePccpchH(1. / aNnhgvGSzDOfunNUFPhsrxktbnXzLhMl, ipYTWVOPDpfJXeTFApPIgldytQSaUFdk) * (dBJktmjlnYZCfkHVkiGkJCaMOYuHpDIz - mNEgXxlqCWHzzUtUhwWutQeMRvDLLrUk)
        if rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.predict_x0:
            if clbgFKGfOFaPvTRBXwoouOOLgsSYaJzB == 'dpm_solver':
                VnmAPlKFRKPJNjSTgsTtFHxWSelTupCY = (
                        PpKdefOZNalnbKKPZYEFkTizePccpchH(zhpCBYkwQkhgdrClReoQrMdATdSZEHOs / MsMCQbDbVKbfvtxySgtTKWSDCYuGdwoI, ipYTWVOPDpfJXeTFApPIgldytQSaUFdk) * NECAaWUrFGIXcLimrerEYmxYIykQBfXb
                        - PpKdefOZNalnbKKPZYEFkTizePccpchH(WJsAttAlgEhvijNBnbITSLwwTXOxBfNI * (torch.exp(-xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab) - 1.), ipYTWVOPDpfJXeTFApPIgldytQSaUFdk) * dBJktmjlnYZCfkHVkiGkJCaMOYuHpDIz
                        - 0.5 * PpKdefOZNalnbKKPZYEFkTizePccpchH(WJsAttAlgEhvijNBnbITSLwwTXOxBfNI * (torch.exp(-xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab) - 1.), ipYTWVOPDpfJXeTFApPIgldytQSaUFdk) * JMGVTAnPDszEzkCSYHRWGONpUuxiYWan
                )
            elif clbgFKGfOFaPvTRBXwoouOOLgsSYaJzB == 'taylor':
                VnmAPlKFRKPJNjSTgsTtFHxWSelTupCY = (
                        PpKdefOZNalnbKKPZYEFkTizePccpchH(zhpCBYkwQkhgdrClReoQrMdATdSZEHOs / MsMCQbDbVKbfvtxySgtTKWSDCYuGdwoI, ipYTWVOPDpfJXeTFApPIgldytQSaUFdk) * NECAaWUrFGIXcLimrerEYmxYIykQBfXb
                        - PpKdefOZNalnbKKPZYEFkTizePccpchH(WJsAttAlgEhvijNBnbITSLwwTXOxBfNI * (torch.exp(-xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab) - 1.), ipYTWVOPDpfJXeTFApPIgldytQSaUFdk) * dBJktmjlnYZCfkHVkiGkJCaMOYuHpDIz
                        + PpKdefOZNalnbKKPZYEFkTizePccpchH(WJsAttAlgEhvijNBnbITSLwwTXOxBfNI * ((torch.exp(-xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab) - 1.) / xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab + 1.), ipYTWVOPDpfJXeTFApPIgldytQSaUFdk) * JMGVTAnPDszEzkCSYHRWGONpUuxiYWan
                )
        else:
            if clbgFKGfOFaPvTRBXwoouOOLgsSYaJzB == 'dpm_solver':
                VnmAPlKFRKPJNjSTgsTtFHxWSelTupCY = (
                        PpKdefOZNalnbKKPZYEFkTizePccpchH(torch.exp(mQPxqKCwqnypKeTKHMQHncgoVnRYGQoB - UhmyIxsZKejneuBmSKTcEPfOqBrixbXR), ipYTWVOPDpfJXeTFApPIgldytQSaUFdk) * NECAaWUrFGIXcLimrerEYmxYIykQBfXb
                        - PpKdefOZNalnbKKPZYEFkTizePccpchH(zhpCBYkwQkhgdrClReoQrMdATdSZEHOs * (torch.exp(xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab) - 1.), ipYTWVOPDpfJXeTFApPIgldytQSaUFdk) * dBJktmjlnYZCfkHVkiGkJCaMOYuHpDIz
                        - 0.5 * PpKdefOZNalnbKKPZYEFkTizePccpchH(zhpCBYkwQkhgdrClReoQrMdATdSZEHOs * (torch.exp(xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab) - 1.), ipYTWVOPDpfJXeTFApPIgldytQSaUFdk) * JMGVTAnPDszEzkCSYHRWGONpUuxiYWan
                )
            elif clbgFKGfOFaPvTRBXwoouOOLgsSYaJzB == 'taylor':
                VnmAPlKFRKPJNjSTgsTtFHxWSelTupCY = (
                        PpKdefOZNalnbKKPZYEFkTizePccpchH(torch.exp(mQPxqKCwqnypKeTKHMQHncgoVnRYGQoB - UhmyIxsZKejneuBmSKTcEPfOqBrixbXR), ipYTWVOPDpfJXeTFApPIgldytQSaUFdk) * NECAaWUrFGIXcLimrerEYmxYIykQBfXb
                        - PpKdefOZNalnbKKPZYEFkTizePccpchH(zhpCBYkwQkhgdrClReoQrMdATdSZEHOs * (torch.exp(xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab) - 1.), ipYTWVOPDpfJXeTFApPIgldytQSaUFdk) * dBJktmjlnYZCfkHVkiGkJCaMOYuHpDIz
                        - PpKdefOZNalnbKKPZYEFkTizePccpchH(zhpCBYkwQkhgdrClReoQrMdATdSZEHOs * ((torch.exp(xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab) - 1.) / xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab - 1.), ipYTWVOPDpfJXeTFApPIgldytQSaUFdk) * JMGVTAnPDszEzkCSYHRWGONpUuxiYWan
                )
        return VnmAPlKFRKPJNjSTgsTtFHxWSelTupCY
    def pKPbxwivZVXNcRLKkSEjOstWSeuupZyj(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, NECAaWUrFGIXcLimrerEYmxYIykQBfXb, mnAIBgWuMvXNfmUTqdOanZcqQsoFdkjZ, wqXgjkKQfegsPGuaedxSYSqZgMJKaPUG, XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz, clbgFKGfOFaPvTRBXwoouOOLgsSYaJzB='dpm_solver'):
        jfvFkkyrHbvxGpVllCdQKVvBSNiKEJLj = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.noise_schedule
        ipYTWVOPDpfJXeTFApPIgldytQSaUFdk = NECAaWUrFGIXcLimrerEYmxYIykQBfXb.yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk()
        lHNEXVeXLhxYHtTbuMQoIINesyWPFoXA, mNEgXxlqCWHzzUtUhwWutQeMRvDLLrUk, dBJktmjlnYZCfkHVkiGkJCaMOYuHpDIz = mnAIBgWuMvXNfmUTqdOanZcqQsoFdkjZ
        EUzLrlpejOGaGOLvDGXwDRZkATqdQcCB, hmGtvRJJMQtlFaEMOaHLnaqPknfiPCob, OOgDeKRaXooJQBZSMdGvFiXBhTpSOvMr = wqXgjkKQfegsPGuaedxSYSqZgMJKaPUG
        JTSnFpwXRSxpuLlACNnylDumDrzyXDFN, JzssbVRxFsWiHdxVebKHGwmGyMFOmLOT, JKzQCoLXfIJoXCRTovJGWkOVVSpOlUzM, kumWCHxVTklyDOVOZlvEdFyJtcLshKec = jfvFkkyrHbvxGpVllCdQKVvBSNiKEJLj.iLJAxGawPgVbuzyTPlMNDawbjHhwvWaG(EUzLrlpejOGaGOLvDGXwDRZkATqdQcCB), jfvFkkyrHbvxGpVllCdQKVvBSNiKEJLj.iLJAxGawPgVbuzyTPlMNDawbjHhwvWaG(
            hmGtvRJJMQtlFaEMOaHLnaqPknfiPCob), jfvFkkyrHbvxGpVllCdQKVvBSNiKEJLj.iLJAxGawPgVbuzyTPlMNDawbjHhwvWaG(OOgDeKRaXooJQBZSMdGvFiXBhTpSOvMr), jfvFkkyrHbvxGpVllCdQKVvBSNiKEJLj.iLJAxGawPgVbuzyTPlMNDawbjHhwvWaG(XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz)
        UhmyIxsZKejneuBmSKTcEPfOqBrixbXR, mQPxqKCwqnypKeTKHMQHncgoVnRYGQoB = jfvFkkyrHbvxGpVllCdQKVvBSNiKEJLj.rbFJZghBKIbgXbmpNDbwzjVehrMOJUAI(OOgDeKRaXooJQBZSMdGvFiXBhTpSOvMr), jfvFkkyrHbvxGpVllCdQKVvBSNiKEJLj.rbFJZghBKIbgXbmpNDbwzjVehrMOJUAI(XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz)
        MsMCQbDbVKbfvtxySgtTKWSDCYuGdwoI, zhpCBYkwQkhgdrClReoQrMdATdSZEHOs = jfvFkkyrHbvxGpVllCdQKVvBSNiKEJLj.uVXtYzlfVxHwJkqqdjvYpiPZXHJTGDgn(OOgDeKRaXooJQBZSMdGvFiXBhTpSOvMr), jfvFkkyrHbvxGpVllCdQKVvBSNiKEJLj.uVXtYzlfVxHwJkqqdjvYpiPZXHJTGDgn(XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz)
        WJsAttAlgEhvijNBnbITSLwwTXOxBfNI = torch.exp(mQPxqKCwqnypKeTKHMQHncgoVnRYGQoB)
        WWYRPNkUKTAWHUatYWDtFEQZUJYCgYhA = JzssbVRxFsWiHdxVebKHGwmGyMFOmLOT - JTSnFpwXRSxpuLlACNnylDumDrzyXDFN
        IwyeUaJKIoxsnfYHQRButOExeHcYfVvM = JKzQCoLXfIJoXCRTovJGWkOVVSpOlUzM - JzssbVRxFsWiHdxVebKHGwmGyMFOmLOT
        xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab = kumWCHxVTklyDOVOZlvEdFyJtcLshKec - JKzQCoLXfIJoXCRTovJGWkOVVSpOlUzM
        aNnhgvGSzDOfunNUFPhsrxktbnXzLhMl, apACmNWgYmlQTXHPQlhMzlFpreaoNbwW = IwyeUaJKIoxsnfYHQRButOExeHcYfVvM / xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab, WWYRPNkUKTAWHUatYWDtFEQZUJYCgYhA / xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab
        JMGVTAnPDszEzkCSYHRWGONpUuxiYWan = PpKdefOZNalnbKKPZYEFkTizePccpchH(1. / aNnhgvGSzDOfunNUFPhsrxktbnXzLhMl, ipYTWVOPDpfJXeTFApPIgldytQSaUFdk) * (dBJktmjlnYZCfkHVkiGkJCaMOYuHpDIz - mNEgXxlqCWHzzUtUhwWutQeMRvDLLrUk)
        mOxpaHKKDTkUvxIlUhdDIZUVBxgVRtno = PpKdefOZNalnbKKPZYEFkTizePccpchH(1. / apACmNWgYmlQTXHPQlhMzlFpreaoNbwW, ipYTWVOPDpfJXeTFApPIgldytQSaUFdk) * (mNEgXxlqCWHzzUtUhwWutQeMRvDLLrUk - lHNEXVeXLhxYHtTbuMQoIINesyWPFoXA)
        tIYldbaSgeVHfQdLotGvnpAoGDTPzJJk = JMGVTAnPDszEzkCSYHRWGONpUuxiYWan + PpKdefOZNalnbKKPZYEFkTizePccpchH(aNnhgvGSzDOfunNUFPhsrxktbnXzLhMl / (aNnhgvGSzDOfunNUFPhsrxktbnXzLhMl + apACmNWgYmlQTXHPQlhMzlFpreaoNbwW), ipYTWVOPDpfJXeTFApPIgldytQSaUFdk) * (JMGVTAnPDszEzkCSYHRWGONpUuxiYWan - mOxpaHKKDTkUvxIlUhdDIZUVBxgVRtno)
        SYIcqiGMboSYKxqMSlRyCphnPmizQRaq = PpKdefOZNalnbKKPZYEFkTizePccpchH(1. / (aNnhgvGSzDOfunNUFPhsrxktbnXzLhMl + apACmNWgYmlQTXHPQlhMzlFpreaoNbwW), ipYTWVOPDpfJXeTFApPIgldytQSaUFdk) * (JMGVTAnPDszEzkCSYHRWGONpUuxiYWan - mOxpaHKKDTkUvxIlUhdDIZUVBxgVRtno)
        if rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.predict_x0:
            VnmAPlKFRKPJNjSTgsTtFHxWSelTupCY = (
                    PpKdefOZNalnbKKPZYEFkTizePccpchH(zhpCBYkwQkhgdrClReoQrMdATdSZEHOs / MsMCQbDbVKbfvtxySgtTKWSDCYuGdwoI, ipYTWVOPDpfJXeTFApPIgldytQSaUFdk) * NECAaWUrFGIXcLimrerEYmxYIykQBfXb
                    - PpKdefOZNalnbKKPZYEFkTizePccpchH(WJsAttAlgEhvijNBnbITSLwwTXOxBfNI * (torch.exp(-xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab) - 1.), ipYTWVOPDpfJXeTFApPIgldytQSaUFdk) * dBJktmjlnYZCfkHVkiGkJCaMOYuHpDIz
                    + PpKdefOZNalnbKKPZYEFkTizePccpchH(WJsAttAlgEhvijNBnbITSLwwTXOxBfNI * ((torch.exp(-xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab) - 1.) / xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab + 1.), ipYTWVOPDpfJXeTFApPIgldytQSaUFdk) * tIYldbaSgeVHfQdLotGvnpAoGDTPzJJk
                    - PpKdefOZNalnbKKPZYEFkTizePccpchH(WJsAttAlgEhvijNBnbITSLwwTXOxBfNI * ((torch.exp(-xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab) - 1. + xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab) / xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab ** 2 - 0.5), ipYTWVOPDpfJXeTFApPIgldytQSaUFdk) * SYIcqiGMboSYKxqMSlRyCphnPmizQRaq
            )
        else:
            VnmAPlKFRKPJNjSTgsTtFHxWSelTupCY = (
                    PpKdefOZNalnbKKPZYEFkTizePccpchH(torch.exp(mQPxqKCwqnypKeTKHMQHncgoVnRYGQoB - UhmyIxsZKejneuBmSKTcEPfOqBrixbXR), ipYTWVOPDpfJXeTFApPIgldytQSaUFdk) * NECAaWUrFGIXcLimrerEYmxYIykQBfXb
                    - PpKdefOZNalnbKKPZYEFkTizePccpchH(zhpCBYkwQkhgdrClReoQrMdATdSZEHOs * (torch.exp(xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab) - 1.), ipYTWVOPDpfJXeTFApPIgldytQSaUFdk) * dBJktmjlnYZCfkHVkiGkJCaMOYuHpDIz
                    - PpKdefOZNalnbKKPZYEFkTizePccpchH(zhpCBYkwQkhgdrClReoQrMdATdSZEHOs * ((torch.exp(xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab) - 1.) / xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab - 1.), ipYTWVOPDpfJXeTFApPIgldytQSaUFdk) * tIYldbaSgeVHfQdLotGvnpAoGDTPzJJk
                    - PpKdefOZNalnbKKPZYEFkTizePccpchH(zhpCBYkwQkhgdrClReoQrMdATdSZEHOs * ((torch.exp(xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab) - 1. - xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab) / xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab ** 2 - 0.5), ipYTWVOPDpfJXeTFApPIgldytQSaUFdk) * SYIcqiGMboSYKxqMSlRyCphnPmizQRaq
            )
        return VnmAPlKFRKPJNjSTgsTtFHxWSelTupCY
    def icRlBlcYVSJeCXqgCSYTVpxXSKwJoOPR(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, NECAaWUrFGIXcLimrerEYmxYIykQBfXb, uPePujIqMVDrwNvZQxJajkuaQFAcacjA, XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz, wXwbcvVCQXFmEpNuIRIfbkuOtOpqgUXt, vjtZlQMIzMiiNQGEDKNLZnhxTIPtimCl=False, clbgFKGfOFaPvTRBXwoouOOLgsSYaJzB='dpm_solver', apACmNWgYmlQTXHPQlhMzlFpreaoNbwW=None,
                                     jUXrpBDWrfGGiwtyaMexgPCaBaIoLdEZ=None):
        if wXwbcvVCQXFmEpNuIRIfbkuOtOpqgUXt == 1:
            return rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.zePJdCbCboaUjzbpiWXxZbXDFHTzATZX(NECAaWUrFGIXcLimrerEYmxYIykQBfXb, uPePujIqMVDrwNvZQxJajkuaQFAcacjA, XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz, vjtZlQMIzMiiNQGEDKNLZnhxTIPtimCl=vjtZlQMIzMiiNQGEDKNLZnhxTIPtimCl)
        elif wXwbcvVCQXFmEpNuIRIfbkuOtOpqgUXt == 2:
            return rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.cCvSYUlWQxEFngXCkZIfAYqQMynNlaPB(NECAaWUrFGIXcLimrerEYmxYIykQBfXb, uPePujIqMVDrwNvZQxJajkuaQFAcacjA, XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz, vjtZlQMIzMiiNQGEDKNLZnhxTIPtimCl=vjtZlQMIzMiiNQGEDKNLZnhxTIPtimCl,
                                                            clbgFKGfOFaPvTRBXwoouOOLgsSYaJzB=clbgFKGfOFaPvTRBXwoouOOLgsSYaJzB, apACmNWgYmlQTXHPQlhMzlFpreaoNbwW=apACmNWgYmlQTXHPQlhMzlFpreaoNbwW)
        elif wXwbcvVCQXFmEpNuIRIfbkuOtOpqgUXt == 3:
            return rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.mHiOgvjyrWlQGUVcvEtjFlvyGnxGiITk(NECAaWUrFGIXcLimrerEYmxYIykQBfXb, uPePujIqMVDrwNvZQxJajkuaQFAcacjA, XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz, vjtZlQMIzMiiNQGEDKNLZnhxTIPtimCl=vjtZlQMIzMiiNQGEDKNLZnhxTIPtimCl,
                                                           clbgFKGfOFaPvTRBXwoouOOLgsSYaJzB=clbgFKGfOFaPvTRBXwoouOOLgsSYaJzB, apACmNWgYmlQTXHPQlhMzlFpreaoNbwW=apACmNWgYmlQTXHPQlhMzlFpreaoNbwW, jUXrpBDWrfGGiwtyaMexgPCaBaIoLdEZ=jUXrpBDWrfGGiwtyaMexgPCaBaIoLdEZ)
        else:
            raise ValueError("Solver order must be 1 or 2 or 3, got {}".format(wXwbcvVCQXFmEpNuIRIfbkuOtOpqgUXt))
    def EHrYXLYwslqTXMAXfyZhmAlAeMRtJUhw(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, NECAaWUrFGIXcLimrerEYmxYIykQBfXb, mnAIBgWuMvXNfmUTqdOanZcqQsoFdkjZ, wqXgjkKQfegsPGuaedxSYSqZgMJKaPUG, XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz, wXwbcvVCQXFmEpNuIRIfbkuOtOpqgUXt, clbgFKGfOFaPvTRBXwoouOOLgsSYaJzB='dpm_solver'):
        if wXwbcvVCQXFmEpNuIRIfbkuOtOpqgUXt == 1:
            return rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.zePJdCbCboaUjzbpiWXxZbXDFHTzATZX(NECAaWUrFGIXcLimrerEYmxYIykQBfXb, wqXgjkKQfegsPGuaedxSYSqZgMJKaPUG[-1], XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz, JKpyVMrnPSyIBxYqPUjWKtnFnXIMmXeu=mnAIBgWuMvXNfmUTqdOanZcqQsoFdkjZ[-1])
        elif wXwbcvVCQXFmEpNuIRIfbkuOtOpqgUXt == 2:
            return rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.aCOxTfpXBERMDYYcDLWtqpDSGEkAcwGl(NECAaWUrFGIXcLimrerEYmxYIykQBfXb, mnAIBgWuMvXNfmUTqdOanZcqQsoFdkjZ, wqXgjkKQfegsPGuaedxSYSqZgMJKaPUG, XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz, clbgFKGfOFaPvTRBXwoouOOLgsSYaJzB=clbgFKGfOFaPvTRBXwoouOOLgsSYaJzB)
        elif wXwbcvVCQXFmEpNuIRIfbkuOtOpqgUXt == 3:
            return rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.pKPbxwivZVXNcRLKkSEjOstWSeuupZyj(NECAaWUrFGIXcLimrerEYmxYIykQBfXb, mnAIBgWuMvXNfmUTqdOanZcqQsoFdkjZ, wqXgjkKQfegsPGuaedxSYSqZgMJKaPUG, XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz, clbgFKGfOFaPvTRBXwoouOOLgsSYaJzB=clbgFKGfOFaPvTRBXwoouOOLgsSYaJzB)
        else:
            raise ValueError("Solver order must be 1 or 2 or 3, got {}".format(wXwbcvVCQXFmEpNuIRIfbkuOtOpqgUXt))
    def lieinrspmvpJdGRvWmbDEsTLywcStiXK(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, NECAaWUrFGIXcLimrerEYmxYIykQBfXb, wXwbcvVCQXFmEpNuIRIfbkuOtOpqgUXt, mHINwRyYsqlVpxxfXBXtIPLPWtuKirPb, cGnQXRSvlLSuUVfhDJjlqWnweLUeQVRQ, nHhdfLfCCuIPTnfLwRoJKgcxTtMzAVNY=0.05, fFzyGDwsUOSTBngTGiKDqIYKKikweEzG=0.0078, lrGjvYpKmgOnrVeFRaijRVZHIZNddmlD=0.05, theta=0.9, t_err=1e-5,
                            clbgFKGfOFaPvTRBXwoouOOLgsSYaJzB='dpm_solver'):
        jfvFkkyrHbvxGpVllCdQKVvBSNiKEJLj = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.noise_schedule
        uPePujIqMVDrwNvZQxJajkuaQFAcacjA = mHINwRyYsqlVpxxfXBXtIPLPWtuKirPb * torch.ones((NECAaWUrFGIXcLimrerEYmxYIykQBfXb.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[0],)).sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ(NECAaWUrFGIXcLimrerEYmxYIykQBfXb)
        vhxMVZkWRybktsQdWBSYgKuXhuebDAKO = jfvFkkyrHbvxGpVllCdQKVvBSNiKEJLj.iLJAxGawPgVbuzyTPlMNDawbjHhwvWaG(uPePujIqMVDrwNvZQxJajkuaQFAcacjA)
        rlgMzMCTGtPbLYjftQCikhppVMmPJmPh = jfvFkkyrHbvxGpVllCdQKVvBSNiKEJLj.iLJAxGawPgVbuzyTPlMNDawbjHhwvWaG(cGnQXRSvlLSuUVfhDJjlqWnweLUeQVRQ * torch.ones_like(uPePujIqMVDrwNvZQxJajkuaQFAcacjA).sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ(NECAaWUrFGIXcLimrerEYmxYIykQBfXb))
        xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab = nHhdfLfCCuIPTnfLwRoJKgcxTtMzAVNY * torch.ones_like(uPePujIqMVDrwNvZQxJajkuaQFAcacjA).sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ(NECAaWUrFGIXcLimrerEYmxYIykQBfXb)
        sIfmGCKFYSuAcKGivnHeSsHXHFOsVWBD = NECAaWUrFGIXcLimrerEYmxYIykQBfXb
        mqjdnLvRIQanefOEDvuxdBhWzpDCvXGA = 0
        if wXwbcvVCQXFmEpNuIRIfbkuOtOpqgUXt == 2:
            apACmNWgYmlQTXHPQlhMzlFpreaoNbwW = 0.5
            fMYtYQEWpfPgLpStFbLcFCAgefCJZVqx = lambda NECAaWUrFGIXcLimrerEYmxYIykQBfXb, uPePujIqMVDrwNvZQxJajkuaQFAcacjA, XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz: rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.zePJdCbCboaUjzbpiWXxZbXDFHTzATZX(NECAaWUrFGIXcLimrerEYmxYIykQBfXb, uPePujIqMVDrwNvZQxJajkuaQFAcacjA, XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz, vjtZlQMIzMiiNQGEDKNLZnhxTIPtimCl=True)
            QTewZLrAXlAdaNowcloNaGfCJDwQBcZA = lambda NECAaWUrFGIXcLimrerEYmxYIykQBfXb, uPePujIqMVDrwNvZQxJajkuaQFAcacjA, XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz, **kwargs: rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.cCvSYUlWQxEFngXCkZIfAYqQMynNlaPB(NECAaWUrFGIXcLimrerEYmxYIykQBfXb, uPePujIqMVDrwNvZQxJajkuaQFAcacjA, XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz, apACmNWgYmlQTXHPQlhMzlFpreaoNbwW=apACmNWgYmlQTXHPQlhMzlFpreaoNbwW,
                                                                                               clbgFKGfOFaPvTRBXwoouOOLgsSYaJzB=clbgFKGfOFaPvTRBXwoouOOLgsSYaJzB,
                                                                                               **kwargs)
        elif wXwbcvVCQXFmEpNuIRIfbkuOtOpqgUXt == 3:
            apACmNWgYmlQTXHPQlhMzlFpreaoNbwW, jUXrpBDWrfGGiwtyaMexgPCaBaIoLdEZ = 1. / 3., 2. / 3.
            fMYtYQEWpfPgLpStFbLcFCAgefCJZVqx = lambda NECAaWUrFGIXcLimrerEYmxYIykQBfXb, uPePujIqMVDrwNvZQxJajkuaQFAcacjA, XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz: rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.cCvSYUlWQxEFngXCkZIfAYqQMynNlaPB(NECAaWUrFGIXcLimrerEYmxYIykQBfXb, uPePujIqMVDrwNvZQxJajkuaQFAcacjA, XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz, apACmNWgYmlQTXHPQlhMzlFpreaoNbwW=apACmNWgYmlQTXHPQlhMzlFpreaoNbwW,
                                                                                    vjtZlQMIzMiiNQGEDKNLZnhxTIPtimCl=True,
                                                                                    clbgFKGfOFaPvTRBXwoouOOLgsSYaJzB=clbgFKGfOFaPvTRBXwoouOOLgsSYaJzB)
            QTewZLrAXlAdaNowcloNaGfCJDwQBcZA = lambda NECAaWUrFGIXcLimrerEYmxYIykQBfXb, uPePujIqMVDrwNvZQxJajkuaQFAcacjA, XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz, **kwargs: rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.mHiOgvjyrWlQGUVcvEtjFlvyGnxGiITk(NECAaWUrFGIXcLimrerEYmxYIykQBfXb, uPePujIqMVDrwNvZQxJajkuaQFAcacjA, XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz, apACmNWgYmlQTXHPQlhMzlFpreaoNbwW=apACmNWgYmlQTXHPQlhMzlFpreaoNbwW, jUXrpBDWrfGGiwtyaMexgPCaBaIoLdEZ=jUXrpBDWrfGGiwtyaMexgPCaBaIoLdEZ,
                                                                                              clbgFKGfOFaPvTRBXwoouOOLgsSYaJzB=clbgFKGfOFaPvTRBXwoouOOLgsSYaJzB,
                                                                                              **kwargs)
        else:
            raise ValueError("For adaptive step size solver, order must be 2 or 3, got {}".format(wXwbcvVCQXFmEpNuIRIfbkuOtOpqgUXt))
        while torch.abs((uPePujIqMVDrwNvZQxJajkuaQFAcacjA - cGnQXRSvlLSuUVfhDJjlqWnweLUeQVRQ)).mean() > t_err:
            XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz = jfvFkkyrHbvxGpVllCdQKVvBSNiKEJLj.wdxFGSVLvnnzjandRpvORBqdoTWJHGVq(vhxMVZkWRybktsQdWBSYgKuXhuebDAKO + xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab)
            ZzwmGCAzqVbgVDDufCMageHeimvqokZE, UEWXAArpwhTkpDqPIXJbWSOohfmCAjKl = fMYtYQEWpfPgLpStFbLcFCAgefCJZVqx(NECAaWUrFGIXcLimrerEYmxYIykQBfXb, uPePujIqMVDrwNvZQxJajkuaQFAcacjA, XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz)
            fLbnHzqZXIqjDVBxiPXyzqHxgTGjIITY = QTewZLrAXlAdaNowcloNaGfCJDwQBcZA(NECAaWUrFGIXcLimrerEYmxYIykQBfXb, uPePujIqMVDrwNvZQxJajkuaQFAcacjA, XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz, **UEWXAArpwhTkpDqPIXJbWSOohfmCAjKl)
            MOjnRhezkNHoQzGPojAUpkgsQLDRoDNC = torch.max(torch.ones_like(NECAaWUrFGIXcLimrerEYmxYIykQBfXb).sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ(NECAaWUrFGIXcLimrerEYmxYIykQBfXb) * fFzyGDwsUOSTBngTGiKDqIYKKikweEzG, lrGjvYpKmgOnrVeFRaijRVZHIZNddmlD * torch.max(torch.abs(ZzwmGCAzqVbgVDDufCMageHeimvqokZE), torch.abs(sIfmGCKFYSuAcKGivnHeSsHXHFOsVWBD)))
            QrPpJxyAhGHDZrIihecpWhUWRoaPrUQe = lambda powGafreWfwlSAqPpTpUhFgpFVqCPavl: torch.sqrt(torch.square(powGafreWfwlSAqPpTpUhFgpFVqCPavl.reshape((powGafreWfwlSAqPpTpUhFgpFVqCPavl.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[0], -1))).mean(yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk=-1, keepdim=True))
            SYYPPAFevKmmdBYrZSfedDPwLiOMXvUY = QrPpJxyAhGHDZrIihecpWhUWRoaPrUQe((fLbnHzqZXIqjDVBxiPXyzqHxgTGjIITY - ZzwmGCAzqVbgVDDufCMageHeimvqokZE) / MOjnRhezkNHoQzGPojAUpkgsQLDRoDNC).max()
            if torch.all(SYYPPAFevKmmdBYrZSfedDPwLiOMXvUY <= 1.):
                NECAaWUrFGIXcLimrerEYmxYIykQBfXb = fLbnHzqZXIqjDVBxiPXyzqHxgTGjIITY
                uPePujIqMVDrwNvZQxJajkuaQFAcacjA = XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz
                sIfmGCKFYSuAcKGivnHeSsHXHFOsVWBD = ZzwmGCAzqVbgVDDufCMageHeimvqokZE
                vhxMVZkWRybktsQdWBSYgKuXhuebDAKO = jfvFkkyrHbvxGpVllCdQKVvBSNiKEJLj.iLJAxGawPgVbuzyTPlMNDawbjHhwvWaG(uPePujIqMVDrwNvZQxJajkuaQFAcacjA)
            xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab = torch.min(theta * xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab * torch.float_power(SYYPPAFevKmmdBYrZSfedDPwLiOMXvUY, -1. / wXwbcvVCQXFmEpNuIRIfbkuOtOpqgUXt).float(), rlgMzMCTGtPbLYjftQCikhppVMmPJmPh - vhxMVZkWRybktsQdWBSYgKuXhuebDAKO)
            mqjdnLvRIQanefOEDvuxdBhWzpDCvXGA += wXwbcvVCQXFmEpNuIRIfbkuOtOpqgUXt
        print('adaptive solver nfe', mqjdnLvRIQanefOEDvuxdBhWzpDCvXGA)
        return NECAaWUrFGIXcLimrerEYmxYIykQBfXb
    def kzeIpaLNSGyUxNmgVakyIZAkNbjmCUjd(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, NECAaWUrFGIXcLimrerEYmxYIykQBfXb, TMepbhrhtxHODfHDPkWDjgPPPikciJwm=20, t_start=None, t_end=None, wXwbcvVCQXFmEpNuIRIfbkuOtOpqgUXt=3, UTnGvkbfsgLpbYIDcBiyoRRbDkNDhDWP='time_uniform',
               RISfvMcsyLUOJmTUeflroCerpGkgEWru='singlestep', kJMeJunfQdJEWlZODkFUJMscnZjowybH=True, denoise_to_zero=False, clbgFKGfOFaPvTRBXwoouOOLgsSYaJzB='dpm_solver',
               fFzyGDwsUOSTBngTGiKDqIYKKikweEzG=0.0078, lrGjvYpKmgOnrVeFRaijRVZHIZNddmlD=0.05,
               ):
        cGnQXRSvlLSuUVfhDJjlqWnweLUeQVRQ = 1. / rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.noise_schedule.total_N if t_end is None else t_end
        mHINwRyYsqlVpxxfXBXtIPLPWtuKirPb = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.noise_schedule.T if t_start is None else t_start
        fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc = NECAaWUrFGIXcLimrerEYmxYIykQBfXb.fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc
        if RISfvMcsyLUOJmTUeflroCerpGkgEWru == 'adaptive':
            with torch.no_grad():
                NECAaWUrFGIXcLimrerEYmxYIykQBfXb = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.lieinrspmvpJdGRvWmbDEsTLywcStiXK(NECAaWUrFGIXcLimrerEYmxYIykQBfXb, wXwbcvVCQXFmEpNuIRIfbkuOtOpqgUXt=wXwbcvVCQXFmEpNuIRIfbkuOtOpqgUXt, mHINwRyYsqlVpxxfXBXtIPLPWtuKirPb=mHINwRyYsqlVpxxfXBXtIPLPWtuKirPb, cGnQXRSvlLSuUVfhDJjlqWnweLUeQVRQ=cGnQXRSvlLSuUVfhDJjlqWnweLUeQVRQ, fFzyGDwsUOSTBngTGiKDqIYKKikweEzG=fFzyGDwsUOSTBngTGiKDqIYKKikweEzG, lrGjvYpKmgOnrVeFRaijRVZHIZNddmlD=lrGjvYpKmgOnrVeFRaijRVZHIZNddmlD,
                                             clbgFKGfOFaPvTRBXwoouOOLgsSYaJzB=clbgFKGfOFaPvTRBXwoouOOLgsSYaJzB)
        elif RISfvMcsyLUOJmTUeflroCerpGkgEWru == 'multistep':
            assert TMepbhrhtxHODfHDPkWDjgPPPikciJwm >= wXwbcvVCQXFmEpNuIRIfbkuOtOpqgUXt
            iaqNqpReXPEdYpNiyUIejEPLCqtbtedA = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.ElndQeTbOYtRDqLuGQeraWztpYSiBrGs(UTnGvkbfsgLpbYIDcBiyoRRbDkNDhDWP=UTnGvkbfsgLpbYIDcBiyoRRbDkNDhDWP, mHINwRyYsqlVpxxfXBXtIPLPWtuKirPb=mHINwRyYsqlVpxxfXBXtIPLPWtuKirPb, cGnQXRSvlLSuUVfhDJjlqWnweLUeQVRQ=cGnQXRSvlLSuUVfhDJjlqWnweLUeQVRQ, CkYaWzCjmffLyFAjukkxYTtrfjqQGpts=TMepbhrhtxHODfHDPkWDjgPPPikciJwm, fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc=fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc)
            assert iaqNqpReXPEdYpNiyUIejEPLCqtbtedA.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[0] - 1 == TMepbhrhtxHODfHDPkWDjgPPPikciJwm
            with torch.no_grad():
                ubgqOHWKiJfkwebByeHqjVWxaVQBtZfc = iaqNqpReXPEdYpNiyUIejEPLCqtbtedA[0].expand((NECAaWUrFGIXcLimrerEYmxYIykQBfXb.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[0]))
                mnAIBgWuMvXNfmUTqdOanZcqQsoFdkjZ = [rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.NRtnQQOkbUbfnbxzIRWvMfkdGBlGyoSB(NECAaWUrFGIXcLimrerEYmxYIykQBfXb, ubgqOHWKiJfkwebByeHqjVWxaVQBtZfc)]
                wqXgjkKQfegsPGuaedxSYSqZgMJKaPUG = [ubgqOHWKiJfkwebByeHqjVWxaVQBtZfc]
                for NXtisIPzJfpoZPYPDAsYSVWzLwRPUvPi in tqdm(range(1, wXwbcvVCQXFmEpNuIRIfbkuOtOpqgUXt), desc="DPM init order"):
                    ubgqOHWKiJfkwebByeHqjVWxaVQBtZfc = iaqNqpReXPEdYpNiyUIejEPLCqtbtedA[NXtisIPzJfpoZPYPDAsYSVWzLwRPUvPi].expand(NECAaWUrFGIXcLimrerEYmxYIykQBfXb.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[0])
                    NECAaWUrFGIXcLimrerEYmxYIykQBfXb = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.EHrYXLYwslqTXMAXfyZhmAlAeMRtJUhw(NECAaWUrFGIXcLimrerEYmxYIykQBfXb, mnAIBgWuMvXNfmUTqdOanZcqQsoFdkjZ, wqXgjkKQfegsPGuaedxSYSqZgMJKaPUG, ubgqOHWKiJfkwebByeHqjVWxaVQBtZfc, NXtisIPzJfpoZPYPDAsYSVWzLwRPUvPi,
                                                         clbgFKGfOFaPvTRBXwoouOOLgsSYaJzB=clbgFKGfOFaPvTRBXwoouOOLgsSYaJzB)
                    mnAIBgWuMvXNfmUTqdOanZcqQsoFdkjZ.append(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.NRtnQQOkbUbfnbxzIRWvMfkdGBlGyoSB(NECAaWUrFGIXcLimrerEYmxYIykQBfXb, ubgqOHWKiJfkwebByeHqjVWxaVQBtZfc))
                    wqXgjkKQfegsPGuaedxSYSqZgMJKaPUG.append(ubgqOHWKiJfkwebByeHqjVWxaVQBtZfc)
                for UHmIQCHeLkozPfaktIdEHKdpTVYzCLhe in tqdm(range(wXwbcvVCQXFmEpNuIRIfbkuOtOpqgUXt, TMepbhrhtxHODfHDPkWDjgPPPikciJwm + 1), desc="DPM multistep"):
                    ubgqOHWKiJfkwebByeHqjVWxaVQBtZfc = iaqNqpReXPEdYpNiyUIejEPLCqtbtedA[UHmIQCHeLkozPfaktIdEHKdpTVYzCLhe].expand(NECAaWUrFGIXcLimrerEYmxYIykQBfXb.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[0])
                    if kJMeJunfQdJEWlZODkFUJMscnZjowybH and TMepbhrhtxHODfHDPkWDjgPPPikciJwm < 15:
                        KkhznVwRNMiGWgfmazqJiXncNhcNXZuU = min(wXwbcvVCQXFmEpNuIRIfbkuOtOpqgUXt, TMepbhrhtxHODfHDPkWDjgPPPikciJwm + 1 - UHmIQCHeLkozPfaktIdEHKdpTVYzCLhe)
                    else:
                        KkhznVwRNMiGWgfmazqJiXncNhcNXZuU = wXwbcvVCQXFmEpNuIRIfbkuOtOpqgUXt
                    NECAaWUrFGIXcLimrerEYmxYIykQBfXb = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.EHrYXLYwslqTXMAXfyZhmAlAeMRtJUhw(NECAaWUrFGIXcLimrerEYmxYIykQBfXb, mnAIBgWuMvXNfmUTqdOanZcqQsoFdkjZ, wqXgjkKQfegsPGuaedxSYSqZgMJKaPUG, ubgqOHWKiJfkwebByeHqjVWxaVQBtZfc, KkhznVwRNMiGWgfmazqJiXncNhcNXZuU,
                                                         clbgFKGfOFaPvTRBXwoouOOLgsSYaJzB=clbgFKGfOFaPvTRBXwoouOOLgsSYaJzB)
                    for HCXmerBqIMuTscBONzTGKYapYSxWTYHo in range(wXwbcvVCQXFmEpNuIRIfbkuOtOpqgUXt - 1):
                        wqXgjkKQfegsPGuaedxSYSqZgMJKaPUG[HCXmerBqIMuTscBONzTGKYapYSxWTYHo] = wqXgjkKQfegsPGuaedxSYSqZgMJKaPUG[HCXmerBqIMuTscBONzTGKYapYSxWTYHo + 1]
                        mnAIBgWuMvXNfmUTqdOanZcqQsoFdkjZ[HCXmerBqIMuTscBONzTGKYapYSxWTYHo] = mnAIBgWuMvXNfmUTqdOanZcqQsoFdkjZ[HCXmerBqIMuTscBONzTGKYapYSxWTYHo + 1]
                    wqXgjkKQfegsPGuaedxSYSqZgMJKaPUG[-1] = ubgqOHWKiJfkwebByeHqjVWxaVQBtZfc
                    if UHmIQCHeLkozPfaktIdEHKdpTVYzCLhe < TMepbhrhtxHODfHDPkWDjgPPPikciJwm:
                        mnAIBgWuMvXNfmUTqdOanZcqQsoFdkjZ[-1] = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.NRtnQQOkbUbfnbxzIRWvMfkdGBlGyoSB(NECAaWUrFGIXcLimrerEYmxYIykQBfXb, ubgqOHWKiJfkwebByeHqjVWxaVQBtZfc)
        elif RISfvMcsyLUOJmTUeflroCerpGkgEWru in ['singlestep', 'singlestep_fixed']:
            if RISfvMcsyLUOJmTUeflroCerpGkgEWru == 'singlestep':
                coSeFJMSLBWMYiIkaNMRNLvdHvyQfsub, CfVKhsKPtOaiLDSyReEIATrYxiCnFRUx = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.OzGAVUZhZNxvvNdRVOEiOFXPHiFcoPXh(TMepbhrhtxHODfHDPkWDjgPPPikciJwm=TMepbhrhtxHODfHDPkWDjgPPPikciJwm, wXwbcvVCQXFmEpNuIRIfbkuOtOpqgUXt=wXwbcvVCQXFmEpNuIRIfbkuOtOpqgUXt,
                                                                                              UTnGvkbfsgLpbYIDcBiyoRRbDkNDhDWP=UTnGvkbfsgLpbYIDcBiyoRRbDkNDhDWP,
                                                                                              mHINwRyYsqlVpxxfXBXtIPLPWtuKirPb=mHINwRyYsqlVpxxfXBXtIPLPWtuKirPb, cGnQXRSvlLSuUVfhDJjlqWnweLUeQVRQ=cGnQXRSvlLSuUVfhDJjlqWnweLUeQVRQ,
                                                                                              fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc=fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc)
            elif RISfvMcsyLUOJmTUeflroCerpGkgEWru == 'singlestep_fixed':
                aNvhFlguADxtQkYwCswjOmevkulEaSVC = TMepbhrhtxHODfHDPkWDjgPPPikciJwm // wXwbcvVCQXFmEpNuIRIfbkuOtOpqgUXt
                CfVKhsKPtOaiLDSyReEIATrYxiCnFRUx = [wXwbcvVCQXFmEpNuIRIfbkuOtOpqgUXt, ] * aNvhFlguADxtQkYwCswjOmevkulEaSVC
                coSeFJMSLBWMYiIkaNMRNLvdHvyQfsub = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.ElndQeTbOYtRDqLuGQeraWztpYSiBrGs(UTnGvkbfsgLpbYIDcBiyoRRbDkNDhDWP=UTnGvkbfsgLpbYIDcBiyoRRbDkNDhDWP, mHINwRyYsqlVpxxfXBXtIPLPWtuKirPb=mHINwRyYsqlVpxxfXBXtIPLPWtuKirPb, cGnQXRSvlLSuUVfhDJjlqWnweLUeQVRQ=cGnQXRSvlLSuUVfhDJjlqWnweLUeQVRQ, CkYaWzCjmffLyFAjukkxYTtrfjqQGpts=aNvhFlguADxtQkYwCswjOmevkulEaSVC, fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc=fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc)
            for HCXmerBqIMuTscBONzTGKYapYSxWTYHo, wXwbcvVCQXFmEpNuIRIfbkuOtOpqgUXt in enumerate(CfVKhsKPtOaiLDSyReEIATrYxiCnFRUx):
                MkemZEpAULATkaYPnlBjSlMeMpUggebX, pKBpOcVPSggUjrsJvYFvWhZizpIXqoJo = coSeFJMSLBWMYiIkaNMRNLvdHvyQfsub[HCXmerBqIMuTscBONzTGKYapYSxWTYHo], coSeFJMSLBWMYiIkaNMRNLvdHvyQfsub[HCXmerBqIMuTscBONzTGKYapYSxWTYHo + 1]
                FSFebfBujeGSDFGyUpPSIyjPnUKTzlVE = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.ElndQeTbOYtRDqLuGQeraWztpYSiBrGs(UTnGvkbfsgLpbYIDcBiyoRRbDkNDhDWP=UTnGvkbfsgLpbYIDcBiyoRRbDkNDhDWP, mHINwRyYsqlVpxxfXBXtIPLPWtuKirPb=MkemZEpAULATkaYPnlBjSlMeMpUggebX.ygFiYnqtfEqFJmbillPxtHRxsUoFqqJk(), cGnQXRSvlLSuUVfhDJjlqWnweLUeQVRQ=pKBpOcVPSggUjrsJvYFvWhZizpIXqoJo.ygFiYnqtfEqFJmbillPxtHRxsUoFqqJk(),
                                                      CkYaWzCjmffLyFAjukkxYTtrfjqQGpts=wXwbcvVCQXFmEpNuIRIfbkuOtOpqgUXt, fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc=fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc)
                ARcuPXUdKWlxsqiFxuAAwYcGtiPuEeUW = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.noise_schedule.iLJAxGawPgVbuzyTPlMNDawbjHhwvWaG(FSFebfBujeGSDFGyUpPSIyjPnUKTzlVE)
                vvuPJagNJJZhVClXSgZmbfzrQPjdoDta, ubgqOHWKiJfkwebByeHqjVWxaVQBtZfc = MkemZEpAULATkaYPnlBjSlMeMpUggebX.tile(NECAaWUrFGIXcLimrerEYmxYIykQBfXb.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[0]), pKBpOcVPSggUjrsJvYFvWhZizpIXqoJo.tile(NECAaWUrFGIXcLimrerEYmxYIykQBfXb.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[0])
                xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab = ARcuPXUdKWlxsqiFxuAAwYcGtiPuEeUW[-1] - ARcuPXUdKWlxsqiFxuAAwYcGtiPuEeUW[0]
                apACmNWgYmlQTXHPQlhMzlFpreaoNbwW = None if wXwbcvVCQXFmEpNuIRIfbkuOtOpqgUXt <= 1 else (ARcuPXUdKWlxsqiFxuAAwYcGtiPuEeUW[1] - ARcuPXUdKWlxsqiFxuAAwYcGtiPuEeUW[0]) / xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab
                jUXrpBDWrfGGiwtyaMexgPCaBaIoLdEZ = None if wXwbcvVCQXFmEpNuIRIfbkuOtOpqgUXt <= 2 else (ARcuPXUdKWlxsqiFxuAAwYcGtiPuEeUW[2] - ARcuPXUdKWlxsqiFxuAAwYcGtiPuEeUW[0]) / xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab
                NECAaWUrFGIXcLimrerEYmxYIykQBfXb = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.icRlBlcYVSJeCXqgCSYTVpxXSKwJoOPR(NECAaWUrFGIXcLimrerEYmxYIykQBfXb, vvuPJagNJJZhVClXSgZmbfzrQPjdoDta, ubgqOHWKiJfkwebByeHqjVWxaVQBtZfc, wXwbcvVCQXFmEpNuIRIfbkuOtOpqgUXt, clbgFKGfOFaPvTRBXwoouOOLgsSYaJzB=clbgFKGfOFaPvTRBXwoouOOLgsSYaJzB, apACmNWgYmlQTXHPQlhMzlFpreaoNbwW=apACmNWgYmlQTXHPQlhMzlFpreaoNbwW, jUXrpBDWrfGGiwtyaMexgPCaBaIoLdEZ=jUXrpBDWrfGGiwtyaMexgPCaBaIoLdEZ)
        if denoise_to_zero:
            NECAaWUrFGIXcLimrerEYmxYIykQBfXb = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.zICaXPrVsokCiDEggpgVRYpzbYydrnAQ(NECAaWUrFGIXcLimrerEYmxYIykQBfXb, torch.ones((NECAaWUrFGIXcLimrerEYmxYIykQBfXb.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[0],)).sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ(fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc) * cGnQXRSvlLSuUVfhDJjlqWnweLUeQVRQ)
        return NECAaWUrFGIXcLimrerEYmxYIykQBfXb
def YcCWLCgdGWkdmvnGxsHCCaNMxPgfJjif(NECAaWUrFGIXcLimrerEYmxYIykQBfXb, xp, yp):
    CkYaWzCjmffLyFAjukkxYTtrfjqQGpts, aNvhFlguADxtQkYwCswjOmevkulEaSVC = NECAaWUrFGIXcLimrerEYmxYIykQBfXb.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[0], xp.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[1]
    GJnTzvJDQaZhOfErvocNUfvXRYMmhxXG = torch.cat([NECAaWUrFGIXcLimrerEYmxYIykQBfXb.unsqueeze(2), xp.unsqueeze(0).kYXcbCDGZMxtOlIZeOtGMsNePlSickQL((CkYaWzCjmffLyFAjukkxYTtrfjqQGpts, 1, 1))], yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk=2)
    veOcQzvqqiEtFTzdrAdOuOuajaCyYaNM, dWAhaIRDKBNliqmxofHmfOxHhgTLXpMX = torch.sort(GJnTzvJDQaZhOfErvocNUfvXRYMmhxXG, yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk=2)
    bBizCRUaUcQjRYZggLIwVdqDmzQUfbgW = torch.argmin(dWAhaIRDKBNliqmxofHmfOxHhgTLXpMX, yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk=2)
    fNfHtiMQEVFblXjpYWUzRLgmOiVskuVB = bBizCRUaUcQjRYZggLIwVdqDmzQUfbgW - 1
    YSWjXMdntvgpMJRlrzjRdAeNJKgXVqSE = torch.where(
        torch.eq(bBizCRUaUcQjRYZggLIwVdqDmzQUfbgW, 0),
        torch.xPmCFphFKpGMpIsczaSKHmMgRPZzJwla(1, fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc=NECAaWUrFGIXcLimrerEYmxYIykQBfXb.fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc),
        torch.where(
            torch.eq(bBizCRUaUcQjRYZggLIwVdqDmzQUfbgW, aNvhFlguADxtQkYwCswjOmevkulEaSVC), torch.xPmCFphFKpGMpIsczaSKHmMgRPZzJwla(aNvhFlguADxtQkYwCswjOmevkulEaSVC - 2, fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc=NECAaWUrFGIXcLimrerEYmxYIykQBfXb.fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc), fNfHtiMQEVFblXjpYWUzRLgmOiVskuVB,
        ),
    )
    diQYjAzcNZDDcoHotvBEFPKulZJvsghn = torch.where(torch.eq(YSWjXMdntvgpMJRlrzjRdAeNJKgXVqSE, fNfHtiMQEVFblXjpYWUzRLgmOiVskuVB), YSWjXMdntvgpMJRlrzjRdAeNJKgXVqSE + 2, YSWjXMdntvgpMJRlrzjRdAeNJKgXVqSE + 1)
    pwLEUGHCChqZduZESifHxuarmFZxzIUb = torch.gather(veOcQzvqqiEtFTzdrAdOuOuajaCyYaNM, yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk=2, index=YSWjXMdntvgpMJRlrzjRdAeNJKgXVqSE.unsqueeze(2)).squeeze(2)
    yRSqwFHimLhBGpEzScGoDIhnPDxhttlY = torch.gather(veOcQzvqqiEtFTzdrAdOuOuajaCyYaNM, yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk=2, index=diQYjAzcNZDDcoHotvBEFPKulZJvsghn.unsqueeze(2)).squeeze(2)
    FipcdKcqUlnptNlBzJoSdjXEuvFHBZYp = torch.where(
        torch.eq(bBizCRUaUcQjRYZggLIwVdqDmzQUfbgW, 0),
        torch.xPmCFphFKpGMpIsczaSKHmMgRPZzJwla(0, fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc=NECAaWUrFGIXcLimrerEYmxYIykQBfXb.fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc),
        torch.where(
            torch.eq(bBizCRUaUcQjRYZggLIwVdqDmzQUfbgW, aNvhFlguADxtQkYwCswjOmevkulEaSVC), torch.xPmCFphFKpGMpIsczaSKHmMgRPZzJwla(aNvhFlguADxtQkYwCswjOmevkulEaSVC - 2, fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc=NECAaWUrFGIXcLimrerEYmxYIykQBfXb.fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc), fNfHtiMQEVFblXjpYWUzRLgmOiVskuVB,
        ),
    )
    hcFRZmYQUsPNFIkzgnATgOxdjUyiIqRE = yp.unsqueeze(0).expand(CkYaWzCjmffLyFAjukkxYTtrfjqQGpts, -1, -1)
    aLjyEPEXBdcjpnDlzFAHCkyAGFJLiQAc = torch.gather(hcFRZmYQUsPNFIkzgnATgOxdjUyiIqRE, yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk=2, index=FipcdKcqUlnptNlBzJoSdjXEuvFHBZYp.unsqueeze(2)).squeeze(2)
    jTYKYcAvoGSJwnzlYUMStKtWxGkSTfir = torch.gather(hcFRZmYQUsPNFIkzgnATgOxdjUyiIqRE, yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk=2, index=(FipcdKcqUlnptNlBzJoSdjXEuvFHBZYp + 1).unsqueeze(2)).squeeze(2)
    RZxSDuuYafTnwyTCRTDfMGrCjxAkeiXg = aLjyEPEXBdcjpnDlzFAHCkyAGFJLiQAc + (NECAaWUrFGIXcLimrerEYmxYIykQBfXb - pwLEUGHCChqZduZESifHxuarmFZxzIUb) * (jTYKYcAvoGSJwnzlYUMStKtWxGkSTfir - aLjyEPEXBdcjpnDlzFAHCkyAGFJLiQAc) / (yRSqwFHimLhBGpEzScGoDIhnPDxhttlY - pwLEUGHCChqZduZESifHxuarmFZxzIUb)
    return RZxSDuuYafTnwyTCRTDfMGrCjxAkeiXg
def PpKdefOZNalnbKKPZYEFkTizePccpchH(powGafreWfwlSAqPpTpUhFgpFVqCPavl, ipYTWVOPDpfJXeTFApPIgldytQSaUFdk):
    return powGafreWfwlSAqPpTpUhFgpFVqCPavl[(...,) + (None,) * (ipYTWVOPDpfJXeTFApPIgldytQSaUFdk - 1)]