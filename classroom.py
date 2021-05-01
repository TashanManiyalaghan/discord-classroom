import os
import discord
from discord.ext import commands
from discord import member

# client = commands.Bot(comman_prefix='$')

# @client.event
# async def on_ready():
#     print("ClassroomBot is initialized")

class Classroom:
    """
    A classroom class that stores information about class, teachers, and students
    """

    def __init__(self, classroom_name, teacher):
        """
        Creates a Classroom object using the classroom name and class teacher
        """
        self.name = classroom_name
        self.teacher = teacher
        self.classlist = []
    
    def __str__(self):
        """
        Generate a string representation of the Classroom object
        """
        return (self.name + 'class will be taught by' + self.teacher)

    def addstudent(self, discord_user_id):
        """
        Create a Student attribute using discord user id
        """
        self.discord_user_id = discord_user_id
        self.classlist.append(self.discord_user_id)


# @client.command(message)
# async def classroom(ctx):
#     if ctx.message.author.guild_permissions.administrator:
#         class_room = classroom(message, ctx.message.author.id)
#         msg = print(class_room).format(ctx.message.author.mention)
#         await ctx.send(msg)

# @client.command()
# async def student(ctx):
#     if ctx.message.author.guild_permissions.administrator:
#         msg = "You are already a Teacher {}".format(ctx.message.author.mention)
#         await ctx.send(msg)
#     else:
#         stu = Classroom.student(ctx.message.author.id)
#         msg = "You're now a Student {}".format(ctx.message.author.mention)
#         await ctx.send(msg)


