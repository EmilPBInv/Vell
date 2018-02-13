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
misc_commands = ["~beta", "~supportserver"]
global command_help
command_help = "For more info on a command type v.commandhelp where command is the name of it. Ex: v.betahelp"
global music_commands
music_commands = "In progress, not available yet..."
bot = commands.Bot(command_prefix=prefix)
bot.remove_command("help")

@bot.event
async def on_ready():
    await bot.change_presence(game=discord.Game(name="Type v.help for help, duh..."))

@bot.command(pass_context=True)
async def help(ctx):
    embed = discord.Embed(title="Vell Bot Help Menu", description="Here you will find all the help you need. Not satisfied? Type join.supportserver!", color=0x00a0ea)
    embed.set_thumbnail(url = self.bot.user.avatar_url)
    embed.add_field(name="Miscellaneous Commands".format("null"), value=misc_commands, inline=False)
    embed.add_field(name="Music Commands".format("null"), value=music_commands)
    embed.add_field(name="Commands Help".format("null"), value=command_help)
    embed.set_footer(text="Vell Bot ~ Developed by Alphi#5113")
    await bot.say(embed=embed)
@bot.command(pass_context=True)
async def betahelp(ctx):
    embed = discord.Embed(title="Info for the <beta> command", description="Beta command displays a text..", color=0x00a0ea)
    await bot.say(embed=embed)
@bot.command()
async def emojimoderate():
    await bot.say("```Please, do not use an emoji repeatedly or in an annoying way, as this might result in a ban.```")
@bot.command()
async def invite():
    await bot.say("Invite me with this link: " + "https://discordapp.com/oauth2/authorize?client_id=368592012116623362&scope=bot&permissions=8")
@bot.command()
async def supportserver():
    await bot.say("Support server: https://discord.gg/YAZNjbe")
token = os.environ.get("TOKEN")
bot.run(f'{token}')
#bot link https://discordapp.com/oauth2/authorize?client_id=368592012116623362&scope=bot&permissions=8
