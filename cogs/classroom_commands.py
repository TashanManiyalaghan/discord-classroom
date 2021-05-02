import discord
from discord.ext import commands
from classroom import *

class classroom_cogs(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    # Command to create a new classroom
    @commands.command()
    async def create_classroom(ctx, name):
        self.classroom = Classroom(name, ctx.author.id)
        category = await ctx.guild.create_category(name)
        announcementsChannel = await ctx.guild.create_text_channel('announcements', category = category)
        client.get_cog('Announcements').channel = announcementsChannel

# Cog setup
def setup(client):
    client.add_cog(classroom_cogs(client))