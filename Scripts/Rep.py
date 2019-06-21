import discord
import sys

client = discord.Client()

userid = int(sys.argv[1])
channelid = int(sys.argv[2])
token = sys.argv[3]
text = "t!rep <@" + str(userid) + ">"
print("Loading...")

@client.event
async def on_ready():
    print ("Logged in")
    try:
        txtchan = client.get_channel(int(channelid))
        await txtchan.send(text)
        print("closing...")
    except Exception as e:
        print(e)
        print("closing...")
    quit() #Btw this is coded by Mattlau04

try:
    client.run(token, bot=False)
except Exception as c:
    print(c)
