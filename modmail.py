import discord
from discord.ext import commands

class ModMail(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.guild is None and not message.author.bot:
            guild = self.bot.guilds[0]
            channel = discord.utils.get(guild.text_channels, name="modmail")
            if channel:
                embed = discord.Embed(title="Mod Mail", description=message.content, color=discord.Color.blue())
                embed.set_author(name=message.author.name, icon_url=message.author.avatar.url)
                await channel.send(embed=embed)

async def setup(bot):
    await bot.add_cog(ModMail(bot))