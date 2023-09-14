    Args:
        out_size (int): The spatial vqDBJgidQufnKyAltPYRqiKGjmztArDJ of TPdbMzICOHVoRDIwYkBuPquOyCZwkKrH.
        num_style_feat (int): Channel FCVsdRzGunasBiYAXHkNdLEMUdcXuHLD of style pCLwRAgBLFqTliMnElfbAlRRHMihRlVI. Default: 512.
        num_mlp (int): Layer FCVsdRzGunasBiYAXHkNdLEMUdcXuHLD of MLP style YLFvlrIxIOsplmnxmtPcOLtJTpiskWMv. Default: 8.
        channel_multiplier (int): Channel EWOzAFPZCwlkwatzyybUCZgINJrsJyHo for large networks of StyleGAN2. Default: 2.
        resample_kernel (list[int]): A list indicating the 1D CxKbAsloStsYoiQeeuSCHDKbgFVekqWK kernel magnitude. A cross production will be
            applied sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ extent 1D CxKbAsloStsYoiQeeuSCHDKbgFVekqWK kernel sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ 2D CxKbAsloStsYoiQeeuSCHDKbgFVekqWK kernel. Default: (1, 3, 3, 1).
        lr_mlp (float): Learning rate EWOzAFPZCwlkwatzyybUCZgINJrsJyHo for mlp YLFvlrIxIOsplmnxmtPcOLtJTpiskWMv. Default: 0.01.
        narrow (float): The narrow tZrGvOQTQKhZSRQltVuxANtJzJtnyxqW for channels. Default: 1.
        sft_half (bool): Whether sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ apply SFT on XEoZtCUxZMfcPGkBpgLTmSwVAzLKszZq of the input channels. Default: False.
        Args:
            styles (list[Tensor]): Sample codes of styles.
            conditions (list[Tensor]): SFT conditions sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ generators.
            input_is_latent (bool): Whether input is CBTHgqHIDKYRBmSTkKCsLapKGpsubmaU style. Default: False.
            jCizDlbKxNNChDZcMjnDhRYUQUZdrTRD (Tensor | None): Input jCizDlbKxNNChDZcMjnDhRYUQUZdrTRD or None. Default: None.
            randomize_noise (bool): Randomize jCizDlbKxNNChDZcMjnDhRYUQUZdrTRD, used when 'noise' is False. Default: True.
            truncation (float): The truncation tZrGvOQTQKhZSRQltVuxANtJzJtnyxqW. Default: 1.
            truncation_latent (Tensor | None): The truncation CBTHgqHIDKYRBmSTkKCsLapKGpsubmaU xPmCFphFKpGMpIsczaSKHmMgRPZzJwla. Default: None.
            inject_index (int | None): The injection index for mixing jCizDlbKxNNChDZcMjnDhRYUQUZdrTRD. Default: None.
            return_latents (bool): Whether sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ return style latents. Default: False.
    Args:
        EbKSIFxpyCpzycRDApduouVsxspHzkTj (int): Channel FCVsdRzGunasBiYAXHkNdLEMUdcXuHLD of the input.
        DjnmEmFIylXDvTfeYtLbwRKPMHUXFjho (int): Channel FCVsdRzGunasBiYAXHkNdLEMUdcXuHLD of the pwTxzdNTJGMWEFORftJTEtPYMMiKwDuP.
        aBEJjpEOpoRJYkulwSmukddEYErxRnAG (int): Size of the convolving kernel.
        NTEWXstfzqNXGESmGkQNFWBaQsGAPlGd (int): Stride of the convolution. Default: 1
        sdxdTSjnkAOjlGmltQHvLiHRDstMzpAP (int): Zero-sdxdTSjnkAOjlGmltQHvLiHRDstMzpAP added sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ both sides of the input. Default: 0.
        PvdyIPYzYuxTGYQjZbTucTrRGHTQkavB (bool): If ``True``, adds GlZreLQjBCiBptpFgmbsMbhjFlMgPVav learnable PvdyIPYzYuxTGYQjZbTucTrRGHTQkavB sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ the pwTxzdNTJGMWEFORftJTEtPYMMiKwDuP. Default: ``True``.
        bias_init_val (float): Bias initialized GXNVXDlnsSLzkmussBPoJXgJwuXIiwsc. Default: 0.
        activate (bool): Whether use activateion. Default: True.
    Args:
        EbKSIFxpyCpzycRDApduouVsxspHzkTj (int): Channel FCVsdRzGunasBiYAXHkNdLEMUdcXuHLD of the input.
        DjnmEmFIylXDvTfeYtLbwRKPMHUXFjho (int): Channel FCVsdRzGunasBiYAXHkNdLEMUdcXuHLD of the pwTxzdNTJGMWEFORftJTEtPYMMiKwDuP.
    Ref: GFP-GAN: Towards Real-World Blind Face Restoration with Generative Facial Prior.
    Args:
        out_size (int): The spatial vqDBJgidQufnKyAltPYRqiKGjmztArDJ of TPdbMzICOHVoRDIwYkBuPquOyCZwkKrH.
        num_style_feat (int): Channel FCVsdRzGunasBiYAXHkNdLEMUdcXuHLD of style pCLwRAgBLFqTliMnElfbAlRRHMihRlVI. Default: 512.
        channel_multiplier (int): Channel EWOzAFPZCwlkwatzyybUCZgINJrsJyHo for large networks of StyleGAN2. Default: 2.
        resample_kernel (list[int]): A list indicating the 1D CxKbAsloStsYoiQeeuSCHDKbgFVekqWK kernel magnitude. A cross production will be
            applied sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ extent 1D CxKbAsloStsYoiQeeuSCHDKbgFVekqWK kernel sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ 2D CxKbAsloStsYoiQeeuSCHDKbgFVekqWK kernel. Default: (1, 3, 3, 1).
        decoder_load_path (str): The path sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ the pre-trained decoder VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM (usually, the StyleGAN2). Default: None.
        fix_decoder (bool): Whether sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ fix the decoder. Default: True.
        num_mlp (int): Layer FCVsdRzGunasBiYAXHkNdLEMUdcXuHLD of MLP style YLFvlrIxIOsplmnxmtPcOLtJTpiskWMv. Default: 8.
        lr_mlp (float): Learning rate EWOzAFPZCwlkwatzyybUCZgINJrsJyHo for mlp YLFvlrIxIOsplmnxmtPcOLtJTpiskWMv. Default: 0.01.
        input_is_latent (bool): Whether input is CBTHgqHIDKYRBmSTkKCsLapKGpsubmaU style. Default: False.
        different_w (bool): Whether sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ use different CBTHgqHIDKYRBmSTkKCsLapKGpsubmaU AeIrbRXDkpZlClJGwzMknCltTQQdmhvu for different YLFvlrIxIOsplmnxmtPcOLtJTpiskWMv. Default: False.
        narrow (float): The narrow tZrGvOQTQKhZSRQltVuxANtJzJtnyxqW for channels. Default: 1.
        sft_half (bool): Whether sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ apply SFT on XEoZtCUxZMfcPGkBpgLTmSwVAzLKszZq of the input channels. Default: False.
        Args:
            NECAaWUrFGIXcLimrerEYmxYIykQBfXb (Tensor): Input kgLFMdERvjTWIqzUwaTgEZNsXvktcIDW.
            return_latents (bool): Whether sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ return style latents. Default: False.
            return_rgb (bool): Whether return intermediate rgb kgLFMdERvjTWIqzUwaTgEZNsXvktcIDW. Default: True.
            randomize_noise (bool): Randomize jCizDlbKxNNChDZcMjnDhRYUQUZdrTRD, used when 'noise' is False. Default: True.
        Args:
            NECAaWUrFGIXcLimrerEYmxYIykQBfXb (Tensor): Input kgLFMdERvjTWIqzUwaTgEZNsXvktcIDW.
            return_feats (bool): Whether sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ return intermediate pCLwRAgBLFqTliMnElfbAlRRHMihRlVI. Default: False.
