import torch
import copy
import inspect
import quasar.utils
class CmIugCFMKLyCSZlTCvUgomMGPXzvLNTG:
    def __init__(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM, load_device, SlzENmVKreawuuvgrVSmYHZXOypOtbgl, vqDBJgidQufnKyAltPYRqiKGjmztArDJ=0, current_device=None):
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.vqDBJgidQufnKyAltPYRqiKGjmztArDJ = vqDBJgidQufnKyAltPYRqiKGjmztArDJ
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM = VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.ekVpHYaEdxHmTAUTGagpPstWpGZqnyTJ = {}
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.backup = {}
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.model_options = {"transformer_options":{}}
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.ymWRjcVVevoMjPXqCNiaROKjJDVRxVuV()
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.load_device = load_device
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.SlzENmVKreawuuvgrVSmYHZXOypOtbgl = SlzENmVKreawuuvgrVSmYHZXOypOtbgl
        if current_device is None:
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.current_device = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.SlzENmVKreawuuvgrVSmYHZXOypOtbgl
        else:
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.current_device = current_device
    def ymWRjcVVevoMjPXqCNiaROKjJDVRxVuV(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS):
        if rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.vqDBJgidQufnKyAltPYRqiKGjmztArDJ > 0:
            return rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.vqDBJgidQufnKyAltPYRqiKGjmztArDJ
        DuCZHcDcohTFINauhREJWKOwRCPqBMNf = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM.TQRgUMPjEwYAaDvSuzgvheADStCoUKzT()
        vqDBJgidQufnKyAltPYRqiKGjmztArDJ = 0
        for EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm in DuCZHcDcohTFINauhREJWKOwRCPqBMNf:
            XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz = DuCZHcDcohTFINauhREJWKOwRCPqBMNf[EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm]
            vqDBJgidQufnKyAltPYRqiKGjmztArDJ += XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz.nelement() * XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz.element_size()
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.vqDBJgidQufnKyAltPYRqiKGjmztArDJ = vqDBJgidQufnKyAltPYRqiKGjmztArDJ
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.model_keys = set(DuCZHcDcohTFINauhREJWKOwRCPqBMNf.keys())
        return vqDBJgidQufnKyAltPYRqiKGjmztArDJ
    def tEcQvpBwXwdqvKxRTLEBROBUyPoodldL(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS):
        zXHJFiFFvWqeQIAxyaTGMUgoRaHrYzjK = CmIugCFMKLyCSZlTCvUgomMGPXzvLNTG(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM, rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.load_device, rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.SlzENmVKreawuuvgrVSmYHZXOypOtbgl, rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.vqDBJgidQufnKyAltPYRqiKGjmztArDJ, rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.current_device)
        zXHJFiFFvWqeQIAxyaTGMUgoRaHrYzjK.ekVpHYaEdxHmTAUTGagpPstWpGZqnyTJ = {}
        for EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm in rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.ekVpHYaEdxHmTAUTGagpPstWpGZqnyTJ:
            zXHJFiFFvWqeQIAxyaTGMUgoRaHrYzjK.ekVpHYaEdxHmTAUTGagpPstWpGZqnyTJ[EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm] = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.ekVpHYaEdxHmTAUTGagpPstWpGZqnyTJ[EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm][:]
        zXHJFiFFvWqeQIAxyaTGMUgoRaHrYzjK.model_options = copy.deepcopy(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.model_options)
        zXHJFiFFvWqeQIAxyaTGMUgoRaHrYzjK.model_keys = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.model_keys
        return zXHJFiFFvWqeQIAxyaTGMUgoRaHrYzjK
    def hlsUPEbCDylvHBJIhHotpulFhpPyOFlW(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, other):
        if hasattr(other, 'model') and rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM is other.VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM:
            return True
        return False
    def qfLPSyeSxlbbWAuRsihXathlrqHkiaIB(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, sampler_cfg_function):
        if len(inspect.signature(sampler_cfg_function).parameters) == 3:
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.model_options["sampler_cfg_function"] = lambda DukiculvUpjhZIVvaGinshRSKLSTgVVl: sampler_cfg_function(DukiculvUpjhZIVvaGinshRSKLSTgVVl["cond"], DukiculvUpjhZIVvaGinshRSKLSTgVVl["uncond"], DukiculvUpjhZIVvaGinshRSKLSTgVVl["cond_scale"]) 
        else:
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.model_options["sampler_cfg_function"] = sampler_cfg_function
    def NSWvVpnNXQNVmvIfTYANKVEUuiTEnfwo(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, unet_wrapper_function):
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.model_options["model_function_wrapper"] = unet_wrapper_function
    def zWHHfZNTuCGrFQaOtVviFqgtDFAJTTcu(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, YBkyOiHLPkzbgIAzSqhyviJVGfxblkPn, pSfJNVvqLWVlUeHdpahCTGSrSPJYAnEQ):
        sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.model_options["transformer_options"]
        if "patches" not in sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ:
            sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ["patches"] = {}
        sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ["patches"][pSfJNVvqLWVlUeHdpahCTGSrSPJYAnEQ] = sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ["patches"].get(pSfJNVvqLWVlUeHdpahCTGSrSPJYAnEQ, []) + [YBkyOiHLPkzbgIAzSqhyviJVGfxblkPn]
    def zFUiKqfWUnwPMzfBXahnOLUJRtWPmxSh(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, YBkyOiHLPkzbgIAzSqhyviJVGfxblkPn, pSfJNVvqLWVlUeHdpahCTGSrSPJYAnEQ, block_name, FCVsdRzGunasBiYAXHkNdLEMUdcXuHLD):
        sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.model_options["transformer_options"]
        if "patches_replace" not in sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ:
            sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ["patches_replace"] = {}
        if pSfJNVvqLWVlUeHdpahCTGSrSPJYAnEQ not in sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ["patches_replace"]:
            sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ["patches_replace"][pSfJNVvqLWVlUeHdpahCTGSrSPJYAnEQ] = {}
        sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ["patches_replace"][pSfJNVvqLWVlUeHdpahCTGSrSPJYAnEQ][(block_name, FCVsdRzGunasBiYAXHkNdLEMUdcXuHLD)] = YBkyOiHLPkzbgIAzSqhyviJVGfxblkPn
    def hHPgZMdHzzFfDXPQMViqoITNoINrStkW(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, YBkyOiHLPkzbgIAzSqhyviJVGfxblkPn):
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.zWHHfZNTuCGrFQaOtVviFqgtDFAJTTcu(YBkyOiHLPkzbgIAzSqhyviJVGfxblkPn, "attn1_patch")
    def jstBFVPVrDeSKOCaLQsAhwclSzZXFUnY(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, YBkyOiHLPkzbgIAzSqhyviJVGfxblkPn):
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.zWHHfZNTuCGrFQaOtVviFqgtDFAJTTcu(YBkyOiHLPkzbgIAzSqhyviJVGfxblkPn, "attn2_patch")
    def ONUgPoPLwDFRemkvUyDNspfXnfbvIhBo(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, YBkyOiHLPkzbgIAzSqhyviJVGfxblkPn, block_name, FCVsdRzGunasBiYAXHkNdLEMUdcXuHLD):
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.zFUiKqfWUnwPMzfBXahnOLUJRtWPmxSh(YBkyOiHLPkzbgIAzSqhyviJVGfxblkPn, "attn1", block_name, FCVsdRzGunasBiYAXHkNdLEMUdcXuHLD)
    def jwvhDuAitkTmaplPxOLpxgtpMTFbiZdI(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, YBkyOiHLPkzbgIAzSqhyviJVGfxblkPn, block_name, FCVsdRzGunasBiYAXHkNdLEMUdcXuHLD):
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.zFUiKqfWUnwPMzfBXahnOLUJRtWPmxSh(YBkyOiHLPkzbgIAzSqhyviJVGfxblkPn, "attn2", block_name, FCVsdRzGunasBiYAXHkNdLEMUdcXuHLD)
    def txbawuMALHkhgtOzAokeJqwirFBcbkye(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, YBkyOiHLPkzbgIAzSqhyviJVGfxblkPn):
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.zWHHfZNTuCGrFQaOtVviFqgtDFAJTTcu(YBkyOiHLPkzbgIAzSqhyviJVGfxblkPn, "attn1_output_patch")
    def RzGUAOyzxMQBYaBeWTTfeAWrrvYsXxTA(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, YBkyOiHLPkzbgIAzSqhyviJVGfxblkPn):
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.zWHHfZNTuCGrFQaOtVviFqgtDFAJTTcu(YBkyOiHLPkzbgIAzSqhyviJVGfxblkPn, "attn2_output_patch")
    def RDTOrwmBjfxGxlZjvgtcnLQViOIXZSlc(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc):
        sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.model_options["transformer_options"]
        if "patches" in sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ:
            ekVpHYaEdxHmTAUTGagpPstWpGZqnyTJ = sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ["patches"]
            for pSfJNVvqLWVlUeHdpahCTGSrSPJYAnEQ in ekVpHYaEdxHmTAUTGagpPstWpGZqnyTJ:
                NhYSPRlcnbfweJUAsezRaHlXQpiOjOyN = ekVpHYaEdxHmTAUTGagpPstWpGZqnyTJ[pSfJNVvqLWVlUeHdpahCTGSrSPJYAnEQ]
                for HCXmerBqIMuTscBONzTGKYapYSxWTYHo in range(len(NhYSPRlcnbfweJUAsezRaHlXQpiOjOyN)):
                    if hasattr(NhYSPRlcnbfweJUAsezRaHlXQpiOjOyN[HCXmerBqIMuTscBONzTGKYapYSxWTYHo], "to"):
                        NhYSPRlcnbfweJUAsezRaHlXQpiOjOyN[HCXmerBqIMuTscBONzTGKYapYSxWTYHo] = NhYSPRlcnbfweJUAsezRaHlXQpiOjOyN[HCXmerBqIMuTscBONzTGKYapYSxWTYHo].sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ(fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc)
        if "patches_replace" in sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ:
            ekVpHYaEdxHmTAUTGagpPstWpGZqnyTJ = sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ["patches_replace"]
            for pSfJNVvqLWVlUeHdpahCTGSrSPJYAnEQ in ekVpHYaEdxHmTAUTGagpPstWpGZqnyTJ:
                NhYSPRlcnbfweJUAsezRaHlXQpiOjOyN = ekVpHYaEdxHmTAUTGagpPstWpGZqnyTJ[pSfJNVvqLWVlUeHdpahCTGSrSPJYAnEQ]
                for EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm in NhYSPRlcnbfweJUAsezRaHlXQpiOjOyN:
                    if hasattr(NhYSPRlcnbfweJUAsezRaHlXQpiOjOyN[EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm], "to"):
                        NhYSPRlcnbfweJUAsezRaHlXQpiOjOyN[EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm] = NhYSPRlcnbfweJUAsezRaHlXQpiOjOyN[EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm].sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ(fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc)
    def LnVirSCOJainsBkOCuBFzVkpVqINXQDh(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS):
        if hasattr(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM, "get_dtype"):
            return rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM.qCYGtbmEmpKHSGaChkRoXdcCONojeSqh()
    def YCDdUyUqMtJdmPkuPqHlFfOepJfSNumr(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, ekVpHYaEdxHmTAUTGagpPstWpGZqnyTJ, strength_patch=1.0, AePTHMNnzpcegVKckEDvKCKXrzsGyVqK=1.0):
        HutkrxeXIuRQKOhCWHkiwqLGAsJjUSKj = set()
        for EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm in ekVpHYaEdxHmTAUTGagpPstWpGZqnyTJ:
            if EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm in rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.model_keys:
                HutkrxeXIuRQKOhCWHkiwqLGAsJjUSKj.add(EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm)
                lFLONOcxqUkiOEFVQcEAEXUbrVfhWnRj = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.ekVpHYaEdxHmTAUTGagpPstWpGZqnyTJ.get(EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm, [])
                lFLONOcxqUkiOEFVQcEAEXUbrVfhWnRj.append((strength_patch, ekVpHYaEdxHmTAUTGagpPstWpGZqnyTJ[EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm], AePTHMNnzpcegVKckEDvKCKXrzsGyVqK))
                rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.ekVpHYaEdxHmTAUTGagpPstWpGZqnyTJ[EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm] = lFLONOcxqUkiOEFVQcEAEXUbrVfhWnRj
        return list(HutkrxeXIuRQKOhCWHkiwqLGAsJjUSKj)
    def MiFcVkRoNonoSGEjRftqYlrqzyKSnTxf(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, filter_prefix=None):
        DuCZHcDcohTFINauhREJWKOwRCPqBMNf = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.wViWufbihckgCqLqPyInDJEhNgDtoTrR()
        HutkrxeXIuRQKOhCWHkiwqLGAsJjUSKj = {}
        for EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm in DuCZHcDcohTFINauhREJWKOwRCPqBMNf:
            if filter_prefix is not None:
                if not EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm.startswith(filter_prefix):
                    continue
            if EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm in rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.ekVpHYaEdxHmTAUTGagpPstWpGZqnyTJ:
                HutkrxeXIuRQKOhCWHkiwqLGAsJjUSKj[EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm] = [DuCZHcDcohTFINauhREJWKOwRCPqBMNf[EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm]] + rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.ekVpHYaEdxHmTAUTGagpPstWpGZqnyTJ[EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm]
            else:
                HutkrxeXIuRQKOhCWHkiwqLGAsJjUSKj[EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm] = (DuCZHcDcohTFINauhREJWKOwRCPqBMNf[EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm],)
        return HutkrxeXIuRQKOhCWHkiwqLGAsJjUSKj
    def wViWufbihckgCqLqPyInDJEhNgDtoTrR(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, filter_prefix=None):
        ylGhUFMpxPbtUUTfCZpemVkdanRhWmHa = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM.TQRgUMPjEwYAaDvSuzgvheADStCoUKzT()
        keys = list(ylGhUFMpxPbtUUTfCZpemVkdanRhWmHa.keys())
        if filter_prefix is not None:
            for EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm in keys:
                if not EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm.startswith(filter_prefix):
                    ylGhUFMpxPbtUUTfCZpemVkdanRhWmHa.pop(EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm)
        return ylGhUFMpxPbtUUTfCZpemVkdanRhWmHa
    def QbcJNaFyswYsDxKtpcxHQUBPsPaTuJFs(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, device_to=None):
        DuCZHcDcohTFINauhREJWKOwRCPqBMNf = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.wViWufbihckgCqLqPyInDJEhNgDtoTrR()
        for nyrzKxQtioheHIZujafABgijbCjrWhBU in rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.ekVpHYaEdxHmTAUTGagpPstWpGZqnyTJ:
            if nyrzKxQtioheHIZujafABgijbCjrWhBU not in DuCZHcDcohTFINauhREJWKOwRCPqBMNf:
                print("could not patch. key doesn'XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz exist in VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM:", key)
                continue
            RXBOtvKSHQkBvdKDbckmnlphvVygYURP = DuCZHcDcohTFINauhREJWKOwRCPqBMNf[nyrzKxQtioheHIZujafABgijbCjrWhBU]
            if nyrzKxQtioheHIZujafABgijbCjrWhBU not in rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.backup:
                rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.backup[nyrzKxQtioheHIZujafABgijbCjrWhBU] = RXBOtvKSHQkBvdKDbckmnlphvVygYURP.sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.SlzENmVKreawuuvgrVSmYHZXOypOtbgl)
            if device_to is not None:
                uCdeLjKNUjhGyZTaKpTfnEwFcwcWIBVC = RXBOtvKSHQkBvdKDbckmnlphvVygYURP.float().sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ(device_to, copy=True)
            else:
                uCdeLjKNUjhGyZTaKpTfnEwFcwcWIBVC = RXBOtvKSHQkBvdKDbckmnlphvVygYURP.sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ(torch.float32, copy=True)
            ulzhfxpWeozEPSDCLiQxrhhDOSufxcZJ = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.hohSFVVKzjRRbdFrdNTiRUVVsZGrIdsh(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.ekVpHYaEdxHmTAUTGagpPstWpGZqnyTJ[nyrzKxQtioheHIZujafABgijbCjrWhBU], uCdeLjKNUjhGyZTaKpTfnEwFcwcWIBVC, nyrzKxQtioheHIZujafABgijbCjrWhBU).sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ(RXBOtvKSHQkBvdKDbckmnlphvVygYURP.DDRQlhrNSGpwTrokWitkZipdfbAqBFxv)
            quasar.utils.set_attr(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM, nyrzKxQtioheHIZujafABgijbCjrWhBU, ulzhfxpWeozEPSDCLiQxrhhDOSufxcZJ)
            del uCdeLjKNUjhGyZTaKpTfnEwFcwcWIBVC
        if device_to is not None:
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM.sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ(device_to)
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.current_device = device_to
        return rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM
    def hohSFVVKzjRRbdFrdNTiRUVVsZGrIdsh(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, ekVpHYaEdxHmTAUTGagpPstWpGZqnyTJ, RXBOtvKSHQkBvdKDbckmnlphvVygYURP, nyrzKxQtioheHIZujafABgijbCjrWhBU):
        for HutkrxeXIuRQKOhCWHkiwqLGAsJjUSKj in ekVpHYaEdxHmTAUTGagpPstWpGZqnyTJ:
            uigKGapaQVcFiOjEiWwRAHjjkAWxsqck = HutkrxeXIuRQKOhCWHkiwqLGAsJjUSKj[0]
            powGafreWfwlSAqPpTpUhFgpFVqCPavl = HutkrxeXIuRQKOhCWHkiwqLGAsJjUSKj[1]
            AePTHMNnzpcegVKckEDvKCKXrzsGyVqK = HutkrxeXIuRQKOhCWHkiwqLGAsJjUSKj[2]
            if AePTHMNnzpcegVKckEDvKCKXrzsGyVqK != 1.0:
                RXBOtvKSHQkBvdKDbckmnlphvVygYURP *= AePTHMNnzpcegVKckEDvKCKXrzsGyVqK
            if isinstance(powGafreWfwlSAqPpTpUhFgpFVqCPavl, list):
                powGafreWfwlSAqPpTpUhFgpFVqCPavl = (rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.hohSFVVKzjRRbdFrdNTiRUVVsZGrIdsh(powGafreWfwlSAqPpTpUhFgpFVqCPavl[1:], powGafreWfwlSAqPpTpUhFgpFVqCPavl[0].tEcQvpBwXwdqvKxRTLEBROBUyPoodldL(), nyrzKxQtioheHIZujafABgijbCjrWhBU), )
            if len(powGafreWfwlSAqPpTpUhFgpFVqCPavl) == 1:
                rahbMaYjYoBuHaHlnFppXkTwWEjOXkZz = powGafreWfwlSAqPpTpUhFgpFVqCPavl[0]
                if uigKGapaQVcFiOjEiWwRAHjjkAWxsqck != 0.0:
                    if rahbMaYjYoBuHaHlnFppXkTwWEjOXkZz.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg != RXBOtvKSHQkBvdKDbckmnlphvVygYURP.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg:
                        print("WARNING SHAPE MISMATCH {} WEIGHT NOT MERGED {} != {}".format(nyrzKxQtioheHIZujafABgijbCjrWhBU, rahbMaYjYoBuHaHlnFppXkTwWEjOXkZz.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg, RXBOtvKSHQkBvdKDbckmnlphvVygYURP.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg))
                    else:
                        RXBOtvKSHQkBvdKDbckmnlphvVygYURP += uigKGapaQVcFiOjEiWwRAHjjkAWxsqck * rahbMaYjYoBuHaHlnFppXkTwWEjOXkZz.type(RXBOtvKSHQkBvdKDbckmnlphvVygYURP.DDRQlhrNSGpwTrokWitkZipdfbAqBFxv).sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ(RXBOtvKSHQkBvdKDbckmnlphvVygYURP.fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc)
            elif len(powGafreWfwlSAqPpTpUhFgpFVqCPavl) == 4: 
                VZNqhEnUabofQRdpcqKPiDFOKIQLZyXy = powGafreWfwlSAqPpTpUhFgpFVqCPavl[0].float().sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ(RXBOtvKSHQkBvdKDbckmnlphvVygYURP.fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc)
                CWlXuzuthlRoWJnhRBJPhPFWvnIgTzrw = powGafreWfwlSAqPpTpUhFgpFVqCPavl[1].float().sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ(RXBOtvKSHQkBvdKDbckmnlphvVygYURP.fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc)
                if powGafreWfwlSAqPpTpUhFgpFVqCPavl[2] is not None:
                    uigKGapaQVcFiOjEiWwRAHjjkAWxsqck *= powGafreWfwlSAqPpTpUhFgpFVqCPavl[2] / CWlXuzuthlRoWJnhRBJPhPFWvnIgTzrw.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[0]
                if powGafreWfwlSAqPpTpUhFgpFVqCPavl[3] is not None:
                    bmrCwyWIElmcwaxRZzPJCDOdVadEBWGL = powGafreWfwlSAqPpTpUhFgpFVqCPavl[3].float().sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ(RXBOtvKSHQkBvdKDbckmnlphvVygYURP.fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc)
                    IUtWwUXXyRIbjKOykiBZUwewIRKJWqXu = [CWlXuzuthlRoWJnhRBJPhPFWvnIgTzrw.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[1], CWlXuzuthlRoWJnhRBJPhPFWvnIgTzrw.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[0], bmrCwyWIElmcwaxRZzPJCDOdVadEBWGL.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[2], bmrCwyWIElmcwaxRZzPJCDOdVadEBWGL.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[3]]
                    CWlXuzuthlRoWJnhRBJPhPFWvnIgTzrw = torch.mm(CWlXuzuthlRoWJnhRBJPhPFWvnIgTzrw.transpose(0, 1).flatten(start_dim=1), bmrCwyWIElmcwaxRZzPJCDOdVadEBWGL.transpose(0, 1).flatten(start_dim=1)).reshape(IUtWwUXXyRIbjKOykiBZUwewIRKJWqXu).transpose(0, 1)
                try:
                    RXBOtvKSHQkBvdKDbckmnlphvVygYURP += (uigKGapaQVcFiOjEiWwRAHjjkAWxsqck * torch.mm(VZNqhEnUabofQRdpcqKPiDFOKIQLZyXy.flatten(start_dim=1), CWlXuzuthlRoWJnhRBJPhPFWvnIgTzrw.flatten(start_dim=1))).reshape(RXBOtvKSHQkBvdKDbckmnlphvVygYURP.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg).type(RXBOtvKSHQkBvdKDbckmnlphvVygYURP.DDRQlhrNSGpwTrokWitkZipdfbAqBFxv)
                except Exception as dgvKdkEDrMSdkCaRxfkDNVbaXWUetgtO:
                    print("ERROR", nyrzKxQtioheHIZujafABgijbCjrWhBU, dgvKdkEDrMSdkCaRxfkDNVbaXWUetgtO)
            elif len(powGafreWfwlSAqPpTpUhFgpFVqCPavl) == 8: 
                rahbMaYjYoBuHaHlnFppXkTwWEjOXkZz = powGafreWfwlSAqPpTpUhFgpFVqCPavl[0]
                XFaYZeQHhHcFoFkifpAZpLIdEgwsCGtr = powGafreWfwlSAqPpTpUhFgpFVqCPavl[1]
                DmZxJLYDLyJTOSqDkZsVLGQouwcjczfv = powGafreWfwlSAqPpTpUhFgpFVqCPavl[3]
                qixTrwIOUXDoQNzjprsLsabWAvkmhSvW = powGafreWfwlSAqPpTpUhFgpFVqCPavl[4]
                fXUsCrvHhtRjMANxFJDpUvvxlXhcTyoH = powGafreWfwlSAqPpTpUhFgpFVqCPavl[5]
                AFDbLtRSuWGiyKjAlbhHDmxikbDhRiQG = powGafreWfwlSAqPpTpUhFgpFVqCPavl[6]
                SXMDczZzLdqpUMJBQtNGtweCYzyrWfqb = powGafreWfwlSAqPpTpUhFgpFVqCPavl[7]
                yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk = None
                if rahbMaYjYoBuHaHlnFppXkTwWEjOXkZz is None:
                    yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk = qixTrwIOUXDoQNzjprsLsabWAvkmhSvW.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[0]
                    rahbMaYjYoBuHaHlnFppXkTwWEjOXkZz = torch.mm(DmZxJLYDLyJTOSqDkZsVLGQouwcjczfv.float(), qixTrwIOUXDoQNzjprsLsabWAvkmhSvW.float())
                else:
                    rahbMaYjYoBuHaHlnFppXkTwWEjOXkZz = rahbMaYjYoBuHaHlnFppXkTwWEjOXkZz.float().sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ(RXBOtvKSHQkBvdKDbckmnlphvVygYURP.fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc)
                if XFaYZeQHhHcFoFkifpAZpLIdEgwsCGtr is None:
                    yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk = AFDbLtRSuWGiyKjAlbhHDmxikbDhRiQG.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[0]
                    if SXMDczZzLdqpUMJBQtNGtweCYzyrWfqb is None:
                        XFaYZeQHhHcFoFkifpAZpLIdEgwsCGtr = torch.mm(fXUsCrvHhtRjMANxFJDpUvvxlXhcTyoH.float().sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ(RXBOtvKSHQkBvdKDbckmnlphvVygYURP.fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc), AFDbLtRSuWGiyKjAlbhHDmxikbDhRiQG.float().sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ(RXBOtvKSHQkBvdKDbckmnlphvVygYURP.fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc))
                    else:
                        XFaYZeQHhHcFoFkifpAZpLIdEgwsCGtr = torch.einsum('i j k l, j r, i p -> p r k l', SXMDczZzLdqpUMJBQtNGtweCYzyrWfqb.float().sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ(RXBOtvKSHQkBvdKDbckmnlphvVygYURP.fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc), AFDbLtRSuWGiyKjAlbhHDmxikbDhRiQG.float().sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ(RXBOtvKSHQkBvdKDbckmnlphvVygYURP.fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc), fXUsCrvHhtRjMANxFJDpUvvxlXhcTyoH.float().sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ(RXBOtvKSHQkBvdKDbckmnlphvVygYURP.fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc))
                else:
                    XFaYZeQHhHcFoFkifpAZpLIdEgwsCGtr = XFaYZeQHhHcFoFkifpAZpLIdEgwsCGtr.float().sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ(RXBOtvKSHQkBvdKDbckmnlphvVygYURP.fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc)
                if len(XFaYZeQHhHcFoFkifpAZpLIdEgwsCGtr.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg) == 4:
                    rahbMaYjYoBuHaHlnFppXkTwWEjOXkZz = rahbMaYjYoBuHaHlnFppXkTwWEjOXkZz.unsqueeze(2).unsqueeze(2)
                if powGafreWfwlSAqPpTpUhFgpFVqCPavl[2] is not None and yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk is not None:
                    uigKGapaQVcFiOjEiWwRAHjjkAWxsqck *= powGafreWfwlSAqPpTpUhFgpFVqCPavl[2] / yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk
                try:
                    RXBOtvKSHQkBvdKDbckmnlphvVygYURP += uigKGapaQVcFiOjEiWwRAHjjkAWxsqck * torch.kron(rahbMaYjYoBuHaHlnFppXkTwWEjOXkZz, XFaYZeQHhHcFoFkifpAZpLIdEgwsCGtr).reshape(RXBOtvKSHQkBvdKDbckmnlphvVygYURP.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg).type(RXBOtvKSHQkBvdKDbckmnlphvVygYURP.DDRQlhrNSGpwTrokWitkZipdfbAqBFxv)
                except Exception as dgvKdkEDrMSdkCaRxfkDNVbaXWUetgtO:
                    print("ERROR", nyrzKxQtioheHIZujafABgijbCjrWhBU, dgvKdkEDrMSdkCaRxfkDNVbaXWUetgtO)
            else: 
                YFRYTblUCvmpudPptnfIkZaGrwHwbCXl = powGafreWfwlSAqPpTpUhFgpFVqCPavl[0]
                TejKyFxxqzSbdZIEQZGiMtkRYUmLdeqH = powGafreWfwlSAqPpTpUhFgpFVqCPavl[1]
                if powGafreWfwlSAqPpTpUhFgpFVqCPavl[2] is not None:
                    uigKGapaQVcFiOjEiWwRAHjjkAWxsqck *= powGafreWfwlSAqPpTpUhFgpFVqCPavl[2] / TejKyFxxqzSbdZIEQZGiMtkRYUmLdeqH.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[0]
                IBQwelvKJYLlbMbMoippWtnKdsAfwOhc = powGafreWfwlSAqPpTpUhFgpFVqCPavl[3]
                mmdlGNZIUiHQQmokxsyshkPaJyuxcETE = powGafreWfwlSAqPpTpUhFgpFVqCPavl[4]
                if powGafreWfwlSAqPpTpUhFgpFVqCPavl[5] is not None: 
                    MStccjMYPXYbPLBRJuuGIaVGkOvnhCnE = powGafreWfwlSAqPpTpUhFgpFVqCPavl[5]
                    SXMDczZzLdqpUMJBQtNGtweCYzyrWfqb = powGafreWfwlSAqPpTpUhFgpFVqCPavl[6]
                    YlClzfOVmSmgToWNeJaIGbCpQyZNxEYR = torch.einsum('i j k l, j r, i p -> p r k l', MStccjMYPXYbPLBRJuuGIaVGkOvnhCnE.float().sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ(RXBOtvKSHQkBvdKDbckmnlphvVygYURP.fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc), TejKyFxxqzSbdZIEQZGiMtkRYUmLdeqH.float().sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ(RXBOtvKSHQkBvdKDbckmnlphvVygYURP.fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc), YFRYTblUCvmpudPptnfIkZaGrwHwbCXl.float().sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ(RXBOtvKSHQkBvdKDbckmnlphvVygYURP.fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc))
                    OhjYNIzWDbfjvHZSFiecRobcokMYcLeE = torch.einsum('i j k l, j r, i p -> p r k l', SXMDczZzLdqpUMJBQtNGtweCYzyrWfqb.float().sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ(RXBOtvKSHQkBvdKDbckmnlphvVygYURP.fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc), mmdlGNZIUiHQQmokxsyshkPaJyuxcETE.float().sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ(RXBOtvKSHQkBvdKDbckmnlphvVygYURP.fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc), IBQwelvKJYLlbMbMoippWtnKdsAfwOhc.float().sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ(RXBOtvKSHQkBvdKDbckmnlphvVygYURP.fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc))
                else:
                    YlClzfOVmSmgToWNeJaIGbCpQyZNxEYR = torch.mm(YFRYTblUCvmpudPptnfIkZaGrwHwbCXl.float().sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ(RXBOtvKSHQkBvdKDbckmnlphvVygYURP.fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc), TejKyFxxqzSbdZIEQZGiMtkRYUmLdeqH.float().sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ(RXBOtvKSHQkBvdKDbckmnlphvVygYURP.fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc))
                    OhjYNIzWDbfjvHZSFiecRobcokMYcLeE = torch.mm(IBQwelvKJYLlbMbMoippWtnKdsAfwOhc.float().sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ(RXBOtvKSHQkBvdKDbckmnlphvVygYURP.fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc), mmdlGNZIUiHQQmokxsyshkPaJyuxcETE.float().sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ(RXBOtvKSHQkBvdKDbckmnlphvVygYURP.fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc))
                try:
                    RXBOtvKSHQkBvdKDbckmnlphvVygYURP += (uigKGapaQVcFiOjEiWwRAHjjkAWxsqck * YlClzfOVmSmgToWNeJaIGbCpQyZNxEYR * OhjYNIzWDbfjvHZSFiecRobcokMYcLeE).reshape(RXBOtvKSHQkBvdKDbckmnlphvVygYURP.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg).type(RXBOtvKSHQkBvdKDbckmnlphvVygYURP.DDRQlhrNSGpwTrokWitkZipdfbAqBFxv)
                except Exception as dgvKdkEDrMSdkCaRxfkDNVbaXWUetgtO:
                    print("ERROR", nyrzKxQtioheHIZujafABgijbCjrWhBU, dgvKdkEDrMSdkCaRxfkDNVbaXWUetgtO)
        return RXBOtvKSHQkBvdKDbckmnlphvVygYURP
    def IPVijuJuWpDdBNNaJrYLjziBbaCAwYlc(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, device_to=None):
        keys = list(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.backup.keys())
        for EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm in keys:
            quasar.utils.set_attr(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM, EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm, rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.backup[EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm])
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.backup = {}
        if device_to is not None:
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM.sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ(device_to)
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.current_device = device_to
