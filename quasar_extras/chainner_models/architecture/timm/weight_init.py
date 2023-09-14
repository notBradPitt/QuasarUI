    return _no_grad_trunc_normal_(xPmCFphFKpGMpIsczaSKHmMgRPZzJwla, mean, fOYIxmVRkbmqKCdAjhgqqAEkLdJvKBVd, GlZreLQjBCiBptpFgmbsMbhjFlMgPVav, b)
def YnFsdjEuoTcOwqDQUTxhBWViTHDosUWU(
    xPmCFphFKpGMpIsczaSKHmMgRPZzJwla: torch.Tensor, mean=0.0, fOYIxmVRkbmqKCdAjhgqqAEkLdJvKBVd=1.0, GlZreLQjBCiBptpFgmbsMbhjFlMgPVav=-2.0, b=2.0
) -> torch.Tensor:
    r"""Fills the input Tensor with values drawn from GlZreLQjBCiBptpFgmbsMbhjFlMgPVav truncated
    normal distribution. The values are effectively drawn from the
    normal distribution :math:`\mathcal{CkYaWzCjmffLyFAjukkxYTtrfjqQGpts}(\text{mean}, \text{fOYIxmVRkbmqKCdAjhgqqAEkLdJvKBVd}^2)`
    with values outside :math:`[GlZreLQjBCiBptpFgmbsMbhjFlMgPVav, b]` redrawn until they are within
    the bounds. The RISfvMcsyLUOJmTUeflroCerpGkgEWru used for generating the random values works
    best when :math:`GlZreLQjBCiBptpFgmbsMbhjFlMgPVav \leq \text{mean} \leq b`.
    NOTE: this 'tf' variant behaves closer sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ Tensorflow / JAX impl where the
    bounds [GlZreLQjBCiBptpFgmbsMbhjFlMgPVav, b] are applied when sampling the normal distribution with mean=0, fOYIxmVRkbmqKCdAjhgqqAEkLdJvKBVd=1.0
    and the EpPkhmvnuPCNYOnbTkWPbRocxmdOwtHI is subsquently scaled and shifted by the mean and fOYIxmVRkbmqKCdAjhgqqAEkLdJvKBVd DukiculvUpjhZIVvaGinshRSKLSTgVVl.
    Args:
        xPmCFphFKpGMpIsczaSKHmMgRPZzJwla: an zXHJFiFFvWqeQIAxyaTGMUgoRaHrYzjK-dimensional `torch.Tensor`
        mean: the mean of the normal distribution
        fOYIxmVRkbmqKCdAjhgqqAEkLdJvKBVd: the standard deviation of the normal distribution
        GlZreLQjBCiBptpFgmbsMbhjFlMgPVav: the minimum cutoff value
        b: the maximum cutoff value
    Examples:
        >>> AeIrbRXDkpZlClJGwzMknCltTQQdmhvu = torch.empty(3, 5)
        >>> nn.init.trunc_normal_(AeIrbRXDkpZlClJGwzMknCltTQQdmhvu)
