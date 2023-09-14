import os
import sys
import copy
import json
import threading
import heapq
import traceback
import gc
import torch
import nodes
import quasar.model_management
def RJtMQsrZYSczxBuFhYkbBGspnaWoaVek(kxdrqSDQHJnEllMOtIqUSWLnexkmvsXK, QVFkmcxYKbGpDWdwPuNpltEZeinkgFbR, OkGbEfBOlXJkHHiIxPCEdAigBwQFWinB, TPdbMzICOHVoRDIwYkBuPquOyCZwkKrH={}, qKBREHoSgcMHYVCNTapmPyODbBOyQAyv={}, vngfynKJfsHLAoqKbHSpKIzjZdROnsZl={}):
    uGbXgzaTSMvbSorVuKNkZxJbIiUjVYlo = QVFkmcxYKbGpDWdwPuNpltEZeinkgFbR.hGTeyOvpHejlssWPjkjTHIgcOKnCfnQl()
    DShVzzegkrjgHxkcKhTwHIgrLbIYjoVy = {}
    for NECAaWUrFGIXcLimrerEYmxYIykQBfXb in kxdrqSDQHJnEllMOtIqUSWLnexkmvsXK:
        BLXYdQZMdSUVXqHWfCWrRSRgDkKAoCGR = kxdrqSDQHJnEllMOtIqUSWLnexkmvsXK[NECAaWUrFGIXcLimrerEYmxYIykQBfXb]
        if isinstance(BLXYdQZMdSUVXqHWfCWrRSRgDkKAoCGR, list):
            rLPruVdmzKDqcYsJgVZgWfYEgKWyJgxe = BLXYdQZMdSUVXqHWfCWrRSRgDkKAoCGR[0]
            WjdDprUAwUFaYOLeMvbVzAgLBDwMxTFK = BLXYdQZMdSUVXqHWfCWrRSRgDkKAoCGR[1]
            if rLPruVdmzKDqcYsJgVZgWfYEgKWyJgxe not in TPdbMzICOHVoRDIwYkBuPquOyCZwkKrH:
                DShVzzegkrjgHxkcKhTwHIgrLbIYjoVy[NECAaWUrFGIXcLimrerEYmxYIykQBfXb] = (None,)
                continue
            glUavvDBRdewYAKFdDMMzdAIZsTAFOso = TPdbMzICOHVoRDIwYkBuPquOyCZwkKrH[rLPruVdmzKDqcYsJgVZgWfYEgKWyJgxe][WjdDprUAwUFaYOLeMvbVzAgLBDwMxTFK]
            DShVzzegkrjgHxkcKhTwHIgrLbIYjoVy[NECAaWUrFGIXcLimrerEYmxYIykQBfXb] = glUavvDBRdewYAKFdDMMzdAIZsTAFOso
        else:
            if ("required" in uGbXgzaTSMvbSorVuKNkZxJbIiUjVYlo and NECAaWUrFGIXcLimrerEYmxYIykQBfXb in uGbXgzaTSMvbSorVuKNkZxJbIiUjVYlo["required"]) or ("optional" in uGbXgzaTSMvbSorVuKNkZxJbIiUjVYlo and NECAaWUrFGIXcLimrerEYmxYIykQBfXb in uGbXgzaTSMvbSorVuKNkZxJbIiUjVYlo["optional"]):
                DShVzzegkrjgHxkcKhTwHIgrLbIYjoVy[NECAaWUrFGIXcLimrerEYmxYIykQBfXb] = [BLXYdQZMdSUVXqHWfCWrRSRgDkKAoCGR]
    if "hidden" in uGbXgzaTSMvbSorVuKNkZxJbIiUjVYlo:
        xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab = uGbXgzaTSMvbSorVuKNkZxJbIiUjVYlo["hidden"]
        for NECAaWUrFGIXcLimrerEYmxYIykQBfXb in xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab:
            if xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab[NECAaWUrFGIXcLimrerEYmxYIykQBfXb] == "PROMPT":
                DShVzzegkrjgHxkcKhTwHIgrLbIYjoVy[NECAaWUrFGIXcLimrerEYmxYIykQBfXb] = [qKBREHoSgcMHYVCNTapmPyODbBOyQAyv]
            if xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab[NECAaWUrFGIXcLimrerEYmxYIykQBfXb] == "EXTRA_PNGINFO":
                if "extra_pnginfo" in vngfynKJfsHLAoqKbHSpKIzjZdROnsZl:
                    DShVzzegkrjgHxkcKhTwHIgrLbIYjoVy[NECAaWUrFGIXcLimrerEYmxYIykQBfXb] = [vngfynKJfsHLAoqKbHSpKIzjZdROnsZl['extra_pnginfo']]
            if xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab[NECAaWUrFGIXcLimrerEYmxYIykQBfXb] == "UNIQUE_ID":
                DShVzzegkrjgHxkcKhTwHIgrLbIYjoVy[NECAaWUrFGIXcLimrerEYmxYIykQBfXb] = [OkGbEfBOlXJkHHiIxPCEdAigBwQFWinB]
    return DShVzzegkrjgHxkcKhTwHIgrLbIYjoVy
def znDMGjLEJesTIoWKbaCIQXMLYNShsqxP(glUavvDBRdewYAKFdDMMzdAIZsTAFOso, DShVzzegkrjgHxkcKhTwHIgrLbIYjoVy, txqWbeldWuTXEOzUjapZMrWhymqrYFLd, allow_interrupt=False):
    nrzzjWZiZOhSQXuToFNicultWHLyobFj = False
    if hasattr(glUavvDBRdewYAKFdDMMzdAIZsTAFOso, "INPUT_IS_LIST"):
        nrzzjWZiZOhSQXuToFNicultWHLyobFj = glUavvDBRdewYAKFdDMMzdAIZsTAFOso.INPUT_IS_LIST
    if len(DShVzzegkrjgHxkcKhTwHIgrLbIYjoVy) == 0:
        ZcbBuNPClHbUKxcWeKHVacLbZJkIWLWS = 0
    else:
        ZcbBuNPClHbUKxcWeKHVacLbZJkIWLWS = max([len(NECAaWUrFGIXcLimrerEYmxYIykQBfXb) for NECAaWUrFGIXcLimrerEYmxYIykQBfXb in DShVzzegkrjgHxkcKhTwHIgrLbIYjoVy.values()])
    def OPwrJaxiFWabzHbUCfNObotDqSQOnmxh(TXGwYXNLgQsYzfHHpRBDJGFCFZEClzIo, HCXmerBqIMuTscBONzTGKYapYSxWTYHo):
        EOnJWuiasqMtRknqRbMQgprwiwcUugIw = dict()
        for EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm,powGafreWfwlSAqPpTpUhFgpFVqCPavl in TXGwYXNLgQsYzfHHpRBDJGFCFZEClzIo.items():
            EOnJWuiasqMtRknqRbMQgprwiwcUugIw[EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm] = powGafreWfwlSAqPpTpUhFgpFVqCPavl[HCXmerBqIMuTscBONzTGKYapYSxWTYHo if len(powGafreWfwlSAqPpTpUhFgpFVqCPavl) > HCXmerBqIMuTscBONzTGKYapYSxWTYHo else -1]
        return EOnJWuiasqMtRknqRbMQgprwiwcUugIw
    NRctuwUflnRJCsQaTaCNgYJowifAWPqJ = []
    if nrzzjWZiZOhSQXuToFNicultWHLyobFj:
        if allow_interrupt:
            nodes.cZCqaSABLYzQIyICXPawBbAkRZgRglpn()
        NRctuwUflnRJCsQaTaCNgYJowifAWPqJ.append(getattr(glUavvDBRdewYAKFdDMMzdAIZsTAFOso, txqWbeldWuTXEOzUjapZMrWhymqrYFLd)(**DShVzzegkrjgHxkcKhTwHIgrLbIYjoVy))
    elif ZcbBuNPClHbUKxcWeKHVacLbZJkIWLWS == 0:
        if allow_interrupt:
            nodes.cZCqaSABLYzQIyICXPawBbAkRZgRglpn()
        NRctuwUflnRJCsQaTaCNgYJowifAWPqJ.append(getattr(glUavvDBRdewYAKFdDMMzdAIZsTAFOso, txqWbeldWuTXEOzUjapZMrWhymqrYFLd)())
    else:
        for HCXmerBqIMuTscBONzTGKYapYSxWTYHo in range(ZcbBuNPClHbUKxcWeKHVacLbZJkIWLWS):
            if allow_interrupt:
                nodes.cZCqaSABLYzQIyICXPawBbAkRZgRglpn()
            NRctuwUflnRJCsQaTaCNgYJowifAWPqJ.append(getattr(glUavvDBRdewYAKFdDMMzdAIZsTAFOso, txqWbeldWuTXEOzUjapZMrWhymqrYFLd)(**OPwrJaxiFWabzHbUCfNObotDqSQOnmxh(DShVzzegkrjgHxkcKhTwHIgrLbIYjoVy, HCXmerBqIMuTscBONzTGKYapYSxWTYHo)))
    return NRctuwUflnRJCsQaTaCNgYJowifAWPqJ
def DBaAmcPKQcrbNgODAUAdHBgSmPIIDflI(glUavvDBRdewYAKFdDMMzdAIZsTAFOso, DShVzzegkrjgHxkcKhTwHIgrLbIYjoVy):
    NRctuwUflnRJCsQaTaCNgYJowifAWPqJ = []
    YBofEVxzfbVmrXEuTuWTcPdFRMQyiGeI = []
    xXYmQfpdSaWHJJrEDZpCApMgIhYmIZXy = znDMGjLEJesTIoWKbaCIQXMLYNShsqxP(glUavvDBRdewYAKFdDMMzdAIZsTAFOso, DShVzzegkrjgHxkcKhTwHIgrLbIYjoVy, glUavvDBRdewYAKFdDMMzdAIZsTAFOso.DCeBXQFyPFIKUXphdMmctDGwHwXgHyTw, allow_interrupt=True)
    for r in xXYmQfpdSaWHJJrEDZpCApMgIhYmIZXy:
        if isinstance(r, dict):
            if 'ui' in r:
                YBofEVxzfbVmrXEuTuWTcPdFRMQyiGeI.append(r['ui'])
            if 'result' in r:
                NRctuwUflnRJCsQaTaCNgYJowifAWPqJ.append(r['result'])
        else:
            NRctuwUflnRJCsQaTaCNgYJowifAWPqJ.append(r)
    pwTxzdNTJGMWEFORftJTEtPYMMiKwDuP = []
    if len(NRctuwUflnRJCsQaTaCNgYJowifAWPqJ) > 0:
        bbQjlsHRHfubilyXLBASZXqxYbqVxJhd = [False] * len(NRctuwUflnRJCsQaTaCNgYJowifAWPqJ[0])
        if hasattr(glUavvDBRdewYAKFdDMMzdAIZsTAFOso, "OUTPUT_IS_LIST"):
            bbQjlsHRHfubilyXLBASZXqxYbqVxJhd = glUavvDBRdewYAKFdDMMzdAIZsTAFOso.OUTPUT_IS_LIST
        for HCXmerBqIMuTscBONzTGKYapYSxWTYHo, dFiizBHZrqWNWmNknTfnkaJemHQcoXIa in zip(range(len(NRctuwUflnRJCsQaTaCNgYJowifAWPqJ[0])), bbQjlsHRHfubilyXLBASZXqxYbqVxJhd):
            if dFiizBHZrqWNWmNknTfnkaJemHQcoXIa:
                pwTxzdNTJGMWEFORftJTEtPYMMiKwDuP.append([NECAaWUrFGIXcLimrerEYmxYIykQBfXb for ZbJdszKEJvcRHFMveXqyJhenPPuBTdnt  in LDnaTUWTECGaKdJqXUUrFoSvDMujRxwx[HCXmerBqIMuTscBONzTGKYapYSxWTYHo]])
            else:
                pwTxzdNTJGMWEFORftJTEtPYMMiKwDuP.append([LDnaTUWTECGaKdJqXUUrFoSvDMujRxwx[HCXmerBqIMuTscBONzTGKYapYSxWTYHo] for LDnaTUWTECGaKdJqXUUrFoSvDMujRxwx in NRctuwUflnRJCsQaTaCNgYJowifAWPqJ])
    IzXOxVroakejZIFmNItuuBtUNMYwmFVr = dict()    
    if len(YBofEVxzfbVmrXEuTuWTcPdFRMQyiGeI) > 0:
        IzXOxVroakejZIFmNItuuBtUNMYwmFVr = {EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm: [ZljqvWVaiqYAYdTFzQHSTXFDKwgstKaW for NECAaWUrFGIXcLimrerEYmxYIykQBfXb in YBofEVxzfbVmrXEuTuWTcPdFRMQyiGeI for ZljqvWVaiqYAYdTFzQHSTXFDKwgstKaW in NECAaWUrFGIXcLimrerEYmxYIykQBfXb[EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm]] for EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm in YBofEVxzfbVmrXEuTuWTcPdFRMQyiGeI[0].keys()}
    return pwTxzdNTJGMWEFORftJTEtPYMMiKwDuP, IzXOxVroakejZIFmNItuuBtUNMYwmFVr
def vXBdjntkFWIYwygzQeRANmLvdjIBYhKV(NECAaWUrFGIXcLimrerEYmxYIykQBfXb):
    if NECAaWUrFGIXcLimrerEYmxYIykQBfXb is None:
        return None
    elif isinstance(NECAaWUrFGIXcLimrerEYmxYIykQBfXb, (int, float, bool, str)):
        return NECAaWUrFGIXcLimrerEYmxYIykQBfXb
    else:
        return str(NECAaWUrFGIXcLimrerEYmxYIykQBfXb)
def jwltmDqWYcEtFryNbsfrnywMaYpQMVcH(REDIKAYZymAzMirxFmomyJtEGktwcqlE, qKBREHoSgcMHYVCNTapmPyODbBOyQAyv, TPdbMzICOHVoRDIwYkBuPquOyCZwkKrH, current_item, vngfynKJfsHLAoqKbHSpKIzjZdROnsZl, hLymBLypSLZVPrzSiZmuWHxSGFfDqIkt, AFursZnPuECGUFTkCjDbdYIYmtroiqfB, outputs_ui, object_storage):
    OkGbEfBOlXJkHHiIxPCEdAigBwQFWinB = current_item
    kxdrqSDQHJnEllMOtIqUSWLnexkmvsXK = qKBREHoSgcMHYVCNTapmPyODbBOyQAyv[OkGbEfBOlXJkHHiIxPCEdAigBwQFWinB]['inputs']
    pBgHpIpwWsKYNXAVImuNRvNCqoZgeKOO = qKBREHoSgcMHYVCNTapmPyODbBOyQAyv[OkGbEfBOlXJkHHiIxPCEdAigBwQFWinB]['class_type']
    QVFkmcxYKbGpDWdwPuNpltEZeinkgFbR = nodes.wJhMfuyrPNjllkMCYXdJHMhubCAizKhP[pBgHpIpwWsKYNXAVImuNRvNCqoZgeKOO]
    if OkGbEfBOlXJkHHiIxPCEdAigBwQFWinB in TPdbMzICOHVoRDIwYkBuPquOyCZwkKrH:
        return (True, None, None)
    for NECAaWUrFGIXcLimrerEYmxYIykQBfXb in kxdrqSDQHJnEllMOtIqUSWLnexkmvsXK:
        BLXYdQZMdSUVXqHWfCWrRSRgDkKAoCGR = kxdrqSDQHJnEllMOtIqUSWLnexkmvsXK[NECAaWUrFGIXcLimrerEYmxYIykQBfXb]
        if isinstance(BLXYdQZMdSUVXqHWfCWrRSRgDkKAoCGR, list):
            rLPruVdmzKDqcYsJgVZgWfYEgKWyJgxe = BLXYdQZMdSUVXqHWfCWrRSRgDkKAoCGR[0]
            WjdDprUAwUFaYOLeMvbVzAgLBDwMxTFK = BLXYdQZMdSUVXqHWfCWrRSRgDkKAoCGR[1]
            if rLPruVdmzKDqcYsJgVZgWfYEgKWyJgxe not in TPdbMzICOHVoRDIwYkBuPquOyCZwkKrH:
                EpPkhmvnuPCNYOnbTkWPbRocxmdOwtHI = jwltmDqWYcEtFryNbsfrnywMaYpQMVcH(REDIKAYZymAzMirxFmomyJtEGktwcqlE, qKBREHoSgcMHYVCNTapmPyODbBOyQAyv, TPdbMzICOHVoRDIwYkBuPquOyCZwkKrH, rLPruVdmzKDqcYsJgVZgWfYEgKWyJgxe, vngfynKJfsHLAoqKbHSpKIzjZdROnsZl, hLymBLypSLZVPrzSiZmuWHxSGFfDqIkt, AFursZnPuECGUFTkCjDbdYIYmtroiqfB, outputs_ui, object_storage)
                if EpPkhmvnuPCNYOnbTkWPbRocxmdOwtHI[0] is not True:
                    return EpPkhmvnuPCNYOnbTkWPbRocxmdOwtHI
    DShVzzegkrjgHxkcKhTwHIgrLbIYjoVy = None
    try:
        DShVzzegkrjgHxkcKhTwHIgrLbIYjoVy = RJtMQsrZYSczxBuFhYkbBGspnaWoaVek(kxdrqSDQHJnEllMOtIqUSWLnexkmvsXK, QVFkmcxYKbGpDWdwPuNpltEZeinkgFbR, OkGbEfBOlXJkHHiIxPCEdAigBwQFWinB, TPdbMzICOHVoRDIwYkBuPquOyCZwkKrH, qKBREHoSgcMHYVCNTapmPyODbBOyQAyv, vngfynKJfsHLAoqKbHSpKIzjZdROnsZl)
        if REDIKAYZymAzMirxFmomyJtEGktwcqlE.client_id is not None:
            REDIKAYZymAzMirxFmomyJtEGktwcqlE.last_node_id = OkGbEfBOlXJkHHiIxPCEdAigBwQFWinB
            REDIKAYZymAzMirxFmomyJtEGktwcqlE.qIpzeiOiFfpTobMBTgFPHfiZRTmLDpoa("executing", { "node": OkGbEfBOlXJkHHiIxPCEdAigBwQFWinB, "prompt_id": AFursZnPuECGUFTkCjDbdYIYmtroiqfB }, REDIKAYZymAzMirxFmomyJtEGktwcqlE.client_id)
        glUavvDBRdewYAKFdDMMzdAIZsTAFOso = object_storage.get((OkGbEfBOlXJkHHiIxPCEdAigBwQFWinB, pBgHpIpwWsKYNXAVImuNRvNCqoZgeKOO), None)
        if glUavvDBRdewYAKFdDMMzdAIZsTAFOso is None:
            glUavvDBRdewYAKFdDMMzdAIZsTAFOso = QVFkmcxYKbGpDWdwPuNpltEZeinkgFbR()
            object_storage[(OkGbEfBOlXJkHHiIxPCEdAigBwQFWinB, pBgHpIpwWsKYNXAVImuNRvNCqoZgeKOO)] = glUavvDBRdewYAKFdDMMzdAIZsTAFOso
        oKXnheZmKUgLmHLpgyoPSPxoJRtreEeT, eZaqEmMnTjjnrKsbSvVCkdUkKhCIEFte = DBaAmcPKQcrbNgODAUAdHBgSmPIIDflI(glUavvDBRdewYAKFdDMMzdAIZsTAFOso, DShVzzegkrjgHxkcKhTwHIgrLbIYjoVy)
        TPdbMzICOHVoRDIwYkBuPquOyCZwkKrH[OkGbEfBOlXJkHHiIxPCEdAigBwQFWinB] = oKXnheZmKUgLmHLpgyoPSPxoJRtreEeT
        if len(eZaqEmMnTjjnrKsbSvVCkdUkKhCIEFte) > 0:
            outputs_ui[OkGbEfBOlXJkHHiIxPCEdAigBwQFWinB] = eZaqEmMnTjjnrKsbSvVCkdUkKhCIEFte
            if REDIKAYZymAzMirxFmomyJtEGktwcqlE.client_id is not None:
                REDIKAYZymAzMirxFmomyJtEGktwcqlE.qIpzeiOiFfpTobMBTgFPHfiZRTmLDpoa("executed", { "node": OkGbEfBOlXJkHHiIxPCEdAigBwQFWinB, "output": eZaqEmMnTjjnrKsbSvVCkdUkKhCIEFte, "prompt_id": AFursZnPuECGUFTkCjDbdYIYmtroiqfB }, REDIKAYZymAzMirxFmomyJtEGktwcqlE.client_id)
    except quasar.model_management.FcmhbKAfUbwHtuUFKflJjsPfbobaJqvP as iex:
        print("Processing interrupted")
        rEpmbaVyTehRFHKUTTOQaWBomKXtQrfp = {
            "node_id": OkGbEfBOlXJkHHiIxPCEdAigBwQFWinB,
        }
        return (False, rEpmbaVyTehRFHKUTTOQaWBomKXtQrfp, iex)
    except Exception as YJIyBYFuSbfDGbTSGjpGoODShSYXRpRz:
        lNaMhSVGVjaibIkJNZqMMpHyVpGvwQoR, _, MFEPhxDvKhTtHiHybdiYCFrdHKnPxOpk = sys.exc_info()
        fHgxuGFQyywnXHSwGpHqZhvbEmkNjhFR = TofpJDHPPEZZyHHPZTbiDOLhnocJgpJM(lNaMhSVGVjaibIkJNZqMMpHyVpGvwQoR)
        uidszEKMKruxeyaXZxcuylCpvtcAsFOd = {}
        if DShVzzegkrjgHxkcKhTwHIgrLbIYjoVy is not None:
            uidszEKMKruxeyaXZxcuylCpvtcAsFOd = {}
            for name, kxdrqSDQHJnEllMOtIqUSWLnexkmvsXK in DShVzzegkrjgHxkcKhTwHIgrLbIYjoVy.items():
                uidszEKMKruxeyaXZxcuylCpvtcAsFOd[name] = [vXBdjntkFWIYwygzQeRANmLvdjIBYhKV(NECAaWUrFGIXcLimrerEYmxYIykQBfXb) for NECAaWUrFGIXcLimrerEYmxYIykQBfXb in kxdrqSDQHJnEllMOtIqUSWLnexkmvsXK]
        RZUjxcnGzofahyVgHKOLhDxiUfRPmtli = {}
        for WUnsDKMtnjEEHIRpEKBjpWsxTOaQPOEe, EIzAayMGFMYCpfiUIUfbqYGhmDtmOFdv in TPdbMzICOHVoRDIwYkBuPquOyCZwkKrH.items():
            RZUjxcnGzofahyVgHKOLhDxiUfRPmtli[WUnsDKMtnjEEHIRpEKBjpWsxTOaQPOEe] = [[vXBdjntkFWIYwygzQeRANmLvdjIBYhKV(NECAaWUrFGIXcLimrerEYmxYIykQBfXb) for NECAaWUrFGIXcLimrerEYmxYIykQBfXb in QBYRnCrsHIHjuDAPBxgVhibLQMjOwjJW] for QBYRnCrsHIHjuDAPBxgVhibLQMjOwjJW in EIzAayMGFMYCpfiUIUfbqYGhmDtmOFdv]
        print("!!! Exception during processing !!!")
        print(traceback.format_exc())
        rEpmbaVyTehRFHKUTTOQaWBomKXtQrfp = {
            "node_id": OkGbEfBOlXJkHHiIxPCEdAigBwQFWinB,
            "exception_message": str(YJIyBYFuSbfDGbTSGjpGoODShSYXRpRz),
            "exception_type": fHgxuGFQyywnXHSwGpHqZhvbEmkNjhFR,
            "traceback": traceback.format_tb(MFEPhxDvKhTtHiHybdiYCFrdHKnPxOpk),
            "current_inputs": uidszEKMKruxeyaXZxcuylCpvtcAsFOd,
            "current_outputs": RZUjxcnGzofahyVgHKOLhDxiUfRPmtli
        }
        return (False, rEpmbaVyTehRFHKUTTOQaWBomKXtQrfp, YJIyBYFuSbfDGbTSGjpGoODShSYXRpRz)
    hLymBLypSLZVPrzSiZmuWHxSGFfDqIkt.add(OkGbEfBOlXJkHHiIxPCEdAigBwQFWinB)
    return (True, None, None)
def XwfrXrUSmKYfmtrwrTSzVawyDMlBRcHb(qKBREHoSgcMHYVCNTapmPyODbBOyQAyv, TPdbMzICOHVoRDIwYkBuPquOyCZwkKrH, current_item):
    OkGbEfBOlXJkHHiIxPCEdAigBwQFWinB = current_item
    kxdrqSDQHJnEllMOtIqUSWLnexkmvsXK = qKBREHoSgcMHYVCNTapmPyODbBOyQAyv[OkGbEfBOlXJkHHiIxPCEdAigBwQFWinB]['inputs']
    HzwTtBCehyHPCSVtKTYMWmRdWIdQMSXR = []
    if OkGbEfBOlXJkHHiIxPCEdAigBwQFWinB in TPdbMzICOHVoRDIwYkBuPquOyCZwkKrH:
        return []
    for NECAaWUrFGIXcLimrerEYmxYIykQBfXb in kxdrqSDQHJnEllMOtIqUSWLnexkmvsXK:
        BLXYdQZMdSUVXqHWfCWrRSRgDkKAoCGR = kxdrqSDQHJnEllMOtIqUSWLnexkmvsXK[NECAaWUrFGIXcLimrerEYmxYIykQBfXb]
        if isinstance(BLXYdQZMdSUVXqHWfCWrRSRgDkKAoCGR, list):
            rLPruVdmzKDqcYsJgVZgWfYEgKWyJgxe = BLXYdQZMdSUVXqHWfCWrRSRgDkKAoCGR[0]
            WjdDprUAwUFaYOLeMvbVzAgLBDwMxTFK = BLXYdQZMdSUVXqHWfCWrRSRgDkKAoCGR[1]
            if rLPruVdmzKDqcYsJgVZgWfYEgKWyJgxe not in TPdbMzICOHVoRDIwYkBuPquOyCZwkKrH:
                HzwTtBCehyHPCSVtKTYMWmRdWIdQMSXR += XwfrXrUSmKYfmtrwrTSzVawyDMlBRcHb(qKBREHoSgcMHYVCNTapmPyODbBOyQAyv, TPdbMzICOHVoRDIwYkBuPquOyCZwkKrH, rLPruVdmzKDqcYsJgVZgWfYEgKWyJgxe)
    return HzwTtBCehyHPCSVtKTYMWmRdWIdQMSXR + [OkGbEfBOlXJkHHiIxPCEdAigBwQFWinB]
def iCiuUpLkiBXTKfIndSfLfDCJjgyKjCAP(qKBREHoSgcMHYVCNTapmPyODbBOyQAyv, old_prompt, TPdbMzICOHVoRDIwYkBuPquOyCZwkKrH, current_item):
    OkGbEfBOlXJkHHiIxPCEdAigBwQFWinB = current_item
    kxdrqSDQHJnEllMOtIqUSWLnexkmvsXK = qKBREHoSgcMHYVCNTapmPyODbBOyQAyv[OkGbEfBOlXJkHHiIxPCEdAigBwQFWinB]['inputs']
    pBgHpIpwWsKYNXAVImuNRvNCqoZgeKOO = qKBREHoSgcMHYVCNTapmPyODbBOyQAyv[OkGbEfBOlXJkHHiIxPCEdAigBwQFWinB]['class_type']
    QVFkmcxYKbGpDWdwPuNpltEZeinkgFbR = nodes.wJhMfuyrPNjllkMCYXdJHMhubCAizKhP[pBgHpIpwWsKYNXAVImuNRvNCqoZgeKOO]
    zsZewgEflaHOKxRWJqJWYrbUKVloKNPO = ''
    yBdlSItcDiylDLnrPupAlGvSpzlrnuWk = ''
    HZgFvSCHHvndfkOsuWOqyKgtGBOkAfAZ = False
    if hasattr(QVFkmcxYKbGpDWdwPuNpltEZeinkgFbR, 'IS_CHANGED'):
        if OkGbEfBOlXJkHHiIxPCEdAigBwQFWinB in old_prompt and 'is_changed' in old_prompt[OkGbEfBOlXJkHHiIxPCEdAigBwQFWinB]:
            zsZewgEflaHOKxRWJqJWYrbUKVloKNPO = old_prompt[OkGbEfBOlXJkHHiIxPCEdAigBwQFWinB]['is_changed']
        if 'is_changed' not in qKBREHoSgcMHYVCNTapmPyODbBOyQAyv[OkGbEfBOlXJkHHiIxPCEdAigBwQFWinB]:
            DShVzzegkrjgHxkcKhTwHIgrLbIYjoVy = RJtMQsrZYSczxBuFhYkbBGspnaWoaVek(kxdrqSDQHJnEllMOtIqUSWLnexkmvsXK, QVFkmcxYKbGpDWdwPuNpltEZeinkgFbR, OkGbEfBOlXJkHHiIxPCEdAigBwQFWinB, TPdbMzICOHVoRDIwYkBuPquOyCZwkKrH)
            if DShVzzegkrjgHxkcKhTwHIgrLbIYjoVy is not None:
                try:
                    yBdlSItcDiylDLnrPupAlGvSpzlrnuWk = znDMGjLEJesTIoWKbaCIQXMLYNShsqxP(QVFkmcxYKbGpDWdwPuNpltEZeinkgFbR, DShVzzegkrjgHxkcKhTwHIgrLbIYjoVy, "IS_CHANGED")
                    qKBREHoSgcMHYVCNTapmPyODbBOyQAyv[OkGbEfBOlXJkHHiIxPCEdAigBwQFWinB]['is_changed'] = yBdlSItcDiylDLnrPupAlGvSpzlrnuWk
                except:
                    HZgFvSCHHvndfkOsuWOqyKgtGBOkAfAZ = True
        else:
            yBdlSItcDiylDLnrPupAlGvSpzlrnuWk = qKBREHoSgcMHYVCNTapmPyODbBOyQAyv[OkGbEfBOlXJkHHiIxPCEdAigBwQFWinB]['is_changed']
    if OkGbEfBOlXJkHHiIxPCEdAigBwQFWinB not in TPdbMzICOHVoRDIwYkBuPquOyCZwkKrH:
        return True
    if not HZgFvSCHHvndfkOsuWOqyKgtGBOkAfAZ:
        if yBdlSItcDiylDLnrPupAlGvSpzlrnuWk != zsZewgEflaHOKxRWJqJWYrbUKVloKNPO:
            HZgFvSCHHvndfkOsuWOqyKgtGBOkAfAZ = True
        elif OkGbEfBOlXJkHHiIxPCEdAigBwQFWinB not in old_prompt:
            HZgFvSCHHvndfkOsuWOqyKgtGBOkAfAZ = True
        elif kxdrqSDQHJnEllMOtIqUSWLnexkmvsXK == old_prompt[OkGbEfBOlXJkHHiIxPCEdAigBwQFWinB]['inputs']:
            for NECAaWUrFGIXcLimrerEYmxYIykQBfXb in kxdrqSDQHJnEllMOtIqUSWLnexkmvsXK:
                BLXYdQZMdSUVXqHWfCWrRSRgDkKAoCGR = kxdrqSDQHJnEllMOtIqUSWLnexkmvsXK[NECAaWUrFGIXcLimrerEYmxYIykQBfXb]
                if isinstance(BLXYdQZMdSUVXqHWfCWrRSRgDkKAoCGR, list):
                    rLPruVdmzKDqcYsJgVZgWfYEgKWyJgxe = BLXYdQZMdSUVXqHWfCWrRSRgDkKAoCGR[0]
                    WjdDprUAwUFaYOLeMvbVzAgLBDwMxTFK = BLXYdQZMdSUVXqHWfCWrRSRgDkKAoCGR[1]
                    if rLPruVdmzKDqcYsJgVZgWfYEgKWyJgxe in TPdbMzICOHVoRDIwYkBuPquOyCZwkKrH:
                        HZgFvSCHHvndfkOsuWOqyKgtGBOkAfAZ = iCiuUpLkiBXTKfIndSfLfDCJjgyKjCAP(qKBREHoSgcMHYVCNTapmPyODbBOyQAyv, old_prompt, TPdbMzICOHVoRDIwYkBuPquOyCZwkKrH, rLPruVdmzKDqcYsJgVZgWfYEgKWyJgxe)
                    else:
                        HZgFvSCHHvndfkOsuWOqyKgtGBOkAfAZ = True
                    if HZgFvSCHHvndfkOsuWOqyKgtGBOkAfAZ:
                        break
        else:
            HZgFvSCHHvndfkOsuWOqyKgtGBOkAfAZ = True
    if HZgFvSCHHvndfkOsuWOqyKgtGBOkAfAZ:
        TXGwYXNLgQsYzfHHpRBDJGFCFZEClzIo = TPdbMzICOHVoRDIwYkBuPquOyCZwkKrH.pop(OkGbEfBOlXJkHHiIxPCEdAigBwQFWinB)
        del TXGwYXNLgQsYzfHHpRBDJGFCFZEClzIo
    return HZgFvSCHHvndfkOsuWOqyKgtGBOkAfAZ
class peTrImVAySgqncNtKhRfuATBVRUZsjwA:
    def __init__(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, REDIKAYZymAzMirxFmomyJtEGktwcqlE):
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.TPdbMzICOHVoRDIwYkBuPquOyCZwkKrH = {}
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.object_storage = {}
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.outputs_ui = {}
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.old_prompt = {}
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.REDIKAYZymAzMirxFmomyJtEGktwcqlE = REDIKAYZymAzMirxFmomyJtEGktwcqlE
    def rqYcEvqEJnTSVvRCylmsNjnSJNyCXwew(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, AFursZnPuECGUFTkCjDbdYIYmtroiqfB, qKBREHoSgcMHYVCNTapmPyODbBOyQAyv, GqiQNpsoosxhpFpRzNWflNFaUzVlGhnV, hLymBLypSLZVPrzSiZmuWHxSGFfDqIkt, PqgBmIFFlGqAiqwTGPXLJksdyclTftXN, YJIyBYFuSbfDGbTSGjpGoODShSYXRpRz):
        WUnsDKMtnjEEHIRpEKBjpWsxTOaQPOEe = PqgBmIFFlGqAiqwTGPXLJksdyclTftXN["node_id"]
        pBgHpIpwWsKYNXAVImuNRvNCqoZgeKOO = qKBREHoSgcMHYVCNTapmPyODbBOyQAyv[WUnsDKMtnjEEHIRpEKBjpWsxTOaQPOEe]["class_type"]
        if isinstance(YJIyBYFuSbfDGbTSGjpGoODShSYXRpRz, quasar.model_management.FcmhbKAfUbwHtuUFKflJjsPfbobaJqvP):
            jijkIozVOeiYRxQMNHWrDLewPOWEpVTX = {
                "prompt_id": AFursZnPuECGUFTkCjDbdYIYmtroiqfB,
                "node_id": WUnsDKMtnjEEHIRpEKBjpWsxTOaQPOEe,
                "node_type": pBgHpIpwWsKYNXAVImuNRvNCqoZgeKOO,
                "executed": list(hLymBLypSLZVPrzSiZmuWHxSGFfDqIkt),
            }
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.REDIKAYZymAzMirxFmomyJtEGktwcqlE.qIpzeiOiFfpTobMBTgFPHfiZRTmLDpoa("execution_interrupted", jijkIozVOeiYRxQMNHWrDLewPOWEpVTX, rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.REDIKAYZymAzMirxFmomyJtEGktwcqlE.client_id)
        else:
            if rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.REDIKAYZymAzMirxFmomyJtEGktwcqlE.client_id is not None:
                jijkIozVOeiYRxQMNHWrDLewPOWEpVTX = {
                    "prompt_id": AFursZnPuECGUFTkCjDbdYIYmtroiqfB,
                    "node_id": WUnsDKMtnjEEHIRpEKBjpWsxTOaQPOEe,
                    "node_type": pBgHpIpwWsKYNXAVImuNRvNCqoZgeKOO,
                    "executed": list(hLymBLypSLZVPrzSiZmuWHxSGFfDqIkt),
                    "exception_message": PqgBmIFFlGqAiqwTGPXLJksdyclTftXN["exception_message"],
                    "exception_type": PqgBmIFFlGqAiqwTGPXLJksdyclTftXN["exception_type"],
                    "traceback": PqgBmIFFlGqAiqwTGPXLJksdyclTftXN["traceback"],
                    "current_inputs": PqgBmIFFlGqAiqwTGPXLJksdyclTftXN["current_inputs"],
                    "current_outputs": PqgBmIFFlGqAiqwTGPXLJksdyclTftXN["current_outputs"],
                }
                rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.REDIKAYZymAzMirxFmomyJtEGktwcqlE.qIpzeiOiFfpTobMBTgFPHfiZRTmLDpoa("execution_error", jijkIozVOeiYRxQMNHWrDLewPOWEpVTX, rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.REDIKAYZymAzMirxFmomyJtEGktwcqlE.client_id)
        HZgFvSCHHvndfkOsuWOqyKgtGBOkAfAZ = []
        for LDnaTUWTECGaKdJqXUUrFoSvDMujRxwx in rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.TPdbMzICOHVoRDIwYkBuPquOyCZwkKrH:
            if (LDnaTUWTECGaKdJqXUUrFoSvDMujRxwx not in GqiQNpsoosxhpFpRzNWflNFaUzVlGhnV) and (LDnaTUWTECGaKdJqXUUrFoSvDMujRxwx not in hLymBLypSLZVPrzSiZmuWHxSGFfDqIkt):
                HZgFvSCHHvndfkOsuWOqyKgtGBOkAfAZ += [LDnaTUWTECGaKdJqXUUrFoSvDMujRxwx]
                if LDnaTUWTECGaKdJqXUUrFoSvDMujRxwx in rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.old_prompt:
                    TXGwYXNLgQsYzfHHpRBDJGFCFZEClzIo = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.old_prompt.pop(LDnaTUWTECGaKdJqXUUrFoSvDMujRxwx)
                    del TXGwYXNLgQsYzfHHpRBDJGFCFZEClzIo
        for LDnaTUWTECGaKdJqXUUrFoSvDMujRxwx in HZgFvSCHHvndfkOsuWOqyKgtGBOkAfAZ:
            TXGwYXNLgQsYzfHHpRBDJGFCFZEClzIo = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.TPdbMzICOHVoRDIwYkBuPquOyCZwkKrH.pop(LDnaTUWTECGaKdJqXUUrFoSvDMujRxwx)
            del TXGwYXNLgQsYzfHHpRBDJGFCFZEClzIo
    def ikeEiwtXFGzELzZxqxOCxIpkRiAYGmXd(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, qKBREHoSgcMHYVCNTapmPyODbBOyQAyv, AFursZnPuECGUFTkCjDbdYIYmtroiqfB, vngfynKJfsHLAoqKbHSpKIzjZdROnsZl={}, execute_outputs=[]):
        nodes.NIMMAjqKpMwgFfFMJGlJLJdwCPLKOQTM(False)
        if "client_id" in vngfynKJfsHLAoqKbHSpKIzjZdROnsZl:
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.REDIKAYZymAzMirxFmomyJtEGktwcqlE.client_id = vngfynKJfsHLAoqKbHSpKIzjZdROnsZl["client_id"]
        else:
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.REDIKAYZymAzMirxFmomyJtEGktwcqlE.client_id = None
        if rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.REDIKAYZymAzMirxFmomyJtEGktwcqlE.client_id is not None:
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.REDIKAYZymAzMirxFmomyJtEGktwcqlE.qIpzeiOiFfpTobMBTgFPHfiZRTmLDpoa("execution_start", { "prompt_id": AFursZnPuECGUFTkCjDbdYIYmtroiqfB}, rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.REDIKAYZymAzMirxFmomyJtEGktwcqlE.client_id)
        with torch.inference_mode():
            HZgFvSCHHvndfkOsuWOqyKgtGBOkAfAZ = []
            for LDnaTUWTECGaKdJqXUUrFoSvDMujRxwx in rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.TPdbMzICOHVoRDIwYkBuPquOyCZwkKrH:
                if LDnaTUWTECGaKdJqXUUrFoSvDMujRxwx not in qKBREHoSgcMHYVCNTapmPyODbBOyQAyv:
                    HZgFvSCHHvndfkOsuWOqyKgtGBOkAfAZ += [LDnaTUWTECGaKdJqXUUrFoSvDMujRxwx]
            for LDnaTUWTECGaKdJqXUUrFoSvDMujRxwx in HZgFvSCHHvndfkOsuWOqyKgtGBOkAfAZ:
                TXGwYXNLgQsYzfHHpRBDJGFCFZEClzIo = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.TPdbMzICOHVoRDIwYkBuPquOyCZwkKrH.pop(LDnaTUWTECGaKdJqXUUrFoSvDMujRxwx)
                del TXGwYXNLgQsYzfHHpRBDJGFCFZEClzIo
            HZgFvSCHHvndfkOsuWOqyKgtGBOkAfAZ = []
            for LDnaTUWTECGaKdJqXUUrFoSvDMujRxwx in rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.object_storage:
                if LDnaTUWTECGaKdJqXUUrFoSvDMujRxwx[0] not in qKBREHoSgcMHYVCNTapmPyODbBOyQAyv:
                    HZgFvSCHHvndfkOsuWOqyKgtGBOkAfAZ += [LDnaTUWTECGaKdJqXUUrFoSvDMujRxwx]
                else:
                    HutkrxeXIuRQKOhCWHkiwqLGAsJjUSKj = qKBREHoSgcMHYVCNTapmPyODbBOyQAyv[LDnaTUWTECGaKdJqXUUrFoSvDMujRxwx[0]]
                    if LDnaTUWTECGaKdJqXUUrFoSvDMujRxwx[1] != HutkrxeXIuRQKOhCWHkiwqLGAsJjUSKj['class_type']:
                        HZgFvSCHHvndfkOsuWOqyKgtGBOkAfAZ += [LDnaTUWTECGaKdJqXUUrFoSvDMujRxwx]
            for LDnaTUWTECGaKdJqXUUrFoSvDMujRxwx in HZgFvSCHHvndfkOsuWOqyKgtGBOkAfAZ:
                TXGwYXNLgQsYzfHHpRBDJGFCFZEClzIo = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.object_storage.pop(LDnaTUWTECGaKdJqXUUrFoSvDMujRxwx)
                del TXGwYXNLgQsYzfHHpRBDJGFCFZEClzIo
            for NECAaWUrFGIXcLimrerEYmxYIykQBfXb in qKBREHoSgcMHYVCNTapmPyODbBOyQAyv:
                iCiuUpLkiBXTKfIndSfLfDCJjgyKjCAP(qKBREHoSgcMHYVCNTapmPyODbBOyQAyv, rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.old_prompt, rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.TPdbMzICOHVoRDIwYkBuPquOyCZwkKrH, NECAaWUrFGIXcLimrerEYmxYIykQBfXb)
            GqiQNpsoosxhpFpRzNWflNFaUzVlGhnV = set(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.TPdbMzICOHVoRDIwYkBuPquOyCZwkKrH.keys())
            for NECAaWUrFGIXcLimrerEYmxYIykQBfXb in list(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.outputs_ui.keys()):
                if NECAaWUrFGIXcLimrerEYmxYIykQBfXb not in GqiQNpsoosxhpFpRzNWflNFaUzVlGhnV:
                    TXGwYXNLgQsYzfHHpRBDJGFCFZEClzIo = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.outputs_ui.pop(NECAaWUrFGIXcLimrerEYmxYIykQBfXb)
                    del TXGwYXNLgQsYzfHHpRBDJGFCFZEClzIo
            quasar.model_management.swGRFPugxSKWuFFSumUDzRojyZMqyytZ()
            if rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.REDIKAYZymAzMirxFmomyJtEGktwcqlE.client_id is not None:
                rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.REDIKAYZymAzMirxFmomyJtEGktwcqlE.qIpzeiOiFfpTobMBTgFPHfiZRTmLDpoa("execution_cached", { "nodes": list(GqiQNpsoosxhpFpRzNWflNFaUzVlGhnV) , "prompt_id": AFursZnPuECGUFTkCjDbdYIYmtroiqfB}, rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.REDIKAYZymAzMirxFmomyJtEGktwcqlE.client_id)
            hLymBLypSLZVPrzSiZmuWHxSGFfDqIkt = set()
            BzHyufYLFDSoSZKuinMlCcqvwCCLeDKY = None
            zddvMQMywxZrtQeWReiVxjDRuwCNfQoE = []
            for WUnsDKMtnjEEHIRpEKBjpWsxTOaQPOEe in list(execute_outputs):
                zddvMQMywxZrtQeWReiVxjDRuwCNfQoE += [(0, WUnsDKMtnjEEHIRpEKBjpWsxTOaQPOEe)]
            while len(zddvMQMywxZrtQeWReiVxjDRuwCNfQoE) > 0:
                zddvMQMywxZrtQeWReiVxjDRuwCNfQoE = sorted(list(map(lambda GlZreLQjBCiBptpFgmbsMbhjFlMgPVav: (len(XwfrXrUSmKYfmtrwrTSzVawyDMlBRcHb(qKBREHoSgcMHYVCNTapmPyODbBOyQAyv, rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.TPdbMzICOHVoRDIwYkBuPquOyCZwkKrH, GlZreLQjBCiBptpFgmbsMbhjFlMgPVav[-1])), GlZreLQjBCiBptpFgmbsMbhjFlMgPVav[-1]), zddvMQMywxZrtQeWReiVxjDRuwCNfQoE)))
                BzHyufYLFDSoSZKuinMlCcqvwCCLeDKY = zddvMQMywxZrtQeWReiVxjDRuwCNfQoE.pop(0)[-1]
                syoCixXNjFxZAimZmlHgvNsypzGRqzuD, PqgBmIFFlGqAiqwTGPXLJksdyclTftXN, YJIyBYFuSbfDGbTSGjpGoODShSYXRpRz = jwltmDqWYcEtFryNbsfrnywMaYpQMVcH(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.REDIKAYZymAzMirxFmomyJtEGktwcqlE, qKBREHoSgcMHYVCNTapmPyODbBOyQAyv, rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.TPdbMzICOHVoRDIwYkBuPquOyCZwkKrH, BzHyufYLFDSoSZKuinMlCcqvwCCLeDKY, vngfynKJfsHLAoqKbHSpKIzjZdROnsZl, hLymBLypSLZVPrzSiZmuWHxSGFfDqIkt, AFursZnPuECGUFTkCjDbdYIYmtroiqfB, rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.outputs_ui, rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.object_storage)
                if syoCixXNjFxZAimZmlHgvNsypzGRqzuD is not True:
                    rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.rqYcEvqEJnTSVvRCylmsNjnSJNyCXwew(AFursZnPuECGUFTkCjDbdYIYmtroiqfB, qKBREHoSgcMHYVCNTapmPyODbBOyQAyv, GqiQNpsoosxhpFpRzNWflNFaUzVlGhnV, hLymBLypSLZVPrzSiZmuWHxSGFfDqIkt, PqgBmIFFlGqAiqwTGPXLJksdyclTftXN, YJIyBYFuSbfDGbTSGjpGoODShSYXRpRz)
                    break
            for NECAaWUrFGIXcLimrerEYmxYIykQBfXb in hLymBLypSLZVPrzSiZmuWHxSGFfDqIkt:
                rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.old_prompt[NECAaWUrFGIXcLimrerEYmxYIykQBfXb] = copy.deepcopy(qKBREHoSgcMHYVCNTapmPyODbBOyQAyv[NECAaWUrFGIXcLimrerEYmxYIykQBfXb])
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.REDIKAYZymAzMirxFmomyJtEGktwcqlE.last_node_id = None
def TwptytSBzFuVrxrtQBUcDlqIrprSpJEg(qKBREHoSgcMHYVCNTapmPyODbBOyQAyv, ygFiYnqtfEqFJmbillPxtHRxsUoFqqJk, GqOVfXlxFqvgpjrwPHnlgBnCkMHDTtqw):
    OkGbEfBOlXJkHHiIxPCEdAigBwQFWinB = ygFiYnqtfEqFJmbillPxtHRxsUoFqqJk
    if OkGbEfBOlXJkHHiIxPCEdAigBwQFWinB in GqOVfXlxFqvgpjrwPHnlgBnCkMHDTtqw:
        return GqOVfXlxFqvgpjrwPHnlgBnCkMHDTtqw[OkGbEfBOlXJkHHiIxPCEdAigBwQFWinB]
    kxdrqSDQHJnEllMOtIqUSWLnexkmvsXK = qKBREHoSgcMHYVCNTapmPyODbBOyQAyv[OkGbEfBOlXJkHHiIxPCEdAigBwQFWinB]['inputs']
    pBgHpIpwWsKYNXAVImuNRvNCqoZgeKOO = qKBREHoSgcMHYVCNTapmPyODbBOyQAyv[OkGbEfBOlXJkHHiIxPCEdAigBwQFWinB]['class_type']
    jKcSNUDNgDXASzMmWRVTLbRKsfRcUIvA = nodes.wJhMfuyrPNjllkMCYXdJHMhubCAizKhP[pBgHpIpwWsKYNXAVImuNRvNCqoZgeKOO]
    IyRXtXYBpHjRAWmqbgMOHybfDEDaNfZh = jKcSNUDNgDXASzMmWRVTLbRKsfRcUIvA.hGTeyOvpHejlssWPjkjTHIgcOKnCfnQl()
    JXybGuivgWrcgWHRoCCzNhyiXuJTTcTH = IyRXtXYBpHjRAWmqbgMOHybfDEDaNfZh['required']
    tyKpUhRcyvkdDsojxSkmAplYEpmXGmUC = []
    ERUVMXIoRhkepyeqXbuVyzEnnckUwodx = True
    for NECAaWUrFGIXcLimrerEYmxYIykQBfXb in JXybGuivgWrcgWHRoCCzNhyiXuJTTcTH:
        if NECAaWUrFGIXcLimrerEYmxYIykQBfXb not in kxdrqSDQHJnEllMOtIqUSWLnexkmvsXK:
            PqgBmIFFlGqAiqwTGPXLJksdyclTftXN = {
                "type": "required_input_missing",
                "message": "Required input is missing",
                "details": f"{x}",
                "extra_info": {
                    "input_name": NECAaWUrFGIXcLimrerEYmxYIykQBfXb
                }
            }
            tyKpUhRcyvkdDsojxSkmAplYEpmXGmUC.append(PqgBmIFFlGqAiqwTGPXLJksdyclTftXN)
            continue
        iQelECAceWgpMwNVKVNfqYXiZvxEyNPn = kxdrqSDQHJnEllMOtIqUSWLnexkmvsXK[NECAaWUrFGIXcLimrerEYmxYIykQBfXb]
        dkvGBiZkeLIFANNbVKlbQzLVBVedCkgi = JXybGuivgWrcgWHRoCCzNhyiXuJTTcTH[NECAaWUrFGIXcLimrerEYmxYIykQBfXb]
        SOtcNfLxXoDBSldZHWFTdTbeiMOiuhxh = dkvGBiZkeLIFANNbVKlbQzLVBVedCkgi[0]
        if isinstance(iQelECAceWgpMwNVKVNfqYXiZvxEyNPn, list):
            if len(iQelECAceWgpMwNVKVNfqYXiZvxEyNPn) != 2:
                PqgBmIFFlGqAiqwTGPXLJksdyclTftXN = {
                    "type": "bad_linked_input",
                    "message": "Bad linked input, must be a length-2 list of [node_id, slot_index]",
                    "details": f"{x}",
                    "extra_info": {
                        "input_name": NECAaWUrFGIXcLimrerEYmxYIykQBfXb,
                        "input_config": dkvGBiZkeLIFANNbVKlbQzLVBVedCkgi,
                        "received_value": iQelECAceWgpMwNVKVNfqYXiZvxEyNPn
                    }
                }
                tyKpUhRcyvkdDsojxSkmAplYEpmXGmUC.append(PqgBmIFFlGqAiqwTGPXLJksdyclTftXN)
                continue
            VKUdGsThnDtIlRiEtCMRSOEsLhTqISUS = iQelECAceWgpMwNVKVNfqYXiZvxEyNPn[0]
            xvwZmYAKQXNTUxmbwFacoHXGGHfmLerL = qKBREHoSgcMHYVCNTapmPyODbBOyQAyv[VKUdGsThnDtIlRiEtCMRSOEsLhTqISUS]['class_type']
            r = nodes.wJhMfuyrPNjllkMCYXdJHMhubCAizKhP[xvwZmYAKQXNTUxmbwFacoHXGGHfmLerL].KmrPlNMyCntWtQIuwTzhYketzPaLUxAX
            if r[iQelECAceWgpMwNVKVNfqYXiZvxEyNPn[1]] != SOtcNfLxXoDBSldZHWFTdTbeiMOiuhxh:
                SgZNbrSQyjbSVmvfXwpNtbeCEpxEeoHu = r[iQelECAceWgpMwNVKVNfqYXiZvxEyNPn[1]]
                TexZuZtxAiaLVRAxGFFVASGePbOCzqHT = f"{x}, {received_type} != {type_input}"
                PqgBmIFFlGqAiqwTGPXLJksdyclTftXN = {
                    "type": "return_type_mismatch",
                    "message": "Return type mismatch between linked nodes",
                    "details": TexZuZtxAiaLVRAxGFFVASGePbOCzqHT,
                    "extra_info": {
                        "input_name": NECAaWUrFGIXcLimrerEYmxYIykQBfXb,
                        "input_config": dkvGBiZkeLIFANNbVKlbQzLVBVedCkgi,
                        "received_type": SgZNbrSQyjbSVmvfXwpNtbeCEpxEeoHu,
                        "linked_node": iQelECAceWgpMwNVKVNfqYXiZvxEyNPn
                    }
                }
                tyKpUhRcyvkdDsojxSkmAplYEpmXGmUC.append(PqgBmIFFlGqAiqwTGPXLJksdyclTftXN)
                continue
            try:
                r = TwptytSBzFuVrxrtQBUcDlqIrprSpJEg(qKBREHoSgcMHYVCNTapmPyODbBOyQAyv, VKUdGsThnDtIlRiEtCMRSOEsLhTqISUS, GqOVfXlxFqvgpjrwPHnlgBnCkMHDTtqw)
                if r[0] is False:
                    ERUVMXIoRhkepyeqXbuVyzEnnckUwodx = False
                    continue
            except Exception as YJIyBYFuSbfDGbTSGjpGoODShSYXRpRz:
                lNaMhSVGVjaibIkJNZqMMpHyVpGvwQoR, _, MFEPhxDvKhTtHiHybdiYCFrdHKnPxOpk = sys.exc_info()
                ERUVMXIoRhkepyeqXbuVyzEnnckUwodx = False
                fHgxuGFQyywnXHSwGpHqZhvbEmkNjhFR = TofpJDHPPEZZyHHPZTbiDOLhnocJgpJM(lNaMhSVGVjaibIkJNZqMMpHyVpGvwQoR)
                pVdSmqRwNYjKODvmWoRhfuuOOogMyUFu = [{
                    "type": "exception_during_inner_validation",
                    "message": "Exception when validating inner node",
                    "details": str(YJIyBYFuSbfDGbTSGjpGoODShSYXRpRz),
                    "extra_info": {
                        "input_name": NECAaWUrFGIXcLimrerEYmxYIykQBfXb,
                        "input_config": dkvGBiZkeLIFANNbVKlbQzLVBVedCkgi,
                        "exception_message": str(YJIyBYFuSbfDGbTSGjpGoODShSYXRpRz),
                        "exception_type": fHgxuGFQyywnXHSwGpHqZhvbEmkNjhFR,
                        "traceback": traceback.format_tb(MFEPhxDvKhTtHiHybdiYCFrdHKnPxOpk),
                        "linked_node": iQelECAceWgpMwNVKVNfqYXiZvxEyNPn
                    }
                }]
                GqOVfXlxFqvgpjrwPHnlgBnCkMHDTtqw[VKUdGsThnDtIlRiEtCMRSOEsLhTqISUS] = (False, pVdSmqRwNYjKODvmWoRhfuuOOogMyUFu, VKUdGsThnDtIlRiEtCMRSOEsLhTqISUS)
                continue
        else:
            try:
                if SOtcNfLxXoDBSldZHWFTdTbeiMOiuhxh == "INT":
                    iQelECAceWgpMwNVKVNfqYXiZvxEyNPn = int(iQelECAceWgpMwNVKVNfqYXiZvxEyNPn)
                    kxdrqSDQHJnEllMOtIqUSWLnexkmvsXK[NECAaWUrFGIXcLimrerEYmxYIykQBfXb] = iQelECAceWgpMwNVKVNfqYXiZvxEyNPn
                if SOtcNfLxXoDBSldZHWFTdTbeiMOiuhxh == "FLOAT":
                    iQelECAceWgpMwNVKVNfqYXiZvxEyNPn = float(iQelECAceWgpMwNVKVNfqYXiZvxEyNPn)
                    kxdrqSDQHJnEllMOtIqUSWLnexkmvsXK[NECAaWUrFGIXcLimrerEYmxYIykQBfXb] = iQelECAceWgpMwNVKVNfqYXiZvxEyNPn
                if SOtcNfLxXoDBSldZHWFTdTbeiMOiuhxh == "STRING":
                    iQelECAceWgpMwNVKVNfqYXiZvxEyNPn = str(iQelECAceWgpMwNVKVNfqYXiZvxEyNPn)
                    kxdrqSDQHJnEllMOtIqUSWLnexkmvsXK[NECAaWUrFGIXcLimrerEYmxYIykQBfXb] = iQelECAceWgpMwNVKVNfqYXiZvxEyNPn
            except Exception as YJIyBYFuSbfDGbTSGjpGoODShSYXRpRz:
                PqgBmIFFlGqAiqwTGPXLJksdyclTftXN = {
                    "type": "invalid_input_type",
                    "message": f"Failed to convert an input value to a {type_input} value",
                    "details": f"{x}, {val}, {ex}",
                    "extra_info": {
                        "input_name": NECAaWUrFGIXcLimrerEYmxYIykQBfXb,
                        "input_config": dkvGBiZkeLIFANNbVKlbQzLVBVedCkgi,
                        "received_value": iQelECAceWgpMwNVKVNfqYXiZvxEyNPn,
                        "exception_message": str(YJIyBYFuSbfDGbTSGjpGoODShSYXRpRz)
                    }
                }
                tyKpUhRcyvkdDsojxSkmAplYEpmXGmUC.append(PqgBmIFFlGqAiqwTGPXLJksdyclTftXN)
                continue
            if len(dkvGBiZkeLIFANNbVKlbQzLVBVedCkgi) > 1:
                if "min" in dkvGBiZkeLIFANNbVKlbQzLVBVedCkgi[1] and iQelECAceWgpMwNVKVNfqYXiZvxEyNPn < dkvGBiZkeLIFANNbVKlbQzLVBVedCkgi[1]["min"]:
                    PqgBmIFFlGqAiqwTGPXLJksdyclTftXN = {
                        "type": "value_smaller_than_min",
                        "message": "Value {} smaller than min of {}".format(iQelECAceWgpMwNVKVNfqYXiZvxEyNPn, dkvGBiZkeLIFANNbVKlbQzLVBVedCkgi[1]["min"]),
                        "details": f"{x}",
                        "extra_info": {
                            "input_name": NECAaWUrFGIXcLimrerEYmxYIykQBfXb,
                            "input_config": dkvGBiZkeLIFANNbVKlbQzLVBVedCkgi,
                            "received_value": iQelECAceWgpMwNVKVNfqYXiZvxEyNPn,
                        }
                    }
                    tyKpUhRcyvkdDsojxSkmAplYEpmXGmUC.append(PqgBmIFFlGqAiqwTGPXLJksdyclTftXN)
                    continue
                if "max" in dkvGBiZkeLIFANNbVKlbQzLVBVedCkgi[1] and iQelECAceWgpMwNVKVNfqYXiZvxEyNPn > dkvGBiZkeLIFANNbVKlbQzLVBVedCkgi[1]["max"]:
                    PqgBmIFFlGqAiqwTGPXLJksdyclTftXN = {
                        "type": "value_bigger_than_max",
                        "message": "Value {} bigger than max of {}".format(iQelECAceWgpMwNVKVNfqYXiZvxEyNPn, dkvGBiZkeLIFANNbVKlbQzLVBVedCkgi[1]["max"]),
                        "details": f"{x}",
                        "extra_info": {
                            "input_name": NECAaWUrFGIXcLimrerEYmxYIykQBfXb,
                            "input_config": dkvGBiZkeLIFANNbVKlbQzLVBVedCkgi,
                            "received_value": iQelECAceWgpMwNVKVNfqYXiZvxEyNPn,
                        }
                    }
                    tyKpUhRcyvkdDsojxSkmAplYEpmXGmUC.append(PqgBmIFFlGqAiqwTGPXLJksdyclTftXN)
                    continue
            if hasattr(jKcSNUDNgDXASzMmWRVTLbRKsfRcUIvA, "VALIDATE_INPUTS"):
                DShVzzegkrjgHxkcKhTwHIgrLbIYjoVy = RJtMQsrZYSczxBuFhYkbBGspnaWoaVek(kxdrqSDQHJnEllMOtIqUSWLnexkmvsXK, jKcSNUDNgDXASzMmWRVTLbRKsfRcUIvA, OkGbEfBOlXJkHHiIxPCEdAigBwQFWinB)
                wTKTCkxEtYuHmqLlpcdxLANFEoxUnsLR = znDMGjLEJesTIoWKbaCIQXMLYNShsqxP(jKcSNUDNgDXASzMmWRVTLbRKsfRcUIvA, DShVzzegkrjgHxkcKhTwHIgrLbIYjoVy, "VALIDATE_INPUTS")
                for HCXmerBqIMuTscBONzTGKYapYSxWTYHo, r in enumerate(wTKTCkxEtYuHmqLlpcdxLANFEoxUnsLR):
                    if r is not True:
                        TexZuZtxAiaLVRAxGFFVASGePbOCzqHT = f"{x}"
                        if r is not False:
                            TexZuZtxAiaLVRAxGFFVASGePbOCzqHT += f" - {str(r)}"
                        PqgBmIFFlGqAiqwTGPXLJksdyclTftXN = {
                            "type": "custom_validation_failed",
                            "message": "Custom validation failed for node",
                            "details": TexZuZtxAiaLVRAxGFFVASGePbOCzqHT,
                            "extra_info": {
                                "input_name": NECAaWUrFGIXcLimrerEYmxYIykQBfXb,
                                "input_config": dkvGBiZkeLIFANNbVKlbQzLVBVedCkgi,
                                "received_value": iQelECAceWgpMwNVKVNfqYXiZvxEyNPn,
                            }
                        }
                        tyKpUhRcyvkdDsojxSkmAplYEpmXGmUC.append(PqgBmIFFlGqAiqwTGPXLJksdyclTftXN)
                        continue
            else:
                if isinstance(SOtcNfLxXoDBSldZHWFTdTbeiMOiuhxh, list):
                    if iQelECAceWgpMwNVKVNfqYXiZvxEyNPn not in SOtcNfLxXoDBSldZHWFTdTbeiMOiuhxh:
                        uONCVAVrXQftXMRJNGOJrhTPURSsHSXH = dkvGBiZkeLIFANNbVKlbQzLVBVedCkgi
                        bnxyLuXGeJRnJAfdKvMUqBetnpmTXDtY = ""
                        if len(SOtcNfLxXoDBSldZHWFTdTbeiMOiuhxh) > 20:
                            bnxyLuXGeJRnJAfdKvMUqBetnpmTXDtY = f"(list of length {len(type_input)})"
                            uONCVAVrXQftXMRJNGOJrhTPURSsHSXH = None
                        else:
                            bnxyLuXGeJRnJAfdKvMUqBetnpmTXDtY = str(SOtcNfLxXoDBSldZHWFTdTbeiMOiuhxh)
                        PqgBmIFFlGqAiqwTGPXLJksdyclTftXN = {
                            "type": "value_not_in_list",
                            "message": "Value not in list",
                            "details": f"{x}: '{iQelECAceWgpMwNVKVNfqYXiZvxEyNPn}' not in {list_info}",
                            "extra_info": {
                                "input_name": NECAaWUrFGIXcLimrerEYmxYIykQBfXb,
                                "input_config": uONCVAVrXQftXMRJNGOJrhTPURSsHSXH,
                                "received_value": iQelECAceWgpMwNVKVNfqYXiZvxEyNPn,
                            }
                        }
                        tyKpUhRcyvkdDsojxSkmAplYEpmXGmUC.append(PqgBmIFFlGqAiqwTGPXLJksdyclTftXN)
                        continue
    if len(tyKpUhRcyvkdDsojxSkmAplYEpmXGmUC) > 0 or ERUVMXIoRhkepyeqXbuVyzEnnckUwodx is not True:
        wTKTCkxEtYuHmqLlpcdxLANFEoxUnsLR = (False, tyKpUhRcyvkdDsojxSkmAplYEpmXGmUC, OkGbEfBOlXJkHHiIxPCEdAigBwQFWinB)
    else:
        wTKTCkxEtYuHmqLlpcdxLANFEoxUnsLR = (True, [], OkGbEfBOlXJkHHiIxPCEdAigBwQFWinB)
    GqOVfXlxFqvgpjrwPHnlgBnCkMHDTtqw[OkGbEfBOlXJkHHiIxPCEdAigBwQFWinB] = wTKTCkxEtYuHmqLlpcdxLANFEoxUnsLR
    return wTKTCkxEtYuHmqLlpcdxLANFEoxUnsLR
def TofpJDHPPEZZyHHPZTbiDOLhnocJgpJM(klass):
    FRIBQCDfDDxIonplwxvPCicvOmmOgYPC = klass.__module__
    if FRIBQCDfDDxIonplwxvPCicvOmmOgYPC == 'builtins':
        return klass.__qualname__
    return FRIBQCDfDDxIonplwxvPCicvOmmOgYPC + '.' + klass.__qualname__
def qcwCQLkogrkGqZWctxxXKVKWwxbopaRJ(qKBREHoSgcMHYVCNTapmPyODbBOyQAyv):
    TPdbMzICOHVoRDIwYkBuPquOyCZwkKrH = set()
    for NECAaWUrFGIXcLimrerEYmxYIykQBfXb in qKBREHoSgcMHYVCNTapmPyODbBOyQAyv:
        qfBrHpKxErrWlwSGmgASuMlNxzYUGSoL = nodes.wJhMfuyrPNjllkMCYXdJHMhubCAizKhP[qKBREHoSgcMHYVCNTapmPyODbBOyQAyv[NECAaWUrFGIXcLimrerEYmxYIykQBfXb]['class_type']]
        if hasattr(qfBrHpKxErrWlwSGmgASuMlNxzYUGSoL, 'OUTPUT_NODE') and qfBrHpKxErrWlwSGmgASuMlNxzYUGSoL.AQnTlfqkrmdAAnLjLNUFibEHomwVhMHv == True:
            TPdbMzICOHVoRDIwYkBuPquOyCZwkKrH.add(NECAaWUrFGIXcLimrerEYmxYIykQBfXb)
    if len(TPdbMzICOHVoRDIwYkBuPquOyCZwkKrH) == 0:
        PqgBmIFFlGqAiqwTGPXLJksdyclTftXN = {
            "type": "prompt_no_outputs",
            "message": "Prompt has no outputs",
            "details": "",
            "extra_info": {}
        }
        return (False, PqgBmIFFlGqAiqwTGPXLJksdyclTftXN, [], [])
    uxUYmkROHfqCLPUZVSaSnkWbbqLlzimI = set()
    tyKpUhRcyvkdDsojxSkmAplYEpmXGmUC = []
    RJlkegGphFKtsePALxQWzsJZWKRFmkvp = {}
    GqOVfXlxFqvgpjrwPHnlgBnCkMHDTtqw = {}
    for LDnaTUWTECGaKdJqXUUrFoSvDMujRxwx in TPdbMzICOHVoRDIwYkBuPquOyCZwkKrH:
        ERUVMXIoRhkepyeqXbuVyzEnnckUwodx = False
        pVdSmqRwNYjKODvmWoRhfuuOOogMyUFu = []
        try:
            FTosLGldclAzaiNbwuLMIEtXfrZQpTnU = TwptytSBzFuVrxrtQBUcDlqIrprSpJEg(qKBREHoSgcMHYVCNTapmPyODbBOyQAyv, LDnaTUWTECGaKdJqXUUrFoSvDMujRxwx, GqOVfXlxFqvgpjrwPHnlgBnCkMHDTtqw)
            ERUVMXIoRhkepyeqXbuVyzEnnckUwodx = FTosLGldclAzaiNbwuLMIEtXfrZQpTnU[0]
            pVdSmqRwNYjKODvmWoRhfuuOOogMyUFu = FTosLGldclAzaiNbwuLMIEtXfrZQpTnU[1]
        except Exception as YJIyBYFuSbfDGbTSGjpGoODShSYXRpRz:
            lNaMhSVGVjaibIkJNZqMMpHyVpGvwQoR, _, MFEPhxDvKhTtHiHybdiYCFrdHKnPxOpk = sys.exc_info()
            ERUVMXIoRhkepyeqXbuVyzEnnckUwodx = False
            fHgxuGFQyywnXHSwGpHqZhvbEmkNjhFR = TofpJDHPPEZZyHHPZTbiDOLhnocJgpJM(lNaMhSVGVjaibIkJNZqMMpHyVpGvwQoR)
            pVdSmqRwNYjKODvmWoRhfuuOOogMyUFu = [{
                "type": "exception_during_validation",
                "message": "Exception when validating node",
                "details": str(YJIyBYFuSbfDGbTSGjpGoODShSYXRpRz),
                "extra_info": {
                    "exception_type": fHgxuGFQyywnXHSwGpHqZhvbEmkNjhFR,
                    "traceback": traceback.format_tb(MFEPhxDvKhTtHiHybdiYCFrdHKnPxOpk)
                }
            }]
            GqOVfXlxFqvgpjrwPHnlgBnCkMHDTtqw[LDnaTUWTECGaKdJqXUUrFoSvDMujRxwx] = (False, pVdSmqRwNYjKODvmWoRhfuuOOogMyUFu, LDnaTUWTECGaKdJqXUUrFoSvDMujRxwx)
        if ERUVMXIoRhkepyeqXbuVyzEnnckUwodx is True:
            uxUYmkROHfqCLPUZVSaSnkWbbqLlzimI.add(LDnaTUWTECGaKdJqXUUrFoSvDMujRxwx)
        else:
            print(f"Failed to validate prompt for output {o}:")
            if len(pVdSmqRwNYjKODvmWoRhfuuOOogMyUFu) > 0:
                print("* (prompt):")
                for pqotJMmtPhFQINyRFDdjZIAwPwfRUicI in pVdSmqRwNYjKODvmWoRhfuuOOogMyUFu:
                    print(f"  - {reason['message']}: {reason['details']}")
            tyKpUhRcyvkdDsojxSkmAplYEpmXGmUC += [(LDnaTUWTECGaKdJqXUUrFoSvDMujRxwx, pVdSmqRwNYjKODvmWoRhfuuOOogMyUFu)]
            for WUnsDKMtnjEEHIRpEKBjpWsxTOaQPOEe, EpPkhmvnuPCNYOnbTkWPbRocxmdOwtHI in GqOVfXlxFqvgpjrwPHnlgBnCkMHDTtqw.items():
                ERUVMXIoRhkepyeqXbuVyzEnnckUwodx = EpPkhmvnuPCNYOnbTkWPbRocxmdOwtHI[0]
                pVdSmqRwNYjKODvmWoRhfuuOOogMyUFu = EpPkhmvnuPCNYOnbTkWPbRocxmdOwtHI[1]
                if ERUVMXIoRhkepyeqXbuVyzEnnckUwodx is not True and len(pVdSmqRwNYjKODvmWoRhfuuOOogMyUFu) > 0:
                    if WUnsDKMtnjEEHIRpEKBjpWsxTOaQPOEe not in RJlkegGphFKtsePALxQWzsJZWKRFmkvp:
                        pBgHpIpwWsKYNXAVImuNRvNCqoZgeKOO = qKBREHoSgcMHYVCNTapmPyODbBOyQAyv[WUnsDKMtnjEEHIRpEKBjpWsxTOaQPOEe]['class_type']
                        RJlkegGphFKtsePALxQWzsJZWKRFmkvp[WUnsDKMtnjEEHIRpEKBjpWsxTOaQPOEe] = {
                            "errors": pVdSmqRwNYjKODvmWoRhfuuOOogMyUFu,
                            "dependent_outputs": [],
                            "class_type": pBgHpIpwWsKYNXAVImuNRvNCqoZgeKOO
                        }
                        print(f"* {class_type} {node_id}:")
                        for pqotJMmtPhFQINyRFDdjZIAwPwfRUicI in pVdSmqRwNYjKODvmWoRhfuuOOogMyUFu:
                            print(f"  - {reason['message']}: {reason['details']}")
                    RJlkegGphFKtsePALxQWzsJZWKRFmkvp[WUnsDKMtnjEEHIRpEKBjpWsxTOaQPOEe]["dependent_outputs"].append(LDnaTUWTECGaKdJqXUUrFoSvDMujRxwx)
            print("Output will be ignored")
    if len(uxUYmkROHfqCLPUZVSaSnkWbbqLlzimI) == 0:
        JcAOYsEPqVatDfpysVDQmxDLzobqcTUw = []
        for LDnaTUWTECGaKdJqXUUrFoSvDMujRxwx, tyKpUhRcyvkdDsojxSkmAplYEpmXGmUC in tyKpUhRcyvkdDsojxSkmAplYEpmXGmUC:
            for PqgBmIFFlGqAiqwTGPXLJksdyclTftXN in tyKpUhRcyvkdDsojxSkmAplYEpmXGmUC:
                JcAOYsEPqVatDfpysVDQmxDLzobqcTUw.append(f"{error['message']}: {error['details']}")
        JcAOYsEPqVatDfpysVDQmxDLzobqcTUw = "\n".join(JcAOYsEPqVatDfpysVDQmxDLzobqcTUw)
        PqgBmIFFlGqAiqwTGPXLJksdyclTftXN = {
            "type": "prompt_outputs_failed_validation",
            "message": "Prompt outputs failed validation",
            "details": JcAOYsEPqVatDfpysVDQmxDLzobqcTUw,
            "extra_info": {}
        }
        return (False, PqgBmIFFlGqAiqwTGPXLJksdyclTftXN, list(uxUYmkROHfqCLPUZVSaSnkWbbqLlzimI), RJlkegGphFKtsePALxQWzsJZWKRFmkvp)
    return (True, None, list(uxUYmkROHfqCLPUZVSaSnkWbbqLlzimI), RJlkegGphFKtsePALxQWzsJZWKRFmkvp)
class djbvqxsurYqUcvHzsaPmWWgRGaFgiGbE:
    def __init__(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, REDIKAYZymAzMirxFmomyJtEGktwcqlE):
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.REDIKAYZymAzMirxFmomyJtEGktwcqlE = REDIKAYZymAzMirxFmomyJtEGktwcqlE
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.mutex = threading.RLock()
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.not_empty = threading.Condition(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.mutex)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.task_counter = 0
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.queue = []
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.currently_running = {}
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.history = {}
        REDIKAYZymAzMirxFmomyJtEGktwcqlE.prompt_queue = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS
    def CCOVuLEMeFpoufRVtjDeWqHtFSDTjTzt(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, ygFiYnqtfEqFJmbillPxtHRxsUoFqqJk):
        with rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.mutex:
            heapq.heappush(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.queue, ygFiYnqtfEqFJmbillPxtHRxsUoFqqJk)
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.REDIKAYZymAzMirxFmomyJtEGktwcqlE.YpzwdlwzVFOboyfWmWHyngylauEuTbaZ()
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.not_empty.notify()
    def get(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS):
        with rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.not_empty:
            while len(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.queue) == 0:
                rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.not_empty.wait()
            ygFiYnqtfEqFJmbillPxtHRxsUoFqqJk = heapq.heappop(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.queue)
            HCXmerBqIMuTscBONzTGKYapYSxWTYHo = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.task_counter
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.currently_running[HCXmerBqIMuTscBONzTGKYapYSxWTYHo] = copy.deepcopy(ygFiYnqtfEqFJmbillPxtHRxsUoFqqJk)
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.task_counter += 1
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.REDIKAYZymAzMirxFmomyJtEGktwcqlE.YpzwdlwzVFOboyfWmWHyngylauEuTbaZ()
            return (ygFiYnqtfEqFJmbillPxtHRxsUoFqqJk, HCXmerBqIMuTscBONzTGKYapYSxWTYHo)
    def lrvDEWUQkaldxPekEUbBYhwXCnIgotQY(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, KGzGLMSBbGKBdjAeEfKInlpESGsdlTUh, TPdbMzICOHVoRDIwYkBuPquOyCZwkKrH):
        with rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.mutex:
            qKBREHoSgcMHYVCNTapmPyODbBOyQAyv = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.currently_running.pop(KGzGLMSBbGKBdjAeEfKInlpESGsdlTUh)
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.history[qKBREHoSgcMHYVCNTapmPyODbBOyQAyv[1]] = { "prompt": qKBREHoSgcMHYVCNTapmPyODbBOyQAyv, "outputs": {} }
            for LDnaTUWTECGaKdJqXUUrFoSvDMujRxwx in TPdbMzICOHVoRDIwYkBuPquOyCZwkKrH:
                rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.history[qKBREHoSgcMHYVCNTapmPyODbBOyQAyv[1]]["outputs"][LDnaTUWTECGaKdJqXUUrFoSvDMujRxwx] = TPdbMzICOHVoRDIwYkBuPquOyCZwkKrH[LDnaTUWTECGaKdJqXUUrFoSvDMujRxwx]
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.REDIKAYZymAzMirxFmomyJtEGktwcqlE.YpzwdlwzVFOboyfWmWHyngylauEuTbaZ()
    def zcXnzbKBPZhuUbUDbBKQYruWvmnWjdXd(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS):
        with rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.mutex:
            iqymPVpxyjOWChGwBkTemSzHJbnJdAIz = []
            for NECAaWUrFGIXcLimrerEYmxYIykQBfXb in rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.currently_running.values():
                iqymPVpxyjOWChGwBkTemSzHJbnJdAIz += [NECAaWUrFGIXcLimrerEYmxYIykQBfXb]
            return (iqymPVpxyjOWChGwBkTemSzHJbnJdAIz, copy.deepcopy(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.queue))
    def EtRSdUTbsAGPQTWeOVUeVvGClCQoJfey(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS):
        with rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.mutex:
            return len(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.queue) + len(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.currently_running)
    def DlgdOtYbsMDZaSavoSpBEHOHGoWiupuW(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS):
        with rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.mutex:
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.queue = []
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.REDIKAYZymAzMirxFmomyJtEGktwcqlE.YpzwdlwzVFOboyfWmWHyngylauEuTbaZ()
    def kqUSARiqrpbKPOIIpqEzyhrJfaGKBQOs(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, function):
        with rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.mutex:
            for NECAaWUrFGIXcLimrerEYmxYIykQBfXb in range(len(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.queue)):
                if function(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.queue[NECAaWUrFGIXcLimrerEYmxYIykQBfXb]):
                    if len(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.queue) == 1:
                        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.DlgdOtYbsMDZaSavoSpBEHOHGoWiupuW()
                    else:
                        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.queue.pop(NECAaWUrFGIXcLimrerEYmxYIykQBfXb)
                        heapq.heapify(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.queue)
                    rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.REDIKAYZymAzMirxFmomyJtEGktwcqlE.YpzwdlwzVFOboyfWmWHyngylauEuTbaZ()
                    return True
        return False
    def nglQBfzxqztJKZZGNtEyLrQsaKQhyjMg(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, AFursZnPuECGUFTkCjDbdYIYmtroiqfB=None):
        with rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.mutex:
            if AFursZnPuECGUFTkCjDbdYIYmtroiqfB is None:
                return copy.deepcopy(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.history)
            elif AFursZnPuECGUFTkCjDbdYIYmtroiqfB in rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.history:
                return {AFursZnPuECGUFTkCjDbdYIYmtroiqfB: copy.deepcopy(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.history[AFursZnPuECGUFTkCjDbdYIYmtroiqfB])}
            else:
                return {}
    def BfUFoNCsskLewFIQhwJteOlDlTrsiYeM(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS):
        with rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.mutex:
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.history = {}
    def SWoBIKPEDgMZbmxkAhUBljmIrxWgVfpt(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, qfBoniFmTgUvqdSyxjmQmiqYnGgWUrtJ):
        with rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.mutex:
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.history.pop(qfBoniFmTgUvqdSyxjmQmiqYnGgWUrtJ, None)
