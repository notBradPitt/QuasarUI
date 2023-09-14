    From: https://github.com/rwightman/pytorch-eLyJtroPthPCROYWyMphoIrGatNOOXCO-models/blob/master/timm/models/YLFvlrIxIOsplmnxmtPcOLtJTpiskWMv/UopxEzgpVJqkfTBuNkdEmNLRqPMUWpUu.py
    From: https://github.com/rwightman/pytorch-eLyJtroPthPCROYWyMphoIrGatNOOXCO-models/blob/master/timm/models/YLFvlrIxIOsplmnxmtPcOLtJTpiskWMv/UopxEzgpVJqkfTBuNkdEmNLRqPMUWpUu.py
    Args:
        num_feat (int): Channel FCVsdRzGunasBiYAXHkNdLEMUdcXuHLD of intermediate pCLwRAgBLFqTliMnElfbAlRRHMihRlVI.
        LiZKhZZsFazwePLQQesGDtcMWqqGyDeP (int): Channel squeeze ZOCdfHhxSDyKGnmTCFXPxBveAfxLOShd. Default: 16.
    Args:
        NECAaWUrFGIXcLimrerEYmxYIykQBfXb: (b, xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab, AeIrbRXDkpZlClJGwzMknCltTQQdmhvu, cjHIelcAqVoHWdLcgzuZiBumKNTVADsY)
        nutobJTmWCYYpulsyYOoRWLklenNVeiu (int): window vqDBJgidQufnKyAltPYRqiKGjmztArDJ
    Returns:
        windows: (num_windows*b, nutobJTmWCYYpulsyYOoRWLklenNVeiu, nutobJTmWCYYpulsyYOoRWLklenNVeiu, cjHIelcAqVoHWdLcgzuZiBumKNTVADsY)
    Args:
        windows: (num_windows*b, nutobJTmWCYYpulsyYOoRWLklenNVeiu, nutobJTmWCYYpulsyYOoRWLklenNVeiu, cjHIelcAqVoHWdLcgzuZiBumKNTVADsY)
        nutobJTmWCYYpulsyYOoRWLklenNVeiu (int): Window vqDBJgidQufnKyAltPYRqiKGjmztArDJ
        xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab (int): Height of eLyJtroPthPCROYWyMphoIrGatNOOXCO
        AeIrbRXDkpZlClJGwzMknCltTQQdmhvu (int): Width of eLyJtroPthPCROYWyMphoIrGatNOOXCO
    Returns:
        NECAaWUrFGIXcLimrerEYmxYIykQBfXb: (b, xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab, AeIrbRXDkpZlClJGwzMknCltTQQdmhvu, cjHIelcAqVoHWdLcgzuZiBumKNTVADsY)
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
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.unQNqNyaXZtDbRPdnrUuajLjwVMuGeHZ = nn.DhMcMyEvvzmWIEJojbQeGHlzfZKiPzHO(yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk, yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk * 3, PvdyIPYzYuxTGYQjZbTucTrRGHTQkavB=uGtxGIAnzLWWZnlGFIWJvzLZRYfyFdwT)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.tGJGoWYafTzhRETOOrClZjPpgXFZUOzU = nn.Dropout(tGJGoWYafTzhRETOOrClZjPpgXFZUOzU)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.proj = nn.DhMcMyEvvzmWIEJojbQeGHlzfZKiPzHO(yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk, yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.hjPwvODBKgggBiPujNmVDnfSDUrbQIXL = nn.Dropout(hjPwvODBKgggBiPujNmVDnfSDUrbQIXL)
        trunc_normal_(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.psppIXxCSyAsmPWaeuPeRLTPCwLBFIOe, fOYIxmVRkbmqKCdAjhgqqAEkLdJvKBVd=0.02)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.softmax = nn.Softmax(yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk=-1)
    def lqBgIcSWZYylbCPjXksJWDguuSOqoPCJ(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, NECAaWUrFGIXcLimrerEYmxYIykQBfXb, rpi, KHpRlHOzblljQyskecSxzUuWZtneWwta=None):
        nSBsnvOKnUAhaYQQLidMDejxIolzcDtg, zXHJFiFFvWqeQIAxyaTGMUgoRaHrYzjK, cjHIelcAqVoHWdLcgzuZiBumKNTVADsY = NECAaWUrFGIXcLimrerEYmxYIykQBfXb.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg
        unQNqNyaXZtDbRPdnrUuajLjwVMuGeHZ = (
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.unQNqNyaXZtDbRPdnrUuajLjwVMuGeHZ(NECAaWUrFGIXcLimrerEYmxYIykQBfXb)
            .reshape(nSBsnvOKnUAhaYQQLidMDejxIolzcDtg, zXHJFiFFvWqeQIAxyaTGMUgoRaHrYzjK, 3, rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.WbSAuusmaEgbrureofeJezeXtfsVoscC, cjHIelcAqVoHWdLcgzuZiBumKNTVADsY // rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.WbSAuusmaEgbrureofeJezeXtfsVoscC)
            .permute(2, 0, 3, 1, 4)
        )
        mxaMgfLZUDPObiqkdCgHnnARjBNVGQnh, EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm, powGafreWfwlSAqPpTpUhFgpFVqCPavl = (
            unQNqNyaXZtDbRPdnrUuajLjwVMuGeHZ[0],
            unQNqNyaXZtDbRPdnrUuajLjwVMuGeHZ[1],
            unQNqNyaXZtDbRPdnrUuajLjwVMuGeHZ[2],
        )  
        mxaMgfLZUDPObiqkdCgHnnARjBNVGQnh = mxaMgfLZUDPObiqkdCgHnnARjBNVGQnh * rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.xmbXivThLFnawFPAJvIDBztziWsaDyEE
        tUmudCfKVwpeKVqJPkVQAwLriIrTDLbW = mxaMgfLZUDPObiqkdCgHnnARjBNVGQnh @ EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm.transpose(-2, -1)
        QknDLfOPGxCnhgwlIhYUagKdzScsoXIB = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.psppIXxCSyAsmPWaeuPeRLTPCwLBFIOe[rpi.view(-1)].view(
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.nutobJTmWCYYpulsyYOoRWLklenNVeiu[0] * rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.nutobJTmWCYYpulsyYOoRWLklenNVeiu[1],
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.nutobJTmWCYYpulsyYOoRWLklenNVeiu[0] * rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.nutobJTmWCYYpulsyYOoRWLklenNVeiu[1],
            -1,
        )  
        QknDLfOPGxCnhgwlIhYUagKdzScsoXIB = QknDLfOPGxCnhgwlIhYUagKdzScsoXIB.permute(
            2, 0, 1
        ).contiguous()  
        tUmudCfKVwpeKVqJPkVQAwLriIrTDLbW = tUmudCfKVwpeKVqJPkVQAwLriIrTDLbW + QknDLfOPGxCnhgwlIhYUagKdzScsoXIB.unsqueeze(0)
        if KHpRlHOzblljQyskecSxzUuWZtneWwta is not None:
            XgdTFfZdOeDRBGreHHBZVLSeyGMsztWM = KHpRlHOzblljQyskecSxzUuWZtneWwta.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[0]
            tUmudCfKVwpeKVqJPkVQAwLriIrTDLbW = tUmudCfKVwpeKVqJPkVQAwLriIrTDLbW.view(nSBsnvOKnUAhaYQQLidMDejxIolzcDtg // XgdTFfZdOeDRBGreHHBZVLSeyGMsztWM, XgdTFfZdOeDRBGreHHBZVLSeyGMsztWM, rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.WbSAuusmaEgbrureofeJezeXtfsVoscC, zXHJFiFFvWqeQIAxyaTGMUgoRaHrYzjK, zXHJFiFFvWqeQIAxyaTGMUgoRaHrYzjK) + KHpRlHOzblljQyskecSxzUuWZtneWwta.unsqueeze(
                1
            ).unsqueeze(0)
            tUmudCfKVwpeKVqJPkVQAwLriIrTDLbW = tUmudCfKVwpeKVqJPkVQAwLriIrTDLbW.view(-1, rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.WbSAuusmaEgbrureofeJezeXtfsVoscC, zXHJFiFFvWqeQIAxyaTGMUgoRaHrYzjK, zXHJFiFFvWqeQIAxyaTGMUgoRaHrYzjK)
            tUmudCfKVwpeKVqJPkVQAwLriIrTDLbW = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.softmax(tUmudCfKVwpeKVqJPkVQAwLriIrTDLbW)
        else:
            tUmudCfKVwpeKVqJPkVQAwLriIrTDLbW = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.softmax(tUmudCfKVwpeKVqJPkVQAwLriIrTDLbW)
        tUmudCfKVwpeKVqJPkVQAwLriIrTDLbW = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.tGJGoWYafTzhRETOOrClZjPpgXFZUOzU(tUmudCfKVwpeKVqJPkVQAwLriIrTDLbW)
        NECAaWUrFGIXcLimrerEYmxYIykQBfXb = (tUmudCfKVwpeKVqJPkVQAwLriIrTDLbW @ powGafreWfwlSAqPpTpUhFgpFVqCPavl).transpose(1, 2).reshape(nSBsnvOKnUAhaYQQLidMDejxIolzcDtg, zXHJFiFFvWqeQIAxyaTGMUgoRaHrYzjK, cjHIelcAqVoHWdLcgzuZiBumKNTVADsY)
        NECAaWUrFGIXcLimrerEYmxYIykQBfXb = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.proj(NECAaWUrFGIXcLimrerEYmxYIykQBfXb)
        NECAaWUrFGIXcLimrerEYmxYIykQBfXb = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.hjPwvODBKgggBiPujNmVDnfSDUrbQIXL(NECAaWUrFGIXcLimrerEYmxYIykQBfXb)
        return NECAaWUrFGIXcLimrerEYmxYIykQBfXb
class GqUiSbLwwnomEgKLhHNfKuOgXhffeazX(nn.Module):
    r"""Hybrid Attention BTYbrqbRvGGOjbsUzDMkWIBzNvOJUbif.
    Args:
        yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk (int): Number of input channels.
        IONObgzScAvEgELMQbHyEzZqOHcvcOTg (tuple[int]): Input BcSwNQTmUGuqaESGKyPNIfMVGtVTPcEr.
        WbSAuusmaEgbrureofeJezeXtfsVoscC (int): Number of psnGIaaNNBTQhtdDvLAOAncJBcOCafNn QEnKImSSxUuBDHahcSgvZCYYpzjKVrVk.
        nutobJTmWCYYpulsyYOoRWLklenNVeiu (int): Window vqDBJgidQufnKyAltPYRqiKGjmztArDJ.
        VxEFwqRUZKQIODDttRLPjJQWwjYKIRso (int): Shift vqDBJgidQufnKyAltPYRqiKGjmztArDJ for SW-MSA.
        uDdUvEneYSYoIevRgfdDqvFctrSBFezp (float): Ratio of mlp hidden yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ FPlsdAwlwymuCRSvDfaEeNjwKAgUwgXu yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk.
        uGtxGIAnzLWWZnlGFIWJvzLZRYfyFdwT (bool, optional): If True, add GlZreLQjBCiBptpFgmbsMbhjFlMgPVav learnable PvdyIPYzYuxTGYQjZbTucTrRGHTQkavB sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ oFxedobBnFbKeewIgTfUgblKziGvmndF, nyrzKxQtioheHIZujafABgijbCjrWhBU, GXNVXDlnsSLzkmussBPoJXgJwuXIiwsc. Default: True
        cXlznDgkSQpxQLziPvmTAyhhxVhSDLoV (float | None, optional): Override zKvTEPbGDoRBsQSYYaddQKLTFDorvdms qk xmbXivThLFnawFPAJvIDBztziWsaDyEE of RJpLGjEjPRhDVOaBfeDFMOtajBlLriPe ** -0.5 if set.
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
        xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab, AeIrbRXDkpZlClJGwzMknCltTQQdmhvu = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.IONObgzScAvEgELMQbHyEzZqOHcvcOTg
        b, KLnrrxhFcKEWWKNviHswhOaKZOTqqZFL, cjHIelcAqVoHWdLcgzuZiBumKNTVADsY = NECAaWUrFGIXcLimrerEYmxYIykQBfXb.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg
        assert KLnrrxhFcKEWWKNviHswhOaKZOTqqZFL == xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab * AeIrbRXDkpZlClJGwzMknCltTQQdmhvu, "input feature has wrong size"
        assert xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab % 2 == 0 and AeIrbRXDkpZlClJGwzMknCltTQQdmhvu % 2 == 0, f"x size ({h}*{w}) are not even."
        NECAaWUrFGIXcLimrerEYmxYIykQBfXb = NECAaWUrFGIXcLimrerEYmxYIykQBfXb.view(b, xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab, AeIrbRXDkpZlClJGwzMknCltTQQdmhvu, cjHIelcAqVoHWdLcgzuZiBumKNTVADsY)
        UBGvtPbFIPlcsBIwyWKuWMZeENGLMRAP = NECAaWUrFGIXcLimrerEYmxYIykQBfXb[:, 0::2, 0::2, :]  
        bokMHjGiefHKvQcAiJMaHIIOvPogwgnt = NECAaWUrFGIXcLimrerEYmxYIykQBfXb[:, 1::2, 0::2, :]  
        qRYyQjEAGRjtIxticvyLLasWEAHJzJrD = NECAaWUrFGIXcLimrerEYmxYIykQBfXb[:, 0::2, 1::2, :]  
        bhIpxBXekbOHXwSyfdqKHptgjtkdVVmj = NECAaWUrFGIXcLimrerEYmxYIykQBfXb[:, 1::2, 1::2, :]  
        NECAaWUrFGIXcLimrerEYmxYIykQBfXb = torch.cat([UBGvtPbFIPlcsBIwyWKuWMZeENGLMRAP, bokMHjGiefHKvQcAiJMaHIIOvPogwgnt, qRYyQjEAGRjtIxticvyLLasWEAHJzJrD, bhIpxBXekbOHXwSyfdqKHptgjtkdVVmj], -1)  
        NECAaWUrFGIXcLimrerEYmxYIykQBfXb = NECAaWUrFGIXcLimrerEYmxYIykQBfXb.view(b, -1, 4 * cjHIelcAqVoHWdLcgzuZiBumKNTVADsY)  
        NECAaWUrFGIXcLimrerEYmxYIykQBfXb = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.norm(NECAaWUrFGIXcLimrerEYmxYIykQBfXb)
        NECAaWUrFGIXcLimrerEYmxYIykQBfXb = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.reduction(NECAaWUrFGIXcLimrerEYmxYIykQBfXb)
        return NECAaWUrFGIXcLimrerEYmxYIykQBfXb
class TsQmkzXYrRBMOljjmgdPloPPXrnVzshu(nn.Module):
    def __init__(
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS,
        yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk,
        IONObgzScAvEgELMQbHyEzZqOHcvcOTg,
        nutobJTmWCYYpulsyYOoRWLklenNVeiu,
        dnKRezjaTeCUtAByzJojuBQwejygJHMX,
        WbSAuusmaEgbrureofeJezeXtfsVoscC,
        uGtxGIAnzLWWZnlGFIWJvzLZRYfyFdwT=True,
        cXlznDgkSQpxQLziPvmTAyhhxVhSDLoV=None,
        uDdUvEneYSYoIevRgfdDqvFctrSBFezp=2,
        LSMbVVMwSksHBLrtUDiFhcEHyPIDcKoh=nn.SeaDiaiECtgJbgiExWzpSnrizTosOUam,
    ):
        super().__init__()
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk = yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.IONObgzScAvEgELMQbHyEzZqOHcvcOTg = IONObgzScAvEgELMQbHyEzZqOHcvcOTg
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.nutobJTmWCYYpulsyYOoRWLklenNVeiu = nutobJTmWCYYpulsyYOoRWLklenNVeiu
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.WbSAuusmaEgbrureofeJezeXtfsVoscC = WbSAuusmaEgbrureofeJezeXtfsVoscC
        RJpLGjEjPRhDVOaBfeDFMOtajBlLriPe = yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk // WbSAuusmaEgbrureofeJezeXtfsVoscC
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.xmbXivThLFnawFPAJvIDBztziWsaDyEE = cXlznDgkSQpxQLziPvmTAyhhxVhSDLoV or RJpLGjEjPRhDVOaBfeDFMOtajBlLriPe**-0.5
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.overlap_win_size = int(nutobJTmWCYYpulsyYOoRWLklenNVeiu * dnKRezjaTeCUtAByzJojuBQwejygJHMX) + nutobJTmWCYYpulsyYOoRWLklenNVeiu
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.norm1 = LSMbVVMwSksHBLrtUDiFhcEHyPIDcKoh(yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.unQNqNyaXZtDbRPdnrUuajLjwVMuGeHZ = nn.DhMcMyEvvzmWIEJojbQeGHlzfZKiPzHO(yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk, yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk * 3, PvdyIPYzYuxTGYQjZbTucTrRGHTQkavB=uGtxGIAnzLWWZnlGFIWJvzLZRYfyFdwT)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.unfold = nn.Unfold(
            aBEJjpEOpoRJYkulwSmukddEYErxRnAG=(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.overlap_win_size, rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.overlap_win_size),
            NTEWXstfzqNXGESmGkQNFWBaQsGAPlGd=nutobJTmWCYYpulsyYOoRWLklenNVeiu,
            sdxdTSjnkAOjlGmltQHvLiHRDstMzpAP=(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.overlap_win_size - nutobJTmWCYYpulsyYOoRWLklenNVeiu) // 2,
        )
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.psppIXxCSyAsmPWaeuPeRLTPCwLBFIOe = nn.Parameter(  
            torch.zeros(
                (nutobJTmWCYYpulsyYOoRWLklenNVeiu + rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.overlap_win_size - 1)
                * (nutobJTmWCYYpulsyYOoRWLklenNVeiu + rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.overlap_win_size - 1),
                WbSAuusmaEgbrureofeJezeXtfsVoscC,
            )
        )  
        trunc_normal_(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.psppIXxCSyAsmPWaeuPeRLTPCwLBFIOe, fOYIxmVRkbmqKCdAjhgqqAEkLdJvKBVd=0.02)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.softmax = nn.Softmax(yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk=-1)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.proj = nn.DhMcMyEvvzmWIEJojbQeGHlzfZKiPzHO(yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk, yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.norm2 = LSMbVVMwSksHBLrtUDiFhcEHyPIDcKoh(yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk)
        AgVLHsFcpvxzlIDWhXfNAagsKzwzXdZw = int(yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk * uDdUvEneYSYoIevRgfdDqvFctrSBFezp)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.mlp = Mlp(
            CaDEyeKgggeATJmmSMQfpwrQVIOWCNYZ=yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk, hidden_features=AgVLHsFcpvxzlIDWhXfNAagsKzwzXdZw, act_layer=nn.GELU
        )
    def lqBgIcSWZYylbCPjXksJWDguuSOqoPCJ(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, NECAaWUrFGIXcLimrerEYmxYIykQBfXb, x_size, rpi):
        xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab, AeIrbRXDkpZlClJGwzMknCltTQQdmhvu = x_size
        b, _, cjHIelcAqVoHWdLcgzuZiBumKNTVADsY = NECAaWUrFGIXcLimrerEYmxYIykQBfXb.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg
        IjbhbOkuGHrZMFVKtXhqMhaWNIzHfvwF = NECAaWUrFGIXcLimrerEYmxYIykQBfXb
        NECAaWUrFGIXcLimrerEYmxYIykQBfXb = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.norm1(NECAaWUrFGIXcLimrerEYmxYIykQBfXb)
        NECAaWUrFGIXcLimrerEYmxYIykQBfXb = NECAaWUrFGIXcLimrerEYmxYIykQBfXb.view(b, xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab, AeIrbRXDkpZlClJGwzMknCltTQQdmhvu, cjHIelcAqVoHWdLcgzuZiBumKNTVADsY)
        unQNqNyaXZtDbRPdnrUuajLjwVMuGeHZ = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.unQNqNyaXZtDbRPdnrUuajLjwVMuGeHZ(NECAaWUrFGIXcLimrerEYmxYIykQBfXb).reshape(b, xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab, AeIrbRXDkpZlClJGwzMknCltTQQdmhvu, 3, cjHIelcAqVoHWdLcgzuZiBumKNTVADsY).permute(3, 0, 4, 1, 2)  
        mxaMgfLZUDPObiqkdCgHnnARjBNVGQnh = unQNqNyaXZtDbRPdnrUuajLjwVMuGeHZ[0].permute(0, 2, 3, 1)  
        VcpuTZvtVErYxSXygBhosTALNwLHJXun = torch.cat((unQNqNyaXZtDbRPdnrUuajLjwVMuGeHZ[1], unQNqNyaXZtDbRPdnrUuajLjwVMuGeHZ[2]), yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk=1)  
        TpIRLkiMsqAoiGiAAgFBffKzeyRIFcuq = window_partition(
            mxaMgfLZUDPObiqkdCgHnnARjBNVGQnh, rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.nutobJTmWCYYpulsyYOoRWLklenNVeiu
        )  
        TpIRLkiMsqAoiGiAAgFBffKzeyRIFcuq = TpIRLkiMsqAoiGiAAgFBffKzeyRIFcuq.view(
            -1, rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.nutobJTmWCYYpulsyYOoRWLklenNVeiu * rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.nutobJTmWCYYpulsyYOoRWLklenNVeiu, cjHIelcAqVoHWdLcgzuZiBumKNTVADsY
        )  
        xmLNhWcbErGBKRLdpWnBZGZxIioKhuzJ = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.unfold(VcpuTZvtVErYxSXygBhosTALNwLHJXun)  
        xmLNhWcbErGBKRLdpWnBZGZxIioKhuzJ = rearrange(
            xmLNhWcbErGBKRLdpWnBZGZxIioKhuzJ,
            "b (nc ch owh oww) nw -> nc (b nw) (owh oww) ch",
            SPKuTOwasLAlPwlgOWdrcoOQjpyXyMLo=2,
            PCiQtOeHrYsokBqtFxBbpDPnOjZourbJ=cjHIelcAqVoHWdLcgzuZiBumKNTVADsY,
            pMkYYohnGmaLdpaRsZkmWkFTlhYrPvHe=rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.overlap_win_size,
            epPXPyOzqkHBmWxuwWCIlOVInymnzPBX=rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.overlap_win_size,
        ).contiguous()  
        GGjanssYJXyfXoOZvaiPKNxPVqzUyhtN, MkZgsHoWSluTusIunXpPrfWmfZrDPerp = xmLNhWcbErGBKRLdpWnBZGZxIioKhuzJ[0], xmLNhWcbErGBKRLdpWnBZGZxIioKhuzJ[1]  
        nSBsnvOKnUAhaYQQLidMDejxIolzcDtg, DobKLVNICVeQHvCzbKAWHWsEoUAngmGQ, _ = TpIRLkiMsqAoiGiAAgFBffKzeyRIFcuq.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg
        _, zXHJFiFFvWqeQIAxyaTGMUgoRaHrYzjK, _ = GGjanssYJXyfXoOZvaiPKNxPVqzUyhtN.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg
        TXGwYXNLgQsYzfHHpRBDJGFCFZEClzIo = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk // rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.WbSAuusmaEgbrureofeJezeXtfsVoscC
        mxaMgfLZUDPObiqkdCgHnnARjBNVGQnh = TpIRLkiMsqAoiGiAAgFBffKzeyRIFcuq.reshape(nSBsnvOKnUAhaYQQLidMDejxIolzcDtg, DobKLVNICVeQHvCzbKAWHWsEoUAngmGQ, rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.WbSAuusmaEgbrureofeJezeXtfsVoscC, TXGwYXNLgQsYzfHHpRBDJGFCFZEClzIo).permute(
            0, 2, 1, 3
        )  
        EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm = GGjanssYJXyfXoOZvaiPKNxPVqzUyhtN.reshape(nSBsnvOKnUAhaYQQLidMDejxIolzcDtg, zXHJFiFFvWqeQIAxyaTGMUgoRaHrYzjK, rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.WbSAuusmaEgbrureofeJezeXtfsVoscC, TXGwYXNLgQsYzfHHpRBDJGFCFZEClzIo).permute(
            0, 2, 1, 3
        )  
        powGafreWfwlSAqPpTpUhFgpFVqCPavl = MkZgsHoWSluTusIunXpPrfWmfZrDPerp.reshape(nSBsnvOKnUAhaYQQLidMDejxIolzcDtg, zXHJFiFFvWqeQIAxyaTGMUgoRaHrYzjK, rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.WbSAuusmaEgbrureofeJezeXtfsVoscC, TXGwYXNLgQsYzfHHpRBDJGFCFZEClzIo).permute(
            0, 2, 1, 3
        )  
        mxaMgfLZUDPObiqkdCgHnnARjBNVGQnh = mxaMgfLZUDPObiqkdCgHnnARjBNVGQnh * rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.xmbXivThLFnawFPAJvIDBztziWsaDyEE
        tUmudCfKVwpeKVqJPkVQAwLriIrTDLbW = mxaMgfLZUDPObiqkdCgHnnARjBNVGQnh @ EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm.transpose(-2, -1)
        QknDLfOPGxCnhgwlIhYUagKdzScsoXIB = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.psppIXxCSyAsmPWaeuPeRLTPCwLBFIOe[rpi.view(-1)].view(
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.nutobJTmWCYYpulsyYOoRWLklenNVeiu * rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.nutobJTmWCYYpulsyYOoRWLklenNVeiu,
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.overlap_win_size * rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.overlap_win_size,
            -1,
        )  
        QknDLfOPGxCnhgwlIhYUagKdzScsoXIB = QknDLfOPGxCnhgwlIhYUagKdzScsoXIB.permute(
            2, 0, 1
        ).contiguous()  
        tUmudCfKVwpeKVqJPkVQAwLriIrTDLbW = tUmudCfKVwpeKVqJPkVQAwLriIrTDLbW + QknDLfOPGxCnhgwlIhYUagKdzScsoXIB.unsqueeze(0)
        tUmudCfKVwpeKVqJPkVQAwLriIrTDLbW = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.softmax(tUmudCfKVwpeKVqJPkVQAwLriIrTDLbW)
        JpoCIOUQIqcQcNjbmukDZyYfkaaRBEux = (tUmudCfKVwpeKVqJPkVQAwLriIrTDLbW @ powGafreWfwlSAqPpTpUhFgpFVqCPavl).transpose(1, 2).reshape(nSBsnvOKnUAhaYQQLidMDejxIolzcDtg, DobKLVNICVeQHvCzbKAWHWsEoUAngmGQ, rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk)
        JpoCIOUQIqcQcNjbmukDZyYfkaaRBEux = JpoCIOUQIqcQcNjbmukDZyYfkaaRBEux.view(
            -1, rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.nutobJTmWCYYpulsyYOoRWLklenNVeiu, rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.nutobJTmWCYYpulsyYOoRWLklenNVeiu, rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk
        )
        NECAaWUrFGIXcLimrerEYmxYIykQBfXb = window_reverse(JpoCIOUQIqcQcNjbmukDZyYfkaaRBEux, rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.nutobJTmWCYYpulsyYOoRWLklenNVeiu, xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab, AeIrbRXDkpZlClJGwzMknCltTQQdmhvu)  
        NECAaWUrFGIXcLimrerEYmxYIykQBfXb = NECAaWUrFGIXcLimrerEYmxYIykQBfXb.view(b, xlkiANyuFAEvVUqnFyKOvZzUpSmHKjab * AeIrbRXDkpZlClJGwzMknCltTQQdmhvu, rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk)
        NECAaWUrFGIXcLimrerEYmxYIykQBfXb = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.proj(NECAaWUrFGIXcLimrerEYmxYIykQBfXb) + IjbhbOkuGHrZMFVKtXhqMhaWNIzHfvwF
        NECAaWUrFGIXcLimrerEYmxYIykQBfXb = NECAaWUrFGIXcLimrerEYmxYIykQBfXb + rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.mlp(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.norm2(NECAaWUrFGIXcLimrerEYmxYIykQBfXb))
        return NECAaWUrFGIXcLimrerEYmxYIykQBfXb
class IqpQoHkoqdHFkshbwZmeerreqIiKrgNI(nn.Module):
    def __init__(
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS,
        yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk,
        IONObgzScAvEgELMQbHyEzZqOHcvcOTg,
        JtnlCSDzHOgtbZVTfQMidKPjmOFZfzZX,
        WbSAuusmaEgbrureofeJezeXtfsVoscC,
        nutobJTmWCYYpulsyYOoRWLklenNVeiu,
        lxYdKmmEScpxJXPBOfypspvqoJfAAdnU,
        LiZKhZZsFazwePLQQesGDtcMWqqGyDeP,
        cdrQFTlIHFNYXoycDqnBVrgVmFTztAwM,
        dnKRezjaTeCUtAByzJojuBQwejygJHMX,
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
                GqUiSbLwwnomEgKLhHNfKuOgXhffeazX(
                    yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk=yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk,
                    IONObgzScAvEgELMQbHyEzZqOHcvcOTg=IONObgzScAvEgELMQbHyEzZqOHcvcOTg,
                    WbSAuusmaEgbrureofeJezeXtfsVoscC=WbSAuusmaEgbrureofeJezeXtfsVoscC,
                    nutobJTmWCYYpulsyYOoRWLklenNVeiu=nutobJTmWCYYpulsyYOoRWLklenNVeiu,
                    VxEFwqRUZKQIODDttRLPjJQWwjYKIRso=0 if (HCXmerBqIMuTscBONzTGKYapYSxWTYHo % 2 == 0) else nutobJTmWCYYpulsyYOoRWLklenNVeiu // 2,
                    lxYdKmmEScpxJXPBOfypspvqoJfAAdnU=lxYdKmmEScpxJXPBOfypspvqoJfAAdnU,
                    LiZKhZZsFazwePLQQesGDtcMWqqGyDeP=LiZKhZZsFazwePLQQesGDtcMWqqGyDeP,
                    cdrQFTlIHFNYXoycDqnBVrgVmFTztAwM=cdrQFTlIHFNYXoycDqnBVrgVmFTztAwM,
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
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.overlap_attn = TsQmkzXYrRBMOljjmgdPloPPXrnVzshu(
            yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk=yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk,
            IONObgzScAvEgELMQbHyEzZqOHcvcOTg=IONObgzScAvEgELMQbHyEzZqOHcvcOTg,
            nutobJTmWCYYpulsyYOoRWLklenNVeiu=nutobJTmWCYYpulsyYOoRWLklenNVeiu,
            dnKRezjaTeCUtAByzJojuBQwejygJHMX=dnKRezjaTeCUtAByzJojuBQwejygJHMX,
            WbSAuusmaEgbrureofeJezeXtfsVoscC=WbSAuusmaEgbrureofeJezeXtfsVoscC,
            uGtxGIAnzLWWZnlGFIWJvzLZRYfyFdwT=uGtxGIAnzLWWZnlGFIWJvzLZRYfyFdwT,
            cXlznDgkSQpxQLziPvmTAyhhxVhSDLoV=cXlznDgkSQpxQLziPvmTAyhhxVhSDLoV,
            uDdUvEneYSYoIevRgfdDqvFctrSBFezp=uDdUvEneYSYoIevRgfdDqvFctrSBFezp,  
            LSMbVVMwSksHBLrtUDiFhcEHyPIDcKoh=LSMbVVMwSksHBLrtUDiFhcEHyPIDcKoh,
        )
        if FNdFYgmARbySAmYyEvSINcVrOJlCpKfW is not None:
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.FNdFYgmARbySAmYyEvSINcVrOJlCpKfW = FNdFYgmARbySAmYyEvSINcVrOJlCpKfW(
                IONObgzScAvEgELMQbHyEzZqOHcvcOTg, yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk=yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk, LSMbVVMwSksHBLrtUDiFhcEHyPIDcKoh=LSMbVVMwSksHBLrtUDiFhcEHyPIDcKoh
            )
        else:
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.FNdFYgmARbySAmYyEvSINcVrOJlCpKfW = None
    def lqBgIcSWZYylbCPjXksJWDguuSOqoPCJ(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, NECAaWUrFGIXcLimrerEYmxYIykQBfXb, x_size, params):
        for LLiMCtLJBqUPDeOUdzNtdeEeLAsRdhQK in rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.blocks:
            NECAaWUrFGIXcLimrerEYmxYIykQBfXb = LLiMCtLJBqUPDeOUdzNtdeEeLAsRdhQK(NECAaWUrFGIXcLimrerEYmxYIykQBfXb, x_size, params["rpi_sa"], params["attn_mask"])
        NECAaWUrFGIXcLimrerEYmxYIykQBfXb = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.overlap_attn(NECAaWUrFGIXcLimrerEYmxYIykQBfXb, x_size, params["rpi_oca"])
        if rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.FNdFYgmARbySAmYyEvSINcVrOJlCpKfW is not None:
            NECAaWUrFGIXcLimrerEYmxYIykQBfXb = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.FNdFYgmARbySAmYyEvSINcVrOJlCpKfW(NECAaWUrFGIXcLimrerEYmxYIykQBfXb)
        return NECAaWUrFGIXcLimrerEYmxYIykQBfXb
class QIsCwvaRrcKIEfAjffdVoEONOuxnZLvl(nn.Module):
    def __init__(
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS,
        yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk,
        IONObgzScAvEgELMQbHyEzZqOHcvcOTg,
        JtnlCSDzHOgtbZVTfQMidKPjmOFZfzZX,
        WbSAuusmaEgbrureofeJezeXtfsVoscC,
        nutobJTmWCYYpulsyYOoRWLklenNVeiu,
        lxYdKmmEScpxJXPBOfypspvqoJfAAdnU,
        LiZKhZZsFazwePLQQesGDtcMWqqGyDeP,
        cdrQFTlIHFNYXoycDqnBVrgVmFTztAwM,
        dnKRezjaTeCUtAByzJojuBQwejygJHMX,
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
        super(QIsCwvaRrcKIEfAjffdVoEONOuxnZLvl, rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS).__init__()
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk = yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.IONObgzScAvEgELMQbHyEzZqOHcvcOTg = IONObgzScAvEgELMQbHyEzZqOHcvcOTg
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.residual_group = IqpQoHkoqdHFkshbwZmeerreqIiKrgNI(
            yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk=yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk,
            IONObgzScAvEgELMQbHyEzZqOHcvcOTg=IONObgzScAvEgELMQbHyEzZqOHcvcOTg,
            JtnlCSDzHOgtbZVTfQMidKPjmOFZfzZX=JtnlCSDzHOgtbZVTfQMidKPjmOFZfzZX,
            WbSAuusmaEgbrureofeJezeXtfsVoscC=WbSAuusmaEgbrureofeJezeXtfsVoscC,
            nutobJTmWCYYpulsyYOoRWLklenNVeiu=nutobJTmWCYYpulsyYOoRWLklenNVeiu,
            lxYdKmmEScpxJXPBOfypspvqoJfAAdnU=lxYdKmmEScpxJXPBOfypspvqoJfAAdnU,
            LiZKhZZsFazwePLQQesGDtcMWqqGyDeP=LiZKhZZsFazwePLQQesGDtcMWqqGyDeP,
            cdrQFTlIHFNYXoycDqnBVrgVmFTztAwM=cdrQFTlIHFNYXoycDqnBVrgVmFTztAwM,
            dnKRezjaTeCUtAByzJojuBQwejygJHMX=dnKRezjaTeCUtAByzJojuBQwejygJHMX,
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
        elif afjLwgjwIXGXlqqPLRgZmElxkEvNNGqp == "identity":
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.VRzIOXLfdDszfSOpzuKgtjeGGtXuyctm = nn.Identity()
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
    def lqBgIcSWZYylbCPjXksJWDguuSOqoPCJ(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, NECAaWUrFGIXcLimrerEYmxYIykQBfXb, x_size, params):
        return (
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.patch_embed(
                rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.VRzIOXLfdDszfSOpzuKgtjeGGtXuyctm(
                    rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.patch_unembed(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.residual_group(NECAaWUrFGIXcLimrerEYmxYIykQBfXb, x_size, params), x_size)
                )
            )
            + NECAaWUrFGIXcLimrerEYmxYIykQBfXb
        )
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
        NECAaWUrFGIXcLimrerEYmxYIykQBfXb = (
            NECAaWUrFGIXcLimrerEYmxYIykQBfXb.transpose(1, 2)
            .contiguous()
            .view(NECAaWUrFGIXcLimrerEYmxYIykQBfXb.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[0], rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.ImrGjiFVgoYlstXoXVYKbphbCLYUVMTp, x_size[0], x_size[1])
        )  
        return NECAaWUrFGIXcLimrerEYmxYIykQBfXb
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
class WZrrBddKAqJphvEwVDvykSHzWqBINdJL(nn.Module):
    r"""Hybrid Attention Transformer
        A PyTorch implementation of : `Activating More Pixels in Image Super-Resolution Transformer`.
        Some codes are based on AChYplcoYnbIdhsQFtwgdTUvUiOViJYb.
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
        cXlznDgkSQpxQLziPvmTAyhhxVhSDLoV (float): Override zKvTEPbGDoRBsQSYYaddQKLTFDorvdms qk xmbXivThLFnawFPAJvIDBztziWsaDyEE of RJpLGjEjPRhDVOaBfeDFMOtajBlLriPe ** -0.5 if set. Default: None
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
