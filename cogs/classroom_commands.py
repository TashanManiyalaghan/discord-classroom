import discord
from discord.ext import commands
from classroom import *

class classroom_cogs(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    # Command to create a new classroom
    @client.command()
    async def create_classroom(ctx, name):
        self.classroom = Classroom(name, ctx.author.id)
        category = await ctx.guild.create_category(name)
        announcementsChannel = await ctx.guild.create_text_channel('announcements', category = category)
        client.get_cog('Announcements').channel = announcementsChannel
    

    # Command to create a new event in the Schedule object.
    @commands.command()
    async def add_event(self, ctx, *, params):
        paramList = params.split()
        name = paramList[0]
        date = paramList[1].split('/')
        time = paramList[2].split(':')
        desc = ' '.join(paramList[3:])

        event = self.schedule.addEvent(name, int(date[0]), int(date[1]), int(date[2]), int(time[0]), int(time[1]), desc)
        await ctx.send(f'The following event was created: \n\t{event}')

    






# Cog setup
def setup(client):
    client.add_cog(classroom_cogs(client))