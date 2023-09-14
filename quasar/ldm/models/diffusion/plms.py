import torch
import numpy as np
from tqdm import tqdm
from functools import partial
from ldm.modules.diffusionmodules.util import vARPohLnkqbmEgaTgkzsKrKSnRlVAXsG, ydGLHegofJxILoEQvdIngtXoioplZMrS, LrAizKrQgKBxXFjYQZHueeWsViuvAXJp
from ldm.models.diffusion.sampling_util import FuFPjwbSOSOGsduutWbGgxcLyqowDcLE
class sXLiacNyCNvYEcqslQTODwAWZJdLwDPI(object):
    def __init__(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM, HtnYKlBDuwwBEVdTVKsUENSQHeXnhZXs="linear", fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc=torch.fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc("cuda"), **kwargs):
        super().__init__()
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM = VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.ddpm_num_timesteps = VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM.num_timesteps
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.HtnYKlBDuwwBEVdTVKsUENSQHeXnhZXs = HtnYKlBDuwwBEVdTVKsUENSQHeXnhZXs
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc = fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc
    def BpOtVuSttURsCNYELWmrxpBkqOPYBBlj(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, name, jXgWCEykFJZnOJknbIlhJGCSQwytwtJP):
        if type(jXgWCEykFJZnOJknbIlhJGCSQwytwtJP) == torch.Tensor:
            if jXgWCEykFJZnOJknbIlhJGCSQwytwtJP.fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc != rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc:
                jXgWCEykFJZnOJknbIlhJGCSQwytwtJP = jXgWCEykFJZnOJknbIlhJGCSQwytwtJP.sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc)
        setattr(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, name, jXgWCEykFJZnOJknbIlhJGCSQwytwtJP)
    def tsMUuSGvjHEShpizgUiHhBUvXzEpNCvO(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, ddim_num_steps, ddim_discretize="uniform", ddim_eta=0., aFZoJwWpCnqyOJdcAMLlqOHxDgjPTNCS=True):
        if ddim_eta != 0:
            raise ValueError('ddim_eta must be 0 for PLMS')
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.xaHdUhZcWVcLrTPEWFnTJjCgaiOMOyDm = ydGLHegofJxILoEQvdIngtXoioplZMrS(ddim_discr_method=ddim_discretize, num_ddim_timesteps=ddim_num_steps,
                                                  buEvQvwasZgYyUqrxGfyNjTbzvwhzPXv=rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.ddpm_num_timesteps,aFZoJwWpCnqyOJdcAMLlqOHxDgjPTNCS=aFZoJwWpCnqyOJdcAMLlqOHxDgjPTNCS)
        IOpmYnAWyhIWgvrJQuznNWQMTUXYwThN = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM.IOpmYnAWyhIWgvrJQuznNWQMTUXYwThN
        assert IOpmYnAWyhIWgvrJQuznNWQMTUXYwThN.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[0] == rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.ddpm_num_timesteps, 'alphas have to be defined for each timestep'
        KCffkVYSQPmjfNVfROGpIWQLEwTjwGnQ = lambda NECAaWUrFGIXcLimrerEYmxYIykQBfXb: NECAaWUrFGIXcLimrerEYmxYIykQBfXb.tEcQvpBwXwdqvKxRTLEBROBUyPoodldL().detach().sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ(torch.float32).sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM.fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.BpOtVuSttURsCNYELWmrxpBkqOPYBBlj('betas', KCffkVYSQPmjfNVfROGpIWQLEwTjwGnQ(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM.aGiatFWLVusbPGSDloFtejqscKjAwtLv))
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.BpOtVuSttURsCNYELWmrxpBkqOPYBBlj('alphas_cumprod', KCffkVYSQPmjfNVfROGpIWQLEwTjwGnQ(IOpmYnAWyhIWgvrJQuznNWQMTUXYwThN))
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.BpOtVuSttURsCNYELWmrxpBkqOPYBBlj('alphas_cumprod_prev', KCffkVYSQPmjfNVfROGpIWQLEwTjwGnQ(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM.xbuEtLNyZNkLwkSOeiFKOKlofYAdfmXP))
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.BpOtVuSttURsCNYELWmrxpBkqOPYBBlj('sqrt_alphas_cumprod', KCffkVYSQPmjfNVfROGpIWQLEwTjwGnQ(np.sqrt(IOpmYnAWyhIWgvrJQuznNWQMTUXYwThN.cpu())))
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.BpOtVuSttURsCNYELWmrxpBkqOPYBBlj('sqrt_one_minus_alphas_cumprod', KCffkVYSQPmjfNVfROGpIWQLEwTjwGnQ(np.sqrt(1. - IOpmYnAWyhIWgvrJQuznNWQMTUXYwThN.cpu())))
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.BpOtVuSttURsCNYELWmrxpBkqOPYBBlj('log_one_minus_alphas_cumprod', KCffkVYSQPmjfNVfROGpIWQLEwTjwGnQ(np.DJwhOGBaLcOjmXnuwXMXOyhMtknqkKXL(1. - IOpmYnAWyhIWgvrJQuznNWQMTUXYwThN.cpu())))
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.BpOtVuSttURsCNYELWmrxpBkqOPYBBlj('sqrt_recip_alphas_cumprod', KCffkVYSQPmjfNVfROGpIWQLEwTjwGnQ(np.sqrt(1. / IOpmYnAWyhIWgvrJQuznNWQMTUXYwThN.cpu())))
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.BpOtVuSttURsCNYELWmrxpBkqOPYBBlj('sqrt_recipm1_alphas_cumprod', KCffkVYSQPmjfNVfROGpIWQLEwTjwGnQ(np.sqrt(1. / IOpmYnAWyhIWgvrJQuznNWQMTUXYwThN.cpu() - 1)))
        UhwxvNJOIOpYuDYuLFnCTFkDJmQARxHP, QjiFjIOgEuLEafnVNKmbYgjRnHbwNhfp, DaGHMszTvPtphdOZZoBVaYSOdJOBoPWO = vARPohLnkqbmEgaTgkzsKrKSnRlVAXsG(alphacums=IOpmYnAWyhIWgvrJQuznNWQMTUXYwThN.cpu(),
                                                                                   xaHdUhZcWVcLrTPEWFnTJjCgaiOMOyDm=rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.xaHdUhZcWVcLrTPEWFnTJjCgaiOMOyDm,
                                                                                   YifKHCfIbeEsuQSFLLpJatOOrlBeQSoO=ddim_eta,aFZoJwWpCnqyOJdcAMLlqOHxDgjPTNCS=aFZoJwWpCnqyOJdcAMLlqOHxDgjPTNCS)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.BpOtVuSttURsCNYELWmrxpBkqOPYBBlj('ddim_sigmas', UhwxvNJOIOpYuDYuLFnCTFkDJmQARxHP)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.BpOtVuSttURsCNYELWmrxpBkqOPYBBlj('ddim_alphas', QjiFjIOgEuLEafnVNKmbYgjRnHbwNhfp)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.BpOtVuSttURsCNYELWmrxpBkqOPYBBlj('ddim_alphas_prev', DaGHMszTvPtphdOZZoBVaYSOdJOBoPWO)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.BpOtVuSttURsCNYELWmrxpBkqOPYBBlj('ddim_sqrt_one_minus_alphas', np.sqrt(1. - QjiFjIOgEuLEafnVNKmbYgjRnHbwNhfp))
        vBPOJjGyjhtkzVvYBwezKxRzAFlVcNcY = ddim_eta * torch.sqrt(
            (1 - rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.xbuEtLNyZNkLwkSOeiFKOKlofYAdfmXP) / (1 - rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.IOpmYnAWyhIWgvrJQuznNWQMTUXYwThN) * (
                        1 - rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.IOpmYnAWyhIWgvrJQuznNWQMTUXYwThN / rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.xbuEtLNyZNkLwkSOeiFKOKlofYAdfmXP))
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.BpOtVuSttURsCNYELWmrxpBkqOPYBBlj('ddim_sigmas_for_original_num_steps', vBPOJjGyjhtkzVvYBwezKxRzAFlVcNcY)
    @torch.no_grad()
    def kzeIpaLNSGyUxNmgVakyIZAkNbjmCUjd(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS,
               S,
               batch_size,
               BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg,
               nKYmGWBrcYyADcANVAMJtCeHkjgKBdNR=None,
               FJsaFpOBdvpFlEdxOzBgjwcWBUfetQGF=None,
               jLCrVTmoUuFKVxGDtatnwzGzCExmBBAT=None,
               zohPmLukTxWcuUrUxAoYaBrbQiOHJrHz=None,
               UWBsOiqOWfnEhbtaqAOxSotxQUnEXBnc=False,
               YifKHCfIbeEsuQSFLLpJatOOrlBeQSoO=0.,
               KHpRlHOzblljQyskecSxzUuWZtneWwta=None,
               UBGvtPbFIPlcsBIwyWKuWMZeENGLMRAP=None,
               bPjNAKUJbfwLGNTyXOwhREwhMbkCGtZT=1.,
               TMglOjqaCnnmFnxLIYsGatkRARSSDlWE=0.,
               uwmipcScpDsNgboUJqvoJOCyptukbayF=None,
               svkqejXkhYfQwesKfbROwkTDdoaLEyDR=None,
               aFZoJwWpCnqyOJdcAMLlqOHxDgjPTNCS=True,
               AqKyQWxyGbtIRJDIpWPDLnPYOoinsvzD=None,
               LjKqtKRWUcXbjFAGJpBnRulwosodqMRC=100,
               dwjsCGpwSsxFQHnTouUTMnLobJXVZRBY=1.,
               yBqylnocrhyQcXxvCQFExhNCxzTGzMKi=None,
               qrcmQREjMkdBFKktuBhBkKwQXjUbXcKA=None,
               **kwargs
               ):
        if nKYmGWBrcYyADcANVAMJtCeHkjgKBdNR is not None:
            if isinstance(nKYmGWBrcYyADcANVAMJtCeHkjgKBdNR, dict):
                YqPlzmfdeRleEugDYgqhXdTzFrNzlJZs = nKYmGWBrcYyADcANVAMJtCeHkjgKBdNR[list(nKYmGWBrcYyADcANVAMJtCeHkjgKBdNR.keys())[0]].BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[0]
                if YqPlzmfdeRleEugDYgqhXdTzFrNzlJZs != batch_size:
                    print(f"Warning: Got {cbs} conditionings but batch-size is {batch_size}")
            else:
                if nKYmGWBrcYyADcANVAMJtCeHkjgKBdNR.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[0] != batch_size:
                    print(f"Warning: Got {conditioning.shape[0]} conditionings but batch-size is {batch_size}")
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.tsMUuSGvjHEShpizgUiHhBUvXzEpNCvO(ddim_num_steps=S, ddim_eta=YifKHCfIbeEsuQSFLLpJatOOrlBeQSoO, aFZoJwWpCnqyOJdcAMLlqOHxDgjPTNCS=aFZoJwWpCnqyOJdcAMLlqOHxDgjPTNCS)
        AHoGYMpsqEtOaZpAamJqoHqHvnlwZSRh, gFdyNTfDqQDeXijWZEnTSFKJXHMWaEiV, vFYBIMOEtqWwjvpBeeDFaIqTrgSbzULJ = BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg
        vqDBJgidQufnKyAltPYRqiKGjmztArDJ = (batch_size, AHoGYMpsqEtOaZpAamJqoHqHvnlwZSRh, gFdyNTfDqQDeXijWZEnTSFKJXHMWaEiV, vFYBIMOEtqWwjvpBeeDFaIqTrgSbzULJ)
        print(f'Data shape for PLMS sampling is {size}')
        bfpFhSQCEeSgZQwablzNZDcPruUlpnjs, YJbEpRPxEWHFEhbTXWwgTAKwhRHagUOK = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.UwqJjdrhfJFeEsSatsTpXYUHVlZDopix(nKYmGWBrcYyADcANVAMJtCeHkjgKBdNR, vqDBJgidQufnKyAltPYRqiKGjmztArDJ,
                                                    FJsaFpOBdvpFlEdxOzBgjwcWBUfetQGF=FJsaFpOBdvpFlEdxOzBgjwcWBUfetQGF,
                                                    zohPmLukTxWcuUrUxAoYaBrbQiOHJrHz=zohPmLukTxWcuUrUxAoYaBrbQiOHJrHz,
                                                    AQYujjqVWCTYeuoWJTDsAGdUIvWSqQDp=UWBsOiqOWfnEhbtaqAOxSotxQUnEXBnc,
                                                    KHpRlHOzblljQyskecSxzUuWZtneWwta=KHpRlHOzblljQyskecSxzUuWZtneWwta, UBGvtPbFIPlcsBIwyWKuWMZeENGLMRAP=UBGvtPbFIPlcsBIwyWKuWMZeENGLMRAP,
                                                    xkeDFKmtUIMseSAuFHuEApMrMWYQEuue=False,
                                                    TMglOjqaCnnmFnxLIYsGatkRARSSDlWE=TMglOjqaCnnmFnxLIYsGatkRARSSDlWE,
                                                    bPjNAKUJbfwLGNTyXOwhREwhMbkCGtZT=bPjNAKUJbfwLGNTyXOwhREwhMbkCGtZT,
                                                    uwmipcScpDsNgboUJqvoJOCyptukbayF=uwmipcScpDsNgboUJqvoJOCyptukbayF,
                                                    svkqejXkhYfQwesKfbROwkTDdoaLEyDR=svkqejXkhYfQwesKfbROwkTDdoaLEyDR,
                                                    AqKyQWxyGbtIRJDIpWPDLnPYOoinsvzD=AqKyQWxyGbtIRJDIpWPDLnPYOoinsvzD,
                                                    LjKqtKRWUcXbjFAGJpBnRulwosodqMRC=LjKqtKRWUcXbjFAGJpBnRulwosodqMRC,
                                                    dwjsCGpwSsxFQHnTouUTMnLobJXVZRBY=dwjsCGpwSsxFQHnTouUTMnLobJXVZRBY,
                                                    yBqylnocrhyQcXxvCQFExhNCxzTGzMKi=yBqylnocrhyQcXxvCQFExhNCxzTGzMKi,
                                                    qrcmQREjMkdBFKktuBhBkKwQXjUbXcKA=qrcmQREjMkdBFKktuBhBkKwQXjUbXcKA,
                                                    )
        return bfpFhSQCEeSgZQwablzNZDcPruUlpnjs, YJbEpRPxEWHFEhbTXWwgTAKwhRHagUOK
    @torch.no_grad()
    def UwqJjdrhfJFeEsSatsTpXYUHVlZDopix(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, BuoWBAnnMxyvqTGoSTHbQAlvPFWHbuUf, BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg,
                      AqKyQWxyGbtIRJDIpWPDLnPYOoinsvzD=None, xkeDFKmtUIMseSAuFHuEApMrMWYQEuue=False,
                      FJsaFpOBdvpFlEdxOzBgjwcWBUfetQGF=None, iaqNqpReXPEdYpNiyUIejEPLCqtbtedA=None, AQYujjqVWCTYeuoWJTDsAGdUIvWSqQDp=False,
                      KHpRlHOzblljQyskecSxzUuWZtneWwta=None, UBGvtPbFIPlcsBIwyWKuWMZeENGLMRAP=None, zohPmLukTxWcuUrUxAoYaBrbQiOHJrHz=None, LjKqtKRWUcXbjFAGJpBnRulwosodqMRC=100,
                      bPjNAKUJbfwLGNTyXOwhREwhMbkCGtZT=1., TMglOjqaCnnmFnxLIYsGatkRARSSDlWE=0., uwmipcScpDsNgboUJqvoJOCyptukbayF=None, svkqejXkhYfQwesKfbROwkTDdoaLEyDR=None,
                      dwjsCGpwSsxFQHnTouUTMnLobJXVZRBY=1., yBqylnocrhyQcXxvCQFExhNCxzTGzMKi=None,
                      qrcmQREjMkdBFKktuBhBkKwQXjUbXcKA=None):
        fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM.aGiatFWLVusbPGSDloFtejqscKjAwtLv.fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc
        b = BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[0]
        if AqKyQWxyGbtIRJDIpWPDLnPYOoinsvzD is None:
            UaFpXseNaoqfcpsDACQmTguYDZsTArhs = torch.randn(BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg, fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc=fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc)
        else:
            UaFpXseNaoqfcpsDACQmTguYDZsTArhs = AqKyQWxyGbtIRJDIpWPDLnPYOoinsvzD
        if iaqNqpReXPEdYpNiyUIejEPLCqtbtedA is None:
            iaqNqpReXPEdYpNiyUIejEPLCqtbtedA = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.ddpm_num_timesteps if xkeDFKmtUIMseSAuFHuEApMrMWYQEuue else rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.xaHdUhZcWVcLrTPEWFnTJjCgaiOMOyDm
        elif iaqNqpReXPEdYpNiyUIejEPLCqtbtedA is not None and not xkeDFKmtUIMseSAuFHuEApMrMWYQEuue:
            bvwJphRoDhZxLTgvwjqBZOVhaUawubVw = int(min(iaqNqpReXPEdYpNiyUIejEPLCqtbtedA / rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.xaHdUhZcWVcLrTPEWFnTJjCgaiOMOyDm.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[0], 1) * rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.xaHdUhZcWVcLrTPEWFnTJjCgaiOMOyDm.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[0]) - 1
            iaqNqpReXPEdYpNiyUIejEPLCqtbtedA = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.xaHdUhZcWVcLrTPEWFnTJjCgaiOMOyDm[:bvwJphRoDhZxLTgvwjqBZOVhaUawubVw]
        YJbEpRPxEWHFEhbTXWwgTAKwhRHagUOK = {'x_inter': [UaFpXseNaoqfcpsDACQmTguYDZsTArhs], 'pred_x0': [UaFpXseNaoqfcpsDACQmTguYDZsTArhs]}
        DlZgArthcSzgtzGqfHDDEnFCHSLHQWRM = list(reversed(range(0,iaqNqpReXPEdYpNiyUIejEPLCqtbtedA))) if xkeDFKmtUIMseSAuFHuEApMrMWYQEuue else np.hAHyMhlDympwYBnEsaNWPsolDQrxyovx(iaqNqpReXPEdYpNiyUIejEPLCqtbtedA)
        TuJjDqKZekSGicNtWVQgPuLDBIQsIxym = iaqNqpReXPEdYpNiyUIejEPLCqtbtedA if xkeDFKmtUIMseSAuFHuEApMrMWYQEuue else iaqNqpReXPEdYpNiyUIejEPLCqtbtedA.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[0]
        print(f"Running PLMS Sampling with {total_steps} timesteps")
        OphIfvlLGVjDrByPmOZajfCurTkgSmqc = tqdm(DlZgArthcSzgtzGqfHDDEnFCHSLHQWRM, desc='PLMS Sampler', total=TuJjDqKZekSGicNtWVQgPuLDBIQsIxym)
        jcXkudggCpllzGQRdXyAuJAqouTGbyMR = []
        for HCXmerBqIMuTscBONzTGKYapYSxWTYHo, UHmIQCHeLkozPfaktIdEHKdpTVYzCLhe in enumerate(OphIfvlLGVjDrByPmOZajfCurTkgSmqc):
            index = TuJjDqKZekSGicNtWVQgPuLDBIQsIxym - HCXmerBqIMuTscBONzTGKYapYSxWTYHo - 1
            cZfLNeHGLvPreutnrDmWGGyKvtymQVKM = torch.full((b,), UHmIQCHeLkozPfaktIdEHKdpTVYzCLhe, fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc=fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc, DDRQlhrNSGpwTrokWitkZipdfbAqBFxv=torch.long)
            kBKfmOKTIvPkfBwmRKllvqMttixsVwwd = torch.full((b,), DlZgArthcSzgtzGqfHDDEnFCHSLHQWRM[min(HCXmerBqIMuTscBONzTGKYapYSxWTYHo + 1, len(DlZgArthcSzgtzGqfHDDEnFCHSLHQWRM) - 1)], fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc=fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc, DDRQlhrNSGpwTrokWitkZipdfbAqBFxv=torch.long)
            if KHpRlHOzblljQyskecSxzUuWZtneWwta is not None:
                assert UBGvtPbFIPlcsBIwyWKuWMZeENGLMRAP is not None
                aUSKPLohyDNFRJMczvWLPVVguMICMoGt = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM.twrldmxqPsdvMdtmZuRtTLKgxMGCJtCm(UBGvtPbFIPlcsBIwyWKuWMZeENGLMRAP, cZfLNeHGLvPreutnrDmWGGyKvtymQVKM)  
                UaFpXseNaoqfcpsDACQmTguYDZsTArhs = aUSKPLohyDNFRJMczvWLPVVguMICMoGt * KHpRlHOzblljQyskecSxzUuWZtneWwta + (1. - KHpRlHOzblljQyskecSxzUuWZtneWwta) * UaFpXseNaoqfcpsDACQmTguYDZsTArhs
            iaKZglbdZWiaDGkgnGdwdPDQlLdcYnMW = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.oFmbrJpwtBIIGhmJLNOtnqLwDFBWBmHn(UaFpXseNaoqfcpsDACQmTguYDZsTArhs, BuoWBAnnMxyvqTGoSTHbQAlvPFWHbuUf, cZfLNeHGLvPreutnrDmWGGyKvtymQVKM, index=index, KtYiLLkMttRIVWgJPwYdrzrduvlLpeov=xkeDFKmtUIMseSAuFHuEApMrMWYQEuue,
                                      AQYujjqVWCTYeuoWJTDsAGdUIvWSqQDp=AQYujjqVWCTYeuoWJTDsAGdUIvWSqQDp, bPjNAKUJbfwLGNTyXOwhREwhMbkCGtZT=bPjNAKUJbfwLGNTyXOwhREwhMbkCGtZT,
                                      TMglOjqaCnnmFnxLIYsGatkRARSSDlWE=TMglOjqaCnnmFnxLIYsGatkRARSSDlWE, uwmipcScpDsNgboUJqvoJOCyptukbayF=uwmipcScpDsNgboUJqvoJOCyptukbayF,
                                      svkqejXkhYfQwesKfbROwkTDdoaLEyDR=svkqejXkhYfQwesKfbROwkTDdoaLEyDR,
                                      dwjsCGpwSsxFQHnTouUTMnLobJXVZRBY=dwjsCGpwSsxFQHnTouUTMnLobJXVZRBY,
                                      yBqylnocrhyQcXxvCQFExhNCxzTGzMKi=yBqylnocrhyQcXxvCQFExhNCxzTGzMKi,
                                      jcXkudggCpllzGQRdXyAuJAqouTGbyMR=jcXkudggCpllzGQRdXyAuJAqouTGbyMR, FeAWRnaTBNovNhgenUWGiCkgCADxZPHQ=kBKfmOKTIvPkfBwmRKllvqMttixsVwwd,
                                      qrcmQREjMkdBFKktuBhBkKwQXjUbXcKA=qrcmQREjMkdBFKktuBhBkKwQXjUbXcKA)
            UaFpXseNaoqfcpsDACQmTguYDZsTArhs, OFZIJlADjsdMdYLlZlOCATiBMXflBfif, uBmQzRLOVgunSnlFcnqpUgJOxetSTMeK = iaKZglbdZWiaDGkgnGdwdPDQlLdcYnMW
            jcXkudggCpllzGQRdXyAuJAqouTGbyMR.append(uBmQzRLOVgunSnlFcnqpUgJOxetSTMeK)
            if len(jcXkudggCpllzGQRdXyAuJAqouTGbyMR) >= 4:
                jcXkudggCpllzGQRdXyAuJAqouTGbyMR.pop(0)
            if FJsaFpOBdvpFlEdxOzBgjwcWBUfetQGF: FJsaFpOBdvpFlEdxOzBgjwcWBUfetQGF(HCXmerBqIMuTscBONzTGKYapYSxWTYHo)
            if zohPmLukTxWcuUrUxAoYaBrbQiOHJrHz: zohPmLukTxWcuUrUxAoYaBrbQiOHJrHz(OFZIJlADjsdMdYLlZlOCATiBMXflBfif, HCXmerBqIMuTscBONzTGKYapYSxWTYHo)
            if index % LjKqtKRWUcXbjFAGJpBnRulwosodqMRC == 0 or index == TuJjDqKZekSGicNtWVQgPuLDBIQsIxym - 1:
                YJbEpRPxEWHFEhbTXWwgTAKwhRHagUOK['x_inter'].append(UaFpXseNaoqfcpsDACQmTguYDZsTArhs)
                YJbEpRPxEWHFEhbTXWwgTAKwhRHagUOK['pred_x0'].append(OFZIJlADjsdMdYLlZlOCATiBMXflBfif)
        return UaFpXseNaoqfcpsDACQmTguYDZsTArhs, YJbEpRPxEWHFEhbTXWwgTAKwhRHagUOK
    @torch.no_grad()
    def oFmbrJpwtBIIGhmJLNOtnqLwDFBWBmHn(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, NECAaWUrFGIXcLimrerEYmxYIykQBfXb, cjHIelcAqVoHWdLcgzuZiBumKNTVADsY, XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz, index, ILPiaoThrLFONsZievnjpKpnQSXeiZbN=False, KtYiLLkMttRIVWgJPwYdrzrduvlLpeov=False, AQYujjqVWCTYeuoWJTDsAGdUIvWSqQDp=False,
                      bPjNAKUJbfwLGNTyXOwhREwhMbkCGtZT=1., TMglOjqaCnnmFnxLIYsGatkRARSSDlWE=0., uwmipcScpDsNgboUJqvoJOCyptukbayF=None, svkqejXkhYfQwesKfbROwkTDdoaLEyDR=None,
                      dwjsCGpwSsxFQHnTouUTMnLobJXVZRBY=1., yBqylnocrhyQcXxvCQFExhNCxzTGzMKi=None, jcXkudggCpllzGQRdXyAuJAqouTGbyMR=None, FeAWRnaTBNovNhgenUWGiCkgCADxZPHQ=None,
                      qrcmQREjMkdBFKktuBhBkKwQXjUbXcKA=None):
        b, *_, fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc = *NECAaWUrFGIXcLimrerEYmxYIykQBfXb.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg, NECAaWUrFGIXcLimrerEYmxYIykQBfXb.fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc
        def RxZQIvZQCuhcUVOnwULaetzqRlFIlYud(NECAaWUrFGIXcLimrerEYmxYIykQBfXb, XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz):
            if yBqylnocrhyQcXxvCQFExhNCxzTGzMKi is None or dwjsCGpwSsxFQHnTouUTMnLobJXVZRBY == 1.:
                uBmQzRLOVgunSnlFcnqpUgJOxetSTMeK = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM.MuUKKVVLhPOQUuXCLkPqFOcgOkyciNHd(NECAaWUrFGIXcLimrerEYmxYIykQBfXb, XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz, cjHIelcAqVoHWdLcgzuZiBumKNTVADsY)
            else:
                pZoNxoVtAYgcFKlLqYosAEKjqMzwRmNs = torch.cat([NECAaWUrFGIXcLimrerEYmxYIykQBfXb] * 2)
                xTGvTRTnrzNeWShiGfMbhVhxqQzWXDWU = torch.cat([XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz] * 2)
                dfJKHENBxSWlCdWWoJqBdANPeXpCQuEv = torch.cat([yBqylnocrhyQcXxvCQFExhNCxzTGzMKi, cjHIelcAqVoHWdLcgzuZiBumKNTVADsY])
                eQxLGgMGfzbpdqlJoqsWEzwuUbagcVaD, uBmQzRLOVgunSnlFcnqpUgJOxetSTMeK = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM.MuUKKVVLhPOQUuXCLkPqFOcgOkyciNHd(pZoNxoVtAYgcFKlLqYosAEKjqMzwRmNs, xTGvTRTnrzNeWShiGfMbhVhxqQzWXDWU, dfJKHENBxSWlCdWWoJqBdANPeXpCQuEv).ebMwMGDmpDsmyMtCQfGxUhZuVHvTpavF(2)
                uBmQzRLOVgunSnlFcnqpUgJOxetSTMeK = eQxLGgMGfzbpdqlJoqsWEzwuUbagcVaD + dwjsCGpwSsxFQHnTouUTMnLobJXVZRBY * (uBmQzRLOVgunSnlFcnqpUgJOxetSTMeK - eQxLGgMGfzbpdqlJoqsWEzwuUbagcVaD)
            if uwmipcScpDsNgboUJqvoJOCyptukbayF is not None:
                assert rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM.parameterization == "eps"
                uBmQzRLOVgunSnlFcnqpUgJOxetSTMeK = uwmipcScpDsNgboUJqvoJOCyptukbayF.modify_score(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM, uBmQzRLOVgunSnlFcnqpUgJOxetSTMeK, NECAaWUrFGIXcLimrerEYmxYIykQBfXb, XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz, cjHIelcAqVoHWdLcgzuZiBumKNTVADsY, **svkqejXkhYfQwesKfbROwkTDdoaLEyDR)
            return uBmQzRLOVgunSnlFcnqpUgJOxetSTMeK
        QgAevolFCLuucRhHfnVzUiISHrgGQRYP = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM.IOpmYnAWyhIWgvrJQuznNWQMTUXYwThN if KtYiLLkMttRIVWgJPwYdrzrduvlLpeov else rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.QjiFjIOgEuLEafnVNKmbYgjRnHbwNhfp
        PgrClhecyuZcmtDWgocBUxaRljPilBZn = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM.xbuEtLNyZNkLwkSOeiFKOKlofYAdfmXP if KtYiLLkMttRIVWgJPwYdrzrduvlLpeov else rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.DaGHMszTvPtphdOZZoBVaYSOdJOBoPWO
        IFcVijiEzGFYdGRIVpuvuNqNwnXpwfVP = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM.ayIzJzknKslZlpJwTeDgXUXhvxStZQpi if KtYiLLkMttRIVWgJPwYdrzrduvlLpeov else rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.ddim_sqrt_one_minus_alphas
        ywkdEDhpSPXHYARENdFhpYnCzsLhiORy = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM.ddim_sigmas_for_original_num_steps if KtYiLLkMttRIVWgJPwYdrzrduvlLpeov else rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.UhwxvNJOIOpYuDYuLFnCTFkDJmQARxHP
        def IOBGhOCYvwZralsaSatWEUBezXfgaWVF(uBmQzRLOVgunSnlFcnqpUgJOxetSTMeK, index):
            zSEsdYsYRoQzRYuMFNBptmaevaZkAzIb = torch.full((b, 1, 1, 1), QgAevolFCLuucRhHfnVzUiISHrgGQRYP[index], fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc=fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc)
            jUZIwXKcGkMkgbozsGgRVWpoQpuLRXeX = torch.full((b, 1, 1, 1), PgrClhecyuZcmtDWgocBUxaRljPilBZn[index], fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc=fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc)
            zhpCBYkwQkhgdrClReoQrMdATdSZEHOs = torch.full((b, 1, 1, 1), ywkdEDhpSPXHYARENdFhpYnCzsLhiORy[index], fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc=fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc)
            xHUMMKzIYwKrFkonVrNjpjgiLwOrNOGM = torch.full((b, 1, 1, 1), IFcVijiEzGFYdGRIVpuvuNqNwnXpwfVP[index],fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc=fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc)
            OFZIJlADjsdMdYLlZlOCATiBMXflBfif = (NECAaWUrFGIXcLimrerEYmxYIykQBfXb - xHUMMKzIYwKrFkonVrNjpjgiLwOrNOGM * uBmQzRLOVgunSnlFcnqpUgJOxetSTMeK) / zSEsdYsYRoQzRYuMFNBptmaevaZkAzIb.sqrt()
            if AQYujjqVWCTYeuoWJTDsAGdUIvWSqQDp:
                OFZIJlADjsdMdYLlZlOCATiBMXflBfif, _, *_ = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM.first_stage_model.igozXCsnhgCZQmnoJMlyfcgGnTBaMSfs(OFZIJlADjsdMdYLlZlOCATiBMXflBfif)
            if qrcmQREjMkdBFKktuBhBkKwQXjUbXcKA is not None:
                OFZIJlADjsdMdYLlZlOCATiBMXflBfif = FuFPjwbSOSOGsduutWbGgxcLyqowDcLE(OFZIJlADjsdMdYLlZlOCATiBMXflBfif, qrcmQREjMkdBFKktuBhBkKwQXjUbXcKA)
            XxaPiEaRsRiuOHxoRmexVbbHxaCFDzBa = (1. - jUZIwXKcGkMkgbozsGgRVWpoQpuLRXeX - zhpCBYkwQkhgdrClReoQrMdATdSZEHOs**2).sqrt() * uBmQzRLOVgunSnlFcnqpUgJOxetSTMeK
            jCizDlbKxNNChDZcMjnDhRYUQUZdrTRD = zhpCBYkwQkhgdrClReoQrMdATdSZEHOs * LrAizKrQgKBxXFjYQZHueeWsViuvAXJp(NECAaWUrFGIXcLimrerEYmxYIykQBfXb.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg, fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc, ILPiaoThrLFONsZievnjpKpnQSXeiZbN) * bPjNAKUJbfwLGNTyXOwhREwhMbkCGtZT
            if TMglOjqaCnnmFnxLIYsGatkRARSSDlWE > 0.:
                jCizDlbKxNNChDZcMjnDhRYUQUZdrTRD = torch.nn.functional.kcIxGCXrUvsLPSfmGoULGFzAthVmTXcA(jCizDlbKxNNChDZcMjnDhRYUQUZdrTRD, HutkrxeXIuRQKOhCWHkiwqLGAsJjUSKj=TMglOjqaCnnmFnxLIYsGatkRARSSDlWE)
            sIfmGCKFYSuAcKGivnHeSsHXHFOsVWBD = jUZIwXKcGkMkgbozsGgRVWpoQpuLRXeX.sqrt() * OFZIJlADjsdMdYLlZlOCATiBMXflBfif + XxaPiEaRsRiuOHxoRmexVbbHxaCFDzBa + jCizDlbKxNNChDZcMjnDhRYUQUZdrTRD
            return sIfmGCKFYSuAcKGivnHeSsHXHFOsVWBD, OFZIJlADjsdMdYLlZlOCATiBMXflBfif
        uBmQzRLOVgunSnlFcnqpUgJOxetSTMeK = RxZQIvZQCuhcUVOnwULaetzqRlFIlYud(NECAaWUrFGIXcLimrerEYmxYIykQBfXb, XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz)
        if len(jcXkudggCpllzGQRdXyAuJAqouTGbyMR) == 0:
            sIfmGCKFYSuAcKGivnHeSsHXHFOsVWBD, OFZIJlADjsdMdYLlZlOCATiBMXflBfif = IOBGhOCYvwZralsaSatWEUBezXfgaWVF(uBmQzRLOVgunSnlFcnqpUgJOxetSTMeK, index)
            LcbRhjSwKaoVkggQarScKpRRkfEMDJCY = RxZQIvZQCuhcUVOnwULaetzqRlFIlYud(sIfmGCKFYSuAcKGivnHeSsHXHFOsVWBD, FeAWRnaTBNovNhgenUWGiCkgCADxZPHQ)
            VzdwXkAjybhJxfbNlQuaVieCHCYjxjSK = (uBmQzRLOVgunSnlFcnqpUgJOxetSTMeK + LcbRhjSwKaoVkggQarScKpRRkfEMDJCY) / 2
        elif len(jcXkudggCpllzGQRdXyAuJAqouTGbyMR) == 1:
            VzdwXkAjybhJxfbNlQuaVieCHCYjxjSK = (3 * uBmQzRLOVgunSnlFcnqpUgJOxetSTMeK - jcXkudggCpllzGQRdXyAuJAqouTGbyMR[-1]) / 2
        elif len(jcXkudggCpllzGQRdXyAuJAqouTGbyMR) == 2:
            VzdwXkAjybhJxfbNlQuaVieCHCYjxjSK = (23 * uBmQzRLOVgunSnlFcnqpUgJOxetSTMeK - 16 * jcXkudggCpllzGQRdXyAuJAqouTGbyMR[-1] + 5 * jcXkudggCpllzGQRdXyAuJAqouTGbyMR[-2]) / 12
        elif len(jcXkudggCpllzGQRdXyAuJAqouTGbyMR) >= 3:
            VzdwXkAjybhJxfbNlQuaVieCHCYjxjSK = (55 * uBmQzRLOVgunSnlFcnqpUgJOxetSTMeK - 59 * jcXkudggCpllzGQRdXyAuJAqouTGbyMR[-1] + 37 * jcXkudggCpllzGQRdXyAuJAqouTGbyMR[-2] - 9 * jcXkudggCpllzGQRdXyAuJAqouTGbyMR[-3]) / 24
        sIfmGCKFYSuAcKGivnHeSsHXHFOsVWBD, OFZIJlADjsdMdYLlZlOCATiBMXflBfif = IOBGhOCYvwZralsaSatWEUBezXfgaWVF(VzdwXkAjybhJxfbNlQuaVieCHCYjxjSK, index)
        return sIfmGCKFYSuAcKGivnHeSsHXHFOsVWBD, OFZIJlADjsdMdYLlZlOCATiBMXflBfif, uBmQzRLOVgunSnlFcnqpUgJOxetSTMeK
