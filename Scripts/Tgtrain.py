import discord
import sys
import random
from time import sleep
import os
import re
import asyncio

client = discord.Client()
successnum = 0
failnum = 0
exgained = 0
totalexpgained = 0
totalsf = 0
token = sys.argv[1]
txtchanid = sys.argv[2]
msgcontent = ['t!pet train', 't!pets train', 't!tg train', 't!tatsugotchi train']
waitratelimit = 'False'
print("loading...")

@client.event
async def on_ready():
    os.system('cls')
    veryepicpfp = client.user.avatar
    print ("Logged in")
    print ("=================")
    txtchan = client.get_channel(int(txtchanid))
    while True:
        if waitratelimit == 'False':
            await txtchan.send(random.choice(msgcontent))
            waitforhowlong = int(str(random.randint(12,15)))
            asyncio.sleep(float(str("0." + str(random.randint(1337,9999)))))
            for count in reversed(range(1, waitforhowlong+1)):
                totalsf = successnum + failnum
                os.system('cls')
                print("#=====================#")
                print("+ Tatsugotchi trainer +")
                print("#=====================#")
                print('')
                print("successes: " + str(successnum))
                print("Failed: " + str(failnum))
                print("% of success: " + str(percentage(successnum, totalsf)))
                print("Exp gained: " + str(totalexpgained))
                print('')
                print(str(count) + " Seconds until next training")
                await asyncio.sleep(1)
        else:
            await asyncio.sleep(float(str("0.") + str(random.randint(1337,9999))))

@client.event
async def on_message(message):
    global successnum
    global failnum
    global exgained
    global totalexpgained
    global waitratelimit
    global totalsf
    if message.author.id == 172002275412279296 and str(message.channel.id) == str(txtchanid):
        sentembed = message.embeds
        if "<:no:390511503238758400>  |  **" + client.user.name + "**, **please wait" in message.content and "seconds before attempting to train your" in message.content:
            owourratelimited = re.findall('\d+', message.content)
            waitratelimit = 'True'
            print("You have to wait " + owourratelimited[-3] + " seconds before continuing")
            await asyncio.sleep(float(owourratelimited[-3]))
            waitratelimit = 'False'
        if sentembed:
            embed = sentembed[0]
            if str(client.user.avatar_url_as(size=128,static_format='jpg')) == str(embed.author.icon_url):
                if embed.author.name == "Success!":
                    successnum = successnum + 1
                    funkynumbe = re.findall('\d+', embed.description)
                    try:
                        exgained = funkynumbe[0]
                        totalexpgained = totalexpgained + int(exgained)
                    except Exception:
                        exgained = funkynumbe[0]
                        totalexpgained = totalexpgained + int(exgained)
                elif embed.author.name == "Try again!":
                    failnum = failnum + 1
            totalsf = successnum + failnum
        if "<:no:390511503238758400>  |  **" + client.user.name + "**, **please wait" in message.content:
            print("-------------------------------")
            print("You got a " + owourratelimited[-3] + " seconds rate limit")

def percentage(part, whole):
    if whole == 0:
        return 0
    elif part == 0:
        return 0
    else:
        return 100 * float(part)/float(whole)


try:
    client.run(token, bot=False)
except Exception as c:
    print(c)
