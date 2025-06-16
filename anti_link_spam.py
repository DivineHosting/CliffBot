from discord.ext import commands
import discord
import time

class AntiLinkSpam(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.user_times = {}

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return

        if "http://" in message.content or "https://" in message.content:
            await message.delete()
            await message.channel.send(f"{message.author.mention} links are not allowed!")
            return

        now = time.time()
        user_id = message.author.id

        if user_id in self.user_times:
            if now - self.user_times[user_id] < 3:
                await message.delete()
                await message.channel.send(f"{message.author.mention}, please avoid spamming!")
        self.user_times[user_id] = now

async def setup(bot):
    await bot.add_cog(AntiLinkSpam(bot))