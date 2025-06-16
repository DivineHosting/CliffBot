from discord.ext import commands

class AutoResponse(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.triggers = {
            "hello": "Hi there! 👋",
            "bye": "Goodbye! 👋"
        }

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
        content = message.content.lower()
        for trigger, response in self.triggers.items():
            if trigger in content:
                await message.channel.send(response)
                break

async def setup(bot):
    await bot.add_cog(AutoResponse(bot))