import discord
import asyncio
from discord.ext import commands, tasks

class Lecture(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.channel = None
        self.lecDict = []


    #def setChannel(self, channel):
       # self.channel = channel


    # Adds lectures to dictionary :)
    @commands.command()
    async def addLec(self, ctx, *, params):
        paramList = params.split('@')
        lecNum = paramList[0]
        lecName = paramList[1]
        link = paramList[2]
        #fileType = paramList[3]
        desc = paramList[4]
        #stuff = [lecNum,lecName,link,fileType]
        
        lecTitle = "Lec #%s: %s" %(lecNum,lecName)
        Lembed = discord.Embed(title = lecTitle, url = link, description = desc, color = discord.Color.blue())

        self.lecDict.append(Lembed)

    # Print out all lectures
    @commands.command()
    async def allLecs(self, ctx):
        buttons = [u"\u23EA", u"\u2B05", u"\u27A1", u"\u23E9"] # skip to start, left, right, skip to end
        current = 0
        msg = await ctx.send(embed=self.lecDict[current])
    
        for button in buttons:
            await msg.add_reaction(button)
        
        while True:
            try:
                reaction, user = await self.client.wait_for("reaction_add", check=lambda reaction, user: user == ctx.author and reaction.emoji in buttons, timeout = 300.0)

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
                    if current < len(self.lecDict)-1:
                        current += 1

                elif reaction.emoji == u"\u23E9":
                    current = len(self.lecDict)-1

                for button in buttons:
                    await msg.remove_reaction(button, ctx.author)

                if current != previous_page:
                    await msg.edit(embed=self.lecDict[current])

    # Command to retrieve a specified lecture
    @commands.command()
    async def getLec(self, ctx, *, params):
        paramList = params.split('@')
        lecNum = paramList[0]

        for x in range(len(self.lecDict)):
            if((x+1) == int(lecNum)):
                await ctx.send(embed = self.lecDict[x])

# Cog setup
def setup(client):
    client.add_cog(Lecture(client))