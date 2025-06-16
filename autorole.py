from discord.ext import commands
import discord

class AutoRole(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.role_id = None

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def setautorole(self, ctx, role: discord.Role):
        self.role_id = role.id
        await ctx.send(f"Auto-role set to {role.name}!")

    @commands.Cog.listener()
    async def on_member_join(self, member):
        if self.role_id:
            role = member.guild.get_role(self.role_id)
            await member.add_roles(role)

async def setup(bot):
    await bot.add_cog(AutoRole(bot))