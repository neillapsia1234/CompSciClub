import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix=".")

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






#client.run('<YOUR TOKEN>')
client.run(os.environ.get('compscitoken'))
