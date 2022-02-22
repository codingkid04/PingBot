import os
import discord
import youtube_dl
import asyncio
import ffmpeg
from  discord import FFmpegPCMAudio

from dotenv import load_dotenv
from discord.ext import commands
intents=discord.Intents.all()

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='.',intents=intents)

youtube_dl.utils.bug_reports_message = lambda: ''

ytdl_format_options = {
    'format': 'bestaudio/best',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0' # bind to ipv4 since ipv6 addresses cause issues sometimes
}

ffmpeg_options = {
    'options': '-vn'
}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)

class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)
        self.data = data
        self.title = data.get('title')
        self.url = ""

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))
        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]
        filename = data['title'] if stream else ytdl.prepare_filename(data)
        return filename


#On Ready Event
@bot.event
async def on_ready():
    print('PingBot is ready to roll!')

#Ping Command
@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

#Say Command
@bot.command()
async def say(ctx, *, text):
    message = ctx.message
    await message.delete()

    await ctx.send(f"{text}")

#Join Command
@bot.command(pass_context = True)
async def rickroll(ctx):
    message = ctx.message
    await message.delete()
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio("Rick_Roll.mp3")
        player = voice.play(source)

    else:
        await ctx.send("No")

#Leave Command
@bot.command(name='leave', help='To make the bot leave the voice channel')
async def leave(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_connected():
        await voice_client.disconnect()
    else:
        await ctx.send("The bot is not connected to a voice channel.")



@bot.event
async def on_member_join(member):
    embed = discord.Embed(title="Welcome to the CAPSOC Server!", description="Here you can find all kinds of stuff, but before you do anything, please take time to look into our **Rules** channel and get familiar with it. If you have any questions or concerns, please contact the moderators of this sever!", color=0x42f5e3)
    embed.set_author(name="CAPSOC Moderators", icon_url="https://pbs.twimg.com/profile_images/538868741455368192/m7HlFzv1_400x400.jpeg")
    embed.set_thumbnail(url="https://cdn-images-1.medium.com/max/650/1*xrx4PIQvza23h7SorC4MnA.gif")
    embed.set_footer(text="Necessaria vis est!")
    await member.send(embed=embed)

@bot.command()
async def message(ctx, user:discord.Member, *, message=None):
    message = ctx.message
    await message.delete()
    embed = discord.Embed(title="Welcome to the CAPSOC Server!", description="Here you can find all kinds of stuff, but before you do anything, please take time to look into our **Rules** channel and get familiar with it. If you have any questions or concerns, please contact the moderators of this sever!", color=0x42f5e3)
    embed.set_author(name="CAPSOC Moderators", icon_url="https://pbs.twimg.com/profile_images/538868741455368192/m7HlFzv1_400x400.jpeg")
    embed.set_thumbnail(url="https://cdn-images-1.medium.com/max/650/1*xrx4PIQvza23h7SorC4MnA.gif")
    embed.set_footer(text="Necessaria vis est!")
    await user.send(embed=embed)


#@bot.event
#async def on_member_join(member):
#    await member.send(f"Hey {member.name}, welcome to the **CAPSOC Discord Server!** Here you can find all kinds of stuff, but before you do anything, please take time to look into our **Rules** channel and get familiar with it. If you have any questions or concerns, please contact the moderators of this sever!")

#@bot.command()
#@commands.has_permissions(administrator=True) # Making sure the person executing the command has the permissions
#async def foo(ctx):
#	await ctx.send("Hello")

bot.run(TOKEN)