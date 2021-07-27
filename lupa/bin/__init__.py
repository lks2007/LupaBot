from .action import *
from .websocket import *
from .threading import *

def start(ws, uid):

    for i in range(0, len(ws)):
        globals()['thread_%s' % i] = Thread(i, ws[i], uid)
        exec('thread_'+str(i)+'.start()')