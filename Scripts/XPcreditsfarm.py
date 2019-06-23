import discord
import sys
import random
from random import randint, choice
import os
import string
import asyncio

client = discord.Client()
min_char = 10
max_char = 25
allchar = string.ascii_letters + string.digits
token = sys.argv[1]
txtchanid = sys.argv[2]
lasterror = "none"
totalwordsent = 0
levelgained = 0
print("loading...")

@client.event
async def on_ready():
    global lasterror
    global totalwordsent
    global msgcontent
    os.system('cls')
    veryepicpfp = client.user.avatar
    print ("Logged in")
    print ("=================")
    txtchan = client.get_channel(int(txtchanid))
    while True:
        lasterror = "none"
        msgcontent = "".join(choice(allchar) for x in range(randint(min_char, max_char)))
        try:
            await txtchan.send(msgcontent)
            totalwordsent = totalwordsent + 1
        except Exception as e:
            lasterror = e
            pass
        waitforhowlong = int(str(random.randint(30,75)))
        asyncio.sleep(float(str("0." + str(random.randint(1337,9999)))))
        for count in reversed(range(1, waitforhowlong+1)):
            os.system('cls')
            print("#=======================#")
            print("+ XP and credits farmer +")
            print("#=======================#")
            print('')
            print("Total word sent: " + str(totalwordsent))
            print("Last word sent: " + str(msgcontent))
            print("Level gained: " + str(levelgained))
            print('')
            if not lasterror == "none":
                print("error while sending last message: " + str(lasterror))
                print('')
            print(str(count) + " Seconds until next message")
            await asyncio.sleep(1)

@client.event
async def on_message(message):
    global levelgained
    if message.author.id == 172002275412279296 and str(message.channel.id) == str(txtchanid):
        if "🆙  |  **" + client.user.name + " leveled up!**" in message.content:
            levelgained = levelgained + 1

try:
    client.run(token, bot=False)
except Exception as c:
    print(c)
