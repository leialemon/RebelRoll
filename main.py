import discord
from discord.ext import commands
import os
from funcoes import dados


intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

bot = commands.Bot(command_prefix='$', intents=intents)
@bot.command()
async def roll(ctx, quantidade):
  await ctx.send(f'rolar {quantidade} dados')
      
      
token = os.environ['TOKEN']
client.run(token)