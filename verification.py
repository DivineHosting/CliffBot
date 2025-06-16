from discord.ext import commands
import discord

class Verification(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def setupverify(self, ctx, role: discord.Role):
        msg = await ctx.send("React with ✅ to verify yourself!")
        await msg.add_reaction("✅")

        def check(reaction, user):
            return str(reaction.emoji) == "✅" and not user.bot

        while True:
            reaction, user = await self.bot.wait_for("reaction_add", check=check)
            await user.add_roles(role)
            await ctx.send(f"{user.mention} has been verified and given the {role.name} role!")

async def setup(bot):
    await bot.add_cog(Verification(bot))