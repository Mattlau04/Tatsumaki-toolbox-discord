import discord
import sys
from random import randint
from time import sleep

client = discord.Client()

userid = int(sys.argv[1])
channelid = int(sys.argv[2])
token = sys.argv[3]
howmuch = "t!credits"
checkcode = """🏧  |  **Credit Transfer**

```ruby
Transferring ¥"""

print("Loading...")

@client.event
async def on_ready():
    print ("Logged in")
    print(client.user.name)
    creditstowithdraw = 0
    try:
        txtchan = client.get_channel(int(channelid))
        await txtchan.send(howmuch)
    except Exception as e:
        print(e)
        print("closing...")
        sys.exit()

@client.event
async def on_message(message):
    veryepicname = client.user.name
    messagelen = len(veryepicname) + 8
    if message.author.id == 172002275412279296 and message.content[:messagelen] == "💳  |  **" + veryepicname:
        funkynumbers = [int(s) for s in message.content.split() if s.isdigit()]
        try:
            print(funkynumbers[-1])
            creditstowithdraw = funkynumbers[-1]
        except Exception:
            print(funkynumbers)
            creditstowithdraw = funkynumbers
        gimmecashlmao = "t!credits <@" + str(userid) + ">" + " " + str(creditstowithdraw)
        timetosleep = str(randint(6,8))
        sleep(float(timetosleep))
        try:
            txtchan = client.get_channel(int(channelid))
            await txtchan.send(gimmecashlmao)
        except Exception as f:
            print(f)
            print("closing...")
            quit()
    try:
        creditstowithdraw = funkynumbers[-1]
    except Exception:
        pass
    if message.author.id == 172002275412279296 and message.content[:49] == checkcode:
        epicnumbers = [int(s) for s in message.content.split() if s.isdigit()]
        try:
            print(epicnumbers[-1])
            confirmcodelol = epicnumbers[-1]
        except Exception:
            print(epicnumbers)
            confirmcodelol = epicnumbers
        timetosleep2 = str(randint(0,2))
        sleep(float(timetosleep2))
        try:
            txtchan = client.get_channel(int(channelid))
            await txtchan.send(confirmcodelol)
            print("done!")
            sys.exit()
        except Exception as n:
            print(n)
            print("closing...")
            quit()

try:
    client.run(token, bot=False)
except Exception as c:
    print(c)
