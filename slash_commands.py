from discord import app_commands
from discord.ext import commands

class SlashCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name='hello', description='Say hello to the bot!')
    async def hello(self, interaction):
        await interaction.response.send_message(f'Hello {interaction.user.mention}!', ephemeral=True)

async def setup(bot):
    await bot.add_cog(SlashCommands(bot))