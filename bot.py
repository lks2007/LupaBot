from lupa import *
from lupa.ext.commands import *
from datetime import datetime
from PIL import ImageDraw
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
        self.status = addCommand(['status', 'bot', 'server'], ['Server start since '+str(getLog()), 'Bot start since '+str(getLog('bot')), 'Server start since '+str(getLog())])
        self.img = addCommand(['img'], '')
        
        self.threading = start(self.response['websocket'], self.response['id'])
        self.disconnect = await disconnect(self.token)


def convertTime(dateL):
    dateLaunch = datetime.strptime(dateL[:19], "%Y-%m-%d %H:%M:%S")
    now = datetime.now()

    year = now.year - dateLaunch.year
    month = now.month - dateLaunch.month
    day = now.day - dateLaunch.day

    hour = now.hour - dateLaunch.hour
    minute = now.minute - dateLaunch.minute
    second = now.second - dateLaunch.second

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
        return str(year)+'Y '+str(month)+"M "+str(day)+"d "+str(hour)+"h "+str(minute)+"min "+str(second)+"s"
    elif month != 0:
        return str(month)+"M "+str(day)+"d "+str(hour)+"h "+str(minute)+"min "+str(second)+"s"
    elif day != 0:
        return str(day)+"d "+str(hour)+"h "+str(minute)+"min "+str(second)+"s"
    elif hour != 0:
        return str(hour)+"h "+str(minute)+"min "+str(second)+"s"
    elif minute != 0:
        return str(minute)+"min "+str(second)+"s"
    elif second >= 0:
        return str(second)+"s"

def getLog(*argv):
    if argv:
        with open('log/bot.log', 'r') as f:
            lines = f.readlines()
            l = lines[-1]
            return convertTime(l)
            
    else:
        with open('log/daphne.log', 'r') as f:  
            lines = f.readlines()
            last = lines[-1]
            return convertTime(last)

def createImg(user):
    w, h = 220, 190


if __name__ == "__main__":
    client = Client()