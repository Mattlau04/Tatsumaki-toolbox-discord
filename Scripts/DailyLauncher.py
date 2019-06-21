import discord
import sys
import os
import subprocess

client = discord.Client()

userid = str(sys.argv[1])
channelid = str(sys.argv[2])
winpy = str(sys.argv[3])
print("loading tokens...")
tokenlist = open("tokens.txt").read().splitlines()
print("Starting subprocess...")
for token in tokenlist:
    p = subprocess.Popen([winpy,'Scripts/Daily.py',userid,channelid,token],stdout=open(os.devnull, "w"), stderr=subprocess.STDOUT)
print("exiting...")
quit()
