#hello from my school computer
# now testing from a different account

import discord
from discord.ext import commands

client = commands.Bot(command_prefix=".")



@client.event
async def on_ready():
	print('We have logged in as {0.user}'.format(client))


@client.command()
async def tictactoe(ctx, playerO):
    spots = [0, 0, 0,
             0, 0, 0,
             0, 0, 0]

    gb = GameBoard(spots)
    await ctx.send("``` 1 | 2 | 3 \n"+
                   "-----------\n"+
                   " 4 | 5 | 6 \n"+
                   "-----------\n"+
                   " 7 | 8 | 9 ```")
    n = 0


    for i in range(len(spots)):
        if(n % 2 == 0):


            # spot = int(input("Player X: ")) - 1
            if message.author == playerX:
                int(message) -= 1

            while(spots[spot] != 0 or spot < 0):
                spot = int(input("SPOT IS NOT AVAILABLE TRY AGAIN\nPlayer X: ")) - 1
            spots[spot] = 1

        else:
            spot = int(input("Player O: ")) - 1
            while(spots[spot] != 0 or spot < 0):
                spot = int(input("SPOT IS NOT AVAILABLE TRY AGAIN\nPlayer O: ")) - 1
            spots[spot] = 2

        n += 1
        gb = GameBoard(spots)
        print(gb)
        if(gb.xWins(spots)):
            print("Player X Wins!")
            break
        elif(gb.oWins(spots)):
            print("Player O Wins!")
            break
    if(n == 9 and not gb.xWins(spots) and not gb.oWins(spots)):
        print("It's a tie!")




#Tic-Tac-Toe by Frankie
class GameBoard:

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
        return str


TOKEN = open("token.txt", "r")
client.run(TOKEN.read())
