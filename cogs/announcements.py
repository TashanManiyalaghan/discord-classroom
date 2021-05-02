# Discord.py, Discord.ext, Schedule class, and helper function imports
import discord
from discord.ext import commands, tasks
from schedule import *
from Helper import *

class Announcements(commands.Cog):

    # Cog constructor to define necessary attributes, as well as start the tasks.loop needed for timed updates
    def __init__(self, client):
        self.client = client
        self.schedule = Schedule()
        self.channel = None
        # Begin the tasks.loop for ping_event command when the cog is loaded
        self.ping_event.start()

    # Disable the tasks.loop for ping_event command when the cog is unloaded
    def cog_unload(self):
        self.ping_event.cancel()

    # Function that can set the channel for announcements to be made in
    def setChannel(self, channel):
        self.channel = channel

    # Command to create a new event in the Schedule object.
    @commands.command()
    async def add_event(self, ctx, *, params):
        paramList = parse_inputs(params)
        name = paramList[0]
        desc = paramList[1]
        date = [int(x) for x in paramList[2].split('/')]
        time = [int(x) for x in paramList[3].split(':')]

        event = self.schedule.addEvent(name, desc, date[0], date[1], date[2], time[0], time[1])
        await ctx.send(f'The following event was created: \n\t{event}')

    # Command to display in the console the events of the Schedule object.
    @commands.command()
    async def view_schedule(self, ctx):
        await ctx.send(str(self.schedule))

    # Tasks loop that will refresh every minute and ping any events currently taking place.
    @tasks.loop(seconds = 60)
    async def ping_event(self):
        if not (self.channel is None):
            currentEvents = self.schedule.checkCurrent()
            # Appropriately format the output to display each event
            if len(currentEvents) > 0:
                string = '@here The following event(s) are taking place right now:'
                for event in self.schedule.checkCurrent():
                    string = f'{string}\n\t{event}'
                    self.schedule.removeEvent(event.name)
                await self.channel.send(string)

# Cog setup
def setup(client):
    client.add_cog(Announcements(client))