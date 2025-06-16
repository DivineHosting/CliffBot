from discord.ext import commands
import openai

openai.api_key = "YOUR_OPENAI_API_KEY"  # Replace with your key

class AIChat(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="chat")
    async def ai_chat(self, ctx, *, prompt: str):
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}]
            )
            reply = response["choices"][0]["message"]["content"]
            await ctx.send(reply)
        except Exception as e:
            await ctx.send(f"⚠️ Error: {e}")

async def setup(bot):
    await bot.add_cog(AIChat(bot))