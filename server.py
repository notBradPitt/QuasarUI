import os
import sys
import asyncio
import traceback
import nodes
import folder_paths
import execution
import uuid
import urllib
import json
import glob
import struct
from PIL import Image, ImageOps
from PIL.PngImagePlugin import PngInfo
from io import BytesIO
try:
    import aiohttp
    from aiohttp import web
except ImportError:
    print("Module 'aiohttp' not installed. Please install it via:")
    print("pip install aiohttp")
    print("or")
    print("pip install -r requirements.txt")
    sys.exit()
import mimetypes
from quasar.cli_args import DukiculvUpjhZIVvaGinshRSKLSTgVVl
import quasar.utils
import quasar.model_management
class hFTRCQDJXYjBTBYxdLVBThHQwQEdvZRj:
    fdlOyZPXWscvoPcQnxxSXdTqmBFxYGDC = 1
    aMTOakoNisHgzZsgUrJBfNFbowQFDzvw = 2
async def xorVUCSjBcCTFixHnjvWgKQmsHYbOoVo(function, JWcvhhSkkAOvOUymGHSWwtMPsUYfbjKO):
    try:
        await function(JWcvhhSkkAOvOUymGHSWwtMPsUYfbjKO)
    except (aiohttp.ClientError, aiohttp.ClientPayloadError, ConnectionResetError) as err:
        print("send error:", err)
@web.middleware
async def gTdSYsyqSyzZdxppfmfsQjsLzkfgXAWR(request: web.Request, TQLMHpzrGHfkKPXOsLxdKBpLrtwSARMk):
    HQlvpyIUUfnfAqKdXyNavyxWXIZkebhk: web.Response = await TQLMHpzrGHfkKPXOsLxdKBpLrtwSARMk(request)
    if request.hxKDuOteESNpOgdClxSsFUWnOOOOTwlR.endswith('.js') or request.hxKDuOteESNpOgdClxSsFUWnOOOOTwlR.endswith('.css'):
        HQlvpyIUUfnfAqKdXyNavyxWXIZkebhk.NUSNKSqfxpvkMAXRONBFajOilLgzJzSm.setdefault('Cache-Control', 'no-cache')
    return HQlvpyIUUfnfAqKdXyNavyxWXIZkebhk
def kVJnBFzyJfOcsuvfeUuXqelGIlFkuGfz(allowed_origin: str):
    @web.middleware
    async def WYeSZQeouHqjIGTlhjoOULhovHfQOTjM(request: web.Request, TQLMHpzrGHfkKPXOsLxdKBpLrtwSARMk):
        if request.RISfvMcsyLUOJmTUeflroCerpGkgEWru == "OPTIONS":
            HQlvpyIUUfnfAqKdXyNavyxWXIZkebhk = web.Response()
        else:
            HQlvpyIUUfnfAqKdXyNavyxWXIZkebhk = await TQLMHpzrGHfkKPXOsLxdKBpLrtwSARMk(request)
        HQlvpyIUUfnfAqKdXyNavyxWXIZkebhk.NUSNKSqfxpvkMAXRONBFajOilLgzJzSm['Access-Control-Allow-Origin'] = allowed_origin
        HQlvpyIUUfnfAqKdXyNavyxWXIZkebhk.NUSNKSqfxpvkMAXRONBFajOilLgzJzSm['Access-Control-Allow-Methods'] = 'POST, GET, DELETE, PUT, OPTIONS'
        HQlvpyIUUfnfAqKdXyNavyxWXIZkebhk.NUSNKSqfxpvkMAXRONBFajOilLgzJzSm['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
        HQlvpyIUUfnfAqKdXyNavyxWXIZkebhk.NUSNKSqfxpvkMAXRONBFajOilLgzJzSm['Access-Control-Allow-Credentials'] = 'true'
        return HQlvpyIUUfnfAqKdXyNavyxWXIZkebhk
    return WYeSZQeouHqjIGTlhjoOULhovHfQOTjM
class vxgUWtGASLBuXQMagWKiaxUXGvlvRxWd():
    def __init__(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, ZkUlcueFlyNvGBkHzyBcsDJMXTjAiuhK):
        vxgUWtGASLBuXQMagWKiaxUXGvlvRxWd.instance = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS
        mimetypes.init()
        mimetypes.types_map['.js'] = 'application/javascript; charset=utf-8'
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.supports = ["custom_nodes_from_web"]
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.prompt_queue = None
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.ZkUlcueFlyNvGBkHzyBcsDJMXTjAiuhK = ZkUlcueFlyNvGBkHzyBcsDJMXTjAiuhK
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.messages = asyncio.Queue()
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.FCVsdRzGunasBiYAXHkNdLEMUdcXuHLD = 0
        ERfeZxZHuDRYhLDbLyBUSFlhtNGNkADD = [gTdSYsyqSyzZdxppfmfsQjsLzkfgXAWR]
        if DukiculvUpjhZIVvaGinshRSKLSTgVVl.enable_cors_header:
            ERfeZxZHuDRYhLDbLyBUSFlhtNGNkADD.append(kVJnBFzyJfOcsuvfeUuXqelGIlFkuGfz(DukiculvUpjhZIVvaGinshRSKLSTgVVl.enable_cors_header))
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.app = web.Application(client_max_size=104857600, ERfeZxZHuDRYhLDbLyBUSFlhtNGNkADD=ERfeZxZHuDRYhLDbLyBUSFlhtNGNkADD)
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.sockets = dict()
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.web_root = os.hxKDuOteESNpOgdClxSsFUWnOOOOTwlR.join(os.hxKDuOteESNpOgdClxSsFUWnOOOOTwlR.dirname(
            os.hxKDuOteESNpOgdClxSsFUWnOOOOTwlR.realpath(__file__)), "web")
        bodEVTWCiQtEgnHDFZUfegjtZIcDqMqP = web.RouteTableDef()
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.bodEVTWCiQtEgnHDFZUfegjtZIcDqMqP = bodEVTWCiQtEgnHDFZUfegjtZIcDqMqP
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.last_node_id = None
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.client_id = None
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.on_prompt_handlers = []
        @bodEVTWCiQtEgnHDFZUfegjtZIcDqMqP.get('/ws')
        async def QoURWDAcNYtjrCckygOtFKpOeuMgBDQL(request):
            xMUuFtzQyRMgVTNGJlNLnSTHJqLOlsTi = web.WebSocketResponse()
            await xMUuFtzQyRMgVTNGJlNLnSTHJqLOlsTi.prepare(request)
            JSUFYNwccnkWErsvCCtXGLoDRqOUNtXT = request.rel_url.oFxedobBnFbKeewIgTfUgblKziGvmndF.get('clientId', '')
            if JSUFYNwccnkWErsvCCtXGLoDRqOUNtXT:
                rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.sockets.pop(JSUFYNwccnkWErsvCCtXGLoDRqOUNtXT, None)
            else:
                JSUFYNwccnkWErsvCCtXGLoDRqOUNtXT = uuid.uuid4().hex
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.sockets[JSUFYNwccnkWErsvCCtXGLoDRqOUNtXT] = xMUuFtzQyRMgVTNGJlNLnSTHJqLOlsTi
            try:
                await rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.BUmulCEcJXhvafjQvItCTXiuvSjzjSFf("status", { "status": rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.yvrrxYUiqVgrQsYWMxXZEJxnLIUXDnbr(), 'sid': JSUFYNwccnkWErsvCCtXGLoDRqOUNtXT }, JSUFYNwccnkWErsvCCtXGLoDRqOUNtXT)
                if rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.client_id == JSUFYNwccnkWErsvCCtXGLoDRqOUNtXT and rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.last_node_id is not None:
                    await rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.BUmulCEcJXhvafjQvItCTXiuvSjzjSFf("executing", { "node": rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.last_node_id }, JSUFYNwccnkWErsvCCtXGLoDRqOUNtXT)
                async for ajOmIBaJxAXoIDFumJtKcydIEAgfQgwV in xMUuFtzQyRMgVTNGJlNLnSTHJqLOlsTi:
                    if ajOmIBaJxAXoIDFumJtKcydIEAgfQgwV.type == aiohttp.WSMsgType.ERROR:
                        print('ws connection closed with exception %s' % xMUuFtzQyRMgVTNGJlNLnSTHJqLOlsTi.exception())
            finally:
                rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.sockets.pop(JSUFYNwccnkWErsvCCtXGLoDRqOUNtXT, None)
            return xMUuFtzQyRMgVTNGJlNLnSTHJqLOlsTi
        @bodEVTWCiQtEgnHDFZUfegjtZIcDqMqP.get("/")
        async def FGJeUnySFrmAvzDAPVrFYSXjeWbMRfbH(request):
            return web.FileResponse(os.hxKDuOteESNpOgdClxSsFUWnOOOOTwlR.join(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.web_root, "index.html"))
        @bodEVTWCiQtEgnHDFZUfegjtZIcDqMqP.get("/embeddings")
        def hmlvbUOjPqAxkIEFxrNPhdBXMFcIlqYU(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS):
            CQDUGzeqFbhJuPQwIUXzCwYMkQNapRqX = folder_paths.DYvodbeLLCWlQGasCGeYTFNFKZRpPvmd("embeddings")
            return web.json_response(list(map(lambda GlZreLQjBCiBptpFgmbsMbhjFlMgPVav: os.hxKDuOteESNpOgdClxSsFUWnOOOOTwlR.splitext(GlZreLQjBCiBptpFgmbsMbhjFlMgPVav)[0], CQDUGzeqFbhJuPQwIUXzCwYMkQNapRqX)))
        @bodEVTWCiQtEgnHDFZUfegjtZIcDqMqP.get("/extensions")
        async def asqcLFixlaHkeYsvIjaQBKNMuqurkiju(request):
            DTcHrFlDIwbrZDZHTOmAOTxRFqptCgyE = glob.glob(os.hxKDuOteESNpOgdClxSsFUWnOOOOTwlR.join(
                rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.web_root, 'extensions/**/*.js'), recursive=True)
            HnjgYzcYVPzWBFjtnXmWmmBUkGpTxjgv = list(map(lambda f: "/" + os.hxKDuOteESNpOgdClxSsFUWnOOOOTwlR.relpath(f, rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.web_root).replace("\\", "/"), files))
            for pSfJNVvqLWVlUeHdpahCTGSrSPJYAnEQ, dir in nodes.OhQOpxGGCySHXalbRgaNhmvFYyGbOLxZ.items():
                DTcHrFlDIwbrZDZHTOmAOTxRFqptCgyE = glob.glob(os.hxKDuOteESNpOgdClxSsFUWnOOOOTwlR.join(dir, '**/*.js'), recursive=True)
                HnjgYzcYVPzWBFjtnXmWmmBUkGpTxjgv.extend(list(map(lambda f: "/extensions/" + urllib.parse.quote(
                    pSfJNVvqLWVlUeHdpahCTGSrSPJYAnEQ) + "/" + os.hxKDuOteESNpOgdClxSsFUWnOOOOTwlR.relpath(f, dir).replace("\\", "/"), files)))
            return web.json_response(HnjgYzcYVPzWBFjtnXmWmmBUkGpTxjgv)
        def mZYpkoTuRffoqoPxsmINFTYRYhLkpbHy(ZYvUveSnZKyFJUuTpSPHWUbByngGqELv):
            if ZYvUveSnZKyFJUuTpSPHWUbByngGqELv is None:
                ZYvUveSnZKyFJUuTpSPHWUbByngGqELv = "input"
            if ZYvUveSnZKyFJUuTpSPHWUbByngGqELv == "input":
                cDlRhmZPZRskqARoapdcoOJOluPSwrzz = folder_paths.oLxzopmIeTVwZiWTpRvVAVRpJiaEjmiS()
            elif ZYvUveSnZKyFJUuTpSPHWUbByngGqELv == "temp":
                cDlRhmZPZRskqARoapdcoOJOluPSwrzz = folder_paths.PlSKGeZYRqtlMHiaBRCToWuXDcNhJEvq()
            elif ZYvUveSnZKyFJUuTpSPHWUbByngGqELv == "output":
                cDlRhmZPZRskqARoapdcoOJOluPSwrzz = folder_paths.gZpMXpjIEjIdWmJXOqOJEBRXYgziLydo()
            return cDlRhmZPZRskqARoapdcoOJOluPSwrzz, ZYvUveSnZKyFJUuTpSPHWUbByngGqELv
        def CQuEhVDJIArLptcdZJgLHnckLEDjrJtL(PWqGBaLAYfSwazFeBMSGmrXYXGQgzIGF, xJzyJWyjsuhrwoIFRCpWeXDLAVxVqiuV=None):
            eLyJtroPthPCROYWyMphoIrGatNOOXCO = PWqGBaLAYfSwazFeBMSGmrXYXGQgzIGF.get("image")
            BqdnPlWzJYaJGGbgGrYQRDAElzLESGqo = PWqGBaLAYfSwazFeBMSGmrXYXGQgzIGF.get("overwrite")
            HgateTCGVeCKZNrFaoAbeXCcKNQOyZRh = PWqGBaLAYfSwazFeBMSGmrXYXGQgzIGF.get("type")
            mylQdErZMSvGLdXwKApSMtgbzVdSovfN, HgateTCGVeCKZNrFaoAbeXCcKNQOyZRh = mZYpkoTuRffoqoPxsmINFTYRYhLkpbHy(HgateTCGVeCKZNrFaoAbeXCcKNQOyZRh)
            if eLyJtroPthPCROYWyMphoIrGatNOOXCO and eLyJtroPthPCROYWyMphoIrGatNOOXCO.GGrVUpHsMvVvEYhZgyWAlwaKJQserwts:
                VpsbOZzufynrTFUvvRofTQeRCOCIKJOM = eLyJtroPthPCROYWyMphoIrGatNOOXCO.VpsbOZzufynrTFUvvRofTQeRCOCIKJOM
                if not VpsbOZzufynrTFUvvRofTQeRCOCIKJOM:
                    return web.Response(status=400)
                EijzAwkTdadIdbBCcDEUbEYNNcstskwi = PWqGBaLAYfSwazFeBMSGmrXYXGQgzIGF.get("subfolder", "")
                NSnmtWjKbAQhROMkmRknqzSaUCojgOin = os.hxKDuOteESNpOgdClxSsFUWnOOOOTwlR.join(mylQdErZMSvGLdXwKApSMtgbzVdSovfN, os.hxKDuOteESNpOgdClxSsFUWnOOOOTwlR.normpath(EijzAwkTdadIdbBCcDEUbEYNNcstskwi))
                jGKkchjlDQuvRrYKaTApaOEWXvxjRZoh = os.hxKDuOteESNpOgdClxSsFUWnOOOOTwlR.abspath(os.hxKDuOteESNpOgdClxSsFUWnOOOOTwlR.join(NSnmtWjKbAQhROMkmRknqzSaUCojgOin, VpsbOZzufynrTFUvvRofTQeRCOCIKJOM))
                if os.hxKDuOteESNpOgdClxSsFUWnOOOOTwlR.commonpath((mylQdErZMSvGLdXwKApSMtgbzVdSovfN, jGKkchjlDQuvRrYKaTApaOEWXvxjRZoh)) != mylQdErZMSvGLdXwKApSMtgbzVdSovfN:
                    return web.Response(status=400)
                if not os.hxKDuOteESNpOgdClxSsFUWnOOOOTwlR.CzuSRmujwDQnNtuxpiDhURIOWmCdbjjH(NSnmtWjKbAQhROMkmRknqzSaUCojgOin):
                    os.makedirs(NSnmtWjKbAQhROMkmRknqzSaUCojgOin)
                split = os.hxKDuOteESNpOgdClxSsFUWnOOOOTwlR.splitext(VpsbOZzufynrTFUvvRofTQeRCOCIKJOM)
                if BqdnPlWzJYaJGGbgGrYQRDAElzLESGqo is not None and (BqdnPlWzJYaJGGbgGrYQRDAElzLESGqo == "true" or BqdnPlWzJYaJGGbgGrYQRDAElzLESGqo == "1"):
                    pass
                else:
                    HCXmerBqIMuTscBONzTGKYapYSxWTYHo = 1
                    while os.hxKDuOteESNpOgdClxSsFUWnOOOOTwlR.CzuSRmujwDQnNtuxpiDhURIOWmCdbjjH(jGKkchjlDQuvRrYKaTApaOEWXvxjRZoh):
                        VpsbOZzufynrTFUvvRofTQeRCOCIKJOM = f"{split[0]} ({i}){split[1]}"
                        jGKkchjlDQuvRrYKaTApaOEWXvxjRZoh = os.hxKDuOteESNpOgdClxSsFUWnOOOOTwlR.join(NSnmtWjKbAQhROMkmRknqzSaUCojgOin, VpsbOZzufynrTFUvvRofTQeRCOCIKJOM)
                        HCXmerBqIMuTscBONzTGKYapYSxWTYHo += 1
                if xJzyJWyjsuhrwoIFRCpWeXDLAVxVqiuV is not None:
                    xJzyJWyjsuhrwoIFRCpWeXDLAVxVqiuV(eLyJtroPthPCROYWyMphoIrGatNOOXCO, PWqGBaLAYfSwazFeBMSGmrXYXGQgzIGF, jGKkchjlDQuvRrYKaTApaOEWXvxjRZoh)
                else:
                    with open(jGKkchjlDQuvRrYKaTApaOEWXvxjRZoh, "wb") as f:
                        f.write(eLyJtroPthPCROYWyMphoIrGatNOOXCO.GGrVUpHsMvVvEYhZgyWAlwaKJQserwts.read())
                return web.json_response({"name" : VpsbOZzufynrTFUvvRofTQeRCOCIKJOM, "subfolder": EijzAwkTdadIdbBCcDEUbEYNNcstskwi, "type": HgateTCGVeCKZNrFaoAbeXCcKNQOyZRh})
            else:
                return web.Response(status=400)
        @bodEVTWCiQtEgnHDFZUfegjtZIcDqMqP.PWqGBaLAYfSwazFeBMSGmrXYXGQgzIGF("/upload/image")
        async def AgNlpBFoKqqXUHWAiSqEkQkHeOqOCAvG(request):
            PWqGBaLAYfSwazFeBMSGmrXYXGQgzIGF = await request.PWqGBaLAYfSwazFeBMSGmrXYXGQgzIGF()
            return CQuEhVDJIArLptcdZJgLHnckLEDjrJtL(PWqGBaLAYfSwazFeBMSGmrXYXGQgzIGF)
        @bodEVTWCiQtEgnHDFZUfegjtZIcDqMqP.PWqGBaLAYfSwazFeBMSGmrXYXGQgzIGF("/upload/mask")
        async def uDKedUzkPtlGfpUUUFLibyltaGqNEXzl(request):
            PWqGBaLAYfSwazFeBMSGmrXYXGQgzIGF = await request.PWqGBaLAYfSwazFeBMSGmrXYXGQgzIGF()
            def xJzyJWyjsuhrwoIFRCpWeXDLAVxVqiuV(eLyJtroPthPCROYWyMphoIrGatNOOXCO, PWqGBaLAYfSwazFeBMSGmrXYXGQgzIGF, jGKkchjlDQuvRrYKaTApaOEWXvxjRZoh):
                OOliRAzneaJzEAQSAVWehbKoxVRnGhvj = json.loads(PWqGBaLAYfSwazFeBMSGmrXYXGQgzIGF.get("original_ref"))
                VpsbOZzufynrTFUvvRofTQeRCOCIKJOM, DIUNPQiJKWsgpSdsJVPWmcWtoPKBTsdh = folder_paths.ZouPnEJNuptYlYBxNIdTXWRhksIQlBbt(OOliRAzneaJzEAQSAVWehbKoxVRnGhvj['filename'])
                if VpsbOZzufynrTFUvvRofTQeRCOCIKJOM[0] == '/' or '..' in VpsbOZzufynrTFUvvRofTQeRCOCIKJOM:
                    return web.Response(status=400)
                if DIUNPQiJKWsgpSdsJVPWmcWtoPKBTsdh is None:
                    type = OOliRAzneaJzEAQSAVWehbKoxVRnGhvj.get("type", "output")
                    DIUNPQiJKWsgpSdsJVPWmcWtoPKBTsdh = folder_paths.kxrHWrKUsAImLcADDJwQctHfTpGpGvug(type)
                if DIUNPQiJKWsgpSdsJVPWmcWtoPKBTsdh is None:
                    return web.Response(status=400)
                if OOliRAzneaJzEAQSAVWehbKoxVRnGhvj.get("subfolder", "") != "":
                    sfJCZlvyEBNJKYZMOKZyjCBnsTwFUBVN = os.hxKDuOteESNpOgdClxSsFUWnOOOOTwlR.join(DIUNPQiJKWsgpSdsJVPWmcWtoPKBTsdh, OOliRAzneaJzEAQSAVWehbKoxVRnGhvj["subfolder"])
                    if os.hxKDuOteESNpOgdClxSsFUWnOOOOTwlR.commonpath((os.hxKDuOteESNpOgdClxSsFUWnOOOOTwlR.abspath(sfJCZlvyEBNJKYZMOKZyjCBnsTwFUBVN), DIUNPQiJKWsgpSdsJVPWmcWtoPKBTsdh)) != DIUNPQiJKWsgpSdsJVPWmcWtoPKBTsdh:
                        return web.Response(status=403)
                    DIUNPQiJKWsgpSdsJVPWmcWtoPKBTsdh = sfJCZlvyEBNJKYZMOKZyjCBnsTwFUBVN
                GGrVUpHsMvVvEYhZgyWAlwaKJQserwts = os.hxKDuOteESNpOgdClxSsFUWnOOOOTwlR.join(DIUNPQiJKWsgpSdsJVPWmcWtoPKBTsdh, VpsbOZzufynrTFUvvRofTQeRCOCIKJOM)
                if os.hxKDuOteESNpOgdClxSsFUWnOOOOTwlR.isfile(GGrVUpHsMvVvEYhZgyWAlwaKJQserwts):
                    with Image.open(GGrVUpHsMvVvEYhZgyWAlwaKJQserwts) as qMMEmvbOxpYzEAqulxKrFTpyCOrlCFTA:
                        bpGrrorhUTFbOXgOoJWMtNiVeQXHqzbi = PngInfo()
                        if hasattr(qMMEmvbOxpYzEAqulxKrFTpyCOrlCFTA,'text'):
                            for nyrzKxQtioheHIZujafABgijbCjrWhBU in qMMEmvbOxpYzEAqulxKrFTpyCOrlCFTA.text:
                                bpGrrorhUTFbOXgOoJWMtNiVeQXHqzbi.add_text(nyrzKxQtioheHIZujafABgijbCjrWhBU, qMMEmvbOxpYzEAqulxKrFTpyCOrlCFTA.text[nyrzKxQtioheHIZujafABgijbCjrWhBU])
                        qMMEmvbOxpYzEAqulxKrFTpyCOrlCFTA = qMMEmvbOxpYzEAqulxKrFTpyCOrlCFTA.convert('RGBA')
                        yxgMZgGuVGbXWHfPgRydDWQbFQUtVHCR = Image.open(eLyJtroPthPCROYWyMphoIrGatNOOXCO.GGrVUpHsMvVvEYhZgyWAlwaKJQserwts).convert('RGBA')
                        orissTTPtmtXIpKSMqkLrXaJamNDAofA = yxgMZgGuVGbXWHfPgRydDWQbFQUtVHCR.getchannel('A')
                        qMMEmvbOxpYzEAqulxKrFTpyCOrlCFTA.putalpha(orissTTPtmtXIpKSMqkLrXaJamNDAofA)
                        qMMEmvbOxpYzEAqulxKrFTpyCOrlCFTA.PXhZDpeqZAdDBfrowpMPOPAWwzXhVAFM(jGKkchjlDQuvRrYKaTApaOEWXvxjRZoh, compress_level=4, pnginfo=bpGrrorhUTFbOXgOoJWMtNiVeQXHqzbi)
            return CQuEhVDJIArLptcdZJgLHnckLEDjrJtL(PWqGBaLAYfSwazFeBMSGmrXYXGQgzIGF, xJzyJWyjsuhrwoIFRCpWeXDLAVxVqiuV)
        @bodEVTWCiQtEgnHDFZUfegjtZIcDqMqP.get("/view")
        async def RwavKKLCFmtLOTSQzYgsWaUvMCptvylN(request):
            if "filename" in request.rel_url.oFxedobBnFbKeewIgTfUgblKziGvmndF:
                VpsbOZzufynrTFUvvRofTQeRCOCIKJOM = request.rel_url.oFxedobBnFbKeewIgTfUgblKziGvmndF["filename"]
                VpsbOZzufynrTFUvvRofTQeRCOCIKJOM,DIUNPQiJKWsgpSdsJVPWmcWtoPKBTsdh = folder_paths.ZouPnEJNuptYlYBxNIdTXWRhksIQlBbt(VpsbOZzufynrTFUvvRofTQeRCOCIKJOM)
                if VpsbOZzufynrTFUvvRofTQeRCOCIKJOM[0] == '/' or '..' in VpsbOZzufynrTFUvvRofTQeRCOCIKJOM:
                    return web.Response(status=400)
                if DIUNPQiJKWsgpSdsJVPWmcWtoPKBTsdh is None:
                    type = request.rel_url.oFxedobBnFbKeewIgTfUgblKziGvmndF.get("type", "output")
                    DIUNPQiJKWsgpSdsJVPWmcWtoPKBTsdh = folder_paths.kxrHWrKUsAImLcADDJwQctHfTpGpGvug(type)
                if DIUNPQiJKWsgpSdsJVPWmcWtoPKBTsdh is None:
                    return web.Response(status=400)
                if "subfolder" in request.rel_url.oFxedobBnFbKeewIgTfUgblKziGvmndF:
                    sfJCZlvyEBNJKYZMOKZyjCBnsTwFUBVN = os.hxKDuOteESNpOgdClxSsFUWnOOOOTwlR.join(DIUNPQiJKWsgpSdsJVPWmcWtoPKBTsdh, request.rel_url.oFxedobBnFbKeewIgTfUgblKziGvmndF["subfolder"])
                    if os.hxKDuOteESNpOgdClxSsFUWnOOOOTwlR.commonpath((os.hxKDuOteESNpOgdClxSsFUWnOOOOTwlR.abspath(sfJCZlvyEBNJKYZMOKZyjCBnsTwFUBVN), DIUNPQiJKWsgpSdsJVPWmcWtoPKBTsdh)) != DIUNPQiJKWsgpSdsJVPWmcWtoPKBTsdh:
                        return web.Response(status=403)
                    DIUNPQiJKWsgpSdsJVPWmcWtoPKBTsdh = sfJCZlvyEBNJKYZMOKZyjCBnsTwFUBVN
                VpsbOZzufynrTFUvvRofTQeRCOCIKJOM = os.hxKDuOteESNpOgdClxSsFUWnOOOOTwlR.basename(VpsbOZzufynrTFUvvRofTQeRCOCIKJOM)
                GGrVUpHsMvVvEYhZgyWAlwaKJQserwts = os.hxKDuOteESNpOgdClxSsFUWnOOOOTwlR.join(DIUNPQiJKWsgpSdsJVPWmcWtoPKBTsdh, VpsbOZzufynrTFUvvRofTQeRCOCIKJOM)
                if os.hxKDuOteESNpOgdClxSsFUWnOOOOTwlR.isfile(GGrVUpHsMvVvEYhZgyWAlwaKJQserwts):
                    if 'preview' in request.rel_url.oFxedobBnFbKeewIgTfUgblKziGvmndF:
                        with Image.open(GGrVUpHsMvVvEYhZgyWAlwaKJQserwts) as UaFpXseNaoqfcpsDACQmTguYDZsTArhs:
                            FEjKaKqRBlOIxhuZQpcgqPPBnnOomKXF = request.rel_url.oFxedobBnFbKeewIgTfUgblKziGvmndF['preview'].split(';')
                            FpFMukbJEDsuvLMXLpkzFqwVQIiIOwjy = FEjKaKqRBlOIxhuZQpcgqPPBnnOomKXF[0]
                            if FpFMukbJEDsuvLMXLpkzFqwVQIiIOwjy not in ['webp', 'jpeg'] or 'a' in request.rel_url.oFxedobBnFbKeewIgTfUgblKziGvmndF.get('channel', ''):
                                FpFMukbJEDsuvLMXLpkzFqwVQIiIOwjy = 'webp'
                            VjCDDDhoOBHYwICKnNldLuMUvRwnLMaR = 90
                            if FEjKaKqRBlOIxhuZQpcgqPPBnnOomKXF[-1].isdigit():
                                VjCDDDhoOBHYwICKnNldLuMUvRwnLMaR = int(FEjKaKqRBlOIxhuZQpcgqPPBnnOomKXF[-1])
                            cwkONaVGEoylzHtriwkevQTGYiyvAsuQ = BytesIO()
                            if FpFMukbJEDsuvLMXLpkzFqwVQIiIOwjy in ['jpeg'] or request.rel_url.oFxedobBnFbKeewIgTfUgblKziGvmndF.get('channel', '') == 'rgb':
                                UaFpXseNaoqfcpsDACQmTguYDZsTArhs = UaFpXseNaoqfcpsDACQmTguYDZsTArhs.convert("RGB")
                            UaFpXseNaoqfcpsDACQmTguYDZsTArhs.PXhZDpeqZAdDBfrowpMPOPAWwzXhVAFM(cwkONaVGEoylzHtriwkevQTGYiyvAsuQ, format=FpFMukbJEDsuvLMXLpkzFqwVQIiIOwjy, VjCDDDhoOBHYwICKnNldLuMUvRwnLMaR=VjCDDDhoOBHYwICKnNldLuMUvRwnLMaR)
                            cwkONaVGEoylzHtriwkevQTGYiyvAsuQ.seek(0)
                            return web.Response(body=cwkONaVGEoylzHtriwkevQTGYiyvAsuQ.read(), content_type=f'image/{image_format}',
                                                NUSNKSqfxpvkMAXRONBFajOilLgzJzSm={"Content-Disposition": f"filename=\"{filename}\""})
                    if 'channel' not in request.rel_url.oFxedobBnFbKeewIgTfUgblKziGvmndF:
                        EiApFIHKVDYyxTYijPXtjyqRuQDlhpED = 'rgba'
                    else:
                        EiApFIHKVDYyxTYijPXtjyqRuQDlhpED = request.rel_url.oFxedobBnFbKeewIgTfUgblKziGvmndF["channel"]
                    if EiApFIHKVDYyxTYijPXtjyqRuQDlhpED == 'rgb':
                        with Image.open(GGrVUpHsMvVvEYhZgyWAlwaKJQserwts) as UaFpXseNaoqfcpsDACQmTguYDZsTArhs:
                            if UaFpXseNaoqfcpsDACQmTguYDZsTArhs.bPTwwoDdWiuYqhtrDEHoDbHGiYcwcsQC == "RGBA":
                                r, zjSCLdcRnfaSDwMwtPZkXXzptdHpOEDh, b, GlZreLQjBCiBptpFgmbsMbhjFlMgPVav = UaFpXseNaoqfcpsDACQmTguYDZsTArhs.split()
                                QiolJCrFzjsIjSCGOIYlUuUaUNGXSmFx = Image.merge('RGB', (r, zjSCLdcRnfaSDwMwtPZkXXzptdHpOEDh, b))
                            else:
                                QiolJCrFzjsIjSCGOIYlUuUaUNGXSmFx = UaFpXseNaoqfcpsDACQmTguYDZsTArhs.convert("RGB")
                            cwkONaVGEoylzHtriwkevQTGYiyvAsuQ = BytesIO()
                            QiolJCrFzjsIjSCGOIYlUuUaUNGXSmFx.PXhZDpeqZAdDBfrowpMPOPAWwzXhVAFM(cwkONaVGEoylzHtriwkevQTGYiyvAsuQ, format='PNG')
                            cwkONaVGEoylzHtriwkevQTGYiyvAsuQ.seek(0)
                            return web.Response(body=cwkONaVGEoylzHtriwkevQTGYiyvAsuQ.read(), content_type='image/png',
                                                NUSNKSqfxpvkMAXRONBFajOilLgzJzSm={"Content-Disposition": f"filename=\"{filename}\""})
                    elif EiApFIHKVDYyxTYijPXtjyqRuQDlhpED == 'a':
                        with Image.open(GGrVUpHsMvVvEYhZgyWAlwaKJQserwts) as UaFpXseNaoqfcpsDACQmTguYDZsTArhs:
                            if UaFpXseNaoqfcpsDACQmTguYDZsTArhs.bPTwwoDdWiuYqhtrDEHoDbHGiYcwcsQC == "RGBA":
                                _, _, _, GlZreLQjBCiBptpFgmbsMbhjFlMgPVav = UaFpXseNaoqfcpsDACQmTguYDZsTArhs.split()
                            else:
                                GlZreLQjBCiBptpFgmbsMbhjFlMgPVav = Image.new('L', UaFpXseNaoqfcpsDACQmTguYDZsTArhs.vqDBJgidQufnKyAltPYRqiKGjmztArDJ, 255)
                            MhtYuxrhaZZkjDcNfnetYDZLnHJurlFD = Image.new('RGBA', UaFpXseNaoqfcpsDACQmTguYDZsTArhs.vqDBJgidQufnKyAltPYRqiKGjmztArDJ)
                            MhtYuxrhaZZkjDcNfnetYDZLnHJurlFD.putalpha(GlZreLQjBCiBptpFgmbsMbhjFlMgPVav)
                            ysblJMcISKiGdMQiuXmzpZVCiHhPWccA = BytesIO()
                            MhtYuxrhaZZkjDcNfnetYDZLnHJurlFD.PXhZDpeqZAdDBfrowpMPOPAWwzXhVAFM(ysblJMcISKiGdMQiuXmzpZVCiHhPWccA, format='PNG')
                            ysblJMcISKiGdMQiuXmzpZVCiHhPWccA.seek(0)
                            return web.Response(body=ysblJMcISKiGdMQiuXmzpZVCiHhPWccA.read(), content_type='image/png',
                                                NUSNKSqfxpvkMAXRONBFajOilLgzJzSm={"Content-Disposition": f"filename=\"{filename}\""})
                    else:
                        return web.FileResponse(GGrVUpHsMvVvEYhZgyWAlwaKJQserwts, NUSNKSqfxpvkMAXRONBFajOilLgzJzSm={"Content-Disposition": f"filename=\"{filename}\""})
            return web.Response(status=404)
        @bodEVTWCiQtEgnHDFZUfegjtZIcDqMqP.get("/view_metadata/{folder_name}")
        async def YAtkowzUhzXxiigGvKTjgrslNGRktWWe(request):
            OiSDAWttaBayZhaRXvjSPjBrXgoDRtfZ = request.match_info.get("folder_name", None)
            if OiSDAWttaBayZhaRXvjSPjBrXgoDRtfZ is None:
                return web.Response(status=404)
            if not "filename" in request.rel_url.oFxedobBnFbKeewIgTfUgblKziGvmndF:
                return web.Response(status=404)
            VpsbOZzufynrTFUvvRofTQeRCOCIKJOM = request.rel_url.oFxedobBnFbKeewIgTfUgblKziGvmndF["filename"]
            if not VpsbOZzufynrTFUvvRofTQeRCOCIKJOM.endswith(".safetensors"):
                return web.Response(status=404)
            aCpBstybtvNanefrpKNRDFwTyFdYYqmv = folder_paths.TIUEGMgxYSpXjfhmEGzFnNfGAqtlBBKE(OiSDAWttaBayZhaRXvjSPjBrXgoDRtfZ, VpsbOZzufynrTFUvvRofTQeRCOCIKJOM)
            if aCpBstybtvNanefrpKNRDFwTyFdYYqmv is None:
                return web.Response(status=404)
            iqymPVpxyjOWChGwBkTemSzHJbnJdAIz = quasar.utils.safetensors_header(aCpBstybtvNanefrpKNRDFwTyFdYYqmv, jedJBMoSqKrLwfdHJIPJxgtLxmLgQAQz=1024*1024)
            if iqymPVpxyjOWChGwBkTemSzHJbnJdAIz is None:
                return web.Response(status=404)
            rYtAWlTfuJKXWhYOjYFOlRbQzowyoxFG = json.loads(iqymPVpxyjOWChGwBkTemSzHJbnJdAIz)
            if not "__metadata__" in rYtAWlTfuJKXWhYOjYFOlRbQzowyoxFG:
                return web.Response(status=404)
            return web.json_response(rYtAWlTfuJKXWhYOjYFOlRbQzowyoxFG["__metadata__"])
        @bodEVTWCiQtEgnHDFZUfegjtZIcDqMqP.get("/system_stats")
        async def lTeCmGwVHMgHEdPdTvDbShdpjolGRgNP(request):
            fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc = quasar.model_management.aIQypJefEzoiiobeXriYBEHMJwDTvZWS()
            LKGttefzMHbQsSCFJjKbAWGhbIpBWTal = quasar.model_management.CIUMTWevcFrsyhsNplwosYXuEZxYMCyJ(fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc)
            RLmugukEYkxzfSCKaEWBGZuHSEOQCFCb, CPmfbKHPexHTdMyYTkWLcWJyDYQUgVoh = quasar.model_management.vJrdZOBBaEUjLkobsDWKZVCBOAICHZyg(fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc, torch_total_too=True)
            kbasCXwVBHYxjnfxoYMePJNFwjOQJuuH, mqBKvQSkDHBcoMjHYqBSBckPFVKkaKxr = quasar.model_management.pEiuPTHzmozHhNpBwWGAaONYuNGSpuqI(fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc, torch_free_too=True)
            zrNEqtwItZmzpRltVnSBfgdEAifrcRDg = {
                "system": {
                    "os": os.pSfJNVvqLWVlUeHdpahCTGSrSPJYAnEQ,
                    "python_version": sys.AXCokaVjpCbdWwYKPYgzJCgAIrWdXrxQ,
                    "embedded_python": os.hxKDuOteESNpOgdClxSsFUWnOOOOTwlR.split(os.hxKDuOteESNpOgdClxSsFUWnOOOOTwlR.split(sys.executable)[0])[1] == "python_embeded"
                },
                "devices": [
                    {
                        "name": LKGttefzMHbQsSCFJjKbAWGhbIpBWTal,
                        "type": fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc.type,
                        "index": fncUdpUPRXGoRKeawVhmqjlxVPGbdjmc.index,
                        "vram_total": RLmugukEYkxzfSCKaEWBGZuHSEOQCFCb,
                        "vram_free": kbasCXwVBHYxjnfxoYMePJNFwjOQJuuH,
                        "torch_vram_total": CPmfbKHPexHTdMyYTkWLcWJyDYQUgVoh,
                        "torch_vram_free": mqBKvQSkDHBcoMjHYqBSBckPFVKkaKxr,
                    }
                ]
            }
            return web.json_response(zrNEqtwItZmzpRltVnSBfgdEAifrcRDg)
        @bodEVTWCiQtEgnHDFZUfegjtZIcDqMqP.get("/prompt")
        async def rtuFHpSyZqnkZElxUNzYjhOTHfGAVlrQ(request):
            return web.json_response(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.yvrrxYUiqVgrQsYWMxXZEJxnLIUXDnbr())
        def UummXdFvEtxfcoqHSKXTIifWtbqQRdVX(xSOZmNYxpkmvdctjGrQpCBJzXGRyWToK):
            jKcSNUDNgDXASzMmWRVTLbRKsfRcUIvA = nodes.wJhMfuyrPNjllkMCYXdJHMhubCAizKhP[xSOZmNYxpkmvdctjGrQpCBJzXGRyWToK]
            dkvGBiZkeLIFANNbVKlbQzLVBVedCkgi = {}
            dkvGBiZkeLIFANNbVKlbQzLVBVedCkgi['input'] = jKcSNUDNgDXASzMmWRVTLbRKsfRcUIvA.hGTeyOvpHejlssWPjkjTHIgcOKnCfnQl()
            dkvGBiZkeLIFANNbVKlbQzLVBVedCkgi['output'] = jKcSNUDNgDXASzMmWRVTLbRKsfRcUIvA.KmrPlNMyCntWtQIuwTzhYketzPaLUxAX
            dkvGBiZkeLIFANNbVKlbQzLVBVedCkgi['output_is_list'] = jKcSNUDNgDXASzMmWRVTLbRKsfRcUIvA.OUTPUT_IS_LIST if hasattr(jKcSNUDNgDXASzMmWRVTLbRKsfRcUIvA, 'OUTPUT_IS_LIST') else [False] * len(jKcSNUDNgDXASzMmWRVTLbRKsfRcUIvA.KmrPlNMyCntWtQIuwTzhYketzPaLUxAX)
            dkvGBiZkeLIFANNbVKlbQzLVBVedCkgi['output_name'] = jKcSNUDNgDXASzMmWRVTLbRKsfRcUIvA.vnnDnTEtmjYBCExrcduKGXUgKSzKzhcS if hasattr(jKcSNUDNgDXASzMmWRVTLbRKsfRcUIvA, 'RETURN_NAMES') else dkvGBiZkeLIFANNbVKlbQzLVBVedCkgi['output']
            dkvGBiZkeLIFANNbVKlbQzLVBVedCkgi['name'] = xSOZmNYxpkmvdctjGrQpCBJzXGRyWToK
            dkvGBiZkeLIFANNbVKlbQzLVBVedCkgi['display_name'] = nodes.fCNmqhLiPJmYYCEegZyrwHUKFhfIrdcf[xSOZmNYxpkmvdctjGrQpCBJzXGRyWToK] if xSOZmNYxpkmvdctjGrQpCBJzXGRyWToK in nodes.fCNmqhLiPJmYYCEegZyrwHUKFhfIrdcf.keys() else xSOZmNYxpkmvdctjGrQpCBJzXGRyWToK
            dkvGBiZkeLIFANNbVKlbQzLVBVedCkgi['description'] = jKcSNUDNgDXASzMmWRVTLbRKsfRcUIvA.DESCRIPTION if hasattr(jKcSNUDNgDXASzMmWRVTLbRKsfRcUIvA,'DESCRIPTION') else ''
            dkvGBiZkeLIFANNbVKlbQzLVBVedCkgi['category'] = 'sd'
            if hasattr(jKcSNUDNgDXASzMmWRVTLbRKsfRcUIvA, 'OUTPUT_NODE') and jKcSNUDNgDXASzMmWRVTLbRKsfRcUIvA.AQnTlfqkrmdAAnLjLNUFibEHomwVhMHv == True:
                dkvGBiZkeLIFANNbVKlbQzLVBVedCkgi['output_node'] = True
            else:
                dkvGBiZkeLIFANNbVKlbQzLVBVedCkgi['output_node'] = False
            if hasattr(jKcSNUDNgDXASzMmWRVTLbRKsfRcUIvA, 'CATEGORY'):
                dkvGBiZkeLIFANNbVKlbQzLVBVedCkgi['category'] = jKcSNUDNgDXASzMmWRVTLbRKsfRcUIvA.VHBvQQsdmXccHUVkiKRmkuIiUnjOTicH
            return dkvGBiZkeLIFANNbVKlbQzLVBVedCkgi
        @bodEVTWCiQtEgnHDFZUfegjtZIcDqMqP.get("/object_info")
        async def IgCCqmDgQOjwZyymVGxeYLwFOkwlFSMe(request):
            iqymPVpxyjOWChGwBkTemSzHJbnJdAIz = {}
            for NECAaWUrFGIXcLimrerEYmxYIykQBfXb in nodes.wJhMfuyrPNjllkMCYXdJHMhubCAizKhP:
                iqymPVpxyjOWChGwBkTemSzHJbnJdAIz[NECAaWUrFGIXcLimrerEYmxYIykQBfXb] = UummXdFvEtxfcoqHSKXTIifWtbqQRdVX(NECAaWUrFGIXcLimrerEYmxYIykQBfXb)
            return web.json_response(iqymPVpxyjOWChGwBkTemSzHJbnJdAIz)
        @bodEVTWCiQtEgnHDFZUfegjtZIcDqMqP.get("/object_info/{node_class}")
        async def UNonCACVdrzPWedMqIyrIufNXCirUFCg(request):
            xSOZmNYxpkmvdctjGrQpCBJzXGRyWToK = request.match_info.get("node_class", None)
            iqymPVpxyjOWChGwBkTemSzHJbnJdAIz = {}
            if (xSOZmNYxpkmvdctjGrQpCBJzXGRyWToK is not None) and (xSOZmNYxpkmvdctjGrQpCBJzXGRyWToK in nodes.wJhMfuyrPNjllkMCYXdJHMhubCAizKhP):
                iqymPVpxyjOWChGwBkTemSzHJbnJdAIz[xSOZmNYxpkmvdctjGrQpCBJzXGRyWToK] = UummXdFvEtxfcoqHSKXTIifWtbqQRdVX(xSOZmNYxpkmvdctjGrQpCBJzXGRyWToK)
            return web.json_response(iqymPVpxyjOWChGwBkTemSzHJbnJdAIz)
        @bodEVTWCiQtEgnHDFZUfegjtZIcDqMqP.get("/history")
        async def nglQBfzxqztJKZZGNtEyLrQsaKQhyjMg(request):
            return web.json_response(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.prompt_queue.nglQBfzxqztJKZZGNtEyLrQsaKQhyjMg())
        @bodEVTWCiQtEgnHDFZUfegjtZIcDqMqP.get("/history/{prompt_id}")
        async def nglQBfzxqztJKZZGNtEyLrQsaKQhyjMg(request):
            AFursZnPuECGUFTkCjDbdYIYmtroiqfB = request.match_info.get("prompt_id", None)
            return web.json_response(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.prompt_queue.nglQBfzxqztJKZZGNtEyLrQsaKQhyjMg(AFursZnPuECGUFTkCjDbdYIYmtroiqfB=AFursZnPuECGUFTkCjDbdYIYmtroiqfB))
        @bodEVTWCiQtEgnHDFZUfegjtZIcDqMqP.get("/queue")
        async def lTeCmGwVHMgHEdPdTvDbShdpjolGRgNP(request):
            zKQRdGZVnNjWfkbPqEGUhWMPvfpeQAoa = {}
            YjhaLUBJRBuzruLsvXqjqFRZVGPPYlsN = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.prompt_queue.zcXnzbKBPZhuUbUDbBKQYruWvmnWjdXd()
            zKQRdGZVnNjWfkbPqEGUhWMPvfpeQAoa['queue_running'] = YjhaLUBJRBuzruLsvXqjqFRZVGPPYlsN[0]
            zKQRdGZVnNjWfkbPqEGUhWMPvfpeQAoa['queue_pending'] = YjhaLUBJRBuzruLsvXqjqFRZVGPPYlsN[1]
            return web.json_response(zKQRdGZVnNjWfkbPqEGUhWMPvfpeQAoa)
        @bodEVTWCiQtEgnHDFZUfegjtZIcDqMqP.PWqGBaLAYfSwazFeBMSGmrXYXGQgzIGF("/prompt")
        async def mEvhoLvejJJzUuEqSHnnuwmtQVWdYrvI(request):
            print("got prompt")
            cicSAkZRUdRnvxwIyGEfxgqfUluMPHFp = 200
            gKOqsXKiMHyMfJdNkNEvdnivNsNJKQyW = ""
            UqQOtoIhkZOOuTekBZnxaFPJmmrLOkwH =  await request.json()
            UqQOtoIhkZOOuTekBZnxaFPJmmrLOkwH = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.CVlpsFZpCaBNCNZqToOXuOcHyMwPHNGp(UqQOtoIhkZOOuTekBZnxaFPJmmrLOkwH)
            if "number" in UqQOtoIhkZOOuTekBZnxaFPJmmrLOkwH:
                FCVsdRzGunasBiYAXHkNdLEMUdcXuHLD = float(UqQOtoIhkZOOuTekBZnxaFPJmmrLOkwH['number'])
            else:
                FCVsdRzGunasBiYAXHkNdLEMUdcXuHLD = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.FCVsdRzGunasBiYAXHkNdLEMUdcXuHLD
                if "front" in UqQOtoIhkZOOuTekBZnxaFPJmmrLOkwH:
                    if UqQOtoIhkZOOuTekBZnxaFPJmmrLOkwH['front']:
                        FCVsdRzGunasBiYAXHkNdLEMUdcXuHLD = -FCVsdRzGunasBiYAXHkNdLEMUdcXuHLD
                rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.FCVsdRzGunasBiYAXHkNdLEMUdcXuHLD += 1
            if "prompt" in UqQOtoIhkZOOuTekBZnxaFPJmmrLOkwH:
                qKBREHoSgcMHYVCNTapmPyODbBOyQAyv = UqQOtoIhkZOOuTekBZnxaFPJmmrLOkwH["prompt"]
                ERUVMXIoRhkepyeqXbuVyzEnnckUwodx = execution.qcwCQLkogrkGqZWctxxXKVKWwxbopaRJ(qKBREHoSgcMHYVCNTapmPyODbBOyQAyv)
                vngfynKJfsHLAoqKbHSpKIzjZdROnsZl = {}
                if "extra_data" in UqQOtoIhkZOOuTekBZnxaFPJmmrLOkwH:
                    vngfynKJfsHLAoqKbHSpKIzjZdROnsZl = UqQOtoIhkZOOuTekBZnxaFPJmmrLOkwH["extra_data"]
                if "client_id" in UqQOtoIhkZOOuTekBZnxaFPJmmrLOkwH:
                    vngfynKJfsHLAoqKbHSpKIzjZdROnsZl["client_id"] = UqQOtoIhkZOOuTekBZnxaFPJmmrLOkwH["client_id"]
                if ERUVMXIoRhkepyeqXbuVyzEnnckUwodx[0]:
                    AFursZnPuECGUFTkCjDbdYIYmtroiqfB = str(uuid.uuid4())
                    brFZitjOvbNclhdGWVUAWGSUfhOfcWsy = ERUVMXIoRhkepyeqXbuVyzEnnckUwodx[2]
                    rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.prompt_queue.CCOVuLEMeFpoufRVtjDeWqHtFSDTjTzt((FCVsdRzGunasBiYAXHkNdLEMUdcXuHLD, AFursZnPuECGUFTkCjDbdYIYmtroiqfB, qKBREHoSgcMHYVCNTapmPyODbBOyQAyv, vngfynKJfsHLAoqKbHSpKIzjZdROnsZl, brFZitjOvbNclhdGWVUAWGSUfhOfcWsy))
                    HQlvpyIUUfnfAqKdXyNavyxWXIZkebhk = {"prompt_id": AFursZnPuECGUFTkCjDbdYIYmtroiqfB, "number": FCVsdRzGunasBiYAXHkNdLEMUdcXuHLD, "node_errors": ERUVMXIoRhkepyeqXbuVyzEnnckUwodx[3]}
                    return web.json_response(HQlvpyIUUfnfAqKdXyNavyxWXIZkebhk)
                else:
                    print("invalid prompt:", ERUVMXIoRhkepyeqXbuVyzEnnckUwodx[1])
                    return web.json_response({"error": ERUVMXIoRhkepyeqXbuVyzEnnckUwodx[1], "node_errors": ERUVMXIoRhkepyeqXbuVyzEnnckUwodx[3]}, status=400)
            else:
                return web.json_response({"error": "no prompt", "node_errors": []}, status=400)
        @bodEVTWCiQtEgnHDFZUfegjtZIcDqMqP.PWqGBaLAYfSwazFeBMSGmrXYXGQgzIGF("/queue")
        async def xnLrDuhtzPuICRupoCUtupkUrhDRSaQZ(request):
            UqQOtoIhkZOOuTekBZnxaFPJmmrLOkwH =  await request.json()
            if "clear" in UqQOtoIhkZOOuTekBZnxaFPJmmrLOkwH:
                if UqQOtoIhkZOOuTekBZnxaFPJmmrLOkwH["clear"]:
                    rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.prompt_queue.DlgdOtYbsMDZaSavoSpBEHOHGoWiupuW()
            if "delete" in UqQOtoIhkZOOuTekBZnxaFPJmmrLOkwH:
                HZgFvSCHHvndfkOsuWOqyKgtGBOkAfAZ = UqQOtoIhkZOOuTekBZnxaFPJmmrLOkwH['delete']
                for qfBoniFmTgUvqdSyxjmQmiqYnGgWUrtJ in HZgFvSCHHvndfkOsuWOqyKgtGBOkAfAZ:
                    WjfJkXCHHmiThFKVEkbbSZBLRoMVLsSb = lambda GlZreLQjBCiBptpFgmbsMbhjFlMgPVav: GlZreLQjBCiBptpFgmbsMbhjFlMgPVav[1] == qfBoniFmTgUvqdSyxjmQmiqYnGgWUrtJ
                    rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.prompt_queue.kqUSARiqrpbKPOIIpqEzyhrJfaGKBQOs(WjfJkXCHHmiThFKVEkbbSZBLRoMVLsSb)
            return web.Response(status=200)
        @bodEVTWCiQtEgnHDFZUfegjtZIcDqMqP.PWqGBaLAYfSwazFeBMSGmrXYXGQgzIGF("/interrupt")
        async def cDLSlLAYYyynyKofSxecnMFzjtnzxHAR(request):
            nodes.NIMMAjqKpMwgFfFMJGlJLJdwCPLKOQTM()
            return web.Response(status=200)
        @bodEVTWCiQtEgnHDFZUfegjtZIcDqMqP.PWqGBaLAYfSwazFeBMSGmrXYXGQgzIGF("/history")
        async def jqPRRzSOTSyvsahholjQokYZyXoxyIAm(request):
            UqQOtoIhkZOOuTekBZnxaFPJmmrLOkwH =  await request.json()
            if "clear" in UqQOtoIhkZOOuTekBZnxaFPJmmrLOkwH:
                if UqQOtoIhkZOOuTekBZnxaFPJmmrLOkwH["clear"]:
                    rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.prompt_queue.BfUFoNCsskLewFIQhwJteOlDlTrsiYeM()
            if "delete" in UqQOtoIhkZOOuTekBZnxaFPJmmrLOkwH:
                HZgFvSCHHvndfkOsuWOqyKgtGBOkAfAZ = UqQOtoIhkZOOuTekBZnxaFPJmmrLOkwH['delete']
                for qfBoniFmTgUvqdSyxjmQmiqYnGgWUrtJ in HZgFvSCHHvndfkOsuWOqyKgtGBOkAfAZ:
                    rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.prompt_queue.SWoBIKPEDgMZbmxkAhUBljmIrxWgVfpt(qfBoniFmTgUvqdSyxjmQmiqYnGgWUrtJ)
            return web.Response(status=200)
    def grMbBVhUPmxLYqHuLTMYkwVmMccNhUyi(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS):
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.app.grMbBVhUPmxLYqHuLTMYkwVmMccNhUyi(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.bodEVTWCiQtEgnHDFZUfegjtZIcDqMqP)
        for pSfJNVvqLWVlUeHdpahCTGSrSPJYAnEQ, dir in nodes.OhQOpxGGCySHXalbRgaNhmvFYyGbOLxZ.items():
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.app.grMbBVhUPmxLYqHuLTMYkwVmMccNhUyi([
                web.static('/extensions/' + urllib.parse.quote(pSfJNVvqLWVlUeHdpahCTGSrSPJYAnEQ), dir, follow_symlinks=True),
            ])
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.app.grMbBVhUPmxLYqHuLTMYkwVmMccNhUyi([
            web.static('/', rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.web_root, follow_symlinks=True),
        ])
    def yvrrxYUiqVgrQsYWMxXZEJxnLIUXDnbr(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS):
        GjFngyPEbvmyWKdohCWlJwQdGDmPFMJv = {}
        xUhsMmEzWOLseFZzkBPJkyceMytFEhem = {}
        xUhsMmEzWOLseFZzkBPJkyceMytFEhem['queue_remaining'] = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.prompt_queue.EtRSdUTbsAGPQTWeOVUeVvGClCQoJfey()
        GjFngyPEbvmyWKdohCWlJwQdGDmPFMJv['exec_info'] = xUhsMmEzWOLseFZzkBPJkyceMytFEhem
        return GjFngyPEbvmyWKdohCWlJwQdGDmPFMJv
    async def BUmulCEcJXhvafjQvItCTXiuvSjzjSFf(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, event, data, JSUFYNwccnkWErsvCCtXGLoDRqOUNtXT=None):
        if event == hFTRCQDJXYjBTBYxdLVBThHQwQEdvZRj.aMTOakoNisHgzZsgUrJBfNFbowQFDzvw:
            await rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.HRgKozExpPGXCQOHNUJqBLOKMbbpygDL(data, JSUFYNwccnkWErsvCCtXGLoDRqOUNtXT=JSUFYNwccnkWErsvCCtXGLoDRqOUNtXT)
        elif isinstance(data, (bytes, bytearray)):
            await rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.xcZrutSLQCYZqeDsqlFkiSCGgszjvDJQ(event, data, JSUFYNwccnkWErsvCCtXGLoDRqOUNtXT)
        else:
            await rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.JIuLLknKmvoFbWnxxCtVPWyssUoyssdx(event, data, JSUFYNwccnkWErsvCCtXGLoDRqOUNtXT)
    def HnYMlAkqypeGWCsLNNuJoKhoyIgGBdGl(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, event, data):
        if not isinstance(event, int):
            raise RuntimeError(f"Binary event types must be integers, got {event}")
        xHwjpgVIeTCBxNVsGEaIQthrVWPRVtKV = struct.pack(">I", event)
        JWcvhhSkkAOvOUymGHSWwtMPsUYfbjKO = bytearray(xHwjpgVIeTCBxNVsGEaIQthrVWPRVtKV)
        JWcvhhSkkAOvOUymGHSWwtMPsUYfbjKO.extend(data)
        return JWcvhhSkkAOvOUymGHSWwtMPsUYfbjKO
    async def HRgKozExpPGXCQOHNUJqBLOKMbbpygDL(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, image_data, JSUFYNwccnkWErsvCCtXGLoDRqOUNtXT=None):
        gMAqwKbAmPSlNutbEQLabUMOSMWTaXiL = image_data[0]
        eLyJtroPthPCROYWyMphoIrGatNOOXCO = image_data[1]
        jedJBMoSqKrLwfdHJIPJxgtLxmLgQAQz = image_data[2]
        if jedJBMoSqKrLwfdHJIPJxgtLxmLgQAQz is not None:
            if hasattr(Image, 'Resampling'):
                VfgMvQQburvHcuDSjykMqzSDOZbAXdKI = Image.Resampling.BILINEAR
            else:
                VfgMvQQburvHcuDSjykMqzSDOZbAXdKI = Image.ANTIALIAS
            eLyJtroPthPCROYWyMphoIrGatNOOXCO = ImageOps.contain(eLyJtroPthPCROYWyMphoIrGatNOOXCO, (jedJBMoSqKrLwfdHJIPJxgtLxmLgQAQz, jedJBMoSqKrLwfdHJIPJxgtLxmLgQAQz), VfgMvQQburvHcuDSjykMqzSDOZbAXdKI)
        iwfbrvoNITTgpyVOMmWYZJdmSsUUGkkP = 1
        if gMAqwKbAmPSlNutbEQLabUMOSMWTaXiL == "JPEG":
            iwfbrvoNITTgpyVOMmWYZJdmSsUUGkkP = 1
        elif gMAqwKbAmPSlNutbEQLabUMOSMWTaXiL == "PNG":
            iwfbrvoNITTgpyVOMmWYZJdmSsUUGkkP = 2
        DefwnHgSlTOAvAStuPkwnHTNmIMWaKYl = BytesIO()
        KDzzBWHjlQwFzHaklntHThjQWIdWuhMw = struct.pack(">I", iwfbrvoNITTgpyVOMmWYZJdmSsUUGkkP)
        DefwnHgSlTOAvAStuPkwnHTNmIMWaKYl.write(KDzzBWHjlQwFzHaklntHThjQWIdWuhMw)
        eLyJtroPthPCROYWyMphoIrGatNOOXCO.PXhZDpeqZAdDBfrowpMPOPAWwzXhVAFM(DefwnHgSlTOAvAStuPkwnHTNmIMWaKYl, format=gMAqwKbAmPSlNutbEQLabUMOSMWTaXiL, VjCDDDhoOBHYwICKnNldLuMUvRwnLMaR=95, compress_level=4)
        ljJUDoqGBoyPevlyawCUEFbfPKfJQjML = DefwnHgSlTOAvAStuPkwnHTNmIMWaKYl.getvalue()
        await rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.xcZrutSLQCYZqeDsqlFkiSCGgszjvDJQ(hFTRCQDJXYjBTBYxdLVBThHQwQEdvZRj.fdlOyZPXWscvoPcQnxxSXdTqmBFxYGDC, ljJUDoqGBoyPevlyawCUEFbfPKfJQjML, JSUFYNwccnkWErsvCCtXGLoDRqOUNtXT=JSUFYNwccnkWErsvCCtXGLoDRqOUNtXT)
    async def xcZrutSLQCYZqeDsqlFkiSCGgszjvDJQ(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, event, data, JSUFYNwccnkWErsvCCtXGLoDRqOUNtXT=None):
        JWcvhhSkkAOvOUymGHSWwtMPsUYfbjKO = rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.HnYMlAkqypeGWCsLNNuJoKhoyIgGBdGl(event, data)
        if JSUFYNwccnkWErsvCCtXGLoDRqOUNtXT is None:
            for xMUuFtzQyRMgVTNGJlNLnSTHJqLOlsTi in rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.sockets.values():
                await xorVUCSjBcCTFixHnjvWgKQmsHYbOoVo(xMUuFtzQyRMgVTNGJlNLnSTHJqLOlsTi.xcZrutSLQCYZqeDsqlFkiSCGgszjvDJQ, JWcvhhSkkAOvOUymGHSWwtMPsUYfbjKO)
        elif JSUFYNwccnkWErsvCCtXGLoDRqOUNtXT in rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.sockets:
            await xorVUCSjBcCTFixHnjvWgKQmsHYbOoVo(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.sockets[JSUFYNwccnkWErsvCCtXGLoDRqOUNtXT].xcZrutSLQCYZqeDsqlFkiSCGgszjvDJQ, JWcvhhSkkAOvOUymGHSWwtMPsUYfbjKO)
    async def JIuLLknKmvoFbWnxxCtVPWyssUoyssdx(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, event, data, JSUFYNwccnkWErsvCCtXGLoDRqOUNtXT=None):
        JWcvhhSkkAOvOUymGHSWwtMPsUYfbjKO = {"type": event, "data": data}
        if JSUFYNwccnkWErsvCCtXGLoDRqOUNtXT is None:
            for xMUuFtzQyRMgVTNGJlNLnSTHJqLOlsTi in rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.sockets.values():
                await xorVUCSjBcCTFixHnjvWgKQmsHYbOoVo(xMUuFtzQyRMgVTNGJlNLnSTHJqLOlsTi.JIuLLknKmvoFbWnxxCtVPWyssUoyssdx, JWcvhhSkkAOvOUymGHSWwtMPsUYfbjKO)
        elif JSUFYNwccnkWErsvCCtXGLoDRqOUNtXT in rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.sockets:
            await xorVUCSjBcCTFixHnjvWgKQmsHYbOoVo(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.sockets[JSUFYNwccnkWErsvCCtXGLoDRqOUNtXT].JIuLLknKmvoFbWnxxCtVPWyssUoyssdx, JWcvhhSkkAOvOUymGHSWwtMPsUYfbjKO)
    def qIpzeiOiFfpTobMBTgFPHfiZRTmLDpoa(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, event, data, JSUFYNwccnkWErsvCCtXGLoDRqOUNtXT=None):
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.ZkUlcueFlyNvGBkHzyBcsDJMXTjAiuhK.call_soon_threadsafe(
            rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.messages.put_nowait, (event, data, JSUFYNwccnkWErsvCCtXGLoDRqOUNtXT))
    def YpzwdlwzVFOboyfWmWHyngylauEuTbaZ(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS):
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.qIpzeiOiFfpTobMBTgFPHfiZRTmLDpoa("status", { "status": rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.yvrrxYUiqVgrQsYWMxXZEJxnLIUXDnbr() })
    async def EBskPkRhwxVtGrdnQMhAvswjrxSyPepP(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS):
        while True:
            ajOmIBaJxAXoIDFumJtKcydIEAgfQgwV = await rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.messages.get()
            await rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.BUmulCEcJXhvafjQvItCTXiuvSjzjSFf(*ajOmIBaJxAXoIDFumJtKcydIEAgfQgwV)
    async def tUuYqnLjDXuftYgMagGpmrobxWgfcbgq(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, CCIjQGzXZAaHfKOvxktxIwIaaauBrFXv, port, aFZoJwWpCnqyOJdcAMLlqOHxDgjPTNCS=True, ALTUFmMSNrTTqeFdmxsHzQmauDwcNVXN=None):
        yVReFCGZqyhbsCCIGNXbTYqonqUiCuEW = web.AppRunner(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.app, access_log=None)
        await yVReFCGZqyhbsCCIGNXbTYqonqUiCuEW.setup()
        xXGxFfTDOPkklznafEFItQoDSdFWqQFg = web.TCPSite(yVReFCGZqyhbsCCIGNXbTYqonqUiCuEW, CCIjQGzXZAaHfKOvxktxIwIaaauBrFXv, port)
        await xXGxFfTDOPkklznafEFItQoDSdFWqQFg.tUuYqnLjDXuftYgMagGpmrobxWgfcbgq()
        if CCIjQGzXZAaHfKOvxktxIwIaaauBrFXv == '':
            CCIjQGzXZAaHfKOvxktxIwIaaauBrFXv = '0.0.0.0'
        if aFZoJwWpCnqyOJdcAMLlqOHxDgjPTNCS:
            print("Starting server\n")
            print("To see the GUI go to: http://{}:{}".format(CCIjQGzXZAaHfKOvxktxIwIaaauBrFXv, port))
        if ALTUFmMSNrTTqeFdmxsHzQmauDwcNVXN is not None:
            ALTUFmMSNrTTqeFdmxsHzQmauDwcNVXN(CCIjQGzXZAaHfKOvxktxIwIaaauBrFXv, port)
    def sWnpCvuipWBHCCscTxhKjaajtVJfMBbv(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, TQLMHpzrGHfkKPXOsLxdKBpLrtwSARMk):
        rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.on_prompt_handlers.append(TQLMHpzrGHfkKPXOsLxdKBpLrtwSARMk)
    def CVlpsFZpCaBNCNZqToOXuOcHyMwPHNGp(rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS, UqQOtoIhkZOOuTekBZnxaFPJmmrLOkwH):
        for TQLMHpzrGHfkKPXOsLxdKBpLrtwSARMk in rmBxqCKJkHuPIHNivpdAAgzvrGlNKdVS.on_prompt_handlers:
            try:
                UqQOtoIhkZOOuTekBZnxaFPJmmrLOkwH = TQLMHpzrGHfkKPXOsLxdKBpLrtwSARMk(UqQOtoIhkZOOuTekBZnxaFPJmmrLOkwH)
            except Exception as dgvKdkEDrMSdkCaRxfkDNVbaXWUetgtO:
                print(f"[ERROR] An error occurred during the on_prompt_handler processing")
                traceback.print_exc()
        return UqQOtoIhkZOOuTekBZnxaFPJmmrLOkwH
