# This example requires the 'message_content' intent.

import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
FUNNY_MESSAGE = 'Polly wants a cracker... and better Wi-Fi! 🦜'


async def send_reply(channel, content):
    await channel.send(f'{content}\n\n{FUNNY_MESSAGE}')


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
        await send_reply(message.channel, message.content)

    if message.content.startswith('$hello'):
        await send_reply(message.channel, 'Hello!')
        return


client.run('YOUR BOT TOKEN HERE')
