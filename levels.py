from discord.ext import commands
import json
import os

class Levels(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.file = "levels.json"
        if not os.path.exists(self.file):
            with open(self.file, 'w') as f:
                json.dump({}, f)

    def add_xp(self, user_id):
        with open(self.file) as f:
            levels = json.load(f)
        levels[str(user_id)] = levels.get(str(user_id), 0) + 10
        with open(self.file, 'w') as f:
            json.dump(levels, f)

    def get_level(self, user_id):
        with open(self.file) as f:
            levels = json.load(f)
        return levels.get(str(user_id), 0)

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
        self.add_xp(message.author.id)

    @commands.command()
    async def level(self, ctx):
        xp = self.get_level(ctx.author.id)
        await ctx.send(f"{ctx.author.mention}, you have {xp} XP!")

async def setup(bot):
    await bot.add_cog(Levels(bot))