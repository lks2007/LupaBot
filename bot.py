from lupa import *
from lupa.ext.commands import *
from datetime import datetime
import asyncio

class Client():
    def __init__(self):
        self.token = '34427d32-ed4f-4133-b891-32482febdcfc'
        self.login = asyncio.get_event_loop()
        self.response = self.login.run_until_complete(run(self.token))
        asyncio.run(self.on_ready())

    async def on_ready(self):
        print('+----------------------+')
        print("+--- Logged as "+self.response['name']+" ---+")
        print('+----------------------+')

        prefix = add_prefix('/')
        self.help = addCommand(['help'], '<b>Help command:</b> <br><em class="m-0">status:    start time "job"</em>')
        self.status = addCommand(['status', 'bot', 'server'], [str('Server start since '+getLog()), str('Bot start since '+getLog('bot')), str('Server start since '+getLog())])

        self.threading = start(self.response['websocket'], self.response['id'])
        self.disconnect = await disconnect(self.token)


def convertTime(date):
    date = datetime.strptime(date[:19], "%Y-%m-%d %H:%M:%S")
    now = datetime.now()

    year = now.year - date.year
    month = now.month - date.month
    day = now.day - date.day

    hour = now.hour - date.hour
    minute = now.minute - date.minute
    second = now.second - date.second

    if hour < 0:
        day -= 1
        hour = 24 + hour

    if minute < 0:
        hour -= 1
        minute = 60 + minute

    if second < 0:
        minute -= 1
        second = 60 + second

    if year != 0:
        r = str(year)+'Y '+str(month)+"M "+str(day)+"d "+str(hour)+"h "+str(minute)+"min "+str(second)+"s"
        return r
    elif month != 0:
        r = str(month)+"M "+str(day)+"d "+str(hour)+"h "+str(minute)+"min "+str(second)+"s"
        return r
    elif day != 0:
        r = str(day)+"d "+str(hour)+"h "+str(minute)+"min "+str(second)+"s"
        return r
    elif hour != 0:
        r = str(hour)+"h "+str(minute)+"min "+str(second)+"s"
        return r
    elif minute != 0:
        r = str(minute)+"min "+str(second)+"s"
        return r
    elif second != 0:
        r = str(second)+"s"
        return r

def getLog(*argv):
    if argv:
        with open('log/bot.log', 'r') as f:
            lines = f.readlines()
            last = lines[-1]
            convertTime(last)
            
    else:
        with open('log/daphne.log', 'r') as f:  
            lines = f.readlines()
            last = lines[-1]
            convertTime(last)

if __name__ == "__main__":
    client = Client()