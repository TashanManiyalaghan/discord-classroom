# Discord.py and Discord.ext imports
import discord
from discord.ext import commands
from classroom import *

# .env setup
import os
from dotenv import load_dotenv
project_folder = os.path.expanduser('./')
load_dotenv(os.path.join(project_folder, '.env'))

client = commands.Bot(command_prefix = '$')

# on_ready event, for when the bot logs onto server
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.command()
async def create_classroom(ctx, name):
    classroom = Classroom(name, ctx.author.id)
    category = await ctx.guild.create_category(name)
    announcementsChannel = await ctx.guild.create_text_channel('announcements', category = category)
    client.get_cog('Announcements').channel = announcementsChannel

# load command for loading the cog with the provided extension
@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f'Loaded \'{extension}\' cog')

# unload command for unloading the cog with the provided extension
@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    await ctx.send(f'Unloaded \'{extension}\' cog')

# reload command for reloading the cog with the provided extension
@client.command()
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f'Reloaded \'{extension}\' cog')

# Load all cogs in the specified directory
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        # Load only .py cogs and strip the extension
        client.load_extension(f'cogs.{filename[:-3]}')


client.run(os.getenv('TOKEN'))