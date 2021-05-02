import discord
from discord.ext import commands

class Classroom:
    """
    A classroom class that stores information about class, teachers, and students
    """

    def __init__(self, classroom_name, teacher):
        """
        Creates a Classroom object using the classroom name and class teacher
        """
        self.name = classroom_name
        self.teacher_name = teacher
        self.teacher_id = teacher.id
        self.classlist = []
    
    def __str__(self):
        """
        Generate a string representation of the Classroom object
        """
        return f'{str(self.name)} class will be taught by {str(self.teacher_name)}'

    def addstudent(self, discord_user_id):
        """
        Create a Student attribute using discord user id
        """
        self.classlist.append(discord_user_id)