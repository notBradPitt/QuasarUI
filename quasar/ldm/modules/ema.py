import torch
from torch import nn
class FNPzkrvGxaqvoCNOqICrVrrNcmdkiBFJ(nn.Module):
    def __init__(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM, eeehCkWlicOSSZeEWMocEIpaDJxlRTfD=0.9999, use_num_upates=True):
        super().__init__()
        if eeehCkWlicOSSZeEWMocEIpaDJxlRTfD < 0.0 or eeehCkWlicOSSZeEWMocEIpaDJxlRTfD > 1.0:
            raise ValueError('Decay must be between 0 and 1')
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.m_name2s_name = {}
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.BpOtVuSttURsCNYELWmrxpBkqOPYBBlj('decay', torch.xPmCFphFKpGMpIsczaSKHmMgRPZzJwla(eeehCkWlicOSSZeEWMocEIpaDJxlRTfD, DDRQlhrNSGpwTrokWitkZipdfbAqBFxv=torch.float32))
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.BpOtVuSttURsCNYELWmrxpBkqOPYBBlj('num_updates', torch.xPmCFphFKpGMpIsczaSKHmMgRPZzJwla(0, DDRQlhrNSGpwTrokWitkZipdfbAqBFxv=torch.int) if use_num_upates
        else torch.xPmCFphFKpGMpIsczaSKHmMgRPZzJwla(-1, DDRQlhrNSGpwTrokWitkZipdfbAqBFxv=torch.int))
        for pSfJNVvqLWVlUeHdpahCTGSrSPJYAnEQ, HutkrxeXIuRQKOhCWHkiwqLGAsJjUSKj in VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM.named_parameters():
            if HutkrxeXIuRQKOhCWHkiwqLGAsJjUSKj.requires_grad:
                mDtiVcQQGxNFjYuUGgPRCKftGiKZKSux = pSfJNVvqLWVlUeHdpahCTGSrSPJYAnEQ.replace('.', '')
                rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.m_name2s_name.update({pSfJNVvqLWVlUeHdpahCTGSrSPJYAnEQ: mDtiVcQQGxNFjYuUGgPRCKftGiKZKSux})
                rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.BpOtVuSttURsCNYELWmrxpBkqOPYBBlj(mDtiVcQQGxNFjYuUGgPRCKftGiKZKSux, HutkrxeXIuRQKOhCWHkiwqLGAsJjUSKj.tEcQvpBwXwdqvKxRTLEBROBUyPoodldL().detach().data)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.collected_params = []
    def QUnBChpydDvJCBjwmHKTcazasCgmERja(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS):
        del rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.num_updates
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.BpOtVuSttURsCNYELWmrxpBkqOPYBBlj('num_updates', torch.xPmCFphFKpGMpIsczaSKHmMgRPZzJwla(0, DDRQlhrNSGpwTrokWitkZipdfbAqBFxv=torch.int))
    def lqBgIcSWZYylbCPjXksJWDguuSOqoPCJ(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM):
        eeehCkWlicOSSZeEWMocEIpaDJxlRTfD = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.eeehCkWlicOSSZeEWMocEIpaDJxlRTfD
        if rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.num_updates >= 0:
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.num_updates += 1
            eeehCkWlicOSSZeEWMocEIpaDJxlRTfD = min(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.eeehCkWlicOSSZeEWMocEIpaDJxlRTfD, (1 + rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.num_updates) / (10 + rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.num_updates))
        csonSzeugGtjtNorYRFkUrrawxpFhjkz = 1.0 - eeehCkWlicOSSZeEWMocEIpaDJxlRTfD
        with torch.no_grad():
            TZZLYnplGsHesOcYSEkicfkLRCTsNCcX = dict(VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM.named_parameters())
            UOsotmsFkQxhAZTWfptQVusQmsCWOlcH = dict(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.named_buffers())
            for nyrzKxQtioheHIZujafABgijbCjrWhBU in TZZLYnplGsHesOcYSEkicfkLRCTsNCcX:
                if TZZLYnplGsHesOcYSEkicfkLRCTsNCcX[nyrzKxQtioheHIZujafABgijbCjrWhBU].requires_grad:
                    qTTUUsKLhwQIxyPAyEGufGzzatNTCuBv = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.m_name2s_name[nyrzKxQtioheHIZujafABgijbCjrWhBU]
                    UOsotmsFkQxhAZTWfptQVusQmsCWOlcH[qTTUUsKLhwQIxyPAyEGufGzzatNTCuBv] = UOsotmsFkQxhAZTWfptQVusQmsCWOlcH[qTTUUsKLhwQIxyPAyEGufGzzatNTCuBv].type_as(TZZLYnplGsHesOcYSEkicfkLRCTsNCcX[nyrzKxQtioheHIZujafABgijbCjrWhBU])
                    UOsotmsFkQxhAZTWfptQVusQmsCWOlcH[qTTUUsKLhwQIxyPAyEGufGzzatNTCuBv].sub_(csonSzeugGtjtNorYRFkUrrawxpFhjkz * (UOsotmsFkQxhAZTWfptQVusQmsCWOlcH[qTTUUsKLhwQIxyPAyEGufGzzatNTCuBv] - TZZLYnplGsHesOcYSEkicfkLRCTsNCcX[nyrzKxQtioheHIZujafABgijbCjrWhBU]))
                else:
                    assert not nyrzKxQtioheHIZujafABgijbCjrWhBU in rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.m_name2s_name
    def cxEZDJIlvgwWEipGcqcszbHomLBZFKCo(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM):
        TZZLYnplGsHesOcYSEkicfkLRCTsNCcX = dict(VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM.named_parameters())
        UOsotmsFkQxhAZTWfptQVusQmsCWOlcH = dict(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.named_buffers())
        for nyrzKxQtioheHIZujafABgijbCjrWhBU in TZZLYnplGsHesOcYSEkicfkLRCTsNCcX:
            if TZZLYnplGsHesOcYSEkicfkLRCTsNCcX[nyrzKxQtioheHIZujafABgijbCjrWhBU].requires_grad:
                TZZLYnplGsHesOcYSEkicfkLRCTsNCcX[nyrzKxQtioheHIZujafABgijbCjrWhBU].data.copy_(UOsotmsFkQxhAZTWfptQVusQmsCWOlcH[rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.m_name2s_name[nyrzKxQtioheHIZujafABgijbCjrWhBU]].data)
            else:
                assert not nyrzKxQtioheHIZujafABgijbCjrWhBU in rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.m_name2s_name
    def RqdzCAmZioTnqOtBxyPpQMpxNZqqYqMv(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, parameters):
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.collected_params = [wqONwpPqzusAImUvAyPmoTAxAbxfcvHV.tEcQvpBwXwdqvKxRTLEBROBUyPoodldL() for wqONwpPqzusAImUvAyPmoTAxAbxfcvHV in parameters]
    def ySkZIiRSiuKfRdBOssYffHcPMeZbGctR(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, parameters):
        for UaQRnthcfypVGFewwSfFsMNpKCsyXrvw, wqONwpPqzusAImUvAyPmoTAxAbxfcvHV in zip(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.collected_params, parameters):
            wqONwpPqzusAImUvAyPmoTAxAbxfcvHV.data.copy_(UaQRnthcfypVGFewwSfFsMNpKCsyXrvw.data)
