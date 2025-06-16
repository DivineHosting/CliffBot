from discord.ext import commands
import json
import os

class Economy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.data_file = "wallet.json"
        if not os.path.exists(self.data_file):
            with open(self.data_file, 'w') as f:
                json.dump({}, f)

    def get_balance(self, user_id):
        with open(self.data_file) as f:
            users = json.load(f)
        return users.get(str(user_id), 0)

    def update_balance(self, user_id, amount):
        with open(self.data_file) as f:
            users = json.load(f)
        users[str(user_id)] = users.get(str(user_id), 0) + amount
        with open(self.data_file, 'w') as f:
            json.dump(users, f)

    @commands.command()
    async def balance(self, ctx):
        balance = self.get_balance(ctx.author.id)
        await ctx.send(f"{ctx.author.mention}, you have 💰 {balance} coins.")

    @commands.command()
    async def daily(self, ctx):
        self.update_balance(ctx.author.id, 100)
        await ctx.send(f"{ctx.author.mention}, you received 💰 100 coins today!")

async def setup(bot):
    await bot.add_cog(Economy(bot))