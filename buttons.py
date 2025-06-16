import discord
from discord.ext import commands

class Buttons(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def button(self, ctx):
        view = discord.ui.View()
        view.add_item(discord.ui.Button(label="Click Me!", style=discord.ButtonStyle.green))
        await ctx.send("Here's a button!", view=view)

async def setup(bot):
    await bot.add_cog(Buttons(bot))