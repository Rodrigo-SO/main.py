import discord #Importa a biblioteca no discord
#---------------------------------------



client = discord.Client()
#Importa a função Client() da biblioteca discord
#Coloca a função Client() dentro da Variável "client"
#---------------------------------------





@client.event
#Usando a variável "client" criada para registrar um evento
async def on_ready():
  print('Bot [{0.user}] startado com sucesso!'.format(client))
#Evento criado para mostrar uma mensagem caso tudo tenha ocorrido corretamente. 
# O {0.user}.format(client) irá pegar a váriavel client subistiturindo o valor "0" antes de user
#---------------------------------------





  
@client.event
#Outro evento criado para iniciar assim que o bot estiver pronto e funcionando
async def on_message(message):
#O evento recebe um argumento 'mesagem'
#Os nomes das funções são especificas da biblioteca do discord
  if message.author == client.user:
    return
#Condição para o bot não fazer nada caso a mensagem venha o usuário do bot

  if message.content.startswith('$hello'):
    await message.channel.send('Hello!')
#Condição, SE o conteúdo da mensagem iniciar com "$hello", Envie uma mensagem para o canal dizendo "Hello!"
#---------------------------------------
    
client.run('OTg5MjkwMTk3NjgwMjYzMTY4.GcdxV7.u-XapoFk4GPq2UYcYOp7cDiHQKtziDS6H9zo6U')
#Essa linha conecta ao Bot utilizando o TOKEN de identificação dele
#---------------------------------------
