import discord
import discord.utils
from discord.ext import commands
from discord.utils import get
import aiohttp
import random
import json


class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='avatar')
    async def avatar(self, ctx, member: discord.Member = None):
        if not member:
            member = ctx.message.author

        show_avatar = discord.Embed(
            title="AVATAR/PROFILE PIC",
            description=f"Here is the **AVATAR/PROFILE PIC** of {member}",
            color=discord.Color.gold()
        )
        show_avatar.set_image(url='{}'.format(member.avatar_url))
        show_avatar.set_footer(text="NightMC bot made by TME#7107",
                               icon_url="https://cdn.discordapp.com/attachments/783224139800510524/786634170779697152/Nightmc_Bot-Logo.png")
        await ctx.send(embed=show_avatar)


    @commands.command(pass_context=True, aliases=['giphy'], name='gif')
    async def gif(self, ctx, *, search=None):
        embed = discord.Embed(colour=discord.Colour.blue())
        session = aiohttp.ClientSession()

        if search == None:
            embed = discord.Embed(title="ERROR", description='Please provide a gif u would like to search :blush:',
                                  colour=discord.Color.red())
            await ctx.message.add_reaction("<:no_icon:803777627521024000>")
        else:
            await ctx.message.add_reaction("✅")
            search.replace(' ', '+')
            response = await session.get(
                'http://api.giphy.com/v1/gifs/search?q=' + search + '&api_key=yourapikey&limit=10')
            data = json.loads(await response.text())
            gif_choice = random.randint(0, 9)
            embed.set_image(url=data['data'][gif_choice]['images']['original']['url'])

        await session.close()

        await ctx.send(embed=embed)



    @commands.command(name='oreo')
    async def oreo(self, ctx):
        embed = discord.Embed(colour=discord.Colour.blue())
        search = 'oreo'
        session = aiohttp.ClientSession()
        response = await session.get(
            f'http://api.giphy.com/v1/gifs/search?q=oreo&api_key=yourapikey&limit=10')
        data = json.loads(await response.text())
        gif_choice = random.randint(0, 9)
        embed.set_image(url=data['data'][gif_choice]['images']['original']['url'])
        await ctx.send(embed=embed)

    @commands.command(name='_8ball', aliases=['8ball'])
    async def _8ball(self, ctx, *, question):
        responses = ['It is certain.',
                     'It is decidedly so.',
                     'Without a doubt',
                     'Yes - definitely',
                     'You may rely on it',
                     'No',
                     'Very doubtful',
                     'Better not tell you now',
                     'Outlook not so good']
        await ctx.channel.send(f'**Question** : {question}\n **Answer** {random.choice(responses)}')

    @commands.command(name='meme')
    async def meme(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"https://www.reddit.com/r/dankmemes/new.json?sort=hot,") as r:
                res = await r.json()
                embed = discord.Embed(title="Meme",
                                      description=f"Fresh Memes  {ctx.author.name}",
                                      colour=discord.Colour.blue()).set_footer(text=f"Requested by {ctx.author.name}",
                                                                               icon_url=ctx.author.avatar_url)
                embed.set_image(url=res['data']['children'][random.randint(0, 25)]['data']['url'])
                await ctx.send(embed=embed)

    @commands.command(name='pat')
    async def pat(self, ctx, member:discord.Member=None):
        if member==None:
            await ctx.send('You are so lonely ;-;')
            return
        embed = discord.Embed(title=f'{ctx.author.name} pats {member.name}')
        embed.set_image(url='https://images-ext-1.discordapp.net/external/5gTEJjgFQmEsfinxmX8eyo8-fiCOW7e-DA_J9KNxh5Q/https/cdn.nekos.life/pat/pat_015.gif')
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Fun(bot))