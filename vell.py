#Vell Bot v0.1
import discord 
import os
from discord.ext import commands
client = discord.Client()
#-----------------------------#
bot = commands.Bot(command_prefix='v.', description='General-purpose bot in beta phase for INV platform.')
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
async def devs():
    await bot.say("Current Developers are: Alphi | Asher")
@bot.command()
async def meme():
    await bot.say("Please choose a number from 1-4")
   
@bot.event
async def on_message(message, timeout=10,):
    if message.content.startswith('ms'):
        await my_bot.send_message(message.channel, 'Music Streaming isn\'t available just yet, sorry!', tts=True)
        msg = await my_bot.wait_for_message(author=message.author, content='Hellooo')
        await my_bot.send_message(message.channel, 'Hello.')
       
        
        
token = os.environ.get("TOKEN")
bot.run(f'{token}')
#bot link https://discordapp.com/oauth2/authorize?client_id=397217109035450368&scope=bot&permissions=0
