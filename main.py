import random
import os
import discord
from discord.ext import commands

def dados(quantidade):
    vitorias = 0
    controles = 0
    nada = 0
    entropias = 0
    for i in range(quantidade):
        dado = random.randint(1,6)
        match dado:
            case 1:
                entropias = entropias + 1
            case 2 | 3:
                nada = nada +1
            case 4 | 5 :
                controles = controles + 1
            case 6 :
                vitorias = vitorias + 1
            case _ :
                return
    
    return f'Vitórias: {vitorias} \nControles: {controles} \nNada: {nada} \nEntropias: {entropias}' 
    
    


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

    if message.content.startswith('*d'):
        await message.channel.send(dados(int(message.content[2:])))


token = os.environ['TOKEN']
client.run(token)

'''
implementar função de reroll. Input? Criar dicionário com os valores do resultado?
def reroll(resultado):
  match resultado:
    case "Vitórias":
'''
  
