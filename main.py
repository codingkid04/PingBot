import os
import discord

from dotenv import load_dotenv
from discord.ext import commands
intents=discord.Intents.all()

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = commands.Bot(command_prefix='.',intents=intents)

@client.event
async def on_ready():
    print('PingBot is ready to roll!')


@client.command()
async def ping(ctx):
    await ctx.send('Pong!')


@client.command()
async def say(ctx, arg):
	await ctx.channel.send(arg)

#@client.event
#async def on_member_join(member):
#    await member.send(f"Hey {member.name}, welcome to the **CAPSOC Discord Server!** Here you can find all kinds of stuff, but before you do anything, please take time to look into our **Rules** channel and get familiar with it. If you have any questions or concerns, please contact the moderators of this sever!")

#@client.command()
#@commands.has_permissions(administrator=True) # Making sure the person executing the command has the permissions
#async def foo(ctx):
#	await ctx.send("Hello")

@client.event
async def on_member_join(member):
    embed = discord.Embed(title="Welcome to the CAPSOC Server!", description="Here you can find all kinds of stuff, but before you do anything, please take time to look into our **Rules** channel and get familiar with it. If you have any questions or concerns, please contact the moderators of this sever!", color=0x42f5e3)
    embed.set_thumbnail(url="https://cdn-images-1.medium.com/max/650/1*xrx4PIQvza23h7SorC4MnA.gif")
    await member.send(embed=embed)

@client.command()
async def message(ctx, user:discord.Member, *, message=None):
    embed = discord.Embed(title="Welcome to the CAPSOC Server!", description="Here you can find all kinds of stuff, but before you do anything, please take time to look into our **Rules** channel and get familiar with it. If you have any questions or concerns, please contact the moderators of this sever!", color=0x42f5e3)
    embed.set_thumbnail(url="https://cdn-images-1.medium.com/max/650/1*xrx4PIQvza23h7SorC4MnA.gif")
    await user.send(embed=embed)


@client.command()
async def embed(ctx):
    embed=discord.Embed(title="Welcome to the CAPSOC Server!", description="Here you can find all kinds of stuff, but before you do anything, please take time to look into our **Rules** channel and get familiar with it. If you have any questions or concerns, please contact the moderators of this sever!", color=0x42f5e3)
    embed.set_thumbnail(url="https://cdn-images-1.medium.com/max/650/1*xrx4PIQvza23h7SorC4MnA.gif")
    await ctx.send(embed=embed)


client.run(TOKEN)