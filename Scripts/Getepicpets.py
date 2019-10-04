import discord
import sys
import random
import os
import asyncio

client = discord.Client()
failnum = 0
token = sys.argv[1]
txtchanid = sys.argv[2]
nameofwantedpettemp = sys.argv[3]
nameofwantedpet = nameofwantedpettemp.replace("-_-", " ")
print("loading...")

@client.event
async def on_ready():
    global failnum
    os.system('cls')
    veryepicpfp = client.user.avatar
    print ("Logged in")
    print ("=================")
    os.system('cls')
    print("#===================#")
    print("+ Custom pet getter +")
    print("#===================#")
    print('')
    print("Number of attempt: 0")
    print("Total cost: 0")
    print("Wanted pet: " + str(nameofwantedpet))
    print("The script will start in about 5 seconds")
    txtchan = client.get_channel(int(txtchanid))
    while True:
        await txtchan.send("t!tg shop")
        await asyncio.sleep(float(str(random.randint(2,4)) + "." + str(random.randint(1337,9999))))
        await txtchan.send("1")
        await asyncio.sleep(float(str(random.randint(2,4)) + "." + str(random.randint(1337,9999))))
        await txtchan.send("confirm")
        await asyncio.sleep(float(str(random.randint(2,4)) + "." + str(random.randint(1337,9999))))
        waitforhowlong = int(str(random.randint(7,11)))
        failnum = failnum + 1
        await asyncio.sleep(float(str("0." + str(random.randint(1337,9999)))))
        for count in reversed(range(1, waitforhowlong+1)):
            totalcost = int(failnum) * 900
            os.system('cls')
            print("#===================#")
            print("+ Custom pet getter +")
            print("#===================#")
            print('')
            print("Number of attempt: " + str(failnum))
            print("Total cost: " + str(totalcost))
            print("Wanted pet: " + str(nameofwantedpet))
            print(str(count) + " Seconds until next buy")
            await asyncio.sleep(1)
        else:
            await asyncio.sleep(float(str("0.") + str(random.randint(1337,9999))))

@client.event
async def on_message(message):
    global failnum
    if message.author.id == 172002275412279296 and str(message.channel.id) == str(txtchanid):
        if "💊  |  **You open a capsule and find: " + str(nameofwantedpet) + "!" in message.content:
            print('')
            print("Found the perfect pet!")
            print("You can close this window")
            os.system("pause > NUL")
            quit()
            
        if "💊  |  **You open a capsule and find: Gold Cat!" in message.content or "💊  |  **You open a capsule and find: Gold Bird!" in message.content or "💊  |  **You open a capsule and find: Gold Dog!" in message.content:
            print('')
            print("YOU GOT A LEGENDARY PET!!!!!!!!!!!!!!!!!!!!!!")
            print("Since they're so rare, i paused the script so you can just close it and keep the legendary pet")
            print("otherwise, just press any key to continue")
            os.system("pause > NUL")
            
        if "<:no:390511503238758400>  |  **" + client.user.name + "**, **you don't have enough credits for that!**" == message.content:
            failnum = int(failnum) - 1
            print('')
            print("Looks like you're out of money :/")
            print("Get some more cash, then press any key to continue")
            os.system("pause > NUL")
            
try:
    client.run(token, bot=False)
except Exception as c:
    print(c)
