from discord.ext import commands

class Permissions(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def securecmd(self, ctx):
        await ctx.send("This command is only for admins!")

    @securecmd.error
    async def securecmd_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You do not have permission to use this command.")

async def setup(bot):
    await bot.add_cog(Permissions(bot))