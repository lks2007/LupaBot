import websockets
import asyncio
import json
import ssl
import pathlib
from lupa.ext.commands import *

ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
localhost_pem = pathlib.Path(__file__).with_name("certificate.crt")
ssl_context.load_verify_locations(localhost_pem)

async def websocket(uri, uid):
    url = "wss://www.lupa.com/ws/channels/"+uri+"/"
    async with websockets.connect(url, ssl=ssl_context) as websocket:
        await websocket.send(json.dumps({'typemsg': 'status', 'user': uid, 'status': 1}))
        
        while True:
            res = await websocket.recv()
            req = json.loads(res)
            try:
                if int(req['user']) != int(uid):
                    response = onMsg(req['message'])
                    await websocket.send(json.dumps({'typemsg': 'text', 'message': str(response), 'user': str(uid), 'channel': str(req['user'])}))
            except:
                pass