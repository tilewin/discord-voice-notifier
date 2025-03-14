import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
CHANNEL = os.getenv('CHANNEL')
TOKEN =  os.getenv('TOKEN')

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_voice_state_update(member, before, after):
    channel = client.get_channel(CHANNEL)
    if before.channel is not None:
        return

    await channel.send(member.name)

client.run(TOKEN)
