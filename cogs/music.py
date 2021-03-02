from discord.ext import commands
import lavalink
from discord import utils
from discord import Embed
import discord
import math
import re

url_rx = re.compile(r'https?://(?:www\.)?.+')


class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bot.music = lavalink.Client(self.bot.user.id)
        self.bot.music.add_node('your lavalink server ip', your server port, 'your password', 'na', 'music-node')
        self.bot.add_listener(self.bot.music.voice_update_handler, 'on_socket_response')
        self.bot.music.add_event_hook(self.track_hook)

    @commands.command(name='join')
    async def join(self, ctx):
        print('join command worked')
        member = utils.find(lambda m: m.id == ctx.author.id, ctx.guild.members)
        if member is not None and member.voice is not None:
            vc = member.voice.channel
            player = self.bot.music.player_manager.create(ctx.guild.id, endpoint=str(ctx.guild.region))
            if not player.is_connected:
                player.store('channel', ctx.channel.id)
                await self.connect_to(ctx.guild.id, str(vc.id))

        else:
            await ctx.send('Please connect to a voice chat first')


    @commands.command(name='play')
    async def play(self, ctx, *, query):
        member = utils.find(lambda m: m.id == ctx.author.id,
                            ctx.guild.members)  # This will connect the bot if it is not already connected.
        if member is not None and member.voice is not None:
            vc = member.voice.channel
            player = self.bot.music.player_manager.create(ctx.guild.id, endpoint=str(ctx.guild.region))
            if not player.is_connected:
                player.store('channel', ctx.channel.id)  # used so we have the ctx.channel usage
                await self.connect_to(ctx.guild.id, str(vc.id))

            if player.is_connected and not ctx.author.voice.channel.id == int(
                    player.channel_id):  # Make sure the person is in the same channel as the bot to add to queue.
                return await ctx.channel.send("Please connect to the same chat as the bot.")

            try:
                player = self.bot.music.player_manager.get(ctx.guild.id)
                query = query.strip('<>')
                if not url_rx.match(query):  # This and the line above and below allow for direct link play
                    query = f'ytsearch:{query}'
                results = await player.node.get_tracks(query)
                try:
                    tracks = results['tracks'][0:10]
                    print(tracks)
                    i = 0
                    query_result = ''
                    for track in tracks:
                        i = i + 1
                        query_result = query_result + f'{i}) {track["info"]["title"]} - {track["info"]["uri"]}\n'

                    embed = Embed()
                    embed.description = query_result

                    await ctx.channel.send(embed=embed)

                    def check(m):
                        return m.author.id == ctx.author.id

                    response = await self.bot.wait_for('message', check=check)
                    track = tracks[int(response.content) - 1]



                    player.add(requester=ctx.author.id, track=track)


                    if not player.is_playing:
                        await player.play()
                        embed2 = Embed()
                        title = track["info"]["title"]
                        uri = track["info"]["uri"]
                        embed2.title = "**PLAYING NOW!!!!**"
                        embed2.description = f'**[{title}]({uri})**'
                        await ctx.send(embed=embed2)
                        print(track)
                        print(track["info"]["title"])

                    elif player.is_playing == True:
                        embed2 = Embed()
                        title = track["info"]["title"]
                        uri = track["info"]["uri"]
                        embed2.title = "**TRACK ENQUEUED**"
                        embed2.description = f'[{title}]({uri})'
                        await ctx.send(embed=embed2)

                except Exception as error:
                    await ctx.channel.send("Song not found. (or title has emojis/symbols)")

            except Exception as error:
                print(error)

    @commands.command(name='skip')
    async def skip(self, ctx, amount = 1):
        try:
            player = self.bot.music.player_manager.get(ctx.guild.id)
            x = 0
            while (x < amount):
                x = x + 1
                if ctx.author.voice is not None and ctx.author.voice.channel.id == int(player.channel_id):
                    if not player.is_playing:
                        return await ctx.channel.send("Nothing playing to skip.")
                    else:
                        await player.skip()
                        if x == 1:  # make sure song skipped only prints once.
                            await ctx.channel.send("Song skipped.")
                            player = self.bot.music.player_manager.get(ctx.guild.id)
                            embed = discord.Embed(title=player.current.title,
                                                  url=f"https://youtube.com/watch?v={player.current.identifier}")
                            await ctx.send(embed=embed)


                else:
                    return await ctx.channel.send("Please join the same voice channel as me.")
        except:
            return await ctx.channel.send("Nothing playing.")

    @commands.command(name='pause')
    async def pause(self, ctx):
        player = self.bot.music.player_manager.get(ctx.guild.id)
        await player.set_pause(True)

    @commands.command(name='resume')
    async def resume(self, ctx):
        player = self.bot.music.player_manager.get(ctx.guild.id)
        await player.set_pause(False)

    @commands.command(name='queue')
    async def queue(self, ctx, page: int = 1):
        player = self.bot.music.player_manager.get(ctx.guild.id)

        items_per_page = 10
        pages = math.ceil(len(player.queue) / items_per_page)

        start = (page - 1) * items_per_page
        end = start + items_per_page

        queue_list = ''
        for index, track in enumerate(player.queue[start:end], start=start):
            queue_list += f'`{index + 1}.` [**{track.title}**]({track.uri})\n'

        embed = discord.Embed(title='QUEUE', colour=discord.Color.blurple(),
                              description=f'**{len(player.queue)} tracks**\n\n{queue_list}')
        embed.set_footer(text=f'Viewing page {page}/{pages}')
        await ctx.send(embed=embed)

    @commands.command(name='stop')
    async def stop(self, ctx):
        global voice
        channel = ctx.message.author.voice.channel

        voice = discord.utils.get(ctx.bot.voice_clients, guild=ctx.guild)

        if voice and voice.is_connected:
            await voice.disconnect()
            await ctx.send(f'Left **{channel}**')



    async def track_hook(self, event):
        if isinstance(event, lavalink.events.QueueEndEvent):
            guild_id = int(event.player.guild_id)
            await self.connect_to(guild_id, None)



    async def connect_to(self, guild_id: int, channel_id: str):
        ws = self.bot._connection._get_websocket(guild_id)
        await ws.voice_state(str(guild_id), channel_id)

    @commands.command(name='shuffle')
    async def shuffle(self,ctx):
        try:
            player = self.bot.music.player_manager.get(ctx.guild.id)
            if ctx.author.voice is not None and ctx.author.voice.channel.id == int(player.channel_id):
                if player.is_playing:
                    try:
                        player.shuffle = True
                        await ctx.channel.send("Currently playing has been shuffled.")
                    except Exception as error:
                        print(error)
                else:
                    await ctx.channel.send("No music playing.")
            else:
                await ctx.channel.send("Please join my channel to shuffle.")
        except:
            await ctx.channel.send("Nothing playing.")


    @commands.command(name='np')
    async def np(self, ctx):
        player = self.bot.music.player_manager.get(ctx.guild.id)
        embed = discord.Embed(title=player.current.title,
                              url=f"https://youtube.com/watch?v={player.current.identifier}")
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Music(bot))