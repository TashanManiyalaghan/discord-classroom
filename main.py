# Discord.py and Discord.ext imports
import discord
from discord.ext import commands

# .env setup
import os
from dotenv import load_dotenv
project_folder = os.path.expanduser('./')
load_dotenv(os.path.join(project_folder, '.env'))

client = commands.Bot(command_prefix = '$')

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

# Generic Discord command
@client.command(aliases = ['hi', 'hey', 'hello'])
async def hello(ctx):
    await ctx.send(f'Hello!')

client.run(os.getenv('TOKEN'))