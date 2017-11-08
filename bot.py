##--------------------------##
##Developed By Jose Barranco##
##Github: //jdcoding01\\
##Bot name\\ Guardian  //
##--------------------------##
import discord as disc
from discord.ext import commands
#-----------------------------#
bot = commands.Bot(command_prefix='&', description='Multi-purpose bot for the Sacred Scarlets guild.')
@bot.event
async def bot_online():
    print('Bot: ')
    print(bot.user.name)
@bot.command()
#Greet command: the bot welcomes a new user that has joined the guild.
async def hello():
    await bot.say("Welcome to Sacred Scarlets!")

@bot.command()
async def Lukas():
    await bot.say("Mi nombre es Lukas")
@bot.command()
async def server():
    await bot.say("Este servidor 'HGEsports' fue creado por @Lukas")

bot.run('Mzc3ODk5MzEwNTY3Nzg0NDYw.DOTptw.MLDHfxr-khaPL8SwNXb4D4gzuLI')

#discord bot 
