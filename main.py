import os
import discord

from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = commands.Bot(command_prefix='.')

@client.event
async def on_ready():
    print('PingBot is ready to roll!')


@client.command()
async def ping(ctx):
    await ctx.send('Pong!')

@client.command()
async def message(ctx, user:discord.Member, *, message=None):
    message = "Welcome to the Server!"
    embed = discord.Embed(title=message)
    await user.send(embed=embed)

client.run(TOKEN)