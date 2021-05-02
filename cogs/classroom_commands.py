# Discord.py, Discord.ext, and Classroom class imports
import discord
from discord.ext import commands
from classroom import *

class classroom_cogs(commands.Cog):

    # Constructor to initialize the client attribute
    def __init__(self, client):
        self.client = client
    
    # Command to create a new classroom
    @commands.command()
    async def create_classroom(self, ctx, name):
        self.classroom = Classroom(name, ctx.author)

        # Create the appropriate category and rols, and set permissions for the category
        self.category = await ctx.guild.create_category(name)
        self.role = await ctx.guild.create_role(name = 'Student')
        await self.category.set_permissions(self.role, read_messages=True, send_messages=False)
        await self.category.set_permissions(ctx.guild.default_role, read_messages=False, send_messages=False)
        
        # Create an overwrites dictionary to contain the permission overwrites for various roles
        overwrites = {
            self.role: discord.PermissionOverwrite(read_messages = True, send_messages = True),
            ctx.guild.default_role: discord.PermissionOverwrite(read_messages = False, send_messages = False)
        }

        # Create appropriate text channels and save them as local attributes so they can be accessed if required
        self.commandsChannel = await ctx.guild.create_text_channel('commands')
        self.welcomeChannel = await ctx.guild.create_text_channel('welcome', category = self.category)
        self.announcementsChannel = await ctx.guild.create_text_channel('announcements', category = self.category)
        self.discussionsChannel = await ctx.guild.create_text_channel('discussions', overwrites = overwrites, category = self.category)
        self.resourcesChannel = await ctx.guild.create_text_channel('resources', overwrites = overwrites, category = self.category)
        self.help_teacherChannel = await ctx.guild.create_text_channel('help_teacher', overwrites = overwrites, category = self.category)
        self.help_classChannel = await ctx.guild.create_text_channel('help_classmates', overwrites = overwrites, category = self.category)

        # Create appropriate voice channels and save them as local attributes so they can be accessed if required
        self.lecture_hallChannel = await ctx.guild.create_voice_channel("lecture hall", category=self.category)
        self.study_call1Channel = await ctx.guild.create_voice_channel("study call 1", category=self.category, user_limit=5)
        self.study_call1Channe2 = await ctx.guild.create_voice_channel("study call 2", category=self.category, user_limit=5)
        self.study_call1Channe3 = await ctx.guild.create_voice_channel("study call 3", category=self.category, user_limit=5)
        self.study_call1Channe4 = await ctx.guild.create_voice_channel("study call 4", category=self.category, user_limit=5)
        self.study_call1Channe5 = await ctx.guild.create_voice_channel("study call 5", category=self.category, user_limit=5)
        self.study_call1Channe6 = await ctx.guild.create_voice_channel("study call 6", category=self.category, user_limit=5)

        # Set the channel for the announcements cog to the announcements channel just made
        self.client.get_cog('Announcements').channel = self.announcementsChannel

        # Delete the $create_classroom <name> line from the channel the command was invoked in
        await ctx.channel.purge(limit = 1)

        # Send appropriate messages to the various channels
        await self.welcomeChannel.send(f'Welcome everyone to {name} class, taught by {ctx.author}')
        await self.commandsChannel.send(f'{name} class created. You\'re now the teacher {ctx.author.mention}')
        await self.commandsChannel.send('Use the commands channel for all Classroom bot commands')

    # Create a cog listener for the on_member_join event to add new students to the class list
    @commands.Cog.listener()
    async def on_member_join(self, member):
        self.classroom.addstudent(member.id)
        await member.add_roles(self.role)
        await self.welcomeChannel.send(f'{member.name} has joined the {self.classroom.name} class as a student')
    
# Cog setup
def setup(client):
    client.add_cog(classroom_cogs(client))