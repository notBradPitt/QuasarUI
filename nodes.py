import torch
import os
import sys
import json
import hashlib
import traceback
import math
import time
import random
from PIL import Image, ImageOps
from PIL.PngImagePlugin import PngInfo
import numpy as np
import safetensors.torch
sys.paTH.insert(0, os.paTH.join(os.paTH.dirname(os.paTH.realpath(__file__)), "quasar"))
import quasar.diffusers_load
import quasar.samplers
import quasar.sample
import quasar.sd
import quasar.utils
import quasar.controlnet
import quasar.clip_vision
import quasar.model_management
from quasar.cli_args import DukiculvUpjhZIVvaGinshRSKLSTgVVl
import importlib
import folder_paths
import latent_preview
def cZCqaSABLYzQIyICXPawBbAkRZgRglpn():
    quasar.model_management.cufzYbsmvfzVPCacJuRroKjPAHWqOusW()
def NIMMAjqKpMwgFfFMJGlJLJdwCPLKOQTM(GXNVXDlnsSLzkmussBPoJXgJwuXIiwsc=True):
    quasar.model_management.ggsUtIbLrBjTjYoMQwfUAZvlFgfjRNAK(GXNVXDlnsSLzkmussBPoJXgJwuXIiwsc)
tUEqFkJYdZNTmWQilLxLUFxmxzEWYVdq=8192
class xFugYlszeGKAKGYYiugpgdmBdgLdixjN:
    @classmethod
    def hGTeyOvpHejlssWPjkjTHIgcOKnCfnQl(uPePujIqMVDrwNvZQxJajkuaQFAcacjA):
        return {"required": {"text": ("STRING", {"multiline": True}), "clip": ("CLIP", )}}
    KmrPlNMyCntWtQIuwTzhYketzPaLUxAX = ("CONDITIONING",)
    DCeBXQFyPFIKUXphdMmctDGwHwXgHyTw = "encode"
    VHBvQQsdmXccHUVkiKRmkuIiUnjOTicH = "conditioning"
    def encode(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, WfkwoxQSNMJYbojfdczjmvPaQWPEJurJ, text):
        SKTuXdEkUTcvRMkWNnuUOzlxSfTAvHGL = WfkwoxQSNMJYbojfdczjmvPaQWPEJurJ.tokenize(text)
        BuoWBAnnMxyvqTGoSTHbQAlvPFWHbuUf, JEVUUwAOLsybeumSAyAWnfqCzuItnDIB = WfkwoxQSNMJYbojfdczjmvPaQWPEJurJ.encode_from_tokens(SKTuXdEkUTcvRMkWNnuUOzlxSfTAvHGL, return_pooled=True)
        return ([[BuoWBAnnMxyvqTGoSTHbQAlvPFWHbuUf, {"pooled_output": JEVUUwAOLsybeumSAyAWnfqCzuItnDIB}]], )
class qvtLCeXRQPHPReAlvcQavnYuAcYQHAdD:
    @classmethod
    def hGTeyOvpHejlssWPjkjTHIgcOKnCfnQl(uPePujIqMVDrwNvZQxJajkuaQFAcacjA):
        return {"required": {"conditioning_1": ("CONDITIONING", ), "conditioning_2": ("CONDITIONING", )}}
    KmrPlNMyCntWtQIuwTzhYketzPaLUxAX = ("CONDITIONING",)
    DCeBXQFyPFIKUXphdMmctDGwHwXgHyTw = "combine"
    VHBvQQsdmXccHUVkiKRmkuIiUnjOTicH = "conditioning"
    def EknVfXGLBgZEPAAAJxDVxtsWkRFSBXfn(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, conditioning_1, conditioning_2):
        return (conditioning_1 + conditioning_2, )
class lkWhhWnSlSzqLNbmCZhegjWlIcKUZzIc :
    @classmethod
    def hGTeyOvpHejlssWPjkjTHIgcOKnCfnQl(uPePujIqMVDrwNvZQxJajkuaQFAcacjA):
        return {"required": {"conditioning_to": ("CONDITIONING", ), "conditioning_from": ("CONDITIONING", ),
                              "conditioning_to_strength": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 1.0, "step": 0.01})
                             }}
    KmrPlNMyCntWtQIuwTzhYketzPaLUxAX = ("CONDITIONING",)
    DCeBXQFyPFIKUXphdMmctDGwHwXgHyTw = "addWeighted"
    VHBvQQsdmXccHUVkiKRmkuIiUnjOTicH = "conditioning"
    def XKMBNlwPShbSVxlLwWKAcahUlLsgmbce(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, conditioning_to, conditioning_from, conditioning_to_strength):
        iqymPVpxyjOWChGwBkTemSzHJbnJdAIz = []
        if len(conditioning_from) > 1:
            print("Warning: ConditioningAverage conditioning_from contains more than 1 cond, only the first one will actually be applied to conditioning_to.")
        pgPPMdYvXZoNNSfDDbHTMeqnVNhLruHM = conditioning_from[0][0]
        QQPitfUhikrTwLoNczHTqjrReZNVzOVi = conditioning_from[0][1].get("pooled_output", None)
        for HCXmerBqIMuTscBONzTGKYapYSxWTYHo in range(len(conditioning_to)):
            MStccjMYPXYbPLBRJuuGIaVGkOvnhCnE = conditioning_to[HCXmerBqIMuTscBONzTGKYapYSxWTYHo][0]
            YRpCXuomhsEEmhwulPxRKCvzIZFzmtkV = conditioning_to[HCXmerBqIMuTscBONzTGKYapYSxWTYHo][1].get("pooled_output", QQPitfUhikrTwLoNczHTqjrReZNVzOVi)
            WFuXrjgnWyCysWFupUPTADHAPjELsNbG = pgPPMdYvXZoNNSfDDbHTMeqnVNhLruHM[:,:MStccjMYPXYbPLBRJuuGIaVGkOvnhCnE.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[1]]
            if WFuXrjgnWyCysWFupUPTADHAPjELsNbG.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[1] < MStccjMYPXYbPLBRJuuGIaVGkOvnhCnE.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[1]:
                WFuXrjgnWyCysWFupUPTADHAPjELsNbG = torch.cat([WFuXrjgnWyCysWFupUPTADHAPjELsNbG] + [torch.zeros((1, (MStccjMYPXYbPLBRJuuGIaVGkOvnhCnE.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[1] - WFuXrjgnWyCysWFupUPTADHAPjELsNbG.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[1]), MStccjMYPXYbPLBRJuuGIaVGkOvnhCnE.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[2]))], yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk=1)
            EaVaaECttSYhxDvJVPgrDnCcVlduPEUd = torch.mul(MStccjMYPXYbPLBRJuuGIaVGkOvnhCnE, conditioning_to_strength) + torch.mul(WFuXrjgnWyCysWFupUPTADHAPjELsNbG, (1.0 - conditioning_to_strength))
            WmSwahUzmeLCgSvMwJBmDhYZnefdmRmV = conditioning_to[HCXmerBqIMuTscBONzTGKYapYSxWTYHo][1].copy()
            if QQPitfUhikrTwLoNczHTqjrReZNVzOVi is not None and YRpCXuomhsEEmhwulPxRKCvzIZFzmtkV is not None:
                WmSwahUzmeLCgSvMwJBmDhYZnefdmRmV["pooled_output"] = torch.mul(YRpCXuomhsEEmhwulPxRKCvzIZFzmtkV, conditioning_to_strength) + torch.mul(QQPitfUhikrTwLoNczHTqjrReZNVzOVi, (1.0 - conditioning_to_strength))
            elif QQPitfUhikrTwLoNczHTqjrReZNVzOVi is not None:
                WmSwahUzmeLCgSvMwJBmDhYZnefdmRmV["pooled_output"] = QQPitfUhikrTwLoNczHTqjrReZNVzOVi
            zXHJFiFFvWqeQIAxyaTGMUgoRaHrYzjK = [EaVaaECttSYhxDvJVPgrDnCcVlduPEUd, WmSwahUzmeLCgSvMwJBmDhYZnefdmRmV]
            iqymPVpxyjOWChGwBkTemSzHJbnJdAIz.append(zXHJFiFFvWqeQIAxyaTGMUgoRaHrYzjK)
        return (iqymPVpxyjOWChGwBkTemSzHJbnJdAIz, )
class VXMFcQDwHLDiOqVxzpyZwaXkTroGCAPs:
    @classmethod
    def hGTeyOvpHejlssWPjkjTHIgcOKnCfnQl(uPePujIqMVDrwNvZQxJajkuaQFAcacjA):
        return {"required": {
            "conditioning_to": ("CONDITIONING",),
            "conditioning_from": ("CONDITIONING",),
            }}
    KmrPlNMyCntWtQIuwTzhYketzPaLUxAX = ("CONDITIONING",)
    DCeBXQFyPFIKUXphdMmctDGwHwXgHyTw = "concat"
    VHBvQQsdmXccHUVkiKRmkuIiUnjOTicH = "conditioning"
    def DLwjOtTssoVQwfNOBntGtewcESlYttnq(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, conditioning_to, conditioning_from):
        iqymPVpxyjOWChGwBkTemSzHJbnJdAIz = []
        if len(conditioning_from) > 1:
            print("Warning: ConditioningConcat conditioning_from contains more than 1 cond, only the first one will actually be applied to conditioning_to.")
        pgPPMdYvXZoNNSfDDbHTMeqnVNhLruHM = conditioning_from[0][0]
        for HCXmerBqIMuTscBONzTGKYapYSxWTYHo in range(len(conditioning_to)):
            MStccjMYPXYbPLBRJuuGIaVGkOvnhCnE = conditioning_to[HCXmerBqIMuTscBONzTGKYapYSxWTYHo][0]
            EaVaaECttSYhxDvJVPgrDnCcVlduPEUd = torch.cat((MStccjMYPXYbPLBRJuuGIaVGkOvnhCnE, pgPPMdYvXZoNNSfDDbHTMeqnVNhLruHM),1)
            zXHJFiFFvWqeQIAxyaTGMUgoRaHrYzjK = [EaVaaECttSYhxDvJVPgrDnCcVlduPEUd, conditioning_to[HCXmerBqIMuTscBONzTGKYapYSxWTYHo][1].copy()]
            iqymPVpxyjOWChGwBkTemSzHJbnJdAIz.append(zXHJFiFFvWqeQIAxyaTGMUgoRaHrYzjK)
        return (iqymPVpxyjOWChGwBkTemSzHJbnJdAIz, )
class uiryePJpXaKctwLymJTRGmDYTnmFpOVu:
    @classmethod
    def hGTeyOvpHejlssWPjkjTHIgcOKnCfnQl(uPePujIqMVDrwNvZQxJajkuaQFAcacjA):
        return {"required": {"conditioning": ("CONDITIONING", ),
                              "width": ("INT", {"default": 64, "min": 64, "max": tUEqFkJYdZNTmWQilLxLUFxmxzEWYVdq, "step": 8}),
                              "height": ("INT", {"default": 64, "min": 64, "max": tUEqFkJYdZNTmWQilLxLUFxmxzEWYVdq, "step": 8}),
                              "x": ("INT", {"default": 0, "min": 0, "max": tUEqFkJYdZNTmWQilLxLUFxmxzEWYVdq, "step": 8}),
                              "y": ("INT", {"default": 0, "min": 0, "max": tUEqFkJYdZNTmWQilLxLUFxmxzEWYVdq, "step": 8}),
                              "strength": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 10.0, "step": 0.01}),
                             }}
    KmrPlNMyCntWtQIuwTzhYketzPaLUxAX = ("CONDITIONING",)
    DCeBXQFyPFIKUXphdMmctDGwHwXgHyTw = "append"
    VHBvQQsdmXccHUVkiKRmkuIiUnjOTicH = "conditioning"
    def append(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, nKYmGWBrcYyADcANVAMJtCeHkjgKBdNR, QfeoFYGsEQNWblsqXsRKWQpzeXgWujaz, yhGxnlfJCKaDHyDtiYhJHxHFcooDKiMM, NECAaWUrFGIXcLimrerEYmxYIykQBfXb, ZljqvWVaiqYAYdTFzQHSTXFDKwgstKaW, strength):
        cjHIelcAqVoHWdLcgzuZiBumKNTVADsY = []
        for XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz in nKYmGWBrcYyADcANVAMJtCeHkjgKBdNR:
            zXHJFiFFvWqeQIAxyaTGMUgoRaHrYzjK = [XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz[0], XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz[1].copy()]
            zXHJFiFFvWqeQIAxyaTGMUgoRaHrYzjK[1]['area'] = (yhGxnlfJCKaDHyDtiYhJHxHFcooDKiMM // 8, QfeoFYGsEQNWblsqXsRKWQpzeXgWujaz // 8, ZljqvWVaiqYAYdTFzQHSTXFDKwgstKaW // 8, NECAaWUrFGIXcLimrerEYmxYIykQBfXb // 8)
            zXHJFiFFvWqeQIAxyaTGMUgoRaHrYzjK[1]['strength'] = strength
            zXHJFiFFvWqeQIAxyaTGMUgoRaHrYzjK[1]['set_area_to_bounds'] = False
            cjHIelcAqVoHWdLcgzuZiBumKNTVADsY.append(zXHJFiFFvWqeQIAxyaTGMUgoRaHrYzjK)
        return (cjHIelcAqVoHWdLcgzuZiBumKNTVADsY, )
class MOhYaVYOzpeAtEFqcdIAWHKLQcntTzGT:
    @classmethod
    def hGTeyOvpHejlssWPjkjTHIgcOKnCfnQl(uPePujIqMVDrwNvZQxJajkuaQFAcacjA):
        return {"required": {"conditioning": ("CONDITIONING", ),
                              "width": ("FLOAT", {"default": 1.0, "min": 0, "max": 1.0, "step": 0.01}),
                              "height": ("FLOAT", {"default": 1.0, "min": 0, "max": 1.0, "step": 0.01}),
                              "x": ("FLOAT", {"default": 0, "min": 0, "max": 1.0, "step": 0.01}),
                              "y": ("FLOAT", {"default": 0, "min": 0, "max": 1.0, "step": 0.01}),
                              "strength": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 10.0, "step": 0.01}),
                             }}
    KmrPlNMyCntWtQIuwTzhYketzPaLUxAX = ("CONDITIONING",)
    DCeBXQFyPFIKUXphdMmctDGwHwXgHyTw = "append"
    VHBvQQsdmXccHUVkiKRmkuIiUnjOTicH = "conditioning"
    def append(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, nKYmGWBrcYyADcANVAMJtCeHkjgKBdNR, QfeoFYGsEQNWblsqXsRKWQpzeXgWujaz, yhGxnlfJCKaDHyDtiYhJHxHFcooDKiMM, NECAaWUrFGIXcLimrerEYmxYIykQBfXb, ZljqvWVaiqYAYdTFzQHSTXFDKwgstKaW, strength):
        cjHIelcAqVoHWdLcgzuZiBumKNTVADsY = []
        for XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz in nKYmGWBrcYyADcANVAMJtCeHkjgKBdNR:
            zXHJFiFFvWqeQIAxyaTGMUgoRaHrYzjK = [XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz[0], XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz[1].copy()]
            zXHJFiFFvWqeQIAxyaTGMUgoRaHrYzjK[1]['area'] = ("percentage", yhGxnlfJCKaDHyDtiYhJHxHFcooDKiMM, QfeoFYGsEQNWblsqXsRKWQpzeXgWujaz, ZljqvWVaiqYAYdTFzQHSTXFDKwgstKaW, NECAaWUrFGIXcLimrerEYmxYIykQBfXb)
            zXHJFiFFvWqeQIAxyaTGMUgoRaHrYzjK[1]['strength'] = strength
            zXHJFiFFvWqeQIAxyaTGMUgoRaHrYzjK[1]['set_area_to_bounds'] = False
            cjHIelcAqVoHWdLcgzuZiBumKNTVADsY.append(zXHJFiFFvWqeQIAxyaTGMUgoRaHrYzjK)
        return (cjHIelcAqVoHWdLcgzuZiBumKNTVADsY, )
class sGJAjzbAeEjMjezMdZmhSjpUrztuIxrd:
    @classmethod
    def hGTeyOvpHejlssWPjkjTHIgcOKnCfnQl(uPePujIqMVDrwNvZQxJajkuaQFAcacjA):
        return {"required": {"conditioning": ("CONDITIONING", ),
                              "mask": ("MASK", ),
                              "strength": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 10.0, "step": 0.01}),
                              "set_cond_area": (["default", "mask bounds"],),
                             }}
    KmrPlNMyCntWtQIuwTzhYketzPaLUxAX = ("CONDITIONING",)
    DCeBXQFyPFIKUXphdMmctDGwHwXgHyTw = "append"
    VHBvQQsdmXccHUVkiKRmkuIiUnjOTicH = "conditioning"
    def append(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, nKYmGWBrcYyADcANVAMJtCeHkjgKBdNR, KHpRlHOzblljQyskecSxzUuWZtneWwta, set_cond_area, strength):
        cjHIelcAqVoHWdLcgzuZiBumKNTVADsY = []
        MXEQWbluiOHFSuTIGDmpHNbNMuAJFDrG = False
        if set_cond_area != "default":
            MXEQWbluiOHFSuTIGDmpHNbNMuAJFDrG = True
        if len(KHpRlHOzblljQyskecSxzUuWZtneWwta.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg) < 3:
            KHpRlHOzblljQyskecSxzUuWZtneWwta = KHpRlHOzblljQyskecSxzUuWZtneWwta.unsqueeze(0)
        for XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz in nKYmGWBrcYyADcANVAMJtCeHkjgKBdNR:
            zXHJFiFFvWqeQIAxyaTGMUgoRaHrYzjK = [XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz[0], XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz[1].copy()]
            _, xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab, AeIrbRXDkpZlClJGwzMknCltTQQdmhvu = KHpRlHOzblljQyskecSxzUuWZtneWwta.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg
            zXHJFiFFvWqeQIAxyaTGMUgoRaHrYzjK[1]['mask'] = KHpRlHOzblljQyskecSxzUuWZtneWwta
            zXHJFiFFvWqeQIAxyaTGMUgoRaHrYzjK[1]['set_area_to_bounds'] = MXEQWbluiOHFSuTIGDmpHNbNMuAJFDrG
            zXHJFiFFvWqeQIAxyaTGMUgoRaHrYzjK[1]['mask_strength'] = strength
            cjHIelcAqVoHWdLcgzuZiBumKNTVADsY.append(zXHJFiFFvWqeQIAxyaTGMUgoRaHrYzjK)
        return (cjHIelcAqVoHWdLcgzuZiBumKNTVADsY, )
class MbOIIXitffUZYmaOhrWLoXmkaSHBaWAJ:
    @classmethod
    def hGTeyOvpHejlssWPjkjTHIgcOKnCfnQl(uPePujIqMVDrwNvZQxJajkuaQFAcacjA):
        return {"required": {"conditioning": ("CONDITIONING", )}}
    KmrPlNMyCntWtQIuwTzhYketzPaLUxAX = ("CONDITIONING",)
    DCeBXQFyPFIKUXphdMmctDGwHwXgHyTw = "zero_out"
    VHBvQQsdmXccHUVkiKRmkuIiUnjOTicH = "advanced/conditioning"
    def wIJVLvhRcrvalZtaXCWiynpisRCDKUQN(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, nKYmGWBrcYyADcANVAMJtCeHkjgKBdNR):
        cjHIelcAqVoHWdLcgzuZiBumKNTVADsY = []
        for XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz in nKYmGWBrcYyADcANVAMJtCeHkjgKBdNR:
            TXGwYXNLgQsYzfHHpRBDJGFCFZEClzIo = XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz[1].copy()
            if "pooled_output" in TXGwYXNLgQsYzfHHpRBDJGFCFZEClzIo:
                TXGwYXNLgQsYzfHHpRBDJGFCFZEClzIo["pooled_output"] = torch.zeros_like(TXGwYXNLgQsYzfHHpRBDJGFCFZEClzIo["pooled_output"])
            zXHJFiFFvWqeQIAxyaTGMUgoRaHrYzjK = [torch.zeros_like(XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz[0]), TXGwYXNLgQsYzfHHpRBDJGFCFZEClzIo]
            cjHIelcAqVoHWdLcgzuZiBumKNTVADsY.append(zXHJFiFFvWqeQIAxyaTGMUgoRaHrYzjK)
        return (cjHIelcAqVoHWdLcgzuZiBumKNTVADsY, )
class xkewWZVEtrrwkpVxpgXOzhuLNUDrAyoA:
    @classmethod
    def hGTeyOvpHejlssWPjkjTHIgcOKnCfnQl(uPePujIqMVDrwNvZQxJajkuaQFAcacjA):
        return {"required": {"conditioning": ("CONDITIONING", ),
                             "start": ("FLOAT", {"default": 0.0, "min": 0.0, "max": 1.0, "step": 0.001}),
                             "end": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 1.0, "step": 0.001})
                             }}
    KmrPlNMyCntWtQIuwTzhYketzPaLUxAX = ("CONDITIONING",)
    DCeBXQFyPFIKUXphdMmctDGwHwXgHyTw = "set_range"
    VHBvQQsdmXccHUVkiKRmkuIiUnjOTicH = "advanced/conditioning"
    def lltoTuldZKQmXxlemNkBHTZQcxQkpAYi(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, nKYmGWBrcYyADcANVAMJtCeHkjgKBdNR, tUuYqnLjDXuftYgMagGpmrobxWgfcbgq, lGLYgANCchGMWZfAOSVuiBulTGaEVaQM):
        cjHIelcAqVoHWdLcgzuZiBumKNTVADsY = []
        for XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz in nKYmGWBrcYyADcANVAMJtCeHkjgKBdNR:
            TXGwYXNLgQsYzfHHpRBDJGFCFZEClzIo = XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz[1].copy()
            TXGwYXNLgQsYzfHHpRBDJGFCFZEClzIo['start_percent'] = 1.0 - tUuYqnLjDXuftYgMagGpmrobxWgfcbgq
            TXGwYXNLgQsYzfHHpRBDJGFCFZEClzIo['end_percent'] = 1.0 - lGLYgANCchGMWZfAOSVuiBulTGaEVaQM
            zXHJFiFFvWqeQIAxyaTGMUgoRaHrYzjK = [XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz[0], TXGwYXNLgQsYzfHHpRBDJGFCFZEClzIo]
            cjHIelcAqVoHWdLcgzuZiBumKNTVADsY.append(zXHJFiFFvWqeQIAxyaTGMUgoRaHrYzjK)
        return (cjHIelcAqVoHWdLcgzuZiBumKNTVADsY, )
class tkeFAusZeYzBDPFSpXbBAbSiGuguweLJ:
    @classmethod
    def hGTeyOvpHejlssWPjkjTHIgcOKnCfnQl(uPePujIqMVDrwNvZQxJajkuaQFAcacjA):
        return {"required": { "samples": ("LATENT", ), "vae": ("VAE", )}}
    KmrPlNMyCntWtQIuwTzhYketzPaLUxAX = ("IMAGE",)
    DCeBXQFyPFIKUXphdMmctDGwHwXgHyTw = "decode"
    VHBvQQsdmXccHUVkiKRmkuIiUnjOTicH = "latent"
    def DzeufPfapTAWMrnfPsMZfOIZEyGYmPHT(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, PBWbWRIKcHQYxJBaTdydnolXDaFqlFKi, bfpFhSQCEeSgZQwablzNZDcPruUlpnjs):
        return (PBWbWRIKcHQYxJBaTdydnolXDaFqlFKi.DzeufPfapTAWMrnfPsMZfOIZEyGYmPHT(bfpFhSQCEeSgZQwablzNZDcPruUlpnjs["samples"]), )
class CcxzNqovaHQVHpxKUeCssGusFOficgdF:
    @classmethod
    def hGTeyOvpHejlssWPjkjTHIgcOKnCfnQl(uPePujIqMVDrwNvZQxJajkuaQFAcacjA):
        return {"required": {"samples": ("LATENT", ), "vae": ("VAE", ),
                             "tile_size": ("INT", {"default": 512, "min": 320, "max": 4096, "step": 64})
                            }}
    KmrPlNMyCntWtQIuwTzhYketzPaLUxAX = ("IMAGE",)
    DCeBXQFyPFIKUXphdMmctDGwHwXgHyTw = "decode"
    VHBvQQsdmXccHUVkiKRmkuIiUnjOTicH = "_for_testing"
    def DzeufPfapTAWMrnfPsMZfOIZEyGYmPHT(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, PBWbWRIKcHQYxJBaTdydnolXDaFqlFKi, bfpFhSQCEeSgZQwablzNZDcPruUlpnjs, tile_size):
        return (PBWbWRIKcHQYxJBaTdydnolXDaFqlFKi.decode_tiled(bfpFhSQCEeSgZQwablzNZDcPruUlpnjs["samples"], tile_x=tile_size // 8, tile_y=tile_size // 8, ), )
class yHdOrZGLzaZsuJPMNoADlrOQJtKypbUC:
    @classmethod
    def hGTeyOvpHejlssWPjkjTHIgcOKnCfnQl(uPePujIqMVDrwNvZQxJajkuaQFAcacjA):
        return {"required": { "pixels": ("IMAGE", ), "vae": ("VAE", )}}
    KmrPlNMyCntWtQIuwTzhYketzPaLUxAX = ("LATENT",)
    DCeBXQFyPFIKUXphdMmctDGwHwXgHyTw = "encode"
    VHBvQQsdmXccHUVkiKRmkuIiUnjOTicH = "latent"
    @staticmethod
    def snFNHFoUdAZQEYQCcLrajgOuliPdcfLR(yRvviORwdqEhCaLCkyVjtwxFonOdeNcP):
        NECAaWUrFGIXcLimrerEYmxYIykQBfXb = (yRvviORwdqEhCaLCkyVjtwxFonOdeNcP.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[1] // 8) * 8
        ZljqvWVaiqYAYdTFzQHSTXFDKwgstKaW = (yRvviORwdqEhCaLCkyVjtwxFonOdeNcP.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[2] // 8) * 8
        if yRvviORwdqEhCaLCkyVjtwxFonOdeNcP.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[1] != NECAaWUrFGIXcLimrerEYmxYIykQBfXb or yRvviORwdqEhCaLCkyVjtwxFonOdeNcP.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[2] != ZljqvWVaiqYAYdTFzQHSTXFDKwgstKaW:
            mjTAPKgRyErnNpDWehUthBVOgGxXodYk = (yRvviORwdqEhCaLCkyVjtwxFonOdeNcP.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[1] % 8) // 2
            BgshOdAbnkGhUyelDmBsZhLVsoWgocfj = (yRvviORwdqEhCaLCkyVjtwxFonOdeNcP.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[2] % 8) // 2
            yRvviORwdqEhCaLCkyVjtwxFonOdeNcP = yRvviORwdqEhCaLCkyVjtwxFonOdeNcP[:, mjTAPKgRyErnNpDWehUthBVOgGxXodYk:NECAaWUrFGIXcLimrerEYmxYIykQBfXb + mjTAPKgRyErnNpDWehUthBVOgGxXodYk, BgshOdAbnkGhUyelDmBsZhLVsoWgocfj:ZljqvWVaiqYAYdTFzQHSTXFDKwgstKaW + BgshOdAbnkGhUyelDmBsZhLVsoWgocfj, :]
        return yRvviORwdqEhCaLCkyVjtwxFonOdeNcP
    def encode(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, PBWbWRIKcHQYxJBaTdydnolXDaFqlFKi, yRvviORwdqEhCaLCkyVjtwxFonOdeNcP):
        yRvviORwdqEhCaLCkyVjtwxFonOdeNcP = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.snFNHFoUdAZQEYQCcLrajgOuliPdcfLR(yRvviORwdqEhCaLCkyVjtwxFonOdeNcP)
        XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz = PBWbWRIKcHQYxJBaTdydnolXDaFqlFKi.encode(yRvviORwdqEhCaLCkyVjtwxFonOdeNcP[:,:,:,:3])
        return ({"samples":XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz}, )
class GnDUARhnfPPMFDGTRWPeOnvfVZuTBjBJ:
    @classmethod
    def hGTeyOvpHejlssWPjkjTHIgcOKnCfnQl(uPePujIqMVDrwNvZQxJajkuaQFAcacjA):
        return {"required": {"pixels": ("IMAGE", ), "vae": ("VAE", ),
                             "tile_size": ("INT", {"default": 512, "min": 320, "max": 4096, "step": 64})
                            }}
    KmrPlNMyCntWtQIuwTzhYketzPaLUxAX = ("LATENT",)
    DCeBXQFyPFIKUXphdMmctDGwHwXgHyTw = "encode"
    VHBvQQsdmXccHUVkiKRmkuIiUnjOTicH = "_for_testing"
    def encode(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, PBWbWRIKcHQYxJBaTdydnolXDaFqlFKi, yRvviORwdqEhCaLCkyVjtwxFonOdeNcP, tile_size):
        yRvviORwdqEhCaLCkyVjtwxFonOdeNcP = yHdOrZGLzaZsuJPMNoADlrOQJtKypbUC.snFNHFoUdAZQEYQCcLrajgOuliPdcfLR(yRvviORwdqEhCaLCkyVjtwxFonOdeNcP)
        XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz = PBWbWRIKcHQYxJBaTdydnolXDaFqlFKi.encode_tiled(yRvviORwdqEhCaLCkyVjtwxFonOdeNcP[:,:,:,:3], tile_x=tile_size, tile_y=tile_size, )
        return ({"samples":XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz}, )
class XcLrUEEGwySqZlhOsrsQexLVMCIATlUX:
    @classmethod
    def hGTeyOvpHejlssWPjkjTHIgcOKnCfnQl(uPePujIqMVDrwNvZQxJajkuaQFAcacjA):
        return {"required": { "pixels": ("IMAGE", ), "vae": ("VAE", ), "mask": ("MASK", ), "grow_mask_by": ("INT", {"default": 6, "min": 0, "max": 64, "step": 1}),}}
    KmrPlNMyCntWtQIuwTzhYketzPaLUxAX = ("LATENT",)
    DCeBXQFyPFIKUXphdMmctDGwHwXgHyTw = "encode"
    VHBvQQsdmXccHUVkiKRmkuIiUnjOTicH = "latent/inpaint"
    def encode(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, PBWbWRIKcHQYxJBaTdydnolXDaFqlFKi, yRvviORwdqEhCaLCkyVjtwxFonOdeNcP, KHpRlHOzblljQyskecSxzUuWZtneWwta, grow_mask_by=6):
        NECAaWUrFGIXcLimrerEYmxYIykQBfXb = (yRvviORwdqEhCaLCkyVjtwxFonOdeNcP.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[1] // 8) * 8
        ZljqvWVaiqYAYdTFzQHSTXFDKwgstKaW = (yRvviORwdqEhCaLCkyVjtwxFonOdeNcP.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[2] // 8) * 8
        KHpRlHOzblljQyskecSxzUuWZtneWwta = torch.nn.functional.interpolate(KHpRlHOzblljQyskecSxzUuWZtneWwta.reshape((-1, 1, KHpRlHOzblljQyskecSxzUuWZtneWwta.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[-2], KHpRlHOzblljQyskecSxzUuWZtneWwta.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[-1])), vqDBJgidQufnKyAltPYRqiKGjmztArDJ=(yRvviORwdqEhCaLCkyVjtwxFonOdeNcP.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[1], yRvviORwdqEhCaLCkyVjtwxFonOdeNcP.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[2]), bPTwwoDdWiuYqhtrDEHoDbHGiYcwcsQC="bilinear")
        yRvviORwdqEhCaLCkyVjtwxFonOdeNcP = yRvviORwdqEhCaLCkyVjtwxFonOdeNcP.tEcQvpBwXwdqvKxRTLEBROBUyPoodldL()
        if yRvviORwdqEhCaLCkyVjtwxFonOdeNcP.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[1] != NECAaWUrFGIXcLimrerEYmxYIykQBfXb or yRvviORwdqEhCaLCkyVjtwxFonOdeNcP.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[2] != ZljqvWVaiqYAYdTFzQHSTXFDKwgstKaW:
            mjTAPKgRyErnNpDWehUthBVOgGxXodYk = (yRvviORwdqEhCaLCkyVjtwxFonOdeNcP.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[1] % 8) // 2
            BgshOdAbnkGhUyelDmBsZhLVsoWgocfj = (yRvviORwdqEhCaLCkyVjtwxFonOdeNcP.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[2] % 8) // 2
            yRvviORwdqEhCaLCkyVjtwxFonOdeNcP = yRvviORwdqEhCaLCkyVjtwxFonOdeNcP[:,mjTAPKgRyErnNpDWehUthBVOgGxXodYk:NECAaWUrFGIXcLimrerEYmxYIykQBfXb + mjTAPKgRyErnNpDWehUthBVOgGxXodYk, BgshOdAbnkGhUyelDmBsZhLVsoWgocfj:ZljqvWVaiqYAYdTFzQHSTXFDKwgstKaW + BgshOdAbnkGhUyelDmBsZhLVsoWgocfj,:]
            KHpRlHOzblljQyskecSxzUuWZtneWwta = KHpRlHOzblljQyskecSxzUuWZtneWwta[:,:,mjTAPKgRyErnNpDWehUthBVOgGxXodYk:NECAaWUrFGIXcLimrerEYmxYIykQBfXb + mjTAPKgRyErnNpDWehUthBVOgGxXodYk, BgshOdAbnkGhUyelDmBsZhLVsoWgocfj:ZljqvWVaiqYAYdTFzQHSTXFDKwgstKaW + BgshOdAbnkGhUyelDmBsZhLVsoWgocfj]
        if grow_mask_by == 0:
            KLTTBAAGhdWFJBvxNyzFefTVgdDrwlys = KHpRlHOzblljQyskecSxzUuWZtneWwta
        else:
            ftzHWwcFwrOvghWNPKIFSlEPtLJaqkze = torch.ones((1, 1, grow_mask_by, grow_mask_by))
            sdxdTSjnkAOjlGmltQHvLiHRDstMzpAP = math.ceil((grow_mask_by - 1) / 2)
            KLTTBAAGhdWFJBvxNyzFefTVgdDrwlys = torch.clamp(torch.nn.functional.conv2d(KHpRlHOzblljQyskecSxzUuWZtneWwta.round(), ftzHWwcFwrOvghWNPKIFSlEPtLJaqkze, sdxdTSjnkAOjlGmltQHvLiHRDstMzpAP=sdxdTSjnkAOjlGmltQHvLiHRDstMzpAP), 0, 1)
        FTosLGldclAzaiNbwuLMIEtXfrZQpTnU = (1.0 - KHpRlHOzblljQyskecSxzUuWZtneWwta.round()).squeeze(1)
        for HCXmerBqIMuTscBONzTGKYapYSxWTYHo in range(3):
            yRvviORwdqEhCaLCkyVjtwxFonOdeNcP[:,:,:,HCXmerBqIMuTscBONzTGKYapYSxWTYHo] -= 0.5
            yRvviORwdqEhCaLCkyVjtwxFonOdeNcP[:,:,:,HCXmerBqIMuTscBONzTGKYapYSxWTYHo] *= FTosLGldclAzaiNbwuLMIEtXfrZQpTnU
            yRvviORwdqEhCaLCkyVjtwxFonOdeNcP[:,:,:,HCXmerBqIMuTscBONzTGKYapYSxWTYHo] += 0.5
        XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz = PBWbWRIKcHQYxJBaTdydnolXDaFqlFKi.encode(yRvviORwdqEhCaLCkyVjtwxFonOdeNcP)
        return ({"samples":XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz, "noise_mask": (KLTTBAAGhdWFJBvxNyzFefTVgdDrwlys[:,:,:NECAaWUrFGIXcLimrerEYmxYIykQBfXb,:ZljqvWVaiqYAYdTFzQHSTXFDKwgstKaW].round())}, )
class KNkmvkLrAPwddvOOzCKLuJvoplliUlqI:
    def __init__(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS):
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.DIUNPQiJKWsgpSdsJVPWmcWtoPKBTsdh = folder_paths.gZpMXpjIEjIdWmJXOqOJEBRXYgziLydo()
    @classmethod
    def hGTeyOvpHejlssWPjkjTHIgcOKnCfnQl(uPePujIqMVDrwNvZQxJajkuaQFAcacjA):
        return {"required": { "samples": ("LATENT", ),
                              "filename_prefix": ("STRING", {"default": "latents/QuasarUI"})},
                "hidden": {"prompt": "PROMPT", "extra_pnginfo": "EXTRA_PNGINFO"},
                }
    KmrPlNMyCntWtQIuwTzhYketzPaLUxAX = ()
    DCeBXQFyPFIKUXphdMmctDGwHwXgHyTw = "save"
    AQnTlfqkrmdAAnLjLNUFibEHomwVhMHv = True
    VHBvQQsdmXccHUVkiKRmkuIiUnjOTicH = "_for_testing"
    def PXhZDpeqZAdDBfrowpMPOPAWwzXhVAFM(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, bfpFhSQCEeSgZQwablzNZDcPruUlpnjs, azafsUqgjjnMJDTDVblsTwqgMmfrAEPm="QuasarUI", qKBREHoSgcMHYVCNTapmPyODbBOyQAyv=None, extra_pnginfo=None):
        NSnmtWjKbAQhROMkmRknqzSaUCojgOin, VpsbOZzufynrTFUvvRofTQeRCOCIKJOM, etmXhuRDTfPuCYAlpkCmiMFiODmDHghZ, EijzAwkTdadIdbBCcDEUbEYNNcstskwi, azafsUqgjjnMJDTDVblsTwqgMmfrAEPm = folder_paths.RzAZobMvYWLmMtiqbeSollhpzISOJhWp(azafsUqgjjnMJDTDVblsTwqgMmfrAEPm, rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.DIUNPQiJKWsgpSdsJVPWmcWtoPKBTsdh)
        GjFngyPEbvmyWKdohCWlJwQdGDmPFMJv = ""
        if qKBREHoSgcMHYVCNTapmPyODbBOyQAyv is not None:
            GjFngyPEbvmyWKdohCWlJwQdGDmPFMJv = json.dumps(qKBREHoSgcMHYVCNTapmPyODbBOyQAyv)
        bpGrrorhUTFbOXgOoJWMtNiVeQXHqzbi = None
        if not DukiculvUpjhZIVvaGinshRSKLSTgVVl.disable_metadata:
            bpGrrorhUTFbOXgOoJWMtNiVeQXHqzbi = {"prompt": GjFngyPEbvmyWKdohCWlJwQdGDmPFMJv}
            if extra_pnginfo is not None:
                for NECAaWUrFGIXcLimrerEYmxYIykQBfXb in extra_pnginfo:
                    bpGrrorhUTFbOXgOoJWMtNiVeQXHqzbi[NECAaWUrFGIXcLimrerEYmxYIykQBfXb] = json.dumps(extra_pnginfo[NECAaWUrFGIXcLimrerEYmxYIykQBfXb])
        GGrVUpHsMvVvEYhZgyWAlwaKJQserwts = f"{filename}_{counter:05}_.latent"
        NRctuwUflnRJCsQaTaCNgYJowifAWPqJ = list()
        NRctuwUflnRJCsQaTaCNgYJowifAWPqJ.append({
            "filename": GGrVUpHsMvVvEYhZgyWAlwaKJQserwts,
            "subfolder": EijzAwkTdadIdbBCcDEUbEYNNcstskwi,
            "type": "output"
        })
        GGrVUpHsMvVvEYhZgyWAlwaKJQserwts = os.paTH.join(NSnmtWjKbAQhROMkmRknqzSaUCojgOin, GGrVUpHsMvVvEYhZgyWAlwaKJQserwts)
        pwTxzdNTJGMWEFORftJTEtPYMMiKwDuP = {}
        pwTxzdNTJGMWEFORftJTEtPYMMiKwDuP["latent_tensor"] = bfpFhSQCEeSgZQwablzNZDcPruUlpnjs["samples"]
        pwTxzdNTJGMWEFORftJTEtPYMMiKwDuP["latent_format_version_0"] = torch.xPmCFphFKpGMpIsczaSKHmMgRPZzJwla([])
        quasar.utils.save_torch_file(pwTxzdNTJGMWEFORftJTEtPYMMiKwDuP, GGrVUpHsMvVvEYhZgyWAlwaKJQserwts, bpGrrorhUTFbOXgOoJWMtNiVeQXHqzbi=bpGrrorhUTFbOXgOoJWMtNiVeQXHqzbi)
        return { "ui": { "latents": NRctuwUflnRJCsQaTaCNgYJowifAWPqJ } }
class VTKGSJncLiFeXyZiGvTCgFXfSARuMFAd:
    @classmethod
    def hGTeyOvpHejlssWPjkjTHIgcOKnCfnQl(uPePujIqMVDrwNvZQxJajkuaQFAcacjA):
        GhiEkpNFOqhdputxuaWhbKlilzZXSMPs = folder_paths.oLxzopmIeTVwZiWTpRvVAVRpJiaEjmiS()
        DTcHrFlDIwbrZDZHTOmAOTxRFqptCgyE = [f for f in os.listdir(GhiEkpNFOqhdputxuaWhbKlilzZXSMPs) if os.paTH.isfile(os.paTH.join(GhiEkpNFOqhdputxuaWhbKlilzZXSMPs, f)) and f.endswith(".latent")]
        return {"required": {"latent": [sorted(DTcHrFlDIwbrZDZHTOmAOTxRFqptCgyE), ]}, }
    VHBvQQsdmXccHUVkiKRmkuIiUnjOTicH = "_for_testing"
    KmrPlNMyCntWtQIuwTzhYketzPaLUxAX = ("LATENT", )
    DCeBXQFyPFIKUXphdMmctDGwHwXgHyTw = "load"
    def yjjLwfEWtXKFjwwmuqReIXUDoGaUzfxz(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, CBTHgqHIDKYRBmSTkKCsLapKGpsubmaU):
        vOJbhjoLfYZpEldBxWNHhCmaFfiJMWew = folder_paths.OPtRRiXTVYmRqsnzHEbbUWCzjjPfVhOl(CBTHgqHIDKYRBmSTkKCsLapKGpsubmaU)
        CBTHgqHIDKYRBmSTkKCsLapKGpsubmaU = safetensors.torch.load_file(vOJbhjoLfYZpEldBxWNHhCmaFfiJMWew, fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc="cpu")
        EWOzAFPZCwlkwatzyybUCZgINJrsJyHo = 1.0
        if "latent_format_version_0" not in CBTHgqHIDKYRBmSTkKCsLapKGpsubmaU:
            EWOzAFPZCwlkwatzyybUCZgINJrsJyHo = 1.0 / 0.18215
        bfpFhSQCEeSgZQwablzNZDcPruUlpnjs = {"samples": CBTHgqHIDKYRBmSTkKCsLapKGpsubmaU["latent_tensor"].float() * EWOzAFPZCwlkwatzyybUCZgINJrsJyHo}
        return (bfpFhSQCEeSgZQwablzNZDcPruUlpnjs, )
    @classmethod
    def xChqCjJamsdgOcXgHPiSyUitQVgwKEUj(uPePujIqMVDrwNvZQxJajkuaQFAcacjA, CBTHgqHIDKYRBmSTkKCsLapKGpsubmaU):
        SsDANhHMZfeDdUZakZVrHtRdKyhJyvRq = folder_paths.OPtRRiXTVYmRqsnzHEbbUWCzjjPfVhOl(CBTHgqHIDKYRBmSTkKCsLapKGpsubmaU)
        FTosLGldclAzaiNbwuLMIEtXfrZQpTnU = hashlib.sha256()
        with open(SsDANhHMZfeDdUZakZVrHtRdKyhJyvRq, 'rb') as f:
            FTosLGldclAzaiNbwuLMIEtXfrZQpTnU.update(f.read())
        return FTosLGldclAzaiNbwuLMIEtXfrZQpTnU.digest().hex()
    @classmethod
    def zdUBozptADSRFmScDjrsNpGclJRkfHVt(uPePujIqMVDrwNvZQxJajkuaQFAcacjA, CBTHgqHIDKYRBmSTkKCsLapKGpsubmaU):
        if not folder_paths.LuEtoKSPwnkgulAqhArQxPlLlkJrpWJM(CBTHgqHIDKYRBmSTkKCsLapKGpsubmaU):
            return "Invalid latent file: {}".format(CBTHgqHIDKYRBmSTkKCsLapKGpsubmaU)
        return True
class gJrMIsATfnXkyxPPuPvhyrflWJwbfiOu:
    @classmethod
    def hGTeyOvpHejlssWPjkjTHIgcOKnCfnQl(uPePujIqMVDrwNvZQxJajkuaQFAcacjA):
        return {"required": { "config_name": (folder_paths.DYvodbeLLCWlQGasCGeYTFNFKZRpPvmd("configs"), ),
                              "ckpt_name": (folder_paths.DYvodbeLLCWlQGasCGeYTFNFKZRpPvmd("checkpoints"), )}}
    KmrPlNMyCntWtQIuwTzhYketzPaLUxAX = ("MODEL", "CLIP", "VAE")
    DCeBXQFyPFIKUXphdMmctDGwHwXgHyTw = "load_checkpoint"
    VHBvQQsdmXccHUVkiKRmkuIiUnjOTicH = "advanced/loaders"
    def LHyInfhWtlCKFbhFfqoifLjBGiaoQbUe(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, config_name, ckpt_name, output_vae=True, output_clip=True):
        MJafEhTfEBNmQGXzAAFXwUBXvYOtnghP = folder_paths.TIUEGMgxYSpXjfhmEGzFnNfGAqtlBBKE("configs", config_name)
        CZOnlrJVXnbYFkZDmLjOAswXNMiGhxHA = folder_paths.TIUEGMgxYSpXjfhmEGzFnNfGAqtlBBKE("checkpoints", ckpt_name)
        return quasar.ylGhUFMpxPbtUUTfCZpemVkdanRhWmHa.LHyInfhWtlCKFbhFfqoifLjBGiaoQbUe(MJafEhTfEBNmQGXzAAFXwUBXvYOtnghP, CZOnlrJVXnbYFkZDmLjOAswXNMiGhxHA, output_vae=True, output_clip=True, embedding_directory=folder_paths.HXYNxZJQjELjaaxuKjoZoxFzWaIvOYmT("embeddings"))
class rrffnjNRHZdVtoFFMasAclfpghoZjVny:
    @classmethod
    def hGTeyOvpHejlssWPjkjTHIgcOKnCfnQl(uPePujIqMVDrwNvZQxJajkuaQFAcacjA):
        return {"required": { "ckpt_name": (folder_paths.DYvodbeLLCWlQGasCGeYTFNFKZRpPvmd("checkpoints"), ),
                             }}
    KmrPlNMyCntWtQIuwTzhYketzPaLUxAX = ("MODEL", "CLIP", "VAE")
    DCeBXQFyPFIKUXphdMmctDGwHwXgHyTw = "load_checkpoint"
    VHBvQQsdmXccHUVkiKRmkuIiUnjOTicH = "loaders"
    def LHyInfhWtlCKFbhFfqoifLjBGiaoQbUe(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, ckpt_name, output_vae=True, output_clip=True):
        CZOnlrJVXnbYFkZDmLjOAswXNMiGhxHA = folder_paths.TIUEGMgxYSpXjfhmEGzFnNfGAqtlBBKE("checkpoints", ckpt_name)
        iqymPVpxyjOWChGwBkTemSzHJbnJdAIz = quasar.ylGhUFMpxPbtUUTfCZpemVkdanRhWmHa.load_checkpoint_guess_config(CZOnlrJVXnbYFkZDmLjOAswXNMiGhxHA, output_vae=True, output_clip=True, embedding_directory=folder_paths.HXYNxZJQjELjaaxuKjoZoxFzWaIvOYmT("embeddings"))
        return iqymPVpxyjOWChGwBkTemSzHJbnJdAIz[:3]
class bsDPHyAnZXnIosnIiQuPBGqfEMEJIqBd:
    @classmethod
    def hGTeyOvpHejlssWPjkjTHIgcOKnCfnQl(qImTjFfovKitSMWzOmePbprJitutCVKi):
        AOGAiLpFWYRqfvQFDHklGCBgbJMOyeLI = []
        for YTXcjRUqHbLVfHitIqjyIaWpbQRXlSNE in folder_paths.HXYNxZJQjELjaaxuKjoZoxFzWaIvOYmT("diffusers"):
            if os.paTH.CzuSRmujwDQnNtuxpiDhURIOWmCdbjjH(YTXcjRUqHbLVfHitIqjyIaWpbQRXlSNE):
                for hpDCmssMBWJUwBayrpShjJoOSQeDdfbl, bwnaMndsjqsroDRgNdISmtBdipLvjCoG, DTcHrFlDIwbrZDZHTOmAOTxRFqptCgyE in os.walk(YTXcjRUqHbLVfHitIqjyIaWpbQRXlSNE, followlinks=True):
                    if "model_index.json" in DTcHrFlDIwbrZDZHTOmAOTxRFqptCgyE:
                        AOGAiLpFWYRqfvQFDHklGCBgbJMOyeLI.append(os.paTH.relpath(hpDCmssMBWJUwBayrpShjJoOSQeDdfbl, tUuYqnLjDXuftYgMagGpmrobxWgfcbgq=YTXcjRUqHbLVfHitIqjyIaWpbQRXlSNE))
        return {"required": {"model_path": (AOGAiLpFWYRqfvQFDHklGCBgbJMOyeLI,), }}
    KmrPlNMyCntWtQIuwTzhYketzPaLUxAX = ("MODEL", "CLIP", "VAE")
    DCeBXQFyPFIKUXphdMmctDGwHwXgHyTw = "load_checkpoint"
    VHBvQQsdmXccHUVkiKRmkuIiUnjOTicH = "advanced/loaders/deprecated"
    def LHyInfhWtlCKFbhFfqoifLjBGiaoQbUe(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, uqDmwCRgGlmMMSwgzjrEvGHoQjjvWqWU, output_vae=True, output_clip=True):
        for YTXcjRUqHbLVfHitIqjyIaWpbQRXlSNE in folder_paths.HXYNxZJQjELjaaxuKjoZoxFzWaIvOYmT("diffusers"):
            if os.paTH.CzuSRmujwDQnNtuxpiDhURIOWmCdbjjH(YTXcjRUqHbLVfHitIqjyIaWpbQRXlSNE):
                paTH = os.paTH.join(YTXcjRUqHbLVfHitIqjyIaWpbQRXlSNE, uqDmwCRgGlmMMSwgzjrEvGHoQjjvWqWU)
                if os.paTH.CzuSRmujwDQnNtuxpiDhURIOWmCdbjjH(paTH):
                    uqDmwCRgGlmMMSwgzjrEvGHoQjjvWqWU = paTH
                    break
        return quasar.diffusers_load.DzQIxZSOpGriDumdVTpwrMDmDIiYkfvv(uqDmwCRgGlmMMSwgzjrEvGHoQjjvWqWU, output_vae=output_vae, output_clip=output_clip, embedding_directory=folder_paths.HXYNxZJQjELjaaxuKjoZoxFzWaIvOYmT("embeddings"))
class qGILltCyOYXZISZAQqJTdClRJVMIyVhd:
    @classmethod
    def hGTeyOvpHejlssWPjkjTHIgcOKnCfnQl(uPePujIqMVDrwNvZQxJajkuaQFAcacjA):
        return {"required": { "ckpt_name": (folder_paths.DYvodbeLLCWlQGasCGeYTFNFKZRpPvmd("checkpoints"), ),
                             }}
    KmrPlNMyCntWtQIuwTzhYketzPaLUxAX = ("MODEL", "CLIP", "VAE", "CLIP_VISION")
    DCeBXQFyPFIKUXphdMmctDGwHwXgHyTw = "load_checkpoint"
    VHBvQQsdmXccHUVkiKRmkuIiUnjOTicH = "loaders"
    def LHyInfhWtlCKFbhFfqoifLjBGiaoQbUe(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, ckpt_name, output_vae=True, output_clip=True):
        CZOnlrJVXnbYFkZDmLjOAswXNMiGhxHA = folder_paths.TIUEGMgxYSpXjfhmEGzFnNfGAqtlBBKE("checkpoints", ckpt_name)
        iqymPVpxyjOWChGwBkTemSzHJbnJdAIz = quasar.ylGhUFMpxPbtUUTfCZpemVkdanRhWmHa.load_checkpoint_guess_config(CZOnlrJVXnbYFkZDmLjOAswXNMiGhxHA, output_vae=True, output_clip=True, output_clipvision=True, embedding_directory=folder_paths.HXYNxZJQjELjaaxuKjoZoxFzWaIvOYmT("embeddings"))
        return iqymPVpxyjOWChGwBkTemSzHJbnJdAIz
class LlMizUiJpMXLbfAHRtmaTRtawJCkifXa:
    @classmethod
    def hGTeyOvpHejlssWPjkjTHIgcOKnCfnQl(uPePujIqMVDrwNvZQxJajkuaQFAcacjA):
        return {"required": { "clip": ("CLIP", ),
                              "stop_at_clip_layer": ("INT", {"default": -1, "min": -24, "max": -1, "step": 1}),
                              }}
    KmrPlNMyCntWtQIuwTzhYketzPaLUxAX = ("CLIP",)
    DCeBXQFyPFIKUXphdMmctDGwHwXgHyTw = "set_last_layer"
    VHBvQQsdmXccHUVkiKRmkuIiUnjOTicH = "conditioning"
    def BSFkmsWvVHJfCkpMjAUmGASSFghdhcov(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, WfkwoxQSNMJYbojfdczjmvPaQWPEJurJ, stop_at_clip_layer):
        WfkwoxQSNMJYbojfdczjmvPaQWPEJurJ = WfkwoxQSNMJYbojfdczjmvPaQWPEJurJ.tEcQvpBwXwdqvKxRTLEBROBUyPoodldL()
        WfkwoxQSNMJYbojfdczjmvPaQWPEJurJ.clip_layer(stop_at_clip_layer)
        return (WfkwoxQSNMJYbojfdczjmvPaQWPEJurJ,)
class tWARkCwiRcNpBDFPksBMZyyZlnZeQKXT:
    def __init__(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS):
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.loaded_lora = None
    @classmethod
    def hGTeyOvpHejlssWPjkjTHIgcOKnCfnQl(uPePujIqMVDrwNvZQxJajkuaQFAcacjA):
        return {"required": { "model": ("MODEL",),
                              "clip": ("CLIP", ),
                              "lora_name": (folder_paths.DYvodbeLLCWlQGasCGeYTFNFKZRpPvmd("loras"), ),
                              "strength_model": ("FLOAT", {"default": 1.0, "min": -10.0, "max": 10.0, "step": 0.01}),
                              "strength_clip": ("FLOAT", {"default": 1.0, "min": -10.0, "max": 10.0, "step": 0.01}),
                              }}
    KmrPlNMyCntWtQIuwTzhYketzPaLUxAX = ("MODEL", "CLIP")
    DCeBXQFyPFIKUXphdMmctDGwHwXgHyTw = "load_lora"
    VHBvQQsdmXccHUVkiKRmkuIiUnjOTicH = "loaders"
    def SrmfspByOhxEpYfUbHxdWOzxdGzupQxv(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM, WfkwoxQSNMJYbojfdczjmvPaQWPEJurJ, lora_name, AePTHMNnzpcegVKckEDvKCKXrzsGyVqK, strength_clip):
        if AePTHMNnzpcegVKckEDvKCKXrzsGyVqK == 0 and strength_clip == 0:
            return (VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM, WfkwoxQSNMJYbojfdczjmvPaQWPEJurJ)
        mFJAAnHHygkTThWfmPXXdCcMPeegmCqq = folder_paths.TIUEGMgxYSpXjfhmEGzFnNfGAqtlBBKE("loras", lora_name)
        nIzLGXVwazNtJWADcRXQeGTPYhxWppqT = None
        if rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.loaded_lora is not None:
            if rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.loaded_lora[0] == mFJAAnHHygkTThWfmPXXdCcMPeegmCqq:
                nIzLGXVwazNtJWADcRXQeGTPYhxWppqT = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.loaded_lora[1]
            else:
                xEFqUNADkGHGuTWgscLRcFtjQusIEAid = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.loaded_lora
                rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.loaded_lora = None
                del xEFqUNADkGHGuTWgscLRcFtjQusIEAid
        if nIzLGXVwazNtJWADcRXQeGTPYhxWppqT is None:
            nIzLGXVwazNtJWADcRXQeGTPYhxWppqT = quasar.utils.load_torch_file(mFJAAnHHygkTThWfmPXXdCcMPeegmCqq, safe_load=True)
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.loaded_lora = (mFJAAnHHygkTThWfmPXXdCcMPeegmCqq, nIzLGXVwazNtJWADcRXQeGTPYhxWppqT)
        ZIrLKZLebWfxmkLsJDkivxloClyjuiFu, DupelxKQOTnChJYwwDSpKkueQIPmZtXs = quasar.ylGhUFMpxPbtUUTfCZpemVkdanRhWmHa.load_lora_for_models(VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM, WfkwoxQSNMJYbojfdczjmvPaQWPEJurJ, nIzLGXVwazNtJWADcRXQeGTPYhxWppqT, AePTHMNnzpcegVKckEDvKCKXrzsGyVqK, strength_clip)
        return (ZIrLKZLebWfxmkLsJDkivxloClyjuiFu, DupelxKQOTnChJYwwDSpKkueQIPmZtXs)
class AuhSmKRAtBABiDBVlzvkmHPAQcReZjMt:
    @classmethod
    def hGTeyOvpHejlssWPjkjTHIgcOKnCfnQl(uPePujIqMVDrwNvZQxJajkuaQFAcacjA):
        return {"required": { "vae_name": (folder_paths.DYvodbeLLCWlQGasCGeYTFNFKZRpPvmd("vae"), )}}
    KmrPlNMyCntWtQIuwTzhYketzPaLUxAX = ("VAE",)
    DCeBXQFyPFIKUXphdMmctDGwHwXgHyTw = "load_vae"
    VHBvQQsdmXccHUVkiKRmkuIiUnjOTicH = "loaders"
    def DhFCZkBxQjBboCcwLWnpsFKZNZyPLUfi(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, vae_name):
        SukNRPIFHgQMbRbMnWQLBnsTPeBwANmJ = folder_paths.TIUEGMgxYSpXjfhmEGzFnNfGAqtlBBKE("vae", vae_name)
        PBWbWRIKcHQYxJBaTdydnolXDaFqlFKi = quasar.ylGhUFMpxPbtUUTfCZpemVkdanRhWmHa.VAE(CZOnlrJVXnbYFkZDmLjOAswXNMiGhxHA=SukNRPIFHgQMbRbMnWQLBnsTPeBwANmJ)
        return (PBWbWRIKcHQYxJBaTdydnolXDaFqlFKi,)
class YNFxJlmnzZYMUgkvImenKmRbdZZaHHKo:
    @classmethod
    def hGTeyOvpHejlssWPjkjTHIgcOKnCfnQl(uPePujIqMVDrwNvZQxJajkuaQFAcacjA):
        return {"required": { "control_net_name": (folder_paths.DYvodbeLLCWlQGasCGeYTFNFKZRpPvmd("controlnet"), )}}
    KmrPlNMyCntWtQIuwTzhYketzPaLUxAX = ("CONTROL_NET",)
    DCeBXQFyPFIKUXphdMmctDGwHwXgHyTw = "load_controlnet"
    VHBvQQsdmXccHUVkiKRmkuIiUnjOTicH = "loaders"
    def efoaRkqBAKlDrlLSRqYEUrVOsSVGKXPb(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, control_net_name):
        jwxIqIODHWzEJxDVAcUheqIHyZkmpWII = folder_paths.TIUEGMgxYSpXjfhmEGzFnNfGAqtlBBKE("controlnet", control_net_name)
        VdWlaPlkqsfXvZUkbqkZdTGuTtMgVkfw = quasar.VdWlaPlkqsfXvZUkbqkZdTGuTtMgVkfw.efoaRkqBAKlDrlLSRqYEUrVOsSVGKXPb(jwxIqIODHWzEJxDVAcUheqIHyZkmpWII)
        return (VdWlaPlkqsfXvZUkbqkZdTGuTtMgVkfw,)
class zQYTVSuLxhISGqACelxrijpNlRcWHRPc:
    @classmethod
    def hGTeyOvpHejlssWPjkjTHIgcOKnCfnQl(uPePujIqMVDrwNvZQxJajkuaQFAcacjA):
        return {"required": { "model": ("MODEL",),
                              "control_net_name": (folder_paths.DYvodbeLLCWlQGasCGeYTFNFKZRpPvmd("controlnet"), )}}
    KmrPlNMyCntWtQIuwTzhYketzPaLUxAX = ("CONTROL_NET",)
    DCeBXQFyPFIKUXphdMmctDGwHwXgHyTw = "load_controlnet"
    VHBvQQsdmXccHUVkiKRmkuIiUnjOTicH = "loaders"
    def efoaRkqBAKlDrlLSRqYEUrVOsSVGKXPb(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM, control_net_name):
        jwxIqIODHWzEJxDVAcUheqIHyZkmpWII = folder_paths.TIUEGMgxYSpXjfhmEGzFnNfGAqtlBBKE("controlnet", control_net_name)
        VdWlaPlkqsfXvZUkbqkZdTGuTtMgVkfw = quasar.VdWlaPlkqsfXvZUkbqkZdTGuTtMgVkfw.efoaRkqBAKlDrlLSRqYEUrVOsSVGKXPb(jwxIqIODHWzEJxDVAcUheqIHyZkmpWII, VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM)
        return (VdWlaPlkqsfXvZUkbqkZdTGuTtMgVkfw,)
class mVdMRJHDdUUxGEmDqyogULmBPSgLFyjR:
    @classmethod
    def hGTeyOvpHejlssWPjkjTHIgcOKnCfnQl(uPePujIqMVDrwNvZQxJajkuaQFAcacjA):
        return {"required": {"conditioning": ("CONDITIONING", ),
                             "control_net": ("CONTROL_NET", ),
                             "image": ("IMAGE", ),
                             "strength": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 10.0, "step": 0.01})
                             }}
    KmrPlNMyCntWtQIuwTzhYketzPaLUxAX = ("CONDITIONING",)
    DCeBXQFyPFIKUXphdMmctDGwHwXgHyTw = "apply_controlnet"
    VHBvQQsdmXccHUVkiKRmkuIiUnjOTicH = "conditioning"
    def kmKTvsVZfYErOBzgocuIEDnPuTjqBEcb(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, nKYmGWBrcYyADcANVAMJtCeHkjgKBdNR, control_net, eLyJtroPthPCROYWyMphoIrGatNOOXCO, strength):
        if strength == 0:
            return (nKYmGWBrcYyADcANVAMJtCeHkjgKBdNR, )
        cjHIelcAqVoHWdLcgzuZiBumKNTVADsY = []
        rIbXPGgxYpFZCLAJnwJdpIIkYPFZgeQW = eLyJtroPthPCROYWyMphoIrGatNOOXCO.movedim(-1,1)
        for XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz in nKYmGWBrcYyADcANVAMJtCeHkjgKBdNR:
            zXHJFiFFvWqeQIAxyaTGMUgoRaHrYzjK = [XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz[0], XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz[1].copy()]
            DJkeQKKSSIzDuUzMxXNSuRCFILnbiHXh = control_net.copy().LDyuFUEWXQnihgTEqvVJdRkoAEEdqHhj(rIbXPGgxYpFZCLAJnwJdpIIkYPFZgeQW, strength)
            if 'control' in XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz[1]:
                DJkeQKKSSIzDuUzMxXNSuRCFILnbiHXh.vNmofEXsbaIjqPudAxTruYiypnCtmibE(XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz[1]['control'])
            zXHJFiFFvWqeQIAxyaTGMUgoRaHrYzjK[1]['control'] = DJkeQKKSSIzDuUzMxXNSuRCFILnbiHXh
            zXHJFiFFvWqeQIAxyaTGMUgoRaHrYzjK[1]['control_apply_to_uncond'] = True
            cjHIelcAqVoHWdLcgzuZiBumKNTVADsY.append(zXHJFiFFvWqeQIAxyaTGMUgoRaHrYzjK)
        return (cjHIelcAqVoHWdLcgzuZiBumKNTVADsY, )
class KSblUWNSuJYUKDpCFiDcqJtyOSxtwxBN:
    @classmethod
    def hGTeyOvpHejlssWPjkjTHIgcOKnCfnQl(uPePujIqMVDrwNvZQxJajkuaQFAcacjA):
        return {"required": {"positive": ("CONDITIONING", ),
                             "negative": ("CONDITIONING", ),
                             "control_net": ("CONTROL_NET", ),
                             "image": ("IMAGE", ),
                             "strength": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 10.0, "step": 0.01}),
                             "start_percent": ("FLOAT", {"default": 0.0, "min": 0.0, "max": 1.0, "step": 0.001}),
                             "end_percent": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 1.0, "step": 0.001})
                             }}
    KmrPlNMyCntWtQIuwTzhYketzPaLUxAX = ("CONDITIONING","CONDITIONING")
    vnnDnTEtmjYBCExrcduKGXUgKSzKzhcS = ("positive", "negative")
    DCeBXQFyPFIKUXphdMmctDGwHwXgHyTw = "apply_controlnet"
    VHBvQQsdmXccHUVkiKRmkuIiUnjOTicH = "conditioning"
    def kmKTvsVZfYErOBzgocuIEDnPuTjqBEcb(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, positive, negative, control_net, eLyJtroPthPCROYWyMphoIrGatNOOXCO, strength, start_percent, end_percent):
        if strength == 0:
            return (positive, negative)
        rIbXPGgxYpFZCLAJnwJdpIIkYPFZgeQW = eLyJtroPthPCROYWyMphoIrGatNOOXCO.movedim(-1,1)
        FxRdoVJRXOPrLjUaYJrngmaOAhVwCuzc = {}
        iqymPVpxyjOWChGwBkTemSzHJbnJdAIz = []
        for nKYmGWBrcYyADcANVAMJtCeHkjgKBdNR in [positive, negative]:
            cjHIelcAqVoHWdLcgzuZiBumKNTVADsY = []
            for XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz in nKYmGWBrcYyADcANVAMJtCeHkjgKBdNR:
                TXGwYXNLgQsYzfHHpRBDJGFCFZEClzIo = XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz[1].copy()
                nJVjYRrgFBccfIWipLpEsbGQXHoAFvQH = TXGwYXNLgQsYzfHHpRBDJGFCFZEClzIo.get('control', None)
                if nJVjYRrgFBccfIWipLpEsbGQXHoAFvQH in FxRdoVJRXOPrLjUaYJrngmaOAhVwCuzc:
                    DJkeQKKSSIzDuUzMxXNSuRCFILnbiHXh = FxRdoVJRXOPrLjUaYJrngmaOAhVwCuzc[nJVjYRrgFBccfIWipLpEsbGQXHoAFvQH]
                else:
                    DJkeQKKSSIzDuUzMxXNSuRCFILnbiHXh = control_net.copy().LDyuFUEWXQnihgTEqvVJdRkoAEEdqHhj(rIbXPGgxYpFZCLAJnwJdpIIkYPFZgeQW, strength, (1.0 - start_percent, 1.0 - end_percent))
                    DJkeQKKSSIzDuUzMxXNSuRCFILnbiHXh.vNmofEXsbaIjqPudAxTruYiypnCtmibE(nJVjYRrgFBccfIWipLpEsbGQXHoAFvQH)
                    FxRdoVJRXOPrLjUaYJrngmaOAhVwCuzc[nJVjYRrgFBccfIWipLpEsbGQXHoAFvQH] = DJkeQKKSSIzDuUzMxXNSuRCFILnbiHXh
                TXGwYXNLgQsYzfHHpRBDJGFCFZEClzIo['control'] = DJkeQKKSSIzDuUzMxXNSuRCFILnbiHXh
                TXGwYXNLgQsYzfHHpRBDJGFCFZEClzIo['control_apply_to_uncond'] = False
                zXHJFiFFvWqeQIAxyaTGMUgoRaHrYzjK = [XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz[0], TXGwYXNLgQsYzfHHpRBDJGFCFZEClzIo]
                cjHIelcAqVoHWdLcgzuZiBumKNTVADsY.append(zXHJFiFFvWqeQIAxyaTGMUgoRaHrYzjK)
            iqymPVpxyjOWChGwBkTemSzHJbnJdAIz.append(cjHIelcAqVoHWdLcgzuZiBumKNTVADsY)
        return (iqymPVpxyjOWChGwBkTemSzHJbnJdAIz[0], iqymPVpxyjOWChGwBkTemSzHJbnJdAIz[1])
class ZJIPzHKaCxfzJZCrIPDhFmCviGVBHwxT:
    @classmethod
    def hGTeyOvpHejlssWPjkjTHIgcOKnCfnQl(uPePujIqMVDrwNvZQxJajkuaQFAcacjA):
        return {"required": { "unet_name": (folder_paths.DYvodbeLLCWlQGasCGeYTFNFKZRpPvmd("unet"), ),
                             }}
    KmrPlNMyCntWtQIuwTzhYketzPaLUxAX = ("MODEL",)
    DCeBXQFyPFIKUXphdMmctDGwHwXgHyTw = "load_unet"
    VHBvQQsdmXccHUVkiKRmkuIiUnjOTicH = "advanced/loaders"
    def dtZfLtBphxBRLHJpIPTIxSOaPKOoVyHs(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, unet_name):
        lUdVoyBhqRkFznaNCaHtBXrzPIxGdAef = folder_paths.TIUEGMgxYSpXjfhmEGzFnNfGAqtlBBKE("unet", unet_name)
        VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM = quasar.ylGhUFMpxPbtUUTfCZpemVkdanRhWmHa.dtZfLtBphxBRLHJpIPTIxSOaPKOoVyHs(lUdVoyBhqRkFznaNCaHtBXrzPIxGdAef)
        return (VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM,)
class wjTFuRtlDVnDUEKlDqDyfyFIojrwJSZB:
    @classmethod
    def hGTeyOvpHejlssWPjkjTHIgcOKnCfnQl(uPePujIqMVDrwNvZQxJajkuaQFAcacjA):
        return {"required": { "clip_name": (folder_paths.DYvodbeLLCWlQGasCGeYTFNFKZRpPvmd("clip"), ),
                             }}
    KmrPlNMyCntWtQIuwTzhYketzPaLUxAX = ("CLIP",)
    DCeBXQFyPFIKUXphdMmctDGwHwXgHyTw = "load_clip"
    VHBvQQsdmXccHUVkiKRmkuIiUnjOTicH = "advanced/loaders"
    def lUJkDFeJtgkghWfgvfOCiPlafTOuBTLh(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, clip_name):
        GYmbiGzZvfXczOLHGETAcmKwauktkxmv = folder_paths.TIUEGMgxYSpXjfhmEGzFnNfGAqtlBBKE("clip", clip_name)
        WfkwoxQSNMJYbojfdczjmvPaQWPEJurJ = quasar.ylGhUFMpxPbtUUTfCZpemVkdanRhWmHa.lUJkDFeJtgkghWfgvfOCiPlafTOuBTLh(ckpt_paths=[GYmbiGzZvfXczOLHGETAcmKwauktkxmv], embedding_directory=folder_paths.HXYNxZJQjELjaaxuKjoZoxFzWaIvOYmT("embeddings"))
        return (WfkwoxQSNMJYbojfdczjmvPaQWPEJurJ,)
class wFxydWVsOuPMENdbkVzPjDhmMOqXFXMA:
    @classmethod
    def hGTeyOvpHejlssWPjkjTHIgcOKnCfnQl(uPePujIqMVDrwNvZQxJajkuaQFAcacjA):
        return {"required": { "clip_name1": (folder_paths.DYvodbeLLCWlQGasCGeYTFNFKZRpPvmd("clip"), ), "clip_name2": (folder_paths.DYvodbeLLCWlQGasCGeYTFNFKZRpPvmd("clip"), ),
                             }}
    KmrPlNMyCntWtQIuwTzhYketzPaLUxAX = ("CLIP",)
    DCeBXQFyPFIKUXphdMmctDGwHwXgHyTw = "load_clip"
    VHBvQQsdmXccHUVkiKRmkuIiUnjOTicH = "advanced/loaders"
    def lUJkDFeJtgkghWfgvfOCiPlafTOuBTLh(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, clip_name1, clip_name2):
        JjteyzlVhUQtMAUCiaKeYIKbQMyNlFkp = folder_paths.TIUEGMgxYSpXjfhmEGzFnNfGAqtlBBKE("clip", clip_name1)
        iajnqdRHWmvqUmmUmBpFvdtjxJojceAM = folder_paths.TIUEGMgxYSpXjfhmEGzFnNfGAqtlBBKE("clip", clip_name2)
        WfkwoxQSNMJYbojfdczjmvPaQWPEJurJ = quasar.ylGhUFMpxPbtUUTfCZpemVkdanRhWmHa.lUJkDFeJtgkghWfgvfOCiPlafTOuBTLh(ckpt_paths=[JjteyzlVhUQtMAUCiaKeYIKbQMyNlFkp, iajnqdRHWmvqUmmUmBpFvdtjxJojceAM], embedding_directory=folder_paths.HXYNxZJQjELjaaxuKjoZoxFzWaIvOYmT("embeddings"))
        return (WfkwoxQSNMJYbojfdczjmvPaQWPEJurJ,)
class VBGplsVXOYjOSHSeaszMPcfeqtPzrirl:
    @classmethod
    def hGTeyOvpHejlssWPjkjTHIgcOKnCfnQl(uPePujIqMVDrwNvZQxJajkuaQFAcacjA):
        return {"required": { "clip_name": (folder_paths.DYvodbeLLCWlQGasCGeYTFNFKZRpPvmd("clip_vision"), ),
                             }}
    KmrPlNMyCntWtQIuwTzhYketzPaLUxAX = ("CLIP_VISION",)
    DCeBXQFyPFIKUXphdMmctDGwHwXgHyTw = "load_clip"
    VHBvQQsdmXccHUVkiKRmkuIiUnjOTicH = "loaders"
    def lUJkDFeJtgkghWfgvfOCiPlafTOuBTLh(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, clip_name):
        GYmbiGzZvfXczOLHGETAcmKwauktkxmv = folder_paths.TIUEGMgxYSpXjfhmEGzFnNfGAqtlBBKE("clip_vision", clip_name)
        oJjvwBRjryeoQIMgjJORkWSyUyVcSVMI = quasar.oJjvwBRjryeoQIMgjJORkWSyUyVcSVMI.yjjLwfEWtXKFjwwmuqReIXUDoGaUzfxz(GYmbiGzZvfXczOLHGETAcmKwauktkxmv)
        return (oJjvwBRjryeoQIMgjJORkWSyUyVcSVMI,)
class dirxAbDzGLspwIXNciTiCbXOItASPyRD:
    @classmethod
    def hGTeyOvpHejlssWPjkjTHIgcOKnCfnQl(uPePujIqMVDrwNvZQxJajkuaQFAcacjA):
        return {"required": { "clip_vision": ("CLIP_VISION",),
                              "image": ("IMAGE",)
                             }}
    KmrPlNMyCntWtQIuwTzhYketzPaLUxAX = ("CLIP_VISION_OUTPUT",)
    DCeBXQFyPFIKUXphdMmctDGwHwXgHyTw = "encode"
    VHBvQQsdmXccHUVkiKRmkuIiUnjOTicH = "conditioning"
    def encode(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, oJjvwBRjryeoQIMgjJORkWSyUyVcSVMI, eLyJtroPthPCROYWyMphoIrGatNOOXCO):
        pwTxzdNTJGMWEFORftJTEtPYMMiKwDuP = oJjvwBRjryeoQIMgjJORkWSyUyVcSVMI.NnAHfuFUGEfFYQJPjptHkPYpiniDBghN(eLyJtroPthPCROYWyMphoIrGatNOOXCO)
        return (pwTxzdNTJGMWEFORftJTEtPYMMiKwDuP,)
class WyUqJFjBBSkvXHOuTDxxHFYkYqJqzebh:
    @classmethod
    def hGTeyOvpHejlssWPjkjTHIgcOKnCfnQl(uPePujIqMVDrwNvZQxJajkuaQFAcacjA):
        return {"required": { "style_model_name": (folder_paths.DYvodbeLLCWlQGasCGeYTFNFKZRpPvmd("style_models"), )}}
    KmrPlNMyCntWtQIuwTzhYketzPaLUxAX = ("STYLE_MODEL",)
    DCeBXQFyPFIKUXphdMmctDGwHwXgHyTw = "load_style_model"
    VHBvQQsdmXccHUVkiKRmkuIiUnjOTicH = "loaders"
    def rectGLJvXYuTZfSfunbcBaPGLRskQuzJ(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, style_model_name):
        kISbCQqCiXgXLotRIRWPIUscmsUcVavA = folder_paths.TIUEGMgxYSpXjfhmEGzFnNfGAqtlBBKE("style_models", style_model_name)
        XbguvARSMZgMOEVQoPEJszfqnkMpwwuz = quasar.ylGhUFMpxPbtUUTfCZpemVkdanRhWmHa.rectGLJvXYuTZfSfunbcBaPGLRskQuzJ(kISbCQqCiXgXLotRIRWPIUscmsUcVavA)
        return (XbguvARSMZgMOEVQoPEJszfqnkMpwwuz,)
class SOjubiEONXRlmSXXxhVtITwyixpxICwa:
    @classmethod
    def hGTeyOvpHejlssWPjkjTHIgcOKnCfnQl(uPePujIqMVDrwNvZQxJajkuaQFAcacjA):
        return {"required": {"conditioning": ("CONDITIONING", ),
                             "style_model": ("STYLE_MODEL", ),
                             "clip_vision_output": ("CLIP_VISION_OUTPUT", ),
                             }}
    KmrPlNMyCntWtQIuwTzhYketzPaLUxAX = ("CONDITIONING",)
    DCeBXQFyPFIKUXphdMmctDGwHwXgHyTw = "apply_stylemodel"
    VHBvQQsdmXccHUVkiKRmkuIiUnjOTicH = "conditioning/style_model"
    def iMaYEnoaPdWuIoTfYsciklgGyrOjwTLC(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, clip_vision_output, XbguvARSMZgMOEVQoPEJszfqnkMpwwuz, nKYmGWBrcYyADcANVAMJtCeHkjgKBdNR):
        BuoWBAnnMxyvqTGoSTHbQAlvPFWHbuUf = XbguvARSMZgMOEVQoPEJszfqnkMpwwuz.get_cond(clip_vision_output).flatten(start_dim=0, end_dim=1).unsqueeze(yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk=0)
        cjHIelcAqVoHWdLcgzuZiBumKNTVADsY = []
        for XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz in nKYmGWBrcYyADcANVAMJtCeHkjgKBdNR:
            zXHJFiFFvWqeQIAxyaTGMUgoRaHrYzjK = [torch.cat((XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz[0], BuoWBAnnMxyvqTGoSTHbQAlvPFWHbuUf), yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk=1), XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz[1].copy()]
            cjHIelcAqVoHWdLcgzuZiBumKNTVADsY.append(zXHJFiFFvWqeQIAxyaTGMUgoRaHrYzjK)
        return (cjHIelcAqVoHWdLcgzuZiBumKNTVADsY, )
class YDCxaWxzbjsFNDcwFDNikWNamdFKYEJr:
    @classmethod
    def hGTeyOvpHejlssWPjkjTHIgcOKnCfnQl(uPePujIqMVDrwNvZQxJajkuaQFAcacjA):
        return {"required": {"conditioning": ("CONDITIONING", ),
                             "clip_vision_output": ("CLIP_VISION_OUTPUT", ),
                             "strength": ("FLOAT", {"default": 1.0, "min": -10.0, "max": 10.0, "step": 0.01}),
                             "noise_augmentation": ("FLOAT", {"default": 0.0, "min": 0.0, "max": 1.0, "step": 0.01}),
                             }}
    KmrPlNMyCntWtQIuwTzhYketzPaLUxAX = ("CONDITIONING",)
    DCeBXQFyPFIKUXphdMmctDGwHwXgHyTw = "apply_adm"
    VHBvQQsdmXccHUVkiKRmkuIiUnjOTicH = "conditioning"
    def zclHoBEMdTfYlpnsjuuAxPZkbLmSSYcq(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, nKYmGWBrcYyADcANVAMJtCeHkjgKBdNR, clip_vision_output, strength, noise_augmentation):
        if strength == 0:
            return (nKYmGWBrcYyADcANVAMJtCeHkjgKBdNR, )
        cjHIelcAqVoHWdLcgzuZiBumKNTVADsY = []
        for XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz in nKYmGWBrcYyADcANVAMJtCeHkjgKBdNR:
            LDnaTUWTECGaKdJqXUUrFoSvDMujRxwx = XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz[1].copy()
            NECAaWUrFGIXcLimrerEYmxYIykQBfXb = {"clip_vision_output": clip_vision_output, "strength": strength, "noise_augmentation": noise_augmentation}
            if "unclip_conditioning" in LDnaTUWTECGaKdJqXUUrFoSvDMujRxwx:
                LDnaTUWTECGaKdJqXUUrFoSvDMujRxwx["unclip_conditioning"] = LDnaTUWTECGaKdJqXUUrFoSvDMujRxwx["unclip_conditioning"][:] + [NECAaWUrFGIXcLimrerEYmxYIykQBfXb]
            else:
                LDnaTUWTECGaKdJqXUUrFoSvDMujRxwx["unclip_conditioning"] = [NECAaWUrFGIXcLimrerEYmxYIykQBfXb]
            zXHJFiFFvWqeQIAxyaTGMUgoRaHrYzjK = [XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz[0], LDnaTUWTECGaKdJqXUUrFoSvDMujRxwx]
            cjHIelcAqVoHWdLcgzuZiBumKNTVADsY.append(zXHJFiFFvWqeQIAxyaTGMUgoRaHrYzjK)
        return (cjHIelcAqVoHWdLcgzuZiBumKNTVADsY, )
class pmpJQceZGpDQRSmOmKyZwIscUkTsJOkN:
    @classmethod
    def hGTeyOvpHejlssWPjkjTHIgcOKnCfnQl(uPePujIqMVDrwNvZQxJajkuaQFAcacjA):
        return {"required": { "gligen_name": (folder_paths.DYvodbeLLCWlQGasCGeYTFNFKZRpPvmd("gligen"), )}}
    KmrPlNMyCntWtQIuwTzhYketzPaLUxAX = ("GLIGEN",)
    DCeBXQFyPFIKUXphdMmctDGwHwXgHyTw = "load_gligen"
    VHBvQQsdmXccHUVkiKRmkuIiUnjOTicH = "loaders"
    def ahutYoNAGGKLXRlfTnRgCkshwGtscWss(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, gligen_name):
        lGwJnYzJKpDdPDzfujMuwMNsZKbjauIS = folder_paths.TIUEGMgxYSpXjfhmEGzFnNfGAqtlBBKE("gligen", gligen_name)
        bQxLSNgPlazghYEcawwmtsRrmJBIwCXU = quasar.ylGhUFMpxPbtUUTfCZpemVkdanRhWmHa.ahutYoNAGGKLXRlfTnRgCkshwGtscWss(lGwJnYzJKpDdPDzfujMuwMNsZKbjauIS)
        return (bQxLSNgPlazghYEcawwmtsRrmJBIwCXU,)
class tYtrMfFbaFUvQdAhLmTEXiDxugViLiCm:
    @classmethod
    def hGTeyOvpHejlssWPjkjTHIgcOKnCfnQl(uPePujIqMVDrwNvZQxJajkuaQFAcacjA):
        return {"required": {"conditioning_to": ("CONDITIONING", ),
                              "clip": ("CLIP", ),
                              "gligen_textbox_model": ("GLIGEN", ),
                              "text": ("STRING", {"multiline": True}),
                              "width": ("INT", {"default": 64, "min": 8, "max": tUEqFkJYdZNTmWQilLxLUFxmxzEWYVdq, "step": 8}),
                              "height": ("INT", {"default": 64, "min": 8, "max": tUEqFkJYdZNTmWQilLxLUFxmxzEWYVdq, "step": 8}),
                              "x": ("INT", {"default": 0, "min": 0, "max": tUEqFkJYdZNTmWQilLxLUFxmxzEWYVdq, "step": 8}),
                              "y": ("INT", {"default": 0, "min": 0, "max": tUEqFkJYdZNTmWQilLxLUFxmxzEWYVdq, "step": 8}),
                             }}
    KmrPlNMyCntWtQIuwTzhYketzPaLUxAX = ("CONDITIONING",)
    DCeBXQFyPFIKUXphdMmctDGwHwXgHyTw = "append"
    VHBvQQsdmXccHUVkiKRmkuIiUnjOTicH = "conditioning/gligen"
    def append(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, conditioning_to, WfkwoxQSNMJYbojfdczjmvPaQWPEJurJ, gligen_textbox_model, text, QfeoFYGsEQNWblsqXsRKWQpzeXgWujaz, yhGxnlfJCKaDHyDtiYhJHxHFcooDKiMM, NECAaWUrFGIXcLimrerEYmxYIykQBfXb, ZljqvWVaiqYAYdTFzQHSTXFDKwgstKaW):
        cjHIelcAqVoHWdLcgzuZiBumKNTVADsY = []
        BuoWBAnnMxyvqTGoSTHbQAlvPFWHbuUf, otExEnXAynOmuosclWTOxAbtTPiksVJV = WfkwoxQSNMJYbojfdczjmvPaQWPEJurJ.encode_from_tokens(WfkwoxQSNMJYbojfdczjmvPaQWPEJurJ.tokenize(text), return_pooled=True)
        for XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz in conditioning_to:
            zXHJFiFFvWqeQIAxyaTGMUgoRaHrYzjK = [XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz[0], XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz[1].copy()]
            fOljKxXLyHfGyNkotLKyQTKMHPpbZVFm = [(otExEnXAynOmuosclWTOxAbtTPiksVJV, yhGxnlfJCKaDHyDtiYhJHxHFcooDKiMM // 8, QfeoFYGsEQNWblsqXsRKWQpzeXgWujaz // 8, ZljqvWVaiqYAYdTFzQHSTXFDKwgstKaW // 8, NECAaWUrFGIXcLimrerEYmxYIykQBfXb // 8)]
            VHKvgGDtxDLaDHmvTEkAHAuODuIIgHxj = []
            if "gligen" in zXHJFiFFvWqeQIAxyaTGMUgoRaHrYzjK[1]:
                VHKvgGDtxDLaDHmvTEkAHAuODuIIgHxj = zXHJFiFFvWqeQIAxyaTGMUgoRaHrYzjK[1]['gligen'][2]
            zXHJFiFFvWqeQIAxyaTGMUgoRaHrYzjK[1]['gligen'] = ("position", gligen_textbox_model, VHKvgGDtxDLaDHmvTEkAHAuODuIIgHxj + fOljKxXLyHfGyNkotLKyQTKMHPpbZVFm)
            cjHIelcAqVoHWdLcgzuZiBumKNTVADsY.append(zXHJFiFFvWqeQIAxyaTGMUgoRaHrYzjK)
        return (cjHIelcAqVoHWdLcgzuZiBumKNTVADsY, )
class zIvxPokXhsKQUkwRRjDGfhTCiBLEdtiP:
    def __init__(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc="cpu"):
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc = fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc
    @classmethod
    def hGTeyOvpHejlssWPjkjTHIgcOKnCfnQl(uPePujIqMVDrwNvZQxJajkuaQFAcacjA):
        return {"required": { "width": ("INT", {"default": 512, "min": 64, "max": tUEqFkJYdZNTmWQilLxLUFxmxzEWYVdq, "step": 8}),
                              "height": ("INT", {"default": 512, "min": 64, "max": tUEqFkJYdZNTmWQilLxLUFxmxzEWYVdq, "step": 8}),
                              "batch_size": ("INT", {"default": 1, "min": 1, "max": 64})}}
    KmrPlNMyCntWtQIuwTzhYketzPaLUxAX = ("LATENT",)
    DCeBXQFyPFIKUXphdMmctDGwHwXgHyTw = "generate"
    VHBvQQsdmXccHUVkiKRmkuIiUnjOTicH = "latent"
    def cMNLLVrjBWvAYnKLhGgZwcTNuoUSsokk(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, QfeoFYGsEQNWblsqXsRKWQpzeXgWujaz, yhGxnlfJCKaDHyDtiYhJHxHFcooDKiMM, batch_size=1):
        CBTHgqHIDKYRBmSTkKCsLapKGpsubmaU = torch.zeros([batch_size, 4, yhGxnlfJCKaDHyDtiYhJHxHFcooDKiMM // 8, QfeoFYGsEQNWblsqXsRKWQpzeXgWujaz // 8])
        return ({"samples":CBTHgqHIDKYRBmSTkKCsLapKGpsubmaU}, )
class BjeSWOzISSYoyQOEAUTNgdoiiiyDqqkI:
    @classmethod
    def hGTeyOvpHejlssWPjkjTHIgcOKnCfnQl(uPePujIqMVDrwNvZQxJajkuaQFAcacjA):
        return {"required": { "samples": ("LATENT",),
                              "batch_index": ("INT", {"default": 0, "min": 0, "max": 63}),
                              "length": ("INT", {"default": 1, "min": 1, "max": 64}),
                              }}
    KmrPlNMyCntWtQIuwTzhYketzPaLUxAX = ("LATENT",)
    DCeBXQFyPFIKUXphdMmctDGwHwXgHyTw = "frombatch"
    VHBvQQsdmXccHUVkiKRmkuIiUnjOTicH = "latent/batch"
    def cvipDSmwvzkChLbzoZAlgRGFnFYdoIVs(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, bfpFhSQCEeSgZQwablzNZDcPruUlpnjs, HhYGQTaiBJXaJkGXPEyNEnEpISDgiTTl, SruGYKDDIYooroMjYWrVQpmbvNQFTTDo):
        uPePujIqMVDrwNvZQxJajkuaQFAcacjA = bfpFhSQCEeSgZQwablzNZDcPruUlpnjs.copy()
        moQRitRqIYEATNnahksUxyKeQfVQohNA = bfpFhSQCEeSgZQwablzNZDcPruUlpnjs["samples"]
        HhYGQTaiBJXaJkGXPEyNEnEpISDgiTTl = min(moQRitRqIYEATNnahksUxyKeQfVQohNA.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[0] - 1, HhYGQTaiBJXaJkGXPEyNEnEpISDgiTTl)
        SruGYKDDIYooroMjYWrVQpmbvNQFTTDo = min(moQRitRqIYEATNnahksUxyKeQfVQohNA.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[0] - HhYGQTaiBJXaJkGXPEyNEnEpISDgiTTl, SruGYKDDIYooroMjYWrVQpmbvNQFTTDo)
        uPePujIqMVDrwNvZQxJajkuaQFAcacjA["samples"] = moQRitRqIYEATNnahksUxyKeQfVQohNA[HhYGQTaiBJXaJkGXPEyNEnEpISDgiTTl:HhYGQTaiBJXaJkGXPEyNEnEpISDgiTTl + SruGYKDDIYooroMjYWrVQpmbvNQFTTDo].tEcQvpBwXwdqvKxRTLEBROBUyPoodldL()
        if "noise_mask" in bfpFhSQCEeSgZQwablzNZDcPruUlpnjs:
            npdIyYBsgKLNOVeVWjQcsjYKmaHpbRXB = bfpFhSQCEeSgZQwablzNZDcPruUlpnjs["noise_mask"]
            if npdIyYBsgKLNOVeVWjQcsjYKmaHpbRXB.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[0] == 1:
                uPePujIqMVDrwNvZQxJajkuaQFAcacjA["noise_mask"] = npdIyYBsgKLNOVeVWjQcsjYKmaHpbRXB.tEcQvpBwXwdqvKxRTLEBROBUyPoodldL()
            else:
                if npdIyYBsgKLNOVeVWjQcsjYKmaHpbRXB.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[0] < moQRitRqIYEATNnahksUxyKeQfVQohNA.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[0]:
                    npdIyYBsgKLNOVeVWjQcsjYKmaHpbRXB = npdIyYBsgKLNOVeVWjQcsjYKmaHpbRXB.kYXcbCDGZMxtOlIZeOtGMsNePlSickQL(math.ceil(moQRitRqIYEATNnahksUxyKeQfVQohNA.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[0] / npdIyYBsgKLNOVeVWjQcsjYKmaHpbRXB.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[0]), 1, 1, 1)[:moQRitRqIYEATNnahksUxyKeQfVQohNA.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[0]]
                uPePujIqMVDrwNvZQxJajkuaQFAcacjA["noise_mask"] = npdIyYBsgKLNOVeVWjQcsjYKmaHpbRXB[HhYGQTaiBJXaJkGXPEyNEnEpISDgiTTl:HhYGQTaiBJXaJkGXPEyNEnEpISDgiTTl + SruGYKDDIYooroMjYWrVQpmbvNQFTTDo].tEcQvpBwXwdqvKxRTLEBROBUyPoodldL()
        if "batch_index" not in uPePujIqMVDrwNvZQxJajkuaQFAcacjA:
            uPePujIqMVDrwNvZQxJajkuaQFAcacjA["batch_index"] = [NECAaWUrFGIXcLimrerEYmxYIykQBfXb for NECAaWUrFGIXcLimrerEYmxYIykQBfXb in range(HhYGQTaiBJXaJkGXPEyNEnEpISDgiTTl, HhYGQTaiBJXaJkGXPEyNEnEpISDgiTTl+SruGYKDDIYooroMjYWrVQpmbvNQFTTDo)]
        else:
            uPePujIqMVDrwNvZQxJajkuaQFAcacjA["batch_index"] = bfpFhSQCEeSgZQwablzNZDcPruUlpnjs["batch_index"][HhYGQTaiBJXaJkGXPEyNEnEpISDgiTTl:HhYGQTaiBJXaJkGXPEyNEnEpISDgiTTl + SruGYKDDIYooroMjYWrVQpmbvNQFTTDo]
        return (uPePujIqMVDrwNvZQxJajkuaQFAcacjA,)
class adIeuebYdlahZUgrpwIFCsqBprKAwwnF:
    @classmethod
    def hGTeyOvpHejlssWPjkjTHIgcOKnCfnQl(uPePujIqMVDrwNvZQxJajkuaQFAcacjA):
        return {"required": { "samples": ("LATENT",),
                              "amount": ("INT", {"default": 1, "min": 1, "max": 64}),
                              }}
    KmrPlNMyCntWtQIuwTzhYketzPaLUxAX = ("LATENT",)
    DCeBXQFyPFIKUXphdMmctDGwHwXgHyTw = "repeat"
    VHBvQQsdmXccHUVkiKRmkuIiUnjOTicH = "latent/batch"
    def kYXcbCDGZMxtOlIZeOtGMsNePlSickQL(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, bfpFhSQCEeSgZQwablzNZDcPruUlpnjs, amount):
        uPePujIqMVDrwNvZQxJajkuaQFAcacjA = bfpFhSQCEeSgZQwablzNZDcPruUlpnjs.copy()
        moQRitRqIYEATNnahksUxyKeQfVQohNA = bfpFhSQCEeSgZQwablzNZDcPruUlpnjs["samples"]
        uPePujIqMVDrwNvZQxJajkuaQFAcacjA["samples"] = moQRitRqIYEATNnahksUxyKeQfVQohNA.kYXcbCDGZMxtOlIZeOtGMsNePlSickQL((amount, 1,1,1))
        if "noise_mask" in bfpFhSQCEeSgZQwablzNZDcPruUlpnjs and bfpFhSQCEeSgZQwablzNZDcPruUlpnjs["noise_mask"].BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[0] > 1:
            npdIyYBsgKLNOVeVWjQcsjYKmaHpbRXB = bfpFhSQCEeSgZQwablzNZDcPruUlpnjs["noise_mask"]
            if npdIyYBsgKLNOVeVWjQcsjYKmaHpbRXB.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[0] < moQRitRqIYEATNnahksUxyKeQfVQohNA.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[0]:
                npdIyYBsgKLNOVeVWjQcsjYKmaHpbRXB = npdIyYBsgKLNOVeVWjQcsjYKmaHpbRXB.kYXcbCDGZMxtOlIZeOtGMsNePlSickQL(math.ceil(moQRitRqIYEATNnahksUxyKeQfVQohNA.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[0] / npdIyYBsgKLNOVeVWjQcsjYKmaHpbRXB.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[0]), 1, 1, 1)[:moQRitRqIYEATNnahksUxyKeQfVQohNA.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[0]]
            uPePujIqMVDrwNvZQxJajkuaQFAcacjA["noise_mask"] = bfpFhSQCEeSgZQwablzNZDcPruUlpnjs["noise_mask"].kYXcbCDGZMxtOlIZeOtGMsNePlSickQL((amount, 1,1,1))
        if "batch_index" in uPePujIqMVDrwNvZQxJajkuaQFAcacjA:
            UgJNpWQgCrhGXhLkNDqPkhNiazfBUzjL = max(uPePujIqMVDrwNvZQxJajkuaQFAcacjA["batch_index"]) - min(uPePujIqMVDrwNvZQxJajkuaQFAcacjA["batch_index"]) + 1
            uPePujIqMVDrwNvZQxJajkuaQFAcacjA["batch_index"] = uPePujIqMVDrwNvZQxJajkuaQFAcacjA["batch_index"] + [NECAaWUrFGIXcLimrerEYmxYIykQBfXb + (HCXmerBqIMuTscBONzTGKYapYSxWTYHo * UgJNpWQgCrhGXhLkNDqPkhNiazfBUzjL) for HCXmerBqIMuTscBONzTGKYapYSxWTYHo in range(1, amount) for NECAaWUrFGIXcLimrerEYmxYIykQBfXb in uPePujIqMVDrwNvZQxJajkuaQFAcacjA["batch_index"]]
        return (uPePujIqMVDrwNvZQxJajkuaQFAcacjA,)
class nnaIKRoFlXjuwnjMXMUxgnefIWJmKJCF:
    nTMejTWQGKEJaifVMLgCiAYoxptTnZdn = ["nearest-exact", "bilinear", "area", "bicubic", "bislerp"]
    XcQdZHKZQDcRHNbXHMmBlmIhMHVffMUf = ["disabled", "center"]
    @classmethod
    def hGTeyOvpHejlssWPjkjTHIgcOKnCfnQl(uPePujIqMVDrwNvZQxJajkuaQFAcacjA):
        return {"required": { "samples": ("LATENT",), "upscale_method": (uPePujIqMVDrwNvZQxJajkuaQFAcacjA.nTMejTWQGKEJaifVMLgCiAYoxptTnZdn,),
                              "width": ("INT", {"default": 512, "min": 64, "max": tUEqFkJYdZNTmWQilLxLUFxmxzEWYVdq, "step": 8}),
                              "height": ("INT", {"default": 512, "min": 64, "max": tUEqFkJYdZNTmWQilLxLUFxmxzEWYVdq, "step": 8}),
                              "crop": (uPePujIqMVDrwNvZQxJajkuaQFAcacjA.XcQdZHKZQDcRHNbXHMmBlmIhMHVffMUf,)}}
    KmrPlNMyCntWtQIuwTzhYketzPaLUxAX = ("LATENT",)
    DCeBXQFyPFIKUXphdMmctDGwHwXgHyTw = "upscale"
    VHBvQQsdmXccHUVkiKRmkuIiUnjOTicH = "latent"
    def VFbOpUjlPHhNgAvxtBCPRqDCJyPQDVlx(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, bfpFhSQCEeSgZQwablzNZDcPruUlpnjs, upscale_method, QfeoFYGsEQNWblsqXsRKWQpzeXgWujaz, yhGxnlfJCKaDHyDtiYhJHxHFcooDKiMM, CWEytKkepwhdVJpGxZvfxcoPmAcpotMo):
        uPePujIqMVDrwNvZQxJajkuaQFAcacjA = bfpFhSQCEeSgZQwablzNZDcPruUlpnjs.copy()
        uPePujIqMVDrwNvZQxJajkuaQFAcacjA["samples"] = quasar.utils.common_upscale(bfpFhSQCEeSgZQwablzNZDcPruUlpnjs["samples"], QfeoFYGsEQNWblsqXsRKWQpzeXgWujaz // 8, yhGxnlfJCKaDHyDtiYhJHxHFcooDKiMM // 8, upscale_method, CWEytKkepwhdVJpGxZvfxcoPmAcpotMo)
        return (uPePujIqMVDrwNvZQxJajkuaQFAcacjA,)
class cmbmlESGPTsYIXObNNeWTijDvbyxFcvY:
    nTMejTWQGKEJaifVMLgCiAYoxptTnZdn = ["nearest-exact", "bilinear", "area", "bicubic", "bislerp"]
    @classmethod
    def hGTeyOvpHejlssWPjkjTHIgcOKnCfnQl(uPePujIqMVDrwNvZQxJajkuaQFAcacjA):
        return {"required": { "samples": ("LATENT",), "upscale_method": (uPePujIqMVDrwNvZQxJajkuaQFAcacjA.nTMejTWQGKEJaifVMLgCiAYoxptTnZdn,),
                              "scale_by": ("FLOAT", {"default": 1.5, "min": 0.01, "max": 8.0, "step": 0.01}),}}
    KmrPlNMyCntWtQIuwTzhYketzPaLUxAX = ("LATENT",)
    DCeBXQFyPFIKUXphdMmctDGwHwXgHyTw = "upscale"
    VHBvQQsdmXccHUVkiKRmkuIiUnjOTicH = "latent"
    def VFbOpUjlPHhNgAvxtBCPRqDCJyPQDVlx(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, bfpFhSQCEeSgZQwablzNZDcPruUlpnjs, upscale_method, scale_by):
        uPePujIqMVDrwNvZQxJajkuaQFAcacjA = bfpFhSQCEeSgZQwablzNZDcPruUlpnjs.copy()
        QfeoFYGsEQNWblsqXsRKWQpzeXgWujaz = round(bfpFhSQCEeSgZQwablzNZDcPruUlpnjs["samples"].BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[3] * scale_by)
        yhGxnlfJCKaDHyDtiYhJHxHFcooDKiMM = round(bfpFhSQCEeSgZQwablzNZDcPruUlpnjs["samples"].BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[2] * scale_by)
        uPePujIqMVDrwNvZQxJajkuaQFAcacjA["samples"] = quasar.utils.common_upscale(bfpFhSQCEeSgZQwablzNZDcPruUlpnjs["samples"], QfeoFYGsEQNWblsqXsRKWQpzeXgWujaz, yhGxnlfJCKaDHyDtiYhJHxHFcooDKiMM, upscale_method, "disabled")
        return (uPePujIqMVDrwNvZQxJajkuaQFAcacjA,)
class WOgqIJshXGCopywgtFStTTikxaMHHKaW:
    @classmethod
    def hGTeyOvpHejlssWPjkjTHIgcOKnCfnQl(uPePujIqMVDrwNvZQxJajkuaQFAcacjA):
        return {"required": { "samples": ("LATENT",),
                              "rotation": (["none", "90 degrees", "180 degrees", "270 degrees"],),
                              }}
    KmrPlNMyCntWtQIuwTzhYketzPaLUxAX = ("LATENT",)
    DCeBXQFyPFIKUXphdMmctDGwHwXgHyTw = "rotate"
    VHBvQQsdmXccHUVkiKRmkuIiUnjOTicH = "latent/transform"
    def qOOeEbzfVrmXAQAstADIDsiKjQySiavk(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, bfpFhSQCEeSgZQwablzNZDcPruUlpnjs, rotation):
        uPePujIqMVDrwNvZQxJajkuaQFAcacjA = bfpFhSQCEeSgZQwablzNZDcPruUlpnjs.copy()
        VmhHRkNgtBinAfXKqLayDdmJBguJhmZi = 0
        if rotation.startswith("90"):
            VmhHRkNgtBinAfXKqLayDdmJBguJhmZi = 1
        elif rotation.startswith("180"):
            VmhHRkNgtBinAfXKqLayDdmJBguJhmZi = 2
        elif rotation.startswith("270"):
            VmhHRkNgtBinAfXKqLayDdmJBguJhmZi = 3
        uPePujIqMVDrwNvZQxJajkuaQFAcacjA["samples"] = torch.rot90(bfpFhSQCEeSgZQwablzNZDcPruUlpnjs["samples"], EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm=VmhHRkNgtBinAfXKqLayDdmJBguJhmZi, ipYTWVOPDpfJXeTFApPIgldytQSaUFdk=[3, 2])
        return (uPePujIqMVDrwNvZQxJajkuaQFAcacjA,)
class eakUMNdfxMfNUbHaLnvvpbbxcStUaAyg:
    @classmethod
    def hGTeyOvpHejlssWPjkjTHIgcOKnCfnQl(uPePujIqMVDrwNvZQxJajkuaQFAcacjA):
        return {"required": { "samples": ("LATENT",),
                              "flip_method": (["x-axis: vertically", "y-axis: horizontally"],),
                              }}
    KmrPlNMyCntWtQIuwTzhYketzPaLUxAX = ("LATENT",)
    DCeBXQFyPFIKUXphdMmctDGwHwXgHyTw = "flip"
    VHBvQQsdmXccHUVkiKRmkuIiUnjOTicH = "latent/transform"
    def hAHyMhlDympwYBnEsaNWPsolDQrxyovx(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, bfpFhSQCEeSgZQwablzNZDcPruUlpnjs, flip_method):
        uPePujIqMVDrwNvZQxJajkuaQFAcacjA = bfpFhSQCEeSgZQwablzNZDcPruUlpnjs.copy()
        if flip_method.startswith("x"):
            uPePujIqMVDrwNvZQxJajkuaQFAcacjA["samples"] = torch.hAHyMhlDympwYBnEsaNWPsolDQrxyovx(bfpFhSQCEeSgZQwablzNZDcPruUlpnjs["samples"], ipYTWVOPDpfJXeTFApPIgldytQSaUFdk=[2])
        elif flip_method.startswith("y"):
            uPePujIqMVDrwNvZQxJajkuaQFAcacjA["samples"] = torch.hAHyMhlDympwYBnEsaNWPsolDQrxyovx(bfpFhSQCEeSgZQwablzNZDcPruUlpnjs["samples"], ipYTWVOPDpfJXeTFApPIgldytQSaUFdk=[3])
        return (uPePujIqMVDrwNvZQxJajkuaQFAcacjA,)
class gYGSnDAIZlHJnpEujwAuWZmOtsaZAMvG:
    @classmethod
    def hGTeyOvpHejlssWPjkjTHIgcOKnCfnQl(uPePujIqMVDrwNvZQxJajkuaQFAcacjA):
        return {"required": { "samples_to": ("LATENT",),
                              "samples_from": ("LATENT",),
                              "x": ("INT", {"default": 0, "min": 0, "max": tUEqFkJYdZNTmWQilLxLUFxmxzEWYVdq, "step": 8}),
                              "y": ("INT", {"default": 0, "min": 0, "max": tUEqFkJYdZNTmWQilLxLUFxmxzEWYVdq, "step": 8}),
                              "feather": ("INT", {"default": 0, "min": 0, "max": tUEqFkJYdZNTmWQilLxLUFxmxzEWYVdq, "step": 8}),
                              }}
    KmrPlNMyCntWtQIuwTzhYketzPaLUxAX = ("LATENT",)
    DCeBXQFyPFIKUXphdMmctDGwHwXgHyTw = "composite"
    VHBvQQsdmXccHUVkiKRmkuIiUnjOTicH = "latent"
    def opRayBIWIGeypbajgYWLNuQzWlwmqgtb(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, JGYDRGBqBWEeeNCmTRlsklKfoKeHyOmb, YtVGWXlgTlnFnkKIiPMkHfpYwohCAzAo, NECAaWUrFGIXcLimrerEYmxYIykQBfXb, ZljqvWVaiqYAYdTFzQHSTXFDKwgstKaW, composite_method="normal", WabjvlpnDbkaMbyxAEQXjxclHhAnNwAn=0):
        NECAaWUrFGIXcLimrerEYmxYIykQBfXb =  NECAaWUrFGIXcLimrerEYmxYIykQBfXb // 8
        ZljqvWVaiqYAYdTFzQHSTXFDKwgstKaW = ZljqvWVaiqYAYdTFzQHSTXFDKwgstKaW // 8
        WabjvlpnDbkaMbyxAEQXjxclHhAnNwAn = WabjvlpnDbkaMbyxAEQXjxclHhAnNwAn // 8
        HEwGkfdJoXzLVUqwdTDnEjXwUaPPEJZX = JGYDRGBqBWEeeNCmTRlsklKfoKeHyOmb.copy()
        uPePujIqMVDrwNvZQxJajkuaQFAcacjA = JGYDRGBqBWEeeNCmTRlsklKfoKeHyOmb["samples"].tEcQvpBwXwdqvKxRTLEBROBUyPoodldL()
        JGYDRGBqBWEeeNCmTRlsklKfoKeHyOmb = JGYDRGBqBWEeeNCmTRlsklKfoKeHyOmb["samples"]
        YtVGWXlgTlnFnkKIiPMkHfpYwohCAzAo = YtVGWXlgTlnFnkKIiPMkHfpYwohCAzAo["samples"]
        if WabjvlpnDbkaMbyxAEQXjxclHhAnNwAn == 0:
            uPePujIqMVDrwNvZQxJajkuaQFAcacjA[:,:,ZljqvWVaiqYAYdTFzQHSTXFDKwgstKaW:ZljqvWVaiqYAYdTFzQHSTXFDKwgstKaW+YtVGWXlgTlnFnkKIiPMkHfpYwohCAzAo.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[2],NECAaWUrFGIXcLimrerEYmxYIykQBfXb:NECAaWUrFGIXcLimrerEYmxYIykQBfXb+YtVGWXlgTlnFnkKIiPMkHfpYwohCAzAo.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[3]] = YtVGWXlgTlnFnkKIiPMkHfpYwohCAzAo[:,:,:JGYDRGBqBWEeeNCmTRlsklKfoKeHyOmb.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[2] - ZljqvWVaiqYAYdTFzQHSTXFDKwgstKaW, :JGYDRGBqBWEeeNCmTRlsklKfoKeHyOmb.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[3] - NECAaWUrFGIXcLimrerEYmxYIykQBfXb]
        else:
            YtVGWXlgTlnFnkKIiPMkHfpYwohCAzAo = YtVGWXlgTlnFnkKIiPMkHfpYwohCAzAo[:,:,:JGYDRGBqBWEeeNCmTRlsklKfoKeHyOmb.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[2] - ZljqvWVaiqYAYdTFzQHSTXFDKwgstKaW, :JGYDRGBqBWEeeNCmTRlsklKfoKeHyOmb.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[3] - NECAaWUrFGIXcLimrerEYmxYIykQBfXb]
            KHpRlHOzblljQyskecSxzUuWZtneWwta = torch.ones_like(YtVGWXlgTlnFnkKIiPMkHfpYwohCAzAo)
            for XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz in range(WabjvlpnDbkaMbyxAEQXjxclHhAnNwAn):
                if ZljqvWVaiqYAYdTFzQHSTXFDKwgstKaW != 0:
                    KHpRlHOzblljQyskecSxzUuWZtneWwta[:,:,XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz:1+XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz,:] *= ((1.0/WabjvlpnDbkaMbyxAEQXjxclHhAnNwAn) * (XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz + 1))
                if ZljqvWVaiqYAYdTFzQHSTXFDKwgstKaW + YtVGWXlgTlnFnkKIiPMkHfpYwohCAzAo.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[2] < JGYDRGBqBWEeeNCmTRlsklKfoKeHyOmb.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[2]:
                    KHpRlHOzblljQyskecSxzUuWZtneWwta[:,:,KHpRlHOzblljQyskecSxzUuWZtneWwta.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[2] -1 -XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz: KHpRlHOzblljQyskecSxzUuWZtneWwta.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[2]-XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz,:] *= ((1.0/WabjvlpnDbkaMbyxAEQXjxclHhAnNwAn) * (XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz + 1))
                if NECAaWUrFGIXcLimrerEYmxYIykQBfXb != 0:
                    KHpRlHOzblljQyskecSxzUuWZtneWwta[:,:,:,XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz:1+XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz] *= ((1.0/WabjvlpnDbkaMbyxAEQXjxclHhAnNwAn) * (XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz + 1))
                if NECAaWUrFGIXcLimrerEYmxYIykQBfXb + YtVGWXlgTlnFnkKIiPMkHfpYwohCAzAo.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[3] < JGYDRGBqBWEeeNCmTRlsklKfoKeHyOmb.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[3]:
                    KHpRlHOzblljQyskecSxzUuWZtneWwta[:,:,:,KHpRlHOzblljQyskecSxzUuWZtneWwta.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[3]- 1 - XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz: KHpRlHOzblljQyskecSxzUuWZtneWwta.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[3]- XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz] *= ((1.0/WabjvlpnDbkaMbyxAEQXjxclHhAnNwAn) * (XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz + 1))
            tMouwchJRcTnBRZbNGDkNoVRMgfNWNkn = torch.ones_like(KHpRlHOzblljQyskecSxzUuWZtneWwta) - KHpRlHOzblljQyskecSxzUuWZtneWwta
            uPePujIqMVDrwNvZQxJajkuaQFAcacjA[:,:,ZljqvWVaiqYAYdTFzQHSTXFDKwgstKaW:ZljqvWVaiqYAYdTFzQHSTXFDKwgstKaW+YtVGWXlgTlnFnkKIiPMkHfpYwohCAzAo.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[2],NECAaWUrFGIXcLimrerEYmxYIykQBfXb:NECAaWUrFGIXcLimrerEYmxYIykQBfXb+YtVGWXlgTlnFnkKIiPMkHfpYwohCAzAo.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[3]] = YtVGWXlgTlnFnkKIiPMkHfpYwohCAzAo[:,:,:JGYDRGBqBWEeeNCmTRlsklKfoKeHyOmb.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[2] - ZljqvWVaiqYAYdTFzQHSTXFDKwgstKaW, :JGYDRGBqBWEeeNCmTRlsklKfoKeHyOmb.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[3] - NECAaWUrFGIXcLimrerEYmxYIykQBfXb] * KHpRlHOzblljQyskecSxzUuWZtneWwta + uPePujIqMVDrwNvZQxJajkuaQFAcacjA[:,:,ZljqvWVaiqYAYdTFzQHSTXFDKwgstKaW:ZljqvWVaiqYAYdTFzQHSTXFDKwgstKaW+YtVGWXlgTlnFnkKIiPMkHfpYwohCAzAo.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[2],NECAaWUrFGIXcLimrerEYmxYIykQBfXb:NECAaWUrFGIXcLimrerEYmxYIykQBfXb+YtVGWXlgTlnFnkKIiPMkHfpYwohCAzAo.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[3]] * tMouwchJRcTnBRZbNGDkNoVRMgfNWNkn
        HEwGkfdJoXzLVUqwdTDnEjXwUaPPEJZX["samples"] = uPePujIqMVDrwNvZQxJajkuaQFAcacjA
        return (HEwGkfdJoXzLVUqwdTDnEjXwUaPPEJZX,)
class ijfkEMojxbOOfagzcQRAdBkeUApzlBrc:
    @classmethod
    def hGTeyOvpHejlssWPjkjTHIgcOKnCfnQl(uPePujIqMVDrwNvZQxJajkuaQFAcacjA):
        return {"required": {
            "samples1": ("LATENT",),
            "samples2": ("LATENT",),
            "blend_factor": ("FLOAT", {
                "default": 0.5,
                "min": 0,
                "max": 1,
                "step": 0.01
            }),
        }}
    KmrPlNMyCntWtQIuwTzhYketzPaLUxAX = ("LATENT",)
    DCeBXQFyPFIKUXphdMmctDGwHwXgHyTw = "blend"
    VHBvQQsdmXccHUVkiKRmkuIiUnjOTicH = "_for_testing"
    def bInJMvyEcRGRaPSKAOkJVzxIdWgjyBVj(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, IaQtJIzGzeFFfWCXvirhDkmYzRxMEXEw, tpxhxmWydZCngCSetgjZSPlQwiSkJcVX, blend_factor:float, alMEcYmcsKBTbSQtHwFJXFKfgFGSgyGR: str="normal"):
        HEwGkfdJoXzLVUqwdTDnEjXwUaPPEJZX = IaQtJIzGzeFFfWCXvirhDkmYzRxMEXEw.copy()
        IaQtJIzGzeFFfWCXvirhDkmYzRxMEXEw = IaQtJIzGzeFFfWCXvirhDkmYzRxMEXEw["samples"]
        tpxhxmWydZCngCSetgjZSPlQwiSkJcVX = tpxhxmWydZCngCSetgjZSPlQwiSkJcVX["samples"]
        if IaQtJIzGzeFFfWCXvirhDkmYzRxMEXEw.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg != tpxhxmWydZCngCSetgjZSPlQwiSkJcVX.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg:
            tpxhxmWydZCngCSetgjZSPlQwiSkJcVX.permute(0, 3, 1, 2)
            tpxhxmWydZCngCSetgjZSPlQwiSkJcVX = quasar.utils.common_upscale(tpxhxmWydZCngCSetgjZSPlQwiSkJcVX, IaQtJIzGzeFFfWCXvirhDkmYzRxMEXEw.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[3], IaQtJIzGzeFFfWCXvirhDkmYzRxMEXEw.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[2], 'bicubic', CWEytKkepwhdVJpGxZvfxcoPmAcpotMo='center')
            tpxhxmWydZCngCSetgjZSPlQwiSkJcVX.permute(0, 2, 3, 1)
        vbrMdvhHVgeTRlppYSnyOPpySRocNtmD = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.alMEcYmcsKBTbSQtHwFJXFKfgFGSgyGR(IaQtJIzGzeFFfWCXvirhDkmYzRxMEXEw, tpxhxmWydZCngCSetgjZSPlQwiSkJcVX, alMEcYmcsKBTbSQtHwFJXFKfgFGSgyGR)
        vbrMdvhHVgeTRlppYSnyOPpySRocNtmD = IaQtJIzGzeFFfWCXvirhDkmYzRxMEXEw * blend_factor + vbrMdvhHVgeTRlppYSnyOPpySRocNtmD * (1 - blend_factor)
        HEwGkfdJoXzLVUqwdTDnEjXwUaPPEJZX["samples"] = vbrMdvhHVgeTRlppYSnyOPpySRocNtmD
        return (HEwGkfdJoXzLVUqwdTDnEjXwUaPPEJZX,)
    def alMEcYmcsKBTbSQtHwFJXFKfgFGSgyGR(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, img1, img2, bPTwwoDdWiuYqhtrDEHoDbHGiYcwcsQC):
        if bPTwwoDdWiuYqhtrDEHoDbHGiYcwcsQC == "normal":
            return img2
        else:
            raise ValueError(f"Unsupported blend mode: {mode}")
class bRRgXVaHGoMyxYkieovkraXGdqMmbIfw:
    @classmethod
    def hGTeyOvpHejlssWPjkjTHIgcOKnCfnQl(uPePujIqMVDrwNvZQxJajkuaQFAcacjA):
        return {"required": { "samples": ("LATENT",),
                              "width": ("INT", {"default": 512, "min": 64, "max": tUEqFkJYdZNTmWQilLxLUFxmxzEWYVdq, "step": 8}),
                              "height": ("INT", {"default": 512, "min": 64, "max": tUEqFkJYdZNTmWQilLxLUFxmxzEWYVdq, "step": 8}),
                              "x": ("INT", {"default": 0, "min": 0, "max": tUEqFkJYdZNTmWQilLxLUFxmxzEWYVdq, "step": 8}),
                              "y": ("INT", {"default": 0, "min": 0, "max": tUEqFkJYdZNTmWQilLxLUFxmxzEWYVdq, "step": 8}),
                              }}
    KmrPlNMyCntWtQIuwTzhYketzPaLUxAX = ("LATENT",)
    DCeBXQFyPFIKUXphdMmctDGwHwXgHyTw = "crop"
    VHBvQQsdmXccHUVkiKRmkuIiUnjOTicH = "latent/transform"
    def CWEytKkepwhdVJpGxZvfxcoPmAcpotMo(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, bfpFhSQCEeSgZQwablzNZDcPruUlpnjs, QfeoFYGsEQNWblsqXsRKWQpzeXgWujaz, yhGxnlfJCKaDHyDtiYhJHxHFcooDKiMM, NECAaWUrFGIXcLimrerEYmxYIykQBfXb, ZljqvWVaiqYAYdTFzQHSTXFDKwgstKaW):
        uPePujIqMVDrwNvZQxJajkuaQFAcacjA = bfpFhSQCEeSgZQwablzNZDcPruUlpnjs.copy()
        bfpFhSQCEeSgZQwablzNZDcPruUlpnjs = bfpFhSQCEeSgZQwablzNZDcPruUlpnjs['samples']
        NECAaWUrFGIXcLimrerEYmxYIykQBfXb =  NECAaWUrFGIXcLimrerEYmxYIykQBfXb // 8
        ZljqvWVaiqYAYdTFzQHSTXFDKwgstKaW = ZljqvWVaiqYAYdTFzQHSTXFDKwgstKaW // 8
        if NECAaWUrFGIXcLimrerEYmxYIykQBfXb > (bfpFhSQCEeSgZQwablzNZDcPruUlpnjs.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[3] - 8):
            NECAaWUrFGIXcLimrerEYmxYIykQBfXb = bfpFhSQCEeSgZQwablzNZDcPruUlpnjs.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[3] - 8
        if ZljqvWVaiqYAYdTFzQHSTXFDKwgstKaW > (bfpFhSQCEeSgZQwablzNZDcPruUlpnjs.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[2] - 8):
            ZljqvWVaiqYAYdTFzQHSTXFDKwgstKaW = bfpFhSQCEeSgZQwablzNZDcPruUlpnjs.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[2] - 8
        VRNiSmmRJaNeBlmvXZnkkdSBJCFrkrKN = yhGxnlfJCKaDHyDtiYhJHxHFcooDKiMM // 8
        CkiCReqpgQGFefoNqxIStaNFZETshyIp = QfeoFYGsEQNWblsqXsRKWQpzeXgWujaz // 8
        fDDYNhxlXaiUUeKUsFfqKTXPMMSyGfwy = CkiCReqpgQGFefoNqxIStaNFZETshyIp + NECAaWUrFGIXcLimrerEYmxYIykQBfXb
        ddrPPqzOUkqFcrukWAiKntnHCUbFDrWa = VRNiSmmRJaNeBlmvXZnkkdSBJCFrkrKN + ZljqvWVaiqYAYdTFzQHSTXFDKwgstKaW
        uPePujIqMVDrwNvZQxJajkuaQFAcacjA['samples'] = bfpFhSQCEeSgZQwablzNZDcPruUlpnjs[:,:,ZljqvWVaiqYAYdTFzQHSTXFDKwgstKaW:ddrPPqzOUkqFcrukWAiKntnHCUbFDrWa, NECAaWUrFGIXcLimrerEYmxYIykQBfXb:fDDYNhxlXaiUUeKUsFfqKTXPMMSyGfwy]
        return (uPePujIqMVDrwNvZQxJajkuaQFAcacjA,)
class arKbozbiqKYljDImFotqJXydUptICTsb:
    @classmethod
    def hGTeyOvpHejlssWPjkjTHIgcOKnCfnQl(uPePujIqMVDrwNvZQxJajkuaQFAcacjA):
        return {"required": { "samples": ("LATENT",),
                              "mask": ("MASK",),
                              }}
    KmrPlNMyCntWtQIuwTzhYketzPaLUxAX = ("LATENT",)
    DCeBXQFyPFIKUXphdMmctDGwHwXgHyTw = "set_mask"
    VHBvQQsdmXccHUVkiKRmkuIiUnjOTicH = "latent/inpaint"
    def dHwNnIuhHBhrlqVHAqLzSawpIIJMOmDP(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, bfpFhSQCEeSgZQwablzNZDcPruUlpnjs, KHpRlHOzblljQyskecSxzUuWZtneWwta):
        uPePujIqMVDrwNvZQxJajkuaQFAcacjA = bfpFhSQCEeSgZQwablzNZDcPruUlpnjs.copy()
        uPePujIqMVDrwNvZQxJajkuaQFAcacjA["noise_mask"] = KHpRlHOzblljQyskecSxzUuWZtneWwta.reshape((-1, 1, KHpRlHOzblljQyskecSxzUuWZtneWwta.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[-2], KHpRlHOzblljQyskecSxzUuWZtneWwta.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[-1]))
        return (uPePujIqMVDrwNvZQxJajkuaQFAcacjA,)
def VrTyfkloViDyVJTqJFiYkcbkozdWrKWO(VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM, qWZgfPzZGdBXrbWzvrSHUmcFFjBFiMVr, TMepbhrhtxHODfHDPkWDjgPPPikciJwm, cfg, sampler_name, scheduler, positive, negative, CBTHgqHIDKYRBmSTkKCsLapKGpsubmaU, afSgIXbCyfvlQaPfcxHjFSVBhUfKNkhV=1.0, fyayyJDxffYaNOsUuSdLGHwdKplWmvvE=False, start_step=None, last_step=None, SdroGuzHgzxvYzlDqyYiuwcZSghgRDUg=False):
    fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc = quasar.model_management.aIQypJefEzoiiobeXriYBEHMJwDTvZWS()
    EUCBZJorhognNSnYSMyloZOBZaIXmOxH = CBTHgqHIDKYRBmSTkKCsLapKGpsubmaU["samples"]
    if fyayyJDxffYaNOsUuSdLGHwdKplWmvvE:
        jCizDlbKxNNChDZcMjnDhRYUQUZdrTRD = torch.zeros(EUCBZJorhognNSnYSMyloZOBZaIXmOxH.vqDBJgidQufnKyAltPYRqiKGjmztArDJ(), DDRQlhrNSGpwTrokWitkZipdfbAqBFxv=EUCBZJorhognNSnYSMyloZOBZaIXmOxH.DDRQlhrNSGpwTrokWitkZipdfbAqBFxv, layout=EUCBZJorhognNSnYSMyloZOBZaIXmOxH.layout, fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc="cpu")
    else:
        qKdkVchxkqsQPrzQfSGXInAOatiJAhNr = CBTHgqHIDKYRBmSTkKCsLapKGpsubmaU["batch_index"] if "batch_index" in CBTHgqHIDKYRBmSTkKCsLapKGpsubmaU else None
        jCizDlbKxNNChDZcMjnDhRYUQUZdrTRD = quasar.kzeIpaLNSGyUxNmgVakyIZAkNbjmCUjd.ARfYECVuQsMwJUYnSXwVsEboysUjSIIC(EUCBZJorhognNSnYSMyloZOBZaIXmOxH, qWZgfPzZGdBXrbWzvrSHUmcFFjBFiMVr, qKdkVchxkqsQPrzQfSGXInAOatiJAhNr)
    RQSOwDjntUoguZxRsdjPunfoeNXsiRBB = None
    if "noise_mask" in CBTHgqHIDKYRBmSTkKCsLapKGpsubmaU:
        RQSOwDjntUoguZxRsdjPunfoeNXsiRBB = CBTHgqHIDKYRBmSTkKCsLapKGpsubmaU["noise_mask"]
    WZfrTIKIyoLlyebhpXlKkKxkJvbKObWx = "JPEG"
    if WZfrTIKIyoLlyebhpXlKkKxkJvbKObWx not in ["JPEG", "PNG"]:
        WZfrTIKIyoLlyebhpXlKkKxkJvbKObWx = "JPEG"
    fkGHWNVipMbnAvghGXTNMtnLnbwOtXxA = latent_preview.RmTUmCNiTKhZZJUuGDzOoGuaHckIMsts(fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc, VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM.VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM.latent_format)
    ehYcJDzojxbXZiwqMPlEiTyCBgASsEBo = quasar.utils.ProgressBar(TMepbhrhtxHODfHDPkWDjgPPPikciJwm)
    def FJsaFpOBdvpFlEdxOzBgjwcWBUfetQGF(UHmIQCHeLkozPfaktIdEHKdpTVYzCLhe, UBGvtPbFIPlcsBIwyWKuWMZeENGLMRAP, NECAaWUrFGIXcLimrerEYmxYIykQBfXb, TuJjDqKZekSGicNtWVQgPuLDBIQsIxym):
        ljJUDoqGBoyPevlyawCUEFbfPKfJQjML = None
        if fkGHWNVipMbnAvghGXTNMtnLnbwOtXxA:
            ljJUDoqGBoyPevlyawCUEFbfPKfJQjML = fkGHWNVipMbnAvghGXTNMtnLnbwOtXxA.mIDrtSLzTJeUKrWDwktrhIkJMffMQfwW(WZfrTIKIyoLlyebhpXlKkKxkJvbKObWx, UBGvtPbFIPlcsBIwyWKuWMZeENGLMRAP)
        ehYcJDzojxbXZiwqMPlEiTyCBgASsEBo.update_absolute(UHmIQCHeLkozPfaktIdEHKdpTVYzCLhe + 1, TuJjDqKZekSGicNtWVQgPuLDBIQsIxym, ljJUDoqGBoyPevlyawCUEFbfPKfJQjML)
    bfpFhSQCEeSgZQwablzNZDcPruUlpnjs = quasar.kzeIpaLNSGyUxNmgVakyIZAkNbjmCUjd.kzeIpaLNSGyUxNmgVakyIZAkNbjmCUjd(VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM, jCizDlbKxNNChDZcMjnDhRYUQUZdrTRD, TMepbhrhtxHODfHDPkWDjgPPPikciJwm, cfg, sampler_name, scheduler, positive, negative, EUCBZJorhognNSnYSMyloZOBZaIXmOxH,
                                  afSgIXbCyfvlQaPfcxHjFSVBhUfKNkhV=afSgIXbCyfvlQaPfcxHjFSVBhUfKNkhV, fyayyJDxffYaNOsUuSdLGHwdKplWmvvE=fyayyJDxffYaNOsUuSdLGHwdKplWmvvE, start_step=start_step, last_step=last_step,
                                  SdroGuzHgzxvYzlDqyYiuwcZSghgRDUg=SdroGuzHgzxvYzlDqyYiuwcZSghgRDUg, RQSOwDjntUoguZxRsdjPunfoeNXsiRBB=RQSOwDjntUoguZxRsdjPunfoeNXsiRBB, FJsaFpOBdvpFlEdxOzBgjwcWBUfetQGF=FJsaFpOBdvpFlEdxOzBgjwcWBUfetQGF, qWZgfPzZGdBXrbWzvrSHUmcFFjBFiMVr=qWZgfPzZGdBXrbWzvrSHUmcFFjBFiMVr)
    iqymPVpxyjOWChGwBkTemSzHJbnJdAIz = CBTHgqHIDKYRBmSTkKCsLapKGpsubmaU.copy()
    iqymPVpxyjOWChGwBkTemSzHJbnJdAIz["samples"] = bfpFhSQCEeSgZQwablzNZDcPruUlpnjs
    return (iqymPVpxyjOWChGwBkTemSzHJbnJdAIz, )
class fISBgXprrvVNVCupajVDXGsVRGuyiyHR:
    @classmethod
    def hGTeyOvpHejlssWPjkjTHIgcOKnCfnQl(uPePujIqMVDrwNvZQxJajkuaQFAcacjA):
        return {"required":
                    {"model": ("MODEL",),
                    "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}),
                    "steps": ("INT", {"default": 20, "min": 1, "max": 10000}),
                    "cfg": ("FLOAT", {"default": 8.0, "min": 0.0, "max": 100.0}),
                    "sampler_name": (quasar.samplers.fISBgXprrvVNVCupajVDXGsVRGuyiyHR.SAMPLERS, ),
                    "scheduler": (quasar.samplers.fISBgXprrvVNVCupajVDXGsVRGuyiyHR.SCHEDULERS, ),
                    "positive": ("CONDITIONING", ),
                    "negative": ("CONDITIONING", ),
                    "latent_image": ("LATENT", ),
                    "denoise": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 1.0, "step": 0.01}),
                     }
                }
    KmrPlNMyCntWtQIuwTzhYketzPaLUxAX = ("LATENT",)
    DCeBXQFyPFIKUXphdMmctDGwHwXgHyTw = "sample"
    VHBvQQsdmXccHUVkiKRmkuIiUnjOTicH = "sampling"
    def kzeIpaLNSGyUxNmgVakyIZAkNbjmCUjd(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM, qWZgfPzZGdBXrbWzvrSHUmcFFjBFiMVr, TMepbhrhtxHODfHDPkWDjgPPPikciJwm, cfg, sampler_name, scheduler, positive, negative, EUCBZJorhognNSnYSMyloZOBZaIXmOxH, afSgIXbCyfvlQaPfcxHjFSVBhUfKNkhV=1.0):
        return VrTyfkloViDyVJTqJFiYkcbkozdWrKWO(VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM, qWZgfPzZGdBXrbWzvrSHUmcFFjBFiMVr, TMepbhrhtxHODfHDPkWDjgPPPikciJwm, cfg, sampler_name, scheduler, positive, negative, EUCBZJorhognNSnYSMyloZOBZaIXmOxH, afSgIXbCyfvlQaPfcxHjFSVBhUfKNkhV=afSgIXbCyfvlQaPfcxHjFSVBhUfKNkhV)
class TbqdfYdqjaIWoRxYYwvNctpyyzwjXrDr:
    @classmethod
    def hGTeyOvpHejlssWPjkjTHIgcOKnCfnQl(uPePujIqMVDrwNvZQxJajkuaQFAcacjA):
        return {"required":
                    {"model": ("MODEL",),
                    "add_noise": (["enable", "disable"], ),
                    "noise_seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}),
                    "steps": ("INT", {"default": 20, "min": 1, "max": 10000}),
                    "cfg": ("FLOAT", {"default": 8.0, "min": 0.0, "max": 100.0}),
                    "sampler_name": (quasar.samplers.fISBgXprrvVNVCupajVDXGsVRGuyiyHR.SAMPLERS, ),
                    "scheduler": (quasar.samplers.fISBgXprrvVNVCupajVDXGsVRGuyiyHR.SCHEDULERS, ),
                    "positive": ("CONDITIONING", ),
                    "negative": ("CONDITIONING", ),
                    "latent_image": ("LATENT", ),
                    "start_at_step": ("INT", {"default": 0, "min": 0, "max": 10000}),
                    "end_at_step": ("INT", {"default": 10000, "min": 0, "max": 10000}),
                    "return_with_leftover_noise": (["disable", "enable"], ),
                     }
                }
    KmrPlNMyCntWtQIuwTzhYketzPaLUxAX = ("LATENT",)
    DCeBXQFyPFIKUXphdMmctDGwHwXgHyTw = "sample"
    VHBvQQsdmXccHUVkiKRmkuIiUnjOTicH = "sampling"
    def kzeIpaLNSGyUxNmgVakyIZAkNbjmCUjd(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM, add_noise, noise_seed, TMepbhrhtxHODfHDPkWDjgPPPikciJwm, cfg, sampler_name, scheduler, positive, negative, EUCBZJorhognNSnYSMyloZOBZaIXmOxH, start_at_step, end_at_step, return_with_leftover_noise, afSgIXbCyfvlQaPfcxHjFSVBhUfKNkhV=1.0):
        SdroGuzHgzxvYzlDqyYiuwcZSghgRDUg = True
        if return_with_leftover_noise == "enable":
            SdroGuzHgzxvYzlDqyYiuwcZSghgRDUg = False
        fyayyJDxffYaNOsUuSdLGHwdKplWmvvE = False
        if add_noise == "disable":
            fyayyJDxffYaNOsUuSdLGHwdKplWmvvE = True
        return VrTyfkloViDyVJTqJFiYkcbkozdWrKWO(VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM, noise_seed, TMepbhrhtxHODfHDPkWDjgPPPikciJwm, cfg, sampler_name, scheduler, positive, negative, EUCBZJorhognNSnYSMyloZOBZaIXmOxH, afSgIXbCyfvlQaPfcxHjFSVBhUfKNkhV=afSgIXbCyfvlQaPfcxHjFSVBhUfKNkhV, fyayyJDxffYaNOsUuSdLGHwdKplWmvvE=fyayyJDxffYaNOsUuSdLGHwdKplWmvvE, start_step=start_at_step, last_step=end_at_step, SdroGuzHgzxvYzlDqyYiuwcZSghgRDUg=SdroGuzHgzxvYzlDqyYiuwcZSghgRDUg)
class cOwvLoELrBaqKtFDUcUFTaWlGFiYoejW:
    def __init__(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS):
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.DIUNPQiJKWsgpSdsJVPWmcWtoPKBTsdh = folder_paths.gZpMXpjIEjIdWmJXOqOJEBRXYgziLydo()
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.type = "output"
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.prefix_append = ""
    @classmethod
    def hGTeyOvpHejlssWPjkjTHIgcOKnCfnQl(uPePujIqMVDrwNvZQxJajkuaQFAcacjA):
        return {"required": 
                    {"images": ("IMAGE", ),
                     "filename_prefix": ("STRING", {"default": "QuasarUI"})},
                "hidden": {"prompt": "PROMPT", "extra_pnginfo": "EXTRA_PNGINFO"},
                }
    KmrPlNMyCntWtQIuwTzhYketzPaLUxAX = ()
    DCeBXQFyPFIKUXphdMmctDGwHwXgHyTw = "save_images"
    AQnTlfqkrmdAAnLjLNUFibEHomwVhMHv = True
    VHBvQQsdmXccHUVkiKRmkuIiUnjOTicH = "image"
    def zgTRIkFoAJNadBuBoRNGQrkOHouUAJeT(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, kgLFMdERvjTWIqzUwaTgEZNsXvktcIDW, azafsUqgjjnMJDTDVblsTwqgMmfrAEPm="QuasarUI", qKBREHoSgcMHYVCNTapmPyODbBOyQAyv=None, extra_pnginfo=None):
        azafsUqgjjnMJDTDVblsTwqgMmfrAEPm += rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.prefix_append
        NSnmtWjKbAQhROMkmRknqzSaUCojgOin, VpsbOZzufynrTFUvvRofTQeRCOCIKJOM, etmXhuRDTfPuCYAlpkCmiMFiODmDHghZ, EijzAwkTdadIdbBCcDEUbEYNNcstskwi, azafsUqgjjnMJDTDVblsTwqgMmfrAEPm = folder_paths.RzAZobMvYWLmMtiqbeSollhpzISOJhWp(azafsUqgjjnMJDTDVblsTwqgMmfrAEPm, rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.DIUNPQiJKWsgpSdsJVPWmcWtoPKBTsdh, kgLFMdERvjTWIqzUwaTgEZNsXvktcIDW[0].BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[1], kgLFMdERvjTWIqzUwaTgEZNsXvktcIDW[0].BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[0])
        NRctuwUflnRJCsQaTaCNgYJowifAWPqJ = list()
        for eLyJtroPthPCROYWyMphoIrGatNOOXCO in kgLFMdERvjTWIqzUwaTgEZNsXvktcIDW:
            HCXmerBqIMuTscBONzTGKYapYSxWTYHo = 255. * eLyJtroPthPCROYWyMphoIrGatNOOXCO.cpu().numpy()
            UaFpXseNaoqfcpsDACQmTguYDZsTArhs = Image.fromarray(np.WfkwoxQSNMJYbojfdczjmvPaQWPEJurJ(HCXmerBqIMuTscBONzTGKYapYSxWTYHo, 0, 255).astype(np.uint8))
            bpGrrorhUTFbOXgOoJWMtNiVeQXHqzbi = None
            if not DukiculvUpjhZIVvaGinshRSKLSTgVVl.disable_metadata:
                bpGrrorhUTFbOXgOoJWMtNiVeQXHqzbi = PngInfo()
                if qKBREHoSgcMHYVCNTapmPyODbBOyQAyv is not None:
                    bpGrrorhUTFbOXgOoJWMtNiVeQXHqzbi.add_text("prompt", json.dumps(qKBREHoSgcMHYVCNTapmPyODbBOyQAyv))
                if extra_pnginfo is not None:
                    for NECAaWUrFGIXcLimrerEYmxYIykQBfXb in extra_pnginfo:
                        bpGrrorhUTFbOXgOoJWMtNiVeQXHqzbi.add_text(NECAaWUrFGIXcLimrerEYmxYIykQBfXb, json.dumps(extra_pnginfo[NECAaWUrFGIXcLimrerEYmxYIykQBfXb]))
            GGrVUpHsMvVvEYhZgyWAlwaKJQserwts = f"{filename}_{counter:05}_.png"
            UaFpXseNaoqfcpsDACQmTguYDZsTArhs.PXhZDpeqZAdDBfrowpMPOPAWwzXhVAFM(os.paTH.join(NSnmtWjKbAQhROMkmRknqzSaUCojgOin, GGrVUpHsMvVvEYhZgyWAlwaKJQserwts), pnginfo=bpGrrorhUTFbOXgOoJWMtNiVeQXHqzbi, compress_level=4)
            NRctuwUflnRJCsQaTaCNgYJowifAWPqJ.append({
                "filename": GGrVUpHsMvVvEYhZgyWAlwaKJQserwts,
                "subfolder": EijzAwkTdadIdbBCcDEUbEYNNcstskwi,
                "type": rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.type
            })
            etmXhuRDTfPuCYAlpkCmiMFiODmDHghZ += 1
        return { "ui": { "images": NRctuwUflnRJCsQaTaCNgYJowifAWPqJ } }
class UeQFaPokrKNDAXwXltiJjZbftArgTtGT(cOwvLoELrBaqKtFDUcUFTaWlGFiYoejW):
    def __init__(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS):
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.DIUNPQiJKWsgpSdsJVPWmcWtoPKBTsdh = folder_paths.PlSKGeZYRqtlMHiaBRCToWuXDcNhJEvq()
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.type = "temp"
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.prefix_append = "_temp_" + ''.join(random.choice("abcdefghijklmnopqrstupvxyz") for NECAaWUrFGIXcLimrerEYmxYIykQBfXb in range(5))
    @classmethod
    def hGTeyOvpHejlssWPjkjTHIgcOKnCfnQl(uPePujIqMVDrwNvZQxJajkuaQFAcacjA):
        return {"required":
                    {"images": ("IMAGE", ), },
                "hidden": {"prompt": "PROMPT", "extra_pnginfo": "EXTRA_PNGINFO"},
                }
class zyddvzayUcTOalKoSNRLJCQrFGCFpvrU:
    @classmethod
    def hGTeyOvpHejlssWPjkjTHIgcOKnCfnQl(uPePujIqMVDrwNvZQxJajkuaQFAcacjA):
        GhiEkpNFOqhdputxuaWhbKlilzZXSMPs = folder_paths.oLxzopmIeTVwZiWTpRvVAVRpJiaEjmiS()
        DTcHrFlDIwbrZDZHTOmAOTxRFqptCgyE = [f for f in os.listdir(GhiEkpNFOqhdputxuaWhbKlilzZXSMPs) if os.paTH.isfile(os.paTH.join(GhiEkpNFOqhdputxuaWhbKlilzZXSMPs, f))]
        return {"required":
                    {"image": (sorted(DTcHrFlDIwbrZDZHTOmAOTxRFqptCgyE), {"image_upload": True})},
                }
    VHBvQQsdmXccHUVkiKRmkuIiUnjOTicH = "image"
    KmrPlNMyCntWtQIuwTzhYketzPaLUxAX = ("IMAGE", "MASK")
    DCeBXQFyPFIKUXphdMmctDGwHwXgHyTw = "load_image"
    def OBmpZvjoFEKdwVxWYqgLagVWDtIbtRlf(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, eLyJtroPthPCROYWyMphoIrGatNOOXCO):
        SsDANhHMZfeDdUZakZVrHtRdKyhJyvRq = folder_paths.OPtRRiXTVYmRqsnzHEbbUWCzjjPfVhOl(eLyJtroPthPCROYWyMphoIrGatNOOXCO)
        HCXmerBqIMuTscBONzTGKYapYSxWTYHo = Image.open(SsDANhHMZfeDdUZakZVrHtRdKyhJyvRq)
        HCXmerBqIMuTscBONzTGKYapYSxWTYHo = ImageOps.exif_transpose(HCXmerBqIMuTscBONzTGKYapYSxWTYHo)
        eLyJtroPthPCROYWyMphoIrGatNOOXCO = HCXmerBqIMuTscBONzTGKYapYSxWTYHo.convert("RGB")
        eLyJtroPthPCROYWyMphoIrGatNOOXCO = np.array(eLyJtroPthPCROYWyMphoIrGatNOOXCO).astype(np.float32) / 255.0
        eLyJtroPthPCROYWyMphoIrGatNOOXCO = torch.from_numpy(eLyJtroPthPCROYWyMphoIrGatNOOXCO)[None,]
        if 'A' in HCXmerBqIMuTscBONzTGKYapYSxWTYHo.getbands():
            KHpRlHOzblljQyskecSxzUuWZtneWwta = np.array(HCXmerBqIMuTscBONzTGKYapYSxWTYHo.getchannel('A')).astype(np.float32) / 255.0
            KHpRlHOzblljQyskecSxzUuWZtneWwta = 1. - torch.from_numpy(KHpRlHOzblljQyskecSxzUuWZtneWwta)
        else:
            KHpRlHOzblljQyskecSxzUuWZtneWwta = torch.zeros((64,64), DDRQlhrNSGpwTrokWitkZipdfbAqBFxv=torch.float32, fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc="cpu")
        return (eLyJtroPthPCROYWyMphoIrGatNOOXCO, KHpRlHOzblljQyskecSxzUuWZtneWwta)
    @classmethod
    def xChqCjJamsdgOcXgHPiSyUitQVgwKEUj(uPePujIqMVDrwNvZQxJajkuaQFAcacjA, eLyJtroPthPCROYWyMphoIrGatNOOXCO):
        SsDANhHMZfeDdUZakZVrHtRdKyhJyvRq = folder_paths.OPtRRiXTVYmRqsnzHEbbUWCzjjPfVhOl(eLyJtroPthPCROYWyMphoIrGatNOOXCO)
        FTosLGldclAzaiNbwuLMIEtXfrZQpTnU = hashlib.sha256()
        with open(SsDANhHMZfeDdUZakZVrHtRdKyhJyvRq, 'rb') as f:
            FTosLGldclAzaiNbwuLMIEtXfrZQpTnU.update(f.read())
        return FTosLGldclAzaiNbwuLMIEtXfrZQpTnU.digest().hex()
    @classmethod
    def zdUBozptADSRFmScDjrsNpGclJRkfHVt(uPePujIqMVDrwNvZQxJajkuaQFAcacjA, eLyJtroPthPCROYWyMphoIrGatNOOXCO):
        if not folder_paths.LuEtoKSPwnkgulAqhArQxPlLlkJrpWJM(eLyJtroPthPCROYWyMphoIrGatNOOXCO):
            return "Invalid image file: {}".format(eLyJtroPthPCROYWyMphoIrGatNOOXCO)
        return True
class ZeEjviALyZWDytVVOgXIdcLgXBMXFprt:
    depiPHfHHXveRYPQjXQESGsHTSNrrUjS = ["alpha", "red", "green", "blue"]
    @classmethod
    def hGTeyOvpHejlssWPjkjTHIgcOKnCfnQl(uPePujIqMVDrwNvZQxJajkuaQFAcacjA):
        GhiEkpNFOqhdputxuaWhbKlilzZXSMPs = folder_paths.oLxzopmIeTVwZiWTpRvVAVRpJiaEjmiS()
        DTcHrFlDIwbrZDZHTOmAOTxRFqptCgyE = [f for f in os.listdir(GhiEkpNFOqhdputxuaWhbKlilzZXSMPs) if os.paTH.isfile(os.paTH.join(GhiEkpNFOqhdputxuaWhbKlilzZXSMPs, f))]
        return {"required":
                    {"image": (sorted(DTcHrFlDIwbrZDZHTOmAOTxRFqptCgyE), {"image_upload": True}),
                     "channel": (uPePujIqMVDrwNvZQxJajkuaQFAcacjA.depiPHfHHXveRYPQjXQESGsHTSNrrUjS, ), }
                }
    VHBvQQsdmXccHUVkiKRmkuIiUnjOTicH = "mask"
    KmrPlNMyCntWtQIuwTzhYketzPaLUxAX = ("MASK",)
    DCeBXQFyPFIKUXphdMmctDGwHwXgHyTw = "load_image"
    def OBmpZvjoFEKdwVxWYqgLagVWDtIbtRlf(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, eLyJtroPthPCROYWyMphoIrGatNOOXCO, EiApFIHKVDYyxTYijPXtjyqRuQDlhpED):
        SsDANhHMZfeDdUZakZVrHtRdKyhJyvRq = folder_paths.OPtRRiXTVYmRqsnzHEbbUWCzjjPfVhOl(eLyJtroPthPCROYWyMphoIrGatNOOXCO)
        HCXmerBqIMuTscBONzTGKYapYSxWTYHo = Image.open(SsDANhHMZfeDdUZakZVrHtRdKyhJyvRq)
        HCXmerBqIMuTscBONzTGKYapYSxWTYHo = ImageOps.exif_transpose(HCXmerBqIMuTscBONzTGKYapYSxWTYHo)
        if HCXmerBqIMuTscBONzTGKYapYSxWTYHo.getbands() != ("R", "G", "B", "A"):
            HCXmerBqIMuTscBONzTGKYapYSxWTYHo = HCXmerBqIMuTscBONzTGKYapYSxWTYHo.convert("RGBA")
        KHpRlHOzblljQyskecSxzUuWZtneWwta = None
        cjHIelcAqVoHWdLcgzuZiBumKNTVADsY = EiApFIHKVDYyxTYijPXtjyqRuQDlhpED[0].upper()
        if cjHIelcAqVoHWdLcgzuZiBumKNTVADsY in HCXmerBqIMuTscBONzTGKYapYSxWTYHo.getbands():
            KHpRlHOzblljQyskecSxzUuWZtneWwta = np.array(HCXmerBqIMuTscBONzTGKYapYSxWTYHo.getchannel(cjHIelcAqVoHWdLcgzuZiBumKNTVADsY)).astype(np.float32) / 255.0
            KHpRlHOzblljQyskecSxzUuWZtneWwta = torch.from_numpy(KHpRlHOzblljQyskecSxzUuWZtneWwta)
            if cjHIelcAqVoHWdLcgzuZiBumKNTVADsY == 'A':
                KHpRlHOzblljQyskecSxzUuWZtneWwta = 1. - KHpRlHOzblljQyskecSxzUuWZtneWwta
        else:
            KHpRlHOzblljQyskecSxzUuWZtneWwta = torch.zeros((64,64), DDRQlhrNSGpwTrokWitkZipdfbAqBFxv=torch.float32, fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc="cpu")
        return (KHpRlHOzblljQyskecSxzUuWZtneWwta,)
    @classmethod
    def xChqCjJamsdgOcXgHPiSyUitQVgwKEUj(uPePujIqMVDrwNvZQxJajkuaQFAcacjA, eLyJtroPthPCROYWyMphoIrGatNOOXCO, EiApFIHKVDYyxTYijPXtjyqRuQDlhpED):
        SsDANhHMZfeDdUZakZVrHtRdKyhJyvRq = folder_paths.OPtRRiXTVYmRqsnzHEbbUWCzjjPfVhOl(eLyJtroPthPCROYWyMphoIrGatNOOXCO)
        FTosLGldclAzaiNbwuLMIEtXfrZQpTnU = hashlib.sha256()
        with open(SsDANhHMZfeDdUZakZVrHtRdKyhJyvRq, 'rb') as f:
            FTosLGldclAzaiNbwuLMIEtXfrZQpTnU.update(f.read())
        return FTosLGldclAzaiNbwuLMIEtXfrZQpTnU.digest().hex()
    @classmethod
    def zdUBozptADSRFmScDjrsNpGclJRkfHVt(uPePujIqMVDrwNvZQxJajkuaQFAcacjA, eLyJtroPthPCROYWyMphoIrGatNOOXCO, EiApFIHKVDYyxTYijPXtjyqRuQDlhpED):
        if not folder_paths.LuEtoKSPwnkgulAqhArQxPlLlkJrpWJM(eLyJtroPthPCROYWyMphoIrGatNOOXCO):
            return "Invalid image file: {}".format(eLyJtroPthPCROYWyMphoIrGatNOOXCO)
        if EiApFIHKVDYyxTYijPXtjyqRuQDlhpED not in uPePujIqMVDrwNvZQxJajkuaQFAcacjA.depiPHfHHXveRYPQjXQESGsHTSNrrUjS:
            return "Invalid color channel: {}".format(EiApFIHKVDYyxTYijPXtjyqRuQDlhpED)
        return True
class ekKhxNsDPHXIAPxHfenkHUzPgvyWmMyZ:
    nTMejTWQGKEJaifVMLgCiAYoxptTnZdn = ["nearest-exact", "bilinear", "area", "bicubic"]
    XcQdZHKZQDcRHNbXHMmBlmIhMHVffMUf = ["disabled", "center"]
    @classmethod
    def hGTeyOvpHejlssWPjkjTHIgcOKnCfnQl(uPePujIqMVDrwNvZQxJajkuaQFAcacjA):
        return {"required": { "image": ("IMAGE",), "upscale_method": (uPePujIqMVDrwNvZQxJajkuaQFAcacjA.nTMejTWQGKEJaifVMLgCiAYoxptTnZdn,),
                              "width": ("INT", {"default": 512, "min": 1, "max": tUEqFkJYdZNTmWQilLxLUFxmxzEWYVdq, "step": 1}),
                              "height": ("INT", {"default": 512, "min": 1, "max": tUEqFkJYdZNTmWQilLxLUFxmxzEWYVdq, "step": 1}),
                              "crop": (uPePujIqMVDrwNvZQxJajkuaQFAcacjA.XcQdZHKZQDcRHNbXHMmBlmIhMHVffMUf,)}}
    KmrPlNMyCntWtQIuwTzhYketzPaLUxAX = ("IMAGE",)
    DCeBXQFyPFIKUXphdMmctDGwHwXgHyTw = "upscale"
    VHBvQQsdmXccHUVkiKRmkuIiUnjOTicH = "image/upscaling"
    def VFbOpUjlPHhNgAvxtBCPRqDCJyPQDVlx(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, eLyJtroPthPCROYWyMphoIrGatNOOXCO, upscale_method, QfeoFYGsEQNWblsqXsRKWQpzeXgWujaz, yhGxnlfJCKaDHyDtiYhJHxHFcooDKiMM, CWEytKkepwhdVJpGxZvfxcoPmAcpotMo):
        bfpFhSQCEeSgZQwablzNZDcPruUlpnjs = eLyJtroPthPCROYWyMphoIrGatNOOXCO.movedim(-1,1)
        uPePujIqMVDrwNvZQxJajkuaQFAcacjA = quasar.utils.common_upscale(bfpFhSQCEeSgZQwablzNZDcPruUlpnjs, QfeoFYGsEQNWblsqXsRKWQpzeXgWujaz, yhGxnlfJCKaDHyDtiYhJHxHFcooDKiMM, upscale_method, CWEytKkepwhdVJpGxZvfxcoPmAcpotMo)
        uPePujIqMVDrwNvZQxJajkuaQFAcacjA = uPePujIqMVDrwNvZQxJajkuaQFAcacjA.movedim(1,-1)
        return (uPePujIqMVDrwNvZQxJajkuaQFAcacjA,)
class kIkOMEFMfxtUMzRvnvuUdHpvEUCmIJKi:
    nTMejTWQGKEJaifVMLgCiAYoxptTnZdn = ["nearest-exact", "bilinear", "area", "bicubic"]
    @classmethod
    def hGTeyOvpHejlssWPjkjTHIgcOKnCfnQl(uPePujIqMVDrwNvZQxJajkuaQFAcacjA):
        return {"required": { "image": ("IMAGE",), "upscale_method": (uPePujIqMVDrwNvZQxJajkuaQFAcacjA.nTMejTWQGKEJaifVMLgCiAYoxptTnZdn,),
                              "scale_by": ("FLOAT", {"default": 1.0, "min": 0.01, "max": 8.0, "step": 0.01}),}}
    KmrPlNMyCntWtQIuwTzhYketzPaLUxAX = ("IMAGE",)
    DCeBXQFyPFIKUXphdMmctDGwHwXgHyTw = "upscale"
    VHBvQQsdmXccHUVkiKRmkuIiUnjOTicH = "image/upscaling"
    def VFbOpUjlPHhNgAvxtBCPRqDCJyPQDVlx(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, eLyJtroPthPCROYWyMphoIrGatNOOXCO, upscale_method, scale_by):
        bfpFhSQCEeSgZQwablzNZDcPruUlpnjs = eLyJtroPthPCROYWyMphoIrGatNOOXCO.movedim(-1,1)
        QfeoFYGsEQNWblsqXsRKWQpzeXgWujaz = round(bfpFhSQCEeSgZQwablzNZDcPruUlpnjs.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[3] * scale_by)
        yhGxnlfJCKaDHyDtiYhJHxHFcooDKiMM = round(bfpFhSQCEeSgZQwablzNZDcPruUlpnjs.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[2] * scale_by)
        uPePujIqMVDrwNvZQxJajkuaQFAcacjA = quasar.utils.common_upscale(bfpFhSQCEeSgZQwablzNZDcPruUlpnjs, QfeoFYGsEQNWblsqXsRKWQpzeXgWujaz, yhGxnlfJCKaDHyDtiYhJHxHFcooDKiMM, upscale_method, "disabled")
        uPePujIqMVDrwNvZQxJajkuaQFAcacjA = uPePujIqMVDrwNvZQxJajkuaQFAcacjA.movedim(1,-1)
        return (uPePujIqMVDrwNvZQxJajkuaQFAcacjA,)
class oxjdRXmocXYCgrBJmPvTNNexvWbVGCXw:
    @classmethod
    def hGTeyOvpHejlssWPjkjTHIgcOKnCfnQl(uPePujIqMVDrwNvZQxJajkuaQFAcacjA):
        return {"required": { "image": ("IMAGE",)}}
    KmrPlNMyCntWtQIuwTzhYketzPaLUxAX = ("IMAGE",)
    DCeBXQFyPFIKUXphdMmctDGwHwXgHyTw = "invert"
    VHBvQQsdmXccHUVkiKRmkuIiUnjOTicH = "image"
    def oolYJHbVDuylUOWWjzbEQnlxkISHBtdp(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, eLyJtroPthPCROYWyMphoIrGatNOOXCO):
        uPePujIqMVDrwNvZQxJajkuaQFAcacjA = 1.0 - eLyJtroPthPCROYWyMphoIrGatNOOXCO
        return (uPePujIqMVDrwNvZQxJajkuaQFAcacjA,)
class MCaSNQSNUViNxaJnQXXUGtZJsbXoekYu:
    @classmethod
    def hGTeyOvpHejlssWPjkjTHIgcOKnCfnQl(uPePujIqMVDrwNvZQxJajkuaQFAcacjA):
        return {"required": { "image1": ("IMAGE",), "image2": ("IMAGE",)}}
    KmrPlNMyCntWtQIuwTzhYketzPaLUxAX = ("IMAGE",)
    DCeBXQFyPFIKUXphdMmctDGwHwXgHyTw = "batch"
    VHBvQQsdmXccHUVkiKRmkuIiUnjOTicH = "image"
    def IEfFCfCTfyvJvVHxiDPsIOnopGWoUJhP(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, image1, AHpbOSBPqIZltNBkRsJfnveOWolgiLMI):
        if image1.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[1:] != AHpbOSBPqIZltNBkRsJfnveOWolgiLMI.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[1:]:
            AHpbOSBPqIZltNBkRsJfnveOWolgiLMI = quasar.utils.common_upscale(AHpbOSBPqIZltNBkRsJfnveOWolgiLMI.movedim(-1,1), image1.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[2], image1.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[1], "bilinear", "center").movedim(1,-1)
        uPePujIqMVDrwNvZQxJajkuaQFAcacjA = torch.cat((image1, AHpbOSBPqIZltNBkRsJfnveOWolgiLMI), yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk=0)
        return (uPePujIqMVDrwNvZQxJajkuaQFAcacjA,)
class nmMKoEkwXQFTTciXhCTpkqkBwDxGYqMr:
    def __init__(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc="cpu"):
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc = fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc
    @classmethod
    def hGTeyOvpHejlssWPjkjTHIgcOKnCfnQl(uPePujIqMVDrwNvZQxJajkuaQFAcacjA):
        return {"required": { "width": ("INT", {"default": 512, "min": 1, "max": tUEqFkJYdZNTmWQilLxLUFxmxzEWYVdq, "step": 1}),
                              "height": ("INT", {"default": 512, "min": 1, "max": tUEqFkJYdZNTmWQilLxLUFxmxzEWYVdq, "step": 1}),
                              "batch_size": ("INT", {"default": 1, "min": 1, "max": 64}),
                              "color": ("INT", {"default": 0, "min": 0, "max": 0xFFFFFF, "step": 1, "display": "color"}),
                              }}
    KmrPlNMyCntWtQIuwTzhYketzPaLUxAX = ("IMAGE",)
    DCeBXQFyPFIKUXphdMmctDGwHwXgHyTw = "generate"
    VHBvQQsdmXccHUVkiKRmkuIiUnjOTicH = "image"
    def cMNLLVrjBWvAYnKLhGgZwcTNuoUSsokk(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, QfeoFYGsEQNWblsqXsRKWQpzeXgWujaz, yhGxnlfJCKaDHyDtiYhJHxHFcooDKiMM, batch_size=1, color=0):
        r = torch.full([batch_size, yhGxnlfJCKaDHyDtiYhJHxHFcooDKiMM, QfeoFYGsEQNWblsqXsRKWQpzeXgWujaz, 1], ((color >> 16) & 0xFF) / 0xFF)
        zjSCLdcRnfaSDwMwtPZkXXzptdHpOEDh = torch.full([batch_size, yhGxnlfJCKaDHyDtiYhJHxHFcooDKiMM, QfeoFYGsEQNWblsqXsRKWQpzeXgWujaz, 1], ((color >> 8) & 0xFF) / 0xFF)
        b = torch.full([batch_size, yhGxnlfJCKaDHyDtiYhJHxHFcooDKiMM, QfeoFYGsEQNWblsqXsRKWQpzeXgWujaz, 1], ((color) & 0xFF) / 0xFF)
        return (torch.cat((r, zjSCLdcRnfaSDwMwtPZkXXzptdHpOEDh, b), yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk=-1), )
class HqsPvyaghocPmHpPPQvZsgJWCpoFqXfm:
    @classmethod
    def hGTeyOvpHejlssWPjkjTHIgcOKnCfnQl(uPePujIqMVDrwNvZQxJajkuaQFAcacjA):
        return {
            "required": {
                "image": ("IMAGE",),
                "left": ("INT", {"default": 0, "min": 0, "max": tUEqFkJYdZNTmWQilLxLUFxmxzEWYVdq, "step": 8}),
                "top": ("INT", {"default": 0, "min": 0, "max": tUEqFkJYdZNTmWQilLxLUFxmxzEWYVdq, "step": 8}),
                "right": ("INT", {"default": 0, "min": 0, "max": tUEqFkJYdZNTmWQilLxLUFxmxzEWYVdq, "step": 8}),
                "bottom": ("INT", {"default": 0, "min": 0, "max": tUEqFkJYdZNTmWQilLxLUFxmxzEWYVdq, "step": 8}),
                "feathering": ("INT", {"default": 40, "min": 0, "max": tUEqFkJYdZNTmWQilLxLUFxmxzEWYVdq, "step": 1}),
            }
        }
    KmrPlNMyCntWtQIuwTzhYketzPaLUxAX = ("IMAGE", "MASK")
    DCeBXQFyPFIKUXphdMmctDGwHwXgHyTw = "expand_image"
    VHBvQQsdmXccHUVkiKRmkuIiUnjOTicH = "image"
    def aUJekyQRJTAnITLgFUCxRMExgCogGzNM(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, eLyJtroPthPCROYWyMphoIrGatNOOXCO, left, top, right, bottom, feathering):
        tbuZnqNEmikCJaKNSLmSqWpMDYVUBzXX, qmVBooQzqysdVWXJerZDBEhryENmpgND, zaSBgPHyzfhxuJsBivIQNoqOsOoJYGsQ, LpoIYArCEUCzsxAjgXNuHOsXqmCHmxOf = eLyJtroPthPCROYWyMphoIrGatNOOXCO.vqDBJgidQufnKyAltPYRqiKGjmztArDJ()
        igalOJmhTttdqurwERHFojRFQRQLJPMJ = torch.zeros(
            (tbuZnqNEmikCJaKNSLmSqWpMDYVUBzXX, qmVBooQzqysdVWXJerZDBEhryENmpgND + top + bottom, zaSBgPHyzfhxuJsBivIQNoqOsOoJYGsQ + left + right, LpoIYArCEUCzsxAjgXNuHOsXqmCHmxOf),
            DDRQlhrNSGpwTrokWitkZipdfbAqBFxv=torch.float32,
        )
        igalOJmhTttdqurwERHFojRFQRQLJPMJ[:, top:top + qmVBooQzqysdVWXJerZDBEhryENmpgND, left:left + zaSBgPHyzfhxuJsBivIQNoqOsOoJYGsQ, :] = eLyJtroPthPCROYWyMphoIrGatNOOXCO
        KHpRlHOzblljQyskecSxzUuWZtneWwta = torch.ones(
            (qmVBooQzqysdVWXJerZDBEhryENmpgND + top + bottom, zaSBgPHyzfhxuJsBivIQNoqOsOoJYGsQ + left + right),
            DDRQlhrNSGpwTrokWitkZipdfbAqBFxv=torch.float32,
        )
        XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz = torch.zeros(
            (qmVBooQzqysdVWXJerZDBEhryENmpgND, zaSBgPHyzfhxuJsBivIQNoqOsOoJYGsQ),
            DDRQlhrNSGpwTrokWitkZipdfbAqBFxv=torch.float32
        )
        if feathering > 0 and feathering * 2 < qmVBooQzqysdVWXJerZDBEhryENmpgND and feathering * 2 < zaSBgPHyzfhxuJsBivIQNoqOsOoJYGsQ:
            for HCXmerBqIMuTscBONzTGKYapYSxWTYHo in range(qmVBooQzqysdVWXJerZDBEhryENmpgND):
                for VyjoFEMsihtolZHiuwJuxJKmDsIroAsQ in range(zaSBgPHyzfhxuJsBivIQNoqOsOoJYGsQ):
                    rYtAWlTfuJKXWhYOjYFOlRbQzowyoxFG = HCXmerBqIMuTscBONzTGKYapYSxWTYHo if top != 0 else qmVBooQzqysdVWXJerZDBEhryENmpgND
                    nMsmwuJOaPgHDsSpElTYkmfVCoEpsdoF = qmVBooQzqysdVWXJerZDBEhryENmpgND - HCXmerBqIMuTscBONzTGKYapYSxWTYHo if bottom != 0 else qmVBooQzqysdVWXJerZDBEhryENmpgND
                    DSNpLYIYzkPZezQjHTLFFaVwYPmeIZJD = VyjoFEMsihtolZHiuwJuxJKmDsIroAsQ if left != 0 else zaSBgPHyzfhxuJsBivIQNoqOsOoJYGsQ
                    LorRfJYMeVebKyQuJLWXNrhpvJfaKjIm = zaSBgPHyzfhxuJsBivIQNoqOsOoJYGsQ - VyjoFEMsihtolZHiuwJuxJKmDsIroAsQ if right != 0 else zaSBgPHyzfhxuJsBivIQNoqOsOoJYGsQ
                    TXGwYXNLgQsYzfHHpRBDJGFCFZEClzIo = min(rYtAWlTfuJKXWhYOjYFOlRbQzowyoxFG, nMsmwuJOaPgHDsSpElTYkmfVCoEpsdoF, DSNpLYIYzkPZezQjHTLFFaVwYPmeIZJD, LorRfJYMeVebKyQuJLWXNrhpvJfaKjIm)
                    if TXGwYXNLgQsYzfHHpRBDJGFCFZEClzIo >= feathering:
                        continue
                    powGafreWfwlSAqPpTpUhFgpFVqCPavl = (feathering - TXGwYXNLgQsYzfHHpRBDJGFCFZEClzIo) / feathering
                    XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz[HCXmerBqIMuTscBONzTGKYapYSxWTYHo, VyjoFEMsihtolZHiuwJuxJKmDsIroAsQ] = powGafreWfwlSAqPpTpUhFgpFVqCPavl * powGafreWfwlSAqPpTpUhFgpFVqCPavl
        KHpRlHOzblljQyskecSxzUuWZtneWwta[top:top + qmVBooQzqysdVWXJerZDBEhryENmpgND, left:left + zaSBgPHyzfhxuJsBivIQNoqOsOoJYGsQ] = XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz
        return (igalOJmhTttdqurwERHFojRFQRQLJPMJ, KHpRlHOzblljQyskecSxzUuWZtneWwta)
wJhMfuyrPNjllkMCYXdJHMhubCAizKhP = {
    "KSampler": fISBgXprrvVNVCupajVDXGsVRGuyiyHR,
    "CheckpointLoaderSimple": rrffnjNRHZdVtoFFMasAclfpghoZjVny,
    "CLIPTextEncode": xFugYlszeGKAKGYYiugpgdmBdgLdixjN,
    "CLIPSetLastLayer": LlMizUiJpMXLbfAHRtmaTRtawJCkifXa,
    "VAEDecode": tkeFAusZeYzBDPFSpXbBAbSiGuguweLJ,
    "VAEEncode": yHdOrZGLzaZsuJPMNoADlrOQJtKypbUC,
    "VAEEncodeForInpaint": XcLrUEEGwySqZlhOsrsQexLVMCIATlUX,
    "VAELoader": AuhSmKRAtBABiDBVlzvkmHPAQcReZjMt,
    "EmptyLatentImage": zIvxPokXhsKQUkwRRjDGfhTCiBLEdtiP,
    "LatentUpscale": nnaIKRoFlXjuwnjMXMUxgnefIWJmKJCF,
    "LatentUpscaleBy": cmbmlESGPTsYIXObNNeWTijDvbyxFcvY,
    "LatentFromBatch": BjeSWOzISSYoyQOEAUTNgdoiiiyDqqkI,
    "RepeatLatentBatch": adIeuebYdlahZUgrpwIFCsqBprKAwwnF,
    "SaveImage": cOwvLoELrBaqKtFDUcUFTaWlGFiYoejW,
    "PreviewImage": UeQFaPokrKNDAXwXltiJjZbftArgTtGT,
    "LoadImage": zyddvzayUcTOalKoSNRLJCQrFGCFpvrU,
    "LoadImageMask": ZeEjviALyZWDytVVOgXIdcLgXBMXFprt,
    "ImageScale": ekKhxNsDPHXIAPxHfenkHUzPgvyWmMyZ,
    "ImageScaleBy": kIkOMEFMfxtUMzRvnvuUdHpvEUCmIJKi,
    "ImageInvert": oxjdRXmocXYCgrBJmPvTNNexvWbVGCXw,
    "ImageBatch": MCaSNQSNUViNxaJnQXXUGtZJsbXoekYu,
    "ImagePadForOutpaint": HqsPvyaghocPmHpPPQvZsgJWCpoFqXfm,
    "EmptyImage": nmMKoEkwXQFTTciXhCTpkqkBwDxGYqMr,
    "ConditioningAverage ": lkWhhWnSlSzqLNbmCZhegjWlIcKUZzIc ,
    "ConditioningCombine": qvtLCeXRQPHPReAlvcQavnYuAcYQHAdD,
    "ConditioningConcat": VXMFcQDwHLDiOqVxzpyZwaXkTroGCAPs,
    "ConditioningSetArea": uiryePJpXaKctwLymJTRGmDYTnmFpOVu,
    "ConditioningSetAreaPercentage": MOhYaVYOzpeAtEFqcdIAWHKLQcntTzGT,
    "ConditioningSetMask": sGJAjzbAeEjMjezMdZmhSjpUrztuIxrd,
    "KSamplerAdvanced": TbqdfYdqjaIWoRxYYwvNctpyyzwjXrDr,
    "SetLatentNoiseMask": arKbozbiqKYljDImFotqJXydUptICTsb,
    "LatentComposite": gYGSnDAIZlHJnpEujwAuWZmOtsaZAMvG,
    "LatentBlend": ijfkEMojxbOOfagzcQRAdBkeUApzlBrc,
    "LatentRotate": WOgqIJshXGCopywgtFStTTikxaMHHKaW,
    "LatentFlip": eakUMNdfxMfNUbHaLnvvpbbxcStUaAyg,
    "LatentCrop": bRRgXVaHGoMyxYkieovkraXGdqMmbIfw,
    "LoraLoader": tWARkCwiRcNpBDFPksBMZyyZlnZeQKXT,
    "CLIPLoader": wjTFuRtlDVnDUEKlDqDyfyFIojrwJSZB,
    "UNETLoader": ZJIPzHKaCxfzJZCrIPDhFmCviGVBHwxT,
    "DualCLIPLoader": wFxydWVsOuPMENdbkVzPjDhmMOqXFXMA,
    "CLIPVisionEncode": dirxAbDzGLspwIXNciTiCbXOItASPyRD,
    "StyleModelApply": SOjubiEONXRlmSXXxhVtITwyixpxICwa,
    "unCLIPConditioning": YDCxaWxzbjsFNDcwFDNikWNamdFKYEJr,
    "ControlNetApply": mVdMRJHDdUUxGEmDqyogULmBPSgLFyjR,
    "ControlNetApplyAdvanced": KSblUWNSuJYUKDpCFiDcqJtyOSxtwxBN,
    "ControlNetLoader": YNFxJlmnzZYMUgkvImenKmRbdZZaHHKo,
    "DiffControlNetLoader": zQYTVSuLxhISGqACelxrijpNlRcWHRPc,
    "StyleModelLoader": WyUqJFjBBSkvXHOuTDxxHFYkYqJqzebh,
    "CLIPVisionLoader": VBGplsVXOYjOSHSeaszMPcfeqtPzrirl,
    "VAEDecodeTiled": CcxzNqovaHQVHpxKUeCssGusFOficgdF,
    "VAEEncodeTiled": GnDUARhnfPPMFDGTRWPeOnvfVZuTBjBJ,
    "unCLIPCheckpointLoader": qGILltCyOYXZISZAQqJTdClRJVMIyVhd,
    "GLIGENLoader": pmpJQceZGpDQRSmOmKyZwIscUkTsJOkN,
    "GLIGENTextBoxApply": tYtrMfFbaFUvQdAhLmTEXiDxugViLiCm,
    "CheckpointLoader": gJrMIsATfnXkyxPPuPvhyrflWJwbfiOu,
    "DiffusersLoader": bsDPHyAnZXnIosnIiQuPBGqfEMEJIqBd,
    "LoadLatent": VTKGSJncLiFeXyZiGvTCgFXfSARuMFAd,
    "SaveLatent": KNkmvkLrAPwddvOOzCKLuJvoplliUlqI,
    "ConditioningZeroOut": MbOIIXitffUZYmaOhrWLoXmkaSHBaWAJ,
    "ConditioningSetTimestepRange": xkewWZVEtrrwkpVxpgXOzhuLNUDrAyoA,
}
fCNmqhLiPJmYYCEegZyrwHUKFhfIrdcf = {
    "KSampler": "KSampler",
    "KSamplerAdvanced": "KSampler (Advanced)",
    "CheckpointLoader": "Load Checkpoint (With Config)",
    "CheckpointLoaderSimple": "Load Checkpoint",
    "VAELoader": "Load VAE",
    "LoraLoader": "Load LoRA",
    "CLIPLoader": "Load CLIP",
    "ControlNetLoader": "Load ControlNet Model",
    "DiffControlNetLoader": "Load ControlNet Model (diff)",
    "StyleModelLoader": "Load Style Model",
    "CLIPVisionLoader": "Load CLIP Vision",
    "UpscaleModelLoader": "Load Upscale Model",
    "CLIPVisionEncode": "CLIP Vision Encode",
    "StyleModelApply": "Apply Style Model",
    "CLIPTextEncode": "CLIP Text Encode (Prompt)",
    "CLIPSetLastLayer": "CLIP Set Last Layer",
    "ConditioningCombine": "Conditioning (Combine)",
    "ConditioningAverage ": "Conditioning (Average)",
    "ConditioningConcat": "Conditioning (Concat)",
    "ConditioningSetArea": "Conditioning (Set Area)",
    "ConditioningSetAreaPercentage": "Conditioning (Set Area with Percentage)",
    "ConditioningSetMask": "Conditioning (Set Mask)",
    "ControlNetApply": "Apply ControlNet",
    "ControlNetApplyAdvanced": "Apply ControlNet (Advanced)",
    "VAEEncodeForInpaint": "VAE Encode (for Inpainting)",
    "SetLatentNoiseMask": "Set Latent Noise Mask",
    "VAEDecode": "VAE Decode",
    "VAEEncode": "VAE Encode",
    "LatentRotate": "Rotate Latent",
    "LatentFlip": "Flip Latent",
    "LatentCrop": "Crop Latent",
    "EmptyLatentImage": "Empty Latent Image",
    "LatentUpscale": "Upscale Latent",
    "LatentUpscaleBy": "Upscale Latent By",
    "LatentComposite": "Latent Composite",
    "LatentBlend": "Latent Blend",
    "LatentFromBatch" : "Latent From Batch",
    "RepeatLatentBatch": "Repeat Latent Batch",
    "SaveImage": "Save Image",
    "PreviewImage": "Preview Image",
    "LoadImage": "Load Image",
    "LoadImageMask": "Load Image (as Mask)",
    "ImageScale": "Upscale Image",
    "ImageScaleBy": "Upscale Image By",
    "ImageUpscaleWithModel": "Upscale Image (using Model)",
    "ImageInvert": "Invert Image",
    "ImagePadForOutpaint": "Pad Image for Outpainting",
    "ImageBatch": "Batch Images",
    "VAEDecodeTiled": "VAE Decode (Tiled)",
    "VAEEncodeTiled": "VAE Encode (Tiled)",
}
OhQOpxGGCySHXalbRgaNhmvFYyGbOLxZ = {}
def VVKZvVLFAmyrpzGZnQKVirGaBCVRzrra(XWKGqxiJgzdJvlFfjMTZuUNvLEbEKBVp, ignore=set()):
    tieEujcveVfDzVXIDWvRBbuhQgiLzcLd = os.paTH.basename(XWKGqxiJgzdJvlFfjMTZuUNvLEbEKBVp)
    if os.paTH.isfile(XWKGqxiJgzdJvlFfjMTZuUNvLEbEKBVp):
        YrPeqrQYIiCxLZFaspxcenNGsDJCGTQo = os.paTH.splitext(XWKGqxiJgzdJvlFfjMTZuUNvLEbEKBVp)
        tieEujcveVfDzVXIDWvRBbuhQgiLzcLd = YrPeqrQYIiCxLZFaspxcenNGsDJCGTQo[0]
    try:
        if os.paTH.isfile(XWKGqxiJgzdJvlFfjMTZuUNvLEbEKBVp):
            module_spec = importlib.util.spec_from_file_location(tieEujcveVfDzVXIDWvRBbuhQgiLzcLd, XWKGqxiJgzdJvlFfjMTZuUNvLEbEKBVp)
            mUseerIsvzYRsklATJBKxbxJiqbRUjQq = os.paTH.split(XWKGqxiJgzdJvlFfjMTZuUNvLEbEKBVp)[0]
        else:
            module_spec = importlib.util.spec_from_file_location(tieEujcveVfDzVXIDWvRBbuhQgiLzcLd, os.paTH.join(XWKGqxiJgzdJvlFfjMTZuUNvLEbEKBVp, "__init__.py"))
            mUseerIsvzYRsklATJBKxbxJiqbRUjQq = XWKGqxiJgzdJvlFfjMTZuUNvLEbEKBVp
        module = importlib.util.module_from_spec(wFboHlUzaysMqHAXRfCClEiaEHkJKBhv)
        sys.modules[tieEujcveVfDzVXIDWvRBbuhQgiLzcLd] = FRIBQCDfDDxIonplwxvPCicvOmmOgYPC
        wFboHlUzaysMqHAXRfCClEiaEHkJKBhv.loader.exec_module(FRIBQCDfDDxIonplwxvPCicvOmmOgYPC)
        if hasattr(FRIBQCDfDDxIonplwxvPCicvOmmOgYPC, "WEB_DIRECTORY") and getattr(FRIBQCDfDDxIonplwxvPCicvOmmOgYPC, "WEB_DIRECTORY") is not None:
            YCwPMrCfndvbAsdSRIxJujNhkijrxjqq = os.paTH.abspath(os.paTH.join(mUseerIsvzYRsklATJBKxbxJiqbRUjQq, getattr(FRIBQCDfDDxIonplwxvPCicvOmmOgYPC, "WEB_DIRECTORY")))
            if os.paTH.isdir(YCwPMrCfndvbAsdSRIxJujNhkijrxjqq):
                OhQOpxGGCySHXalbRgaNhmvFYyGbOLxZ[tieEujcveVfDzVXIDWvRBbuhQgiLzcLd] = YCwPMrCfndvbAsdSRIxJujNhkijrxjqq
        if hasattr(FRIBQCDfDDxIonplwxvPCicvOmmOgYPC, "NODE_CLASS_MAPPINGS") and getattr(FRIBQCDfDDxIonplwxvPCicvOmmOgYPC, "NODE_CLASS_MAPPINGS") is not None:
            for pSfJNVvqLWVlUeHdpahCTGSrSPJYAnEQ in FRIBQCDfDDxIonplwxvPCicvOmmOgYPC.wJhMfuyrPNjllkMCYXdJHMhubCAizKhP:
                if pSfJNVvqLWVlUeHdpahCTGSrSPJYAnEQ not in ignore:
                    wJhMfuyrPNjllkMCYXdJHMhubCAizKhP[pSfJNVvqLWVlUeHdpahCTGSrSPJYAnEQ] = FRIBQCDfDDxIonplwxvPCicvOmmOgYPC.wJhMfuyrPNjllkMCYXdJHMhubCAizKhP[pSfJNVvqLWVlUeHdpahCTGSrSPJYAnEQ]
            if hasattr(FRIBQCDfDDxIonplwxvPCicvOmmOgYPC, "NODE_DISPLAY_NAME_MAPPINGS") and getattr(FRIBQCDfDDxIonplwxvPCicvOmmOgYPC, "NODE_DISPLAY_NAME_MAPPINGS") is not None:
                fCNmqhLiPJmYYCEegZyrwHUKFhfIrdcf.update(FRIBQCDfDDxIonplwxvPCicvOmmOgYPC.fCNmqhLiPJmYYCEegZyrwHUKFhfIrdcf)
            return True
        else:
            print(f"Skip {module_path} module for custom nodes due to the lack of NODE_CLASS_MAPPINGS.")
            return False
    except Exception as dgvKdkEDrMSdkCaRxfkDNVbaXWUetgtO:
        print(traceback.format_exc())
        print(f"Cannot import {module_path} module for custom nodes:", e)
        return False
def dcfAcZtKluJqyIGNEuRjJvrqFDjMRAov():
    xGHXeNMXhwogNiYpBBpsWEKxnckwdywG = set(wJhMfuyrPNjllkMCYXdJHMhubCAizKhP.keys())
    ilqocNyegtMYlXcyAFNfxWmTetNNqjnj = folder_paths.HXYNxZJQjELjaaxuKjoZoxFzWaIvOYmT("custom_nodes")
    node_import_times = []
    for tbhgVJfBEgGoZORDUqSjCwMtYKScIpcZ in ilqocNyegtMYlXcyAFNfxWmTetNNqjnj:
        HkkqgQWYDLsuxsCvbAqAGbfYAPmyFswl = os.listdir(tbhgVJfBEgGoZORDUqSjCwMtYKScIpcZ)
        if "__pycache__" in HkkqgQWYDLsuxsCvbAqAGbfYAPmyFswl:
            HkkqgQWYDLsuxsCvbAqAGbfYAPmyFswl.remove("__pycache__")
        for uzcEftlpQdaRTMylsKksTMmyjgzcrlLK in HkkqgQWYDLsuxsCvbAqAGbfYAPmyFswl:
            XWKGqxiJgzdJvlFfjMTZuUNvLEbEKBVp = os.paTH.join(tbhgVJfBEgGoZORDUqSjCwMtYKScIpcZ, uzcEftlpQdaRTMylsKksTMmyjgzcrlLK)
            if os.paTH.isfile(XWKGqxiJgzdJvlFfjMTZuUNvLEbEKBVp) and os.paTH.splitext(XWKGqxiJgzdJvlFfjMTZuUNvLEbEKBVp)[1] != ".py": continue
            if XWKGqxiJgzdJvlFfjMTZuUNvLEbEKBVp.endswith(".disabled"): continue
            NxDTHICOqkfnhyLwtejLSCWiivMDAyZv = time.perf_counter()
            syoCixXNjFxZAimZmlHgvNsypzGRqzuD = VVKZvVLFAmyrpzGZnQKVirGaBCVRzrra(XWKGqxiJgzdJvlFfjMTZuUNvLEbEKBVp, xGHXeNMXhwogNiYpBBpsWEKxnckwdywG)
            node_import_times.append((time.perf_counter() - time_before, module_path, success))
    if len(node_import_times) > 0:
        print("\nImport times for custom nodes:")
        for n in sorted(node_import_times):
            if zXHJFiFFvWqeQIAxyaTGMUgoRaHrYzjK[2]:
                import_message = ""
            else:
                import_message = " (IMPORT FAILED)"
            print("{:6.1f} seconds{}:".format(n[0], import_message), n[1])
        print()
def TfsMRLhzuJSfPYCmvEXkbVNjMGyUQnEL():
    VVKZvVLFAmyrpzGZnQKVirGaBCVRzrra(os.paTH.join(os.paTH.join(os.paTH.dirname(os.paTH.realpath(__file__)), "quasar_extras"), "nodes_hypernetwork.py"))
    VVKZvVLFAmyrpzGZnQKVirGaBCVRzrra(os.paTH.join(os.paTH.join(os.paTH.dirname(os.paTH.realpath(__file__)), "quasar_extras"), "nodes_upscale_model.py"))
    VVKZvVLFAmyrpzGZnQKVirGaBCVRzrra(os.paTH.join(os.paTH.join(os.paTH.dirname(os.paTH.realpath(__file__)), "quasar_extras"), "nodes_post_processing.py"))
    VVKZvVLFAmyrpzGZnQKVirGaBCVRzrra(os.paTH.join(os.paTH.join(os.paTH.dirname(os.paTH.realpath(__file__)), "quasar_extras"), "nodes_mask.py"))
    VVKZvVLFAmyrpzGZnQKVirGaBCVRzrra(os.paTH.join(os.paTH.join(os.paTH.dirname(os.paTH.realpath(__file__)), "quasar_extras"), "nodes_rebatch.py"))
    VVKZvVLFAmyrpzGZnQKVirGaBCVRzrra(os.paTH.join(os.paTH.join(os.paTH.dirname(os.paTH.realpath(__file__)), "quasar_extras"), "nodes_model_merging.py"))
    VVKZvVLFAmyrpzGZnQKVirGaBCVRzrra(os.paTH.join(os.paTH.join(os.paTH.dirname(os.paTH.realpath(__file__)), "quasar_extras"), "nodes_tomesd.py"))
    VVKZvVLFAmyrpzGZnQKVirGaBCVRzrra(os.paTH.join(os.paTH.join(os.paTH.dirname(os.paTH.realpath(__file__)), "quasar_extras"), "nodes_clip_sdxl.py"))
    VVKZvVLFAmyrpzGZnQKVirGaBCVRzrra(os.paTH.join(os.paTH.join(os.paTH.dirname(os.paTH.realpath(__file__)), "quasar_extras"), "nodes_canny.py"))
    dcfAcZtKluJqyIGNEuRjJvrqFDjMRAov()
