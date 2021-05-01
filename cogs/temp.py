import discord
from discord.ext import commands, tasks
from schedule import *

class Temp(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.schedule = Schedule()
        self.ping_event.start()

    def cog_unload(self):
        self.ping_event.cancel()

    # Basic Discord command
    @commands.command(aliases = ['hi', 'hey'])
    async def hello(self, ctx):
        await ctx.send('Hello')

    @commands.command()
    async def add_event(self, ctx):
        self.schedule.addEvent('Testing', 2021, 5, 1, 14, 5, 'This is a test')

    @commands.command()
    async def check_events(self, ctx):
        print(self.schedule)

    @tasks.loop(seconds = 60)
    async def ping_event(self):
        for event in self.schedule.checkCurrent():
            print(event)
            self.schedule.removeEvent(event.name)

# Cog setup
def setup(client):
    client.add_cog(Temp(client))