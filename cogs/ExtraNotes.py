import discord
import asyncio
from discord.ext import commands, tasks
from Helper import *

class Notes(commands.Cog):

    # Constructor for lecture cog to keep track of the client, as well as a list for lectures
    def __init__(self, client):
        self.client = client
        self.channel = None
        self.noteList = []


    # Adds notes to the list
    @commands.command()
    async def addNote(self, ctx, *, params):
        paramList = parse_inputs(params)
        noteNum = paramList[0]
        noteName = paramList[1]
        link = paramList[2]
        #fileType = paramList[3]
        desc = paramList[4]

        # Create a Discord embed and save it to the list of notes
        noteTitle = "Note #%s: %s" %(noteNum,noteName)
        Nembed = discord.Embed(title = lecTitle, url = link, description = desc, color = discord.Color.blue())
        self.noteList.append(Lembed)

    # Print out all lectures
    @commands.command()
    async def allNotes(self, ctx):
        buttons = [u"\u23EA", u"\u2B05", u"\u27A1", u"\u23E9"] # skip to start, left, right, skip to end
        current = 0
        msg = await ctx.send(embed=self.noteList[current])
    
        for button in buttons:
            await msg.add_reaction(button)
        
        while True:
            try:
                reaction, user = await self.client.wait_for("reaction_add", check=lambda reaction, user: user == ctx.author and reaction.emoji in buttons, timeout = 60.0)

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
                    if current < len(self.noteList)-1:
                        current += 1

                elif reaction.emoji == u"\u23E9":
                    current = len(self.noteList)-1

                for button in buttons:
                    await msg.remove_reaction(button, ctx.author)

                if current != previous_page:
                    await msg.edit(embed=self.noteList[current])

# Cog setup
def setup(client):
    client.add_cog(Notes(client))
    