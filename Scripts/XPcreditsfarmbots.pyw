import discord
import sys
import random
from random import randint, choice
import string
import asyncio

client = discord.Client()
min_char = 10
max_char = 25
allchar = string.ascii_letters + string.digits
token = sys.argv[1]
txtchanid = sys.argv[2]
print("loading...")

@client.event
async def on_ready():
    global msgcontent
    txtchan = client.get_channel(int(txtchanid))
    print ("Logged in")
    print ("=================")
    msgcontent = "".join(choice(allchar) for x in range(randint(min_char, max_char)))
    asyncio.sleep(float(str("0." + str(random.randint(1337,9999)))))
    try:
        await txtchan.send(msgcontent)
    except Exception:
        pass
    quit()

try:
    client.run(token, bot=False)
except Exception as c:
    print(c)
