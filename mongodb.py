from discord.ext import commands
from pymongo import MongoClient
import os

class MongoDB(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.cluster = MongoClient("mongodb://localhost:27017/")
        self.db = self.cluster["discord_bot"]
        self.users = self.db["users"]

    @commands.command()
    async def mongobal(self, ctx):
        user_id = str(ctx.author.id)
        user = self.users.find_one({"_id": user_id})
        if user:
            await ctx.send(f"You have {user['coins']} coins.")
        else:
            self.users.insert_one({"_id": user_id, "coins": 100})
            await ctx.send("MongoDB account created with 100 coins.")

async def setup(bot):
    await bot.add_cog(MongoDB(bot))