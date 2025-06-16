from discord.ext import commands
import discord

class AFK(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.afk_users = {}

    @commands.command()
    async def afk(self, ctx, *, reason="AFK"):
        self.afk_users[ctx.author.id] = reason
        await ctx.send(f"{ctx.author.display_name} is now AFK: {reason}")

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id in self.afk_users:
            del self.afk_users[message.author.id]
            await message.channel.send(f"Welcome back {message.author.mention}, I removed your AFK status.")

        for user_id, reason in self.afk_users.items():
            if message.mentions and any(u.id == user_id for u in message.mentions):
                user = message.guild.get_member(user_id)
                await message.channel.send(f"{user.display_name} is AFK: {reason}")

async def setup(bot):
    await bot.add_cog(AFK(bot))