# This example requires the 'message_content' intent.

import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    try:
        channel_name = message.channel.name
    except AttributeError:
        channel_name = None

    print(F'Message received in {channel_name} from {message.author.name}')

    if message.author == client.user:
        return

    if channel_name == 'papagei':
        await message.channel.send(message.content)

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
        return


client.run('YOUR BOT TOKEN HERE')
