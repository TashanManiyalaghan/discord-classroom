import discord
from discord.ext import commands

# Temporary cog
class Temp(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Basic Discord command
    @commands.command(aliases = ['hi', 'hey'])
    async def hello(self, ctx):
        await ctx.send('Hello')

# Cog setup
def setup(client):
    client.add_cog(Temp(client))