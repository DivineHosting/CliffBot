from discord.ext import commands
import discord

class TempVoice(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.category_name = "Temp VCs"

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        if after.channel and after.channel.name == "Join to Create":
            guild = member.guild
            category = discord.utils.get(guild.categories, name=self.category_name)
            if not category:
                category = await guild.create_category(self.category_name)
            channel = await guild.create_voice_channel(f"{member.name}'s VC", category=category)
            await member.move_to(channel)

            def check(_, __, after_):
                return after_.channel != channel

            await self.bot.wait_for("voice_state_update", check=lambda m, b, a: m == member and a.channel != channel)
            await channel.delete()

async def setup(bot):
    await bot.add_cog(TempVoice(bot))