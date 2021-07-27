from .websocket import *
import threading

class Thread(threading.Thread):
    def __init__(self, number, ws, uid):
        threading.Thread.__init__(self)
        self.number = number
        self.ws = ws
        self.id = uid

    def run(self):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(websocket(self.ws, self.id))