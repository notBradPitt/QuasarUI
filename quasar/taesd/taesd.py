#!/usr/bin/env python3
import torch
import torch.nn as nn
def VRzIOXLfdDszfSOpzuKgtjeGGtXuyctm(n_in, n_out, **kwargs):
    return nn.LcFcvNeYCKrBHlNkoWrkqdbxdkNCJBBK(n_in, n_out, 3, sdxdTSjnkAOjlGmltQHvLiHRDstMzpAP=1, **kwargs)
class dpfnYoNSApllTfgzQyCcRJKPGHYjggia(nn.Module):
    def lqBgIcSWZYylbCPjXksJWDguuSOqoPCJ(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, NECAaWUrFGIXcLimrerEYmxYIykQBfXb):
        return torch.tanh(NECAaWUrFGIXcLimrerEYmxYIykQBfXb / 3) * 3
class BTYbrqbRvGGOjbsUzDMkWIBzNvOJUbif(nn.Module):
    def __init__(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, n_in, n_out):
        super().__init__()
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.VRzIOXLfdDszfSOpzuKgtjeGGtXuyctm = nn.Sequential(VRzIOXLfdDszfSOpzuKgtjeGGtXuyctm(n_in, n_out), nn.ReLU(), VRzIOXLfdDszfSOpzuKgtjeGGtXuyctm(n_out, n_out), nn.ReLU(), VRzIOXLfdDszfSOpzuKgtjeGGtXuyctm(n_out, n_out))
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.skip = nn.LcFcvNeYCKrBHlNkoWrkqdbxdkNCJBBK(n_in, n_out, 1, PvdyIPYzYuxTGYQjZbTucTrRGHTQkavB=False) if n_in != n_out else nn.Identity()
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.fuse = nn.ReLU()
    def lqBgIcSWZYylbCPjXksJWDguuSOqoPCJ(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, NECAaWUrFGIXcLimrerEYmxYIykQBfXb):
        return rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.fuse(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.VRzIOXLfdDszfSOpzuKgtjeGGtXuyctm(NECAaWUrFGIXcLimrerEYmxYIykQBfXb) + rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.skip(NECAaWUrFGIXcLimrerEYmxYIykQBfXb))
def HAhRJZDsPfbaJIpLwjOXFEkHqjueFULJ():
    return nn.Sequential(
        VRzIOXLfdDszfSOpzuKgtjeGGtXuyctm(3, 64), BTYbrqbRvGGOjbsUzDMkWIBzNvOJUbif(64, 64),
        VRzIOXLfdDszfSOpzuKgtjeGGtXuyctm(64, 64, NTEWXstfzqNXGESmGkQNFWBaQsGAPlGd=2, PvdyIPYzYuxTGYQjZbTucTrRGHTQkavB=False), BTYbrqbRvGGOjbsUzDMkWIBzNvOJUbif(64, 64), BTYbrqbRvGGOjbsUzDMkWIBzNvOJUbif(64, 64), BTYbrqbRvGGOjbsUzDMkWIBzNvOJUbif(64, 64),
        VRzIOXLfdDszfSOpzuKgtjeGGtXuyctm(64, 64, NTEWXstfzqNXGESmGkQNFWBaQsGAPlGd=2, PvdyIPYzYuxTGYQjZbTucTrRGHTQkavB=False), BTYbrqbRvGGOjbsUzDMkWIBzNvOJUbif(64, 64), BTYbrqbRvGGOjbsUzDMkWIBzNvOJUbif(64, 64), BTYbrqbRvGGOjbsUzDMkWIBzNvOJUbif(64, 64),
        VRzIOXLfdDszfSOpzuKgtjeGGtXuyctm(64, 64, NTEWXstfzqNXGESmGkQNFWBaQsGAPlGd=2, PvdyIPYzYuxTGYQjZbTucTrRGHTQkavB=False), BTYbrqbRvGGOjbsUzDMkWIBzNvOJUbif(64, 64), BTYbrqbRvGGOjbsUzDMkWIBzNvOJUbif(64, 64), BTYbrqbRvGGOjbsUzDMkWIBzNvOJUbif(64, 64),
        VRzIOXLfdDszfSOpzuKgtjeGGtXuyctm(64, 4),
    )
def KfKIubLWuMYndZytaOVMUrnTLHiwPiVV():
    return nn.Sequential(
        dpfnYoNSApllTfgzQyCcRJKPGHYjggia(), VRzIOXLfdDszfSOpzuKgtjeGGtXuyctm(4, 64), nn.ReLU(),
        BTYbrqbRvGGOjbsUzDMkWIBzNvOJUbif(64, 64), BTYbrqbRvGGOjbsUzDMkWIBzNvOJUbif(64, 64), BTYbrqbRvGGOjbsUzDMkWIBzNvOJUbif(64, 64), nn.kjruhryvXAQxnjJDeOXqTJbBrTkRFQSk(scale_factor=2), VRzIOXLfdDszfSOpzuKgtjeGGtXuyctm(64, 64, PvdyIPYzYuxTGYQjZbTucTrRGHTQkavB=False),
        BTYbrqbRvGGOjbsUzDMkWIBzNvOJUbif(64, 64), BTYbrqbRvGGOjbsUzDMkWIBzNvOJUbif(64, 64), BTYbrqbRvGGOjbsUzDMkWIBzNvOJUbif(64, 64), nn.kjruhryvXAQxnjJDeOXqTJbBrTkRFQSk(scale_factor=2), VRzIOXLfdDszfSOpzuKgtjeGGtXuyctm(64, 64, PvdyIPYzYuxTGYQjZbTucTrRGHTQkavB=False),
        BTYbrqbRvGGOjbsUzDMkWIBzNvOJUbif(64, 64), BTYbrqbRvGGOjbsUzDMkWIBzNvOJUbif(64, 64), BTYbrqbRvGGOjbsUzDMkWIBzNvOJUbif(64, 64), nn.kjruhryvXAQxnjJDeOXqTJbBrTkRFQSk(scale_factor=2), VRzIOXLfdDszfSOpzuKgtjeGGtXuyctm(64, 64, PvdyIPYzYuxTGYQjZbTucTrRGHTQkavB=False),
        BTYbrqbRvGGOjbsUzDMkWIBzNvOJUbif(64, 64), VRzIOXLfdDszfSOpzuKgtjeGGtXuyctm(64, 3),
    )
class CFXvAYULVpQFvvdJNHbevhEXAaaPZtnO(nn.Module):
    pPAfAhpjQLUeBOeVGPCztdIPaafFqoFu = 3
    YfkmagSHlCMAQtchSRvkRwdqcFVXTcKL = 0.5
    def __init__(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, encoder_path="taesd_encoder.pth", decoder_path="taesd_decoder.pth"):
        super().__init__()
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.encoder = HAhRJZDsPfbaJIpLwjOXFEkHqjueFULJ()
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.decoder = KfKIubLWuMYndZytaOVMUrnTLHiwPiVV()
        if encoder_path is not None:
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.encoder.OVlRwgmJvqggImaZMfxKZfQnVYfyhIsc(torch.yjjLwfEWtXKFjwwmuqReIXUDoGaUzfxz(encoder_path, map_location="cpu", weights_only=True))
        if decoder_path is not None:
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.decoder.OVlRwgmJvqggImaZMfxKZfQnVYfyhIsc(torch.yjjLwfEWtXKFjwwmuqReIXUDoGaUzfxz(decoder_path, map_location="cpu", weights_only=True))
    @staticmethod
    def TROuNVXftwVbUVYFwriuVbfjZaLMQOHg(NECAaWUrFGIXcLimrerEYmxYIykQBfXb):
        return NECAaWUrFGIXcLimrerEYmxYIykQBfXb.div(2 * CFXvAYULVpQFvvdJNHbevhEXAaaPZtnO.pPAfAhpjQLUeBOeVGPCztdIPaafFqoFu).add(CFXvAYULVpQFvvdJNHbevhEXAaaPZtnO.YfkmagSHlCMAQtchSRvkRwdqcFVXTcKL).clamp(0, 1)
    @staticmethod
    def UciIVErOIRBvhxJjpGpBdTssyhbfGtLg(NECAaWUrFGIXcLimrerEYmxYIykQBfXb):
        return NECAaWUrFGIXcLimrerEYmxYIykQBfXb.sub(CFXvAYULVpQFvvdJNHbevhEXAaaPZtnO.YfkmagSHlCMAQtchSRvkRwdqcFVXTcKL).mul(2 * CFXvAYULVpQFvvdJNHbevhEXAaaPZtnO.pPAfAhpjQLUeBOeVGPCztdIPaafFqoFu)
