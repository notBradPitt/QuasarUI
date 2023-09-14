    Args:
        NECAaWUrFGIXcLimrerEYmxYIykQBfXb: (oKoLNmqMHsUubaMUUnyDFEgClwoExDJu, gFdyNTfDqQDeXijWZEnTSFKJXHMWaEiV, vFYBIMOEtqWwjvpBeeDFaIqTrgSbzULJ, AHoGYMpsqEtOaZpAamJqoHqHvnlwZSRh)
        nutobJTmWCYYpulsyYOoRWLklenNVeiu (int): window vqDBJgidQufnKyAltPYRqiKGjmztArDJ
    Returns:
        windows: (num_windows*oKoLNmqMHsUubaMUUnyDFEgClwoExDJu, nutobJTmWCYYpulsyYOoRWLklenNVeiu, nutobJTmWCYYpulsyYOoRWLklenNVeiu, AHoGYMpsqEtOaZpAamJqoHqHvnlwZSRh)
    Args:
        windows: (num_windows*oKoLNmqMHsUubaMUUnyDFEgClwoExDJu, nutobJTmWCYYpulsyYOoRWLklenNVeiu, nutobJTmWCYYpulsyYOoRWLklenNVeiu, AHoGYMpsqEtOaZpAamJqoHqHvnlwZSRh)
        nutobJTmWCYYpulsyYOoRWLklenNVeiu (int): Window vqDBJgidQufnKyAltPYRqiKGjmztArDJ
        gFdyNTfDqQDeXijWZEnTSFKJXHMWaEiV (int): Height of eLyJtroPthPCROYWyMphoIrGatNOOXCO
        vFYBIMOEtqWwjvpBeeDFaIqTrgSbzULJ (int): Width of eLyJtroPthPCROYWyMphoIrGatNOOXCO
    Returns:
        NECAaWUrFGIXcLimrerEYmxYIykQBfXb: (oKoLNmqMHsUubaMUUnyDFEgClwoExDJu, gFdyNTfDqQDeXijWZEnTSFKJXHMWaEiV, vFYBIMOEtqWwjvpBeeDFaIqTrgSbzULJ, AHoGYMpsqEtOaZpAamJqoHqHvnlwZSRh)
    def __init__(
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS,
        yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk,
        nutobJTmWCYYpulsyYOoRWLklenNVeiu,
        WbSAuusmaEgbrureofeJezeXtfsVoscC,
        uGtxGIAnzLWWZnlGFIWJvzLZRYfyFdwT=True,
        cXlznDgkSQpxQLziPvmTAyhhxVhSDLoV=None,
        tGJGoWYafTzhRETOOrClZjPpgXFZUOzU=0.0,
        hjPwvODBKgggBiPujNmVDnfSDUrbQIXL=0.0,
    ):
        super().__init__()
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk = yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.nutobJTmWCYYpulsyYOoRWLklenNVeiu = nutobJTmWCYYpulsyYOoRWLklenNVeiu  
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.WbSAuusmaEgbrureofeJezeXtfsVoscC = WbSAuusmaEgbrureofeJezeXtfsVoscC
        RJpLGjEjPRhDVOaBfeDFMOtajBlLriPe = yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk // WbSAuusmaEgbrureofeJezeXtfsVoscC
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.xmbXivThLFnawFPAJvIDBztziWsaDyEE = cXlznDgkSQpxQLziPvmTAyhhxVhSDLoV or RJpLGjEjPRhDVOaBfeDFMOtajBlLriPe**-0.5
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.psppIXxCSyAsmPWaeuPeRLTPCwLBFIOe = nn.Parameter(  
            torch.zeros((2 * nutobJTmWCYYpulsyYOoRWLklenNVeiu[0] - 1) * (2 * nutobJTmWCYYpulsyYOoRWLklenNVeiu[1] - 1), WbSAuusmaEgbrureofeJezeXtfsVoscC)
        )  
        HWcEeGtBJtpOChhCnNTOPoGJYugATHVi = torch.arange(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.nutobJTmWCYYpulsyYOoRWLklenNVeiu[0])
        lslaUtgDIUhsMqGwoodDkFdnnUaajlOH = torch.arange(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.nutobJTmWCYYpulsyYOoRWLklenNVeiu[1])
        jbKWsVJoZAEQliICCLiLwJEyKLeiQKao = torch.stack(torch.meshgrid([HWcEeGtBJtpOChhCnNTOPoGJYugATHVi, lslaUtgDIUhsMqGwoodDkFdnnUaajlOH]))  
        LpMPNzJBbTIafGKEoMlfJAYESjxwvwJu = torch.flatten(jbKWsVJoZAEQliICCLiLwJEyKLeiQKao, 1)  
        xUtSxqTWrKPLWSsgdjbVmdBZqgCgUkXg = (
            LpMPNzJBbTIafGKEoMlfJAYESjxwvwJu[:, :, None] - LpMPNzJBbTIafGKEoMlfJAYESjxwvwJu[:, None, :]
        )  
        xUtSxqTWrKPLWSsgdjbVmdBZqgCgUkXg = xUtSxqTWrKPLWSsgdjbVmdBZqgCgUkXg.permute(
            1, 2, 0
        ).contiguous()  
        xUtSxqTWrKPLWSsgdjbVmdBZqgCgUkXg[:, :, 0] += rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.nutobJTmWCYYpulsyYOoRWLklenNVeiu[0] - 1  
        xUtSxqTWrKPLWSsgdjbVmdBZqgCgUkXg[:, :, 1] += rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.nutobJTmWCYYpulsyYOoRWLklenNVeiu[1] - 1
        xUtSxqTWrKPLWSsgdjbVmdBZqgCgUkXg[:, :, 0] *= 2 * rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.nutobJTmWCYYpulsyYOoRWLklenNVeiu[1] - 1
        oRUZBArRhEMoqHYrzRoSroQpwOYCIvBp = xUtSxqTWrKPLWSsgdjbVmdBZqgCgUkXg.sum(-1)  
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.BpOtVuSttURsCNYELWmrxpBkqOPYBBlj("relative_position_index", oRUZBArRhEMoqHYrzRoSroQpwOYCIvBp)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.unQNqNyaXZtDbRPdnrUuajLjwVMuGeHZ = nn.DhMcMyEvvzmWIEJojbQeGHlzfZKiPzHO(yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk, yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk * 3, PvdyIPYzYuxTGYQjZbTucTrRGHTQkavB=uGtxGIAnzLWWZnlGFIWJvzLZRYfyFdwT)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.tGJGoWYafTzhRETOOrClZjPpgXFZUOzU = nn.Dropout(tGJGoWYafTzhRETOOrClZjPpgXFZUOzU)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.proj = nn.DhMcMyEvvzmWIEJojbQeGHlzfZKiPzHO(yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk, yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.hjPwvODBKgggBiPujNmVDnfSDUrbQIXL = nn.Dropout(hjPwvODBKgggBiPujNmVDnfSDUrbQIXL)
        trunc_normal_(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.psppIXxCSyAsmPWaeuPeRLTPCwLBFIOe, fOYIxmVRkbmqKCdAjhgqqAEkLdJvKBVd=0.02)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.softmax = nn.Softmax(yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk=-1)
    def lqBgIcSWZYylbCPjXksJWDguuSOqoPCJ(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, NECAaWUrFGIXcLimrerEYmxYIykQBfXb, KHpRlHOzblljQyskecSxzUuWZtneWwta=None):
        qNFDCcJCurubqgfYKilsAnvvBJnmzOLl, CkYaWzCjmffLyFAjukkxYTtrfjqQGpts, AHoGYMpsqEtOaZpAamJqoHqHvnlwZSRh = NECAaWUrFGIXcLimrerEYmxYIykQBfXb.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg
        unQNqNyaXZtDbRPdnrUuajLjwVMuGeHZ = (
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.unQNqNyaXZtDbRPdnrUuajLjwVMuGeHZ(NECAaWUrFGIXcLimrerEYmxYIykQBfXb)
            .reshape(qNFDCcJCurubqgfYKilsAnvvBJnmzOLl, CkYaWzCjmffLyFAjukkxYTtrfjqQGpts, 3, rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.WbSAuusmaEgbrureofeJezeXtfsVoscC, AHoGYMpsqEtOaZpAamJqoHqHvnlwZSRh // rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.WbSAuusmaEgbrureofeJezeXtfsVoscC)
            .permute(2, 0, 3, 1, 4)
        )
        mxaMgfLZUDPObiqkdCgHnnARjBNVGQnh, EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm, powGafreWfwlSAqPpTpUhFgpFVqCPavl = (
            unQNqNyaXZtDbRPdnrUuajLjwVMuGeHZ[0],
            unQNqNyaXZtDbRPdnrUuajLjwVMuGeHZ[1],
            unQNqNyaXZtDbRPdnrUuajLjwVMuGeHZ[2],
        )  
        mxaMgfLZUDPObiqkdCgHnnARjBNVGQnh = mxaMgfLZUDPObiqkdCgHnnARjBNVGQnh * rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.xmbXivThLFnawFPAJvIDBztziWsaDyEE
        tUmudCfKVwpeKVqJPkVQAwLriIrTDLbW = mxaMgfLZUDPObiqkdCgHnnARjBNVGQnh @ EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm.transpose(-2, -1)
        QknDLfOPGxCnhgwlIhYUagKdzScsoXIB = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.psppIXxCSyAsmPWaeuPeRLTPCwLBFIOe[
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.oRUZBArRhEMoqHYrzRoSroQpwOYCIvBp.view(-1)  
        ].view(
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.nutobJTmWCYYpulsyYOoRWLklenNVeiu[0] * rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.nutobJTmWCYYpulsyYOoRWLklenNVeiu[1],
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.nutobJTmWCYYpulsyYOoRWLklenNVeiu[0] * rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.nutobJTmWCYYpulsyYOoRWLklenNVeiu[1],
            -1,
        )  
        QknDLfOPGxCnhgwlIhYUagKdzScsoXIB = QknDLfOPGxCnhgwlIhYUagKdzScsoXIB.permute(
            2, 0, 1
        ).contiguous()  
        tUmudCfKVwpeKVqJPkVQAwLriIrTDLbW = tUmudCfKVwpeKVqJPkVQAwLriIrTDLbW + QknDLfOPGxCnhgwlIhYUagKdzScsoXIB.unsqueeze(0)
        if KHpRlHOzblljQyskecSxzUuWZtneWwta is not None:
            ziQrOWJJTQePfPYDwdxSXQFLRreOKbvR = KHpRlHOzblljQyskecSxzUuWZtneWwta.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[0]
            tUmudCfKVwpeKVqJPkVQAwLriIrTDLbW = tUmudCfKVwpeKVqJPkVQAwLriIrTDLbW.view(qNFDCcJCurubqgfYKilsAnvvBJnmzOLl // ziQrOWJJTQePfPYDwdxSXQFLRreOKbvR, ziQrOWJJTQePfPYDwdxSXQFLRreOKbvR, rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.WbSAuusmaEgbrureofeJezeXtfsVoscC, CkYaWzCjmffLyFAjukkxYTtrfjqQGpts, CkYaWzCjmffLyFAjukkxYTtrfjqQGpts) + KHpRlHOzblljQyskecSxzUuWZtneWwta.unsqueeze(
                1
            ).unsqueeze(0)
            tUmudCfKVwpeKVqJPkVQAwLriIrTDLbW = tUmudCfKVwpeKVqJPkVQAwLriIrTDLbW.view(-1, rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.WbSAuusmaEgbrureofeJezeXtfsVoscC, CkYaWzCjmffLyFAjukkxYTtrfjqQGpts, CkYaWzCjmffLyFAjukkxYTtrfjqQGpts)
            tUmudCfKVwpeKVqJPkVQAwLriIrTDLbW = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.softmax(tUmudCfKVwpeKVqJPkVQAwLriIrTDLbW)
        else:
            tUmudCfKVwpeKVqJPkVQAwLriIrTDLbW = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.softmax(tUmudCfKVwpeKVqJPkVQAwLriIrTDLbW)
        tUmudCfKVwpeKVqJPkVQAwLriIrTDLbW = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.tGJGoWYafTzhRETOOrClZjPpgXFZUOzU(tUmudCfKVwpeKVqJPkVQAwLriIrTDLbW)
        NECAaWUrFGIXcLimrerEYmxYIykQBfXb = (tUmudCfKVwpeKVqJPkVQAwLriIrTDLbW @ powGafreWfwlSAqPpTpUhFgpFVqCPavl).transpose(1, 2).reshape(qNFDCcJCurubqgfYKilsAnvvBJnmzOLl, CkYaWzCjmffLyFAjukkxYTtrfjqQGpts, AHoGYMpsqEtOaZpAamJqoHqHvnlwZSRh)
        NECAaWUrFGIXcLimrerEYmxYIykQBfXb = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.proj(NECAaWUrFGIXcLimrerEYmxYIykQBfXb)
        NECAaWUrFGIXcLimrerEYmxYIykQBfXb = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.hjPwvODBKgggBiPujNmVDnfSDUrbQIXL(NECAaWUrFGIXcLimrerEYmxYIykQBfXb)
        return NECAaWUrFGIXcLimrerEYmxYIykQBfXb
    def UQQrTqiwAKPKtTyuidtRpsLNWekTFczd(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS) -> str:
        return f"dim={self.dim}, window_size={self.window_size}, num_heads={self.num_heads}"
    def epXNvUYhxcvAnkNxLYKoeNLGkQZyoeec(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, CkYaWzCjmffLyFAjukkxYTtrfjqQGpts):
        epXNvUYhxcvAnkNxLYKoeNLGkQZyoeec = 0
        epXNvUYhxcvAnkNxLYKoeNLGkQZyoeec += CkYaWzCjmffLyFAjukkxYTtrfjqQGpts * rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk * 3 * rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk
        epXNvUYhxcvAnkNxLYKoeNLGkQZyoeec += rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.WbSAuusmaEgbrureofeJezeXtfsVoscC * CkYaWzCjmffLyFAjukkxYTtrfjqQGpts * (rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk // rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.WbSAuusmaEgbrureofeJezeXtfsVoscC) * CkYaWzCjmffLyFAjukkxYTtrfjqQGpts
        epXNvUYhxcvAnkNxLYKoeNLGkQZyoeec += rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.WbSAuusmaEgbrureofeJezeXtfsVoscC * CkYaWzCjmffLyFAjukkxYTtrfjqQGpts * CkYaWzCjmffLyFAjukkxYTtrfjqQGpts * (rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk // rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.WbSAuusmaEgbrureofeJezeXtfsVoscC)
        epXNvUYhxcvAnkNxLYKoeNLGkQZyoeec += CkYaWzCjmffLyFAjukkxYTtrfjqQGpts * rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk * rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk
        return epXNvUYhxcvAnkNxLYKoeNLGkQZyoeec
class kdrkFBfJmtiPIYqxzEHXaLXyHdTuEzkK(nn.Module):
    r"""Swin Transformer BTYbrqbRvGGOjbsUzDMkWIBzNvOJUbif.
    Args:
        yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk (int): Number of input channels.
        IONObgzScAvEgELMQbHyEzZqOHcvcOTg (tuple[int]): Input resulotion.
        WbSAuusmaEgbrureofeJezeXtfsVoscC (int): Number of psnGIaaNNBTQhtdDvLAOAncJBcOCafNn QEnKImSSxUuBDHahcSgvZCYYpzjKVrVk.
        nutobJTmWCYYpulsyYOoRWLklenNVeiu (int): Window vqDBJgidQufnKyAltPYRqiKGjmztArDJ.
        VxEFwqRUZKQIODDttRLPjJQWwjYKIRso (int): Shift vqDBJgidQufnKyAltPYRqiKGjmztArDJ for SW-MSA.
        uDdUvEneYSYoIevRgfdDqvFctrSBFezp (float): Ratio of mlp hidden yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ FPlsdAwlwymuCRSvDfaEeNjwKAgUwgXu yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk.
        uGtxGIAnzLWWZnlGFIWJvzLZRYfyFdwT (bool, optional): If True, add GlZreLQjBCiBptpFgmbsMbhjFlMgPVav learnable PvdyIPYzYuxTGYQjZbTucTrRGHTQkavB sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ oFxedobBnFbKeewIgTfUgblKziGvmndF, nyrzKxQtioheHIZujafABgijbCjrWhBU, GXNVXDlnsSLzkmussBPoJXgJwuXIiwsc. Default: True
        cXlznDgkSQpxQLziPvmTAyhhxVhSDLoV (float | None, optional): Override default qk xmbXivThLFnawFPAJvIDBztziWsaDyEE of RJpLGjEjPRhDVOaBfeDFMOtajBlLriPe ** -0.5 if set.
        UopxEzgpVJqkfTBuNkdEmNLRqPMUWpUu (float, optional): Dropout rate. Default: 0.0
        tGJGoWYafTzhRETOOrClZjPpgXFZUOzU (float, optional): Attention kcIxGCXrUvsLPSfmGoULGFzAthVmTXcA rate. Default: 0.0
        rzBOFNtNGPLXcyQbBkTWNeSrLkUVYuYg (float, optional): Stochastic JtnlCSDzHOgtbZVTfQMidKPjmOFZfzZX rate. Default: 0.0
        act_layer (nn.Module, optional): Activation rmOubEJgfxmJuwTevhKPPVPDYGHXWRFZ. Default: nn.GELU
        LSMbVVMwSksHBLrtUDiFhcEHyPIDcKoh (nn.Module, optional): Normalization rmOubEJgfxmJuwTevhKPPVPDYGHXWRFZ.  Default: nn.SeaDiaiECtgJbgiExWzpSnrizTosOUam
    def __init__(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, IONObgzScAvEgELMQbHyEzZqOHcvcOTg, yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk, LSMbVVMwSksHBLrtUDiFhcEHyPIDcKoh=nn.SeaDiaiECtgJbgiExWzpSnrizTosOUam):
        super().__init__()
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.IONObgzScAvEgELMQbHyEzZqOHcvcOTg = IONObgzScAvEgELMQbHyEzZqOHcvcOTg
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk = yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.reduction = nn.DhMcMyEvvzmWIEJojbQeGHlzfZKiPzHO(4 * yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk, 2 * yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk, PvdyIPYzYuxTGYQjZbTucTrRGHTQkavB=False)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.norm = LSMbVVMwSksHBLrtUDiFhcEHyPIDcKoh(4 * yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk)
    def lqBgIcSWZYylbCPjXksJWDguuSOqoPCJ(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, NECAaWUrFGIXcLimrerEYmxYIykQBfXb):
        gFdyNTfDqQDeXijWZEnTSFKJXHMWaEiV, vFYBIMOEtqWwjvpBeeDFaIqTrgSbzULJ = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.IONObgzScAvEgELMQbHyEzZqOHcvcOTg
        oKoLNmqMHsUubaMUUnyDFEgClwoExDJu, iDkmScOFEQSvigzoQVmokXyFnStBqjCR, AHoGYMpsqEtOaZpAamJqoHqHvnlwZSRh = NECAaWUrFGIXcLimrerEYmxYIykQBfXb.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg
        assert iDkmScOFEQSvigzoQVmokXyFnStBqjCR == gFdyNTfDqQDeXijWZEnTSFKJXHMWaEiV * vFYBIMOEtqWwjvpBeeDFaIqTrgSbzULJ, "input feature has wrong size"
        assert gFdyNTfDqQDeXijWZEnTSFKJXHMWaEiV % 2 == 0 and vFYBIMOEtqWwjvpBeeDFaIqTrgSbzULJ % 2 == 0, f"x size ({H}*{W}) are not even."
        NECAaWUrFGIXcLimrerEYmxYIykQBfXb = NECAaWUrFGIXcLimrerEYmxYIykQBfXb.view(oKoLNmqMHsUubaMUUnyDFEgClwoExDJu, gFdyNTfDqQDeXijWZEnTSFKJXHMWaEiV, vFYBIMOEtqWwjvpBeeDFaIqTrgSbzULJ, AHoGYMpsqEtOaZpAamJqoHqHvnlwZSRh)
        UBGvtPbFIPlcsBIwyWKuWMZeENGLMRAP = NECAaWUrFGIXcLimrerEYmxYIykQBfXb[:, 0::2, 0::2, :]  
        bokMHjGiefHKvQcAiJMaHIIOvPogwgnt = NECAaWUrFGIXcLimrerEYmxYIykQBfXb[:, 1::2, 0::2, :]  
        qRYyQjEAGRjtIxticvyLLasWEAHJzJrD = NECAaWUrFGIXcLimrerEYmxYIykQBfXb[:, 0::2, 1::2, :]  
        bhIpxBXekbOHXwSyfdqKHptgjtkdVVmj = NECAaWUrFGIXcLimrerEYmxYIykQBfXb[:, 1::2, 1::2, :]  
        NECAaWUrFGIXcLimrerEYmxYIykQBfXb = torch.cat([UBGvtPbFIPlcsBIwyWKuWMZeENGLMRAP, bokMHjGiefHKvQcAiJMaHIIOvPogwgnt, qRYyQjEAGRjtIxticvyLLasWEAHJzJrD, bhIpxBXekbOHXwSyfdqKHptgjtkdVVmj], -1)  
        NECAaWUrFGIXcLimrerEYmxYIykQBfXb = NECAaWUrFGIXcLimrerEYmxYIykQBfXb.view(oKoLNmqMHsUubaMUUnyDFEgClwoExDJu, -1, 4 * AHoGYMpsqEtOaZpAamJqoHqHvnlwZSRh)  
        NECAaWUrFGIXcLimrerEYmxYIykQBfXb = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.norm(NECAaWUrFGIXcLimrerEYmxYIykQBfXb)
        NECAaWUrFGIXcLimrerEYmxYIykQBfXb = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.reduction(NECAaWUrFGIXcLimrerEYmxYIykQBfXb)
        return NECAaWUrFGIXcLimrerEYmxYIykQBfXb
    def UQQrTqiwAKPKtTyuidtRpsLNWekTFczd(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS) -> str:
        return f"input_resolution={self.input_resolution}, dim={self.dim}"
    def epXNvUYhxcvAnkNxLYKoeNLGkQZyoeec(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS):
        gFdyNTfDqQDeXijWZEnTSFKJXHMWaEiV, vFYBIMOEtqWwjvpBeeDFaIqTrgSbzULJ = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.IONObgzScAvEgELMQbHyEzZqOHcvcOTg
        epXNvUYhxcvAnkNxLYKoeNLGkQZyoeec = gFdyNTfDqQDeXijWZEnTSFKJXHMWaEiV * vFYBIMOEtqWwjvpBeeDFaIqTrgSbzULJ * rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk
        epXNvUYhxcvAnkNxLYKoeNLGkQZyoeec += (gFdyNTfDqQDeXijWZEnTSFKJXHMWaEiV // 2) * (vFYBIMOEtqWwjvpBeeDFaIqTrgSbzULJ // 2) * 4 * rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk * 2 * rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk
        return epXNvUYhxcvAnkNxLYKoeNLGkQZyoeec
class UfzxIOJuREOajqPOZefZyUrSfxDATsJp(nn.Module):
    def __init__(
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS,
        yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk,
        IONObgzScAvEgELMQbHyEzZqOHcvcOTg,
        JtnlCSDzHOgtbZVTfQMidKPjmOFZfzZX,
        WbSAuusmaEgbrureofeJezeXtfsVoscC,
        nutobJTmWCYYpulsyYOoRWLklenNVeiu,
        uDdUvEneYSYoIevRgfdDqvFctrSBFezp=4.0,
        uGtxGIAnzLWWZnlGFIWJvzLZRYfyFdwT=True,
        cXlznDgkSQpxQLziPvmTAyhhxVhSDLoV=None,
        UopxEzgpVJqkfTBuNkdEmNLRqPMUWpUu=0.0,
        tGJGoWYafTzhRETOOrClZjPpgXFZUOzU=0.0,
        rzBOFNtNGPLXcyQbBkTWNeSrLkUVYuYg=0.0,
        LSMbVVMwSksHBLrtUDiFhcEHyPIDcKoh=nn.SeaDiaiECtgJbgiExWzpSnrizTosOUam,
        FNdFYgmARbySAmYyEvSINcVrOJlCpKfW=None,
        TkHgGRFhDYRqyKuFvQRlKbpOBXUaEDVU=False,
    ):
        super().__init__()
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk = yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.IONObgzScAvEgELMQbHyEzZqOHcvcOTg = IONObgzScAvEgELMQbHyEzZqOHcvcOTg
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.JtnlCSDzHOgtbZVTfQMidKPjmOFZfzZX = JtnlCSDzHOgtbZVTfQMidKPjmOFZfzZX
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.TkHgGRFhDYRqyKuFvQRlKbpOBXUaEDVU = TkHgGRFhDYRqyKuFvQRlKbpOBXUaEDVU
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.blocks = nn.ModuleList(
            [
                kdrkFBfJmtiPIYqxzEHXaLXyHdTuEzkK(
                    yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk=yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk,
                    IONObgzScAvEgELMQbHyEzZqOHcvcOTg=IONObgzScAvEgELMQbHyEzZqOHcvcOTg,
                    WbSAuusmaEgbrureofeJezeXtfsVoscC=WbSAuusmaEgbrureofeJezeXtfsVoscC,
                    nutobJTmWCYYpulsyYOoRWLklenNVeiu=nutobJTmWCYYpulsyYOoRWLklenNVeiu,
                    VxEFwqRUZKQIODDttRLPjJQWwjYKIRso=0 if (HCXmerBqIMuTscBONzTGKYapYSxWTYHo % 2 == 0) else nutobJTmWCYYpulsyYOoRWLklenNVeiu // 2,
                    uDdUvEneYSYoIevRgfdDqvFctrSBFezp=uDdUvEneYSYoIevRgfdDqvFctrSBFezp,
                    uGtxGIAnzLWWZnlGFIWJvzLZRYfyFdwT=uGtxGIAnzLWWZnlGFIWJvzLZRYfyFdwT,
                    cXlznDgkSQpxQLziPvmTAyhhxVhSDLoV=cXlznDgkSQpxQLziPvmTAyhhxVhSDLoV,
                    UopxEzgpVJqkfTBuNkdEmNLRqPMUWpUu=UopxEzgpVJqkfTBuNkdEmNLRqPMUWpUu,
                    tGJGoWYafTzhRETOOrClZjPpgXFZUOzU=tGJGoWYafTzhRETOOrClZjPpgXFZUOzU,
                    rzBOFNtNGPLXcyQbBkTWNeSrLkUVYuYg=rzBOFNtNGPLXcyQbBkTWNeSrLkUVYuYg[HCXmerBqIMuTscBONzTGKYapYSxWTYHo]
                    if isinstance(rzBOFNtNGPLXcyQbBkTWNeSrLkUVYuYg, list)
                    else rzBOFNtNGPLXcyQbBkTWNeSrLkUVYuYg,
                    LSMbVVMwSksHBLrtUDiFhcEHyPIDcKoh=LSMbVVMwSksHBLrtUDiFhcEHyPIDcKoh,
                )
                for HCXmerBqIMuTscBONzTGKYapYSxWTYHo in range(JtnlCSDzHOgtbZVTfQMidKPjmOFZfzZX)
            ]
        )
        if FNdFYgmARbySAmYyEvSINcVrOJlCpKfW is not None:
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.FNdFYgmARbySAmYyEvSINcVrOJlCpKfW = FNdFYgmARbySAmYyEvSINcVrOJlCpKfW(
                IONObgzScAvEgELMQbHyEzZqOHcvcOTg, yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk=yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk, LSMbVVMwSksHBLrtUDiFhcEHyPIDcKoh=LSMbVVMwSksHBLrtUDiFhcEHyPIDcKoh
            )
        else:
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.FNdFYgmARbySAmYyEvSINcVrOJlCpKfW = None
    def lqBgIcSWZYylbCPjXksJWDguuSOqoPCJ(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, NECAaWUrFGIXcLimrerEYmxYIykQBfXb, x_size):
        for LLiMCtLJBqUPDeOUdzNtdeEeLAsRdhQK in rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.blocks:
            if rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.TkHgGRFhDYRqyKuFvQRlKbpOBXUaEDVU:
                NECAaWUrFGIXcLimrerEYmxYIykQBfXb = vcSlHLxBcVodHmZrzACHLEJuENMXjWTG.vcSlHLxBcVodHmZrzACHLEJuENMXjWTG(LLiMCtLJBqUPDeOUdzNtdeEeLAsRdhQK, NECAaWUrFGIXcLimrerEYmxYIykQBfXb, x_size)
            else:
                NECAaWUrFGIXcLimrerEYmxYIykQBfXb = LLiMCtLJBqUPDeOUdzNtdeEeLAsRdhQK(NECAaWUrFGIXcLimrerEYmxYIykQBfXb, x_size)
        if rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.FNdFYgmARbySAmYyEvSINcVrOJlCpKfW is not None:
            NECAaWUrFGIXcLimrerEYmxYIykQBfXb = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.FNdFYgmARbySAmYyEvSINcVrOJlCpKfW(NECAaWUrFGIXcLimrerEYmxYIykQBfXb)
        return NECAaWUrFGIXcLimrerEYmxYIykQBfXb
    def UQQrTqiwAKPKtTyuidtRpsLNWekTFczd(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS) -> str:
        return f"dim={self.dim}, input_resolution={self.input_resolution}, depth={self.depth}"
    def epXNvUYhxcvAnkNxLYKoeNLGkQZyoeec(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS):
        epXNvUYhxcvAnkNxLYKoeNLGkQZyoeec = 0
        for LLiMCtLJBqUPDeOUdzNtdeEeLAsRdhQK in rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.blocks:
            epXNvUYhxcvAnkNxLYKoeNLGkQZyoeec += LLiMCtLJBqUPDeOUdzNtdeEeLAsRdhQK.epXNvUYhxcvAnkNxLYKoeNLGkQZyoeec()  
        if rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.FNdFYgmARbySAmYyEvSINcVrOJlCpKfW is not None:
            epXNvUYhxcvAnkNxLYKoeNLGkQZyoeec += rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.FNdFYgmARbySAmYyEvSINcVrOJlCpKfW.epXNvUYhxcvAnkNxLYKoeNLGkQZyoeec()
        return epXNvUYhxcvAnkNxLYKoeNLGkQZyoeec
class yApHPTBISkIKCdCqKXuDUjyCboIbEVqB(nn.Module):
    def __init__(
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS,
        yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk,
        IONObgzScAvEgELMQbHyEzZqOHcvcOTg,
        JtnlCSDzHOgtbZVTfQMidKPjmOFZfzZX,
        WbSAuusmaEgbrureofeJezeXtfsVoscC,
        nutobJTmWCYYpulsyYOoRWLklenNVeiu,
        uDdUvEneYSYoIevRgfdDqvFctrSBFezp=4.0,
        uGtxGIAnzLWWZnlGFIWJvzLZRYfyFdwT=True,
        cXlznDgkSQpxQLziPvmTAyhhxVhSDLoV=None,
        UopxEzgpVJqkfTBuNkdEmNLRqPMUWpUu=0.0,
        tGJGoWYafTzhRETOOrClZjPpgXFZUOzU=0.0,
        rzBOFNtNGPLXcyQbBkTWNeSrLkUVYuYg=0.0,
        LSMbVVMwSksHBLrtUDiFhcEHyPIDcKoh=nn.SeaDiaiECtgJbgiExWzpSnrizTosOUam,
        FNdFYgmARbySAmYyEvSINcVrOJlCpKfW=None,
        TkHgGRFhDYRqyKuFvQRlKbpOBXUaEDVU=False,
        FRfCpqDfnuqJOdWObzdWdyzDuFpQbGQE=224,
        HtvgnwOLVGNIRZoncKchqGwewNWrcyOO=4,
        afjLwgjwIXGXlqqPLRgZmElxkEvNNGqp="1conv",
    ):
        super(yApHPTBISkIKCdCqKXuDUjyCboIbEVqB, rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS).__init__()
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk = yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.IONObgzScAvEgELMQbHyEzZqOHcvcOTg = IONObgzScAvEgELMQbHyEzZqOHcvcOTg
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.residual_group = UfzxIOJuREOajqPOZefZyUrSfxDATsJp(
            yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk=yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk,
            IONObgzScAvEgELMQbHyEzZqOHcvcOTg=IONObgzScAvEgELMQbHyEzZqOHcvcOTg,
            JtnlCSDzHOgtbZVTfQMidKPjmOFZfzZX=JtnlCSDzHOgtbZVTfQMidKPjmOFZfzZX,
            WbSAuusmaEgbrureofeJezeXtfsVoscC=WbSAuusmaEgbrureofeJezeXtfsVoscC,
            nutobJTmWCYYpulsyYOoRWLklenNVeiu=nutobJTmWCYYpulsyYOoRWLklenNVeiu,
            uDdUvEneYSYoIevRgfdDqvFctrSBFezp=uDdUvEneYSYoIevRgfdDqvFctrSBFezp,
            uGtxGIAnzLWWZnlGFIWJvzLZRYfyFdwT=uGtxGIAnzLWWZnlGFIWJvzLZRYfyFdwT,
            cXlznDgkSQpxQLziPvmTAyhhxVhSDLoV=cXlznDgkSQpxQLziPvmTAyhhxVhSDLoV,
            UopxEzgpVJqkfTBuNkdEmNLRqPMUWpUu=UopxEzgpVJqkfTBuNkdEmNLRqPMUWpUu,
            tGJGoWYafTzhRETOOrClZjPpgXFZUOzU=tGJGoWYafTzhRETOOrClZjPpgXFZUOzU,
            rzBOFNtNGPLXcyQbBkTWNeSrLkUVYuYg=rzBOFNtNGPLXcyQbBkTWNeSrLkUVYuYg,
            LSMbVVMwSksHBLrtUDiFhcEHyPIDcKoh=LSMbVVMwSksHBLrtUDiFhcEHyPIDcKoh,
            FNdFYgmARbySAmYyEvSINcVrOJlCpKfW=FNdFYgmARbySAmYyEvSINcVrOJlCpKfW,
            TkHgGRFhDYRqyKuFvQRlKbpOBXUaEDVU=TkHgGRFhDYRqyKuFvQRlKbpOBXUaEDVU,
        )
        if afjLwgjwIXGXlqqPLRgZmElxkEvNNGqp == "1conv":
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.VRzIOXLfdDszfSOpzuKgtjeGGtXuyctm = nn.LcFcvNeYCKrBHlNkoWrkqdbxdkNCJBBK(yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk, yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk, 3, 1, 1)
        elif afjLwgjwIXGXlqqPLRgZmElxkEvNNGqp == "3conv":
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.VRzIOXLfdDszfSOpzuKgtjeGGtXuyctm = nn.Sequential(
                nn.LcFcvNeYCKrBHlNkoWrkqdbxdkNCJBBK(yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk, yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk // 4, 3, 1, 1),
                nn.LeakyReLU(negative_slope=0.2, inplace=True),
                nn.LcFcvNeYCKrBHlNkoWrkqdbxdkNCJBBK(yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk // 4, yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk // 4, 1, 1, 0),
                nn.LeakyReLU(negative_slope=0.2, inplace=True),
                nn.LcFcvNeYCKrBHlNkoWrkqdbxdkNCJBBK(yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk // 4, yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk, 3, 1, 1),
            )
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.patch_embed = wGvAtecRwaUEsRiKuHUaxqkCHvuCyqjL(
            FRfCpqDfnuqJOdWObzdWdyzDuFpQbGQE=FRfCpqDfnuqJOdWObzdWdyzDuFpQbGQE,
            HtvgnwOLVGNIRZoncKchqGwewNWrcyOO=HtvgnwOLVGNIRZoncKchqGwewNWrcyOO,
            RnQeJtCTKIYBykxuudjZsYNxhhDUcfst=0,
            ImrGjiFVgoYlstXoXVYKbphbCLYUVMTp=yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk,
            LSMbVVMwSksHBLrtUDiFhcEHyPIDcKoh=None,
        )
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.patch_unembed = PatchUnEmbed(
            FRfCpqDfnuqJOdWObzdWdyzDuFpQbGQE=FRfCpqDfnuqJOdWObzdWdyzDuFpQbGQE,
            HtvgnwOLVGNIRZoncKchqGwewNWrcyOO=HtvgnwOLVGNIRZoncKchqGwewNWrcyOO,
            RnQeJtCTKIYBykxuudjZsYNxhhDUcfst=0,
            ImrGjiFVgoYlstXoXVYKbphbCLYUVMTp=yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk,
            LSMbVVMwSksHBLrtUDiFhcEHyPIDcKoh=None,
        )
    def lqBgIcSWZYylbCPjXksJWDguuSOqoPCJ(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, NECAaWUrFGIXcLimrerEYmxYIykQBfXb, x_size):
        return (
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.patch_embed(
                rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.VRzIOXLfdDszfSOpzuKgtjeGGtXuyctm(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.patch_unembed(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.residual_group(NECAaWUrFGIXcLimrerEYmxYIykQBfXb, x_size), x_size))
            )
            + NECAaWUrFGIXcLimrerEYmxYIykQBfXb
        )
    def epXNvUYhxcvAnkNxLYKoeNLGkQZyoeec(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS):
        epXNvUYhxcvAnkNxLYKoeNLGkQZyoeec = 0
        epXNvUYhxcvAnkNxLYKoeNLGkQZyoeec += rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.residual_group.epXNvUYhxcvAnkNxLYKoeNLGkQZyoeec()
        gFdyNTfDqQDeXijWZEnTSFKJXHMWaEiV, vFYBIMOEtqWwjvpBeeDFaIqTrgSbzULJ = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.IONObgzScAvEgELMQbHyEzZqOHcvcOTg
        epXNvUYhxcvAnkNxLYKoeNLGkQZyoeec += gFdyNTfDqQDeXijWZEnTSFKJXHMWaEiV * vFYBIMOEtqWwjvpBeeDFaIqTrgSbzULJ * rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk * rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk * 9
        epXNvUYhxcvAnkNxLYKoeNLGkQZyoeec += rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.patch_embed.epXNvUYhxcvAnkNxLYKoeNLGkQZyoeec()
        epXNvUYhxcvAnkNxLYKoeNLGkQZyoeec += rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.patch_unembed.epXNvUYhxcvAnkNxLYKoeNLGkQZyoeec()
        return epXNvUYhxcvAnkNxLYKoeNLGkQZyoeec
class wGvAtecRwaUEsRiKuHUaxqkCHvuCyqjL(nn.Module):
    r"""Image sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ Patch Embedding
    Args:
        FRfCpqDfnuqJOdWObzdWdyzDuFpQbGQE (int): Image vqDBJgidQufnKyAltPYRqiKGjmztArDJ.  Default: 224.
        HtvgnwOLVGNIRZoncKchqGwewNWrcyOO (int): Patch token vqDBJgidQufnKyAltPYRqiKGjmztArDJ. Default: 4.
        RnQeJtCTKIYBykxuudjZsYNxhhDUcfst (int): Number of input eLyJtroPthPCROYWyMphoIrGatNOOXCO channels. Default: 3.
        ImrGjiFVgoYlstXoXVYKbphbCLYUVMTp (int): Number of BJkSsAwbTZLfucgvGkDLcVEiRIlYJCmK projection pwTxzdNTJGMWEFORftJTEtPYMMiKwDuP channels. Default: 96.
        LSMbVVMwSksHBLrtUDiFhcEHyPIDcKoh (nn.Module, optional): Normalization rmOubEJgfxmJuwTevhKPPVPDYGHXWRFZ. Default: None
    def __init__(
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, FRfCpqDfnuqJOdWObzdWdyzDuFpQbGQE=224, HtvgnwOLVGNIRZoncKchqGwewNWrcyOO=4, RnQeJtCTKIYBykxuudjZsYNxhhDUcfst=3, ImrGjiFVgoYlstXoXVYKbphbCLYUVMTp=96, LSMbVVMwSksHBLrtUDiFhcEHyPIDcKoh=None
    ):
        super().__init__()
        FRfCpqDfnuqJOdWObzdWdyzDuFpQbGQE = to_2tuple(FRfCpqDfnuqJOdWObzdWdyzDuFpQbGQE)
        HtvgnwOLVGNIRZoncKchqGwewNWrcyOO = to_2tuple(HtvgnwOLVGNIRZoncKchqGwewNWrcyOO)
        ZhBQpOcXqgRdyopMzHJslgylqnbfLHtC = [
            FRfCpqDfnuqJOdWObzdWdyzDuFpQbGQE[0] // HtvgnwOLVGNIRZoncKchqGwewNWrcyOO[0],  
            FRfCpqDfnuqJOdWObzdWdyzDuFpQbGQE[1] // HtvgnwOLVGNIRZoncKchqGwewNWrcyOO[1],  
        ]
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.FRfCpqDfnuqJOdWObzdWdyzDuFpQbGQE = FRfCpqDfnuqJOdWObzdWdyzDuFpQbGQE
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.HtvgnwOLVGNIRZoncKchqGwewNWrcyOO = HtvgnwOLVGNIRZoncKchqGwewNWrcyOO
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.ZhBQpOcXqgRdyopMzHJslgylqnbfLHtC = ZhBQpOcXqgRdyopMzHJslgylqnbfLHtC
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.num_patches = ZhBQpOcXqgRdyopMzHJslgylqnbfLHtC[0] * ZhBQpOcXqgRdyopMzHJslgylqnbfLHtC[1]
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.RnQeJtCTKIYBykxuudjZsYNxhhDUcfst = RnQeJtCTKIYBykxuudjZsYNxhhDUcfst
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.ImrGjiFVgoYlstXoXVYKbphbCLYUVMTp = ImrGjiFVgoYlstXoXVYKbphbCLYUVMTp
    def lqBgIcSWZYylbCPjXksJWDguuSOqoPCJ(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, NECAaWUrFGIXcLimrerEYmxYIykQBfXb, x_size):
        oKoLNmqMHsUubaMUUnyDFEgClwoExDJu, QbOVoViABVXfgtBCCrsAyegyEKKYSFJC, AHoGYMpsqEtOaZpAamJqoHqHvnlwZSRh = NECAaWUrFGIXcLimrerEYmxYIykQBfXb.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg
        NECAaWUrFGIXcLimrerEYmxYIykQBfXb = NECAaWUrFGIXcLimrerEYmxYIykQBfXb.transpose(1, 2).view(oKoLNmqMHsUubaMUUnyDFEgClwoExDJu, rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.ImrGjiFVgoYlstXoXVYKbphbCLYUVMTp, x_size[0], x_size[1])  
        return NECAaWUrFGIXcLimrerEYmxYIykQBfXb
    def epXNvUYhxcvAnkNxLYKoeNLGkQZyoeec(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS):
        epXNvUYhxcvAnkNxLYKoeNLGkQZyoeec = 0
        return epXNvUYhxcvAnkNxLYKoeNLGkQZyoeec
class kjruhryvXAQxnjJDeOXqTJbBrTkRFQSk(nn.Sequential):
    def __init__(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, xmbXivThLFnawFPAJvIDBztziWsaDyEE, num_feat):
        FTosLGldclAzaiNbwuLMIEtXfrZQpTnU = []
        if (xmbXivThLFnawFPAJvIDBztziWsaDyEE & (xmbXivThLFnawFPAJvIDBztziWsaDyEE - 1)) == 0:  
            for _ in range(int(math.DJwhOGBaLcOjmXnuwXMXOyhMtknqkKXL(xmbXivThLFnawFPAJvIDBztziWsaDyEE, 2))):
                FTosLGldclAzaiNbwuLMIEtXfrZQpTnU.append(nn.LcFcvNeYCKrBHlNkoWrkqdbxdkNCJBBK(num_feat, 4 * num_feat, 3, 1, 1))
                FTosLGldclAzaiNbwuLMIEtXfrZQpTnU.append(nn.PixelShuffle(2))
        elif xmbXivThLFnawFPAJvIDBztziWsaDyEE == 3:
            FTosLGldclAzaiNbwuLMIEtXfrZQpTnU.append(nn.LcFcvNeYCKrBHlNkoWrkqdbxdkNCJBBK(num_feat, 9 * num_feat, 3, 1, 1))
            FTosLGldclAzaiNbwuLMIEtXfrZQpTnU.append(nn.PixelShuffle(3))
        else:
            raise ValueError(
                f"scale {scale} is not supported. " "Supported scales: 2^n and 3."
            )
        super(kjruhryvXAQxnjJDeOXqTJbBrTkRFQSk, rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS).__init__(*FTosLGldclAzaiNbwuLMIEtXfrZQpTnU)
class VgiPcdFmOGbVykMkVjJgYVmmCBCJZMQH(nn.Sequential):
    def __init__(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, xmbXivThLFnawFPAJvIDBztziWsaDyEE, num_feat, num_out_ch, IONObgzScAvEgELMQbHyEzZqOHcvcOTg=None):
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.num_feat = num_feat
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.IONObgzScAvEgELMQbHyEzZqOHcvcOTg = IONObgzScAvEgELMQbHyEzZqOHcvcOTg
        FTosLGldclAzaiNbwuLMIEtXfrZQpTnU = []
        FTosLGldclAzaiNbwuLMIEtXfrZQpTnU.append(nn.LcFcvNeYCKrBHlNkoWrkqdbxdkNCJBBK(num_feat, (xmbXivThLFnawFPAJvIDBztziWsaDyEE**2) * num_out_ch, 3, 1, 1))
        FTosLGldclAzaiNbwuLMIEtXfrZQpTnU.append(nn.PixelShuffle(xmbXivThLFnawFPAJvIDBztziWsaDyEE))
        super(VgiPcdFmOGbVykMkVjJgYVmmCBCJZMQH, rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS).__init__(*FTosLGldclAzaiNbwuLMIEtXfrZQpTnU)
    def epXNvUYhxcvAnkNxLYKoeNLGkQZyoeec(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS):
        gFdyNTfDqQDeXijWZEnTSFKJXHMWaEiV, vFYBIMOEtqWwjvpBeeDFaIqTrgSbzULJ = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.IONObgzScAvEgELMQbHyEzZqOHcvcOTg  
        epXNvUYhxcvAnkNxLYKoeNLGkQZyoeec = gFdyNTfDqQDeXijWZEnTSFKJXHMWaEiV * vFYBIMOEtqWwjvpBeeDFaIqTrgSbzULJ * rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.num_feat * 3 * 9
        return epXNvUYhxcvAnkNxLYKoeNLGkQZyoeec
class AChYplcoYnbIdhsQFtwgdTUvUiOViJYb(nn.Module):
    r"""AChYplcoYnbIdhsQFtwgdTUvUiOViJYb
        A PyTorch impl of : `AChYplcoYnbIdhsQFtwgdTUvUiOViJYb: Image Restoration Using Swin Transformer`, based on Swin Transformer.
    Args:
        FRfCpqDfnuqJOdWObzdWdyzDuFpQbGQE (int | tuple(int)): Input eLyJtroPthPCROYWyMphoIrGatNOOXCO vqDBJgidQufnKyAltPYRqiKGjmztArDJ. Default 64
        HtvgnwOLVGNIRZoncKchqGwewNWrcyOO (int | tuple(int)): Patch vqDBJgidQufnKyAltPYRqiKGjmztArDJ. Default: 1
        RnQeJtCTKIYBykxuudjZsYNxhhDUcfst (int): Number of input eLyJtroPthPCROYWyMphoIrGatNOOXCO channels. Default: 3
        ImrGjiFVgoYlstXoXVYKbphbCLYUVMTp (int): Patch FPlsdAwlwymuCRSvDfaEeNjwKAgUwgXu dimension. Default: 96
        depths (tuple(int)): Depth of each Swin Transformer rmOubEJgfxmJuwTevhKPPVPDYGHXWRFZ.
        WbSAuusmaEgbrureofeJezeXtfsVoscC (tuple(int)): Number of psnGIaaNNBTQhtdDvLAOAncJBcOCafNn QEnKImSSxUuBDHahcSgvZCYYpzjKVrVk in different YLFvlrIxIOsplmnxmtPcOLtJTpiskWMv.
        nutobJTmWCYYpulsyYOoRWLklenNVeiu (int): Window vqDBJgidQufnKyAltPYRqiKGjmztArDJ. Default: 7
        uDdUvEneYSYoIevRgfdDqvFctrSBFezp (float): Ratio of mlp hidden yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ FPlsdAwlwymuCRSvDfaEeNjwKAgUwgXu yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk. Default: 4
        uGtxGIAnzLWWZnlGFIWJvzLZRYfyFdwT (bool): If True, add GlZreLQjBCiBptpFgmbsMbhjFlMgPVav learnable PvdyIPYzYuxTGYQjZbTucTrRGHTQkavB sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ oFxedobBnFbKeewIgTfUgblKziGvmndF, nyrzKxQtioheHIZujafABgijbCjrWhBU, GXNVXDlnsSLzkmussBPoJXgJwuXIiwsc. Default: True
        cXlznDgkSQpxQLziPvmTAyhhxVhSDLoV (float): Override default qk xmbXivThLFnawFPAJvIDBztziWsaDyEE of RJpLGjEjPRhDVOaBfeDFMOtajBlLriPe ** -0.5 if set. Default: None
        drop_rate (float): Dropout rate. Default: 0
        attn_drop_rate (float): Attention kcIxGCXrUvsLPSfmGoULGFzAthVmTXcA rate. Default: 0
        drop_path_rate (float): Stochastic JtnlCSDzHOgtbZVTfQMidKPjmOFZfzZX rate. Default: 0.1
        LSMbVVMwSksHBLrtUDiFhcEHyPIDcKoh (nn.Module): Normalization rmOubEJgfxmJuwTevhKPPVPDYGHXWRFZ. Default: nn.SeaDiaiECtgJbgiExWzpSnrizTosOUam.
        ape (bool): If True, add absolute position FPlsdAwlwymuCRSvDfaEeNjwKAgUwgXu sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ the YBkyOiHLPkzbgIAzSqhyviJVGfxblkPn FPlsdAwlwymuCRSvDfaEeNjwKAgUwgXu. Default: False
        patch_norm (bool): If True, add DvCWYnpMIBQxXcLuPCRaTuuQvPYPGGWh after YBkyOiHLPkzbgIAzSqhyviJVGfxblkPn FPlsdAwlwymuCRSvDfaEeNjwKAgUwgXu. Default: True
        TkHgGRFhDYRqyKuFvQRlKbpOBXUaEDVU (bool): Whether sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ use checkpointing sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ PXhZDpeqZAdDBfrowpMPOPAWwzXhVAFM memory. Default: False
        VFbOpUjlPHhNgAvxtBCPRqDCJyPQDVlx: Upscale ZOCdfHhxSDyKGnmTCFXPxBveAfxLOShd. 2/3/4/8 for eLyJtroPthPCROYWyMphoIrGatNOOXCO SR, 1 for denoising and compress artifact reduction
        img_range: Image range. 1. or 255.
        upsampler: The reconstruction reconstruction FRIBQCDfDDxIonplwxvPCicvOmmOgYPC. 'pixelshuffle'/'pixelshuffledirect'/'nearest+conv'/None
        afjLwgjwIXGXlqqPLRgZmElxkEvNNGqp: The convolutional lPmJfojDSUTFirrgKPryiJRYyZOFajzZ before RJgGCfauvfBVooxMlJcnrJywZAxzDscI connection. '1conv'/'3conv'
