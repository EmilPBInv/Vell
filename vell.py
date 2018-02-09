#Vell Bot v0.1  -------  Test rep, THIS IS NOT THE MAIN REP, IT IS PRIVATE!
import discord 
import os
from discord.ext import commands
client = discord.Client()
from datetime import datetime
now = datetime.now()
str(now.month) + "/" +str(now.day) + "/" + str(now.year) + "/"
#-----------------------------#
bot = commands.Bot(command_prefix=['v.', 'join.'], description='General-purpose bot in beta phase for INV platform.')
@bot.event
async def bot_online():
    print('Bot: ')
    print(bot.user.name)
@bot.command()
async def karmaguild():
    await bot.say("Karma Recruitment Center Invite Link: <https://discord.gg/BYc3Der>")
@bot.command()
async def beta():
    await bot.say("Beta phase, what else?!")
@bot.command()
async def supportserver():
    await bot.say("https://discord.gg/pMXFPbM")

@bot.command()
async def date():
    await bot.say(now)

@client.event
async def on_message(message):
    if message.content.startswith('!embedd'):
        embed = discord.Embed(title="Tile", description="Desc", color=0x00ff00)
        embed.add_field(name="Alphi", value="hi", inline=False)
        embed.add_field(name="Asher", value="hi2", inline=False)
        await client.send_message(message.channel, embed=embed)    
    
@bot.command()
async def git():
    await bot.say("https://github.com/ " + "jdcoding01")
    
    
token = os.environ.get("TOKEN")
bot.run(f'{token}')
#bot link https://discordapp.com/oauth2/authorize?client_id=397217109035450368&scope=bot&permissions=0
