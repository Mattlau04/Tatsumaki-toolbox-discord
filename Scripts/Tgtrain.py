import discord
import sys
import random
from time import sleep
import os
import re
import asyncio
from math import *

client = discord.Client()
successnum = 0
failnum = 0
exgained = 0
totalexpgained = 0
totalsf = 0
questcompleted = 0
token = sys.argv[1]
txtchanid = sys.argv[2]
msgcontent = ['t!pet train', 't!pets train', 't!tg train', 't!tatsugotchi train']
levelgained = 0
totalXP = "Unkwown until we get a success message"
XPuntillvlup = "Unkwown until we get a success message"
lastmessage = "None"
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
                try:
                    averageXPbySuccess = str(int(totalexpgained) / int(successnum))
                except Exception:
                    averageXPbySuccess = "Unkwown until we get a success message"
                try:
                    estimatedmsglvlupsuccess = int(XPuntillvlup) / float(averageXPbySuccess)
                except Exception:
                    estimatedmsglvlupsuccess = "Unkwown until we get a success message"
                # try:
                    # if totalsf > 100:
                        # estimatedmsglvlup = int(estimatedmsglvlupsuccess) * int((int(totalsf) / int(successnum)))
                    # else:
                        # estimatedmsglvlup = int(estimatedmsglvlupsuccess) * int(100 / 35)
                        # if estimatedmsglvlup == 0:
                            # estimatedmsglvlup = 1
                # except Exception:
                    # estimatedmsglvlup = "Unkwown until we get a success message"
                try:
                    estimatedmsglvluparondi = ceil(estimatedmsglvlup)
                except Exception:
                    estimatedmsglvluparondi = "Unkwown until we get a success message"
                try:
                    estimatedmsglvlupsuccessarondi = ceil(estimatedmsglvlupsuccess)
                except Exception:
                    estimatedmsglvlupsuccessarondi = "Unkwown until we get a success message"
                totalsf = successnum + failnum
                os.system('cls')
                print("#=====================#")
                print("+ Tatsugotchi trainer +")
                print("#=====================#")
                print('')
                print("successes: " + str(successnum))
                print("Failed: " + str(failnum))
                print("% of success: " + str(percentage(successnum, totalsf))[:5])
                print("Exp gained: " + str(totalexpgained))
                print("Level gained: " + str(levelgained))
                print("Total XP: " + str(totalXP))
                print("XP until level up: " + str(XPuntillvlup))
                print("Quests completed: " + str(questcompleted))
                print('')
                if averageXPbySuccess == "Unkwown until we get a success message":
                    print("Average XP gained by success: " + str(averageXPbySuccess))
                else:
                    print("Average XP gained by success: " + str(averageXPbySuccess)[:5])
                print("Estimated number of success before leveling up: " + str(estimatedmsglvlupsuccessarondi))
                # print("Estimated number of message before leveling up: " + str(estimatedmsglvluparondi))
                print('')
                print("Last message: " + str(lastmessage))
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
    global levelgained
    global lastmessage
    global totalXP
    global XPuntillvlup
    global questcompleted
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
                    lastmessage = embed.description.splitlines()[0]
                    if "Congratulations! Your Tatsugotchi has reached level" in embed.description:
                        levelgained = int(levelgained) + 1
                    try:
                        exgained = funkynumbe[0]
                        totalXP = funkynumbe[1]
                        totalexpgained = totalexpgained + int(exgained)
                        XPuntillvlup = int(funkynumbe[2]) - int(funkynumbe[1])
                    except Exception:
                        exgained = funkynumbe[0]
                        totalXP = funkynumbe[1]
                        totalexpgained = totalexpgained + int(exgained)
                        XPuntillvlup = int(funkynumbe[2]) - int(funkynumbe[1])
                elif embed.author.name == "Try again!":
                    lastmessage = embed.description.splitlines()[0]
                    failnum = failnum + 1
                if "Congratulations! You have completed a quest. Check it out with `t!tatsugotchi quests`!" in embed.description:
                    questcompleted = questcompleted + 1
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
