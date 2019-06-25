import discord
import sys
import random
import os
import asyncio

client = discord.Client()

token = sys.argv[1]
txtchanid = sys.argv[2]
idofcookietarget = sys.argv[3]
sentcookie = 0
print("Loading...")

@client.event
async def on_ready():
    global sentcookie
    os.system('cls')
    txtchan = client.get_channel(int(txtchanid))
    if not idofcookietarget == "random" and not idofcookietarget == "Random":
        namofcookietarget = client.get_user(int(idofcookietarget))
    print("Logged in")
    print("=================")
    while True:
        if idofcookietarget == "random" or idofcookietarget == "Random":
            randommember = random.choice(txtchan.members)
            if randommember.id == client.user.id:
                while randommember.id == client.user.id:
                    randommember = random.choice(txtchan.members)
        waitforhowlong = int(str(random.randint(15,20)))
        for count in reversed(range(1, waitforhowlong+1)):
            os.system('cls')
            print("#===============#")
            print("+ Cookie sender +")
            print("#===============#")
            print('')
            print("Number of cookies sent: " + str(sentcookie))
            if idofcookietarget == "random" or idofcookietarget == "Random":
                print("Next cookies target: " + str(randommember.name))
                print("Next target id: " + str(randommember.id))
            else:
                print("Cookies target: " + str(namofcookietarget.name))
                print("Cookies target id: " + str(idofcookietarget))
            print('')
            print(str(count) + " Seconds until next cookie")
            await asyncio.sleep(1)
        await asyncio.sleep(float(str("0.") + str(random.randint(1337,9999))))
        if idofcookietarget == "random" or idofcookietarget == "Random":
            await txtchan.send("t!cookie " + str(randommember.id))
            sentcookie = int(sentcookie) + 1
        else:
            await txtchan.send("t!cookie " + str(idofcookietarget))
            sentcookie = int(sentcookie) + 1

try:
    client.run(token, bot=False)
except Exception as c:
    print(c)
