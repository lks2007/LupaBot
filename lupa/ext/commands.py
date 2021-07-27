from bot import getLog

global prefix
prefix = None

def add_prefix(p):
    global prefix
    prefix = p

list = {}
def addCommand(name, response):
    global prefix
    if len(name) > 1:
        for n in range(0, len(name)):
            if n > 0:
                list[prefix+name[0]+" "+name[n]] = response[n]
            else:
                list[prefix+name[0]] = response[n]
    else:
        list[prefix+name[0]] = response

def onMsg(msg):
    if prefix != None:
        if msg == prefix+"status" or msg == prefix+"status bot" or msg == prefix+"status server":
            addCommand(['status', 'bot', 'server'], ['Server start since '+str(getLog()), 'Bot start since '+str(getLog('bot')), 'Server start since '+str(getLog())])

        m = msg.split()
        if len(m) > 1:
            if list[m[0]+" "+m[1]] != None:
                return list[m[0]+" "+m[1]]
        else:
            if list[m[0]] != None:
                return list[m[0]]