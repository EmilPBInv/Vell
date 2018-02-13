#Vell Bot v0.1  -------  Test rep, THIS IS NOT THE MAIN REP, IT IS PRIVATE!
import os
# CONFIG
# --------- #
token = "TOKEN_HERE" # This is what the bot uses to log into Discord.
prefix = "!" # This will be used at the start of commands.
embed_role = "ROLE_NAME_HERE" # The role in your server used for embedding.
game = "with embeds!" # This will display as the game on Discord.
# ---------- #
from discord.ext import commands
from discord.ext.commands import Bot
import discord

bot = commands.Bot(command_prefix=prefix)
bot.remove_command("help")

@bot.event
async def on_ready():
    await bot.change_presence(game=discord.Game(name=game))

@bot.command(pass_context=True)
async def help(ctx):
    embed = discord.Embed(title="Vell Bot Help Menu", description="Here you will find all the help you need.Not satisfied? Type join.supportserver", color=0x00a0ea)
    embed.add_field(name="{}embed".format(prefix), value=".")
    embed.add_field(name="{}rembed".format(prefix), value="Let's you embed with more user input. After entering your message the bot will ask questions about the color and thumbnail.")
    embed.set_footer(text="Embed-This!")
    await bot.say(embed=embed)

@bot.command(pass_context=True)
@commands.has_role(embed_role)

token = os.environ.get("TOKEN")
bot.run(f'{token}')
#bot link https://discordapp.com/oauth2/authorize?client_id=397217109035450368&scope=bot&permissions=0
