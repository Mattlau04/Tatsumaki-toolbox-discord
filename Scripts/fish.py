import discord
import random
import asyncio
import re
import sys
import os

client = discord.Client()
types = ['garbage', 'common', 'uncommon']
token = sys.argv[1]
txtchanid = sys.argv[2]
cash = 0
totalcommonsold = 0
totaluncommonsold = 0
totaltrashsold = 0
lasterror = "noerror"
isleeplol = int(random.randint(31,37))
totalnumberfishing = 0
print("Loading...")

@client.event
async def on_ready():
    global cash
    global isleeplol
    global totalnumberfishing
    global lasterror
    txtchan = client.get_channel(int(txtchanid))
    os.system('cls')
    print("#=============#")
    print("+ Fishing bot +")
    print("#=============#")
    print('')
    print("Total gain: 0 (this will go down until the sell part, so don't freak out when it goes down)")
    print('')
    print("Total number of fishing: 0")
    print('')
    print("Total common fish sold: 0")
    print("Total uncommon fish sold: 0")
    print("Total trash items sold: 0")
    await asyncio.sleep(5)
    while True:
        loopfishing = random.randint(24,98)
        howmuchbeforsshop = loopfishing
        for _ in range(loopfishing):
            howmuchbeforsshop = howmuchbeforsshop - 1
            lasterror = "noerror"
            await txtchan.send("t!fish")
            totalnumberfishing = int(totalnumberfishing) + 1
            cash = float(cash) - float(10)
            for count in reversed(range(1, isleeplol+1)):
                os.system('cls')
                print("#=============#")
                print("+ Fishing bot +")
                print("#=============#")
                print('')
                print("Total gain: " + str(cash))
                print('')
                print("Total number of fishing: " + str(totalnumberfishing))
                print('')
                print("Next selling in " + str(int(howmuchbeforsshop) + 1) + " fishing")
                print('')
                print("Total common fish sold: " + str(totalcommonsold))
                print("Total uncommon fish sold: " + str(totaluncommonsold))
                print("Total trash items sold: " + str(totaltrashsold))
                print('')
                print("Next fishing in " + str(count) + " seconds")
                if not lasterror == "noerror":
                    print('')
                    print("Error on last fishing: " + str(lasterror))
                await asyncio.sleep(1)
            isleeplol = int(random.randint(32,37))
            await asyncio.sleep(float((str("0.") + str(random.randint(1337,9999)))))
        print('')
        print("selling common...")
        await txtchan.send("t!fish sell common")
        await asyncio.sleep(float(str(random.randint(6,9)) + "." + str(random.randint(1337,9999))))
        print("selling uncommon...")
        await txtchan.send("t!fish sell uncommon")
        await asyncio.sleep(float(str(random.randint(6,9)) + "." + str(random.randint(1337,9999))))
        print("selling garbage...")
        await txtchan.send("t!fish sell garbage")
        isleeplol = random.randint(30,35)
        await asyncio.sleep(float(str(random.randint(6,10)) + "." + str(random.randint(1337,9999))))

@client.event
async def on_message(message):
    global lasterror
    global totalcommonsold
    global totaluncommonsold
    global totaltrashsold
    global cash
    if message.author.id == 172002275412279296 and str(message.channel.id) == str(txtchanid):
        if "🎣  |  **" + client.user.name + "**, **you can fish again in" in message.content:
            print("Rate limited by tatsumaki")
            lasterror = "Rate limited by tatsumaki"
            await asyncio.sleep(float(str(random.randint(7,18)) + "." + str(random.randint(1337,9999))))
        if "🎣  |  **" + client.user.name + "**, sold **" in message.content and "** __common__ items for 💴 **" in message.content:
            funkynumbercommon = re.findall('\d+', message.content)
            lastsoldcommon = funkynumbercommon[-2]
            soldcommonfor = funkynumbercommon[-1]
            totalcommonsold = int(totalcommonsold) + int(lastsoldcommon)
            cash = float(cash) + float(soldcommonfor)
        if "🎣  |  **" + client.user.name + "**, sold **" in message.content and "** __uncommon__ items for 💴 **" in message.content:
            funkynumberuncommon = re.findall('\d+', message.content)
            lastsolduncommon = funkynumberuncommon[-2]
            solduncommonfor = funkynumberuncommon[-1]
            totaluncommonsold = int(totaluncommonsold) + int(lastsolduncommon)
            cash = float(cash) + float(solduncommonfor)
        if "🎣  |  **" + client.user.name + "**, sold **" in message.content and "** __trash__ items for 💴 **" in message.content:
            funkynumbertrash = re.findall('\d+', message.content)
            lastsoldtrash = funkynumbertrash[-2]
            soldtrashfor = funkynumbertrash[-1]
            totaltrashsold = int(totaltrashsold) + int(lastsoldtrash)
            cash = float(cash) + float(soldtrashfor)

client.run(token, bot=False)
