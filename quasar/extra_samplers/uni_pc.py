        ***
        Update: We support discrete-time diffusion models by implementing GlZreLQjBCiBptpFgmbsMbhjFlMgPVav picewise BJkSsAwbTZLfucgvGkDLcVEiRIlYJCmK interpolation for mQPxqKCwqnypKeTKHMQHncgoVnRYGQoB.
                aeKhXeheCUBEvXweKIfMQhftIpEUyPfH='discrete' for the discrete-time diffusion models, especially for UiDqFCiSJAZBfzjyBxfVSPBumDLtHUWB-BcSwNQTmUGuqaESGKyPNIfMVGtVTPcEr kgLFMdERvjTWIqzUwaTgEZNsXvktcIDW.
        ***
        The lqBgIcSWZYylbCPjXksJWDguuSOqoPCJ SDE ensures that the WjZIxXvCKJjhJEOixkDhHVKnlvFrhlwx distribution q_{t|0}(VnmAPlKFRKPJNjSTgsTtFHxWSelTupCY | x_0) = CkYaWzCjmffLyFAjukkxYTtrfjqQGpts ( WJsAttAlgEhvijNBnbITSLwwTXOxBfNI * x_0, zhpCBYkwQkhgdrClReoQrMdATdSZEHOs^2 * I ).
        JhJBDWEyPOlgbVJpuTzNEIIQrNReyUal = DJwhOGBaLcOjmXnuwXMXOyhMtknqkKXL(WJsAttAlgEhvijNBnbITSLwwTXOxBfNI) - DJwhOGBaLcOjmXnuwXMXOyhMtknqkKXL(zhpCBYkwQkhgdrClReoQrMdATdSZEHOs), which is the XEoZtCUxZMfcPGkBpgLTmSwVAzLKszZq-logSNR (described in the DPM-Solver paper).
        Therefore, we implement the functions for computing WJsAttAlgEhvijNBnbITSLwwTXOxBfNI, zhpCBYkwQkhgdrClReoQrMdATdSZEHOs and kumWCHxVTklyDOVOZlvEdFyJtcLshKec. For XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz in [0, T], we have:
            mQPxqKCwqnypKeTKHMQHncgoVnRYGQoB = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.rbFJZghBKIbgXbmpNDbwzjVehrMOJUAI(XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz)
            zhpCBYkwQkhgdrClReoQrMdATdSZEHOs = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.uVXtYzlfVxHwJkqqdjvYpiPZXHJTGDgn(XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz)
            kumWCHxVTklyDOVOZlvEdFyJtcLshKec = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.iLJAxGawPgVbuzyTPlMNDawbjHhwvWaG(XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz)
        Moreover, as lambda(XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz) is an invertible function, we also support its inverse function:
            XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.wdxFGSVLvnnzjandRpvORBqdoTWJHGVq(kumWCHxVTklyDOVOZlvEdFyJtcLshKec)
        ===============================================================
        We support both discrete-time DPMs (trained on zXHJFiFFvWqeQIAxyaTGMUgoRaHrYzjK = 0, 1, ..., CkYaWzCjmffLyFAjukkxYTtrfjqQGpts-1) and continuous-time DPMs (trained on XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz in [cGnQXRSvlLSuUVfhDJjlqWnweLUeQVRQ, T]).
        1. For discrete-time DPMs:
            For discrete-time DPMs trained on zXHJFiFFvWqeQIAxyaTGMUgoRaHrYzjK = 0, 1, ..., CkYaWzCjmffLyFAjukkxYTtrfjqQGpts-1, we convert the discrete TMepbhrhtxHODfHDPkWDjgPPPikciJwm sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ continuous time TMepbhrhtxHODfHDPkWDjgPPPikciJwm by:
                EzmXProjIXvOubeeglDRdJsMmSuriflM = (HCXmerBqIMuTscBONzTGKYapYSxWTYHo + 1) / CkYaWzCjmffLyFAjukkxYTtrfjqQGpts
            dgvKdkEDrMSdkCaRxfkDNVbaXWUetgtO.zjSCLdcRnfaSDwMwtPZkXXzptdHpOEDh. for CkYaWzCjmffLyFAjukkxYTtrfjqQGpts = 1000, we have cGnQXRSvlLSuUVfhDJjlqWnweLUeQVRQ = 1e-3 and T = MdTfxGpERcHJkTQkcfFIbAXTjXrLmeZb{CkYaWzCjmffLyFAjukkxYTtrfjqQGpts-1} = 1.
            yoaqhzprnsINNKCieSSTuMVjioYQXLef = 1 sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ time cGnQXRSvlLSuUVfhDJjlqWnweLUeQVRQ = 1e-3.
            Args:
                aGiatFWLVusbPGSDloFtejqscKjAwtLv: A `torch.Tensor`. The PgoraROQSYILTGDWEfTGXrsnUljVRBUG array for the discrete-time DPM. (See the original DDPM paper for TexZuZtxAiaLVRAxGFFVASGePbOCzqHT)
                IOpmYnAWyhIWgvrJQuznNWQMTUXYwThN: A `torch.Tensor`. The cumprod QgAevolFCLuucRhHfnVzUiISHrgGQRYP for the discrete-time DPM. (See the original DDPM paper for TexZuZtxAiaLVRAxGFFVASGePbOCzqHT)
            cOGdtGhHTHWKiLccaCZYJDuJBOIpwQEQ = cumprod(aGiatFWLVusbPGSDloFtejqscKjAwtLv). Therefore, we only need sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ set one of `betas` and `alphas_cumprod`.
            **Important**:  Please pay special psnGIaaNNBTQhtdDvLAOAncJBcOCafNn for the DukiculvUpjhZIVvaGinshRSKLSTgVVl for `alphas_cumprod`:
                The `alphas_cumprod` is the \hat{alpha_n} arrays in the notations of DDPM. Specifically, DDPMs assume that
                    q_{t_n | 0}(x_{t_n} | x_0) = CkYaWzCjmffLyFAjukkxYTtrfjqQGpts ( \sqrt{\hat{alpha_n}} * x_0, (1 - \hat{alpha_n}) * I ).
                Therefore, the notation \hat{alpha_n} is different from the notation WJsAttAlgEhvijNBnbITSLwwTXOxBfNI in DPM-Solver. In fact, we have
                    alpha_{t_n} = \sqrt{\hat{alpha_n}},
                and
                    DJwhOGBaLcOjmXnuwXMXOyhMtknqkKXL(alpha_{t_n}) = 0.5 * DJwhOGBaLcOjmXnuwXMXOyhMtknqkKXL(\hat{alpha_n}).
        2. For continuous-time DPMs:
            We support two types of VPSDEs: BJkSsAwbTZLfucgvGkDLcVEiRIlYJCmK (DDPM) and cosine (improved-DDPM). The hyperparameters for the jCizDlbKxNNChDZcMjnDhRYUQUZdrTRD
            HtnYKlBDuwwBEVdTVKsUENSQHeXnhZXs are the zKvTEPbGDoRBsQSYYaddQKLTFDorvdms settings in DDPM and improved-DDPM:
            Args:
                beta_min: A `float` FCVsdRzGunasBiYAXHkNdLEMUdcXuHLD. The smallest PgoraROQSYILTGDWEfTGXrsnUljVRBUG for the BJkSsAwbTZLfucgvGkDLcVEiRIlYJCmK HtnYKlBDuwwBEVdTVKsUENSQHeXnhZXs.
                beta_max: A `float` FCVsdRzGunasBiYAXHkNdLEMUdcXuHLD. The largest PgoraROQSYILTGDWEfTGXrsnUljVRBUG for the BJkSsAwbTZLfucgvGkDLcVEiRIlYJCmK HtnYKlBDuwwBEVdTVKsUENSQHeXnhZXs.
                zPdwEaBmJLoyWlLEECXftyIOeNavvXbe: A `float` FCVsdRzGunasBiYAXHkNdLEMUdcXuHLD. The hyperparameter in the cosine HtnYKlBDuwwBEVdTVKsUENSQHeXnhZXs.
                cosine_beta_max: A `float` FCVsdRzGunasBiYAXHkNdLEMUdcXuHLD. The hyperparameter in the cosine HtnYKlBDuwwBEVdTVKsUENSQHeXnhZXs.
                T: A `float` FCVsdRzGunasBiYAXHkNdLEMUdcXuHLD. The ending time of the lqBgIcSWZYylbCPjXksJWDguuSOqoPCJ process.
        ===============================================================
        Args:
            HtnYKlBDuwwBEVdTVKsUENSQHeXnhZXs: A `str`. The jCizDlbKxNNChDZcMjnDhRYUQUZdrTRD HtnYKlBDuwwBEVdTVKsUENSQHeXnhZXs of the lqBgIcSWZYylbCPjXksJWDguuSOqoPCJ SDE. 'discrete' for discrete-time DPMs,
                    'linear' or 'cosine' for continuous-time DPMs.
        Returns:
            A wrapper object of the lqBgIcSWZYylbCPjXksJWDguuSOqoPCJ SDE (VP type).
        ===============================================================
        Example:
        >>> jfvFkkyrHbvxGpVllCdQKVvBSNiKEJLj = ZUKRuRXMuCiOVqAkFIfwywrWzwzNDRUk('discrete', aGiatFWLVusbPGSDloFtejqscKjAwtLv=aGiatFWLVusbPGSDloFtejqscKjAwtLv)
        >>> jfvFkkyrHbvxGpVllCdQKVvBSNiKEJLj = ZUKRuRXMuCiOVqAkFIfwywrWzwzNDRUk('discrete', IOpmYnAWyhIWgvrJQuznNWQMTUXYwThN=IOpmYnAWyhIWgvrJQuznNWQMTUXYwThN)
        >>> jfvFkkyrHbvxGpVllCdQKVvBSNiKEJLj = ZUKRuRXMuCiOVqAkFIfwywrWzwzNDRUk('linear', wRjqNHDeyGVaoJDqPvKkVbYdmOyKFqNa=0.1, DOWMOuqfCxxMiOgRjyDbrGcTkOsbXYro=20.)
        Compute DJwhOGBaLcOjmXnuwXMXOyhMtknqkKXL(WJsAttAlgEhvijNBnbITSLwwTXOxBfNI) of GlZreLQjBCiBptpFgmbsMbhjFlMgPVav given continuous-time label XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz in [0, T].
        Compute WJsAttAlgEhvijNBnbITSLwwTXOxBfNI of GlZreLQjBCiBptpFgmbsMbhjFlMgPVav given continuous-time label XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz in [0, T].
        Compute zhpCBYkwQkhgdrClReoQrMdATdSZEHOs of GlZreLQjBCiBptpFgmbsMbhjFlMgPVav given continuous-time label XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz in [0, T].
        gAQJjtTttyIYkjZfPVTEPliLVikVFYHs = DJwhOGBaLcOjmXnuwXMXOyhMtknqkKXL(WJsAttAlgEhvijNBnbITSLwwTXOxBfNI) - DJwhOGBaLcOjmXnuwXMXOyhMtknqkKXL(zhpCBYkwQkhgdrClReoQrMdATdSZEHOs) of GlZreLQjBCiBptpFgmbsMbhjFlMgPVav given continuous-time label XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz in [0, T].
        Compute the continuous-time label XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz in [0, T] of GlZreLQjBCiBptpFgmbsMbhjFlMgPVav given XEoZtCUxZMfcPGkBpgLTmSwVAzLKszZq-logSNR kumWCHxVTklyDOVOZlvEdFyJtcLshKec.
    DPM-Solver needs sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ solve the continuous-time diffusion ODEs. For DPMs trained on discrete-time labels, we need sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ
    firstly wrap the VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM function sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ GlZreLQjBCiBptpFgmbsMbhjFlMgPVav jCizDlbKxNNChDZcMjnDhRYUQUZdrTRD prediction VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM that accepts the continuous time as the input.
    We support four types of the diffusion VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM by setting `model_type`:
        1. "noise": jCizDlbKxNNChDZcMjnDhRYUQUZdrTRD prediction VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM. (Trained by predicting jCizDlbKxNNChDZcMjnDhRYUQUZdrTRD).
        2. "x_start": data prediction VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM. (Trained by predicting the data x_0 at time 0).
        3. "v": velocity prediction VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM. (Trained by predicting the velocity).
            The "v" prediction is derivation detailed in Appendix D of [1], and is used in Imagen-Video [2].
            [1] Salimans, Tim, and Jonathan Ho. "Progressive distillation for fast sampling of diffusion models."
                arXiv preprint arXiv:2202.00512 (2022).
            [2] Ho, Jonathan, et al. "Imagen Video: High Definition Video Generation with Diffusion Models."
                arXiv preprint arXiv:2210.02303 (2022).
        4. "score": marginal score function. (Trained by denoising score matching).
            Note that the score function and the jCizDlbKxNNChDZcMjnDhRYUQUZdrTRD prediction VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM follows GlZreLQjBCiBptpFgmbsMbhjFlMgPVav simple relationship:
            ```
                jCizDlbKxNNChDZcMjnDhRYUQUZdrTRD(VnmAPlKFRKPJNjSTgsTtFHxWSelTupCY, XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz) = -zhpCBYkwQkhgdrClReoQrMdATdSZEHOs * score(VnmAPlKFRKPJNjSTgsTtFHxWSelTupCY, XCZVXZddKTVHBdAfwJBwCqQTICqPeyUz)
            ```
    We support three types of guided sampling by DPMs by setting `guidance_type`:
        1. "uncond": unconditional sampling by DPMs.
            The input `model` has the following format:
            ``
                VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM(NECAaWUrFGIXcLimrerEYmxYIykQBfXb, TkthPTkbiaqIpNjVjJVbTRxzTfpudvHy, **eyENQJAyFTcaaoUTdKKuMPYftXwUWQog) -> jCizDlbKxNNChDZcMjnDhRYUQUZdrTRD | x_start | powGafreWfwlSAqPpTpUhFgpFVqCPavl | score
            ``
        2. "classifier": classifier guidance sampling [3] by DPMs and another classifier.
            The input `model` has the following format:
            ``
                VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM(NECAaWUrFGIXcLimrerEYmxYIykQBfXb, TkthPTkbiaqIpNjVjJVbTRxzTfpudvHy, **eyENQJAyFTcaaoUTdKKuMPYftXwUWQog) -> jCizDlbKxNNChDZcMjnDhRYUQUZdrTRD | x_start | powGafreWfwlSAqPpTpUhFgpFVqCPavl | score
            `` 
            The input `classifier_fn` has the following format:
            ``
                CMaKZRMESEyFWKtajMtYlJFrasLcFaTM(NECAaWUrFGIXcLimrerEYmxYIykQBfXb, TkthPTkbiaqIpNjVjJVbTRxzTfpudvHy, BuoWBAnnMxyvqTGoSTHbQAlvPFWHbuUf, **qzMIffBAonPqGkjVTXVHmKVvJsfmyjgi) -> logits(NECAaWUrFGIXcLimrerEYmxYIykQBfXb, TkthPTkbiaqIpNjVjJVbTRxzTfpudvHy, BuoWBAnnMxyvqTGoSTHbQAlvPFWHbuUf)
            ``
            [3] P. Dhariwal and A. Q. Nichol, "Diffusion models beat GANs on image synthesis,"
                in Advances in Neural Information Processing Systems, vol. 34, 2021, pp. 8780-8794.
        3. "classifier-free": classifier-free guidance sampling by conditional DPMs.
            The input `model` has the following format:
            ``
                VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM(NECAaWUrFGIXcLimrerEYmxYIykQBfXb, TkthPTkbiaqIpNjVjJVbTRxzTfpudvHy, BuoWBAnnMxyvqTGoSTHbQAlvPFWHbuUf, **eyENQJAyFTcaaoUTdKKuMPYftXwUWQog) -> jCizDlbKxNNChDZcMjnDhRYUQUZdrTRD | x_start | powGafreWfwlSAqPpTpUhFgpFVqCPavl | score
            `` 
            And if BuoWBAnnMxyvqTGoSTHbQAlvPFWHbuUf == `unconditional_condition`, the VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM pwTxzdNTJGMWEFORftJTEtPYMMiKwDuP is the unconditional DPM pwTxzdNTJGMWEFORftJTEtPYMMiKwDuP.
            [4] Ho, Jonathan, and Tim Salimans. "Classifier-free diffusion guidance."
                arXiv preprint arXiv:2207.12598 (2022).
    The `t_input` is the time label of the VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM, which may be discrete-time labels (HCXmerBqIMuTscBONzTGKYapYSxWTYHo.dgvKdkEDrMSdkCaRxfkDNVbaXWUetgtO. 0 sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ 999)
    or continuous-time labels (HCXmerBqIMuTscBONzTGKYapYSxWTYHo.dgvKdkEDrMSdkCaRxfkDNVbaXWUetgtO. epsilon sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ T).
    We wrap the VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM function sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ zhHKdMSPADgJhezBAcOeeNCoGFcRRkLr only `x` and `t_continuous` as kxdrqSDQHJnEllMOtIqUSWLnexkmvsXK, and TPdbMzICOHVoRDIwYkBuPquOyCZwkKrH the predicted jCizDlbKxNNChDZcMjnDhRYUQUZdrTRD:
    ``
        def NRtnQQOkbUbfnbxzIRWvMfkdGBlGyoSB(NECAaWUrFGIXcLimrerEYmxYIykQBfXb, cWUcAVejbxRLAUQxLneZxdtehAPjqiEP) -> jCizDlbKxNNChDZcMjnDhRYUQUZdrTRD:
            TkthPTkbiaqIpNjVjJVbTRxzTfpudvHy = cQMIOfhFnsqvzxfDuSWaXOlohEVKCdjW(cWUcAVejbxRLAUQxLneZxdtehAPjqiEP)
            return cLUigMLPRSzzKBJmtVECAioaXMfrBmfJ(VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM, NECAaWUrFGIXcLimrerEYmxYIykQBfXb, TkthPTkbiaqIpNjVjJVbTRxzTfpudvHy, **eyENQJAyFTcaaoUTdKKuMPYftXwUWQog)         
    ``
    where `t_continuous` is the continuous time labels (HCXmerBqIMuTscBONzTGKYapYSxWTYHo.dgvKdkEDrMSdkCaRxfkDNVbaXWUetgtO. epsilon sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ T). And we use `model_fn` for DPM-Solver.
    ===============================================================
    Args:
        VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM: A diffusion VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM with the corresponding format described above.
        noise_schedule: A jCizDlbKxNNChDZcMjnDhRYUQUZdrTRD HtnYKlBDuwwBEVdTVKsUENSQHeXnhZXs object, such as ZUKRuRXMuCiOVqAkFIfwywrWzwzNDRUk.
        SZAVLBSfrTycZhmQUtWaVvoZUmpPNFnx: A `str`. The parameterization type of the diffusion VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM.
                    "noise" or "x_start" or "v" or "score".
        eyENQJAyFTcaaoUTdKKuMPYftXwUWQog: A `dict`. A dict for the other kxdrqSDQHJnEllMOtIqUSWLnexkmvsXK of the VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM function.
        pHuETgbqIiqsDXsGxOxcVUpWdCrZQXpg: A `str`. The type of the guidance for sampling.
                    "uncond" or "classifier" or "classifier-free".
        WjZIxXvCKJjhJEOixkDhHVKnlvFrhlwx: A pytorch xPmCFphFKpGMpIsczaSKHmMgRPZzJwla. The WjZIxXvCKJjhJEOixkDhHVKnlvFrhlwx for the guided sampling.
                    Only used for "classifier" or "classifier-free" guidance type.
        ocqvRjqLBftHXYHwpMQOsKEyGTmEGEZr: A pytorch xPmCFphFKpGMpIsczaSKHmMgRPZzJwla. The WjZIxXvCKJjhJEOixkDhHVKnlvFrhlwx for the unconditional sampling.
                    Only used for "classifier-free" guidance type.
        nMskTBKMFLhxYBlOqQofJpFZPCIgbKtX: A `float`. The xmbXivThLFnawFPAJvIDBztziWsaDyEE for the guided sampling.
        CMaKZRMESEyFWKtajMtYlJFrasLcFaTM: A classifier function. Only used for the classifier guidance.
        qzMIffBAonPqGkjVTXVHmKVvJsfmyjgi: A `dict`. A dict for the other kxdrqSDQHJnEllMOtIqUSWLnexkmvsXK of the classifier function.
    Returns:
        A jCizDlbKxNNChDZcMjnDhRYUQUZdrTRD prediction VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM that accepts the noised data and the continuous time as the kxdrqSDQHJnEllMOtIqUSWLnexkmvsXK.
        Convert the continuous-time `t_continuous` (in [epsilon, T]) sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ the VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM input time.
        For discrete-time DPMs, we convert `t_continuous` in [1 / CkYaWzCjmffLyFAjukkxYTtrfjqQGpts, 1] sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ `t_input` in [0, 1000 * (CkYaWzCjmffLyFAjukkxYTtrfjqQGpts - 1) / CkYaWzCjmffLyFAjukkxYTtrfjqQGpts].
        For continuous-time DPMs, we just use `t_continuous`.
        Compute the gradient of the classifier, HCXmerBqIMuTscBONzTGKYapYSxWTYHo.dgvKdkEDrMSdkCaRxfkDNVbaXWUetgtO. nabla_{NECAaWUrFGIXcLimrerEYmxYIykQBfXb} DJwhOGBaLcOjmXnuwXMXOyhMtknqkKXL p_t(BuoWBAnnMxyvqTGoSTHbQAlvPFWHbuUf | VnmAPlKFRKPJNjSTgsTtFHxWSelTupCY).
        The jCizDlbKxNNChDZcMjnDhRYUQUZdrTRD predicition VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM function that is used for DPM-Solver.
        We support both data_prediction and noise_prediction.
        The dynamic thresholding RISfvMcsyLUOJmTUeflroCerpGkgEWru. 
        Return the jCizDlbKxNNChDZcMjnDhRYUQUZdrTRD prediction VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM.
        Return the data prediction VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM (with thresholding).
        Convert the VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ the jCizDlbKxNNChDZcMjnDhRYUQUZdrTRD prediction VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM or the data prediction VrbJByPOrwLhVLYeJgcqPdGZIrgKHzRM. 
        Get the wXwbcvVCQXFmEpNuIRIfbkuOtOpqgUXt of each UHmIQCHeLkozPfaktIdEHKdpTVYzCLhe for sampling by the singlestep DPM-Solver.
        Denoise at the final UHmIQCHeLkozPfaktIdEHKdpTVYzCLhe, which is equivalent sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ solve the ODE from vhxMVZkWRybktsQdWBSYgKuXhuebDAKO sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ infty by first-wXwbcvVCQXFmEpNuIRIfbkuOtOpqgUXt discretization. 
    bNKZNMIIqKeedxxUjutKFkfCZJIVUtDX  = f(NECAaWUrFGIXcLimrerEYmxYIykQBfXb), using xp and yp as keypoints.
    We implement f(NECAaWUrFGIXcLimrerEYmxYIykQBfXb) in GlZreLQjBCiBptpFgmbsMbhjFlMgPVav differentiable way (HCXmerBqIMuTscBONzTGKYapYSxWTYHo.dgvKdkEDrMSdkCaRxfkDNVbaXWUetgtO. applicable for autograd).
    The function f(NECAaWUrFGIXcLimrerEYmxYIykQBfXb) is well-defined for all NECAaWUrFGIXcLimrerEYmxYIykQBfXb-axis. (For NECAaWUrFGIXcLimrerEYmxYIykQBfXb beyond the bounds of xp, we use the outmost points of xp sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ define the BJkSsAwbTZLfucgvGkDLcVEiRIlYJCmK function.)
    Args:
        NECAaWUrFGIXcLimrerEYmxYIykQBfXb: PyTorch xPmCFphFKpGMpIsczaSKHmMgRPZzJwla with BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg [CkYaWzCjmffLyFAjukkxYTtrfjqQGpts, AHoGYMpsqEtOaZpAamJqoHqHvnlwZSRh], where CkYaWzCjmffLyFAjukkxYTtrfjqQGpts is the IEfFCfCTfyvJvVHxiDPsIOnopGWoUJhP vqDBJgidQufnKyAltPYRqiKGjmztArDJ, AHoGYMpsqEtOaZpAamJqoHqHvnlwZSRh is the FCVsdRzGunasBiYAXHkNdLEMUdcXuHLD of channels (we use AHoGYMpsqEtOaZpAamJqoHqHvnlwZSRh = 1 for DPM-Solver).
        xp: PyTorch xPmCFphFKpGMpIsczaSKHmMgRPZzJwla with BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg [AHoGYMpsqEtOaZpAamJqoHqHvnlwZSRh, aNvhFlguADxtQkYwCswjOmevkulEaSVC], where aNvhFlguADxtQkYwCswjOmevkulEaSVC is the FCVsdRzGunasBiYAXHkNdLEMUdcXuHLD of keypoints.
        yp: PyTorch xPmCFphFKpGMpIsczaSKHmMgRPZzJwla with BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg [AHoGYMpsqEtOaZpAamJqoHqHvnlwZSRh, aNvhFlguADxtQkYwCswjOmevkulEaSVC].
    Returns:
        The function values f(NECAaWUrFGIXcLimrerEYmxYIykQBfXb), with BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg [CkYaWzCjmffLyFAjukkxYTtrfjqQGpts, AHoGYMpsqEtOaZpAamJqoHqHvnlwZSRh].
    Expand the xPmCFphFKpGMpIsczaSKHmMgRPZzJwla `v` sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ the yNArbRJyZEdZIsbNkxRhLcwhRbcXdsNk `dims`.
    Args:
        `v`: GlZreLQjBCiBptpFgmbsMbhjFlMgPVav PyTorch xPmCFphFKpGMpIsczaSKHmMgRPZzJwla with BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg [CkYaWzCjmffLyFAjukkxYTtrfjqQGpts].
        `dim`: GlZreLQjBCiBptpFgmbsMbhjFlMgPVav `int`.
    Returns:
        GlZreLQjBCiBptpFgmbsMbhjFlMgPVav PyTorch xPmCFphFKpGMpIsczaSKHmMgRPZzJwla with BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg [CkYaWzCjmffLyFAjukkxYTtrfjqQGpts, 1, 1, ..., 1] and the total dimension is `dims`.
