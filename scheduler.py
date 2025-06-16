from discord.ext import commands, tasks
import asyncio

class Scheduler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def remind(self, ctx, time: int, *, message: str):
        await ctx.send(f"⏳ I will remind you in {time} seconds!")
        await asyncio.sleep(time)
        await ctx.send(f"⏰ Reminder: {message}")

async def setup(bot):
    await bot.add_cog(Scheduler(bot))