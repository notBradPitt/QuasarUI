import re
import torch
UmHyIqJdhlkWwWvjuGufACIeDVplfufU = [
    ("time_embed.0.weight", "time_embedding.linear_1.weight"),
    ("time_embed.0.bias", "time_embedding.linear_1.bias"),
    ("time_embed.2.weight", "time_embedding.linear_2.weight"),
    ("time_embed.2.bias", "time_embedding.linear_2.bias"),
    ("input_blocks.0.0.weight", "conv_in.weight"),
    ("input_blocks.0.0.bias", "conv_in.bias"),
    ("out.0.weight", "conv_norm_out.weight"),
    ("out.0.bias", "conv_norm_out.bias"),
    ("out.2.weight", "conv_out.weight"),
    ("out.2.bias", "conv_out.bias"),
]
RLqjJJqywiqYQsPFepbFGXJaHiLcfzxE = [
    ("in_layers.0", "norm1"),
    ("in_layers.2", "conv1"),
    ("out_layers.0", "norm2"),
    ("out_layers.3", "conv2"),
    ("emb_layers.1", "time_emb_proj"),
    ("skip_connection", "conv_shortcut"),
]
QDEIShDfewUHHfbDFBaswEVdyCZqoDkI = []
for HCXmerBqIMuTscBONzTGKYapYSxWTYHo in range(4):
    for VyjoFEMsihtolZHiuwJuxJKmDsIroAsQ in range(2):
        RIbhcEBghEvHffKurCDoBHhayepVDGBN = f"down_blocks.{i}.resnets.{j}."
        VOlSognHYSWvWpRCbYgkOBJvIAmJAECS = f"input_blocks.{3 * i + j + 1}.0."
        QDEIShDfewUHHfbDFBaswEVdyCZqoDkI.append((VOlSognHYSWvWpRCbYgkOBJvIAmJAECS, RIbhcEBghEvHffKurCDoBHhayepVDGBN))
        if HCXmerBqIMuTscBONzTGKYapYSxWTYHo < 3:
            CDWsXLTJTuAbpEOqZjLqczLvswGrjwYX = f"down_blocks.{i}.attentions.{j}."
            jjSHGMuZrJwTPdFaJvcOEGWFcFRFLHpR = f"input_blocks.{3 * i + j + 1}.1."
            QDEIShDfewUHHfbDFBaswEVdyCZqoDkI.append((jjSHGMuZrJwTPdFaJvcOEGWFcFRFLHpR, CDWsXLTJTuAbpEOqZjLqczLvswGrjwYX))
    for VyjoFEMsihtolZHiuwJuxJKmDsIroAsQ in range(3):
        aZTCCtTmdwOqFIzrtnAHEKdggcAGSGoU = f"up_blocks.{i}.resnets.{j}."
        RILsWspvjUaSvauQhzzBluMMFkmSaEpn = f"output_blocks.{3 * i + j}.0."
        QDEIShDfewUHHfbDFBaswEVdyCZqoDkI.append((RILsWspvjUaSvauQhzzBluMMFkmSaEpn, aZTCCtTmdwOqFIzrtnAHEKdggcAGSGoU))
        if HCXmerBqIMuTscBONzTGKYapYSxWTYHo > 0:
            lGavZglwjsXRqopYfHXtFzkHTqGszFhD = f"up_blocks.{i}.attentions.{j}."
            bfjXJkXfhhGYdEMdsdpvxlBUmlhaKhJg = f"output_blocks.{3 * i + j}.1."
            QDEIShDfewUHHfbDFBaswEVdyCZqoDkI.append((bfjXJkXfhhGYdEMdsdpvxlBUmlhaKhJg, lGavZglwjsXRqopYfHXtFzkHTqGszFhD))
    if HCXmerBqIMuTscBONzTGKYapYSxWTYHo < 3:
        SJAvDJIbDjmRvuRxqHZiItgOwoSkBUeo = f"down_blocks.{i}.downsamplers.0.conv."
        pWunViTuMGvpzPtYZifyciBMuzvgXENP = f"input_blocks.{3 * (i + 1)}.0.op."
        QDEIShDfewUHHfbDFBaswEVdyCZqoDkI.append((pWunViTuMGvpzPtYZifyciBMuzvgXENP, SJAvDJIbDjmRvuRxqHZiItgOwoSkBUeo))
        TfUrlKpLPrjBihcxebSeSalaIsKLsacq = f"up_blocks.{i}.upsamplers.0."
        JtHFbHxzvHRjncHiobRmsnvWtDJhTvQp = f"output_blocks.{3 * i + 2}.{1 if i == 0 else 2}."
        QDEIShDfewUHHfbDFBaswEVdyCZqoDkI.append((JtHFbHxzvHRjncHiobRmsnvWtDJhTvQp, TfUrlKpLPrjBihcxebSeSalaIsKLsacq))
sfHbsHuFqCqhKcIXJWbzVbeoPysgpXOE = "mid_block.attentions.0."
OKceRlbVLIXZDFAGhItgRVeQMQwvMFlq = "middle_block.1."
QDEIShDfewUHHfbDFBaswEVdyCZqoDkI.append((OKceRlbVLIXZDFAGhItgRVeQMQwvMFlq, sfHbsHuFqCqhKcIXJWbzVbeoPysgpXOE))
for VyjoFEMsihtolZHiuwJuxJKmDsIroAsQ in range(2):
    dUrnOZsUTcYBokweWCNnGGxyiASiKDkQ = f"mid_block.resnets.{j}."
    aqESDCOvxzBOCHcJKBFuPqpCUsJbKcbN = f"middle_block.{2 * j}."
    QDEIShDfewUHHfbDFBaswEVdyCZqoDkI.append((aqESDCOvxzBOCHcJKBFuPqpCUsJbKcbN, dUrnOZsUTcYBokweWCNnGGxyiASiKDkQ))
def RHYwdKdueYEYpigJaMEQHdhPkGQuhSWD(gXYsYkJbPWMeavbmLkVsXBfRMdjBmWrT):
    rsURCWTCboilKpKjxalFpgfvAczsBquq = {EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm: EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm for EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm in gXYsYkJbPWMeavbmLkVsXBfRMdjBmWrT.keys()}
    for udJwlVmGhLmsCigWRpJIfJVqMQvoGxuq, NoIsWbsfElgbWYqRyXrBfmTMqvILIWsz in UmHyIqJdhlkWwWvjuGufACIeDVplfufU:
        rsURCWTCboilKpKjxalFpgfvAczsBquq[NoIsWbsfElgbWYqRyXrBfmTMqvILIWsz] = udJwlVmGhLmsCigWRpJIfJVqMQvoGxuq
    for EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm, powGafreWfwlSAqPpTpUhFgpFVqCPavl in rsURCWTCboilKpKjxalFpgfvAczsBquq.items():
        if "resnets" in EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm:
            for afaMLYcIQzSdRRVsPwsbjaBkOCVclxue, ldgcfZxRDmCxSgqqQYOFhIjgTrwZCCQx in RLqjJJqywiqYQsPFepbFGXJaHiLcfzxE:
                powGafreWfwlSAqPpTpUhFgpFVqCPavl = powGafreWfwlSAqPpTpUhFgpFVqCPavl.replace(ldgcfZxRDmCxSgqqQYOFhIjgTrwZCCQx, afaMLYcIQzSdRRVsPwsbjaBkOCVclxue)
            rsURCWTCboilKpKjxalFpgfvAczsBquq[EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm] = powGafreWfwlSAqPpTpUhFgpFVqCPavl
    for EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm, powGafreWfwlSAqPpTpUhFgpFVqCPavl in rsURCWTCboilKpKjxalFpgfvAczsBquq.items():
        for afaMLYcIQzSdRRVsPwsbjaBkOCVclxue, ldgcfZxRDmCxSgqqQYOFhIjgTrwZCCQx in QDEIShDfewUHHfbDFBaswEVdyCZqoDkI:
            powGafreWfwlSAqPpTpUhFgpFVqCPavl = powGafreWfwlSAqPpTpUhFgpFVqCPavl.replace(ldgcfZxRDmCxSgqqQYOFhIjgTrwZCCQx, afaMLYcIQzSdRRVsPwsbjaBkOCVclxue)
        rsURCWTCboilKpKjxalFpgfvAczsBquq[EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm] = powGafreWfwlSAqPpTpUhFgpFVqCPavl
    NtwbWJftksJLJogLEhqgoCQhMuuhOeqR = {powGafreWfwlSAqPpTpUhFgpFVqCPavl: gXYsYkJbPWMeavbmLkVsXBfRMdjBmWrT[EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm] for EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm, powGafreWfwlSAqPpTpUhFgpFVqCPavl in rsURCWTCboilKpKjxalFpgfvAczsBquq.items()}
    return NtwbWJftksJLJogLEhqgoCQhMuuhOeqR
jTncvHwjpcTmNxGFZTCAxIXkVwImAJWp = [
    ("nin_shortcut", "conv_shortcut"),
    ("norm_out", "conv_norm_out"),
    ("mid.attn_1.", "mid_block.attentions.0."),
]
for HCXmerBqIMuTscBONzTGKYapYSxWTYHo in range(4):
    for VyjoFEMsihtolZHiuwJuxJKmDsIroAsQ in range(2):
        KYaCPDUoJAcoBpYCpGgOCjDasjQimGty = f"encoder.down_blocks.{i}.resnets.{j}."
        wMDDkeaxFxZbJiiiHwpbkGThlCdrqSyC = f"encoder.down.{i}.block.{j}."
        jTncvHwjpcTmNxGFZTCAxIXkVwImAJWp.append((wMDDkeaxFxZbJiiiHwpbkGThlCdrqSyC, KYaCPDUoJAcoBpYCpGgOCjDasjQimGty))
    if HCXmerBqIMuTscBONzTGKYapYSxWTYHo < 3:
        SJAvDJIbDjmRvuRxqHZiItgOwoSkBUeo = f"down_blocks.{i}.downsamplers.0."
        pWunViTuMGvpzPtYZifyciBMuzvgXENP = f"down.{i}.downsample."
        jTncvHwjpcTmNxGFZTCAxIXkVwImAJWp.append((pWunViTuMGvpzPtYZifyciBMuzvgXENP, SJAvDJIbDjmRvuRxqHZiItgOwoSkBUeo))
        TfUrlKpLPrjBihcxebSeSalaIsKLsacq = f"up_blocks.{i}.upsamplers.0."
        JtHFbHxzvHRjncHiobRmsnvWtDJhTvQp = f"up.{3 - i}.upsample."
        jTncvHwjpcTmNxGFZTCAxIXkVwImAJWp.append((JtHFbHxzvHRjncHiobRmsnvWtDJhTvQp, TfUrlKpLPrjBihcxebSeSalaIsKLsacq))
    for VyjoFEMsihtolZHiuwJuxJKmDsIroAsQ in range(3):
        WRlCWppQancUsKXrMXZkGtzIYsUYKMnA = f"decoder.up_blocks.{i}.resnets.{j}."
        iiYvveVEMtTrzLNxcZydUDrVHiNyIKOd = f"decoder.up.{3 - i}.block.{j}."
        jTncvHwjpcTmNxGFZTCAxIXkVwImAJWp.append((iiYvveVEMtTrzLNxcZydUDrVHiNyIKOd, WRlCWppQancUsKXrMXZkGtzIYsUYKMnA))
for HCXmerBqIMuTscBONzTGKYapYSxWTYHo in range(2):
    dUrnOZsUTcYBokweWCNnGGxyiASiKDkQ = f"mid_block.resnets.{i}."
    aqESDCOvxzBOCHcJKBFuPqpCUsJbKcbN = f"mid.block_{i + 1}."
    jTncvHwjpcTmNxGFZTCAxIXkVwImAJWp.append((aqESDCOvxzBOCHcJKBFuPqpCUsJbKcbN, dUrnOZsUTcYBokweWCNnGGxyiASiKDkQ))
UpGXGFhHyKnfvRoWzxZteOumtEpKagaO = [
    ("norm.", "group_norm."),
    ("q.", "query."),
    ("k.", "key."),
    ("v.", "value."),
    ("q.", "to_q."),
    ("k.", "to_k."),
    ("v.", "to_v."),
    ("proj_out.", "to_out.0."),
    ("proj_out.", "proj_attn."),
]
def bMIZtKofdGCLugAAeSxBNXLRdAzwttMg(AeIrbRXDkpZlClJGwzMknCltTQQdmhvu):
    return AeIrbRXDkpZlClJGwzMknCltTQQdmhvu.reshape(*AeIrbRXDkpZlClJGwzMknCltTQQdmhvu.BElyDvcGzbvMmmwmYRGBIJogcxsyYZSg, 1, 1)
def ixNEzYSlBdsJDwRvhkuJPuACSqEcVOYP(QLykPMMghQkBzNKJlfgFZKhZZUmaNrQv):
    rsURCWTCboilKpKjxalFpgfvAczsBquq = {EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm: EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm for EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm in QLykPMMghQkBzNKJlfgFZKhZZUmaNrQv.keys()}
    for EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm, powGafreWfwlSAqPpTpUhFgpFVqCPavl in rsURCWTCboilKpKjxalFpgfvAczsBquq.items():
        for afaMLYcIQzSdRRVsPwsbjaBkOCVclxue, ldgcfZxRDmCxSgqqQYOFhIjgTrwZCCQx in jTncvHwjpcTmNxGFZTCAxIXkVwImAJWp:
            powGafreWfwlSAqPpTpUhFgpFVqCPavl = powGafreWfwlSAqPpTpUhFgpFVqCPavl.replace(ldgcfZxRDmCxSgqqQYOFhIjgTrwZCCQx, afaMLYcIQzSdRRVsPwsbjaBkOCVclxue)
        rsURCWTCboilKpKjxalFpgfvAczsBquq[EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm] = powGafreWfwlSAqPpTpUhFgpFVqCPavl
    for EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm, powGafreWfwlSAqPpTpUhFgpFVqCPavl in rsURCWTCboilKpKjxalFpgfvAczsBquq.items():
        if "attentions" in EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm:
            for afaMLYcIQzSdRRVsPwsbjaBkOCVclxue, ldgcfZxRDmCxSgqqQYOFhIjgTrwZCCQx in UpGXGFhHyKnfvRoWzxZteOumtEpKagaO:
                powGafreWfwlSAqPpTpUhFgpFVqCPavl = powGafreWfwlSAqPpTpUhFgpFVqCPavl.replace(ldgcfZxRDmCxSgqqQYOFhIjgTrwZCCQx, afaMLYcIQzSdRRVsPwsbjaBkOCVclxue)
            rsURCWTCboilKpKjxalFpgfvAczsBquq[EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm] = powGafreWfwlSAqPpTpUhFgpFVqCPavl
    NtwbWJftksJLJogLEhqgoCQhMuuhOeqR = {powGafreWfwlSAqPpTpUhFgpFVqCPavl: QLykPMMghQkBzNKJlfgFZKhZZUmaNrQv[EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm] for EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm, powGafreWfwlSAqPpTpUhFgpFVqCPavl in rsURCWTCboilKpKjxalFpgfvAczsBquq.items()}
    CEnzWRPlAkrAPTleHjeuQDNBUauFknlt = ["q", "k", "v", "proj_out"]
    for EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm, powGafreWfwlSAqPpTpUhFgpFVqCPavl in NtwbWJftksJLJogLEhqgoCQhMuuhOeqR.items():
        for NZOMBEFWqRKHmDPkcUYaUTPkcxKoVTSG in CEnzWRPlAkrAPTleHjeuQDNBUauFknlt:
            if f"mid.attn_1.{weight_name}.weight" in EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm:
                print(f"Reshaping {k} for SD format")
                NtwbWJftksJLJogLEhqgoCQhMuuhOeqR[EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm] = bMIZtKofdGCLugAAeSxBNXLRdAzwttMg(powGafreWfwlSAqPpTpUhFgpFVqCPavl)
    return NtwbWJftksJLJogLEhqgoCQhMuuhOeqR
VRQfHqxjjaPAVTNtOYdYMjLUpwCjRPHG = [
    ("resblocks.", "text_model.encoder.layers."),
    ("ln_1", "layer_norm1"),
    ("ln_2", "layer_norm2"),
    (".c_fc.", ".fc1."),
    (".c_proj.", ".fc2."),
    (".attn", ".self_attn"),
    ("ln_final.", "transformer.text_model.final_layer_norm."),
    ("token_embedding.weight", "transformer.text_model.embeddings.token_embedding.weight"),
    ("positional_embedding", "transformer.text_model.embeddings.position_embedding.weight"),
]
BNRKRIUmvWVrvKtYcQLmmRxqBalGcEhO = {re.escape(NECAaWUrFGIXcLimrerEYmxYIykQBfXb[1]): NECAaWUrFGIXcLimrerEYmxYIykQBfXb[0] for NECAaWUrFGIXcLimrerEYmxYIykQBfXb in VRQfHqxjjaPAVTNtOYdYMjLUpwCjRPHG}
SkEFifPtYJYBmnewcVvaYjmsyVzwbyxv = re.compile("|".join(BNRKRIUmvWVrvKtYcQLmmRxqBalGcEhO.keys()))
utKozdMNuHDqbbhBEhodIVYStygDgYJI = {"q": 0, "k": 1, "v": 2}
def wUrAXRxmwTySRsKvyhTJhkkYRzPmNEiw(text_enc_dict, mAocOLWlgMJvPYVmSRndfhQdAcKHgPwi=""):
    NtwbWJftksJLJogLEhqgoCQhMuuhOeqR = {}
    XhKTxiXGUwWKKWzQNKhZnCFeFXRvMZiO = {}
    QMnDDSTAgYNTxLzjGeRJqmjzhcUerWfi = {}
    for EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm, powGafreWfwlSAqPpTpUhFgpFVqCPavl in text_enc_dict.items():
        if not EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm.startswith(mAocOLWlgMJvPYVmSRndfhQdAcKHgPwi):
            continue
        if (
                EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm.endswith(".self_attn.q_proj.weight")
                or EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm.endswith(".self_attn.k_proj.weight")
                or EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm.endswith(".self_attn.v_proj.weight")
        ):
            VtAuqKInTzRvbTitMmWkiMRwCZnVvimF = EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm[: -len(".q_proj.weight")]
            lxpvmyXfjVVlUseDVzmEuPFAiwXSoEwH = EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm[-len("q_proj.weight")]
            if VtAuqKInTzRvbTitMmWkiMRwCZnVvimF not in XhKTxiXGUwWKKWzQNKhZnCFeFXRvMZiO:
                XhKTxiXGUwWKKWzQNKhZnCFeFXRvMZiO[VtAuqKInTzRvbTitMmWkiMRwCZnVvimF] = [None, None, None]
            XhKTxiXGUwWKKWzQNKhZnCFeFXRvMZiO[VtAuqKInTzRvbTitMmWkiMRwCZnVvimF][utKozdMNuHDqbbhBEhodIVYStygDgYJI[lxpvmyXfjVVlUseDVzmEuPFAiwXSoEwH]] = powGafreWfwlSAqPpTpUhFgpFVqCPavl
            continue
        if (
                EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm.endswith(".self_attn.q_proj.bias")
                or EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm.endswith(".self_attn.k_proj.bias")
                or EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm.endswith(".self_attn.v_proj.bias")
        ):
            VtAuqKInTzRvbTitMmWkiMRwCZnVvimF = EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm[: -len(".q_proj.bias")]
            lxpvmyXfjVVlUseDVzmEuPFAiwXSoEwH = EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm[-len("q_proj.bias")]
            if VtAuqKInTzRvbTitMmWkiMRwCZnVvimF not in QMnDDSTAgYNTxLzjGeRJqmjzhcUerWfi:
                QMnDDSTAgYNTxLzjGeRJqmjzhcUerWfi[VtAuqKInTzRvbTitMmWkiMRwCZnVvimF] = [None, None, None]
            QMnDDSTAgYNTxLzjGeRJqmjzhcUerWfi[VtAuqKInTzRvbTitMmWkiMRwCZnVvimF][utKozdMNuHDqbbhBEhodIVYStygDgYJI[lxpvmyXfjVVlUseDVzmEuPFAiwXSoEwH]] = powGafreWfwlSAqPpTpUhFgpFVqCPavl
            continue
        FNncfUWIVSZNyRchqQXolEOrYQLOdGtr = SkEFifPtYJYBmnewcVvaYjmsyVzwbyxv.sub(lambda FTosLGldclAzaiNbwuLMIEtXfrZQpTnU: BNRKRIUmvWVrvKtYcQLmmRxqBalGcEhO[re.escape(FTosLGldclAzaiNbwuLMIEtXfrZQpTnU.EBSqSRjSGRxQZGLBDNBFhqftXyLrzJTb(0))], EWOrdNFMIwTeWNNYWAYyRJvhctFfHPqm)
        NtwbWJftksJLJogLEhqgoCQhMuuhOeqR[FNncfUWIVSZNyRchqQXolEOrYQLOdGtr] = powGafreWfwlSAqPpTpUhFgpFVqCPavl
    for VtAuqKInTzRvbTitMmWkiMRwCZnVvimF, ibpplCpMyGvmcNhdPbuiRzLXosZnzkul in XhKTxiXGUwWKKWzQNKhZnCFeFXRvMZiO.items():
        if None in ibpplCpMyGvmcNhdPbuiRzLXosZnzkul:
            raise Exception("CORRUPTED MODEL: one of the q-k-v values for the text encoder was missing")
        FNncfUWIVSZNyRchqQXolEOrYQLOdGtr = SkEFifPtYJYBmnewcVvaYjmsyVzwbyxv.sub(lambda FTosLGldclAzaiNbwuLMIEtXfrZQpTnU: BNRKRIUmvWVrvKtYcQLmmRxqBalGcEhO[re.escape(FTosLGldclAzaiNbwuLMIEtXfrZQpTnU.EBSqSRjSGRxQZGLBDNBFhqftXyLrzJTb(0))], VtAuqKInTzRvbTitMmWkiMRwCZnVvimF)
        NtwbWJftksJLJogLEhqgoCQhMuuhOeqR[FNncfUWIVSZNyRchqQXolEOrYQLOdGtr + ".in_proj_weight"] = torch.cat(ibpplCpMyGvmcNhdPbuiRzLXosZnzkul)
    for VtAuqKInTzRvbTitMmWkiMRwCZnVvimF, ibpplCpMyGvmcNhdPbuiRzLXosZnzkul in QMnDDSTAgYNTxLzjGeRJqmjzhcUerWfi.items():
        if None in ibpplCpMyGvmcNhdPbuiRzLXosZnzkul:
            raise Exception("CORRUPTED MODEL: one of the q-k-v values for the text encoder was missing")
        FNncfUWIVSZNyRchqQXolEOrYQLOdGtr = SkEFifPtYJYBmnewcVvaYjmsyVzwbyxv.sub(lambda FTosLGldclAzaiNbwuLMIEtXfrZQpTnU: BNRKRIUmvWVrvKtYcQLmmRxqBalGcEhO[re.escape(FTosLGldclAzaiNbwuLMIEtXfrZQpTnU.EBSqSRjSGRxQZGLBDNBFhqftXyLrzJTb(0))], VtAuqKInTzRvbTitMmWkiMRwCZnVvimF)
        NtwbWJftksJLJogLEhqgoCQhMuuhOeqR[FNncfUWIVSZNyRchqQXolEOrYQLOdGtr + ".in_proj_bias"] = torch.cat(ibpplCpMyGvmcNhdPbuiRzLXosZnzkul)
    return NtwbWJftksJLJogLEhqgoCQhMuuhOeqR
def eAgcZYmnHQiguoukMyIhWoevMjaMfhJD(text_enc_dict):
    return text_enc_dict
