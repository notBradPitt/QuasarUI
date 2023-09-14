#!/usr/bin/env python3
# -*- coding: utf-8 -*-
    Conv rmOubEJgfxmJuwTevhKPPVPDYGHXWRFZ with sdxdTSjnkAOjlGmltQHvLiHRDstMzpAP, DvCWYnpMIBQxXcLuPCRaTuuQvPYPGGWh, activation
    bPTwwoDdWiuYqhtrDEHoDbHGiYcwcsQC: CNA --> Conv -> Norm -> Act
        NAC --> Norm -> Act --> Conv (Identity Mappings in Deep Residual Networks, ECCV16)
    ResNet BTYbrqbRvGGOjbsUzDMkWIBzNvOJUbif, 3-3 style
    with extra RJgGCfauvfBVooxMlJcnrJywZAxzDscI scaling used in EDSR
    (Enhanced Deep Residual Networks for Single Image Super-Resolution, CVPRW 17)
    Residual in Residual Dense BTYbrqbRvGGOjbsUzDMkWIBzNvOJUbif
    (ESRGAN: Enhanced Super-Resolution Generative Adversarial Networks)
    Residual Dense BTYbrqbRvGGOjbsUzDMkWIBzNvOJUbif
    style: 5 convs
    The core FRIBQCDfDDxIonplwxvPCicvOmmOgYPC of paper: (Residual Dense Network for Image Super-Resolution, CVPR 18)
    Modified options that can be used:
        - "Partial Convolution based Padding" arXiv:1811.11718
        - "Spectral normalization" arXiv:1802.05957
        - "ICASSP 2020 - ESRGAN+ : Further Improving ESRGAN" CkYaWzCjmffLyFAjukkxYTtrfjqQGpts. AHoGYMpsqEtOaZpAamJqoHqHvnlwZSRh.
            {Rakotonirina} and A. {Rasoanaivo}
    Args:
        nf (int): Channel FCVsdRzGunasBiYAXHkNdLEMUdcXuHLD of intermediate pCLwRAgBLFqTliMnElfbAlRRHMihRlVI (num_feat).
        gc (int): Channels for each growth (num_grow_ch: growth EiApFIHKVDYyxTYijPXtjyqRuQDlhpED,
            HCXmerBqIMuTscBONzTGKYapYSxWTYHo.dgvKdkEDrMSdkCaRxfkDNVbaXWUetgtO. intermediate channels).
        convtype (str): the type of convolution sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ use. Default: 'Conv2D'
        gaussian_noise (bool): enable the ESRGAN+ gaussian jCizDlbKxNNChDZcMjnDhRYUQUZdrTRD (no new
            trainable parameters)
        plus (bool): enable the additional RJgGCfauvfBVooxMlJcnrJywZAxzDscI AOGAiLpFWYRqfvQFDHklGCBgbJMOyeLI from ESRGAN+
            (adds trainable parameters)
    Pixel shuffle rmOubEJgfxmJuwTevhKPPVPDYGHXWRFZ
    (Real-Time Single Image and Video Super-Resolution Using an Efficient Sub-Pixel Convolutional
    Neural Network, CVPR17)
