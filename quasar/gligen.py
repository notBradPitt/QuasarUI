import torch
from torch import nn, einsum
from .ldm.modules.attention import qQrohQXiAITQznFuShydRodggjOWexBZ
from inspect import isfunction
def exists(iQelECAceWgpMwNVKVNfqYXiZvxEyNPn):
    return iQelECAceWgpMwNVKVNfqYXiZvxEyNPn is not None
def mbvxGTzHRegamxLbMgjoxyrZBBDzHvEV(arr):
    return{qRswSnOBtvyzjhnKgbIzXEJZeYxpAFNw: True for qRswSnOBtvyzjhnKgbIzXEJZeYxpAFNw in arr}.keys()
def default(iQelECAceWgpMwNVKVNfqYXiZvxEyNPn, TXGwYXNLgQsYzfHHpRBDJGFCFZEClzIo):
    if exists(iQelECAceWgpMwNVKVNfqYXiZvxEyNPn):
        return iQelECAceWgpMwNVKVNfqYXiZvxEyNPn
    return TXGwYXNLgQsYzfHHpRBDJGFCFZEClzIo() if isfunction(TXGwYXNLgQsYzfHHpRBDJGFCFZEClzIo) else TXGwYXNLgQsYzfHHpRBDJGFCFZEClzIo
class arWeRcSKaVoQCynVIqZcAcRgBnhxHCvR(nn.Module):
    def __init__(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, dim_in, tgbtPhzliVInSVGKVTqssTxzfwkNlUPr):
        super().__init__()
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.proj = nn.DhMcMyEvvzmWIEJojbQeGHlzfZKiPzHO(dim_in, tgbtPhzliVInSVGKVTqssTxzfwkNlUPr * 2)
    def lqBgIcSWZYylbCPjXksJWDguuSOqoPCJ(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, NECAaWUrFGIXcLimrerEYmxYIykQBfXb):
        NECAaWUrFGIXcLimrerEYmxYIykQBfXb, wnJEgZdCPmnnmkKlktStjfXXkbZbbqLH = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.proj(NECAaWUrFGIXcLimrerEYmxYIykQBfXb).ebMwMGDmpDsmyMtCQfGxUhZuVHvTpavF(2, yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk=-1)
        return NECAaWUrFGIXcLimrerEYmxYIykQBfXb * torch.nn.functional.gelu(wnJEgZdCPmnnmkKlktStjfXXkbZbbqLH)
class nVIpLCPoeZxavETSbXIKgqMNJkfGLLVs(nn.Module):
    def __init__(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk, tgbtPhzliVInSVGKVTqssTxzfwkNlUPr=None, XVFRnfSDhyHpjboFTGKCmAMvovOXxqYP=4, glu=False, kcIxGCXrUvsLPSfmGoULGFzAthVmTXcA=0.):
        super().__init__()
        mnMnCdMaVdGNkPTuQLMKyEjwOMhAgIMR = int(yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk * XVFRnfSDhyHpjboFTGKCmAMvovOXxqYP)
        tgbtPhzliVInSVGKVTqssTxzfwkNlUPr = default(tgbtPhzliVInSVGKVTqssTxzfwkNlUPr, yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk)
        sXmfwvmjHIkRpPcXiyglCLqfExhzEyXD = nn.Sequential(
            nn.DhMcMyEvvzmWIEJojbQeGHlzfZKiPzHO(yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk, mnMnCdMaVdGNkPTuQLMKyEjwOMhAgIMR),
            nn.GELU()
        ) if not glu else arWeRcSKaVoQCynVIqZcAcRgBnhxHCvR(yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk, mnMnCdMaVdGNkPTuQLMKyEjwOMhAgIMR)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.faINqTMSsQxdMDXBAGUozMnWtvraUbzj = nn.Sequential(
            sXmfwvmjHIkRpPcXiyglCLqfExhzEyXD,
            nn.Dropout(kcIxGCXrUvsLPSfmGoULGFzAthVmTXcA),
            nn.DhMcMyEvvzmWIEJojbQeGHlzfZKiPzHO(mnMnCdMaVdGNkPTuQLMKyEjwOMhAgIMR, tgbtPhzliVInSVGKVTqssTxzfwkNlUPr)
        )
    def lqBgIcSWZYylbCPjXksJWDguuSOqoPCJ(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, NECAaWUrFGIXcLimrerEYmxYIykQBfXb):
        return rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.faINqTMSsQxdMDXBAGUozMnWtvraUbzj(NECAaWUrFGIXcLimrerEYmxYIykQBfXb)
class IPefarnhUxmGTVSYuYJPndOpvjACjrzk(nn.Module):
    def __init__(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, ZqiCYiNfDUNCIdHmASCiuNWYfvyqQifY, FEAAZHeTRQEJCsYHCOEPpfOenpVZIhNT, QJCnIiVfahCOVrhUgUzEjPLvCsBDwnir, SiOpzQSDRgWVXXhLenDXhMYFnSfQmjiy):
        super().__init__()
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.tUmudCfKVwpeKVqJPkVQAwLriIrTDLbW = qQrohQXiAITQznFuShydRodggjOWexBZ(
            ZqiCYiNfDUNCIdHmASCiuNWYfvyqQifY=ZqiCYiNfDUNCIdHmASCiuNWYfvyqQifY,
            FEAAZHeTRQEJCsYHCOEPpfOenpVZIhNT=FEAAZHeTRQEJCsYHCOEPpfOenpVZIhNT,
            QEnKImSSxUuBDHahcSgvZCYYpzjKVrVk=QJCnIiVfahCOVrhUgUzEjPLvCsBDwnir,
            QiYWcbRqbdDfAfhjULhYwmIlOStjgPlv=SiOpzQSDRgWVXXhLenDXhMYFnSfQmjiy)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.ff = nVIpLCPoeZxavETSbXIKgqMNJkfGLLVs(ZqiCYiNfDUNCIdHmASCiuNWYfvyqQifY, glu=True)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.norm1 = nn.SeaDiaiECtgJbgiExWzpSnrizTosOUam(ZqiCYiNfDUNCIdHmASCiuNWYfvyqQifY)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.norm2 = nn.SeaDiaiECtgJbgiExWzpSnrizTosOUam(ZqiCYiNfDUNCIdHmASCiuNWYfvyqQifY)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.register_parameter('alpha_attn', nn.Parameter(torch.xPmCFphFKpGMpIsczaSKHmMgRPZzJwla(0.)))
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.register_parameter('alpha_dense', nn.Parameter(torch.xPmCFphFKpGMpIsczaSKHmMgRPZzJwla(0.)))
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.xmbXivThLFnawFPAJvIDBztziWsaDyEE = 1
    def lqBgIcSWZYylbCPjXksJWDguuSOqoPCJ(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, NECAaWUrFGIXcLimrerEYmxYIykQBfXb, GbeDcLyKATsStDYQhKCKXmNoYGzFwvQi):
        NECAaWUrFGIXcLimrerEYmxYIykQBfXb = NECAaWUrFGIXcLimrerEYmxYIykQBfXb + rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.xmbXivThLFnawFPAJvIDBztziWsaDyEE * \
            torch.tanh(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.alpha_attn) * rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.tUmudCfKVwpeKVqJPkVQAwLriIrTDLbW(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.norm1(NECAaWUrFGIXcLimrerEYmxYIykQBfXb), GbeDcLyKATsStDYQhKCKXmNoYGzFwvQi, GbeDcLyKATsStDYQhKCKXmNoYGzFwvQi)
        NECAaWUrFGIXcLimrerEYmxYIykQBfXb = NECAaWUrFGIXcLimrerEYmxYIykQBfXb + rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.xmbXivThLFnawFPAJvIDBztziWsaDyEE * \
            torch.tanh(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.alpha_dense) * rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.ff(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.norm2(NECAaWUrFGIXcLimrerEYmxYIykQBfXb))
        return NECAaWUrFGIXcLimrerEYmxYIykQBfXb
class IGYPavhLjYtCTqdiWrZVTtEUKsfKknrF(nn.Module):
    def __init__(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, ZqiCYiNfDUNCIdHmASCiuNWYfvyqQifY, FEAAZHeTRQEJCsYHCOEPpfOenpVZIhNT, QJCnIiVfahCOVrhUgUzEjPLvCsBDwnir, SiOpzQSDRgWVXXhLenDXhMYFnSfQmjiy):
        super().__init__()
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.BJkSsAwbTZLfucgvGkDLcVEiRIlYJCmK = nn.DhMcMyEvvzmWIEJojbQeGHlzfZKiPzHO(FEAAZHeTRQEJCsYHCOEPpfOenpVZIhNT, ZqiCYiNfDUNCIdHmASCiuNWYfvyqQifY)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.tUmudCfKVwpeKVqJPkVQAwLriIrTDLbW = qQrohQXiAITQznFuShydRodggjOWexBZ(
            ZqiCYiNfDUNCIdHmASCiuNWYfvyqQifY=ZqiCYiNfDUNCIdHmASCiuNWYfvyqQifY,
            FEAAZHeTRQEJCsYHCOEPpfOenpVZIhNT=ZqiCYiNfDUNCIdHmASCiuNWYfvyqQifY,
            QEnKImSSxUuBDHahcSgvZCYYpzjKVrVk=QJCnIiVfahCOVrhUgUzEjPLvCsBDwnir,
            QiYWcbRqbdDfAfhjULhYwmIlOStjgPlv=SiOpzQSDRgWVXXhLenDXhMYFnSfQmjiy)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.ff = nVIpLCPoeZxavETSbXIKgqMNJkfGLLVs(ZqiCYiNfDUNCIdHmASCiuNWYfvyqQifY, glu=True)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.norm1 = nn.SeaDiaiECtgJbgiExWzpSnrizTosOUam(ZqiCYiNfDUNCIdHmASCiuNWYfvyqQifY)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.norm2 = nn.SeaDiaiECtgJbgiExWzpSnrizTosOUam(ZqiCYiNfDUNCIdHmASCiuNWYfvyqQifY)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.register_parameter('alpha_attn', nn.Parameter(torch.xPmCFphFKpGMpIsczaSKHmMgRPZzJwla(0.)))
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.register_parameter('alpha_dense', nn.Parameter(torch.xPmCFphFKpGMpIsczaSKHmMgRPZzJwla(0.)))
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.xmbXivThLFnawFPAJvIDBztziWsaDyEE = 1
    def lqBgIcSWZYylbCPjXksJWDguuSOqoPCJ(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, NECAaWUrFGIXcLimrerEYmxYIykQBfXb, GbeDcLyKATsStDYQhKCKXmNoYGzFwvQi):
        etfoZTOQArObRWzcpiWrWJyWulehZpaq = NECAaWUrFGIXcLimrerEYmxYIykQBfXb.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[1]
        GbeDcLyKATsStDYQhKCKXmNoYGzFwvQi = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.BJkSsAwbTZLfucgvGkDLcVEiRIlYJCmK(GbeDcLyKATsStDYQhKCKXmNoYGzFwvQi)
        NECAaWUrFGIXcLimrerEYmxYIykQBfXb = NECAaWUrFGIXcLimrerEYmxYIykQBfXb + rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.xmbXivThLFnawFPAJvIDBztziWsaDyEE * torch.tanh(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.alpha_attn) * rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.tUmudCfKVwpeKVqJPkVQAwLriIrTDLbW(
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.norm1(torch.cat([NECAaWUrFGIXcLimrerEYmxYIykQBfXb, GbeDcLyKATsStDYQhKCKXmNoYGzFwvQi], yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk=1)))[:, 0:etfoZTOQArObRWzcpiWrWJyWulehZpaq, :]
        NECAaWUrFGIXcLimrerEYmxYIykQBfXb = NECAaWUrFGIXcLimrerEYmxYIykQBfXb + rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.xmbXivThLFnawFPAJvIDBztziWsaDyEE * \
            torch.tanh(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.alpha_dense) * rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.ff(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.norm2(NECAaWUrFGIXcLimrerEYmxYIykQBfXb))
        return NECAaWUrFGIXcLimrerEYmxYIykQBfXb
class UvLdgyASpDFTzhXKvQYiMzdmZvrqyIDp(nn.Module):
    def __init__(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, ZqiCYiNfDUNCIdHmASCiuNWYfvyqQifY, FEAAZHeTRQEJCsYHCOEPpfOenpVZIhNT, QJCnIiVfahCOVrhUgUzEjPLvCsBDwnir, SiOpzQSDRgWVXXhLenDXhMYFnSfQmjiy):
        super().__init__()
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.BJkSsAwbTZLfucgvGkDLcVEiRIlYJCmK = nn.DhMcMyEvvzmWIEJojbQeGHlzfZKiPzHO(FEAAZHeTRQEJCsYHCOEPpfOenpVZIhNT, ZqiCYiNfDUNCIdHmASCiuNWYfvyqQifY)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.tUmudCfKVwpeKVqJPkVQAwLriIrTDLbW = qQrohQXiAITQznFuShydRodggjOWexBZ(
            ZqiCYiNfDUNCIdHmASCiuNWYfvyqQifY=ZqiCYiNfDUNCIdHmASCiuNWYfvyqQifY, FEAAZHeTRQEJCsYHCOEPpfOenpVZIhNT=ZqiCYiNfDUNCIdHmASCiuNWYfvyqQifY, QiYWcbRqbdDfAfhjULhYwmIlOStjgPlv=SiOpzQSDRgWVXXhLenDXhMYFnSfQmjiy)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.ff = nVIpLCPoeZxavETSbXIKgqMNJkfGLLVs(ZqiCYiNfDUNCIdHmASCiuNWYfvyqQifY, glu=True)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.norm1 = nn.SeaDiaiECtgJbgiExWzpSnrizTosOUam(ZqiCYiNfDUNCIdHmASCiuNWYfvyqQifY)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.norm2 = nn.SeaDiaiECtgJbgiExWzpSnrizTosOUam(ZqiCYiNfDUNCIdHmASCiuNWYfvyqQifY)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.register_parameter('alpha_attn', nn.Parameter(torch.xPmCFphFKpGMpIsczaSKHmMgRPZzJwla(0.)))
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.register_parameter('alpha_dense', nn.Parameter(torch.xPmCFphFKpGMpIsczaSKHmMgRPZzJwla(0.)))
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.xmbXivThLFnawFPAJvIDBztziWsaDyEE = 1
    def lqBgIcSWZYylbCPjXksJWDguuSOqoPCJ(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, NECAaWUrFGIXcLimrerEYmxYIykQBfXb, GbeDcLyKATsStDYQhKCKXmNoYGzFwvQi):
        oKoLNmqMHsUubaMUUnyDFEgClwoExDJu, etfoZTOQArObRWzcpiWrWJyWulehZpaq, _ = NECAaWUrFGIXcLimrerEYmxYIykQBfXb.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg
        oKoLNmqMHsUubaMUUnyDFEgClwoExDJu, waaaZWuemlDkkJyCSaHnUTMbsllFcFnJ, _ = GbeDcLyKATsStDYQhKCKXmNoYGzFwvQi.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg
        GbeDcLyKATsStDYQhKCKXmNoYGzFwvQi = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.BJkSsAwbTZLfucgvGkDLcVEiRIlYJCmK(GbeDcLyKATsStDYQhKCKXmNoYGzFwvQi)
        GAylgQoQFIOXkxYMsGiwdkUCKEjTUWmH = math.sqrt(etfoZTOQArObRWzcpiWrWJyWulehZpaq)
        rJVVvVpAgzELjhhvbYjwKCQqycPvqHIQ = math.sqrt(waaaZWuemlDkkJyCSaHnUTMbsllFcFnJ)
        assert int(GAylgQoQFIOXkxYMsGiwdkUCKEjTUWmH) == GAylgQoQFIOXkxYMsGiwdkUCKEjTUWmH, "Visual tokens must be square rootable"
        assert int(rJVVvVpAgzELjhhvbYjwKCQqycPvqHIQ) == rJVVvVpAgzELjhhvbYjwKCQqycPvqHIQ, "Grounding tokens must be square rootable"
        GAylgQoQFIOXkxYMsGiwdkUCKEjTUWmH = int(GAylgQoQFIOXkxYMsGiwdkUCKEjTUWmH)
        rJVVvVpAgzELjhhvbYjwKCQqycPvqHIQ = int(rJVVvVpAgzELjhhvbYjwKCQqycPvqHIQ)
        iqymPVpxyjOWChGwBkTemSzHJbnJdAIz = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.tUmudCfKVwpeKVqJPkVQAwLriIrTDLbW(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.norm1(torch.cat([NECAaWUrFGIXcLimrerEYmxYIykQBfXb, GbeDcLyKATsStDYQhKCKXmNoYGzFwvQi], yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk=1)))[
            :, etfoZTOQArObRWzcpiWrWJyWulehZpaq:, :]
        iqymPVpxyjOWChGwBkTemSzHJbnJdAIz = iqymPVpxyjOWChGwBkTemSzHJbnJdAIz.permute(0, 2, 1).reshape(oKoLNmqMHsUubaMUUnyDFEgClwoExDJu, -1, rJVVvVpAgzELjhhvbYjwKCQqycPvqHIQ, rJVVvVpAgzELjhhvbYjwKCQqycPvqHIQ)
        iqymPVpxyjOWChGwBkTemSzHJbnJdAIz = torch.nn.functional.interpolate(
            iqymPVpxyjOWChGwBkTemSzHJbnJdAIz, (GAylgQoQFIOXkxYMsGiwdkUCKEjTUWmH, GAylgQoQFIOXkxYMsGiwdkUCKEjTUWmH), bPTwwoDdWiuYqhtrDEHoDbHGiYcwcsQC='bicubic')
        RJgGCfauvfBVooxMlJcnrJywZAxzDscI = iqymPVpxyjOWChGwBkTemSzHJbnJdAIz.reshape(oKoLNmqMHsUubaMUUnyDFEgClwoExDJu, -1, etfoZTOQArObRWzcpiWrWJyWulehZpaq).permute(0, 2, 1)
        NECAaWUrFGIXcLimrerEYmxYIykQBfXb = NECAaWUrFGIXcLimrerEYmxYIykQBfXb + rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.xmbXivThLFnawFPAJvIDBztziWsaDyEE * torch.tanh(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.alpha_attn) * RJgGCfauvfBVooxMlJcnrJywZAxzDscI
        NECAaWUrFGIXcLimrerEYmxYIykQBfXb = NECAaWUrFGIXcLimrerEYmxYIykQBfXb + rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.xmbXivThLFnawFPAJvIDBztziWsaDyEE * \
            torch.tanh(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.alpha_dense) * rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.ff(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.norm2(NECAaWUrFGIXcLimrerEYmxYIykQBfXb))
        return NECAaWUrFGIXcLimrerEYmxYIykQBfXb
class zmsTvWBzKMkuQrgypDRwgwSKjMthTVgg():
    def __init__(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, num_freqs=64, bPjNAKUJbfwLGNTyXOwhREwhMbkCGtZT=100):
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.num_freqs = num_freqs
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.bPjNAKUJbfwLGNTyXOwhREwhMbkCGtZT = bPjNAKUJbfwLGNTyXOwhREwhMbkCGtZT
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.freq_bands = bPjNAKUJbfwLGNTyXOwhREwhMbkCGtZT ** (torch.arange(num_freqs) / num_freqs)
    @torch.no_grad()
    def __call__(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, NECAaWUrFGIXcLimrerEYmxYIykQBfXb, cat_dim=-1):
        "x: arbitrary shape of tensor. dim: cat dim"
        iqymPVpxyjOWChGwBkTemSzHJbnJdAIz = []
        for tGtPzoMGgihsdZjwznYiQOolfjOhkaZV in rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.freq_bands:
            iqymPVpxyjOWChGwBkTemSzHJbnJdAIz.append(torch.sin(tGtPzoMGgihsdZjwznYiQOolfjOhkaZV * NECAaWUrFGIXcLimrerEYmxYIykQBfXb))
            iqymPVpxyjOWChGwBkTemSzHJbnJdAIz.append(torch.cos(tGtPzoMGgihsdZjwznYiQOolfjOhkaZV * NECAaWUrFGIXcLimrerEYmxYIykQBfXb))
        return torch.cat(iqymPVpxyjOWChGwBkTemSzHJbnJdAIz, cat_dim)
class NbnWHlaAfbJuIOjrfBViCkwlgfCLRzHJ(nn.Module):
    def __init__(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, IWvtxNbnlwblSXsnVBYEWWvPOluAqqwm, wNdbUArAtdHxCSdEcrgdxbSGltYHXcyp, fourier_freqs=8):
        super().__init__()
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.IWvtxNbnlwblSXsnVBYEWWvPOluAqqwm = IWvtxNbnlwblSXsnVBYEWWvPOluAqqwm
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.wNdbUArAtdHxCSdEcrgdxbSGltYHXcyp = wNdbUArAtdHxCSdEcrgdxbSGltYHXcyp
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.fourier_embedder = zmsTvWBzKMkuQrgypDRwgwSKjMthTVgg(num_freqs=fourier_freqs)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.position_dim = fourier_freqs * 2 * 4  
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.linears = nn.Sequential(
            nn.DhMcMyEvvzmWIEJojbQeGHlzfZKiPzHO(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.IWvtxNbnlwblSXsnVBYEWWvPOluAqqwm + rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.position_dim, 512),
            nn.XHAfRvdQzGhVBUIWzxCQjrhAiQInnRoY(),
            nn.DhMcMyEvvzmWIEJojbQeGHlzfZKiPzHO(512, 512),
            nn.XHAfRvdQzGhVBUIWzxCQjrhAiQInnRoY(),
            nn.DhMcMyEvvzmWIEJojbQeGHlzfZKiPzHO(512, wNdbUArAtdHxCSdEcrgdxbSGltYHXcyp),
        )
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.null_positive_feature = torch.nn.Parameter(
            torch.zeros([rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.IWvtxNbnlwblSXsnVBYEWWvPOluAqqwm]))
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.null_position_feature = torch.nn.Parameter(
            torch.zeros([rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.position_dim]))
    def lqBgIcSWZYylbCPjXksJWDguuSOqoPCJ(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, ogkvBNIZRgGqiRrUKuoYmaTooyiayAsC, npdIyYBsgKLNOVeVWjQcsjYKmaHpbRXB, MQeyDqeqMLSbgCJXnAWPPtoJFFjCWTsF):
        oKoLNmqMHsUubaMUUnyDFEgClwoExDJu, CkYaWzCjmffLyFAjukkxYTtrfjqQGpts, _ = ogkvBNIZRgGqiRrUKuoYmaTooyiayAsC.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg
        DDRQlhrNSGpwTrokWitkZipdfbAqBFxv = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.linears[0].RXBOtvKSHQkBvdKDbckmnlphvVygYURP.DDRQlhrNSGpwTrokWitkZipdfbAqBFxv
        npdIyYBsgKLNOVeVWjQcsjYKmaHpbRXB = npdIyYBsgKLNOVeVWjQcsjYKmaHpbRXB.unsqueeze(-1).sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ(DDRQlhrNSGpwTrokWitkZipdfbAqBFxv)
        MQeyDqeqMLSbgCJXnAWPPtoJFFjCWTsF = MQeyDqeqMLSbgCJXnAWPPtoJFFjCWTsF.sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ(DDRQlhrNSGpwTrokWitkZipdfbAqBFxv)
        kdQzhduVBegJJFHgyQFbxHxZfIGkdhLC = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.fourier_embedder(ogkvBNIZRgGqiRrUKuoYmaTooyiayAsC.sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ(DDRQlhrNSGpwTrokWitkZipdfbAqBFxv))  
        nXIiUbMiyJYoIGPWWJKPjtLPRkfgdwlD = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.null_positive_feature.view(1, 1, -1)
        tytkvwnUYtVTgOzQIlpJtrWQsRVDPeqY = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.null_position_feature.view(1, 1, -1)
        MQeyDqeqMLSbgCJXnAWPPtoJFFjCWTsF = MQeyDqeqMLSbgCJXnAWPPtoJFFjCWTsF * \
            npdIyYBsgKLNOVeVWjQcsjYKmaHpbRXB + (1 - npdIyYBsgKLNOVeVWjQcsjYKmaHpbRXB) * nXIiUbMiyJYoIGPWWJKPjtLPRkfgdwlD
        kdQzhduVBegJJFHgyQFbxHxZfIGkdhLC = kdQzhduVBegJJFHgyQFbxHxZfIGkdhLC * npdIyYBsgKLNOVeVWjQcsjYKmaHpbRXB + (1 - npdIyYBsgKLNOVeVWjQcsjYKmaHpbRXB) * tytkvwnUYtVTgOzQIlpJtrWQsRVDPeqY
        GbeDcLyKATsStDYQhKCKXmNoYGzFwvQi = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.linears(
            torch.cat([MQeyDqeqMLSbgCJXnAWPPtoJFFjCWTsF, kdQzhduVBegJJFHgyQFbxHxZfIGkdhLC], yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk=-1))
        assert GbeDcLyKATsStDYQhKCKXmNoYGzFwvQi.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg == torch.Size([oKoLNmqMHsUubaMUUnyDFEgClwoExDJu, CkYaWzCjmffLyFAjukkxYTtrfjqQGpts, rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.wNdbUArAtdHxCSdEcrgdxbSGltYHXcyp])
        return GbeDcLyKATsStDYQhKCKXmNoYGzFwvQi
class TkCiOuLLRdcjcbAtFUudNpOGjQNrlciP(nn.Module):
    def __init__(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, modules, position_net, ZsGHpZgKPOIjXFUZAXBCrwDjyxVsoOxb):
        super().__init__()
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.module_list = nn.ModuleList(modules)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.position_net = position_net
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.ZsGHpZgKPOIjXFUZAXBCrwDjyxVsoOxb = ZsGHpZgKPOIjXFUZAXBCrwDjyxVsoOxb
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.max_objs = 30
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.current_device = torch.fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc("cpu")
    def CXbyaiMAdPMoXHFFZWXMHZdxjVHxbwap(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, ogkvBNIZRgGqiRrUKuoYmaTooyiayAsC, npdIyYBsgKLNOVeVWjQcsjYKmaHpbRXB, MQeyDqeqMLSbgCJXnAWPPtoJFFjCWTsF):
        GbeDcLyKATsStDYQhKCKXmNoYGzFwvQi = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.position_net(ogkvBNIZRgGqiRrUKuoYmaTooyiayAsC, npdIyYBsgKLNOVeVWjQcsjYKmaHpbRXB, MQeyDqeqMLSbgCJXnAWPPtoJFFjCWTsF)
        def txqWbeldWuTXEOzUjapZMrWhymqrYFLd(NECAaWUrFGIXcLimrerEYmxYIykQBfXb, XlZLJsLRPiguOUrwnKgvbOtnsJeZSwPk):
            nyrzKxQtioheHIZujafABgijbCjrWhBU = XlZLJsLRPiguOUrwnKgvbOtnsJeZSwPk["transformer_index"]
            FRIBQCDfDDxIonplwxvPCicvOmmOgYPC = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.module_list[nyrzKxQtioheHIZujafABgijbCjrWhBU]
            return FRIBQCDfDDxIonplwxvPCicvOmmOgYPC(NECAaWUrFGIXcLimrerEYmxYIykQBfXb, GbeDcLyKATsStDYQhKCKXmNoYGzFwvQi)
        return txqWbeldWuTXEOzUjapZMrWhymqrYFLd
    def HawvDdphzyQfAbXsaAhdEHvyTyKIgYeZ(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, latent_image_shape, fOljKxXLyHfGyNkotLKyQTKMHPpbZVFm, fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc):
        IEfFCfCTfyvJvVHxiDPsIOnopGWoUJhP, cjHIelcAqVoHWdLcgzuZiBumKNTVADsY, xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab, AeIrbRXDkpZlClJGwzMknCltTQQdmhvu = latent_image_shape
        npdIyYBsgKLNOVeVWjQcsjYKmaHpbRXB = torch.zeros([rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.max_objs], fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc="cpu")
        ogkvBNIZRgGqiRrUKuoYmaTooyiayAsC = []
        MQeyDqeqMLSbgCJXnAWPPtoJFFjCWTsF = []
        for HutkrxeXIuRQKOhCWHkiwqLGAsJjUSKj in fOljKxXLyHfGyNkotLKyQTKMHPpbZVFm:
            bokMHjGiefHKvQcAiJMaHIIOvPogwgnt = (HutkrxeXIuRQKOhCWHkiwqLGAsJjUSKj[4]) / AeIrbRXDkpZlClJGwzMknCltTQQdmhvu
            bsjvQkBKRhHOwgGNWMMBjAitwiNOZomL = (HutkrxeXIuRQKOhCWHkiwqLGAsJjUSKj[3]) / xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab
            qRYyQjEAGRjtIxticvyLLasWEAHJzJrD = (HutkrxeXIuRQKOhCWHkiwqLGAsJjUSKj[4] + HutkrxeXIuRQKOhCWHkiwqLGAsJjUSKj[2]) / AeIrbRXDkpZlClJGwzMknCltTQQdmhvu
            ObkVyAOyJafcMOoSWuVQgaIuzeFgXJXF = (HutkrxeXIuRQKOhCWHkiwqLGAsJjUSKj[3] + HutkrxeXIuRQKOhCWHkiwqLGAsJjUSKj[1]) / xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab
            npdIyYBsgKLNOVeVWjQcsjYKmaHpbRXB[len(ogkvBNIZRgGqiRrUKuoYmaTooyiayAsC)] = 1.0
            ogkvBNIZRgGqiRrUKuoYmaTooyiayAsC += [torch.xPmCFphFKpGMpIsczaSKHmMgRPZzJwla((bokMHjGiefHKvQcAiJMaHIIOvPogwgnt, bsjvQkBKRhHOwgGNWMMBjAitwiNOZomL, qRYyQjEAGRjtIxticvyLLasWEAHJzJrD, ObkVyAOyJafcMOoSWuVQgaIuzeFgXJXF)).unsqueeze(0)]
            MQeyDqeqMLSbgCJXnAWPPtoJFFjCWTsF += [HutkrxeXIuRQKOhCWHkiwqLGAsJjUSKj[0]]
        vYljBhDqExCWHlHyZbevrCvDZvERVZco = []
        lYTCYVoxoRoPIiTexoTBOkViQTZGXkEb = []
        if len(ogkvBNIZRgGqiRrUKuoYmaTooyiayAsC) < rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.max_objs:
            vYljBhDqExCWHlHyZbevrCvDZvERVZco = [torch.zeros(
                [rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.max_objs - len(ogkvBNIZRgGqiRrUKuoYmaTooyiayAsC), 4], fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc="cpu")]
            lYTCYVoxoRoPIiTexoTBOkViQTZGXkEb = [torch.zeros(
                [rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.max_objs - len(ogkvBNIZRgGqiRrUKuoYmaTooyiayAsC), rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.ZsGHpZgKPOIjXFUZAXBCrwDjyxVsoOxb], fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc="cpu")]
        pEaUbPUeiKNnMLLQysnfNbmeDNaPjFYE = torch.cat(
            ogkvBNIZRgGqiRrUKuoYmaTooyiayAsC + vYljBhDqExCWHlHyZbevrCvDZvERVZco).unsqueeze(0).kYXcbCDGZMxtOlIZeOtGMsNePlSickQL(IEfFCfCTfyvJvVHxiDPsIOnopGWoUJhP, 1, 1)
        npdIyYBsgKLNOVeVWjQcsjYKmaHpbRXB = npdIyYBsgKLNOVeVWjQcsjYKmaHpbRXB.unsqueeze(0).kYXcbCDGZMxtOlIZeOtGMsNePlSickQL(IEfFCfCTfyvJvVHxiDPsIOnopGWoUJhP, 1)
        AUPHIuKysplzquSfCUyOYZeXeMCpdwhe = torch.cat(MQeyDqeqMLSbgCJXnAWPPtoJFFjCWTsF +
                          lYTCYVoxoRoPIiTexoTBOkViQTZGXkEb).unsqueeze(0).kYXcbCDGZMxtOlIZeOtGMsNePlSickQL(IEfFCfCTfyvJvVHxiDPsIOnopGWoUJhP, 1, 1)
        return rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.CXbyaiMAdPMoXHFFZWXMHZdxjVHxbwap(
            pEaUbPUeiKNnMLLQysnfNbmeDNaPjFYE.sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ(fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc),
            npdIyYBsgKLNOVeVWjQcsjYKmaHpbRXB.sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ(fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc),
            AUPHIuKysplzquSfCUyOYZeXeMCpdwhe.sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ(fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc))
    def zLcxonapnXKVJLjEMFNHUVXeVQUXvOAT(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, latent_image_shape, fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc):
        IEfFCfCTfyvJvVHxiDPsIOnopGWoUJhP, cjHIelcAqVoHWdLcgzuZiBumKNTVADsY, xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab, AeIrbRXDkpZlClJGwzMknCltTQQdmhvu = latent_image_shape
        npdIyYBsgKLNOVeVWjQcsjYKmaHpbRXB = torch.zeros([rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.max_objs], fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc="cpu").kYXcbCDGZMxtOlIZeOtGMsNePlSickQL(IEfFCfCTfyvJvVHxiDPsIOnopGWoUJhP, 1)
        pEaUbPUeiKNnMLLQysnfNbmeDNaPjFYE = torch.zeros([rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.max_objs, 4],
                              fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc="cpu").kYXcbCDGZMxtOlIZeOtGMsNePlSickQL(IEfFCfCTfyvJvVHxiDPsIOnopGWoUJhP, 1, 1)
        AUPHIuKysplzquSfCUyOYZeXeMCpdwhe = torch.zeros([rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.max_objs, rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.ZsGHpZgKPOIjXFUZAXBCrwDjyxVsoOxb],
                            fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc="cpu").kYXcbCDGZMxtOlIZeOtGMsNePlSickQL(IEfFCfCTfyvJvVHxiDPsIOnopGWoUJhP, 1, 1)
        return rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.CXbyaiMAdPMoXHFFZWXMHZdxjVHxbwap(
            pEaUbPUeiKNnMLLQysnfNbmeDNaPjFYE.sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ(fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc),
            npdIyYBsgKLNOVeVWjQcsjYKmaHpbRXB.sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ(fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc),
            AUPHIuKysplzquSfCUyOYZeXeMCpdwhe.sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ(fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc))
def ahutYoNAGGKLXRlfTnRgCkshwGtscWss(ylGhUFMpxPbtUUTfCZpemVkdanRhWmHa):
    AoohABMepYXCBHWerRYrughjaUiujBnQ = ylGhUFMpxPbtUUTfCZpemVkdanRhWmHa.keys()
    GgpaBLoBmoIhHNvNAUUHscrTPvveyTGt = []
    ZsGHpZgKPOIjXFUZAXBCrwDjyxVsoOxb = 768
    for GlZreLQjBCiBptpFgmbsMbhjFlMgPVav in ["input_blocks", "middle_block", "output_blocks"]:
        for b in range(20):
            KWfygTFwVKyNUQhdrkGIWGOYWYhfoVeA = filter(lambda EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm: "{}.{}.".format(GlZreLQjBCiBptpFgmbsMbhjFlMgPVav, b)
                            in EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm and ".fuser." in EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm, AoohABMepYXCBHWerRYrughjaUiujBnQ)
            KWfygTFwVKyNUQhdrkGIWGOYWYhfoVeA = map(lambda EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm: (EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm, EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm.split(".fuser.")[-1]), KWfygTFwVKyNUQhdrkGIWGOYWYhfoVeA)
            gfueIbncTbxWKraajpcCRwNSKjuwXVUC = {}
            for EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm in KWfygTFwVKyNUQhdrkGIWGOYWYhfoVeA:
                gfueIbncTbxWKraajpcCRwNSKjuwXVUC[EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm[1]] = ylGhUFMpxPbtUUTfCZpemVkdanRhWmHa[EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm[0]]
            if len(gfueIbncTbxWKraajpcCRwNSKjuwXVUC) > 0:
                ZqiCYiNfDUNCIdHmASCiuNWYfvyqQifY = gfueIbncTbxWKraajpcCRwNSKjuwXVUC["linear.weight"].BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[0]
                ZsGHpZgKPOIjXFUZAXBCrwDjyxVsoOxb = gfueIbncTbxWKraajpcCRwNSKjuwXVUC["linear.weight"].BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[1]
                if ZsGHpZgKPOIjXFUZAXBCrwDjyxVsoOxb == 768:  
                    QJCnIiVfahCOVrhUgUzEjPLvCsBDwnir = 8
                    SiOpzQSDRgWVXXhLenDXhMYFnSfQmjiy = ZqiCYiNfDUNCIdHmASCiuNWYfvyqQifY // QJCnIiVfahCOVrhUgUzEjPLvCsBDwnir
                else:
                    SiOpzQSDRgWVXXhLenDXhMYFnSfQmjiy = 64
                    QJCnIiVfahCOVrhUgUzEjPLvCsBDwnir = ZqiCYiNfDUNCIdHmASCiuNWYfvyqQifY // SiOpzQSDRgWVXXhLenDXhMYFnSfQmjiy
                laopDrIxhbSgiVDQWHRtttlxyOqWQUtB = IGYPavhLjYtCTqdiWrZVTtEUKsfKknrF(
                    ZqiCYiNfDUNCIdHmASCiuNWYfvyqQifY, ZsGHpZgKPOIjXFUZAXBCrwDjyxVsoOxb, QJCnIiVfahCOVrhUgUzEjPLvCsBDwnir, SiOpzQSDRgWVXXhLenDXhMYFnSfQmjiy)
                laopDrIxhbSgiVDQWHRtttlxyOqWQUtB.OVlRwgmJvqggImaZMfxKZfQnVYfyhIsc(gfueIbncTbxWKraajpcCRwNSKjuwXVUC, strict=False)
                GgpaBLoBmoIhHNvNAUUHscrTPvveyTGt.append(laopDrIxhbSgiVDQWHRtttlxyOqWQUtB)
    if "position_net.null_positive_feature" in AoohABMepYXCBHWerRYrughjaUiujBnQ:
        IWvtxNbnlwblSXsnVBYEWWvPOluAqqwm = ylGhUFMpxPbtUUTfCZpemVkdanRhWmHa["position_net.null_positive_feature"].BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[0]
        wNdbUArAtdHxCSdEcrgdxbSGltYHXcyp = ylGhUFMpxPbtUUTfCZpemVkdanRhWmHa["position_net.linears.4.weight"].BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[0]
        class QZnYAWjUGrGUSUTGoVBSPqGhLUfRqqRR(torch.nn.Module):
            pass
        AeIrbRXDkpZlClJGwzMknCltTQQdmhvu = QZnYAWjUGrGUSUTGoVBSPqGhLUfRqqRR()
        AeIrbRXDkpZlClJGwzMknCltTQQdmhvu.position_net = NbnWHlaAfbJuIOjrfBViCkwlgfCLRzHJ(IWvtxNbnlwblSXsnVBYEWWvPOluAqqwm, wNdbUArAtdHxCSdEcrgdxbSGltYHXcyp)
        AeIrbRXDkpZlClJGwzMknCltTQQdmhvu.OVlRwgmJvqggImaZMfxKZfQnVYfyhIsc(ylGhUFMpxPbtUUTfCZpemVkdanRhWmHa, strict=False)
    bQxLSNgPlazghYEcawwmtsRrmJBIwCXU = TkCiOuLLRdcjcbAtFUudNpOGjQNrlciP(GgpaBLoBmoIhHNvNAUUHscrTPvveyTGt, AeIrbRXDkpZlClJGwzMknCltTQQdmhvu.position_net, ZsGHpZgKPOIjXFUZAXBCrwDjyxVsoOxb)
    return bQxLSNgPlazghYEcawwmtsRrmJBIwCXU
