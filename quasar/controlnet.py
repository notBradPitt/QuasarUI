import torch
import math
import os
import quasar.utils
import quasar.model_management
import quasar.model_detection
import quasar.model_patcher
import quasar.cldm.cldm
import quasar.t2i_adapter.adapter
def XaWuNSGWVpidbPpqOMxwLzayHbrlGbVP(xPmCFphFKpGMpIsczaSKHmMgRPZzJwla, target_batch_size, batched_number):
    uePWnTjDNXOJQcXNFqZyNbyuFJSabkJU = xPmCFphFKpGMpIsczaSKHmMgRPZzJwla.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[0]
    if uePWnTjDNXOJQcXNFqZyNbyuFJSabkJU == 1:
        return xPmCFphFKpGMpIsczaSKHmMgRPZzJwla
    jOtwWmazuqTqvUDEqJxRkeNhFFYkjros = target_batch_size // batched_number
    xPmCFphFKpGMpIsczaSKHmMgRPZzJwla = xPmCFphFKpGMpIsczaSKHmMgRPZzJwla[:jOtwWmazuqTqvUDEqJxRkeNhFFYkjros]
    if jOtwWmazuqTqvUDEqJxRkeNhFFYkjros > xPmCFphFKpGMpIsczaSKHmMgRPZzJwla.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[0]:
        xPmCFphFKpGMpIsczaSKHmMgRPZzJwla = torch.cat([xPmCFphFKpGMpIsczaSKHmMgRPZzJwla] * (jOtwWmazuqTqvUDEqJxRkeNhFFYkjros // xPmCFphFKpGMpIsczaSKHmMgRPZzJwla.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[0]) + [xPmCFphFKpGMpIsczaSKHmMgRPZzJwla[:(jOtwWmazuqTqvUDEqJxRkeNhFFYkjros % xPmCFphFKpGMpIsczaSKHmMgRPZzJwla.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[0])]], yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk=0)
    uePWnTjDNXOJQcXNFqZyNbyuFJSabkJU = xPmCFphFKpGMpIsczaSKHmMgRPZzJwla.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[0]
    if uePWnTjDNXOJQcXNFqZyNbyuFJSabkJU == target_batch_size:
        return xPmCFphFKpGMpIsczaSKHmMgRPZzJwla
    else:
        return torch.cat([xPmCFphFKpGMpIsczaSKHmMgRPZzJwla] * batched_number, yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk=0)
class CWVeLYZPFdaBkgeCgPwDqRzZkbynSwvc:
    def __init__(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc=None):
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.cond_hint_original = None
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.cond_hint = None
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.strength = 1.0
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.timestep_percent_range = (1.0, 0.0)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.timestep_range = None
        if fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc is None:
            fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc = quasar.model_management.aIQypJefEzoiiobeXriYBEHMJwDTvZWS()
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc = fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.previous_controlnet = None
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.HjruQiHdVrxzTiigTfByhAWcFJXqnpgW = False
    def LDyuFUEWXQnihgTEqvVJdRkoAEEdqHhj(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, cond_hint, strength=1.0, timestep_percent_range=(1.0, 0.0)):
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.cond_hint_original = cond_hint
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.strength = strength
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.timestep_percent_range = timestep_percent_range
        return rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS
    def inedfSSNQGlKdNwbapOZJAQSMRiRFMBE(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM, percent_to_timestep_function):
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.timestep_range = (percent_to_timestep_function(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.timestep_percent_range[0]), percent_to_timestep_function(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.timestep_percent_range[1]))
        if rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.previous_controlnet is not None:
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.previous_controlnet.inedfSSNQGlKdNwbapOZJAQSMRiRFMBE(VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM, percent_to_timestep_function)
    def vNmofEXsbaIjqPudAxTruYiypnCtmibE(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, VdWlaPlkqsfXvZUkbqkZdTGuTtMgVkfw):
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.previous_controlnet = VdWlaPlkqsfXvZUkbqkZdTGuTtMgVkfw
        return rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS
    def ADNGMoIYiqFmiietOULLcgwBgBJRVXyd(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS):
        if rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.previous_controlnet is not None:
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.previous_controlnet.ADNGMoIYiqFmiietOULLcgwBgBJRVXyd()
        if rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.cond_hint is not None:
            del rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.cond_hint
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.cond_hint = None
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.timestep_range = None
    def yuXtJvOLzeJppncqVylgYKmpmFYJVrdQ(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS):
        iqymPVpxyjOWChGwBkTemSzHJbnJdAIz = []
        if rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.previous_controlnet is not None:
            iqymPVpxyjOWChGwBkTemSzHJbnJdAIz += rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.previous_controlnet.yuXtJvOLzeJppncqVylgYKmpmFYJVrdQ()
        return iqymPVpxyjOWChGwBkTemSzHJbnJdAIz
    def cxEZDJIlvgwWEipGcqcszbHomLBZFKCo(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, cjHIelcAqVoHWdLcgzuZiBumKNTVADsY):
        cjHIelcAqVoHWdLcgzuZiBumKNTVADsY.cond_hint_original = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.cond_hint_original
        cjHIelcAqVoHWdLcgzuZiBumKNTVADsY.strength = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.strength
        cjHIelcAqVoHWdLcgzuZiBumKNTVADsY.timestep_percent_range = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.timestep_percent_range
    def MGOcWFVZtebtyHBEPpFKWVIQLpSexrKy(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, DDRQlhrNSGpwTrokWitkZipdfbAqBFxv):
        if rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.previous_controlnet is not None:
            return rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.previous_controlnet.MGOcWFVZtebtyHBEPpFKWVIQLpSexrKy(DDRQlhrNSGpwTrokWitkZipdfbAqBFxv)
        return 0
    def AkySdoEEUHRkqYmcyORdNpzCwfNxNwJP(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, NSmEZDQlMumYyWixaxKWEvPezZqFOAMs, control_output, VhhVoGBlTHcbuJzNwTNwXApnpXKQFdoq, tIlfLosbqZZnKoQydAAewJNfOfntjkbV):
        iqymPVpxyjOWChGwBkTemSzHJbnJdAIz = {'input':[], 'middle':[], 'output': []}
        if NSmEZDQlMumYyWixaxKWEvPezZqFOAMs is not None:
            for HCXmerBqIMuTscBONzTGKYapYSxWTYHo in range(len(NSmEZDQlMumYyWixaxKWEvPezZqFOAMs)):
                nyrzKxQtioheHIZujafABgijbCjrWhBU = 'input'
                NECAaWUrFGIXcLimrerEYmxYIykQBfXb = NSmEZDQlMumYyWixaxKWEvPezZqFOAMs[HCXmerBqIMuTscBONzTGKYapYSxWTYHo]
                if NECAaWUrFGIXcLimrerEYmxYIykQBfXb is not None:
                    NECAaWUrFGIXcLimrerEYmxYIykQBfXb *= rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.strength
                    if NECAaWUrFGIXcLimrerEYmxYIykQBfXb.DDRQlhrNSGpwTrokWitkZipdfbAqBFxv != tIlfLosbqZZnKoQydAAewJNfOfntjkbV:
                        NECAaWUrFGIXcLimrerEYmxYIykQBfXb = NECAaWUrFGIXcLimrerEYmxYIykQBfXb.sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ(tIlfLosbqZZnKoQydAAewJNfOfntjkbV)
                iqymPVpxyjOWChGwBkTemSzHJbnJdAIz[nyrzKxQtioheHIZujafABgijbCjrWhBU].insert(0, NECAaWUrFGIXcLimrerEYmxYIykQBfXb)
        if control_output is not None:
            for HCXmerBqIMuTscBONzTGKYapYSxWTYHo in range(len(control_output)):
                if HCXmerBqIMuTscBONzTGKYapYSxWTYHo == (len(control_output) - 1):
                    nyrzKxQtioheHIZujafABgijbCjrWhBU = 'middle'
                    index = 0
                else:
                    nyrzKxQtioheHIZujafABgijbCjrWhBU = 'output'
                    index = HCXmerBqIMuTscBONzTGKYapYSxWTYHo
                NECAaWUrFGIXcLimrerEYmxYIykQBfXb = control_output[HCXmerBqIMuTscBONzTGKYapYSxWTYHo]
                if NECAaWUrFGIXcLimrerEYmxYIykQBfXb is not None:
                    if rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.HjruQiHdVrxzTiigTfByhAWcFJXqnpgW:
                        NECAaWUrFGIXcLimrerEYmxYIykQBfXb = torch.mean(NECAaWUrFGIXcLimrerEYmxYIykQBfXb, yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk=(2, 3), keepdim=True).kYXcbCDGZMxtOlIZeOtGMsNePlSickQL(1, 1, NECAaWUrFGIXcLimrerEYmxYIykQBfXb.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[2], NECAaWUrFGIXcLimrerEYmxYIykQBfXb.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[3])
                    NECAaWUrFGIXcLimrerEYmxYIykQBfXb *= rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.strength
                    if NECAaWUrFGIXcLimrerEYmxYIykQBfXb.DDRQlhrNSGpwTrokWitkZipdfbAqBFxv != tIlfLosbqZZnKoQydAAewJNfOfntjkbV:
                        NECAaWUrFGIXcLimrerEYmxYIykQBfXb = NECAaWUrFGIXcLimrerEYmxYIykQBfXb.sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ(tIlfLosbqZZnKoQydAAewJNfOfntjkbV)
                iqymPVpxyjOWChGwBkTemSzHJbnJdAIz[nyrzKxQtioheHIZujafABgijbCjrWhBU].append(NECAaWUrFGIXcLimrerEYmxYIykQBfXb)
        if VhhVoGBlTHcbuJzNwTNwXApnpXKQFdoq is not None:
            for NECAaWUrFGIXcLimrerEYmxYIykQBfXb in ['input', 'middle', 'output']:
                LDnaTUWTECGaKdJqXUUrFoSvDMujRxwx = iqymPVpxyjOWChGwBkTemSzHJbnJdAIz[NECAaWUrFGIXcLimrerEYmxYIykQBfXb]
                for HCXmerBqIMuTscBONzTGKYapYSxWTYHo in range(len(VhhVoGBlTHcbuJzNwTNwXApnpXKQFdoq[NECAaWUrFGIXcLimrerEYmxYIykQBfXb])):
                    pDdYtKYWkVthQwsKpFOvzlXTtwttYWpm = VhhVoGBlTHcbuJzNwTNwXApnpXKQFdoq[NECAaWUrFGIXcLimrerEYmxYIykQBfXb][HCXmerBqIMuTscBONzTGKYapYSxWTYHo]
                    if HCXmerBqIMuTscBONzTGKYapYSxWTYHo >= len(LDnaTUWTECGaKdJqXUUrFoSvDMujRxwx):
                        LDnaTUWTECGaKdJqXUUrFoSvDMujRxwx.append(pDdYtKYWkVthQwsKpFOvzlXTtwttYWpm)
                    elif pDdYtKYWkVthQwsKpFOvzlXTtwttYWpm is not None:
                        if LDnaTUWTECGaKdJqXUUrFoSvDMujRxwx[HCXmerBqIMuTscBONzTGKYapYSxWTYHo] is None:
                            LDnaTUWTECGaKdJqXUUrFoSvDMujRxwx[HCXmerBqIMuTscBONzTGKYapYSxWTYHo] = pDdYtKYWkVthQwsKpFOvzlXTtwttYWpm
                        else:
                            LDnaTUWTECGaKdJqXUUrFoSvDMujRxwx[HCXmerBqIMuTscBONzTGKYapYSxWTYHo] += pDdYtKYWkVthQwsKpFOvzlXTtwttYWpm
        return iqymPVpxyjOWChGwBkTemSzHJbnJdAIz
class ASOhbXLheqZOwyaVCVwziGwCNciSreag(CWVeLYZPFdaBkgeCgPwDqRzZkbynSwvc):
    def __init__(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, fAZBifOalqUSDAjqeirszagfOSRLKzcX, HjruQiHdVrxzTiigTfByhAWcFJXqnpgW=False, fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc=None):
        super().__init__(fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.fAZBifOalqUSDAjqeirszagfOSRLKzcX = fAZBifOalqUSDAjqeirszagfOSRLKzcX
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.control_model_wrapped = quasar.model_patcher.CmIugCFMKLyCSZlTCvUgomMGPXzvLNTG(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.fAZBifOalqUSDAjqeirszagfOSRLKzcX, load_device=quasar.model_management.aIQypJefEzoiiobeXriYBEHMJwDTvZWS(), SlzENmVKreawuuvgrVSmYHZXOypOtbgl=quasar.model_management.NPYgJTJBLTgTpVRGASjizjQOHZYHkGwk())
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.HjruQiHdVrxzTiigTfByhAWcFJXqnpgW = HjruQiHdVrxzTiigTfByhAWcFJXqnpgW
    def FBPNlUFILIIclgDKQBbOOIcwPxmSSrcB(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, x_noisy, XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz, BuoWBAnnMxyvqTGoSTHbQAlvPFWHbuUf, batched_number):
        VhhVoGBlTHcbuJzNwTNwXApnpXKQFdoq = None
        if rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.previous_controlnet is not None:
            VhhVoGBlTHcbuJzNwTNwXApnpXKQFdoq = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.previous_controlnet.FBPNlUFILIIclgDKQBbOOIcwPxmSSrcB(x_noisy, XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz, BuoWBAnnMxyvqTGoSTHbQAlvPFWHbuUf, batched_number)
        if rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.timestep_range is not None:
            if XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz[0] > rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.timestep_range[0] or XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz[0] < rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.timestep_range[1]:
                if VhhVoGBlTHcbuJzNwTNwXApnpXKQFdoq is not None:
                    return VhhVoGBlTHcbuJzNwTNwXApnpXKQFdoq
                else:
                    return None
        tIlfLosbqZZnKoQydAAewJNfOfntjkbV = x_noisy.DDRQlhrNSGpwTrokWitkZipdfbAqBFxv
        if rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.cond_hint is None or x_noisy.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[2] * 8 != rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.cond_hint.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[2] or x_noisy.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[3] * 8 != rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.cond_hint.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[3]:
            if rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.cond_hint is not None:
                del rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.cond_hint
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.cond_hint = None
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.cond_hint = quasar.utils.common_upscale(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.cond_hint_original, x_noisy.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[3] * 8, x_noisy.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[2] * 8, 'nearest-exact', "center").sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.fAZBifOalqUSDAjqeirszagfOSRLKzcX.DDRQlhrNSGpwTrokWitkZipdfbAqBFxv).sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc)
        if x_noisy.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[0] != rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.cond_hint.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[0]:
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.cond_hint = XaWuNSGWVpidbPpqOMxwLzayHbrlGbVP(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.cond_hint, x_noisy.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[0], batched_number)
        tRdCjhUPYVVxnSEkGmJIHWRitDXRXSZS = BuoWBAnnMxyvqTGoSTHbQAlvPFWHbuUf['c_crossattn']
        ZljqvWVaiqYAYdTFzQHSTXFDKwgstKaW = BuoWBAnnMxyvqTGoSTHbQAlvPFWHbuUf.get('c_adm', None)
        if ZljqvWVaiqYAYdTFzQHSTXFDKwgstKaW is not None:
            ZljqvWVaiqYAYdTFzQHSTXFDKwgstKaW = ZljqvWVaiqYAYdTFzQHSTXFDKwgstKaW.sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.fAZBifOalqUSDAjqeirszagfOSRLKzcX.DDRQlhrNSGpwTrokWitkZipdfbAqBFxv)
        lxwsNGReZsRzPAGinnJJBaOYnaZlIssl = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.fAZBifOalqUSDAjqeirszagfOSRLKzcX(NECAaWUrFGIXcLimrerEYmxYIykQBfXb=x_noisy.sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.fAZBifOalqUSDAjqeirszagfOSRLKzcX.DDRQlhrNSGpwTrokWitkZipdfbAqBFxv), hint=rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.cond_hint, iaqNqpReXPEdYpNiyUIejEPLCqtbtedA=XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz, tRdCjhUPYVVxnSEkGmJIHWRitDXRXSZS=tRdCjhUPYVVxnSEkGmJIHWRitDXRXSZS.sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.fAZBifOalqUSDAjqeirszagfOSRLKzcX.DDRQlhrNSGpwTrokWitkZipdfbAqBFxv), ZljqvWVaiqYAYdTFzQHSTXFDKwgstKaW=ZljqvWVaiqYAYdTFzQHSTXFDKwgstKaW)
        return rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.AkySdoEEUHRkqYmcyORdNpzCwfNxNwJP(None, lxwsNGReZsRzPAGinnJJBaOYnaZlIssl, VhhVoGBlTHcbuJzNwTNwXApnpXKQFdoq, tIlfLosbqZZnKoQydAAewJNfOfntjkbV)
    def copy(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS):
        cjHIelcAqVoHWdLcgzuZiBumKNTVADsY = ASOhbXLheqZOwyaVCVwziGwCNciSreag(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.fAZBifOalqUSDAjqeirszagfOSRLKzcX, HjruQiHdVrxzTiigTfByhAWcFJXqnpgW=rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.HjruQiHdVrxzTiigTfByhAWcFJXqnpgW)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.cxEZDJIlvgwWEipGcqcszbHomLBZFKCo(cjHIelcAqVoHWdLcgzuZiBumKNTVADsY)
        return cjHIelcAqVoHWdLcgzuZiBumKNTVADsY
    def yuXtJvOLzeJppncqVylgYKmpmFYJVrdQ(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS):
        iqymPVpxyjOWChGwBkTemSzHJbnJdAIz = super().yuXtJvOLzeJppncqVylgYKmpmFYJVrdQ()
        iqymPVpxyjOWChGwBkTemSzHJbnJdAIz.append(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.control_model_wrapped)
        return iqymPVpxyjOWChGwBkTemSzHJbnJdAIz
class UGzPlDNXDOmIpGzrytMlyGaClpoPseEY:
    class DhMcMyEvvzmWIEJojbQeGHlzfZKiPzHO(torch.nn.Module):
        def __init__(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, CaDEyeKgggeATJmmSMQfpwrQVIOWCNYZ: int, out_features: int, PvdyIPYzYuxTGYQjZbTucTrRGHTQkavB: bool = True,
                    fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc=None, DDRQlhrNSGpwTrokWitkZipdfbAqBFxv=None) -> None:
            umZdJQgruqrzWHqlMeOMCFLXiRcMXftU = {'device': fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc, 'dtype': DDRQlhrNSGpwTrokWitkZipdfbAqBFxv}
            super().__init__()
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.CaDEyeKgggeATJmmSMQfpwrQVIOWCNYZ = CaDEyeKgggeATJmmSMQfpwrQVIOWCNYZ
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.out_features = out_features
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.RXBOtvKSHQkBvdKDbckmnlphvVygYURP = None
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.kvJZslyswPMVzCnLtIoKrkpdfusdzxSS = None
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.PKmeubCqZPUpSfmqJozYuvYsQsIMTIOn = None
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.PvdyIPYzYuxTGYQjZbTucTrRGHTQkavB = None
        def lqBgIcSWZYylbCPjXksJWDguuSOqoPCJ(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, input):
            if rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.kvJZslyswPMVzCnLtIoKrkpdfusdzxSS is not None:
                return torch.nn.functional.BJkSsAwbTZLfucgvGkDLcVEiRIlYJCmK(input, rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.RXBOtvKSHQkBvdKDbckmnlphvVygYURP.sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ(input.fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc) + (torch.mm(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.kvJZslyswPMVzCnLtIoKrkpdfusdzxSS.flatten(start_dim=1), rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.PKmeubCqZPUpSfmqJozYuvYsQsIMTIOn.flatten(start_dim=1))).reshape(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.RXBOtvKSHQkBvdKDbckmnlphvVygYURP.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg).type(input.DDRQlhrNSGpwTrokWitkZipdfbAqBFxv), rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.PvdyIPYzYuxTGYQjZbTucTrRGHTQkavB)
            else:
                return torch.nn.functional.BJkSsAwbTZLfucgvGkDLcVEiRIlYJCmK(input, rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.RXBOtvKSHQkBvdKDbckmnlphvVygYURP.sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ(input.fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc), rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.PvdyIPYzYuxTGYQjZbTucTrRGHTQkavB)
    class LcFcvNeYCKrBHlNkoWrkqdbxdkNCJBBK(torch.nn.Module):
        def __init__(
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS,
            EbKSIFxpyCpzycRDApduouVsxspHzkTj,
            DjnmEmFIylXDvTfeYtLbwRKPMHUXFjho,
            aBEJjpEOpoRJYkulwSmukddEYErxRnAG,
            NTEWXstfzqNXGESmGkQNFWBaQsGAPlGd=1,
            sdxdTSjnkAOjlGmltQHvLiHRDstMzpAP=0,
            PYWHQpeBxaeMxKXZylrHbMEJvVWcXIiH=1,
            iyOTuhNfRQdmPDAgoyRfWQlAlbwUjdVd=1,
            PvdyIPYzYuxTGYQjZbTucTrRGHTQkavB=True,
            mywsOUGpKnEVweSoLVklSHmxXBoRsFKp='zeros',
            fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc=None,
            DDRQlhrNSGpwTrokWitkZipdfbAqBFxv=None
        ):
            super().__init__()
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.EbKSIFxpyCpzycRDApduouVsxspHzkTj = EbKSIFxpyCpzycRDApduouVsxspHzkTj
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.DjnmEmFIylXDvTfeYtLbwRKPMHUXFjho = DjnmEmFIylXDvTfeYtLbwRKPMHUXFjho
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.aBEJjpEOpoRJYkulwSmukddEYErxRnAG = aBEJjpEOpoRJYkulwSmukddEYErxRnAG
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.NTEWXstfzqNXGESmGkQNFWBaQsGAPlGd = NTEWXstfzqNXGESmGkQNFWBaQsGAPlGd
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.sdxdTSjnkAOjlGmltQHvLiHRDstMzpAP = sdxdTSjnkAOjlGmltQHvLiHRDstMzpAP
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.PYWHQpeBxaeMxKXZylrHbMEJvVWcXIiH = PYWHQpeBxaeMxKXZylrHbMEJvVWcXIiH
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.transposed = False
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.output_padding = 0
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.iyOTuhNfRQdmPDAgoyRfWQlAlbwUjdVd = iyOTuhNfRQdmPDAgoyRfWQlAlbwUjdVd
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.mywsOUGpKnEVweSoLVklSHmxXBoRsFKp = mywsOUGpKnEVweSoLVklSHmxXBoRsFKp
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.RXBOtvKSHQkBvdKDbckmnlphvVygYURP = None
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.PvdyIPYzYuxTGYQjZbTucTrRGHTQkavB = None
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.kvJZslyswPMVzCnLtIoKrkpdfusdzxSS = None
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.PKmeubCqZPUpSfmqJozYuvYsQsIMTIOn = None
        def lqBgIcSWZYylbCPjXksJWDguuSOqoPCJ(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, input):
            if rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.kvJZslyswPMVzCnLtIoKrkpdfusdzxSS is not None:
                return torch.nn.functional.conv2d(input, rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.RXBOtvKSHQkBvdKDbckmnlphvVygYURP.sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ(input.fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc) + (torch.mm(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.kvJZslyswPMVzCnLtIoKrkpdfusdzxSS.flatten(start_dim=1), rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.PKmeubCqZPUpSfmqJozYuvYsQsIMTIOn.flatten(start_dim=1))).reshape(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.RXBOtvKSHQkBvdKDbckmnlphvVygYURP.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg).type(input.DDRQlhrNSGpwTrokWitkZipdfbAqBFxv), rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.PvdyIPYzYuxTGYQjZbTucTrRGHTQkavB, rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.NTEWXstfzqNXGESmGkQNFWBaQsGAPlGd, rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.sdxdTSjnkAOjlGmltQHvLiHRDstMzpAP, rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.PYWHQpeBxaeMxKXZylrHbMEJvVWcXIiH, rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.iyOTuhNfRQdmPDAgoyRfWQlAlbwUjdVd)
            else:
                return torch.nn.functional.conv2d(input, rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.RXBOtvKSHQkBvdKDbckmnlphvVygYURP.sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ(input.fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc), rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.PvdyIPYzYuxTGYQjZbTucTrRGHTQkavB, rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.NTEWXstfzqNXGESmGkQNFWBaQsGAPlGd, rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.sdxdTSjnkAOjlGmltQHvLiHRDstMzpAP, rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.PYWHQpeBxaeMxKXZylrHbMEJvVWcXIiH, rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.iyOTuhNfRQdmPDAgoyRfWQlAlbwUjdVd)
    def XqmPajboESpTdLShIQpHOQZiwGoVuVAj(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, ipYTWVOPDpfJXeTFApPIgldytQSaUFdk, *DukiculvUpjhZIVvaGinshRSKLSTgVVl, **kwargs):
        if ipYTWVOPDpfJXeTFApPIgldytQSaUFdk == 2:
            return rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.LcFcvNeYCKrBHlNkoWrkqdbxdkNCJBBK(*DukiculvUpjhZIVvaGinshRSKLSTgVVl, **kwargs)
        else:
            raise ValueError(f"unsupported dimensions: {dims}")
class NsOGFhWDWacoQQgyquIzEPKdEjPoThNh(ASOhbXLheqZOwyaVCVwziGwCNciSreag):
    def __init__(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, control_weights, HjruQiHdVrxzTiigTfByhAWcFJXqnpgW=False, fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc=None):
        CWVeLYZPFdaBkgeCgPwDqRzZkbynSwvc.__init__(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.control_weights = control_weights
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.HjruQiHdVrxzTiigTfByhAWcFJXqnpgW = HjruQiHdVrxzTiigTfByhAWcFJXqnpgW
    def inedfSSNQGlKdNwbapOZJAQSMRiRFMBE(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM, percent_to_timestep_function):
        super().inedfSSNQGlKdNwbapOZJAQSMRiRFMBE(VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM, percent_to_timestep_function)
        sxroFCrJpvHXNGtTQymYtSHFkashJdmp = VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM.QndHjlfwhEimYkuHnNTDxkEXYaCwJdZe.lLgbOYEeDmYyyxASAROATrPmlqgqYORG.copy()
        sxroFCrJpvHXNGtTQymYtSHFkashJdmp.pop("out_channels")
        sxroFCrJpvHXNGtTQymYtSHFkashJdmp["hint_channels"] = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.control_weights["input_hint_block.0.weight"].BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[1]
        sxroFCrJpvHXNGtTQymYtSHFkashJdmp["operations"] = UGzPlDNXDOmIpGzrytMlyGaClpoPseEY()
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.fAZBifOalqUSDAjqeirszagfOSRLKzcX = quasar.cldm.cldm.ASOhbXLheqZOwyaVCVwziGwCNciSreag(**sxroFCrJpvHXNGtTQymYtSHFkashJdmp)
        DDRQlhrNSGpwTrokWitkZipdfbAqBFxv = VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM.qCYGtbmEmpKHSGaChkRoXdcCONojeSqh()
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.fAZBifOalqUSDAjqeirszagfOSRLKzcX.sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ(DDRQlhrNSGpwTrokWitkZipdfbAqBFxv)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.fAZBifOalqUSDAjqeirszagfOSRLKzcX.sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ(quasar.model_management.aIQypJefEzoiiobeXriYBEHMJwDTvZWS())
        iVdKrUYRzQdKeaSQTeCVqHvUmmINpkSC = VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM.iVdKrUYRzQdKeaSQTeCVqHvUmmINpkSC
        ylGhUFMpxPbtUUTfCZpemVkdanRhWmHa = iVdKrUYRzQdKeaSQTeCVqHvUmmINpkSC.TQRgUMPjEwYAaDvSuzgvheADStCoUKzT()
        FSFdnFCSKycfexqVZvmgnRDarBLgbRlR = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.fAZBifOalqUSDAjqeirszagfOSRLKzcX.TQRgUMPjEwYAaDvSuzgvheADStCoUKzT()
        for EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm in ylGhUFMpxPbtUUTfCZpemVkdanRhWmHa:
            RXBOtvKSHQkBvdKDbckmnlphvVygYURP = quasar.model_management.fJSttSHgRmTiJkiWezuwVxBkdvWTIAvw(ylGhUFMpxPbtUUTfCZpemVkdanRhWmHa[EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm], iVdKrUYRzQdKeaSQTeCVqHvUmmINpkSC, EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm)
            try:
                quasar.utils.set_attr(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.fAZBifOalqUSDAjqeirszagfOSRLKzcX, EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm, RXBOtvKSHQkBvdKDbckmnlphvVygYURP)
            except:
                pass
        for EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm in rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.control_weights:
            if EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm not in {"lora_controlnet"}:
                quasar.utils.set_attr(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.fAZBifOalqUSDAjqeirszagfOSRLKzcX, EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm, rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.control_weights[EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm].sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ(DDRQlhrNSGpwTrokWitkZipdfbAqBFxv).sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ(quasar.model_management.aIQypJefEzoiiobeXriYBEHMJwDTvZWS()))
    def copy(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS):
        cjHIelcAqVoHWdLcgzuZiBumKNTVADsY = NsOGFhWDWacoQQgyquIzEPKdEjPoThNh(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.control_weights, HjruQiHdVrxzTiigTfByhAWcFJXqnpgW=rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.HjruQiHdVrxzTiigTfByhAWcFJXqnpgW)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.cxEZDJIlvgwWEipGcqcszbHomLBZFKCo(cjHIelcAqVoHWdLcgzuZiBumKNTVADsY)
        return cjHIelcAqVoHWdLcgzuZiBumKNTVADsY
    def ADNGMoIYiqFmiietOULLcgwBgBJRVXyd(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS):
        del rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.fAZBifOalqUSDAjqeirszagfOSRLKzcX
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.fAZBifOalqUSDAjqeirszagfOSRLKzcX = None
        super().ADNGMoIYiqFmiietOULLcgwBgBJRVXyd()
    def yuXtJvOLzeJppncqVylgYKmpmFYJVrdQ(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS):
        iqymPVpxyjOWChGwBkTemSzHJbnJdAIz = CWVeLYZPFdaBkgeCgPwDqRzZkbynSwvc.yuXtJvOLzeJppncqVylgYKmpmFYJVrdQ(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS)
        return iqymPVpxyjOWChGwBkTemSzHJbnJdAIz
    def MGOcWFVZtebtyHBEPpFKWVIQLpSexrKy(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, DDRQlhrNSGpwTrokWitkZipdfbAqBFxv):
        return quasar.utils.calculate_parameters(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.control_weights) * quasar.model_management.YtdGBnIPnrvLkEwWTnnTACWnmoKQkWef(DDRQlhrNSGpwTrokWitkZipdfbAqBFxv) + CWVeLYZPFdaBkgeCgPwDqRzZkbynSwvc.MGOcWFVZtebtyHBEPpFKWVIQLpSexrKy(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, DDRQlhrNSGpwTrokWitkZipdfbAqBFxv)
def efoaRkqBAKlDrlLSRqYEUrVOsSVGKXPb(CZOnlrJVXnbYFkZDmLjOAswXNMiGhxHA, VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM=None):
    EQAEUipkOPLJxnGsWwLZaOgFPzgveejh = quasar.utils.load_torch_file(CZOnlrJVXnbYFkZDmLjOAswXNMiGhxHA, safe_load=True)
    if "lora_controlnet" in EQAEUipkOPLJxnGsWwLZaOgFPzgveejh:
        return NsOGFhWDWacoQQgyquIzEPKdEjPoThNh(EQAEUipkOPLJxnGsWwLZaOgFPzgveejh)
    sxroFCrJpvHXNGtTQymYtSHFkashJdmp = None
    if "controlnet_cond_embedding.conv_in.weight" in EQAEUipkOPLJxnGsWwLZaOgFPzgveejh: 
        HzaWhAqAbytRDBNdzYQQeTtjNGGUstsT = quasar.model_management.LlPEFQdsyRQPhjrfArraPsqqOdqUiGhQ()
        sxroFCrJpvHXNGtTQymYtSHFkashJdmp = quasar.model_detection.xySSEzFdNBmsMIgcTEsdJVqMgpLUBwLW(EQAEUipkOPLJxnGsWwLZaOgFPzgveejh, HzaWhAqAbytRDBNdzYQQeTtjNGGUstsT)
        HrtjFPTyNnkcmhLsoJQXqFqnticsQeZI = quasar.utils.unet_to_diffusers(sxroFCrJpvHXNGtTQymYtSHFkashJdmp)
        HrtjFPTyNnkcmhLsoJQXqFqnticsQeZI["controlnet_mid_block.weight"] = "middle_block_out.0.weight"
        HrtjFPTyNnkcmhLsoJQXqFqnticsQeZI["controlnet_mid_block.bias"] = "middle_block_out.0.bias"
        count = 0
        ZkUlcueFlyNvGBkHzyBcsDJMXTjAiuhK = True
        while ZkUlcueFlyNvGBkHzyBcsDJMXTjAiuhK:
            BsNMPzInPMJbfbtzWNcCZMzWMgmxchHs = [".weight", ".bias"]
            for uPePujIqMVDrwNvZQxJajkuaQFAcacjA in BsNMPzInPMJbfbtzWNcCZMzWMgmxchHs:
                gHCkQmZHCJBMKEUaqadAmkHhDHcisxdV = "controlnet_down_blocks.{}{}".format(count, uPePujIqMVDrwNvZQxJajkuaQFAcacjA)
                DSoJmYZgKCYVUKoFisObEjLpEnLaKPxS = "zero_convs.{}.0{}".format(count, uPePujIqMVDrwNvZQxJajkuaQFAcacjA)
                if gHCkQmZHCJBMKEUaqadAmkHhDHcisxdV not in EQAEUipkOPLJxnGsWwLZaOgFPzgveejh:
                    ZkUlcueFlyNvGBkHzyBcsDJMXTjAiuhK = False
                    break
                HrtjFPTyNnkcmhLsoJQXqFqnticsQeZI[gHCkQmZHCJBMKEUaqadAmkHhDHcisxdV] = DSoJmYZgKCYVUKoFisObEjLpEnLaKPxS
            count += 1
        count = 0
        ZkUlcueFlyNvGBkHzyBcsDJMXTjAiuhK = True
        while ZkUlcueFlyNvGBkHzyBcsDJMXTjAiuhK:
            BsNMPzInPMJbfbtzWNcCZMzWMgmxchHs = [".weight", ".bias"]
            for uPePujIqMVDrwNvZQxJajkuaQFAcacjA in BsNMPzInPMJbfbtzWNcCZMzWMgmxchHs:
                if count == 0:
                    gHCkQmZHCJBMKEUaqadAmkHhDHcisxdV = "controlnet_cond_embedding.conv_in{}".format(uPePujIqMVDrwNvZQxJajkuaQFAcacjA)
                else:
                    gHCkQmZHCJBMKEUaqadAmkHhDHcisxdV = "controlnet_cond_embedding.blocks.{}{}".format(count - 1, uPePujIqMVDrwNvZQxJajkuaQFAcacjA)
                DSoJmYZgKCYVUKoFisObEjLpEnLaKPxS = "input_hint_block.{}{}".format(count * 2, uPePujIqMVDrwNvZQxJajkuaQFAcacjA)
                if gHCkQmZHCJBMKEUaqadAmkHhDHcisxdV not in EQAEUipkOPLJxnGsWwLZaOgFPzgveejh:
                    gHCkQmZHCJBMKEUaqadAmkHhDHcisxdV = "controlnet_cond_embedding.conv_out{}".format(uPePujIqMVDrwNvZQxJajkuaQFAcacjA)
                    ZkUlcueFlyNvGBkHzyBcsDJMXTjAiuhK = False
                HrtjFPTyNnkcmhLsoJQXqFqnticsQeZI[gHCkQmZHCJBMKEUaqadAmkHhDHcisxdV] = DSoJmYZgKCYVUKoFisObEjLpEnLaKPxS
            count += 1
        edrLXjDjEmVJdInokgPIUfohVNTWCQLU = {}
        for EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm in HrtjFPTyNnkcmhLsoJQXqFqnticsQeZI:
            if EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm in EQAEUipkOPLJxnGsWwLZaOgFPzgveejh:
                edrLXjDjEmVJdInokgPIUfohVNTWCQLU[HrtjFPTyNnkcmhLsoJQXqFqnticsQeZI[EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm]] = EQAEUipkOPLJxnGsWwLZaOgFPzgveejh.pop(EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm)
        LJhuzEaXYNXkZOieHsnqoyZiLQvLSkyw = EQAEUipkOPLJxnGsWwLZaOgFPzgveejh.keys()
        if len(LJhuzEaXYNXkZOieHsnqoyZiLQvLSkyw) > 0:
            print("leftover keys:", LJhuzEaXYNXkZOieHsnqoyZiLQvLSkyw)
        EQAEUipkOPLJxnGsWwLZaOgFPzgveejh = edrLXjDjEmVJdInokgPIUfohVNTWCQLU
    nslYItjykHOjDbJlIBacMcLnNTavdxBX = 'control_model.zero_convs.0.0.weight'
    ilGGkDiOMlnfsPRyRtDQOSlDElPOUfRz = False
    nyrzKxQtioheHIZujafABgijbCjrWhBU = 'zero_convs.0.0.weight'
    if nslYItjykHOjDbJlIBacMcLnNTavdxBX in EQAEUipkOPLJxnGsWwLZaOgFPzgveejh:
        ilGGkDiOMlnfsPRyRtDQOSlDElPOUfRz = True
        nyrzKxQtioheHIZujafABgijbCjrWhBU = nslYItjykHOjDbJlIBacMcLnNTavdxBX
        mAocOLWlgMJvPYVmSRndfhQdAcKHgPwi = "control_model."
    elif nyrzKxQtioheHIZujafABgijbCjrWhBU in EQAEUipkOPLJxnGsWwLZaOgFPzgveejh:
        mAocOLWlgMJvPYVmSRndfhQdAcKHgPwi = ""
    else:
        faINqTMSsQxdMDXBAGUozMnWtvraUbzj = XqtufPbXGyOEbPTDKemGWnFbYtZQDHHr(EQAEUipkOPLJxnGsWwLZaOgFPzgveejh)
        if faINqTMSsQxdMDXBAGUozMnWtvraUbzj is None:
            print("error checkpoint does not contain controlnet or t2i adapter data", CZOnlrJVXnbYFkZDmLjOAswXNMiGhxHA)
        return faINqTMSsQxdMDXBAGUozMnWtvraUbzj
    if sxroFCrJpvHXNGtTQymYtSHFkashJdmp is None:
        HzaWhAqAbytRDBNdzYQQeTtjNGGUstsT = quasar.model_management.LlPEFQdsyRQPhjrfArraPsqqOdqUiGhQ()
        sxroFCrJpvHXNGtTQymYtSHFkashJdmp = quasar.model_detection.VYidlmtssyLEAglEVVdSlThVhDzTSICW(EQAEUipkOPLJxnGsWwLZaOgFPzgveejh, mAocOLWlgMJvPYVmSRndfhQdAcKHgPwi, HzaWhAqAbytRDBNdzYQQeTtjNGGUstsT).lLgbOYEeDmYyyxASAROATrPmlqgqYORG
    sxroFCrJpvHXNGtTQymYtSHFkashJdmp.pop("out_channels")
    sxroFCrJpvHXNGtTQymYtSHFkashJdmp["hint_channels"] = EQAEUipkOPLJxnGsWwLZaOgFPzgveejh["{}input_hint_block.0.weight".format(mAocOLWlgMJvPYVmSRndfhQdAcKHgPwi)].BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[1]
    fAZBifOalqUSDAjqeirszagfOSRLKzcX = quasar.cldm.cldm.ASOhbXLheqZOwyaVCVwziGwCNciSreag(**sxroFCrJpvHXNGtTQymYtSHFkashJdmp)
    if ilGGkDiOMlnfsPRyRtDQOSlDElPOUfRz:
        if 'difference' in EQAEUipkOPLJxnGsWwLZaOgFPzgveejh:
            if VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM is not None:
                quasar.model_management.hePDtJntacOxTjWwcIlTXDXxmfFUQfAv([VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM])
                DuCZHcDcohTFINauhREJWKOwRCPqBMNf = VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM.wViWufbihckgCqLqPyInDJEhNgDtoTrR()
                for NECAaWUrFGIXcLimrerEYmxYIykQBfXb in EQAEUipkOPLJxnGsWwLZaOgFPzgveejh:
                    tkPkvWIEIQEXKlYhYgjRTZyuUgxixZdY = "control_model."
                    if NECAaWUrFGIXcLimrerEYmxYIykQBfXb.startswith(tkPkvWIEIQEXKlYhYgjRTZyuUgxixZdY):
                        YMtHWSoVUWtpVKrXgdyZtpEaWIUyBxvK = "diffusion_model.{}".format(NECAaWUrFGIXcLimrerEYmxYIykQBfXb[len(tkPkvWIEIQEXKlYhYgjRTZyuUgxixZdY):])
                        if YMtHWSoVUWtpVKrXgdyZtpEaWIUyBxvK in DuCZHcDcohTFINauhREJWKOwRCPqBMNf:
                            NijrVYQUeyxabptLxcGIegvAVssnnDED = EQAEUipkOPLJxnGsWwLZaOgFPzgveejh[NECAaWUrFGIXcLimrerEYmxYIykQBfXb]
                            NijrVYQUeyxabptLxcGIegvAVssnnDED += DuCZHcDcohTFINauhREJWKOwRCPqBMNf[YMtHWSoVUWtpVKrXgdyZtpEaWIUyBxvK].type(NijrVYQUeyxabptLxcGIegvAVssnnDED.DDRQlhrNSGpwTrokWitkZipdfbAqBFxv).sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ(NijrVYQUeyxabptLxcGIegvAVssnnDED.fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc)
            else:
                print("WARNING: Loaded a diff controlnet without a model. It will very likely not work.")
        class QZnYAWjUGrGUSUTGoVBSPqGhLUfRqqRR(torch.nn.Module):
            pass
        AeIrbRXDkpZlClJGwzMknCltTQQdmhvu = QZnYAWjUGrGUSUTGoVBSPqGhLUfRqqRR()
        AeIrbRXDkpZlClJGwzMknCltTQQdmhvu.fAZBifOalqUSDAjqeirszagfOSRLKzcX = fAZBifOalqUSDAjqeirszagfOSRLKzcX
        itInrnlMbMUQsVbCUNKuGZgybidIXUTP, jXybhECNsUqCxKWpEaraZKpjQHkXCoFI = AeIrbRXDkpZlClJGwzMknCltTQQdmhvu.OVlRwgmJvqggImaZMfxKZfQnVYfyhIsc(EQAEUipkOPLJxnGsWwLZaOgFPzgveejh, strict=False)
    else:
        itInrnlMbMUQsVbCUNKuGZgybidIXUTP, jXybhECNsUqCxKWpEaraZKpjQHkXCoFI = fAZBifOalqUSDAjqeirszagfOSRLKzcX.OVlRwgmJvqggImaZMfxKZfQnVYfyhIsc(EQAEUipkOPLJxnGsWwLZaOgFPzgveejh, strict=False)
    print(itInrnlMbMUQsVbCUNKuGZgybidIXUTP, jXybhECNsUqCxKWpEaraZKpjQHkXCoFI)
    if HzaWhAqAbytRDBNdzYQQeTtjNGGUstsT:
        fAZBifOalqUSDAjqeirszagfOSRLKzcX = fAZBifOalqUSDAjqeirszagfOSRLKzcX.XEoZtCUxZMfcPGkBpgLTmSwVAzLKszZq()
    HjruQiHdVrxzTiigTfByhAWcFJXqnpgW = False
    VpsbOZzufynrTFUvvRofTQeRCOCIKJOM = os.path.splitext(CZOnlrJVXnbYFkZDmLjOAswXNMiGhxHA)[0]
    if VpsbOZzufynrTFUvvRofTQeRCOCIKJOM.endswith("_shuffle") or VpsbOZzufynrTFUvvRofTQeRCOCIKJOM.endswith("_shuffle_fp16"): 
        HjruQiHdVrxzTiigTfByhAWcFJXqnpgW = True
    lxwsNGReZsRzPAGinnJJBaOYnaZlIssl = ASOhbXLheqZOwyaVCVwziGwCNciSreag(fAZBifOalqUSDAjqeirszagfOSRLKzcX, HjruQiHdVrxzTiigTfByhAWcFJXqnpgW=HjruQiHdVrxzTiigTfByhAWcFJXqnpgW)
    return lxwsNGReZsRzPAGinnJJBaOYnaZlIssl
class kYWmzLMeubbyOBnaLUHSDZySKcenFKsf(CWVeLYZPFdaBkgeCgPwDqRzZkbynSwvc):
    def __init__(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, t2i_model, channels_in, fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc=None):
        super().__init__(fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.t2i_model = t2i_model
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.channels_in = channels_in
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.NSmEZDQlMumYyWixaxKWEvPezZqFOAMs = None
    def LuMlpJYQiuuNSQlFRXlDpHCOtREPyqwv(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, QfeoFYGsEQNWblsqXsRKWQpzeXgWujaz, yhGxnlfJCKaDHyDtiYhJHxHFcooDKiMM):
        RxZmotBdOdFtUFLUWizeTJiDqLkJiiCu = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.t2i_model.RxZmotBdOdFtUFLUWizeTJiDqLkJiiCu
        QfeoFYGsEQNWblsqXsRKWQpzeXgWujaz = math.ceil(QfeoFYGsEQNWblsqXsRKWQpzeXgWujaz / RxZmotBdOdFtUFLUWizeTJiDqLkJiiCu) * RxZmotBdOdFtUFLUWizeTJiDqLkJiiCu
        yhGxnlfJCKaDHyDtiYhJHxHFcooDKiMM = math.ceil(yhGxnlfJCKaDHyDtiYhJHxHFcooDKiMM / RxZmotBdOdFtUFLUWizeTJiDqLkJiiCu) * RxZmotBdOdFtUFLUWizeTJiDqLkJiiCu
        return QfeoFYGsEQNWblsqXsRKWQpzeXgWujaz, yhGxnlfJCKaDHyDtiYhJHxHFcooDKiMM
    def FBPNlUFILIIclgDKQBbOOIcwPxmSSrcB(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, x_noisy, XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz, BuoWBAnnMxyvqTGoSTHbQAlvPFWHbuUf, batched_number):
        VhhVoGBlTHcbuJzNwTNwXApnpXKQFdoq = None
        if rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.previous_controlnet is not None:
            VhhVoGBlTHcbuJzNwTNwXApnpXKQFdoq = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.previous_controlnet.FBPNlUFILIIclgDKQBbOOIcwPxmSSrcB(x_noisy, XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz, BuoWBAnnMxyvqTGoSTHbQAlvPFWHbuUf, batched_number)
        if rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.timestep_range is not None:
            if XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz[0] > rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.timestep_range[0] or XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz[0] < rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.timestep_range[1]:
                if VhhVoGBlTHcbuJzNwTNwXApnpXKQFdoq is not None:
                    return VhhVoGBlTHcbuJzNwTNwXApnpXKQFdoq
                else:
                    return {}
        if rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.cond_hint is None or x_noisy.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[2] * 8 != rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.cond_hint.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[2] or x_noisy.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[3] * 8 != rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.cond_hint.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[3]:
            if rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.cond_hint is not None:
                del rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.cond_hint
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.NSmEZDQlMumYyWixaxKWEvPezZqFOAMs = None
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.cond_hint = None
            QfeoFYGsEQNWblsqXsRKWQpzeXgWujaz, yhGxnlfJCKaDHyDtiYhJHxHFcooDKiMM = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.LuMlpJYQiuuNSQlFRXlDpHCOtREPyqwv(x_noisy.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[3] * 8, x_noisy.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[2] * 8)
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.cond_hint = quasar.utils.common_upscale(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.cond_hint_original, QfeoFYGsEQNWblsqXsRKWQpzeXgWujaz, yhGxnlfJCKaDHyDtiYhJHxHFcooDKiMM, 'nearest-exact', "center").float().sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc)
            if rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.channels_in == 1 and rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.cond_hint.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[1] > 1:
                rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.cond_hint = torch.mean(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.cond_hint, 1, keepdim=True)
        if x_noisy.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[0] != rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.cond_hint.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[0]:
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.cond_hint = XaWuNSGWVpidbPpqOMxwLzayHbrlGbVP(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.cond_hint, x_noisy.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[0], batched_number)
        if rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.NSmEZDQlMumYyWixaxKWEvPezZqFOAMs is None:
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.t2i_model.sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ(x_noisy.DDRQlhrNSGpwTrokWitkZipdfbAqBFxv)
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.t2i_model.sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc)
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.NSmEZDQlMumYyWixaxKWEvPezZqFOAMs = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.t2i_model(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.cond_hint.sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ(x_noisy.DDRQlhrNSGpwTrokWitkZipdfbAqBFxv))
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.t2i_model.cpu()
        NSmEZDQlMumYyWixaxKWEvPezZqFOAMs = list(map(lambda GlZreLQjBCiBptpFgmbsMbhjFlMgPVav: None if GlZreLQjBCiBptpFgmbsMbhjFlMgPVav is None else GlZreLQjBCiBptpFgmbsMbhjFlMgPVav.tEcQvpBwXwdqvKxRTLEBROBUyPoodldL(), rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.NSmEZDQlMumYyWixaxKWEvPezZqFOAMs))
        rnBVwgYeGkHoRDXjLPBaCTIXNAZYBHGr = None
        if rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.t2i_model.woDONBBxfEKwjIgxrZSxOuFkXiNJfLMx == True:
            rnBVwgYeGkHoRDXjLPBaCTIXNAZYBHGr = NSmEZDQlMumYyWixaxKWEvPezZqFOAMs[-1:]
            NSmEZDQlMumYyWixaxKWEvPezZqFOAMs = NSmEZDQlMumYyWixaxKWEvPezZqFOAMs[:-1]
        return rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.AkySdoEEUHRkqYmcyORdNpzCwfNxNwJP(NSmEZDQlMumYyWixaxKWEvPezZqFOAMs, rnBVwgYeGkHoRDXjLPBaCTIXNAZYBHGr, VhhVoGBlTHcbuJzNwTNwXApnpXKQFdoq, x_noisy.DDRQlhrNSGpwTrokWitkZipdfbAqBFxv)
    def copy(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS):
        cjHIelcAqVoHWdLcgzuZiBumKNTVADsY = kYWmzLMeubbyOBnaLUHSDZySKcenFKsf(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.t2i_model, rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.channels_in)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.cxEZDJIlvgwWEipGcqcszbHomLBZFKCo(cjHIelcAqVoHWdLcgzuZiBumKNTVADsY)
        return cjHIelcAqVoHWdLcgzuZiBumKNTVADsY
def XqtufPbXGyOEbPTDKemGWnFbYtZQDHHr(VDZFBupqMvTJWEjPAtOrplMAFbilScHU):
    if 'adapter' in VDZFBupqMvTJWEjPAtOrplMAFbilScHU:
        VDZFBupqMvTJWEjPAtOrplMAFbilScHU = VDZFBupqMvTJWEjPAtOrplMAFbilScHU['adapter']
    if 'adapter.body.0.resnets.0.block1.weight' in VDZFBupqMvTJWEjPAtOrplMAFbilScHU: 
        NDhsofsNPmnpSHcgIjBvcCByfaQWPkYh = {}
        for HCXmerBqIMuTscBONzTGKYapYSxWTYHo in range(4):
            for VyjoFEMsihtolZHiuwJuxJKmDsIroAsQ in range(2):
                NDhsofsNPmnpSHcgIjBvcCByfaQWPkYh["adapter.body.{}.resnets.{}.".format(HCXmerBqIMuTscBONzTGKYapYSxWTYHo, VyjoFEMsihtolZHiuwJuxJKmDsIroAsQ)] = "body.{}.".format(HCXmerBqIMuTscBONzTGKYapYSxWTYHo * 2 + VyjoFEMsihtolZHiuwJuxJKmDsIroAsQ)
            NDhsofsNPmnpSHcgIjBvcCByfaQWPkYh["adapter.body.{}.".format(HCXmerBqIMuTscBONzTGKYapYSxWTYHo, VyjoFEMsihtolZHiuwJuxJKmDsIroAsQ)] = "body.{}.".format(HCXmerBqIMuTscBONzTGKYapYSxWTYHo * 2)
        NDhsofsNPmnpSHcgIjBvcCByfaQWPkYh["adapter."] = ""
        VDZFBupqMvTJWEjPAtOrplMAFbilScHU = quasar.utils.state_dict_prefix_replace(VDZFBupqMvTJWEjPAtOrplMAFbilScHU, NDhsofsNPmnpSHcgIjBvcCByfaQWPkYh)
    keys = VDZFBupqMvTJWEjPAtOrplMAFbilScHU.keys()
    if "body.0.in_conv.weight" in keys:
        lZFDQGrsxjmuPKhiBycouNmmtdgourGD = VDZFBupqMvTJWEjPAtOrplMAFbilScHU['body.0.in_conv.weight'].BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[1]
        wRBTXeioMFnznzhRFkdHUfDGrzDEdXkW = quasar.t2i_adapter.adapter.qgeSgitlrURgBLleGvUEMOpdoielgAYL(lZFDQGrsxjmuPKhiBycouNmmtdgourGD=lZFDQGrsxjmuPKhiBycouNmmtdgourGD, channels=[320, 640, 1280, 1280], nums_rb=4)
    elif 'conv_in.weight' in keys:
        lZFDQGrsxjmuPKhiBycouNmmtdgourGD = VDZFBupqMvTJWEjPAtOrplMAFbilScHU['conv_in.weight'].BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[1]
        EiApFIHKVDYyxTYijPXtjyqRuQDlhpED = VDZFBupqMvTJWEjPAtOrplMAFbilScHU['conv_in.weight'].BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[0]
        gcxqXDVvHPuehBbNpJwzTveeqNWyZNze = VDZFBupqMvTJWEjPAtOrplMAFbilScHU['body.0.block2.weight'].BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[2]
        BMidABgMadzWxSilVoOpGtdqLSQhQAjN = False
        ItEAZxZWSseqVIzQYmOkYFmeWfMebwkh = list(filter(lambda GlZreLQjBCiBptpFgmbsMbhjFlMgPVav: GlZreLQjBCiBptpFgmbsMbhjFlMgPVav.endswith("down_opt.op.weight"), keys))
        if len(ItEAZxZWSseqVIzQYmOkYFmeWfMebwkh) > 0:
            BMidABgMadzWxSilVoOpGtdqLSQhQAjN = True
        woDONBBxfEKwjIgxrZSxOuFkXiNJfLMx = False
        if lZFDQGrsxjmuPKhiBycouNmmtdgourGD == 256 or lZFDQGrsxjmuPKhiBycouNmmtdgourGD == 768:
            woDONBBxfEKwjIgxrZSxOuFkXiNJfLMx = True
        wRBTXeioMFnznzhRFkdHUfDGrzDEdXkW = quasar.t2i_adapter.adapter.ZPOXjvfzXIIyNqBeetwWBnTgzptlxmjU(lZFDQGrsxjmuPKhiBycouNmmtdgourGD=lZFDQGrsxjmuPKhiBycouNmmtdgourGD, channels=[EiApFIHKVDYyxTYijPXtjyqRuQDlhpED, EiApFIHKVDYyxTYijPXtjyqRuQDlhpED*2, EiApFIHKVDYyxTYijPXtjyqRuQDlhpED*4, EiApFIHKVDYyxTYijPXtjyqRuQDlhpED*4][:4], nums_rb=2, gcxqXDVvHPuehBbNpJwzTveeqNWyZNze=gcxqXDVvHPuehBbNpJwzTveeqNWyZNze, sk=True, BMidABgMadzWxSilVoOpGtdqLSQhQAjN=BMidABgMadzWxSilVoOpGtdqLSQhQAjN, woDONBBxfEKwjIgxrZSxOuFkXiNJfLMx=woDONBBxfEKwjIgxrZSxOuFkXiNJfLMx)
    else:
        return None
    itInrnlMbMUQsVbCUNKuGZgybidIXUTP, jXybhECNsUqCxKWpEaraZKpjQHkXCoFI = wRBTXeioMFnznzhRFkdHUfDGrzDEdXkW.OVlRwgmJvqggImaZMfxKZfQnVYfyhIsc(VDZFBupqMvTJWEjPAtOrplMAFbilScHU)
    if len(itInrnlMbMUQsVbCUNKuGZgybidIXUTP) > 0:
        print("t2i missing", itInrnlMbMUQsVbCUNKuGZgybidIXUTP)
    if len(jXybhECNsUqCxKWpEaraZKpjQHkXCoFI) > 0:
        print("t2i unexpected", jXybhECNsUqCxKWpEaraZKpjQHkXCoFI)
    return kYWmzLMeubbyOBnaLUHSDZySKcenFKsf(wRBTXeioMFnznzhRFkdHUfDGrzDEdXkW, wRBTXeioMFnznzhRFkdHUfDGrzDEdXkW.input_channels)
