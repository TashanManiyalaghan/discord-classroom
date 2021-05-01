import discord
from discord.ext import commands
from classroom import *

class classroom_cogs(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    # Command to create a new classroom
    @commands.command()
    async def create_classroom(self, ctx, name):
        class_1 = Classroom(name, ctx.author)
        category = await ctx.guild.create_category(name)
        announcementsChannel = await ctx.guild.create_text_channel('announcements', category = category)
        self.client.get_cog('Announcements').channel = announcementsChannel
        print(class_1)

    # Create Reactions for new memebers joining
    @commands.Cog.listener()
    async def on_member_join(self):
        msg = 'React to this message with the emoji: 🎓'
        await ctx.send(msg)
    
    #Command to create new students from reaction
    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        class_1.addstudent(user.id)

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        class_1.classroom.addstudent(user.id)

  

    






# Cog setup
def setup(client):
    client.add_cog(classroom_cogs(client))