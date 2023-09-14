import torch
from quasar.ldm.modules.diffusionmodules.openaimodel import ECDCaNzfsUCStonxUHNJYFmsGbuTLSRS
from quasar.ldm.modules.encoders.noise_aug_modules import NgrOydhziQoGvGMNEZwABugeswryRyaC
from quasar.ldm.modules.diffusionmodules.util import zaisjRTCkjpiDfZeBMSaxmKWIiSAGqnS
from quasar.ldm.modules.diffusionmodules.openaimodel import zGGBuzFwarRcjrVdvKsXbQZONUVfKAiA
import quasar.model_management
import numpy as np
from enum import Enum
from . import utils
class DwnytdzUnaxYSvjidBVNMySSZNKfKUln(Enum):
    kAXyAlkwERgiSykVggDfAbBFSPRWsPbJ = 1
    IfSpexRRCKcIegeOUYKebxpBmBzRLaRR = 2
class FysyHDAhzveVQGJRNBJHfHxZedLYKfhV(torch.nn.Module):
    def __init__(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, QndHjlfwhEimYkuHnNTDxkEXYaCwJdZe, SZAVLBSfrTycZhmQUtWaVvoZUmpPNFnx=DwnytdzUnaxYSvjidBVNMySSZNKfKUln.kAXyAlkwERgiSykVggDfAbBFSPRWsPbJ, fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc=None):
        super().__init__()
        lLgbOYEeDmYyyxASAROATrPmlqgqYORG = QndHjlfwhEimYkuHnNTDxkEXYaCwJdZe.lLgbOYEeDmYyyxASAROATrPmlqgqYORG
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.latent_format = QndHjlfwhEimYkuHnNTDxkEXYaCwJdZe.latent_format
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.QndHjlfwhEimYkuHnNTDxkEXYaCwJdZe = QndHjlfwhEimYkuHnNTDxkEXYaCwJdZe
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.OnzWlzKaxvcGRiDToHScHroOvomgpvlX(given_betas=None, beta_schedule=QndHjlfwhEimYkuHnNTDxkEXYaCwJdZe.beta_schedule, iaqNqpReXPEdYpNiyUIejEPLCqtbtedA=1000, uxpvmlqmOaPaMVrpHrWCryZCjOHCVbkJ=0.00085, linear_end=0.012, zPdwEaBmJLoyWlLEECXftyIOeNavvXbe=8e-3)
        if not lLgbOYEeDmYyyxASAROATrPmlqgqYORG.get("disable_unet_model_creation", False):
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.iVdKrUYRzQdKeaSQTeCVqHvUmmINpkSC = ECDCaNzfsUCStonxUHNJYFmsGbuTLSRS(**lLgbOYEeDmYyyxASAROATrPmlqgqYORG, fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc=fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.SZAVLBSfrTycZhmQUtWaVvoZUmpPNFnx = SZAVLBSfrTycZhmQUtWaVvoZUmpPNFnx
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.adm_channels = lLgbOYEeDmYyyxASAROATrPmlqgqYORG.get("adm_in_channels", None)
        if rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.adm_channels is None:
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.adm_channels = 0
        print("model_type", SZAVLBSfrTycZhmQUtWaVvoZUmpPNFnx.name)
        print("adm", rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.adm_channels)
    def OnzWlzKaxvcGRiDToHScHroOvomgpvlX(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, given_betas=None, beta_schedule="linear", iaqNqpReXPEdYpNiyUIejEPLCqtbtedA=1000,
                          uxpvmlqmOaPaMVrpHrWCryZCjOHCVbkJ=1e-4, linear_end=2e-2, zPdwEaBmJLoyWlLEECXftyIOeNavvXbe=8e-3):
        if given_betas is not None:
            aGiatFWLVusbPGSDloFtejqscKjAwtLv = given_betas
        else:
            aGiatFWLVusbPGSDloFtejqscKjAwtLv = zaisjRTCkjpiDfZeBMSaxmKWIiSAGqnS(beta_schedule, iaqNqpReXPEdYpNiyUIejEPLCqtbtedA, uxpvmlqmOaPaMVrpHrWCryZCjOHCVbkJ=uxpvmlqmOaPaMVrpHrWCryZCjOHCVbkJ, linear_end=linear_end, zPdwEaBmJLoyWlLEECXftyIOeNavvXbe=zPdwEaBmJLoyWlLEECXftyIOeNavvXbe)
        QgAevolFCLuucRhHfnVzUiISHrgGQRYP = 1. - aGiatFWLVusbPGSDloFtejqscKjAwtLv
        IOpmYnAWyhIWgvrJQuznNWQMTUXYwThN = np.cumprod(QgAevolFCLuucRhHfnVzUiISHrgGQRYP, axis=0)
        xbuEtLNyZNkLwkSOeiFKOKlofYAdfmXP = np.append(1., IOpmYnAWyhIWgvrJQuznNWQMTUXYwThN[:-1])
        iaqNqpReXPEdYpNiyUIejEPLCqtbtedA, = aGiatFWLVusbPGSDloFtejqscKjAwtLv.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.num_timesteps = int(iaqNqpReXPEdYpNiyUIejEPLCqtbtedA)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.uxpvmlqmOaPaMVrpHrWCryZCjOHCVbkJ = uxpvmlqmOaPaMVrpHrWCryZCjOHCVbkJ
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.linear_end = linear_end
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.BpOtVuSttURsCNYELWmrxpBkqOPYBBlj('betas', torch.xPmCFphFKpGMpIsczaSKHmMgRPZzJwla(aGiatFWLVusbPGSDloFtejqscKjAwtLv, DDRQlhrNSGpwTrokWitkZipdfbAqBFxv=torch.float32))
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.BpOtVuSttURsCNYELWmrxpBkqOPYBBlj('alphas_cumprod', torch.xPmCFphFKpGMpIsczaSKHmMgRPZzJwla(IOpmYnAWyhIWgvrJQuznNWQMTUXYwThN, DDRQlhrNSGpwTrokWitkZipdfbAqBFxv=torch.float32))
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.BpOtVuSttURsCNYELWmrxpBkqOPYBBlj('alphas_cumprod_prev', torch.xPmCFphFKpGMpIsczaSKHmMgRPZzJwla(xbuEtLNyZNkLwkSOeiFKOKlofYAdfmXP, DDRQlhrNSGpwTrokWitkZipdfbAqBFxv=torch.float32))
    def MuUKKVVLhPOQUuXCLkPqFOcgOkyciNHd(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, NECAaWUrFGIXcLimrerEYmxYIykQBfXb, XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz, NxPzLGoygEGpTpJOvmrPwoSPnCtjjNUI=None, IAcIseSrcOgfiCQlLtmRUgpgfxAzxiKm=None, RFYqqRKKmjXUBaAsdvUNUVYmwpdtlLAs=None, lxwsNGReZsRzPAGinnJJBaOYnaZlIssl=None, transformer_options={}):
        if NxPzLGoygEGpTpJOvmrPwoSPnCtjjNUI is not None:
            RFDsQwESUjeJfiPgSSVsMLLYlHaZhFoO = torch.cat([NECAaWUrFGIXcLimrerEYmxYIykQBfXb] + [NxPzLGoygEGpTpJOvmrPwoSPnCtjjNUI], yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk=1)
        else:
            RFDsQwESUjeJfiPgSSVsMLLYlHaZhFoO = NECAaWUrFGIXcLimrerEYmxYIykQBfXb
        tRdCjhUPYVVxnSEkGmJIHWRitDXRXSZS = IAcIseSrcOgfiCQlLtmRUgpgfxAzxiKm
        DDRQlhrNSGpwTrokWitkZipdfbAqBFxv = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.qCYGtbmEmpKHSGaChkRoXdcCONojeSqh()
        RFDsQwESUjeJfiPgSSVsMLLYlHaZhFoO = RFDsQwESUjeJfiPgSSVsMLLYlHaZhFoO.sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ(DDRQlhrNSGpwTrokWitkZipdfbAqBFxv)
        XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz = XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz.sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ(DDRQlhrNSGpwTrokWitkZipdfbAqBFxv)
        tRdCjhUPYVVxnSEkGmJIHWRitDXRXSZS = tRdCjhUPYVVxnSEkGmJIHWRitDXRXSZS.sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ(DDRQlhrNSGpwTrokWitkZipdfbAqBFxv)
        if RFYqqRKKmjXUBaAsdvUNUVYmwpdtlLAs is not None:
            RFYqqRKKmjXUBaAsdvUNUVYmwpdtlLAs = RFYqqRKKmjXUBaAsdvUNUVYmwpdtlLAs.sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ(DDRQlhrNSGpwTrokWitkZipdfbAqBFxv)
        return rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.iVdKrUYRzQdKeaSQTeCVqHvUmmINpkSC(RFDsQwESUjeJfiPgSSVsMLLYlHaZhFoO, XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz, tRdCjhUPYVVxnSEkGmJIHWRitDXRXSZS=tRdCjhUPYVVxnSEkGmJIHWRitDXRXSZS, ZljqvWVaiqYAYdTFzQHSTXFDKwgstKaW=RFYqqRKKmjXUBaAsdvUNUVYmwpdtlLAs, lxwsNGReZsRzPAGinnJJBaOYnaZlIssl=lxwsNGReZsRzPAGinnJJBaOYnaZlIssl, transformer_options=transformer_options).float()
    def qCYGtbmEmpKHSGaChkRoXdcCONojeSqh(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS):
        return rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.iVdKrUYRzQdKeaSQTeCVqHvUmmINpkSC.DDRQlhrNSGpwTrokWitkZipdfbAqBFxv
    def wUvyCicKdvaazYCIRWNYqgfcZriaCvpW(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS):
        return rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.adm_channels > 0
    def iadrkNoUAKhvRZERXmJdkECHhlSflify(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, **kwargs):
        return None
    def GUNVLCHKRhIXqmOuPUqHjLzZAStPIRju(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, ylGhUFMpxPbtUUTfCZpemVkdanRhWmHa, unet_prefix=""):
        nOrtXSpMTcWOSkkcnhMSnuMMVQqbTRkc = {}
        keys = list(ylGhUFMpxPbtUUTfCZpemVkdanRhWmHa.keys())
        for EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm in keys:
            if EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm.startswith(unet_prefix):
                nOrtXSpMTcWOSkkcnhMSnuMMVQqbTRkc[EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm[len(unet_prefix):]] = ylGhUFMpxPbtUUTfCZpemVkdanRhWmHa.pop(EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm)
        FTosLGldclAzaiNbwuLMIEtXfrZQpTnU, u = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.iVdKrUYRzQdKeaSQTeCVqHvUmmINpkSC.OVlRwgmJvqggImaZMfxKZfQnVYfyhIsc(nOrtXSpMTcWOSkkcnhMSnuMMVQqbTRkc, strict=False)
        if len(FTosLGldclAzaiNbwuLMIEtXfrZQpTnU) > 0:
            print("unet missing:", FTosLGldclAzaiNbwuLMIEtXfrZQpTnU)
        if len(u) > 0:
            print("unet unexpected:", u)
        del nOrtXSpMTcWOSkkcnhMSnuMMVQqbTRkc
        return rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS
    def KhoxXknIobbVmYvZfpegxkSMbvsNHutJ(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, CBTHgqHIDKYRBmSTkKCsLapKGpsubmaU):
        return rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.latent_format.BOKxozlShczbzCevlTVDFuqIkiCiUaSa(CBTHgqHIDKYRBmSTkKCsLapKGpsubmaU)
    def dcmEEQRpXTSuEBJYzQkVJZjzPldwdzjo(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, CBTHgqHIDKYRBmSTkKCsLapKGpsubmaU):
        return rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.latent_format.wYPnepxibBpmaPAYZvgmTZSwUlzzhsSA(CBTHgqHIDKYRBmSTkKCsLapKGpsubmaU)
    def DdcaagrgpPGSYtkvmjUBoZZcPdQftSdt(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, FnZbFCkHuRexyskhUCReCSwUnaALeeGy, QLykPMMghQkBzNKJlfgFZKhZZUmaNrQv):
        FnZbFCkHuRexyskhUCReCSwUnaALeeGy = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.QndHjlfwhEimYkuHnNTDxkEXYaCwJdZe.process_clip_state_dict_for_saving(FnZbFCkHuRexyskhUCReCSwUnaALeeGy)
        IokSFeQRZIOmjSPlODZSOYaXzRibrXHZ = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.iVdKrUYRzQdKeaSQTeCVqHvUmmINpkSC.TQRgUMPjEwYAaDvSuzgvheADStCoUKzT()
        gXYsYkJbPWMeavbmLkVsXBfRMdjBmWrT = {}
        for EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm in IokSFeQRZIOmjSPlODZSOYaXzRibrXHZ:
            gXYsYkJbPWMeavbmLkVsXBfRMdjBmWrT[EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm] = quasar.model_management.fJSttSHgRmTiJkiWezuwVxBkdvWTIAvw(IokSFeQRZIOmjSPlODZSOYaXzRibrXHZ[EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm], rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.iVdKrUYRzQdKeaSQTeCVqHvUmmINpkSC, EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm)
        gXYsYkJbPWMeavbmLkVsXBfRMdjBmWrT = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.QndHjlfwhEimYkuHnNTDxkEXYaCwJdZe.process_unet_state_dict_for_saving(gXYsYkJbPWMeavbmLkVsXBfRMdjBmWrT)
        QLykPMMghQkBzNKJlfgFZKhZZUmaNrQv = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.QndHjlfwhEimYkuHnNTDxkEXYaCwJdZe.process_vae_state_dict_for_saving(QLykPMMghQkBzNKJlfgFZKhZZUmaNrQv)
        if rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.qCYGtbmEmpKHSGaChkRoXdcCONojeSqh() == torch.float16:
            FnZbFCkHuRexyskhUCReCSwUnaALeeGy = utils.convert_sd_to(FnZbFCkHuRexyskhUCReCSwUnaALeeGy, torch.float16)
            QLykPMMghQkBzNKJlfgFZKhZZUmaNrQv = utils.convert_sd_to(QLykPMMghQkBzNKJlfgFZKhZZUmaNrQv, torch.float16)
        if rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.SZAVLBSfrTycZhmQUtWaVvoZUmpPNFnx == DwnytdzUnaxYSvjidBVNMySSZNKfKUln.IfSpexRRCKcIegeOUYKebxpBmBzRLaRR:
            gXYsYkJbPWMeavbmLkVsXBfRMdjBmWrT["v_pred"] = torch.xPmCFphFKpGMpIsczaSKHmMgRPZzJwla([])
        return {**gXYsYkJbPWMeavbmLkVsXBfRMdjBmWrT, **QLykPMMghQkBzNKJlfgFZKhZZUmaNrQv, **FnZbFCkHuRexyskhUCReCSwUnaALeeGy}
    def GPYZjPIdclSwgLaKrXWreKklFJhGERaI(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS):
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.concat_keys = ("mask", "masked_image")
def YGCBPyMASawsnGcFuVwXihSDBCdMBjHG(ZzfVwnmJdpNHBYfiTQQyOPhQeKDLCUve, fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc, noise_augmentor, noise_augment_merge=0.0):
    rfiKAdiqRQeTirTUKMkGSoSgxQgENUKe = []
    wFSdIFoZKBPqDyrRSUXxPVfhYIDtPHnL = []
    VFhTjsmzeHEdSrUsxaFAmkaDsSUlsECW = []
    for FowYOdoKCdRGlgpDFdjCFhiKMWgxTQew in ZzfVwnmJdpNHBYfiTQQyOPhQeKDLCUve:
        for YgSctTRyhrOwtcmPdBylexnnttVabPJd in FowYOdoKCdRGlgpDFdjCFhiKMWgxTQew["clip_vision_output"].image_embeds:
            RXBOtvKSHQkBvdKDbckmnlphvVygYURP = FowYOdoKCdRGlgpDFdjCFhiKMWgxTQew["strength"]
            AcBfVgQzdpMehXemtMscysvFoJToBnFw = FowYOdoKCdRGlgpDFdjCFhiKMWgxTQew["noise_augmentation"]
            ihxtcBCJYsyuUxoavxlsNSboBlsKZXwh = round((noise_augmentor.max_noise_level - 1) * AcBfVgQzdpMehXemtMscysvFoJToBnFw)
            RFYqqRKKmjXUBaAsdvUNUVYmwpdtlLAs, DdOKIUfxJrXFIHAKuVLUlmUgnrQkZRli = noise_augmentor(YgSctTRyhrOwtcmPdBylexnnttVabPJd.sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ(fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc), ihxtcBCJYsyuUxoavxlsNSboBlsKZXwh=torch.xPmCFphFKpGMpIsczaSKHmMgRPZzJwla([ihxtcBCJYsyuUxoavxlsNSboBlsKZXwh], fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc=fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc))
            zRgvHDpLPapjNJFYZGjIsEFUGSeSLqvB = torch.cat((RFYqqRKKmjXUBaAsdvUNUVYmwpdtlLAs, DdOKIUfxJrXFIHAKuVLUlmUgnrQkZRli), 1) * RXBOtvKSHQkBvdKDbckmnlphvVygYURP
            wFSdIFoZKBPqDyrRSUXxPVfhYIDtPHnL.append(RXBOtvKSHQkBvdKDbckmnlphvVygYURP)
            VFhTjsmzeHEdSrUsxaFAmkaDsSUlsECW.append(AcBfVgQzdpMehXemtMscysvFoJToBnFw)
            rfiKAdiqRQeTirTUKMkGSoSgxQgENUKe.append(zRgvHDpLPapjNJFYZGjIsEFUGSeSLqvB)
    if len(VFhTjsmzeHEdSrUsxaFAmkaDsSUlsECW) > 1:
        zRgvHDpLPapjNJFYZGjIsEFUGSeSLqvB = torch.stack(rfiKAdiqRQeTirTUKMkGSoSgxQgENUKe).sum(0)
        AcBfVgQzdpMehXemtMscysvFoJToBnFw = noise_augment_merge
        ihxtcBCJYsyuUxoavxlsNSboBlsKZXwh = round((noise_augmentor.max_noise_level - 1) * AcBfVgQzdpMehXemtMscysvFoJToBnFw)
        RFYqqRKKmjXUBaAsdvUNUVYmwpdtlLAs, DdOKIUfxJrXFIHAKuVLUlmUgnrQkZRli = noise_augmentor(zRgvHDpLPapjNJFYZGjIsEFUGSeSLqvB[:, :noise_augmentor.time_embed.yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk], ihxtcBCJYsyuUxoavxlsNSboBlsKZXwh=torch.xPmCFphFKpGMpIsczaSKHmMgRPZzJwla([ihxtcBCJYsyuUxoavxlsNSboBlsKZXwh], fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc=fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc))
        zRgvHDpLPapjNJFYZGjIsEFUGSeSLqvB = torch.cat((RFYqqRKKmjXUBaAsdvUNUVYmwpdtlLAs, DdOKIUfxJrXFIHAKuVLUlmUgnrQkZRli), 1)
    return zRgvHDpLPapjNJFYZGjIsEFUGSeSLqvB
class tAFRhnnpyvANwFHLoOiQKhbxekqneEYc(FysyHDAhzveVQGJRNBJHfHxZedLYKfhV):
    def __init__(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, QndHjlfwhEimYkuHnNTDxkEXYaCwJdZe, noise_aug_config, SZAVLBSfrTycZhmQUtWaVvoZUmpPNFnx=DwnytdzUnaxYSvjidBVNMySSZNKfKUln.IfSpexRRCKcIegeOUYKebxpBmBzRLaRR, fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc=None):
        super().__init__(QndHjlfwhEimYkuHnNTDxkEXYaCwJdZe, SZAVLBSfrTycZhmQUtWaVvoZUmpPNFnx, fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc=fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.noise_augmentor = NgrOydhziQoGvGMNEZwABugeswryRyaC(**noise_aug_config)
    def iadrkNoUAKhvRZERXmJdkECHhlSflify(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, **kwargs):
        ZzfVwnmJdpNHBYfiTQQyOPhQeKDLCUve = kwargs.get("unclip_conditioning", None)
        fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc = kwargs["device"]
        if ZzfVwnmJdpNHBYfiTQQyOPhQeKDLCUve is None:
            return torch.zeros((1, rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.adm_channels))
        else:
            return YGCBPyMASawsnGcFuVwXihSDBCdMBjHG(ZzfVwnmJdpNHBYfiTQQyOPhQeKDLCUve, fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc, rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.noise_augmentor, kwargs.get("unclip_noise_augment_merge", 0.05))
def NFyeLLVysrVhovomSVRlQnhDWhqLBJRX(DukiculvUpjhZIVvaGinshRSKLSTgVVl, noise_augmentor):
    if "unclip_conditioning" in DukiculvUpjhZIVvaGinshRSKLSTgVVl:
        return YGCBPyMASawsnGcFuVwXihSDBCdMBjHG(DukiculvUpjhZIVvaGinshRSKLSTgVVl.get("unclip_conditioning", None), DukiculvUpjhZIVvaGinshRSKLSTgVVl["device"], noise_augmentor)[:,:1280]
    else:
        return DukiculvUpjhZIVvaGinshRSKLSTgVVl["pooled_output"]
class ahTMwLxNlVsoQmeFJViVzKGaCTtMabpM(FysyHDAhzveVQGJRNBJHfHxZedLYKfhV):
    def __init__(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, QndHjlfwhEimYkuHnNTDxkEXYaCwJdZe, SZAVLBSfrTycZhmQUtWaVvoZUmpPNFnx=DwnytdzUnaxYSvjidBVNMySSZNKfKUln.kAXyAlkwERgiSykVggDfAbBFSPRWsPbJ, fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc=None):
        super().__init__(QndHjlfwhEimYkuHnNTDxkEXYaCwJdZe, SZAVLBSfrTycZhmQUtWaVvoZUmpPNFnx, fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc=fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.embedder = zGGBuzFwarRcjrVdvKsXbQZONUVfKAiA(256)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.noise_augmentor = NgrOydhziQoGvGMNEZwABugeswryRyaC(**{"noise_schedule_config": {"timesteps": 1000, "beta_schedule": "squaredcos_cap_v2"}, "timestep_dim": 1280})
    def iadrkNoUAKhvRZERXmJdkECHhlSflify(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, **kwargs):
        JbRmbaVunzHLSnmtOIGFVqxUjyPuorzp = NFyeLLVysrVhovomSVRlQnhDWhqLBJRX(kwargs, rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.noise_augmentor)
        QfeoFYGsEQNWblsqXsRKWQpzeXgWujaz = kwargs.get("width", 768)
        yhGxnlfJCKaDHyDtiYhJHxHFcooDKiMM = kwargs.get("height", 768)
        gNBQsENpfAEjUTlqLNIsjPlUsljIbCBQ = kwargs.get("crop_w", 0)
        nhLpIvItTMyjINvSBHRVUTXxNWzrYxER = kwargs.get("crop_h", 0)
        if kwargs.get("prompt_type", "") == "negative":
            KEyecOkfNjuTthURrYKtLIohdlkPUfkA = kwargs.get("aesthetic_score", 2.5)
        else:
            KEyecOkfNjuTthURrYKtLIohdlkPUfkA = kwargs.get("aesthetic_score", 6)
        iqymPVpxyjOWChGwBkTemSzHJbnJdAIz = []
        iqymPVpxyjOWChGwBkTemSzHJbnJdAIz.append(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.embedder(torch.Tensor([yhGxnlfJCKaDHyDtiYhJHxHFcooDKiMM])))
        iqymPVpxyjOWChGwBkTemSzHJbnJdAIz.append(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.embedder(torch.Tensor([QfeoFYGsEQNWblsqXsRKWQpzeXgWujaz])))
        iqymPVpxyjOWChGwBkTemSzHJbnJdAIz.append(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.embedder(torch.Tensor([nhLpIvItTMyjINvSBHRVUTXxNWzrYxER])))
        iqymPVpxyjOWChGwBkTemSzHJbnJdAIz.append(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.embedder(torch.Tensor([gNBQsENpfAEjUTlqLNIsjPlUsljIbCBQ])))
        iqymPVpxyjOWChGwBkTemSzHJbnJdAIz.append(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.embedder(torch.Tensor([KEyecOkfNjuTthURrYKtLIohdlkPUfkA])))
        dMNYoiekoVGXpGCuaVbLxmdvNkyLfQxu = torch.flatten(torch.cat(iqymPVpxyjOWChGwBkTemSzHJbnJdAIz))[None, ]
        return torch.cat((JbRmbaVunzHLSnmtOIGFVqxUjyPuorzp.sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ(dMNYoiekoVGXpGCuaVbLxmdvNkyLfQxu.fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc), dMNYoiekoVGXpGCuaVbLxmdvNkyLfQxu), yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk=1)
class hTIrchlPHYZofZJBRoQFMjAnlKwSEPlB(FysyHDAhzveVQGJRNBJHfHxZedLYKfhV):
    def __init__(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, QndHjlfwhEimYkuHnNTDxkEXYaCwJdZe, SZAVLBSfrTycZhmQUtWaVvoZUmpPNFnx=DwnytdzUnaxYSvjidBVNMySSZNKfKUln.kAXyAlkwERgiSykVggDfAbBFSPRWsPbJ, fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc=None):
        super().__init__(QndHjlfwhEimYkuHnNTDxkEXYaCwJdZe, SZAVLBSfrTycZhmQUtWaVvoZUmpPNFnx, fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc=fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.embedder = zGGBuzFwarRcjrVdvKsXbQZONUVfKAiA(256)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.noise_augmentor = NgrOydhziQoGvGMNEZwABugeswryRyaC(**{"noise_schedule_config": {"timesteps": 1000, "beta_schedule": "squaredcos_cap_v2"}, "timestep_dim": 1280})
    def iadrkNoUAKhvRZERXmJdkECHhlSflify(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, **kwargs):
        JbRmbaVunzHLSnmtOIGFVqxUjyPuorzp = NFyeLLVysrVhovomSVRlQnhDWhqLBJRX(kwargs, rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.noise_augmentor)
        QfeoFYGsEQNWblsqXsRKWQpzeXgWujaz = kwargs.get("width", 768)
        yhGxnlfJCKaDHyDtiYhJHxHFcooDKiMM = kwargs.get("height", 768)
        gNBQsENpfAEjUTlqLNIsjPlUsljIbCBQ = kwargs.get("crop_w", 0)
        nhLpIvItTMyjINvSBHRVUTXxNWzrYxER = kwargs.get("crop_h", 0)
        bVODaYwLNfOuGacesUknmlKdenPENBxe = kwargs.get("target_width", QfeoFYGsEQNWblsqXsRKWQpzeXgWujaz)
        LrCIzQBLSdvHzuvIPhNZjYkKeYNNmKRh = kwargs.get("target_height", yhGxnlfJCKaDHyDtiYhJHxHFcooDKiMM)
        iqymPVpxyjOWChGwBkTemSzHJbnJdAIz = []
        iqymPVpxyjOWChGwBkTemSzHJbnJdAIz.append(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.embedder(torch.Tensor([yhGxnlfJCKaDHyDtiYhJHxHFcooDKiMM])))
        iqymPVpxyjOWChGwBkTemSzHJbnJdAIz.append(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.embedder(torch.Tensor([QfeoFYGsEQNWblsqXsRKWQpzeXgWujaz])))
        iqymPVpxyjOWChGwBkTemSzHJbnJdAIz.append(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.embedder(torch.Tensor([nhLpIvItTMyjINvSBHRVUTXxNWzrYxER])))
        iqymPVpxyjOWChGwBkTemSzHJbnJdAIz.append(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.embedder(torch.Tensor([gNBQsENpfAEjUTlqLNIsjPlUsljIbCBQ])))
        iqymPVpxyjOWChGwBkTemSzHJbnJdAIz.append(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.embedder(torch.Tensor([LrCIzQBLSdvHzuvIPhNZjYkKeYNNmKRh])))
        iqymPVpxyjOWChGwBkTemSzHJbnJdAIz.append(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.embedder(torch.Tensor([bVODaYwLNfOuGacesUknmlKdenPENBxe])))
        dMNYoiekoVGXpGCuaVbLxmdvNkyLfQxu = torch.flatten(torch.cat(iqymPVpxyjOWChGwBkTemSzHJbnJdAIz))[None, ]
        return torch.cat((JbRmbaVunzHLSnmtOIGFVqxUjyPuorzp.sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ(dMNYoiekoVGXpGCuaVbLxmdvNkyLfQxu.fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc), dMNYoiekoVGXpGCuaVbLxmdvNkyLfQxu), yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk=1)
