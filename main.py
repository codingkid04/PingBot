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

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hey {member.name}, welcome to the **CAPSOC Discord Server!** Here you can find all kinds of stuff, but before you do anything, please take time to look into our **Rules** channel and get familiar with it. If you have any questions or concerns, please contact the moderators of this sever!'
    )

@client.command()
async def ping(ctx):
    await ctx.send('Pong!')

@client.command()
async def message(ctx, user:discord.Member, *, message=None):
    message = "Welcome to the Server!"
    embed = discord.Embed(title=message)
    await user.send(embed=embed)

client.run(TOKEN)