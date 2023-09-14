import os
import time
hZQMFPwtakjynkeurEyZiPAYMqwfPAZc = set(['.ckpt', '.pt', '.bin', '.pth', '.safetensors'])
RtqMYVjkHvPjjwaAjZzZiDKOhSnoAwQG = {}
TkQiWYaXtJuzzefZQkRCbaAzWTYQqpiC = os.path.dirname(os.path.realpath(__file__))
iTgDKqnzsINaQjOfADlnzvTrjwAMQoHM = os.path.join(TkQiWYaXtJuzzefZQkRCbaAzWTYQqpiC, "models")
RtqMYVjkHvPjjwaAjZzZiDKOhSnoAwQG["checkpoints"] = ([os.path.join(iTgDKqnzsINaQjOfADlnzvTrjwAMQoHM, "checkpoints")], hZQMFPwtakjynkeurEyZiPAYMqwfPAZc)
RtqMYVjkHvPjjwaAjZzZiDKOhSnoAwQG["configs"] = ([os.path.join(iTgDKqnzsINaQjOfADlnzvTrjwAMQoHM, "configs")], [".yaml"])
RtqMYVjkHvPjjwaAjZzZiDKOhSnoAwQG["loras"] = ([os.path.join(iTgDKqnzsINaQjOfADlnzvTrjwAMQoHM, "loras")], hZQMFPwtakjynkeurEyZiPAYMqwfPAZc)
RtqMYVjkHvPjjwaAjZzZiDKOhSnoAwQG["vae"] = ([os.path.join(iTgDKqnzsINaQjOfADlnzvTrjwAMQoHM, "vae")], hZQMFPwtakjynkeurEyZiPAYMqwfPAZc)
RtqMYVjkHvPjjwaAjZzZiDKOhSnoAwQG["clip"] = ([os.path.join(iTgDKqnzsINaQjOfADlnzvTrjwAMQoHM, "clip")], hZQMFPwtakjynkeurEyZiPAYMqwfPAZc)
RtqMYVjkHvPjjwaAjZzZiDKOhSnoAwQG["unet"] = ([os.path.join(iTgDKqnzsINaQjOfADlnzvTrjwAMQoHM, "unet")], hZQMFPwtakjynkeurEyZiPAYMqwfPAZc)
RtqMYVjkHvPjjwaAjZzZiDKOhSnoAwQG["clip_vision"] = ([os.path.join(iTgDKqnzsINaQjOfADlnzvTrjwAMQoHM, "clip_vision")], hZQMFPwtakjynkeurEyZiPAYMqwfPAZc)
RtqMYVjkHvPjjwaAjZzZiDKOhSnoAwQG["style_models"] = ([os.path.join(iTgDKqnzsINaQjOfADlnzvTrjwAMQoHM, "style_models")], hZQMFPwtakjynkeurEyZiPAYMqwfPAZc)
RtqMYVjkHvPjjwaAjZzZiDKOhSnoAwQG["embeddings"] = ([os.path.join(iTgDKqnzsINaQjOfADlnzvTrjwAMQoHM, "embeddings")], hZQMFPwtakjynkeurEyZiPAYMqwfPAZc)
RtqMYVjkHvPjjwaAjZzZiDKOhSnoAwQG["diffusers"] = ([os.path.join(iTgDKqnzsINaQjOfADlnzvTrjwAMQoHM, "diffusers")], ["folder"])
RtqMYVjkHvPjjwaAjZzZiDKOhSnoAwQG["vae_approx"] = ([os.path.join(iTgDKqnzsINaQjOfADlnzvTrjwAMQoHM, "vae_approx")], hZQMFPwtakjynkeurEyZiPAYMqwfPAZc)
RtqMYVjkHvPjjwaAjZzZiDKOhSnoAwQG["controlnet"] = ([os.path.join(iTgDKqnzsINaQjOfADlnzvTrjwAMQoHM, "controlnet"), os.path.join(iTgDKqnzsINaQjOfADlnzvTrjwAMQoHM, "t2i_adapter")], hZQMFPwtakjynkeurEyZiPAYMqwfPAZc)
RtqMYVjkHvPjjwaAjZzZiDKOhSnoAwQG["gligen"] = ([os.path.join(iTgDKqnzsINaQjOfADlnzvTrjwAMQoHM, "gligen")], hZQMFPwtakjynkeurEyZiPAYMqwfPAZc)
RtqMYVjkHvPjjwaAjZzZiDKOhSnoAwQG["upscale_models"] = ([os.path.join(iTgDKqnzsINaQjOfADlnzvTrjwAMQoHM, "upscale_models")], hZQMFPwtakjynkeurEyZiPAYMqwfPAZc)
RtqMYVjkHvPjjwaAjZzZiDKOhSnoAwQG["custom_nodes"] = ([os.path.join(TkQiWYaXtJuzzefZQkRCbaAzWTYQqpiC, "custom_nodes")], [])
RtqMYVjkHvPjjwaAjZzZiDKOhSnoAwQG["hypernetworks"] = ([os.path.join(iTgDKqnzsINaQjOfADlnzvTrjwAMQoHM, "hypernetworks")], hZQMFPwtakjynkeurEyZiPAYMqwfPAZc)
GtSyetIaLksMxiwaHjRuEDPDczomOxfB = os.path.join(os.path.dirname(os.path.realpath(__file__)), "output")
sBxeZEvOLuqHjzzCBAVYRZTjCrezBxCX = os.path.join(os.path.dirname(os.path.realpath(__file__)), "temp")
JVnqMUCDCOqhSclOtgLoQNuaQwivvlwP = os.path.join(os.path.dirname(os.path.realpath(__file__)), "input")
JyZmzIiPwdUaqrBdrvxSwDliHEuoQwXM = {}
if not os.path.exists(JVnqMUCDCOqhSclOtgLoQNuaQwivvlwP):
    os.makedirs(JVnqMUCDCOqhSclOtgLoQNuaQwivvlwP)
def QaqVOGrCQsMzyJzwFXeqRMUkMfnKwrHp(DIUNPQiJKWsgpSdsJVPWmcWtoPKBTsdh):
    global GtSyetIaLksMxiwaHjRuEDPDczomOxfB
    GtSyetIaLksMxiwaHjRuEDPDczomOxfB = DIUNPQiJKWsgpSdsJVPWmcWtoPKBTsdh
def UjFfHXPSSdYnVuSiGnNlPxKKudSjKFNY(CtmzHSDvDEVGVbXeTIhzZgbBXVjSiNhP):
    global sBxeZEvOLuqHjzzCBAVYRZTjCrezBxCX
    sBxeZEvOLuqHjzzCBAVYRZTjCrezBxCX = CtmzHSDvDEVGVbXeTIhzZgbBXVjSiNhP
def gZpMXpjIEjIdWmJXOqOJEBRXYgziLydo():
    global GtSyetIaLksMxiwaHjRuEDPDczomOxfB
    return GtSyetIaLksMxiwaHjRuEDPDczomOxfB
def PlSKGeZYRqtlMHiaBRCToWuXDcNhJEvq():
    global sBxeZEvOLuqHjzzCBAVYRZTjCrezBxCX
    return sBxeZEvOLuqHjzzCBAVYRZTjCrezBxCX
def oLxzopmIeTVwZiWTpRvVAVRpJiaEjmiS():
    global JVnqMUCDCOqhSclOtgLoQNuaQwivvlwP
    return JVnqMUCDCOqhSclOtgLoQNuaQwivvlwP
def kxrHWrKUsAImLcADDJwQctHfTpGpGvug(type_name):
    if type_name == "output":
        return gZpMXpjIEjIdWmJXOqOJEBRXYgziLydo()
    if type_name == "temp":
        return PlSKGeZYRqtlMHiaBRCToWuXDcNhJEvq()
    if type_name == "input":
        return oLxzopmIeTVwZiWTpRvVAVRpJiaEjmiS()
    return None
def ZouPnEJNuptYlYBxNIdTXWRhksIQlBbt(pSfJNVvqLWVlUeHdpahCTGSrSPJYAnEQ):
    if pSfJNVvqLWVlUeHdpahCTGSrSPJYAnEQ.endswith("[output]"):
        qQaBpsOaFfJUnrTGkifLbJyCyczdakPQ = gZpMXpjIEjIdWmJXOqOJEBRXYgziLydo()
        pSfJNVvqLWVlUeHdpahCTGSrSPJYAnEQ = pSfJNVvqLWVlUeHdpahCTGSrSPJYAnEQ[:-9]
    elif pSfJNVvqLWVlUeHdpahCTGSrSPJYAnEQ.endswith("[input]"):
        qQaBpsOaFfJUnrTGkifLbJyCyczdakPQ = oLxzopmIeTVwZiWTpRvVAVRpJiaEjmiS()
        pSfJNVvqLWVlUeHdpahCTGSrSPJYAnEQ = pSfJNVvqLWVlUeHdpahCTGSrSPJYAnEQ[:-8]
    elif pSfJNVvqLWVlUeHdpahCTGSrSPJYAnEQ.endswith("[temp]"):
        qQaBpsOaFfJUnrTGkifLbJyCyczdakPQ = PlSKGeZYRqtlMHiaBRCToWuXDcNhJEvq()
        pSfJNVvqLWVlUeHdpahCTGSrSPJYAnEQ = pSfJNVvqLWVlUeHdpahCTGSrSPJYAnEQ[:-7]
    else:
        return pSfJNVvqLWVlUeHdpahCTGSrSPJYAnEQ, None
    return pSfJNVvqLWVlUeHdpahCTGSrSPJYAnEQ, qQaBpsOaFfJUnrTGkifLbJyCyczdakPQ
def OPtRRiXTVYmRqsnzHEbbUWCzjjPfVhOl(pSfJNVvqLWVlUeHdpahCTGSrSPJYAnEQ, default_dir=None):
    pSfJNVvqLWVlUeHdpahCTGSrSPJYAnEQ, qQaBpsOaFfJUnrTGkifLbJyCyczdakPQ = ZouPnEJNuptYlYBxNIdTXWRhksIQlBbt(pSfJNVvqLWVlUeHdpahCTGSrSPJYAnEQ)
    if qQaBpsOaFfJUnrTGkifLbJyCyczdakPQ is None:
        if default_dir is not None:
            qQaBpsOaFfJUnrTGkifLbJyCyczdakPQ = default_dir
        else:
            qQaBpsOaFfJUnrTGkifLbJyCyczdakPQ = oLxzopmIeTVwZiWTpRvVAVRpJiaEjmiS()  
    return os.path.join(qQaBpsOaFfJUnrTGkifLbJyCyczdakPQ, pSfJNVvqLWVlUeHdpahCTGSrSPJYAnEQ)
def LuEtoKSPwnkgulAqhArQxPlLlkJrpWJM(pSfJNVvqLWVlUeHdpahCTGSrSPJYAnEQ):
    pSfJNVvqLWVlUeHdpahCTGSrSPJYAnEQ, qQaBpsOaFfJUnrTGkifLbJyCyczdakPQ = ZouPnEJNuptYlYBxNIdTXWRhksIQlBbt(pSfJNVvqLWVlUeHdpahCTGSrSPJYAnEQ)
    if qQaBpsOaFfJUnrTGkifLbJyCyczdakPQ is None:
        qQaBpsOaFfJUnrTGkifLbJyCyczdakPQ = oLxzopmIeTVwZiWTpRvVAVRpJiaEjmiS()  
    jGKkchjlDQuvRrYKaTApaOEWXvxjRZoh = os.path.join(qQaBpsOaFfJUnrTGkifLbJyCyczdakPQ, pSfJNVvqLWVlUeHdpahCTGSrSPJYAnEQ)
    return os.path.exists(jGKkchjlDQuvRrYKaTApaOEWXvxjRZoh)
def tXboLlrRieKqwPeTtnDtKOeZJiYAGlLt(OiSDAWttaBayZhaRXvjSPjBrXgoDRtfZ, full_folder_path):
    global RtqMYVjkHvPjjwaAjZzZiDKOhSnoAwQG
    if OiSDAWttaBayZhaRXvjSPjBrXgoDRtfZ in RtqMYVjkHvPjjwaAjZzZiDKOhSnoAwQG:
        RtqMYVjkHvPjjwaAjZzZiDKOhSnoAwQG[OiSDAWttaBayZhaRXvjSPjBrXgoDRtfZ][0].append(full_folder_path)
    else:
        RtqMYVjkHvPjjwaAjZzZiDKOhSnoAwQG[OiSDAWttaBayZhaRXvjSPjBrXgoDRtfZ] = ([full_folder_path], set())
def HXYNxZJQjELjaaxuKjoZoxFzWaIvOYmT(OiSDAWttaBayZhaRXvjSPjBrXgoDRtfZ):
    return RtqMYVjkHvPjjwaAjZzZiDKOhSnoAwQG[OiSDAWttaBayZhaRXvjSPjBrXgoDRtfZ][0][:]
def obGgHnWHZHxVqLnvnUwXaOsmgUVmduqj(directory, hycpXyDmpuOeQeuwvqXUjhiJtDOFTONs=None):
    if not os.path.isdir(directory):
        return [], {}
    if hycpXyDmpuOeQeuwvqXUjhiJtDOFTONs is None:
        hycpXyDmpuOeQeuwvqXUjhiJtDOFTONs = []
    EpPkhmvnuPCNYOnbTkWPbRocxmdOwtHI = []
    tMqhONnNTXdwHJmOQatOuImsYofVgJxi = {directory: os.path.getmtime(directory)}
    for XCrmLuQijIRiBbHWvECkfaKyKAGmZfFW, fCAMhpfBWcaJjstQXXJyoBiwKjkwqxdP, mkvCrqyejrekyuWxgtHkShApwhhCDyMu in os.walk(directory, followlinks=True, topdown=True):
        fCAMhpfBWcaJjstQXXJyoBiwKjkwqxdP[:] = [TXGwYXNLgQsYzfHHpRBDJGFCFZEClzIo for TXGwYXNLgQsYzfHHpRBDJGFCFZEClzIo in fCAMhpfBWcaJjstQXXJyoBiwKjkwqxdP if TXGwYXNLgQsYzfHHpRBDJGFCFZEClzIo not in hycpXyDmpuOeQeuwvqXUjhiJtDOFTONs]
        for cUwDjpDYeDLcRutcYgVbXhXpxYeYFdHt in mkvCrqyejrekyuWxgtHkShApwhhCDyMu:
            qNWMfFLBJiRgAvaCCCCahKsWaeudkTaD = os.path.relpath(os.path.join(XCrmLuQijIRiBbHWvECkfaKyKAGmZfFW, cUwDjpDYeDLcRutcYgVbXhXpxYeYFdHt), directory)
            EpPkhmvnuPCNYOnbTkWPbRocxmdOwtHI.append(qNWMfFLBJiRgAvaCCCCahKsWaeudkTaD)
        for TXGwYXNLgQsYzfHHpRBDJGFCFZEClzIo in fCAMhpfBWcaJjstQXXJyoBiwKjkwqxdP:
            path = os.path.join(XCrmLuQijIRiBbHWvECkfaKyKAGmZfFW, TXGwYXNLgQsYzfHHpRBDJGFCFZEClzIo)
            tMqhONnNTXdwHJmOQatOuImsYofVgJxi[path] = os.path.getmtime(path)
    return EpPkhmvnuPCNYOnbTkWPbRocxmdOwtHI, tMqhONnNTXdwHJmOQatOuImsYofVgJxi
def ogrHHnnoHaDAeFerfHoOKjouTxChktKm(DTcHrFlDIwbrZDZHTOmAOTxRFqptCgyE, HnjgYzcYVPzWBFjtnXmWmmBUkGpTxjgv):
    return sorted(list(filter(lambda GlZreLQjBCiBptpFgmbsMbhjFlMgPVav: os.path.splitext(GlZreLQjBCiBptpFgmbsMbhjFlMgPVav)[-1].lower() in HnjgYzcYVPzWBFjtnXmWmmBUkGpTxjgv, DTcHrFlDIwbrZDZHTOmAOTxRFqptCgyE)))
def TIUEGMgxYSpXjfhmEGzFnNfGAqtlBBKE(OiSDAWttaBayZhaRXvjSPjBrXgoDRtfZ, VpsbOZzufynrTFUvvRofTQeRCOCIKJOM):
    global RtqMYVjkHvPjjwaAjZzZiDKOhSnoAwQG
    if OiSDAWttaBayZhaRXvjSPjBrXgoDRtfZ not in RtqMYVjkHvPjjwaAjZzZiDKOhSnoAwQG:
        return None
    LjTAnyqWGFlIaOwfqQTfGKbkmjrAjQnu = RtqMYVjkHvPjjwaAjZzZiDKOhSnoAwQG[OiSDAWttaBayZhaRXvjSPjBrXgoDRtfZ]
    VpsbOZzufynrTFUvvRofTQeRCOCIKJOM = os.path.relpath(os.path.join("/", VpsbOZzufynrTFUvvRofTQeRCOCIKJOM), "/")
    for NECAaWUrFGIXcLimrerEYmxYIykQBfXb in LjTAnyqWGFlIaOwfqQTfGKbkmjrAjQnu[0]:
        BvZbFoQIcgYmFXROwptYbIKgzYJORrYY = os.path.join(NECAaWUrFGIXcLimrerEYmxYIykQBfXb, VpsbOZzufynrTFUvvRofTQeRCOCIKJOM)
        if os.path.isfile(BvZbFoQIcgYmFXROwptYbIKgzYJORrYY):
            return BvZbFoQIcgYmFXROwptYbIKgzYJORrYY
    return None
def wZITfTxkrUGlgkNhyVkQeGQnBOOGviUn(OiSDAWttaBayZhaRXvjSPjBrXgoDRtfZ):
    global RtqMYVjkHvPjjwaAjZzZiDKOhSnoAwQG
    GgpaBLoBmoIhHNvNAUUHscrTPvveyTGt = set()
    LjTAnyqWGFlIaOwfqQTfGKbkmjrAjQnu = RtqMYVjkHvPjjwaAjZzZiDKOhSnoAwQG[OiSDAWttaBayZhaRXvjSPjBrXgoDRtfZ]
    MeRskWbjCfHyBXapOnnGcEMlMZxTeiIR = {}
    for NECAaWUrFGIXcLimrerEYmxYIykQBfXb in LjTAnyqWGFlIaOwfqQTfGKbkmjrAjQnu[0]:
        DTcHrFlDIwbrZDZHTOmAOTxRFqptCgyE, ZBGyBxxmhCoTmaItLhabPXHZIdhzfXYB = obGgHnWHZHxVqLnvnUwXaOsmgUVmduqj(NECAaWUrFGIXcLimrerEYmxYIykQBfXb, hycpXyDmpuOeQeuwvqXUjhiJtDOFTONs=[".git"])
        GgpaBLoBmoIhHNvNAUUHscrTPvveyTGt.update(ogrHHnnoHaDAeFerfHoOKjouTxChktKm(DTcHrFlDIwbrZDZHTOmAOTxRFqptCgyE, LjTAnyqWGFlIaOwfqQTfGKbkmjrAjQnu[1]))
        MeRskWbjCfHyBXapOnnGcEMlMZxTeiIR = {**MeRskWbjCfHyBXapOnnGcEMlMZxTeiIR, **ZBGyBxxmhCoTmaItLhabPXHZIdhzfXYB}
    return (sorted(list(GgpaBLoBmoIhHNvNAUUHscrTPvveyTGt)), MeRskWbjCfHyBXapOnnGcEMlMZxTeiIR, time.perf_counter())
def cbzhDWvXQBiEgEVdjzZaBlkWnnmGvfgj(OiSDAWttaBayZhaRXvjSPjBrXgoDRtfZ):
    global JyZmzIiPwdUaqrBdrvxSwDliHEuoQwXM
    global RtqMYVjkHvPjjwaAjZzZiDKOhSnoAwQG
    if OiSDAWttaBayZhaRXvjSPjBrXgoDRtfZ not in JyZmzIiPwdUaqrBdrvxSwDliHEuoQwXM:
        return None
    iqymPVpxyjOWChGwBkTemSzHJbnJdAIz = JyZmzIiPwdUaqrBdrvxSwDliHEuoQwXM[OiSDAWttaBayZhaRXvjSPjBrXgoDRtfZ]
    if time.perf_counter() < (iqymPVpxyjOWChGwBkTemSzHJbnJdAIz[2] + 0.5):
        return iqymPVpxyjOWChGwBkTemSzHJbnJdAIz
    for NECAaWUrFGIXcLimrerEYmxYIykQBfXb in iqymPVpxyjOWChGwBkTemSzHJbnJdAIz[1]:
        ufReozYqFDHrDJiiCgVhHqnMnsesjFSb = iqymPVpxyjOWChGwBkTemSzHJbnJdAIz[1][NECAaWUrFGIXcLimrerEYmxYIykQBfXb]
        OwJCTJVwyMUEtfjtMzVQMjEELeqLNhyX = NECAaWUrFGIXcLimrerEYmxYIykQBfXb
        if os.path.getmtime(OwJCTJVwyMUEtfjtMzVQMjEELeqLNhyX) != ufReozYqFDHrDJiiCgVhHqnMnsesjFSb:
            return None
    LjTAnyqWGFlIaOwfqQTfGKbkmjrAjQnu = RtqMYVjkHvPjjwaAjZzZiDKOhSnoAwQG[OiSDAWttaBayZhaRXvjSPjBrXgoDRtfZ]
    for NECAaWUrFGIXcLimrerEYmxYIykQBfXb in LjTAnyqWGFlIaOwfqQTfGKbkmjrAjQnu[0]:
        if os.path.isdir(NECAaWUrFGIXcLimrerEYmxYIykQBfXb):
            if NECAaWUrFGIXcLimrerEYmxYIykQBfXb not in iqymPVpxyjOWChGwBkTemSzHJbnJdAIz[1]:
                return None
    return iqymPVpxyjOWChGwBkTemSzHJbnJdAIz
def DYvodbeLLCWlQGasCGeYTFNFKZRpPvmd(OiSDAWttaBayZhaRXvjSPjBrXgoDRtfZ):
    iqymPVpxyjOWChGwBkTemSzHJbnJdAIz = cbzhDWvXQBiEgEVdjzZaBlkWnnmGvfgj(OiSDAWttaBayZhaRXvjSPjBrXgoDRtfZ)
    if iqymPVpxyjOWChGwBkTemSzHJbnJdAIz is None:
        iqymPVpxyjOWChGwBkTemSzHJbnJdAIz = wZITfTxkrUGlgkNhyVkQeGQnBOOGviUn(OiSDAWttaBayZhaRXvjSPjBrXgoDRtfZ)
        global JyZmzIiPwdUaqrBdrvxSwDliHEuoQwXM
        JyZmzIiPwdUaqrBdrvxSwDliHEuoQwXM[OiSDAWttaBayZhaRXvjSPjBrXgoDRtfZ] = iqymPVpxyjOWChGwBkTemSzHJbnJdAIz
    return list(iqymPVpxyjOWChGwBkTemSzHJbnJdAIz[0])
def RzAZobMvYWLmMtiqbeSollhpzISOJhWp(azafsUqgjjnMJDTDVblsTwqgMmfrAEPm, DIUNPQiJKWsgpSdsJVPWmcWtoPKBTsdh, image_width=0, image_height=0):
    def kvXDIOWWdUPJRythbyaKVomFIZtNHPIf(VpsbOZzufynrTFUvvRofTQeRCOCIKJOM):
        EHPJUgMmqUaZlktbaRCBTfLvSXvWOHtL = len(os.path.basename(azafsUqgjjnMJDTDVblsTwqgMmfrAEPm))
        mAocOLWlgMJvPYVmSRndfhQdAcKHgPwi = VpsbOZzufynrTFUvvRofTQeRCOCIKJOM[:EHPJUgMmqUaZlktbaRCBTfLvSXvWOHtL + 1]
        try:
            hCVGAfCArAJbgwQyBsUtCdmTkaFHlUwI = int(VpsbOZzufynrTFUvvRofTQeRCOCIKJOM[EHPJUgMmqUaZlktbaRCBTfLvSXvWOHtL + 1:].split('_')[0])
        except:
            hCVGAfCArAJbgwQyBsUtCdmTkaFHlUwI = 0
        return (hCVGAfCArAJbgwQyBsUtCdmTkaFHlUwI, mAocOLWlgMJvPYVmSRndfhQdAcKHgPwi)
    def UWfTdcFvxzbgLumqlxvZmrHJBBJcgAIR(input, image_width, image_height):
        input = input.replace("%width%", str(image_width))
        input = input.replace("%height%", str(image_height))
        return input
    azafsUqgjjnMJDTDVblsTwqgMmfrAEPm = UWfTdcFvxzbgLumqlxvZmrHJBBJcgAIR(azafsUqgjjnMJDTDVblsTwqgMmfrAEPm, image_width, image_height)
    EijzAwkTdadIdbBCcDEUbEYNNcstskwi = os.path.dirname(os.path.normpath(azafsUqgjjnMJDTDVblsTwqgMmfrAEPm))
    VpsbOZzufynrTFUvvRofTQeRCOCIKJOM = os.path.basename(os.path.normpath(azafsUqgjjnMJDTDVblsTwqgMmfrAEPm))
    NSnmtWjKbAQhROMkmRknqzSaUCojgOin = os.path.join(DIUNPQiJKWsgpSdsJVPWmcWtoPKBTsdh, EijzAwkTdadIdbBCcDEUbEYNNcstskwi)
    if os.path.commonpath((DIUNPQiJKWsgpSdsJVPWmcWtoPKBTsdh, os.path.abspath(NSnmtWjKbAQhROMkmRknqzSaUCojgOin))) != DIUNPQiJKWsgpSdsJVPWmcWtoPKBTsdh:
        print("Saving image outside the output folder is not allowed.")
        return {}
    try:
        etmXhuRDTfPuCYAlpkCmiMFiODmDHghZ = max(filter(lambda GlZreLQjBCiBptpFgmbsMbhjFlMgPVav: GlZreLQjBCiBptpFgmbsMbhjFlMgPVav[1][:-1] == VpsbOZzufynrTFUvvRofTQeRCOCIKJOM and GlZreLQjBCiBptpFgmbsMbhjFlMgPVav[1][-1] == "_", map(kvXDIOWWdUPJRythbyaKVomFIZtNHPIf, os.listdir(NSnmtWjKbAQhROMkmRknqzSaUCojgOin))))[0] + 1
    except ValueError:
        etmXhuRDTfPuCYAlpkCmiMFiODmDHghZ = 1
    except FileNotFoundError:
        os.makedirs(NSnmtWjKbAQhROMkmRknqzSaUCojgOin, exist_ok=True)
        etmXhuRDTfPuCYAlpkCmiMFiODmDHghZ = 1
    return NSnmtWjKbAQhROMkmRknqzSaUCojgOin, VpsbOZzufynrTFUvvRofTQeRCOCIKJOM, etmXhuRDTfPuCYAlpkCmiMFiODmDHghZ, EijzAwkTdadIdbBCcDEUbEYNNcstskwi, azafsUqgjjnMJDTDVblsTwqgMmfrAEPm
