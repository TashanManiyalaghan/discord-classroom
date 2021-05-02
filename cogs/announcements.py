import discord
from discord.ext import commands, tasks
from schedule import *
from Helper import *

class Announcements(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.schedule = Schedule()
        self.channel = None
        # Begin the tasks.loop for ping_event command when the cog is loaded.
        self.ping_event.start()

    # Disable the tasks.loop for ping_event command when the cog is unloaded.
    def cog_unload(self):
        self.ping_event.cancel()

    def setChannel(self, channel):
        self.channel = channel

    # Command to create a new event in the Schedule object.
    @commands.command()
    async def add_event(self, ctx, *, params):
        paramList = parse_inputs(params)
        name = paramList[0]
        date = [int(x) for x in paramList[1].split('/')]
        time = [int(x) for x in paramList[2].split(':')]
        desc = paramList[3]

        event = self.schedule.addEvent(name, date[0], date[1], date[2], time[0], time[1], desc)
        await ctx.send(f'The following event was created: \n\t{event}')

    # Command to display in the console the events of the Schedule object.
    @commands.command()
    async def view_schedule(self, ctx):
        await ctx.send(str(self.schedule))

    # Tasks loop that will refresh every minute and ping any events currently taking place.
    # NOTE: Pinging system for when an event is taking place is still required.
    @tasks.loop(seconds = 60)
    async def ping_event(self):
        if not (self.channel is None):
            currentEvents = self.schedule.checkCurrent()

            if len(currentEvents) > 0:
                await self.channel.send('@here The following event(s) are taking place right now:')
                for event in self.schedule.checkCurrent():
                    await self.channel.send(f'\t{event}')
                    self.schedule.removeEvent(event.name)

# Cog setup
def setup(client):
    client.add_cog(Announcements(client))