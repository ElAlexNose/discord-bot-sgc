import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # Comando para decir la IP del servidor "test"
    if message.content.startswith('!ip'):
        await message.channel.send("ip server 'test'")

client.run(os.getenv('TOKEN'))
