#Vell Bot v0.1  -------  Test rep, THIS IS NOT THE MAIN REP, IT IS PRIVATE!
import os
import youtube_dl

# CONFIG
# --------- #
prefix = ["v.", "join.", "mod."]
embed_role = "Vell" # The role in your server used for embedding.
game = "Type v.help" # This will display as the game on Discord.
# ---------- #
from discord.voice_client import VoiceClient
from discord.ext import commands
import asyncio
from discord.ext.commands import Bot
import discord
import requests
global misc_commands
misc_commands = ["supportserver"]
global command_help
command_help = "For more info on a command type v.commandhelp where command is the name of it. Ex: v.nsfwhelp"
global music_commands
music_commands = ["In progress, not available yet..."]
global mod_commands
mod_commands = ["emoji", "text", "nsfw", "kick"]
bot = commands.Bot(command_prefix=prefix)
bot.remove_command("help")

@bot.event
async def on_ready():
    await bot.change_presence(game=discord.Game(name="Use v.help for help menu."))
    print("Bot online")
startup_extensions = ["Music"]
    
class Main_Commands():
 def __init__(self, bot):
  self.bot = bot
  

  
@bot.command(pass_context=True)
async def hello(ctx):
    await bot.say("Hey there! :wave:")

@bot.command(pass_context=True)
async def kick(ctx, user:discord.Member, *, reason:str=None):
    """Kicks someone from the server"""
    if reason is None:
        reason = "The ban hammer has spoken. :ban:"
        try:
            await bot.kick(user)
        except discord.errors.Forbidden:
                await bot.say("Either I do not have permission, or you do not... Please contact server admins if you should be able to.")
                return "{0.mention} has been kicked from the server."
                return reason
@bot.command(pass_context=True)
async def ban(ctx, user:discord.Member, *, reason:str=None):
    """Bans someone from the server"""
    if reason is None:
        reason = "The ban hammer has spoken. :ban:"
        try:
            await bot.kick(user)
        except discord.errors.Forbidden:
                await bot.say("Either I do not have permission, or you do not... Please contact server admins if you should be able to.")
                return "{0.mention} has been banned from the server."
                return reason
          

@bot.event
async def on_member_join(member):
    server = member.server.default_channel
    fmt = 'Hey! {0.mention} Welcome to {1.name} the official support server for Vell Bot, any issues? Talk to us!'
    channel = member.server.get_channel("410605613354319872")
    await bot.send_message(channel, fmt.format(member, member.server))

@bot.event
async def on_member_remove(member):
    server = member.server.default_channel
    fmt = '{0.mention} has left/been kicked/banned from the server.'
    channel = member.server.get_channel("429774341152964618")
    await bot.send_message(channel, fmt.format(member, member.server))   

@bot.command(pass_context=True)
async def website(ctx):
    embed1 = embed.discord.Embed(title="The official Vell website is located at: www.jdcoding7.wixsite.com/vellbot", description="Leave a comment!", colorr=0x00a0ea)
    embed1.set_thumbnail(url= "https://thumb.ibb.co/c1yBAS/icon.jpg") 
    await bot.say(embed=embed1)
@bot.command(pass_context=True)
async def help(ctx):
    
    embed = discord.Embed(title="Vell Bot Help Menu", description="Here you will find all the help you need. Not satisfied? Type join.supportserver, to join our Official Support Server.", color=0x00a0ea)
    embed.add_field(name="This is my website".format("null"), value="www.jdcoding7.wixsite.com/vellbot")
    embed.add_field(name="My prefixes".format("null"), value="v. for general commands | join. for joining support server |mod. for mod commands")
    embed.set_thumbnail(url = "https://thumb.ibb.co/c1yBAS/icon.jpg")
    embed.add_field(name="Miscellaneous Commands".format("null"), value=misc_commands, inline=False)
    embed.add_field(name="Music Commands".format("null"), value=music_commands, inline=False)
    embed.add_field(name="Commands Help".format("null"), value=command_help)
    embed.add_field(name="Moderator Commands".format("null"), value=mod_commands)
    embed.set_footer(text="Vell Bot ~ Developed by Alphi#5113")
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def betahelp(ctx):
    embed = discord.Embed(title="Info for the <beta> command", description="Beta command displays a text..", color=0x00a0ea)
    await bot.say(embed=embed)
@bot.command(pass_context=True)
async def emojihelp(ctx):
    embed = discord.Embed(title="Info for the <emoji> moderator command", description="Sends a text warning regarding the misuse of server emojis.", color=0x00a0ea)
    await bot.say(embed=embed)
@bot.command(pass_context=True)
async def texthelp(ctx):
    embed = discord.Embed(title="Info for the <text> moderator command", description="Sends a text warning regarding the bad behavior with texts. Like harrasing or bullying.", color=0x00a0ea)
    await bot.say(embed=embed)
@bot.command(pass_context=True)
async def nsfwhelp(ctx):
    embed = discord.Embed(title="Info for the <nsfw> moderator command", description="Sends a text warning regarding the use of NSFW or innappropiate language outside of the NSFW channel.", color=0x00a0ea)
    await bot.say(embed=embed)
@bot.command(pass_context=True)
async def kickhelp(ctx):
    embed = discord.Embed(title="Info for the <kick> moderator command", description="Kicks the @mentioned user fom the server. (Only for Admins/Owners/Mods", color=0x00a0ea)
    await bot.say(embed=embed)
@bot.command()
async def emoji():
    await bot.say("```Please, do not use an emoji repeatedly or in an annoying way, as this might result in a ban.```")
@bot.command()
async def text():
    await bot.say("```The texts you're sending right now are inappropiate, please stop or you might be kicked from the server.```")
@bot.command()
async def nsfw():
    await bot.say("```That message is considered NSFW, which is not allowed in this channel. It will be removed immediately, if you persist you will earn a kick or ban as the responsible MOD considers it.```")
@bot.command()
async def invite():
    await bot.say("Invite me with this link: " + "https://discordapp.com/oauth2/authorize?client_id=368592012116623362&scope=bot&permissions=8")
@bot.command()
async def supportserver():
    await bot.say("Support server: https://discord.gg/YAZNjbe")

if __name__ == "__main__":
 for extension in startup_extensions:
  try:
   bot.load_extension(extension)
  except Exception as e:
   exc = '{}: {}'.format(type(e).__name__, e)
   print('Failed to load extension {}\n{}'.format(extension, exc))
  


  
  

token = os.environ.get("TOKEN")
bot.run(f'{token}')

