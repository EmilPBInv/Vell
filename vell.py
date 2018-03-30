#Vell Bot v0.1  -------  Test rep, THIS IS NOT THE MAIN REP, IT IS PRIVATE!
import os
# CONFIG
# --------- #
prefix = ['v.', 'join.', 'mod.'] # This will be used at the start of commands.
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
misc_commands = ["beta", "supportserver"]
global command_help
command_help = "For more info on a command type v.commandhelp where command is the name of it. Ex: v.betahelp"
global music_commands
music_commands = ["In progress, not available yet..."]
global mod_commands
mod_commands = "emoji", "text", "nsfw"
bot = commands.Bot(command_prefix=prefix)
bot.remove_command("help")


 
@bot.event
async def on_ready():
    await bot.change_presence(game=discord.Game(name="Use v.help for help menu."))
  
@bot.command(pass_context=True)
async def kick(ctx, user:discord.Member, *, reason:str=None):
    """Kicks someone from the server"""
    if reason is None:
        reason = "The ban hammer has spoken."
        try:
            await bot.kick(user)
        except discord.errors.Forbidden:
                await bot.say("Either I do no have permission, or you do not... Please contact server admins if you should be able to.")
                return

@bot.event
async def on_member_join(member):
    server = member.server.default_channel
    fmt = ':karma: What goes around, must come back around. :karma: Hey! {0.mention} Welcome to {1.name}. Please read #karma_page and #peerages \
    Karma is now recruiting for dedicated players to blow through the game. Help us grow stronger and your karma will be served. May your blade run red with the blood of our enemies'
    channel = member.server.get_channel("336499566906179585")
    await bot.send_message(channel, fmt.format(member, member.server))

@bot.event
async def on_member_remove(member):
    server = member.server.default_channel
    fmt = '{0.mention} has left/been kicked/banned from the server.'
    channel = member.server.get_channel("336499566906179585")
    await bot.send_message(channel, fmt.format(member, member.server))   
    
@bot.command(pass_context=True)
async def help(ctx):
    embed = discord.Embed(title="Vell Bot Help Menu", description="Here you will find all the help you need. Not satisfied? Type join.supportserver, to join our Official Support Server.", color=0x00a0ea)
    embed.add_field(name="My prefixes".format("null"), value="v. for general commands|join. for joining support server|mod. for mod commands")
    embed.set_thumbnail(url = "https://www.freepik.com/free-icon/info-logo-in-a-circle_692769.htm")
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

      
@bot.command(pass_context = True) 
async def serverinfo(ctx):
 server = ctx.message.server
 roles = [x.name for x in server.role_hierarchy]
 role_length = len(roles)
if role_length > 50: 
    roles = roles[:50]
    roles.append('>>>> [50/%s] Roles'%len(roles))

roles = ', '.join(roles);
channelz = len(server.channels);
time = str(server.created_at); time = time.split(' '); time= time[0];
join = discord.Embed(description= '%s '%(str(server)),title = 'Server Name', colour = 0xFFFF);
join.set_thumbnail(url = server.icon_url);
join.add_field(name = '__Owner__', value = str(server.owner) + '\n' + server.owner.id);
join.add_field(name = '__ID__', value = str(server.id))
join.add_field(name = '__Member Count__', value = str(server.member_count));
join.add_field(name = '__Text/Voice Channels__', value = str(channelz));
join.add_field(name = '__Roles (%s)__'%str(role_length), value = roles);
join.set_footer(text ='Created: %s'%time);
  return await bot.say(embed = join);
token = os.environ.get("TOKEN")
bot.run(f'{token}')
