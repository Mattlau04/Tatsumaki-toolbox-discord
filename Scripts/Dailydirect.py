import discord
import sys

client = discord.Client()

userid = int(sys.argv[1])
channelid = int(sys.argv[2])
token = sys.argv[3]
print("Loading...")

@client.event
async def on_ready():
    print ("Logged in")
    try:
        txtchan = client.get_channel(int(channelid))
    except Exception as f:
        print(f)
        pass
    try:
        await txtchan.send("t!daily <@" + str(userid) + ">")
        print("closing...")
    except Exception as e:
        print(e)
        print("closing...")
    quit()

try:
    client.run(token, bot=False)
except Exception as c:
    print(c)
    pass
