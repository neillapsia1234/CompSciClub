# Tic-Tac-Toe by Frankie
# 1/16/21

import discord
from discord.ext import commands

class TicTacToe(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.gameOff = False
        self.n = 0
        self.playerX = ""
        self.playerO = ""
        self.spots = [0, 0, 0,
             0, 0, 0,
             0, 0, 0]
        self.turnEnded = False
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.content.isdigit() and len(message.content) == 1 and message.author.equals(playerX) and n % 2 == 0:
            self.spots[int(message.content) - 1] = 1
            self.turnEnded = True
        elif message.content.isdigit() and len(message.content) == 1 and message.author.equals(playerO):
            self.spots[int(message.content) - 1] = 2
            self.turnEnded = True
        print(str(self.spots)[1:-1])

    @commands.command()
    async def tictactoe(self, ctx, friend):
        

        gb = GameBoard(self.spots)
        
        self.playerX = ctx.author
        self.playerO = friend

        await ctx.send(f"{self.playerX.mention}``` 1 | 2 | 3 \n"+
                    "-----------\n"+
                    " 4 | 5 | 6 \n"+
                    "-----------\n"+
                    " 7 | 8 | 9 ```")
        

        for i in range(len(self.spots)): # total 9 turns in a game

            if self.n % 2 == 0 and not self.turnEnded: # if n is even it's player X's turn
                gb = GameBoard(self.spots)
                await ctx.send(f"{self.playerX.mention} ```{gb}```")
                self.turnEnded = False

            elif not self.turnEnded: # otherwise it's player O's turn
                gb = GameBoard(self.spots)
                await ctx.send(f"{self.playerO} ```{gb}```")
                self.turnEnded = False


            self.n+=1


            if(gb.xWins(self.spots)):
                await ctx.send(f"{self.playerX.mention} Wins!")
                break

            elif(gb.oWins(self.spots)):
                await ctx.send(f"{self.playerO} Wins!")
                break

            if(n == 9 and not gb.xWins(self.spots) and not gb.oWins(self.spots)):
                await ctx.send("It's a tie!")
        # for i in range(len(self.spots)):
        #     if(n % 2 == 0):
        #         if ctx.author == playerX:
        #             spot = int(input("Player X: ")) - 1

        #         while(self.spots[spot] != 0 or spot < 0):
        #             spot = int(input("SPOT IS NOT AVAILABLE TRY AGAIN\nPlayer X: ")) - 1
        #         self.spots[spot] = 1

        #     else:
        #         spot = int(input("Player O: ")) - 1
        #         while(self.spots[spot] != 0 or spot < 0):
        #             spot = int(input("SPOT IS NOT AVAILABLE TRY AGAIN\nPlayer O: ")) - 1
        #         self.spots[spot] = 2

        #     n += 1
        #     gb = GameBoard(self.spots)
        #     print(gb)
            
            

# if self.gameOff:
#     await ctx.send("THE GAME HAS ENDED")
#     break

    @commands.command()
    async def endGame(self, ctx):
        ctx = ""
        self.gameOff = True
    
    
        
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


