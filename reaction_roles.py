import discord
from discord.ext import commands

class ReactionRoles(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def reactrole(self, ctx, role: discord.Role, emoji: str):
        msg = await ctx.send(f"React with {emoji} to get the {role.name} role.")
        await msg.add_reaction(emoji)

        def check(reaction, user):
            return str(reaction.emoji) == emoji and not user.bot

        while True:
            reaction, user = await self.bot.wait_for('reaction_add', check=check)
            await user.add_roles(role)
            await ctx.send(f"{user.mention} got the {role.name} role!")

async def setup(bot):
    await bot.add_cog(ReactionRoles(bot))