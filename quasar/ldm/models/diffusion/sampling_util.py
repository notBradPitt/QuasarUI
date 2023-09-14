import torch
import numpy as np
def CMxxOxdPTSrjIzfwUpFYdWOyWfmNnQNF(NECAaWUrFGIXcLimrerEYmxYIykQBfXb, target_dims):
    QiRZNddHeMNZMeQGOXQJGIdEqODiwlSP = target_dims - NECAaWUrFGIXcLimrerEYmxYIykQBfXb.ndim
    if QiRZNddHeMNZMeQGOXQJGIdEqODiwlSP < 0:
        raise ValueError(f'input has {x.ndim} dims but target_dims is {target_dims}, which is less')
    return NECAaWUrFGIXcLimrerEYmxYIykQBfXb[(...,) + (None,) * QiRZNddHeMNZMeQGOXQJGIdEqODiwlSP]
def FuFPjwbSOSOGsduutWbGgxcLyqowDcLE(UBGvtPbFIPlcsBIwyWKuWMZeENGLMRAP, GXNVXDlnsSLzkmussBPoJXgJwuXIiwsc):
    uPePujIqMVDrwNvZQxJajkuaQFAcacjA = CMxxOxdPTSrjIzfwUpFYdWOyWfmNnQNF(UBGvtPbFIPlcsBIwyWKuWMZeENGLMRAP.pow(2).flatten(1).mean(1).sqrt().clamp(min=GXNVXDlnsSLzkmussBPoJXgJwuXIiwsc), UBGvtPbFIPlcsBIwyWKuWMZeENGLMRAP.ndim)
    return UBGvtPbFIPlcsBIwyWKuWMZeENGLMRAP * (GXNVXDlnsSLzkmussBPoJXgJwuXIiwsc / uPePujIqMVDrwNvZQxJajkuaQFAcacjA)
def owQGZtHKBeWpCIIYKcGzOpQQVYHrjpiG(UBGvtPbFIPlcsBIwyWKuWMZeENGLMRAP, GXNVXDlnsSLzkmussBPoJXgJwuXIiwsc):
    uPePujIqMVDrwNvZQxJajkuaQFAcacjA = UBGvtPbFIPlcsBIwyWKuWMZeENGLMRAP.pow(2).mean(1, keepdim=True).sqrt().clamp(min=GXNVXDlnsSLzkmussBPoJXgJwuXIiwsc)
    return UBGvtPbFIPlcsBIwyWKuWMZeENGLMRAP * (GXNVXDlnsSLzkmussBPoJXgJwuXIiwsc / uPePujIqMVDrwNvZQxJajkuaQFAcacjA)