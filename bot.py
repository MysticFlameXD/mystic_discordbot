# bot.py
import os
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD = os.getenv("DISCORD_GUILD")

client = discord.Client()


@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(f"{client.user} has entered the room! ({guild.name})")

    members = "\n - ".join([member.name for member in guild.members])
    print(f"Guild Members:\n - {members}")


@client.event
async def on_member_join(member):
    await member.create.dm()
    await member.dm_channel.send(
        f"Ara ara~? {member.name} also wants some pampering?"
    )


@client.event
async def on_guild_channel_update(before, after):
    await after.send(f"The channel name has been changed to: {after.name}.")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == "!channelname":
        print(f"\nSomeone tried to change the channel name!")

client.run(TOKEN)
