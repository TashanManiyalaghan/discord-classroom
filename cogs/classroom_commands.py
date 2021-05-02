import discord
from discord.ext import commands
from classroom import *

class classroom_cogs(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    # Command to create a new classroom
    @commands.command()
    async def create_classroom(self, ctx, name):
        self.class_1 = Classroom(name, ctx.author)
        category = await ctx.guild.create_category(name)
        announcementsChannel = await ctx.guild.create_text_channel('announcements', category = category)
        self.client.get_cog('Announcements').channel = announcementsChannel
        self.newstudentsChannel = await ctx.guild.create_text_channel('new_students', category = category)

    # Create Reactions for new memebers joining
    @commands.Cog.listener()
    async def on_member_join(self, member):
        self.class_1.addstudent(member.id)
        msg = member.name + ' has joined the ' + self.class_1.name + ' class as a student'
        await self.newstudentsChannel.send(msg)
    

# Cog setup
def setup(client):
    client.add_cog(classroom_cogs(client))