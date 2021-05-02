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
        self.role = await ctx.guild.create_role(name = 'Student')
        await category.set_permissions(self.role, read_messages=True, send_messages=False)
        await category.set_permissions(ctx.guild.default_role, read_messages=False, send_messages=False)

        #create messages for respective channels
        msg=name + " class created. You're now the teacher {}".format(ctx.author.mention)
        other_msg = "Use the commands channel for all Classroom bot commands"
        
        #overwrite the permissions
        overwrites = {self.role:discord.PermissionOverwrite(read_messages=True, send_messages=True),
        ctx.guild.default_role: discord.PermissionOverwrite(read_messages=False, send_messages=False)
        }

        #create text channels
        self.welcomeChannel = await ctx.guild.create_text_channel('welcome', category = category)
        self.announcementsChannel = await ctx.guild.create_text_channel('announcements', category = category)
        self.client.get_cog('Announcements').channel = self.announcementsChannel
        self.discussionsChannel = await ctx.guild.create_text_channel('discussions', overwrites=overwrites, category = category)
        self.resourcesChannel = await ctx.guild.create_text_channel('resources', overwrites=overwrites, category = category)
        self.commandsChannel = await ctx.guild.create_text_channel('commands')
        self.help_teacherChannel = await ctx.guild.create_text_channel('help_teacher', overwrites=overwrites, category = category)
        self.help_classChannel = await ctx.guild.create_text_channel('help_class', overwrites=overwrites, category = category)

        #delete call line from repective text channel
        await ctx.channel.purge(limit = 1)

        #send messages to respective channels
        await self.commandsChannel.send(msg)
        await self.commandsChannel.send(other_msg)

    # Use addstudent method to assign new memebers to class list
    @commands.Cog.listener()
    async def on_member_join(self, member):
        self.class_1.addstudent(member.id)
        msg = member.name + ' has joined the ' + self.class_1.name + ' class as a student'
        await member.add_roles(self.role)
        await self.welcomeChannel.send(msg)
    
    
# Cog setup
def setup(client):
    client.add_cog(classroom_cogs(client))