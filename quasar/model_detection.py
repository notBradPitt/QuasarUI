from . import plerLAIlEUdlrDugwPUkpJeEHQyvYTCL
def kXWGbNfnuWSIvQgSIPsGxvMKYQjbjUsA(lKVoYdskwQoUtnPCsdhpAodWMgcWgDPz, prefix_string):
    count = 0
    while True:
        cjHIelcAqVoHWdLcgzuZiBumKNTVADsY = False
        for EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm in lKVoYdskwQoUtnPCsdhpAodWMgcWgDPz:
            if EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm.startswith(prefix_string.format(count)):
                cjHIelcAqVoHWdLcgzuZiBumKNTVADsY = True
                break
        if cjHIelcAqVoHWdLcgzuZiBumKNTVADsY == False:
            break
        count += 1
    return count
def TPovHLKrRtCbMVIJowftdMdsKYAZHlqF(TQRgUMPjEwYAaDvSuzgvheADStCoUKzT, key_prefix, HzaWhAqAbytRDBNdzYQQeTtjNGGUstsT):
    lKVoYdskwQoUtnPCsdhpAodWMgcWgDPz = list(TQRgUMPjEwYAaDvSuzgvheADStCoUKzT.keys())
    lLgbOYEeDmYyyxASAROATrPmlqgqYORG = {
        "use_checkpoint": False,
        "image_size": 32,
        "out_channels": 4,
        "use_spatial_transformer": True,
        "legacy": False
    }
    LRuCZFNLWAKRNLjshYpcxgYSrAVSORrD = '{}label_emb.0.0.weight'.format(key_prefix)
    if LRuCZFNLWAKRNLjshYpcxgYSrAVSORrD in lKVoYdskwQoUtnPCsdhpAodWMgcWgDPz:
        lLgbOYEeDmYyyxASAROATrPmlqgqYORG["num_classes"] = "sequential"
        lLgbOYEeDmYyyxASAROATrPmlqgqYORG["adm_in_channels"] = TQRgUMPjEwYAaDvSuzgvheADStCoUKzT[LRuCZFNLWAKRNLjshYpcxgYSrAVSORrD].BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[1]
    else:
        lLgbOYEeDmYyyxASAROATrPmlqgqYORG["adm_in_channels"] = None
    lLgbOYEeDmYyyxASAROATrPmlqgqYORG["use_fp16"] = HzaWhAqAbytRDBNdzYQQeTtjNGGUstsT
    rfffeowUobVqguyCFHTDeTaijHAmTODl = TQRgUMPjEwYAaDvSuzgvheADStCoUKzT['{}input_blocks.0.0.weight'.format(key_prefix)].BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[0]
    EbKSIFxpyCpzycRDApduouVsxspHzkTj = TQRgUMPjEwYAaDvSuzgvheADStCoUKzT['{}input_blocks.0.0.weight'.format(key_prefix)].BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[1]
    CCAXgmpIWICHAxdXRCbCjrvfPSDecjrB = []
    PobbJiwtnxNwnEHqwlZzMzYFDrQuLuRE = []
    fnGjYHqQPjLHiqvqzJoEFfKlYjtXwlEV = []
    mvciuYyNHMqmFhQqZCFnjvXvgTuOnAAU = []
    FEAAZHeTRQEJCsYHCOEPpfOenpVZIhNT = None
    PRCmYmLASLnRTlacrSLaZCNiipiIjyAo = False
    PggaNyPZvLSKuTUXrmAmAHWdChMlMIDe = 1
    count = 0
    xcAeAmSVIGtMHvRexXNYQctdmgitDWTF = 0
    PhRsbOOJbIqrQkgmFpxiWEHQwrRvAYRG = 0
    wUXeYucsZclpitbcuJlqaZzqjjmivAGv = 0
    while True:
        mAocOLWlgMJvPYVmSRndfhQdAcKHgPwi = '{}input_blocks.{}.'.format(key_prefix, count)
        LcRQuSckJlzqzHuFtDEfHDGMqMKtDDKW = sorted(list(filter(lambda GlZreLQjBCiBptpFgmbsMbhjFlMgPVav: GlZreLQjBCiBptpFgmbsMbhjFlMgPVav.startswith(mAocOLWlgMJvPYVmSRndfhQdAcKHgPwi), lKVoYdskwQoUtnPCsdhpAodWMgcWgDPz)))
        if len(LcRQuSckJlzqzHuFtDEfHDGMqMKtDDKW) == 0:
            break
        if "{}0.op.weight".format(mAocOLWlgMJvPYVmSRndfhQdAcKHgPwi) in LcRQuSckJlzqzHuFtDEfHDGMqMKtDDKW: 
            if PhRsbOOJbIqrQkgmFpxiWEHQwrRvAYRG > 0:
                fnGjYHqQPjLHiqvqzJoEFfKlYjtXwlEV.append(PggaNyPZvLSKuTUXrmAmAHWdChMlMIDe)
            mvciuYyNHMqmFhQqZCFnjvXvgTuOnAAU.append(PhRsbOOJbIqrQkgmFpxiWEHQwrRvAYRG)
            CCAXgmpIWICHAxdXRCbCjrvfPSDecjrB.append(xcAeAmSVIGtMHvRexXNYQctdmgitDWTF)
            PobbJiwtnxNwnEHqwlZzMzYFDrQuLuRE.append(wUXeYucsZclpitbcuJlqaZzqjjmivAGv)
            PggaNyPZvLSKuTUXrmAmAHWdChMlMIDe *= 2
            xcAeAmSVIGtMHvRexXNYQctdmgitDWTF = 0
            PhRsbOOJbIqrQkgmFpxiWEHQwrRvAYRG = 0
            wUXeYucsZclpitbcuJlqaZzqjjmivAGv = 0
        else:
            gHVNKXUIxZTZpHEDSdNbsAkiqRbSnGxg = "{}0.in_layers.0.weight".format(mAocOLWlgMJvPYVmSRndfhQdAcKHgPwi)
            if gHVNKXUIxZTZpHEDSdNbsAkiqRbSnGxg in LcRQuSckJlzqzHuFtDEfHDGMqMKtDDKW:
                xcAeAmSVIGtMHvRexXNYQctdmgitDWTF += 1
                wUXeYucsZclpitbcuJlqaZzqjjmivAGv = TQRgUMPjEwYAaDvSuzgvheADStCoUKzT["{}0.out_layers.3.weight".format(mAocOLWlgMJvPYVmSRndfhQdAcKHgPwi)].BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[0] // rfffeowUobVqguyCFHTDeTaijHAmTODl
            yIpVhLRiJPTpIRVqbcMQoVmwgjBNxplX = mAocOLWlgMJvPYVmSRndfhQdAcKHgPwi + "1.transformer_blocks."
            UzJpAcRFrfXXkpoAVAceUwOomgGXfnUN = sorted(list(filter(lambda GlZreLQjBCiBptpFgmbsMbhjFlMgPVav: GlZreLQjBCiBptpFgmbsMbhjFlMgPVav.startswith(yIpVhLRiJPTpIRVqbcMQoVmwgjBNxplX), lKVoYdskwQoUtnPCsdhpAodWMgcWgDPz)))
            if len(UzJpAcRFrfXXkpoAVAceUwOomgGXfnUN) > 0:
                PhRsbOOJbIqrQkgmFpxiWEHQwrRvAYRG = kXWGbNfnuWSIvQgSIPsGxvMKYQjbjUsA(lKVoYdskwQoUtnPCsdhpAodWMgcWgDPz, yIpVhLRiJPTpIRVqbcMQoVmwgjBNxplX + '{}')
                if FEAAZHeTRQEJCsYHCOEPpfOenpVZIhNT is None:
                    FEAAZHeTRQEJCsYHCOEPpfOenpVZIhNT = TQRgUMPjEwYAaDvSuzgvheADStCoUKzT['{}0.attn2.to_k.weight'.format(yIpVhLRiJPTpIRVqbcMQoVmwgjBNxplX)].BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[1]
                    PRCmYmLASLnRTlacrSLaZCNiipiIjyAo = len(TQRgUMPjEwYAaDvSuzgvheADStCoUKzT['{}1.proj_in.weight'.format(mAocOLWlgMJvPYVmSRndfhQdAcKHgPwi)].BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg) == 2
        count += 1
    if PhRsbOOJbIqrQkgmFpxiWEHQwrRvAYRG > 0:
        fnGjYHqQPjLHiqvqzJoEFfKlYjtXwlEV.append(PggaNyPZvLSKuTUXrmAmAHWdChMlMIDe)
    mvciuYyNHMqmFhQqZCFnjvXvgTuOnAAU.append(PhRsbOOJbIqrQkgmFpxiWEHQwrRvAYRG)
    CCAXgmpIWICHAxdXRCbCjrvfPSDecjrB.append(xcAeAmSVIGtMHvRexXNYQctdmgitDWTF)
    PobbJiwtnxNwnEHqwlZzMzYFDrQuLuRE.append(wUXeYucsZclpitbcuJlqaZzqjjmivAGv)
    bNRNtGADYHWmhhfDRZvMDNGtMgvwCBHd = kXWGbNfnuWSIvQgSIPsGxvMKYQjbjUsA(lKVoYdskwQoUtnPCsdhpAodWMgcWgDPz, '{}middle_block.1.transformer_blocks.'.format(key_prefix) + '{}')
    if len(set(CCAXgmpIWICHAxdXRCbCjrvfPSDecjrB)) == 1:
        CCAXgmpIWICHAxdXRCbCjrvfPSDecjrB = CCAXgmpIWICHAxdXRCbCjrvfPSDecjrB[0]
    if len(set(mvciuYyNHMqmFhQqZCFnjvXvgTuOnAAU)) == 1:
        mvciuYyNHMqmFhQqZCFnjvXvgTuOnAAU = mvciuYyNHMqmFhQqZCFnjvXvgTuOnAAU[0]
    lLgbOYEeDmYyyxASAROATrPmlqgqYORG["in_channels"] = EbKSIFxpyCpzycRDApduouVsxspHzkTj
    lLgbOYEeDmYyyxASAROATrPmlqgqYORG["model_channels"] = rfffeowUobVqguyCFHTDeTaijHAmTODl
    lLgbOYEeDmYyyxASAROATrPmlqgqYORG["num_res_blocks"] = CCAXgmpIWICHAxdXRCbCjrvfPSDecjrB
    lLgbOYEeDmYyyxASAROATrPmlqgqYORG["attention_resolutions"] = fnGjYHqQPjLHiqvqzJoEFfKlYjtXwlEV
    lLgbOYEeDmYyyxASAROATrPmlqgqYORG["transformer_depth"] = mvciuYyNHMqmFhQqZCFnjvXvgTuOnAAU
    lLgbOYEeDmYyyxASAROATrPmlqgqYORG["channel_mult"] = PobbJiwtnxNwnEHqwlZzMzYFDrQuLuRE
    lLgbOYEeDmYyyxASAROATrPmlqgqYORG["transformer_depth_middle"] = bNRNtGADYHWmhhfDRZvMDNGtMgvwCBHd
    lLgbOYEeDmYyyxASAROATrPmlqgqYORG['use_linear_in_transformer'] = PRCmYmLASLnRTlacrSLaZCNiipiIjyAo
    lLgbOYEeDmYyyxASAROATrPmlqgqYORG["context_dim"] = FEAAZHeTRQEJCsYHCOEPpfOenpVZIhNT
    return lLgbOYEeDmYyyxASAROATrPmlqgqYORG
def EuzsbjrrgKrTkfcBoMFZzWEywaHOxzBP(lLgbOYEeDmYyyxASAROATrPmlqgqYORG):
    for QndHjlfwhEimYkuHnNTDxkEXYaCwJdZe in plerLAIlEUdlrDugwPUkpJeEHQyvYTCL.models:
        if QndHjlfwhEimYkuHnNTDxkEXYaCwJdZe.EmdemYfqcZwKxzMFIqlEDyyJOFHcDLYk(lLgbOYEeDmYyyxASAROATrPmlqgqYORG):
            return QndHjlfwhEimYkuHnNTDxkEXYaCwJdZe(lLgbOYEeDmYyyxASAROATrPmlqgqYORG)
    print("no match", lLgbOYEeDmYyyxASAROATrPmlqgqYORG)
    return None
def VYidlmtssyLEAglEVVdSlThVhDzTSICW(TQRgUMPjEwYAaDvSuzgvheADStCoUKzT, unet_key_prefix, HzaWhAqAbytRDBNdzYQQeTtjNGGUstsT):
    lLgbOYEeDmYyyxASAROATrPmlqgqYORG = TPovHLKrRtCbMVIJowftdMdsKYAZHlqF(TQRgUMPjEwYAaDvSuzgvheADStCoUKzT, unet_key_prefix, HzaWhAqAbytRDBNdzYQQeTtjNGGUstsT)
    return EuzsbjrrgKrTkfcBoMFZzWEywaHOxzBP(lLgbOYEeDmYyyxASAROATrPmlqgqYORG)
def xySSEzFdNBmsMIgcTEsdJVqMgpLUBwLW(TQRgUMPjEwYAaDvSuzgvheADStCoUKzT, HzaWhAqAbytRDBNdzYQQeTtjNGGUstsT):
    aTtGvrcNbpJkYrNtoqbGYpIWUWDLYOBz = {}
    fnGjYHqQPjLHiqvqzJoEFfKlYjtXwlEV = []
    oNcXfoASUGnaySJgwkbBUdUiwdLrTojR = 1
    for HCXmerBqIMuTscBONzTGKYapYSxWTYHo in range(5):
        EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm = "down_blocks.{}.attentions.1.transformer_blocks.0.attn2.to_k.weight".format(HCXmerBqIMuTscBONzTGKYapYSxWTYHo)
        if EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm in TQRgUMPjEwYAaDvSuzgvheADStCoUKzT:
            aTtGvrcNbpJkYrNtoqbGYpIWUWDLYOBz["context_dim"] = TQRgUMPjEwYAaDvSuzgvheADStCoUKzT[EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm].BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[1]
            fnGjYHqQPjLHiqvqzJoEFfKlYjtXwlEV.append(oNcXfoASUGnaySJgwkbBUdUiwdLrTojR)
        oNcXfoASUGnaySJgwkbBUdUiwdLrTojR *= 2
    aTtGvrcNbpJkYrNtoqbGYpIWUWDLYOBz["attention_resolutions"] = fnGjYHqQPjLHiqvqzJoEFfKlYjtXwlEV
    aTtGvrcNbpJkYrNtoqbGYpIWUWDLYOBz["model_channels"] = TQRgUMPjEwYAaDvSuzgvheADStCoUKzT["conv_in.weight"].BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[0]
    aTtGvrcNbpJkYrNtoqbGYpIWUWDLYOBz["in_channels"] = TQRgUMPjEwYAaDvSuzgvheADStCoUKzT["conv_in.weight"].BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[1]
    aTtGvrcNbpJkYrNtoqbGYpIWUWDLYOBz["adm_in_channels"] = None
    if "class_embedding.linear_1.weight" in TQRgUMPjEwYAaDvSuzgvheADStCoUKzT:
        aTtGvrcNbpJkYrNtoqbGYpIWUWDLYOBz["adm_in_channels"] = TQRgUMPjEwYAaDvSuzgvheADStCoUKzT["class_embedding.linear_1.weight"].BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[1]
    elif "add_embedding.linear_1.weight" in TQRgUMPjEwYAaDvSuzgvheADStCoUKzT:
        aTtGvrcNbpJkYrNtoqbGYpIWUWDLYOBz["adm_in_channels"] = TQRgUMPjEwYAaDvSuzgvheADStCoUKzT["add_embedding.linear_1.weight"].BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg[1]
    hTIrchlPHYZofZJBRoQFMjAnlKwSEPlB = {'use_checkpoint': False, 'image_size': 32, 'out_channels': 4, 'use_spatial_transformer': True, 'legacy': False,
            'num_classes': 'sequential', 'adm_in_channels': 2816, 'use_fp16': HzaWhAqAbytRDBNdzYQQeTtjNGGUstsT, 'in_channels': 4, 'model_channels': 320,
            'num_res_blocks': 2, 'attention_resolutions': [2, 4], 'transformer_depth': [0, 2, 10], 'channel_mult': [1, 2, 4],
            'transformer_depth_middle': 10, 'use_linear_in_transformer': True, 'context_dim': 2048, "num_head_channels": 64}
    rKuYZDeUTMKOszHSYSIXlegaiIgSvpra = {'use_checkpoint': False, 'image_size': 32, 'out_channels': 4, 'use_spatial_transformer': True, 'legacy': False,
                    'num_classes': 'sequential', 'adm_in_channels': 2560, 'use_fp16': HzaWhAqAbytRDBNdzYQQeTtjNGGUstsT, 'in_channels': 4, 'model_channels': 384,
                    'num_res_blocks': 2, 'attention_resolutions': [2, 4], 'transformer_depth': [0, 4, 4, 0], 'channel_mult': [1, 2, 4, 4],
                    'transformer_depth_middle': 4, 'use_linear_in_transformer': True, 'context_dim': 1280, "num_head_channels": 64}
    rqacOpJSPWDNLdhfPYRxumhBdlKkTaHI = {'use_checkpoint': False, 'image_size': 32, 'out_channels': 4, 'use_spatial_transformer': True, 'legacy': False,
            'adm_in_channels': None, 'use_fp16': HzaWhAqAbytRDBNdzYQQeTtjNGGUstsT, 'in_channels': 4, 'model_channels': 320, 'num_res_blocks': 2,
            'attention_resolutions': [1, 2, 4], 'transformer_depth': [1, 1, 1, 0], 'channel_mult': [1, 2, 4, 4],
            'transformer_depth_middle': 1, 'use_linear_in_transformer': True, 'context_dim': 1024, "num_head_channels": 64}
    dpmCZvpSEHoTdKsZQMqfkcmeNjFLgqsQ = {'use_checkpoint': False, 'image_size': 32, 'out_channels': 4, 'use_spatial_transformer': True, 'legacy': False,
                    'num_classes': 'sequential', 'adm_in_channels': 2048, 'use_fp16': HzaWhAqAbytRDBNdzYQQeTtjNGGUstsT, 'in_channels': 4, 'model_channels': 320,
                    'num_res_blocks': 2, 'attention_resolutions': [1, 2, 4], 'transformer_depth': [1, 1, 1, 0], 'channel_mult': [1, 2, 4, 4],
                    'transformer_depth_middle': 1, 'use_linear_in_transformer': True, 'context_dim': 1024, "num_head_channels": 64}
    WpUdlMsnoiTiCAtAQggpjMPzQoNwAKlr = {'use_checkpoint': False, 'image_size': 32, 'out_channels': 4, 'use_spatial_transformer': True, 'legacy': False,
                    'num_classes': 'sequential', 'adm_in_channels': 1536, 'use_fp16': HzaWhAqAbytRDBNdzYQQeTtjNGGUstsT, 'in_channels': 4, 'model_channels': 320,
                    'num_res_blocks': 2, 'attention_resolutions': [1, 2, 4], 'transformer_depth': [1, 1, 1, 0], 'channel_mult': [1, 2, 4, 4],
                    'transformer_depth_middle': 1, 'use_linear_in_transformer': True, 'context_dim': 1024}
    YlEWwgaMKiTVEpSjHUNNzLiJqMZaVSZP = {'use_checkpoint': False, 'image_size': 32, 'out_channels': 4, 'use_spatial_transformer': True, 'legacy': False,
            'adm_in_channels': None, 'use_fp16': HzaWhAqAbytRDBNdzYQQeTtjNGGUstsT, 'in_channels': 4, 'model_channels': 320, 'num_res_blocks': 2,
            'attention_resolutions': [1, 2, 4], 'transformer_depth': [1, 1, 1, 0], 'channel_mult': [1, 2, 4, 4],
            'transformer_depth_middle': 1, 'use_linear_in_transformer': False, 'context_dim': 768, "num_heads": 8}
    MlRccaGYXAVvHzOUIyYEpckLNzAUehwy = {'use_checkpoint': False, 'image_size': 32, 'out_channels': 4, 'use_spatial_transformer': True, 'legacy': False,
            'num_classes': 'sequential', 'adm_in_channels': 2816, 'use_fp16': HzaWhAqAbytRDBNdzYQQeTtjNGGUstsT, 'in_channels': 4, 'model_channels': 320,
            'num_res_blocks': 2, 'attention_resolutions': [4], 'transformer_depth': [0, 0, 1], 'channel_mult': [1, 2, 4],
            'transformer_depth_middle': 1, 'use_linear_in_transformer': True, 'context_dim': 2048, "num_head_channels": 64}
    RTPtSLCHsZiCxVExECqPShLKWDRkAKGD = {'use_checkpoint': False, 'image_size': 32, 'out_channels': 4, 'use_spatial_transformer': True, 'legacy': False,
            'num_classes': 'sequential', 'adm_in_channels': 2816, 'use_fp16': HzaWhAqAbytRDBNdzYQQeTtjNGGUstsT, 'in_channels': 4, 'model_channels': 320,
            'num_res_blocks': 2, 'attention_resolutions': [], 'transformer_depth': [0, 0, 0], 'channel_mult': [1, 2, 4],
            'transformer_depth_middle': 0, 'use_linear_in_transformer': True, "num_head_channels": 64, 'context_dim': 1}
    bTlSRfuiCqKMvYEppCIKhhQfsIRkRRCc = {'use_checkpoint': False, 'image_size': 32, 'out_channels': 4, 'use_spatial_transformer': True, 'legacy': False,
            'num_classes': 'sequential', 'adm_in_channels': 2816, 'use_fp16': HzaWhAqAbytRDBNdzYQQeTtjNGGUstsT, 'in_channels': 9, 'model_channels': 320,
            'num_res_blocks': 2, 'attention_resolutions': [2, 4], 'transformer_depth': [0, 2, 10], 'channel_mult': [1, 2, 4],
            'transformer_depth_middle': 10, 'use_linear_in_transformer': True, 'context_dim': 2048, "num_head_channels": 64}
    plerLAIlEUdlrDugwPUkpJeEHQyvYTCL = [hTIrchlPHYZofZJBRoQFMjAnlKwSEPlB, rKuYZDeUTMKOszHSYSIXlegaiIgSvpra, rqacOpJSPWDNLdhfPYRxumhBdlKkTaHI, YlEWwgaMKiTVEpSjHUNNzLiJqMZaVSZP, dpmCZvpSEHoTdKsZQMqfkcmeNjFLgqsQ, WpUdlMsnoiTiCAtAQggpjMPzQoNwAKlr, MlRccaGYXAVvHzOUIyYEpckLNzAUehwy, RTPtSLCHsZiCxVExECqPShLKWDRkAKGD, bTlSRfuiCqKMvYEppCIKhhQfsIRkRRCc]
    for lLgbOYEeDmYyyxASAROATrPmlqgqYORG in plerLAIlEUdlrDugwPUkpJeEHQyvYTCL:
        EmdemYfqcZwKxzMFIqlEDyyJOFHcDLYk = True
        for EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm in aTtGvrcNbpJkYrNtoqbGYpIWUWDLYOBz:
            if aTtGvrcNbpJkYrNtoqbGYpIWUWDLYOBz[EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm] != lLgbOYEeDmYyyxASAROATrPmlqgqYORG[EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm]:
                EmdemYfqcZwKxzMFIqlEDyyJOFHcDLYk = False
                break
        if EmdemYfqcZwKxzMFIqlEDyyJOFHcDLYk:
            return lLgbOYEeDmYyyxASAROATrPmlqgqYORG
    return None
def KSCpmTprXUXkMiIbeHEXqnbmtoKMmpEy(TQRgUMPjEwYAaDvSuzgvheADStCoUKzT, HzaWhAqAbytRDBNdzYQQeTtjNGGUstsT):
    lLgbOYEeDmYyyxASAROATrPmlqgqYORG = xySSEzFdNBmsMIgcTEsdJVqMgpLUBwLW(TQRgUMPjEwYAaDvSuzgvheADStCoUKzT, HzaWhAqAbytRDBNdzYQQeTtjNGGUstsT)
    if lLgbOYEeDmYyyxASAROATrPmlqgqYORG is not None:
        return EuzsbjrrgKrTkfcBoMFZzWEywaHOxzBP(lLgbOYEeDmYyyxASAROATrPmlqgqYORG)
    return None
