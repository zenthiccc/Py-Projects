import discord
import random
import os
import time
from discord.ext import commands, tasks
from itertools import cycle

status = cycle(['Cyperbunk 2077', 'Rocket League', 'SpeedRunners', 'Grand Theft Auto V'])
class Commands(commands.Cog):

    def __init__(self, client):
        self.client=client
    
    #Events
    @commands.Cog.listener()
    async def on_ready(self):
        self.change_status.start()
        await self.client.change_presence(status=discord.Status.do_not_disturb)
        print("Bot is running")
    
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.send('Command does not exist.')
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Please input the required argument')
    
    #Tasks
    @tasks.loop(seconds=600)
    async def change_status(self):
        await self.client.change_presence(activity=discord.Game(next(status)))
        
    #Commands 
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'{round(self.client.latency * 1000)}ms')

    @commands.command()
    async def clear(self, ctx, amount, times):
        times = int(times)
        amount = int(amount)
        while times:
            await ctx.channel.purge(limit=amount)
            time.sleep(2)
            times-=1
    
    @commands.command(aliases=["8ball"])
    async def _8ball(self, ctx, *, question):
        responses = ["It is certain.",
                 "It is decidedly so.",
                "Without a doubt.",
                  "Yes - definitely.",
                     "You may rely on it.",
                      "As I see it, yes.",
                    "Most likely.",
                    "Outlook good.",
               "Signs point to yes.",
              "Reply hazy, try again.",
           "Ask again later.",
                "Better not tell you now.",
             "Cannot predict now.",
               "Concentrate and ask again.",
              "Don't count on it.",
                 "My reply is no.",
               "My sources say no.",
            "Outlook not so good.",
             "Very doubtful."]
        await ctx.send(f"Question: {question}\nAnswer: {random.choice(responses)}")
        

def setup(client):
    client.add_cog(Commands(client))