from discord.ext import commands
import discord

class Greetings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.system_channel
        if channel:
            await channel.send(f"Welcome {member.mention} to {member.guild.name}!")

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = member.guild.system_channel
        if channel:
            await channel.send(f"{member.name} has left the server.")

async def setup(bot):
    await bot.add_cog(Greetings(bot))