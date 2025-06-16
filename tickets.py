import discord
from discord.ext import commands

class Tickets(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.ticket_category_name = "Tickets"

    @commands.command()
    async def ticket(self, ctx):
        guild = ctx.guild
        category = discord.utils.get(guild.categories, name=self.ticket_category_name)
        if category is None:
            category = await guild.create_category(self.ticket_category_name)

        overwrites = {
            guild.default_role: discord.PermissionOverwrite(read_messages=False),
            ctx.author: discord.PermissionOverwrite(read_messages=True, send_messages=True),
            guild.me: discord.PermissionOverwrite(read_messages=True, send_messages=True)
        }

        channel = await guild.create_text_channel(f"ticket-{ctx.author.name}", overwrites=overwrites, category=category)
        await channel.send(f"{ctx.author.mention}, this is your support ticket.")
        await ctx.send(f"✅ Ticket created: {channel.mention}")

async def setup(bot):
    await bot.add_cog(Tickets(bot))