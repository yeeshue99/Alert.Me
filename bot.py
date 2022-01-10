import discord
from settings import *

client = discord.Client()


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("amFriend"):
        await message.channel.send("Hello!")


client.run(DISCORD_TOKEN)
