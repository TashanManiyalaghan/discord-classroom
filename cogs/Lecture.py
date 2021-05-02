import discord
import asyncio
from discord.ext import commands
from Helper import *

class Lecture(commands.Cog):

    # Constructor for lecture cog to keep track of the client, as well as a list for lectures
    def __init__(self, client):
        self.client = client
        self.lecList = []

    # Adds lectures to the list
    @commands.command()
    async def addLec(self, ctx, *, params):
        paramList = parse_inputs(params)
        lecNum = paramList[0]
        lecName = paramList[1]
        link = paramList[2]
        #fileType = paramList[3]
        desc = paramList[4]
        
        # Create a Discord embed and save it to the list of lectures
        lecTitle = f'Lecture #{lecNum}: {lecName}'
        Lembed = discord.Embed(title = lecTitle, url = link, description = desc, color = discord.Color.blue())
        self.lecList.append(Lembed)

    # Display all lectures by using embeds and reaction arrows to navigate
    @commands.command()
    async def allLecs(self, ctx):
        buttons = [u"\u23EA", u"\u2B05", u"\u27A1", u"\u23E9"] # skip to start, left, right, skip to end
        current = 0
        msg = await ctx.send(embed = self.lecList[current])
    
        for button in buttons:
            await msg.add_reaction(button)
        
        while True:
            try:
                reaction, user = await self.client.wait_for("reaction_add", check = lambda reaction, user: user == ctx.author and reaction.emoji in buttons, timeout = 60.0)
            except asyncio.TimeoutError:
                return print("test")
            else:
                previous_page = current
                if reaction.emoji == u"\u23EA":
                    current = 0
                elif reaction.emoji == u"\u2B05":
                    if current > 0:
                        current -= 1
                elif reaction.emoji == u"\u27A1":
                    if current < len(self.lecList) - 1:
                        current += 1
                elif reaction.emoji == u"\u23E9":
                    current = len(self.lecList) - 1

                for button in buttons:
                    await msg.remove_reaction(button, ctx.author)

                if current != previous_page:
                    await msg.edit(embed = self.lecList[current])

    # Command to retrieve a specified lecture
    @commands.command()
    async def getLec(self, ctx, lecNum):
        for x in range(len(self.lecList)):
            if ((x + 1) == int(lecNum)):
                #await ctx.send(embed = self.lecList[x])
                #await self.client.send(ctx.author, embed = self.lecList[x])
                await ctx.author.send(embed = self.lecList[x])
        await ctx.channel.purge(limit = 1)

# Cog setup
def setup(client):
    client.add_cog(Lecture(client))