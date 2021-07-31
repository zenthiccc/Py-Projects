import discord
import random
import os
from key import BOT
from discord.ext import commands

client = commands.Bot(command_prefix=">")


#Commands
@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    await ctx.send('loading commands')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    await ctx.send('unloading commands')
  
@client.command()
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')
    await ctx.send('reloading commands')
  
#Scan thru files in cogs folder and load them
for filename in os.listdir('discord-bot\cogs'):
      if filename.endswith('.py'):
            client.load_extension(f'cogs.{filename[:-3]}')


client.run(BOT.key)
