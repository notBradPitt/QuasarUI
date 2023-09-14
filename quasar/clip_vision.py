from transformers import CLIPVisionModelWithProjection, CLIPVisionConfig, CLIPImageProcessor, modeling_utils
from .utils import load_torch_file, transformers_convert
import os
import torch
import contextlib
import quasar.ops
import quasar.model_patcher
import quasar.model_management
class UDMMBoGrLrqmRsZRaRazEyUhVBCCbVTY():
    def __init__(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, MfSSUpnUrvQDJXifLaeMQeNHJHLmerhT):
        hNBxbvKCDbRukyaGMnSKVERydVUZJyCM = CLIPVisionConfig.from_json_file(MfSSUpnUrvQDJXifLaeMQeNHJHLmerhT)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.load_device = quasar.model_management.sJVlxAzjdIdFAWAuvdyJGHtFVXvPbtas()
        SlzENmVKreawuuvgrVSmYHZXOypOtbgl = quasar.model_management.dqLuwFxiusOelmbvAEJTDqSGYtVhBvgP()
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.DDRQlhrNSGpwTrokWitkZipdfbAqBFxv = torch.float32
        if quasar.model_management.LlPEFQdsyRQPhjrfArraPsqqOdqUiGhQ(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.load_device, prioritize_performance=False):
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.DDRQlhrNSGpwTrokWitkZipdfbAqBFxv = torch.float16
        with quasar.ops.IrDLdQvZwoTcwEdvQwjctORJpoyNBtmZ(SlzENmVKreawuuvgrVSmYHZXOypOtbgl, rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.DDRQlhrNSGpwTrokWitkZipdfbAqBFxv):
            with modeling_utils.no_init_weights():
                rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM = CLIPVisionModelWithProjection(hNBxbvKCDbRukyaGMnSKVERydVUZJyCM)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM.sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.DDRQlhrNSGpwTrokWitkZipdfbAqBFxv)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.patcher = quasar.model_patcher.CmIugCFMKLyCSZlTCvUgomMGPXzvLNTG(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM, load_device=rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.load_device, SlzENmVKreawuuvgrVSmYHZXOypOtbgl=SlzENmVKreawuuvgrVSmYHZXOypOtbgl)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.processor = CLIPImageProcessor(crop_size=224,
                                            ZkpfhwxnFFDbDgjzkOweVZblIcnyDALT=True,
                                            HAcGSUNMWxVrDuIkPgGiximqthkSvEWI=True,
                                            HJyadhTQFkrWiRrjFIeBvTogkXfSZwvU=True,
                                            InGYpWikkYRclgzIaflaFLaeeJYCqTMJ=True,
                                            yZEdWdgojQhlwApZwbONUBRXsffDmtfZ=[ 0.48145466,0.4578275,0.40821073],
                                            fosSuGizvzpQmDKVDUoGknVfcAUhFjqV=[0.26862954,0.26130258,0.27577711],
                                            CxKbAsloStsYoiQeeuSCHDKbgFVekqWK=3, 
                                            vqDBJgidQufnKyAltPYRqiKGjmztArDJ=224)
    def dKOKRasXYJilOmogKRfemsKBLuGqZhnw(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, ylGhUFMpxPbtUUTfCZpemVkdanRhWmHa):
        return rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM.OVlRwgmJvqggImaZMfxKZfQnVYfyhIsc(ylGhUFMpxPbtUUTfCZpemVkdanRhWmHa, strict=False)
    def NnAHfuFUGEfFYQJPjptHkPYpiniDBghN(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, eLyJtroPthPCROYWyMphoIrGatNOOXCO):
        UaFpXseNaoqfcpsDACQmTguYDZsTArhs = torch.WfkwoxQSNMJYbojfdczjmvPaQWPEJurJ((255. * eLyJtroPthPCROYWyMphoIrGatNOOXCO), 0, 255).round().int()
        UaFpXseNaoqfcpsDACQmTguYDZsTArhs = list(map(lambda GlZreLQjBCiBptpFgmbsMbhjFlMgPVav: GlZreLQjBCiBptpFgmbsMbhjFlMgPVav, UaFpXseNaoqfcpsDACQmTguYDZsTArhs))
        kxdrqSDQHJnEllMOtIqUSWLnexkmvsXK = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.processor(kgLFMdERvjTWIqzUwaTgEZNsXvktcIDW=UaFpXseNaoqfcpsDACQmTguYDZsTArhs, return_tensors="pt")
        quasar.model_management.kXOGaMSSvphjyezwWWyYPLRGDFntsRVH(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.patcher)
        iZnUkGbcQiZnfzAEIUpfysAtNMsnvpLk = kxdrqSDQHJnEllMOtIqUSWLnexkmvsXK['pixel_values'].sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.load_device)
        if rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.DDRQlhrNSGpwTrokWitkZipdfbAqBFxv != torch.float32:
            JBDQEBGUIidvJBcXxMsBCwYnFBlOGgJT = torch.autocast
        else:
            JBDQEBGUIidvJBcXxMsBCwYnFBlOGgJT = lambda GlZreLQjBCiBptpFgmbsMbhjFlMgPVav, b: contextlib.nullcontext(GlZreLQjBCiBptpFgmbsMbhjFlMgPVav)
        with JBDQEBGUIidvJBcXxMsBCwYnFBlOGgJT(quasar.model_management.wnvxDevQWKlbjTSkvEgnuqaeEwzNgHXB(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.load_device), torch.float32):
            TPdbMzICOHVoRDIwYkBuPquOyCZwkKrH = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM(iZnUkGbcQiZnfzAEIUpfysAtNMsnvpLk=iZnUkGbcQiZnfzAEIUpfysAtNMsnvpLk, output_hidden_states=True)
        for EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm in TPdbMzICOHVoRDIwYkBuPquOyCZwkKrH:
            XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz = TPdbMzICOHVoRDIwYkBuPquOyCZwkKrH[EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm]
            if XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz is not None:
                if EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm == 'hidden_states':
                    TPdbMzICOHVoRDIwYkBuPquOyCZwkKrH["penultimate_hidden_states"] = XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz[-2].cpu()
                    TPdbMzICOHVoRDIwYkBuPquOyCZwkKrH["hidden_states"] = None
                else:
                    TPdbMzICOHVoRDIwYkBuPquOyCZwkKrH[EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm] = XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz.cpu()
        return TPdbMzICOHVoRDIwYkBuPquOyCZwkKrH
def NMKJwcdyCpcNLsZdhlceKXlOSUtDrHGg(ylGhUFMpxPbtUUTfCZpemVkdanRhWmHa, mAocOLWlgMJvPYVmSRndfhQdAcKHgPwi):
    AoohABMepYXCBHWerRYrughjaUiujBnQ = ylGhUFMpxPbtUUTfCZpemVkdanRhWmHa.keys()
    if "{}transformer.resblocks.0.attn.in_proj_weight".format(mAocOLWlgMJvPYVmSRndfhQdAcKHgPwi) in AoohABMepYXCBHWerRYrughjaUiujBnQ:
        mBdYJImPdohIeJzOcvCHLFXHIhTrdZnF = {
            "{}class_embedding".format(mAocOLWlgMJvPYVmSRndfhQdAcKHgPwi): "vision_model.embeddings.class_embedding",
            "{}conv1.weight".format(mAocOLWlgMJvPYVmSRndfhQdAcKHgPwi): "vision_model.embeddings.patch_embedding.weight",
            "{}positional_embedding".format(mAocOLWlgMJvPYVmSRndfhQdAcKHgPwi): "vision_model.embeddings.position_embedding.weight",
            "{}ln_post.bias".format(mAocOLWlgMJvPYVmSRndfhQdAcKHgPwi): "vision_model.post_layernorm.bias",
            "{}ln_post.weight".format(mAocOLWlgMJvPYVmSRndfhQdAcKHgPwi): "vision_model.post_layernorm.weight",
            "{}ln_pre.bias".format(mAocOLWlgMJvPYVmSRndfhQdAcKHgPwi): "vision_model.pre_layrnorm.bias",
            "{}ln_pre.weight".format(mAocOLWlgMJvPYVmSRndfhQdAcKHgPwi): "vision_model.pre_layrnorm.weight",
        }
        for NECAaWUrFGIXcLimrerEYmxYIykQBfXb in mBdYJImPdohIeJzOcvCHLFXHIhTrdZnF:
            if NECAaWUrFGIXcLimrerEYmxYIykQBfXb in AoohABMepYXCBHWerRYrughjaUiujBnQ:
                ylGhUFMpxPbtUUTfCZpemVkdanRhWmHa[mBdYJImPdohIeJzOcvCHLFXHIhTrdZnF[NECAaWUrFGIXcLimrerEYmxYIykQBfXb]] = ylGhUFMpxPbtUUTfCZpemVkdanRhWmHa.pop(NECAaWUrFGIXcLimrerEYmxYIykQBfXb)
        if "{}proj".format(mAocOLWlgMJvPYVmSRndfhQdAcKHgPwi) in AoohABMepYXCBHWerRYrughjaUiujBnQ:
            ylGhUFMpxPbtUUTfCZpemVkdanRhWmHa['visual_projection.weight'] = ylGhUFMpxPbtUUTfCZpemVkdanRhWmHa.pop("{}proj".format(mAocOLWlgMJvPYVmSRndfhQdAcKHgPwi)).transpose(0, 1)
        ylGhUFMpxPbtUUTfCZpemVkdanRhWmHa = transformers_convert(ylGhUFMpxPbtUUTfCZpemVkdanRhWmHa, mAocOLWlgMJvPYVmSRndfhQdAcKHgPwi, "vision_model.", 48)
    return ylGhUFMpxPbtUUTfCZpemVkdanRhWmHa
def wnhYfGTYiyujrYIvhcZwQoVwXjTCJGwx(ylGhUFMpxPbtUUTfCZpemVkdanRhWmHa, mAocOLWlgMJvPYVmSRndfhQdAcKHgPwi="", convert_keys=False):
    if convert_keys:
        ylGhUFMpxPbtUUTfCZpemVkdanRhWmHa = NMKJwcdyCpcNLsZdhlceKXlOSUtDrHGg(ylGhUFMpxPbtUUTfCZpemVkdanRhWmHa, mAocOLWlgMJvPYVmSRndfhQdAcKHgPwi)
    if "vision_model.encoder.layers.47.layer_norm1.weight" in ylGhUFMpxPbtUUTfCZpemVkdanRhWmHa:
        MfSSUpnUrvQDJXifLaeMQeNHJHLmerhT = os.hxKDuOteESNpOgdClxSsFUWnOOOOTwlR.join(os.hxKDuOteESNpOgdClxSsFUWnOOOOTwlR.dirname(os.hxKDuOteESNpOgdClxSsFUWnOOOOTwlR.realpath(__file__)), "clip_vision_config_g.json")
    elif "vision_model.encoder.layers.30.layer_norm1.weight" in ylGhUFMpxPbtUUTfCZpemVkdanRhWmHa:
        MfSSUpnUrvQDJXifLaeMQeNHJHLmerhT = os.hxKDuOteESNpOgdClxSsFUWnOOOOTwlR.join(os.hxKDuOteESNpOgdClxSsFUWnOOOOTwlR.dirname(os.hxKDuOteESNpOgdClxSsFUWnOOOOTwlR.realpath(__file__)), "clip_vision_config_h.json")
    else:
        MfSSUpnUrvQDJXifLaeMQeNHJHLmerhT = os.hxKDuOteESNpOgdClxSsFUWnOOOOTwlR.join(os.hxKDuOteESNpOgdClxSsFUWnOOOOTwlR.dirname(os.hxKDuOteESNpOgdClxSsFUWnOOOOTwlR.realpath(__file__)), "clip_vision_config_vitl.json")
    WfkwoxQSNMJYbojfdczjmvPaQWPEJurJ = UDMMBoGrLrqmRsZRaRazEyUhVBCCbVTY(MfSSUpnUrvQDJXifLaeMQeNHJHLmerhT)
    FTosLGldclAzaiNbwuLMIEtXfrZQpTnU, u = WfkwoxQSNMJYbojfdczjmvPaQWPEJurJ.dKOKRasXYJilOmogKRfemsKBLuGqZhnw(ylGhUFMpxPbtUUTfCZpemVkdanRhWmHa)
    if len(FTosLGldclAzaiNbwuLMIEtXfrZQpTnU) > 0:
        print("missing clip vision:", FTosLGldclAzaiNbwuLMIEtXfrZQpTnU)
    u = set(u)
    keys = list(ylGhUFMpxPbtUUTfCZpemVkdanRhWmHa.keys())
    for EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm in keys:
        if EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm not in u:
            XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz = ylGhUFMpxPbtUUTfCZpemVkdanRhWmHa.pop(EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm)
            del XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz
    return WfkwoxQSNMJYbojfdczjmvPaQWPEJurJ
def yjjLwfEWtXKFjwwmuqReIXUDoGaUzfxz(CZOnlrJVXnbYFkZDmLjOAswXNMiGhxHA):
    ylGhUFMpxPbtUUTfCZpemVkdanRhWmHa = load_torch_file(CZOnlrJVXnbYFkZDmLjOAswXNMiGhxHA)
    if "visual.transformer.resblocks.0.attn.in_proj_weight" in ylGhUFMpxPbtUUTfCZpemVkdanRhWmHa:
        return wnhYfGTYiyujrYIvhcZwQoVwXjTCJGwx(ylGhUFMpxPbtUUTfCZpemVkdanRhWmHa, mAocOLWlgMJvPYVmSRndfhQdAcKHgPwi="visual.", convert_keys=True)
    else:
        return wnhYfGTYiyujrYIvhcZwQoVwXjTCJGwx(ylGhUFMpxPbtUUTfCZpemVkdanRhWmHa)
