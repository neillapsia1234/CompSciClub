# Tic-Tac-Toe by Frankie
# 1/16/21

import discord
from discord.ext import commands

class TicTacToe(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.gameOn = False
        

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, discord.ext.commands.errors.MissingRequiredArgument):
            await ctx.send("You can't play alone, ping ther person you want to play with ``.tictactoe @<YOUR FRIEND>``") 


    @commands.command()
    async def tictactoe(self, ctx, friend):
        self.gameOn = True
        spots = [0, 0, 0,
                0, 0, 0,
                0, 0, 0]
        
        gb = GameBoard(spots)

        await ctx.send(f"{ctx.author.mention}``` 1 | 2 | 3 \n"+
                    "-----------\n"+
                    " 4 | 5 | 6 \n"+
                    "-----------\n"+
                    " 7 | 8 | 9 ```")
        n = 0
        spot = 0

        for i in range(len(spots)):
            if self.gameOn:
                if n % 2 == 0:
                    msg = await self.client.wait_for(
                        "message",
                        check=lambda message: message.author == ctx.author and message.channel == ctx.channel and message.content.isdigit() and len(message.content) == 1
                    )
                    
                    if msg:
                        print(f"x turn")
                        print(f"n --> {n}")
                        print(f"OG GUY: {ctx.author}")
                        print(f"AUTHOR: {msg.author}")
                        spot = int(msg.content) - 1
                        print(f"SPOT --> {spot}")
                        while spots[spot] != 0 or spot < 0 or spot > 9 and self.gameOn:
                            await ctx.send(f"{msg.author.mention} SPOT IS NOT AVAILABLE TRY AGAIN")
                            msg = await self.client.wait_for(
                                "message",
                                check=lambda message: message.author == ctx.author and message.channel == ctx.channel and message.content.isdigit() and len(message.content) == 1
                            )
                            if msg:
                                spot = int(msg.content) - 1
                            print(f"SPOT --> {spot}")
                        spots[spot] = 1
                        print(' '.join(map(str, spots)))
                        gb = GameBoard(spots)
                        n += 1
                    await ctx.send(f"{friend} {gb}")
                else:
                    msg = await self.client.wait_for(
                        "message",
                        check=lambda message: message.author.mention[2:] == friend[3:] and message.channel == ctx.channel and message.content.isdigit() and len(message.content) == 1
                    )
                    if msg:
                        print(f"o turn")
                        print(f"n --> {n}")
                        print(f"FRIEND: {friend[3:]}")
                        print(f"AUTHOR: {msg.author.mention[2:]}")
                        print(f"FRIEND: {friend}")
                        print(f"AUTHOR: {msg.author.mention}")
                        spot = int(msg.content) - 1
                        print(f"SPOT --> {spot}")
                        while spots[spot] != 0 or spot < 0 or spot > 9 and self.gameOn:
                            await ctx.send(f"{msg.author.mention} SPOT IS NOT AVAILABLE TRY AGAIN")
                            msg = await self.client.wait_for(
                                "message",
                                check=lambda message: message.author.mention[2:] == friend[3:] and message.channel == ctx.channel and message.content.isdigit() and len(message.content) == 1
                            )
                            if msg:
                                spot = int(msg.content) - 1
                            print(f"SPOT --> {spot}")
                        spots[spot] = 2
                        print(' '.join(map(str, spots)))
                        gb = GameBoard(spots)
                        n += 1
                    await ctx.send(f"{ctx.author.mention} {gb}")
                
                
                if(gb.xWins(spots)):
                    await ctx.send(f"\n\n{ctx.author.mention} Wins!! \n\n{friend}")
                    self.gameOn = False
                    break
                elif(gb.oWins(spots)):
                    await ctx.send(f"\n\n{friend} Wins! \n\n{ctx.author.mention}")
                    self.gameOn = False
                    break
                if(n == 9 and not gb.xWins(spots) and not gb.oWins(spots)):
                    await ctx.send(f"\n\nIt's a tie! \n\n{friend} {ctx.author.mention}")
                    self.gameOn = False
                    break
            else:
                break
                

    @commands.command()
    async def endGame(self, ctx):
        if self.gameOn:
            await ctx.send("THE GAME HAS ENDED")
            self.gameOn = False
        else:
            await ctx.send("What game lol?")
        


def setup(client):
    client.add_cog(TicTacToe(client))





class GameBoard():
    def __init__(self, spots):
        self.spots = spots
        self.board = [["" for i in range(3)] for j in range(3)]

        self.populate(spots)

    def populate(self, init):
        n = 0
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if(init[n] == 0):
                    self.board[i][j] = "   "
                elif(init[n] == 1):
                    self.board[i][j] = " X "
                elif(init[n] == 2):
                    self.board[i][j] = " O "
                n += 1

    def xWins(self, spots):
        if((spots[0] == 1 and spots[1] == 1 and spots[2] == 1) or
           (spots[3] == 1 and spots[4] == 1 and spots[5] == 1) or
           (spots[6] == 1 and spots[7] == 1 and spots[8] == 1) or
           (spots[0] == 1 and spots[3] == 1 and spots[6] == 1) or
           (spots[1] == 1 and spots[4] == 1 and spots[7] == 1) or
           (spots[2] == 1 and spots[5] == 1 and spots[8] == 1) or
           (spots[0] == 1 and spots[4] == 1 and spots[8] == 1) or
           (spots[6] == 1 and spots[4] == 1 and spots[2] == 1)):
            return True
        else:
            return False
    def oWins(self, spots):
        if((spots[0] == 2 and spots[1] == 2 and spots[2] == 2) or
           (spots[3] == 2 and spots[4] == 2 and spots[5] == 2) or
           (spots[6] == 2 and spots[7] == 2 and spots[8] == 2) or
           (spots[0] == 2 and spots[3] == 2 and spots[6] == 2) or
           (spots[1] == 2 and spots[4] == 2 and spots[7] == 2) or
           (spots[2] == 2 and spots[5] == 2 and spots[8] == 2) or
           (spots[0] == 2 and spots[4] == 2 and spots[8] == 2) or
           (spots[6] == 2 and spots[4] == 2 and spots[2] == 2)):
            return True
        else:
            return False

    def isEmpty(self, spots, spot):
        return spots[spot] == 0

    def __str__(self):
        str = ""
        j = 0
        for i in range(len(self.board)):
            if(j == 1 or j == 2):
                str += "\n-----------\t-----------\n"
            str += self.board[i][0] + "|" + self.board[i][1] + "|" + self.board[i][2]
            if(i == 0):
                str += "\t 1 | 2 | 3 "
            elif(i == 1):
                str += "\t 4 | 5 | 6 "
            elif(i == 2):
                str += "\t 7 | 8 | 9 "
            j += 1
        return f"```{str}```"
