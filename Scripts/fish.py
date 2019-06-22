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
minimumtosell = sys.argv[3]
cash = 0
totalcommonsold = 0
totaluncommonsold = 0
totaltrashsold = 0
totalcommoncatched = 0
totaluncommoncatched = 0
totaltrashcatched = 0
totalrarecatched = 0
totalstuffcatched = 0
howmanycommonsell = 0
howmanyuncommonsell = 0
howmanytrashsell = 0
lasterror = "noerror"
isleeplol = int(random.randint(31,37))
totalnumberfishing = 0
print("Loading...")
os.system('cls')
print("#=========#")
print("+ Loading +")
print("#=========#")
print('')
print("Total gain: 0 (this will go down until the sell part, so don't freak out when it goes down)")
print('')
print("Total number of fishing: 0")
print('')
print("Fish rewards:")
print("Common: 12 yen")
print("Uncommon: 20 yen")
print("Garbage: 6 yen")
print("Rare: 1250 yen")
print('')
print("Catch rate for items:")
print("Common: 34.85%")
print("Uncommon: 10%")
print("Garbage: 55%")
print("Rare: 0.15%")
print('')
print("(these stats are from the official tatsumaki discord server)")

@client.event
async def on_ready():
    global cash
    global isleeplol
    global totalnumberfishing
    global lasterror
    global howmanytrashsell
    global howmanycommonsell
    global howmanyuncommonsell
    txtchan = client.get_channel(int(txtchanid))
    await txtchan.send("t!fish inv")
    await asyncio.sleep(float((str("1.") + str(random.randint(1337,9999)))))
    os.system('cls')
    print("#=============#")
    print("+ Fishing bot +")
    print("#=============#")
    print('')
    print("Total gain: 0 (this will go down until the sell part, so don't freak out when it goes down)")
    print('')
    print("Total number of fishing: 0")
    print('')
    print("Fish rewards:")
    print("Common: 12 yen")
    print("Uncommon: 20 yen")
    print("Garbage: 6 yen")
    print("Rare: 1250 yen")
    print('')
    print("Catch rate for items:")
    print("Common: 34.85%")
    print("Uncommon: 10%")
    print("Garbage: 55%")
    print("Rare: 0.15%")
    print('')
    print("(these stats are from the official tatsumaki discord server)")
    await asyncio.sleep(5)
    while True:
        loopfishing = random.randint(7,20)
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
                print("Current number of common fish in inventory: " + str(howmanycommonsell))
                print("Current number of uncommon fish in inventory: " + str(howmanyuncommonsell))
                print("Current number of trash items in inventory: " + str(howmanytrashsell))
                print('')
                print("Total common fish catched: " + str(totalcommoncatched) + " [" + str(percentage(totalcommoncatched, totalstuffcatched)) + "%]")
                print("Total uncommon fish catched: " + str(totaluncommoncatched) + " [" + str(percentage(totaluncommoncatched, totalstuffcatched)) + "%]")
                print("Total trash items catched: " + str(totaltrashcatched) + " [" + str(percentage(totaltrashcatched, totalstuffcatched)) + "%]")
                print("Total rare fish catched: " + str(totalrarecatched) + " [" + str(percentage(totalrarecatched, totalstuffcatched)) + "%]")
                print('')
                print("Next fishing in " + str(count) + " seconds")
                if not lasterror == "noerror":
                    print('')
                    print("Error on last fishing: " + str(lasterror))
                await asyncio.sleep(1)
            isleeplol = int(random.randint(32,37))
            await asyncio.sleep(float((str("0.") + str(random.randint(1337,9999)))))
        print('')
        if not int(howmanycommonsell) >= int(minimumtosell) and not int(howmanyuncommonsell) >= int(minimumtosell) and not int(howmanytrashsell) >= int(minimumtosell):
            print("Selling nothing because no item have the minimum ammont required of " + str(minimumtosell))
        if int(howmanycommonsell) >= int(minimumtosell):
            print("selling common...")
            await txtchan.send("t!fish sell common")
            howmanycommonsell = 0
            await asyncio.sleep(float(str(random.randint(6,9)) + "." + str(random.randint(1337,9999))))
        if int(howmanyuncommonsell) >= int(minimumtosell):
            print("selling uncommon...")
            await txtchan.send("t!fish sell uncommon")
            howmanyuncommonsell = 0
            await asyncio.sleep(float(str(random.randint(6,9)) + "." + str(random.randint(1337,9999))))
        if int(howmanytrashsell) >= int(minimumtosell):
            print("selling garbage...")
            await txtchan.send("t!fish sell garbage")
            howmanytrashsell = 0
            await asyncio.sleep(float(str(random.randint(6,9)) + "." + str(random.randint(1337,9999))))
        isleeplol = random.randint(30,35)
        print('')
        await asyncio.sleep(float("0." + str(random.randint(1337,9999))))

@client.event
async def on_message(message):
    global lasterror
    global totalcommonsold
    global totaluncommonsold
    global totaltrashsold
    global totalcommoncatched
    global totaluncommoncatched
    global totaltrashcatched
    global totalrarecatched
    global totalstuffcatched
    global howmanytrashsell
    global howmanycommonsell
    global howmanyuncommonsell
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
        if "🎣  |  **" + client.user.name + "**, **you caught: " in message.content and "You paid 💴 **10** for casting." in message.content:
            totalstuffcatched = totalstuffcatched + 1
            if "🔋" in message.content or "🔧" in message.content or "👞" in message.content or "📎" in message.content or "🛒" in message.content:
                totaltrashcatched = totaltrashcatched + 1
                howmanytrashsell = int(howmanytrashsell) + 1
            elif "🐠" in message.content:
                totaluncommoncatched = totaluncommoncatched + 1
                howmanyuncommonsell = int(howmanyuncommonsell) + 1
            elif "🐟" in message.content:
                totalcommoncatched = totalcommoncatched + 1
                howmanycommonsell = int(howmanycommonsell) + 1
            else:
                totalrarecatched = totalrarecatched + 1
        if "🎣  |  **" + client.user.name + "**, displaying fishy inventory:" in message.content:
            funkynumberinvstart = re.findall('\d+', message.content)
            howmanytrashsell = funkynumberinvstart[-1]
            howmanyuncommonsell = funkynumberinvstart[-2]
            howmanycommonsell = funkynumberinvstart[-3]

def percentage(part, whole):
    if whole == 0:
        return 0
    elif part == 0:
        return 0
    else:
        return 100 * float(part)/float(whole)

client.run(token, bot=False)
