#Vell Bot v0.1  -------  Test rep, THIS IS NOT THE MAIN REP, IT IS PRIVATE!
import os
# CONFIG
# --------- #
prefix = ['v.', 'join.'] # This will be used at the start of commands.
embed_role = "Vell" # The role in your server used for embedding.
game = "Type v.help" # This will display as the game on Discord.
# ---------- #
from discord.ext import commands
from discord.ext.commands import Bot
import discord
global misc_commands
misc_commands = "In progress..."
bot = commands.Bot(command_prefix=prefix)
bot.remove_command("help")

@bot.event
async def on_ready():
    await bot.change_presence(game=discord.Game(name=game))

@bot.command(pass_context=True)
async def help(ctx):
    embed = discord.Embed(title="Vell Bot Help Menu", description="Here you will find all the help you need. Not satisfied? Type join.supportserver!", color=0x00a0ea)
    embed.add_field(name="{}embed".format("Miscellaneous Commands"), value=misc_commands)
    embed.add_field(name="{}rembed".format("Music Commands"), value="In progress...")
    embed.add_field(name="{}rembed".format("Command Help"), value="For info on a specific command type info-nameofthecommand")
    embed.set_footer(text="Vell Bot ~ Developed by Alphi#5113")
    await bot.say(embed=embed)
@bot.command(pass_context=True)
async def beta(ctx):
    embed = discord.Embed(title="Info for the <beta> command", description="Beta command displays a text..", color=0x00a0ea)
    await bot.say(embed=embed)
@bot.command()
async def emojimoderate():
    await bot.say("```Please, do not use an emoji repeatedly or in an annoying way, as this might result in a ban.```")
token = os.environ.get("TOKEN")
bot.run(f'{token}')
#bot link https://discordapp.com/oauth2/authorize?client_id=397217109035450368&scope=bot&permissions=0
