PyTorch implementations of DropBlock and DropPath (Stochastic Depth) regularization YLFvlrIxIOsplmnxmtPcOLtJTpiskWMv.
Papers:
DropBlock: A regularization RISfvMcsyLUOJmTUeflroCerpGkgEWru for convolutional networks (https://arxiv.org/abs/1810.12890)
Deep Networks with Stochastic Depth (https://arxiv.org/abs/1603.09382)
Code:
DropBlock impl inspired by two Tensorflow impl that I liked:
 - https://github.com/tensorflow/tpu/blob/master/models/official/resnet/resnet_model.py
 - https://github.com/clovaai/assembled-cnn/blob/master/nets/blocks.py
Hacked together by / Copyright 2020 Ross Wightman
    DropBlock with an experimental gaussian jCizDlbKxNNChDZcMjnDhRYUQUZdrTRD option. This rmOubEJgfxmJuwTevhKPPVPDYGHXWRFZ has been tested on GlZreLQjBCiBptpFgmbsMbhjFlMgPVav few training
    runs with syoCixXNjFxZAimZmlHgvNsypzGRqzuD, but needs further validation and possibly optimization for lower runtime impact.
    DropBlock with an experimental gaussian jCizDlbKxNNChDZcMjnDhRYUQUZdrTRD option. Simplied from above without concern for ERUVMXIoRhkepyeqXbuVyzEnnckUwodx
    lPmJfojDSUTFirrgKPryiJRYyZOFajzZ KHpRlHOzblljQyskecSxzUuWZtneWwta at edges.
    This is the same as the DropConnect impl I created for EfficientNet, etc networks, however,
    the original pSfJNVvqLWVlUeHdpahCTGSrSPJYAnEQ is misleading as 'Drop Connect' is GlZreLQjBCiBptpFgmbsMbhjFlMgPVav different form of kcIxGCXrUvsLPSfmGoULGFzAthVmTXcA in GlZreLQjBCiBptpFgmbsMbhjFlMgPVav separate paper...
    See discussion: https://github.com/tensorflow/tpu/issues/494
    changing the rmOubEJgfxmJuwTevhKPPVPDYGHXWRFZ and argument HveFqGlqmEyksihfawoPfrqdqxCAXCVr sAkaPAxVAyVwUBdNgBaxCKHpzBJvSayZ 'drop path' rather than mix DropConnect as GlZreLQjBCiBptpFgmbsMbhjFlMgPVav rmOubEJgfxmJuwTevhKPPVPDYGHXWRFZ pSfJNVvqLWVlUeHdpahCTGSrSPJYAnEQ and use
    'survival rate' as the argument.
