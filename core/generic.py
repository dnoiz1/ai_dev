### Generic Function Callbacks
# These are all the functions that are super common and likely to not change
# 
try:
    from core.helper import *
except ImportError:
    from helper import *

import json
import re 
from urllib.request import urlopen

async def helpCB(room, event):
    await aiLog(event)
    helpFile = await readFile('assets/helpfile.txt')
    return helpFile

async def testCB(room,event):
    await aiLog(event)
    return "Test Success!"

async def archCB(room, event):
    await aiLog(event)
    s = event.sender
    out = "Hey {}, use this guide! https://gist.github.com/netspooky/cad9a183daf3dfcbc677221ff452c15b".format(s)
    return out

async def ballCB(room, event):
    await aiLog(event)
    ball = await getLine("assets/8ball.txt")
    return ball

async def skrtCB(room, event):
    await aiLog(event)
    return "This message requires Matrix Gold to view"

async def stressedCB(room, event):
    await aiLog(event)
    dStressTip = await getLine("assets/stressed.txt")
    return dStressTip

async def cryptoCB(room,event):
    args = event.body.split()
    coin = args[1]
    if len(coin) > 4:
        return "Not a coin lol"
    else:
        try:
            rOut  = urlopen("https://min-api.cryptocompare.com/data/price?fsym="+coin+"&tsyms=USD")
            rRaw  = rOut.read()
            jOut  = json.loads(rRaw.decode('utf-8'))
            price = str(jOut["USD"])
            coinOut = "{}: ${}".format(coin,price)
            return coinOut
        except Exception as aiEx:
            await crashLog(event,aiEx)
