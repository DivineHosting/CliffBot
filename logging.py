from discord.ext import commands
import discord

class Logging(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        if not message.author.bot:
            log = f"🗑️ Message deleted in {message.channel}: {message.content}"
            await self.log(message.guild, log)

    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        if not before.author.bot:
            log = (f"✏️ Message edited in {before.channel}\n"
                   f"Before: {before.content}\nAfter: {after.content}")
            await self.log(before.guild, log)

    @commands.Cog.listener()
    async def on_member_join(self, member):
        await self.log(member.guild, f"✅ {member} joined the server.")

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        await self.log(member.guild, f"❌ {member} left the server.")

    async def log(self, guild, message):
        log_channel = discord.utils.get(guild.text_channels, name="logs")
        if log_channel:
            await log_channel.send(message)

async def setup(bot):
    await bot.add_cog(Logging(bot))