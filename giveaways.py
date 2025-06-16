import discord
from discord.ext import commands, tasks
import asyncio
import random

class Giveaways(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def giveaway(self, ctx, duration: int, *, prize: str):
        embed = discord.Embed(
            title="🎉 Giveaway!",
            description=f"Prize: **{prize}**\nReact with 🎉 to enter!\nEnds in {duration} seconds.",
            color=discord.Color.gold()
        )
        message = await ctx.send(embed=embed)
        await message.add_reaction("🎉")

        await asyncio.sleep(duration)

        new_message = await ctx.channel.fetch_message(message.id)
        users = await new_message.reactions[0].users().flatten()
        users = [u for u in users if not u.bot]

        if users:
            winner = random.choice(users)
            await ctx.send(f"🎊 Congratulations {winner.mention}, you won **{prize}**!")
        else:
            await ctx.send("😕 No valid entries, no winner this time.")

async def setup(bot):
    await bot.add_cog(Giveaways(bot))