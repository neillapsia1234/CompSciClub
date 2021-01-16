class Player(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def getName(self, memeber)