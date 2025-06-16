from discord.ext import commands
import discord

class EmbedTemplates(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def customembed(self, ctx, title: str, *, description: str):
        embed = discord.Embed(title=title, description=description, color=discord.Color.random())
        embed.set_footer(text="Custom Embed Template")
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(EmbedTemplates(bot))