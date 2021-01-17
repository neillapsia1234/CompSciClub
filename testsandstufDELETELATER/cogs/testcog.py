import discord
from discord.ext import commands

class TicTacToe(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.gameOff = False
        self.spots = [0, 0, 0, 
                       0, 0, 0, 
                       0, 0, 0]

    # @commands.command()
    # async def test(self, ctx, friend):
        
        


    # @commands.command()
    # async def endGame(self, ctx):
    #     ctx = ""
    #     self.gameOff = True
    
    
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.content.isdigit() and len(message.content) == 1 and message.author == :
            self.spots[int(message.content) - 1] = 1
        print(str(self.spots)[1:-1])
        
def setup(client):
    client.add_cog(TicTacToe(client))
    

