import discord
import requests
import json
import random
from replit import db

client = discord.Client()

sad_words = ['sad', 'depressed', 'lonely', 'alone', 'sorrow', 'kill', 'death', 'suicide', 'die', 'dying', 'tears', 'miss', 'missed', 'destruct', 'destructive', 'abusive', 'toxic person', 'triste', 'depressivo', 'sozinho', 'solitário', 'tristeza', 'matar', 'morte', 'suicidio', 'morrer', 'morrendo', 'lagrimas', 'choro', 'chorar', 'saudades', 'saudade', 'sentir falta', 'esquecido', 'destruir', 'destrutivo', 'destruido', 'abusivo', 'pessoa toxica', 'toxico', 'unhappy', 'infeliz', 'com raiva', 'angry', 'puto', 'miserable', 'miseravel', 'depressing']

starter_encourage = ['Aguente Firme!', 'Se Anime :D.', 'Fique feliz!', 'Você é uma pessoa muito legal.', 'você é Incrivel', 'Pratique esportes :D']

def get_quote():
  response = requests.get ("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -  " + json_data[0]['a']
  return(quote)

def update_encourage(encourage_message):
  if 'encourage' in db.keys():
    encourage = db["encourage"]
    encourage.append(encourage_message)
    db["encourage"] = encourage
  else:
    db["encourage"] = [encourage_message]

def delete_encourage(index):
  encourage = db["encourage"]
  if len(encourage) > index:
    del encourage[index]
    db["encourage"] = encourage

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message): 
  if message.author == client.user:
    return

  msg = message.content
  
  if message.content.startswith("$cite"):
    quote = get_quote()
    await message.channel.send(quote)

  options = starter_encourage
  if encourage in db.keys():
    options = options + db["encourage"]

  if any(word in msg for word in sad_words): 
    await message.channel.send(random.choice(options))

  if msg.startwith('$adicionar'):
    encourage_message = msg.split("$adiciona ", 1)[1]
    update_encourage(encourage_message)
    await message.channel.send("Nova Frase Adicionada :D")

  if msg.startwith('$deletar'):
    encourage = []
    if "encourage" in db.keys():
      index = int(msg.split("$deletar", 1)[1])
      delete_encourage(index)
      encourage = db("encourage")
    await message.channel.send("Frase Deletada")
    


client.run('OTg5MjkwMTk3NjgwMjYzMTY4.GTb5gf.baJ_NRLO8rNhGg9YT1P__OytZiZD6ncBvGRFqI')
# Essa linha usa a biblioteca do discord e inicia o Bot por meio do TOKEN identificador adicionado