import os
import time
import json
import urllib
# import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD = os.getenv("DISCORD_GUILD")

# client = discord.Client()
bot = commands.Bot(command_prefix="!")


@bot.event
async def on_ready():
    print(f"{bot.user.name} has entered the room!")
    print(time.ctime())
    print("\n")

    # if not os.path.exists('./emotes'):
    #     os.makedirs('./emotes')
    # print('Saving emotes to folder: ' + os.path.abspath('./emotes') + '...')
    # print('Grabbing emote list...')
    # twitch_emotes = json.load(urllib.request.urlopen('https://api.twitchemotes.com/api/v4/emotes'))
    # for code, emote in twitch_emotes["emotes"].items():
    #     print(f"Downloading {code}...")
    #     urllib.urlretrieve('http:' + twitch_emotes['template']['large'].replace('{image_id}',
    #         str(emote['image_id'])), './emotes/' + code + '.png')
    # print("Done downloading emotes!")

    print("\n")


@bot.event
async def on_command_error(ctx, error):
    if ctx.command.name == "channelname":
        print("!channelname: Missing channel name")
        await ctx.send("You need a name for the channel!")
        async for message in ctx.channel.history(limit=5):
            if message.author == bot.user:
                break
        time.sleep(5)
        await ctx.message.delete()
        await message.delete()

    if ctx.command.name == "servername":
        print("!servername: Sending current server name")
        await ctx.send(f"The current server name is **{ctx.guild.name}**")
        async for message in ctx.channel.history(limit=5):
            if message.author == bot.user:
                break
        time.sleep(5)
        await ctx.message.delete()
        await message.delete()


@bot.command(name="channelname", help="Changes channel name.")
async def _changeChannelName(ctx, newname, check=None):
    if ctx.message.author == bot.user:
        return

    if check != None:
        await ctx.send("You need to replace spaces with underscores! ( _ )")
        async for message in ctx.channel.history(limit=5):
            if message.author == bot.user:
                break
        time.sleep(5)
        await ctx.message.delete()
        await message.delete()
        return

    else:
        await ctx.channel.edit(name=newname)
        await ctx.message.delete()
        time.sleep(1)
        await ctx.send(f"**{ctx.author.display_name}** changed the channel name: **{ctx.channel.name}**")


@bot.command(name="servername", help="Changes the server name")
async def _changeServerName(ctx, *, arg):
    if ctx.message.author == bot.user:
        return

    else:
        await ctx.guild.edit(name=arg)
        await ctx.message.delete()
        time.sleep(1)
        await ctx.send(f"**{ctx.author.display_name}** changed the server name: **{ctx.guild.name}**")


@bot.command(name="shutdown", help="Shuts down the bot.")
async def _shutdown(ctx):
    if ctx.message.author == bot.user:
        return

    await ctx.send("Aww... You don't want me pampering you anymore?")
    async for message in ctx.channel.history(limit=5):
        if message.author == bot.user:
            break
    time.sleep(2)
    await ctx.message.delete()
    await message.delete()
    await bot.logout()

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return



# @bot.event
# async def on_guild_channel_update(before, after):
    # bot.
    # await after.send(f"The channel name has been changed to: {after.name}.")

bot.run(TOKEN)
