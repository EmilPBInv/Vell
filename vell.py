#Vell Bot v0.1
import discord 
import os
from discord.ext import commands
client = discord.Client()
#-----------------------------#
bot = commands.Bot(command_prefix='v.' or '.join', description='General-purpose bot in beta phase for INV platform.')
@bot.event
async def bot_online():
    print('Bot: ')
    print(bot.user.name)
@bot.command()
async def link():
    await bot.say("Karma Recruitment Center Invite Link: <https://discord.gg/BYc3Der>")
@bot.command()
async def beta():
    await bot.say("Beta phase, what else?!")
@bot.command()
async def supportserver():
   await bot.say("https://discord.gg/pMXFPbM")


token = os.environ.get("TOKEN")
bot.run(f'{token}')
#bot link https://discordapp.com/oauth2/authorize?client_id=397217109035450368&scope=bot&permissions=0
