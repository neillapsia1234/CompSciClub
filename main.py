import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix=".")

#.tictactoe @friend
#play tictactoe
#only accept stuff from those two people
#.endgame

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            try:
                client.load_extension(f"cogs.{filename[:-3]}")
                print(f"Loaded {filename}")
            except Exception as e:
                print(f"Failed to load {filename}")
                print(f"[ERROR] {e}")






client.run('Nzk4OTI2OTgwNTk3ODA5MTUy.X_8Iuw.dJ1vbGGuQIuwoRVTVtiRJ6As1Rs')
#client.run(os.environ.get('compscitoken'))
