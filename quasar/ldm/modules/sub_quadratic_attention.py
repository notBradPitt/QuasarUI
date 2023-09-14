from functools import partial
import torch
from torch import Tensor
from torch.utils.checkpoint import vcSlHLxBcVodHmZrzACHLEJuENMXjWTG
import math
try:
	from typing import Optional, NamedTuple, List, Protocol
except ImportError:
	from typing import Optional, NamedTuple, List
	from typing_extensions import Protocol
from torch import Tensor
from typing import List
from quasar import model_management
def TiHcmODrAnLUWoxXbBRMfICrBFykEeQF(
    NECAaWUrFGIXcLimrerEYmxYIykQBfXb: Tensor,
    starts: List[int],
    sizes: List[int],
) -> Tensor:
    bVNnXXxRyxdFjtzxpOOKKCeFJzAbDeBQ = [slice(tUuYqnLjDXuftYgMagGpmrobxWgfcbgq, tUuYqnLjDXuftYgMagGpmrobxWgfcbgq + vqDBJgidQufnKyAltPYRqiKGjmztArDJ) for tUuYqnLjDXuftYgMagGpmrobxWgfcbgq, vqDBJgidQufnKyAltPYRqiKGjmztArDJ in zip(starts, sizes)]
    return NECAaWUrFGIXcLimrerEYmxYIykQBfXb[bVNnXXxRyxdFjtzxpOOKKCeFJzAbDeBQ]
class OCjNCdccJxoGVVQletkjVWeVOAmWiNGI(NamedTuple):
    llCWWXfyFzdhsFPoiVuMbxabfQiPjBqJ: Tensor
    exp_weights_sum: Tensor
    hynkNXIyYWrIEMTVgXLlgOGgSAXJJtdO: Tensor
class vXHlvOcVyLrXJsIrRSHVyFHmnilSBZBN(Protocol):
    @staticmethod
    def __call__(
        oFxedobBnFbKeewIgTfUgblKziGvmndF: Tensor,
        uvCuKDkdVEPRdZyyLHLiivxCEmonrfgb: Tensor,
        GXNVXDlnsSLzkmussBPoJXgJwuXIiwsc: Tensor,
    ) -> OCjNCdccJxoGVVQletkjVWeVOAmWiNGI: ...
class ZZSahaaVoHHzyEljoaFzSSXrQvUNpitI(Protocol):
    @staticmethod
    def __call__(
        oFxedobBnFbKeewIgTfUgblKziGvmndF: Tensor,
        uvCuKDkdVEPRdZyyLHLiivxCEmonrfgb: Tensor,
        GXNVXDlnsSLzkmussBPoJXgJwuXIiwsc: Tensor,
    ) -> Tensor: ...
def CzVRoUlfNavdOPFUeHmfdhVbPgBdHYXd(
    oFxedobBnFbKeewIgTfUgblKziGvmndF: Tensor,
    uvCuKDkdVEPRdZyyLHLiivxCEmonrfgb: Tensor,
    GXNVXDlnsSLzkmussBPoJXgJwuXIiwsc: Tensor,
    xmbXivThLFnawFPAJvIDBztziWsaDyEE: float,
    ggPIURSGXIcuVBVgCWAEVPDrcubVXMiD: bool,
) -> OCjNCdccJxoGVVQletkjVWeVOAmWiNGI:
    if ggPIURSGXIcuVBVgCWAEVPDrcubVXMiD:
        with torch.autocast(ClvYjtcXylmicwCwVQPykJTWmcwImVEP=False, device_type = 'cuda'):
            oFxedobBnFbKeewIgTfUgblKziGvmndF = oFxedobBnFbKeewIgTfUgblKziGvmndF.float()
            uvCuKDkdVEPRdZyyLHLiivxCEmonrfgb = uvCuKDkdVEPRdZyyLHLiivxCEmonrfgb.float()
            TxLodEIQABQAbzQPKvJakcaMASqoXfNL = torch.baddbmm(
                torch.empty(1, 1, 1, fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc=oFxedobBnFbKeewIgTfUgblKziGvmndF.fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc, DDRQlhrNSGpwTrokWitkZipdfbAqBFxv=oFxedobBnFbKeewIgTfUgblKziGvmndF.DDRQlhrNSGpwTrokWitkZipdfbAqBFxv),
                oFxedobBnFbKeewIgTfUgblKziGvmndF,
                uvCuKDkdVEPRdZyyLHLiivxCEmonrfgb,
                uigKGapaQVcFiOjEiWwRAHjjkAWxsqck=xmbXivThLFnawFPAJvIDBztziWsaDyEE,
                PgoraROQSYILTGDWEfTGXrsnUljVRBUG=0,
            )
    else:
        TxLodEIQABQAbzQPKvJakcaMASqoXfNL = torch.baddbmm(
            torch.empty(1, 1, 1, fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc=oFxedobBnFbKeewIgTfUgblKziGvmndF.fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc, DDRQlhrNSGpwTrokWitkZipdfbAqBFxv=oFxedobBnFbKeewIgTfUgblKziGvmndF.DDRQlhrNSGpwTrokWitkZipdfbAqBFxv),
            oFxedobBnFbKeewIgTfUgblKziGvmndF,
            uvCuKDkdVEPRdZyyLHLiivxCEmonrfgb,
            uigKGapaQVcFiOjEiWwRAHjjkAWxsqck=xmbXivThLFnawFPAJvIDBztziWsaDyEE,
            PgoraROQSYILTGDWEfTGXrsnUljVRBUG=0,
        )
    hynkNXIyYWrIEMTVgXLlgOGgSAXJJtdO, _ = torch.max(TxLodEIQABQAbzQPKvJakcaMASqoXfNL, -1, keepdim=True)
    hynkNXIyYWrIEMTVgXLlgOGgSAXJJtdO = hynkNXIyYWrIEMTVgXLlgOGgSAXJJtdO.detach()
    torch.exp(TxLodEIQABQAbzQPKvJakcaMASqoXfNL - hynkNXIyYWrIEMTVgXLlgOGgSAXJJtdO, iqymPVpxyjOWChGwBkTemSzHJbnJdAIz=TxLodEIQABQAbzQPKvJakcaMASqoXfNL)
    IWuvGfhYjWlmwsIwTorSovVtKageuslb = TxLodEIQABQAbzQPKvJakcaMASqoXfNL.sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ(GXNVXDlnsSLzkmussBPoJXgJwuXIiwsc.DDRQlhrNSGpwTrokWitkZipdfbAqBFxv)
    llCWWXfyFzdhsFPoiVuMbxabfQiPjBqJ = torch.bmm(IWuvGfhYjWlmwsIwTorSovVtKageuslb, GXNVXDlnsSLzkmussBPoJXgJwuXIiwsc)
    hynkNXIyYWrIEMTVgXLlgOGgSAXJJtdO = hynkNXIyYWrIEMTVgXLlgOGgSAXJJtdO.squeeze(-1)
    return OCjNCdccJxoGVVQletkjVWeVOAmWiNGI(llCWWXfyFzdhsFPoiVuMbxabfQiPjBqJ, IWuvGfhYjWlmwsIwTorSovVtKageuslb.sum(yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk=-1), hynkNXIyYWrIEMTVgXLlgOGgSAXJJtdO)
def HwdJEpGDkZZHvKnQeXxCmtFGEjWnzZba(
    oFxedobBnFbKeewIgTfUgblKziGvmndF: Tensor,
    uvCuKDkdVEPRdZyyLHLiivxCEmonrfgb: Tensor,
    GXNVXDlnsSLzkmussBPoJXgJwuXIiwsc: Tensor,
    DfqImPnvPuITkZhtYaMhhbmbkKExcoTd: vXHlvOcVyLrXJsIrRSHVyFHmnilSBZBN,
    uDTBZQdxCndcOBROTvXuOsdAOWRULsLj: int,
) -> Tensor:
    OxxKceEwXIPmBcVPFFUdYjDLrGLsvryX, XPgUEzMMzNQKXGADEiNmdyCqBqrXhInh, xdRMOqMyVzbfhYwKMCvFapJiNdJvFZoS = uvCuKDkdVEPRdZyyLHLiivxCEmonrfgb.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg
    _, _, wZJXSDhgBpHWDhHnFjGzGxKtqEmwBxRG = GXNVXDlnsSLzkmussBPoJXgJwuXIiwsc.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg
    def mfdaKDVDJLNlmwtTMdZcnZMQCtUgPSeU(chunk_idx: int) -> OCjNCdccJxoGVVQletkjVWeVOAmWiNGI:
        lHMnaZnbRdzDtJChlOILqmjglOnCTImz = TiHcmODrAnLUWoxXbBRMfICrBFykEeQF(
            uvCuKDkdVEPRdZyyLHLiivxCEmonrfgb,
            (0, 0, chunk_idx),
            (OxxKceEwXIPmBcVPFFUdYjDLrGLsvryX, XPgUEzMMzNQKXGADEiNmdyCqBqrXhInh, uDTBZQdxCndcOBROTvXuOsdAOWRULsLj)
        )
        zLVchVlVFYsxAyDlXkuZMZcTjYYpTmQZ = TiHcmODrAnLUWoxXbBRMfICrBFykEeQF(
            GXNVXDlnsSLzkmussBPoJXgJwuXIiwsc,
            (0, chunk_idx, 0),
            (OxxKceEwXIPmBcVPFFUdYjDLrGLsvryX, uDTBZQdxCndcOBROTvXuOsdAOWRULsLj, wZJXSDhgBpHWDhHnFjGzGxKtqEmwBxRG)
        )
        return DfqImPnvPuITkZhtYaMhhbmbkKExcoTd(oFxedobBnFbKeewIgTfUgblKziGvmndF, lHMnaZnbRdzDtJChlOILqmjglOnCTImz, zLVchVlVFYsxAyDlXkuZMZcTjYYpTmQZ)
    chunks: List[OCjNCdccJxoGVVQletkjVWeVOAmWiNGI] = [
        mfdaKDVDJLNlmwtTMdZcnZMQCtUgPSeU(ebMwMGDmpDsmyMtCQfGxUhZuVHvTpavF) for ebMwMGDmpDsmyMtCQfGxUhZuVHvTpavF in torch.arange(0, xdRMOqMyVzbfhYwKMCvFapJiNdJvFZoS, uDTBZQdxCndcOBROTvXuOsdAOWRULsLj)
    ]
    wMxpzmMLeeCmmhtjFYRCsFDjcxydFjyj = OCjNCdccJxoGVVQletkjVWeVOAmWiNGI(*map(torch.stack, zip(*chunks)))
    RcuozIygluqxEVHrlZjNZJiSbmiaelkJ, hvNWZoyFrMibivOvlpCFDhHUrFFShxOh, ZVqRnBRuTrpSKaqOcPtyocwViXPGhUBp = wMxpzmMLeeCmmhtjFYRCsFDjcxydFjyj
    kLigoebCEiOpqFIRqYVtJZsCusmvYldr, _ = torch.max(ZVqRnBRuTrpSKaqOcPtyocwViXPGhUBp, 0, keepdim=True)
    kDWkyVbCcnndDpbjdsAfiGPEUFansNHD = torch.exp(ZVqRnBRuTrpSKaqOcPtyocwViXPGhUBp - kLigoebCEiOpqFIRqYVtJZsCusmvYldr)
    RcuozIygluqxEVHrlZjNZJiSbmiaelkJ *= torch.unsqueeze(kDWkyVbCcnndDpbjdsAfiGPEUFansNHD, -1)
    hvNWZoyFrMibivOvlpCFDhHUrFFShxOh *= kDWkyVbCcnndDpbjdsAfiGPEUFansNHD
    HmoBUyanWGyWwuJfkuZztuxMTpBelGoN = RcuozIygluqxEVHrlZjNZJiSbmiaelkJ.sum(yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk=0)
    MAHdyiitDHiDItecDXdqpEZGPvrVrgxJ = torch.unsqueeze(hvNWZoyFrMibivOvlpCFDhHUrFFShxOh, -1).sum(yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk=0)
    return HmoBUyanWGyWwuJfkuZztuxMTpBelGoN / MAHdyiitDHiDItecDXdqpEZGPvrVrgxJ
def haaTGDaPlcJTmeEjXbMGXFcMXgpzvrqG(
    oFxedobBnFbKeewIgTfUgblKziGvmndF: Tensor,
    uvCuKDkdVEPRdZyyLHLiivxCEmonrfgb: Tensor,
    GXNVXDlnsSLzkmussBPoJXgJwuXIiwsc: Tensor,
    xmbXivThLFnawFPAJvIDBztziWsaDyEE: float,
    ggPIURSGXIcuVBVgCWAEVPDrcubVXMiD: bool,
) -> Tensor:
    if ggPIURSGXIcuVBVgCWAEVPDrcubVXMiD:
        with torch.autocast(ClvYjtcXylmicwCwVQPykJTWmcwImVEP=False, device_type = 'cuda'):
            oFxedobBnFbKeewIgTfUgblKziGvmndF = oFxedobBnFbKeewIgTfUgblKziGvmndF.float()
            uvCuKDkdVEPRdZyyLHLiivxCEmonrfgb = uvCuKDkdVEPRdZyyLHLiivxCEmonrfgb.float()
            ZmGhrzmiPSUkYMFtekYbKQbUZGYYMtfK = torch.baddbmm(
                torch.empty(1, 1, 1, fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc=oFxedobBnFbKeewIgTfUgblKziGvmndF.fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc, DDRQlhrNSGpwTrokWitkZipdfbAqBFxv=oFxedobBnFbKeewIgTfUgblKziGvmndF.DDRQlhrNSGpwTrokWitkZipdfbAqBFxv),
                oFxedobBnFbKeewIgTfUgblKziGvmndF,
                uvCuKDkdVEPRdZyyLHLiivxCEmonrfgb,
                uigKGapaQVcFiOjEiWwRAHjjkAWxsqck=xmbXivThLFnawFPAJvIDBztziWsaDyEE,
                PgoraROQSYILTGDWEfTGXrsnUljVRBUG=0,
            )
    else:
        ZmGhrzmiPSUkYMFtekYbKQbUZGYYMtfK = torch.baddbmm(
            torch.empty(1, 1, 1, fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc=oFxedobBnFbKeewIgTfUgblKziGvmndF.fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc, DDRQlhrNSGpwTrokWitkZipdfbAqBFxv=oFxedobBnFbKeewIgTfUgblKziGvmndF.DDRQlhrNSGpwTrokWitkZipdfbAqBFxv),
            oFxedobBnFbKeewIgTfUgblKziGvmndF,
            uvCuKDkdVEPRdZyyLHLiivxCEmonrfgb,
            uigKGapaQVcFiOjEiWwRAHjjkAWxsqck=xmbXivThLFnawFPAJvIDBztziWsaDyEE,
            PgoraROQSYILTGDWEfTGXrsnUljVRBUG=0,
        )
    try:
        oFsPYpKMfaHxlKmMhBoqaRdUoaAophfm = ZmGhrzmiPSUkYMFtekYbKQbUZGYYMtfK.softmax(yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk=-1)
        del ZmGhrzmiPSUkYMFtekYbKQbUZGYYMtfK
    except model_management.uiFxRFoacIkrFnuAQlLvqBYROTajCRaW:
        print("ran out of memory while running softmax in  _get_attention_scores_no_kv_chunking, trying slower in place softmax instead")
        ZmGhrzmiPSUkYMFtekYbKQbUZGYYMtfK -= ZmGhrzmiPSUkYMFtekYbKQbUZGYYMtfK.max(yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk=-1, keepdim=True).values
        torch.exp(ZmGhrzmiPSUkYMFtekYbKQbUZGYYMtfK, iqymPVpxyjOWChGwBkTemSzHJbnJdAIz=ZmGhrzmiPSUkYMFtekYbKQbUZGYYMtfK)
        RLxBEliiAqUpJZocUuRvUtjTmqegSfXE = torch.sum(ZmGhrzmiPSUkYMFtekYbKQbUZGYYMtfK, yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk=-1, keepdim=True)
        ZmGhrzmiPSUkYMFtekYbKQbUZGYYMtfK /= RLxBEliiAqUpJZocUuRvUtjTmqegSfXE
        oFsPYpKMfaHxlKmMhBoqaRdUoaAophfm = ZmGhrzmiPSUkYMFtekYbKQbUZGYYMtfK
    QrMXbOCKlTzOHaYbWtZFQhtyCshZXiuU = torch.bmm(oFsPYpKMfaHxlKmMhBoqaRdUoaAophfm.sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ(GXNVXDlnsSLzkmussBPoJXgJwuXIiwsc.DDRQlhrNSGpwTrokWitkZipdfbAqBFxv), GXNVXDlnsSLzkmussBPoJXgJwuXIiwsc)
    return QrMXbOCKlTzOHaYbWtZFQhtyCshZXiuU
class vcKmAfdmwJlFfRDjMqmCdwSkqMQcNJof(NamedTuple):
    chunk_idx: int
    attn_chunk: OCjNCdccJxoGVVQletkjVWeVOAmWiNGI
def wWGvJoqsrPWDPWsQTifuSjfltmBzpUdK(
    oFxedobBnFbKeewIgTfUgblKziGvmndF: Tensor,
    uvCuKDkdVEPRdZyyLHLiivxCEmonrfgb: Tensor,
    GXNVXDlnsSLzkmussBPoJXgJwuXIiwsc: Tensor,
    sRpdDMYTVMeNesUzSLRWIgcClptmNebH=1024,
    uDTBZQdxCndcOBROTvXuOsdAOWRULsLj: Optional[int] = None,
    XAMYbWMRzvpvukEerBoKgjYJduCqwDOF: Optional[int] = None,
    TkHgGRFhDYRqyKuFvQRlKbpOBXUaEDVU=True,
    ggPIURSGXIcuVBVgCWAEVPDrcubVXMiD=False,
):
    OxxKceEwXIPmBcVPFFUdYjDLrGLsvryX, eCRSPzKosCQhJWveukAUVqFsWrMfGOHN, nDBSapJYAEMLCwYQBBZXaXnAAjzvleqS = oFxedobBnFbKeewIgTfUgblKziGvmndF.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg
    _, _, xdRMOqMyVzbfhYwKMCvFapJiNdJvFZoS = uvCuKDkdVEPRdZyyLHLiivxCEmonrfgb.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg
    xmbXivThLFnawFPAJvIDBztziWsaDyEE = nDBSapJYAEMLCwYQBBZXaXnAAjzvleqS ** -0.5
    uDTBZQdxCndcOBROTvXuOsdAOWRULsLj = min(uDTBZQdxCndcOBROTvXuOsdAOWRULsLj or int(math.sqrt(xdRMOqMyVzbfhYwKMCvFapJiNdJvFZoS)), xdRMOqMyVzbfhYwKMCvFapJiNdJvFZoS)
    if XAMYbWMRzvpvukEerBoKgjYJduCqwDOF is not None:
        uDTBZQdxCndcOBROTvXuOsdAOWRULsLj = max(uDTBZQdxCndcOBROTvXuOsdAOWRULsLj, XAMYbWMRzvpvukEerBoKgjYJduCqwDOF)
    def RSiZFukXzGgjaBqMGJBfQKCWhumsGnnc(chunk_idx: int) -> Tensor:
        return TiHcmODrAnLUWoxXbBRMfICrBFykEeQF(
            oFxedobBnFbKeewIgTfUgblKziGvmndF,
            (0, chunk_idx, 0),
            (OxxKceEwXIPmBcVPFFUdYjDLrGLsvryX, min(sRpdDMYTVMeNesUzSLRWIgcClptmNebH, eCRSPzKosCQhJWveukAUVqFsWrMfGOHN), nDBSapJYAEMLCwYQBBZXaXnAAjzvleqS)
        )
    DfqImPnvPuITkZhtYaMhhbmbkKExcoTd: vXHlvOcVyLrXJsIrRSHVyFHmnilSBZBN = partial(CzVRoUlfNavdOPFUeHmfdhVbPgBdHYXd, xmbXivThLFnawFPAJvIDBztziWsaDyEE=xmbXivThLFnawFPAJvIDBztziWsaDyEE, ggPIURSGXIcuVBVgCWAEVPDrcubVXMiD=ggPIURSGXIcuVBVgCWAEVPDrcubVXMiD)
    DfqImPnvPuITkZhtYaMhhbmbkKExcoTd: vXHlvOcVyLrXJsIrRSHVyFHmnilSBZBN = partial(vcSlHLxBcVodHmZrzACHLEJuENMXjWTG, DfqImPnvPuITkZhtYaMhhbmbkKExcoTd) if TkHgGRFhDYRqyKuFvQRlKbpOBXUaEDVU else DfqImPnvPuITkZhtYaMhhbmbkKExcoTd
    compute_query_chunk_attn: ZZSahaaVoHHzyEljoaFzSSXrQvUNpitI = partial(
        haaTGDaPlcJTmeEjXbMGXFcMXgpzvrqG,
        xmbXivThLFnawFPAJvIDBztziWsaDyEE=xmbXivThLFnawFPAJvIDBztziWsaDyEE,
        ggPIURSGXIcuVBVgCWAEVPDrcubVXMiD=ggPIURSGXIcuVBVgCWAEVPDrcubVXMiD
    ) if xdRMOqMyVzbfhYwKMCvFapJiNdJvFZoS <= uDTBZQdxCndcOBROTvXuOsdAOWRULsLj else (
        partial(
            HwdJEpGDkZZHvKnQeXxCmtFGEjWnzZba,
            uDTBZQdxCndcOBROTvXuOsdAOWRULsLj=uDTBZQdxCndcOBROTvXuOsdAOWRULsLj,
            DfqImPnvPuITkZhtYaMhhbmbkKExcoTd=DfqImPnvPuITkZhtYaMhhbmbkKExcoTd,
        )
    )
    if eCRSPzKosCQhJWveukAUVqFsWrMfGOHN <= sRpdDMYTVMeNesUzSLRWIgcClptmNebH:
        return compute_query_chunk_attn(
            oFxedobBnFbKeewIgTfUgblKziGvmndF=oFxedobBnFbKeewIgTfUgblKziGvmndF,
            uvCuKDkdVEPRdZyyLHLiivxCEmonrfgb=uvCuKDkdVEPRdZyyLHLiivxCEmonrfgb,
            GXNVXDlnsSLzkmussBPoJXgJwuXIiwsc=GXNVXDlnsSLzkmussBPoJXgJwuXIiwsc,
        )
    mkGrvZQFRhRjbYdNQFvVwEiuLdtvTywf = torch.cat([
        compute_query_chunk_attn(
            oFxedobBnFbKeewIgTfUgblKziGvmndF=RSiZFukXzGgjaBqMGJBfQKCWhumsGnnc(HCXmerBqIMuTscBONzTGKYapYSxWTYHo * sRpdDMYTVMeNesUzSLRWIgcClptmNebH),
            uvCuKDkdVEPRdZyyLHLiivxCEmonrfgb=uvCuKDkdVEPRdZyyLHLiivxCEmonrfgb,
            GXNVXDlnsSLzkmussBPoJXgJwuXIiwsc=GXNVXDlnsSLzkmussBPoJXgJwuXIiwsc,
        ) for HCXmerBqIMuTscBONzTGKYapYSxWTYHo in range(math.ceil(eCRSPzKosCQhJWveukAUVqFsWrMfGOHN / sRpdDMYTVMeNesUzSLRWIgcClptmNebH))
    ], yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk=1)
    return mkGrvZQFRhRjbYdNQFvVwEiuLdtvTywf
