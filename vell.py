#Vell Bot v0.1  -------  Test rep, THIS IS NOT THE MAIN REP, IT IS PRIVATE!
import os
# CONFIG
# --------- #
prefix = ['v.', 'join.', 'mod.'] # This will be used at the start of commands.
embed_role = "Vell" # The role in your server used for embedding.
game = "Type v.help" # This will display as the game on Discord.
# ---------- #
from discord.ext import commands
import asyncio
from discord.ext.commands import Bot
import discord
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
    await bot.change_presence(game=discord.Game(name="Type v.help for help, duh..."))

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
    
#------Music Module-----#
if not discord.opus.is_loaded():
    discord.opus.load_opus('opus')

def __init__(self, bot):
        self.bot = bot

class VoiceEntry:
    def __init__(self, message, player):
        self.requester = message.author
        self.channel = message.channel
        self.player = player

    def __str__(self):
        fmt = ' {0.title} uploaded by {0.uploader} and requested by {1.display_name}'
        duration = self.player.duration
        if duration:
            fmt = fmt + ' [length: {0[0]}m {0[1]}s]'.format(divmod(duration, 60))
        return fmt.format(self.player, self.requester)

class VoiceState:
    def __init__(self, bot):
        self.current = None
        self.voice = None
        self.bot = bot
        self.play_next_song = asyncio.Event()
        self.songs = asyncio.Queue()
        self.skip_votes = set() # a set of user_ids that voted
        self.audio_player = self.bot.loop.create_task(self.audio_player_task())

    def is_playing(self):
        if self.voice is None or self.current is None:
            return False

        player = self.current.player
        return not player.is_done()

    @property
    def player(self):
        return self.current.player

    def skip(self):
        self.skip_votes.clear()
        if self.is_playing():
            self.player.stop()

    def toggle_next(self):
        self.bot.loop.call_soon_threadsafe(self.play_next_song.set)

    async def audio_player_task(self):
        while True:
            self.play_next_song.clear()
            self.current = await self.songs.get()
            await self.bot.send_message(self.current.channel, 'Now playing' + str(self.current))
            self.current.player.start()
            await self.play_next_song.wait()
class Music:
    """Voice related commands.
    Works in multiple servers at once.
    """
    def __init__(self, bot):
        self.bot = bot
        self.voice_states = {}

    def get_voice_state(self, server):
        state = self.voice_states.get(server.id)
        if state is None:
            state = VoiceState(self.bot)
            self.voice_states[server.id] = state

        return state

    async def create_voice_client(self, channel):
        voice = await self.bot.join_voice_channel(channel)
        state = self.get_voice_state(channel.server)
        state.voice = voice

    def __unload(self):
        for state in self.voice_states.values():
            try:
                state.audio_player.cancel()
                if state.voice:
                    self.bot.loop.create_task(state.voice.disconnect())
            except:
                pass

    @bot.command(pass_context=True, no_pm=True)
    async def join(self, ctx, *, channel : discord.Channel):
        """Joins a voice channel."""
        try:
            await self.create_voice_client(channel)
        except discord.ClientException:
            await self.bot.say('Already in a voice channel...')
        except discord.InvalidArgument:
            await self.bot.say('This is not a voice channel...')
        else:
            await self.bot.say('Ready to play audio in **' + channel.name)

    @commands.command(pass_context=True, no_pm=True)
    async def summon(self, ctx):
        """Summons the bot to join your voice channel."""
        summoned_channel = ctx.message.author.voice_channel
        if summoned_channel is None:
            await self.bot.say('Are you sure your in a channel?')
            return False

        state = self.get_voice_state(ctx.message.server)
        if state.voice is None:
            state.voice = await self.bot.join_voice_channel(summoned_channel)
        else:
            await state.voice.move_to(summoned_channel)

        return True

    @commands.command(pass_context=True, no_pm=True)
    async def play(self, ctx, *, song : str):
        """Plays a song.
        If there is a song currently in the queue, then it is
        queued until the next song is done playing.
        This command automatically searches as well from YouTube.
        The list of supported sites can be found here:
        https://rg3.github.io/youtube-dl/supportedsites.html
        """
        state = self.get_voice_state(ctx.message.server)
        opts = {
            'default_search': 'auto',
            'quiet': True,
        }

        if state.voice is None:
            success = await ctx.invoke(self.summon)
            await self.bot.say("Loading the song please be patient..")
            if not success:
                return

        try:
            player = await state.voice.create_ytdl_player(song, ytdl_options=opts, after=state.toggle_next)
        except Exception as e:
            fmt = 'An error occurred while processing this request: ```py\n{}: {}\n```'
            await self.bot.send_message(ctx.message.channel, fmt.format(type(e).__name__, e))
        else:
            player.volume = 0.6
            entry = VoiceEntry(ctx.message, player)
            await self.bot.say('Enqueued ' + str(entry))
            await state.songs.put(entry)

    @commands.command(pass_context=True, no_pm=True)
    async def volume(self, ctx, value : int):
        """Sets the volume of the currently playing song."""

        state = self.get_voice_state(ctx.message.server)
        if state.is_playing():
            player = state.player
            player.volume = value / 100
            await self.bot.say('Set the volume to {:.0%}'.format(player.volume))
    @commands.command(pass_context=True, no_pm=True)
    async def resume(self, ctx):
        """Resumes the currently played song."""
        state = self.get_voice_state(ctx.message.server)
        if state.is_playing():
            player = state.player
            player.resume()

    @commands.command(pass_context=True, no_pm=True)
    async def stop(self, ctx):
        """Stops playing audio and leaves the voice channel.
        This also clears the queue.
        """
        server = ctx.message.server
        state = self.get_voice_state(server)

        if state.is_playing():
            player = state.player
            player.stop()

        try:
            state.audio_player.cancel()
            del self.voice_states[server.id]
            await state.voice.disconnect()
            await self.bot.say("Cleared the queue and disconnected from voice channel ")
        except:
            pass

    @commands.command(pass_context=True, no_pm=True)
    async def skip(self, ctx):
        """Vote to skip a song. The song requester can automatically skip.
        3 skip votes are needed for the song to be skipped.
        """

        state = self.get_voice_state(ctx.message.server)
        if not state.is_playing():
            await self.bot.say('Not playing any music right now...')
            return

        voter = ctx.message.author
        if voter == state.current.requester:
            await self.bot.say('Requester requested skipping song...')
            state.skip()
        elif voter.id not in state.skip_votes:
            state.skip_votes.add(voter.id)
            total_votes = len(state.skip_votes)
            if total_votes >= 3:
                await self.bot.say('Skip vote passed, skipping song...')
                state.skip()
            else:
                await self.bot.say('Skip vote added, currently at [{}/3]'.format(total_votes))
        else:
            await self.bot.say('You have already voted to skip this song.')

    @commands.command(pass_context=True, no_pm=True)
    async def playing(self, ctx):
        """Shows info about the currently played song."""

        state = self.get_voice_state(ctx.message.server)
        if state.current is None:
            await self.bot.say('Not playing anything.')
        else:
            skip_count = len(state.skip_votes)
            await self.bot.say('Now playing {} [skips: {}/3]'.format(state.current, skip_count))
            
def setup(bot):
    bot.add_cog(Music(bot))
    print('Music is loaded')

token = os.environ.get("TOKEN")
bot.run(f'{token}')
#bot link https://discordapp.com/oauth2/authorize?client_id=368592012116623362&scope=bot&permissions=8
