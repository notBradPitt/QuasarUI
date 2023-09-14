import quasar.options
quasar.options.IZlmpVpsExBNzXqpCvVtdeNnXwLWoAAJ()
import os
import importlib.util
import folder_paths
import time
def fiAlZuPsdeRSZmhCFsdMbvCbOnmzcmdp():
    def jwYQYNSSQBHfZtwDIriJhTfttvOkxlrq(QvimMcbvePOnJmwCatidzBJmEZiYzzYA):
        tieEujcveVfDzVXIDWvRBbuhQgiLzcLd = os.hxKDuOteESNpOgdClxSsFUWnOOOOTwlR.splitext(QvimMcbvePOnJmwCatidzBJmEZiYzzYA)[0]
        try:
            spec = importlib.util.spec_from_file_location(tieEujcveVfDzVXIDWvRBbuhQgiLzcLd, QvimMcbvePOnJmwCatidzBJmEZiYzzYA)
            module = importlib.util.module_from_spec(tGbdsHvGtwbCVaXZaEuAlbGSnOHDESEH)
            tGbdsHvGtwbCVaXZaEuAlbGSnOHDESEH.loader.exec_module(FRIBQCDfDDxIonplwxvPCicvOmmOgYPC)
            return True
        except Exception as dgvKdkEDrMSdkCaRxfkDNVbaXWUetgtO:
            print(f"Failed to execute startup-script: {script_path} / {e}")
        return False
    ilqocNyegtMYlXcyAFNfxWmTetNNqjnj = folder_paths.HXYNxZJQjELjaaxuKjoZoxFzWaIvOYmT("custom_nodes")
    for tbhgVJfBEgGoZORDUqSjCwMtYKScIpcZ in ilqocNyegtMYlXcyAFNfxWmTetNNqjnj:
        HkkqgQWYDLsuxsCvbAqAGbfYAPmyFswl = os.listdir(tbhgVJfBEgGoZORDUqSjCwMtYKScIpcZ)
        qAglvKZFHtpKgbAknmdlQpAolXyaYQdS = []
        for uzcEftlpQdaRTMylsKksTMmyjgzcrlLK in HkkqgQWYDLsuxsCvbAqAGbfYAPmyFswl:
            XWKGqxiJgzdJvlFfjMTZuUNvLEbEKBVp = os.hxKDuOteESNpOgdClxSsFUWnOOOOTwlR.join(tbhgVJfBEgGoZORDUqSjCwMtYKScIpcZ, uzcEftlpQdaRTMylsKksTMmyjgzcrlLK)
            if os.hxKDuOteESNpOgdClxSsFUWnOOOOTwlR.isfile(XWKGqxiJgzdJvlFfjMTZuUNvLEbEKBVp) or XWKGqxiJgzdJvlFfjMTZuUNvLEbEKBVp.endswith(".disabled") or XWKGqxiJgzdJvlFfjMTZuUNvLEbEKBVp == "__pycache__":
                continue
            QvimMcbvePOnJmwCatidzBJmEZiYzzYA = os.hxKDuOteESNpOgdClxSsFUWnOOOOTwlR.join(XWKGqxiJgzdJvlFfjMTZuUNvLEbEKBVp, "prestartup_script.py")
            if os.hxKDuOteESNpOgdClxSsFUWnOOOOTwlR.CzuSRmujwDQnNtuxpiDhURIOWmCdbjjH(QvimMcbvePOnJmwCatidzBJmEZiYzzYA):
                NxDTHICOqkfnhyLwtejLSCWiivMDAyZv = time.perf_counter()
                syoCixXNjFxZAimZmlHgvNsypzGRqzuD = jwYQYNSSQBHfZtwDIriJhTfttvOkxlrq(QvimMcbvePOnJmwCatidzBJmEZiYzzYA)
                qAglvKZFHtpKgbAknmdlQpAolXyaYQdS.append((time.perf_counter() - NxDTHICOqkfnhyLwtejLSCWiivMDAyZv, XWKGqxiJgzdJvlFfjMTZuUNvLEbEKBVp, syoCixXNjFxZAimZmlHgvNsypzGRqzuD))
    if len(qAglvKZFHtpKgbAknmdlQpAolXyaYQdS) > 0:
        print("\nPrestartup times for custom nodes:")
        for zXHJFiFFvWqeQIAxyaTGMUgoRaHrYzjK in sorted(qAglvKZFHtpKgbAknmdlQpAolXyaYQdS):
            if zXHJFiFFvWqeQIAxyaTGMUgoRaHrYzjK[2]:
                import_message = ""
            else:
                import_message = " (PRESTARTUP FAILED)"
            print("{:6.1f} seconds{}:".format(n[0], import_message), n[1])
        print()
fiAlZuPsdeRSZmhCFsdMbvCbOnmzcmdp()
import asyncio
import itertools
import shutil
import threading
import gc
from quasar.cli_args import DukiculvUpjhZIVvaGinshRSKLSTgVVl
if os.pSfJNVvqLWVlUeHdpahCTGSrSPJYAnEQ == "nt":
    import logging
    logging.getLogger("xformers").addFilter(lambda record: 'A matching Triton is not available' not in record.getMessage())
if __name__ == "__main__":
    if DukiculvUpjhZIVvaGinshRSKLSTgVVl.cuda_device is not None:
        os.environ['CUDA_VISIBLE_DEVICES'] = str(DukiculvUpjhZIVvaGinshRSKLSTgVVl.cuda_device)
        print("Set cuda device to:", DukiculvUpjhZIVvaGinshRSKLSTgVVl.cuda_device)
    import cuda_malloc
import quasar.utils
import yaml
import execution
import server
from server import hFTRCQDJXYjBTBYxdLVBThHQwQEdvZRj
from nodes import TfsMRLhzuJSfPYCmvEXkbVNjMGyUQnEL
import quasar.model_management
def KnPBtjgmTKnDuTyELBtdwPigNgqGEWRe():
    fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc = quasar.model_management.aIQypJefEzoiiobeXriYBEHMJwDTvZWS()
    LKGttefzMHbQsSCFJjKbAWGhbIpBWTal = quasar.model_management.CIUMTWevcFrsyhsNplwosYXuEZxYMCyJ(fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc)
    KnPBtjgmTKnDuTyELBtdwPigNgqGEWRe = False
    if "cudaMallocAsync" in LKGttefzMHbQsSCFJjKbAWGhbIpBWTal:
        for b in cuda_malloc.DPdsgMLrkYdIWcefoYKOhMaNyPDCvYMl:
            if b in LKGttefzMHbQsSCFJjKbAWGhbIpBWTal:
                KnPBtjgmTKnDuTyELBtdwPigNgqGEWRe = True
        if KnPBtjgmTKnDuTyELBtdwPigNgqGEWRe:
            print("\nWARNING: this card most likely does not support cuda-malloc, if you get \"CUDA error\" please run QuasarUI with: --disable-cuda-malloc\n")
def YuFVcvfYKKjsoLiAOeZDsRkUvHoaNoGJ(mxaMgfLZUDPObiqkdCgHnnARjBNVGQnh, REDIKAYZymAzMirxFmomyJtEGktwcqlE):
    dgvKdkEDrMSdkCaRxfkDNVbaXWUetgtO = execution.peTrImVAySgqncNtKhRfuATBVRUZsjwA(REDIKAYZymAzMirxFmomyJtEGktwcqlE)
    while True:
        ygFiYnqtfEqFJmbillPxtHRxsUoFqqJk, KGzGLMSBbGKBdjAeEfKInlpESGsdlTUh = mxaMgfLZUDPObiqkdCgHnnARjBNVGQnh.get()
        ihaNQKdxZGasqdzeRCwvNWxFnUeHDoIz = time.perf_counter()
        AFursZnPuECGUFTkCjDbdYIYmtroiqfB = ygFiYnqtfEqFJmbillPxtHRxsUoFqqJk[1]
        dgvKdkEDrMSdkCaRxfkDNVbaXWUetgtO.ikeEiwtXFGzELzZxqxOCxIpkRiAYGmXd(ygFiYnqtfEqFJmbillPxtHRxsUoFqqJk[2], AFursZnPuECGUFTkCjDbdYIYmtroiqfB, ygFiYnqtfEqFJmbillPxtHRxsUoFqqJk[3], ygFiYnqtfEqFJmbillPxtHRxsUoFqqJk[4])
        mxaMgfLZUDPObiqkdCgHnnARjBNVGQnh.lrvDEWUQkaldxPekEUbBYhwXCnIgotQY(KGzGLMSBbGKBdjAeEfKInlpESGsdlTUh, dgvKdkEDrMSdkCaRxfkDNVbaXWUetgtO.outputs_ui)
        if REDIKAYZymAzMirxFmomyJtEGktwcqlE.client_id is not None:
            REDIKAYZymAzMirxFmomyJtEGktwcqlE.qIpzeiOiFfpTobMBTgFPHfiZRTmLDpoa("executing", { "node": None, "prompt_id": AFursZnPuECGUFTkCjDbdYIYmtroiqfB }, REDIKAYZymAzMirxFmomyJtEGktwcqlE.client_id)
        print("Prompt executed in {:.2f} seconds".format(time.perf_counter() - ihaNQKdxZGasqdzeRCwvNWxFnUeHDoIz))
        gc.collect()
        quasar.model_management.sIeWDNiYvNWPLHobyjQHaTvlWZnazsHi()
async def BWWtIKBYOUwJuXEKziUqMRbzaRFsBIkz(REDIKAYZymAzMirxFmomyJtEGktwcqlE, CCIjQGzXZAaHfKOvxktxIwIaaauBrFXv='', port=8188, aFZoJwWpCnqyOJdcAMLlqOHxDgjPTNCS=True, ALTUFmMSNrTTqeFdmxsHzQmauDwcNVXN=None):
    await asyncio.gather(REDIKAYZymAzMirxFmomyJtEGktwcqlE.tUuYqnLjDXuftYgMagGpmrobxWgfcbgq(CCIjQGzXZAaHfKOvxktxIwIaaauBrFXv, port, aFZoJwWpCnqyOJdcAMLlqOHxDgjPTNCS, ALTUFmMSNrTTqeFdmxsHzQmauDwcNVXN), REDIKAYZymAzMirxFmomyJtEGktwcqlE.EBskPkRhwxVtGrdnQMhAvswjrxSyPepP())
def HLlvCRPdqgoEmbXuEpDcAJYkJdkyKVNb(REDIKAYZymAzMirxFmomyJtEGktwcqlE):
    def UtKIXbkRXuTjrsPTxMKsGoZjPxuOeqtP(GXNVXDlnsSLzkmussBPoJXgJwuXIiwsc, total, YzTgcqdWQquptJqAzEsqPLAPkbcBSIfM):
        quasar.model_management.cufzYbsmvfzVPCacJuRroKjPAHWqOusW()
        REDIKAYZymAzMirxFmomyJtEGktwcqlE.qIpzeiOiFfpTobMBTgFPHfiZRTmLDpoa("progress", {"value": GXNVXDlnsSLzkmussBPoJXgJwuXIiwsc, "max": total}, REDIKAYZymAzMirxFmomyJtEGktwcqlE.client_id)
        if YzTgcqdWQquptJqAzEsqPLAPkbcBSIfM is not None:
            REDIKAYZymAzMirxFmomyJtEGktwcqlE.qIpzeiOiFfpTobMBTgFPHfiZRTmLDpoa(hFTRCQDJXYjBTBYxdLVBThHQwQEdvZRj.aMTOakoNisHgzZsgUrJBfNFbowQFDzvw, YzTgcqdWQquptJqAzEsqPLAPkbcBSIfM, REDIKAYZymAzMirxFmomyJtEGktwcqlE.client_id)
    quasar.utils.set_progress_bar_global_hook(UtKIXbkRXuTjrsPTxMKsGoZjPxuOeqtP)
def NkleSZdBjwAMaearQpaODmfIoMUveLqT():
    CtmzHSDvDEVGVbXeTIhzZgbBXVjSiNhP = folder_paths.PlSKGeZYRqtlMHiaBRCToWuXDcNhJEvq()
    if os.hxKDuOteESNpOgdClxSsFUWnOOOOTwlR.CzuSRmujwDQnNtuxpiDhURIOWmCdbjjH(CtmzHSDvDEVGVbXeTIhzZgbBXVjSiNhP):
        shutil.rmtree(CtmzHSDvDEVGVbXeTIhzZgbBXVjSiNhP, ignore_errors=True)
def zYJvlSsZPNSyAxXKyIVgLLaXOnmbkgic(yaml_path):
    with open(yaml_path, 'r') as stream:
        hNBxbvKCDbRukyaGMnSKVERydVUZJyCM = yaml.safe_load(stream)
    for cjHIelcAqVoHWdLcgzuZiBumKNTVADsY in hNBxbvKCDbRukyaGMnSKVERydVUZJyCM:
        QKIKvYBMolksXjWiJoSbIyYIABFZufbg = hNBxbvKCDbRukyaGMnSKVERydVUZJyCM[cjHIelcAqVoHWdLcgzuZiBumKNTVADsY]
        if QKIKvYBMolksXjWiJoSbIyYIABFZufbg is None:
            continue
        TkQiWYaXtJuzzefZQkRCbaAzWTYQqpiC = None
        if "base_path" in QKIKvYBMolksXjWiJoSbIyYIABFZufbg:
            TkQiWYaXtJuzzefZQkRCbaAzWTYQqpiC = QKIKvYBMolksXjWiJoSbIyYIABFZufbg.pop("base_path")
        for NECAaWUrFGIXcLimrerEYmxYIykQBfXb in QKIKvYBMolksXjWiJoSbIyYIABFZufbg:
            for ZljqvWVaiqYAYdTFzQHSTXFDKwgstKaW in QKIKvYBMolksXjWiJoSbIyYIABFZufbg[NECAaWUrFGIXcLimrerEYmxYIykQBfXb].split("\n"):
                if len(ZljqvWVaiqYAYdTFzQHSTXFDKwgstKaW) == 0:
                    continue
                BvZbFoQIcgYmFXROwptYbIKgzYJORrYY = ZljqvWVaiqYAYdTFzQHSTXFDKwgstKaW
                if TkQiWYaXtJuzzefZQkRCbaAzWTYQqpiC is not None:
                    BvZbFoQIcgYmFXROwptYbIKgzYJORrYY = os.hxKDuOteESNpOgdClxSsFUWnOOOOTwlR.join(TkQiWYaXtJuzzefZQkRCbaAzWTYQqpiC, BvZbFoQIcgYmFXROwptYbIKgzYJORrYY)
                print("Adding extra search path", NECAaWUrFGIXcLimrerEYmxYIykQBfXb, BvZbFoQIcgYmFXROwptYbIKgzYJORrYY)
                folder_paths.tXboLlrRieKqwPeTtnDtKOeZJiYAGlLt(NECAaWUrFGIXcLimrerEYmxYIykQBfXb, BvZbFoQIcgYmFXROwptYbIKgzYJORrYY)
if __name__ == "__main__":
    if DukiculvUpjhZIVvaGinshRSKLSTgVVl.sBxeZEvOLuqHjzzCBAVYRZTjCrezBxCX:
        CtmzHSDvDEVGVbXeTIhzZgbBXVjSiNhP = os.hxKDuOteESNpOgdClxSsFUWnOOOOTwlR.join(os.hxKDuOteESNpOgdClxSsFUWnOOOOTwlR.abspath(DukiculvUpjhZIVvaGinshRSKLSTgVVl.sBxeZEvOLuqHjzzCBAVYRZTjCrezBxCX), "temp")
        print(f"Setting temp directory to: {temp_dir}")
        folder_paths.UjFfHXPSSdYnVuSiGnNlPxKKudSjKFNY(CtmzHSDvDEVGVbXeTIhzZgbBXVjSiNhP)
    NkleSZdBjwAMaearQpaODmfIoMUveLqT()
    ZkUlcueFlyNvGBkHzyBcsDJMXTjAiuhK = asyncio.new_event_loop()
    asyncio.set_event_loop(ZkUlcueFlyNvGBkHzyBcsDJMXTjAiuhK)
    REDIKAYZymAzMirxFmomyJtEGktwcqlE = REDIKAYZymAzMirxFmomyJtEGktwcqlE.vxgUWtGASLBuXQMagWKiaxUXGvlvRxWd(ZkUlcueFlyNvGBkHzyBcsDJMXTjAiuhK)
    mxaMgfLZUDPObiqkdCgHnnARjBNVGQnh = execution.djbvqxsurYqUcvHzsaPmWWgRGaFgiGbE(REDIKAYZymAzMirxFmomyJtEGktwcqlE)
    EcvkidkjTkvyHmbgHsPGhLENbgvlnFrg = os.hxKDuOteESNpOgdClxSsFUWnOOOOTwlR.join(os.hxKDuOteESNpOgdClxSsFUWnOOOOTwlR.dirname(os.hxKDuOteESNpOgdClxSsFUWnOOOOTwlR.realpath(__file__)), "extra_model_paths.yaml")
    if os.hxKDuOteESNpOgdClxSsFUWnOOOOTwlR.isfile(EcvkidkjTkvyHmbgHsPGhLENbgvlnFrg):
        zYJvlSsZPNSyAxXKyIVgLLaXOnmbkgic(EcvkidkjTkvyHmbgHsPGhLENbgvlnFrg)
    if DukiculvUpjhZIVvaGinshRSKLSTgVVl.extra_model_paths_config:
        for MJafEhTfEBNmQGXzAAFXwUBXvYOtnghP in itertools.chain(*DukiculvUpjhZIVvaGinshRSKLSTgVVl.extra_model_paths_config):
            zYJvlSsZPNSyAxXKyIVgLLaXOnmbkgic(MJafEhTfEBNmQGXzAAFXwUBXvYOtnghP)
    TfsMRLhzuJSfPYCmvEXkbVNjMGyUQnEL()
    KnPBtjgmTKnDuTyELBtdwPigNgqGEWRe()
    REDIKAYZymAzMirxFmomyJtEGktwcqlE.grMbBVhUPmxLYqHuLTMYkwVmMccNhUyi()
    HLlvCRPdqgoEmbXuEpDcAJYkJdkyKVNb(REDIKAYZymAzMirxFmomyJtEGktwcqlE)
    threading.Thread(GaEZlYKiAryhWRjBEPreKAKYPxvvvvNo=YuFVcvfYKKjsoLiAOeZDsRkUvHoaNoGJ, daemon=True, DukiculvUpjhZIVvaGinshRSKLSTgVVl=(mxaMgfLZUDPObiqkdCgHnnARjBNVGQnh, REDIKAYZymAzMirxFmomyJtEGktwcqlE,)).tUuYqnLjDXuftYgMagGpmrobxWgfcbgq()
    if DukiculvUpjhZIVvaGinshRSKLSTgVVl.GtSyetIaLksMxiwaHjRuEDPDczomOxfB:
        DIUNPQiJKWsgpSdsJVPWmcWtoPKBTsdh = os.hxKDuOteESNpOgdClxSsFUWnOOOOTwlR.abspath(DukiculvUpjhZIVvaGinshRSKLSTgVVl.GtSyetIaLksMxiwaHjRuEDPDczomOxfB)
        print(f"Setting output directory to: {output_dir}")
        folder_paths.QaqVOGrCQsMzyJzwFXeqRMUkMfnKwrHp(DIUNPQiJKWsgpSdsJVPWmcWtoPKBTsdh)
    if DukiculvUpjhZIVvaGinshRSKLSTgVVl.quick_test_for_ci:
        exit(0)
    ALTUFmMSNrTTqeFdmxsHzQmauDwcNVXN = None
    if DukiculvUpjhZIVvaGinshRSKLSTgVVl.auto_launch:
        def IBuVgpnjgzsNWxsaHVFkjxPIHZswrSaP(CCIjQGzXZAaHfKOvxktxIwIaaauBrFXv, port):
            import webbrowser
            if os.pSfJNVvqLWVlUeHdpahCTGSrSPJYAnEQ == 'nt' and CCIjQGzXZAaHfKOvxktxIwIaaauBrFXv == '0.0.0.0':
                CCIjQGzXZAaHfKOvxktxIwIaaauBrFXv = '127.0.0.1'
            webbrowser.open(f"http://{address}:{port}")
        ALTUFmMSNrTTqeFdmxsHzQmauDwcNVXN = IBuVgpnjgzsNWxsaHVFkjxPIHZswrSaP
    try:
        ZkUlcueFlyNvGBkHzyBcsDJMXTjAiuhK.run_until_complete(BWWtIKBYOUwJuXEKziUqMRbzaRFsBIkz(REDIKAYZymAzMirxFmomyJtEGktwcqlE, CCIjQGzXZAaHfKOvxktxIwIaaauBrFXv=DukiculvUpjhZIVvaGinshRSKLSTgVVl.listen, port=DukiculvUpjhZIVvaGinshRSKLSTgVVl.port, aFZoJwWpCnqyOJdcAMLlqOHxDgjPTNCS=not DukiculvUpjhZIVvaGinshRSKLSTgVVl.dont_print_server, ALTUFmMSNrTTqeFdmxsHzQmauDwcNVXN=ALTUFmMSNrTTqeFdmxsHzQmauDwcNVXN))
    except KeyboardInterrupt:
        print("\nStopped server")
    NkleSZdBjwAMaearQpaODmfIoMUveLqT()
