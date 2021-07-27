import asyncio
import aiohttp
import signal
import sys
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
   
async def run(token):
    token = {"token": token}

    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(limit=64, ssl=False)) as session:
        async with session.post('https://www.lupa.com/api/v1/login/', json=token) as response:
            req = await response.json()
            return req

async def disconnect(token):
    def signal_handler(sig, frame):
        r = requests.post('https://www.lupa.com/api/v1/disconnect/', json={"token": token}, verify=False)
        sys.exit(0)

    signal.signal(signal.SIGINT, signal_handler)
    print('\nPress Ctrl+C to exit')
    signal.pause()