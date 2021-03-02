import discord
import discord.utils
from discord.ext import commands
from discord.utils import get

class CustomEmbeds(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='boosters', aliases=['booster'])
    async def boosters(self, ctx):
        embed = discord.Embed(title="Booster perks", description='''
    1. Bypass All Slowmodes.
    2. Exclusive @Server Boosters and @Donators Role.
    3. @V.I.P  Role on our Minecraft Server and As well as Discord.
    4. Priority Service.
    5. 5% Higher Chances of Winning Giveaways!
    Note -> Applied for 1 Boost only and Max 2 times also Ranks and Perks will be removed if Unboosted the Server.    
    ''', color=discord.Color.blue())
        embed.set_footer(text="NightMC bot made by TME#7107",
                         icon_url="https://cdn.discordapp.com/attachments/783224139800510524/786634170779697152/Nightmc_Bot-Logo.png")
        embed.set_image(url="https://cdn.discordapp.com/attachments/783224073450553344/786994537830154290/9CGKx4jR.gif")
        embed.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/766232569716277249/786991725708705822/7552_Pepe_NitroBoost.gif")
        await ctx.channel.send(embed=embed)

    @commands.command(name='store')
    async def store(self, ctx):
        embed = discord.Embed(title=":crescent_moon:   NightMC  Store", description='''
        Due to Cross-Play and Bedrock People dont have A UUID So we are not Able to make online Store However We Made our Store On Discord Now So you Guys can get some Awesome ranks with tons of features like cosmetics and 
        permissions like fly, nick, vanish or hide, disguise and Many more! 
        1. **V.I.P** -> This The Cheapest Rank Available and Has Some Basic Perms like /fly, Use only First 3 Cosmetics for Free. Due to Being a Premium Member of the Server, They are Automatically the Part of Beta Tester | Member and Can are  Whitelisted so they can still play. This Rank has a prefix of @V.I.P .
        **Price -> 3 USD**
        2. **V.I.P+** -> This rank being the Second most cheapest rank, it inherits the same features as the V.I.Ps and including the perms to use /disguise, /skin, and can use the first 5 Cosmetics for Free! Its has a Prefix of @V.I.P+.
        **Price -> 5 USD**
    ''', color=discord.Color.blue())
        await ctx.channel.send(embed=embed)
        embed = discord.Embed(description='''
        3. **M.V.P** -> This Rank is Marked as one of the Most Premium ranks on the Server and has all the Previous features mentioned in the Above rank. This is the Most Highly Recommended Rank and Most Small Youtuber Use it as its a Budget Rank and gives you access to almost everything! Including the Previous features, it has /nick, /kaboom, and some more interesting features including the the perms to access the first 10 Cosmetics for Free! It has a Prefix of @M.V.P.
    **Price -> 7.5 USD**
    4. **M.V.P+** -> This is the Second most premium rank and can claim Monthly Rewards like coins, experience, and has 10% more chances in winning giveways like store cash or paypal money and also has access to 15 Best cosmetics in the server and also all the Previously mentioned Perms. It has a Prefix of @M.V.P+.
    **Price -> 3.5 USD Per Month**
    5. **M.V.P++** -> _This Rank is the Most Premium Rank and Has all the Perms a Youtuber Rank would have and Has
    access to all Cosmetics and also access to all Cosmetics on the server. They can claim Weekly Rewards and have 25% more chances of winning Giveaways like store cash and all.
    **Price -> 5.5 USD Per Month**
    ''', colour=discord.Color.blue())
        embed.set_image(url="https://cdn.discordapp.com/attachments/786546606127317022/786988979542425621/zJXwJrDd.gif")
        embed.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/766232569716277249/782142295523852328/759106735389802586.gif")
        await ctx.channel.send(embed=embed)

    @commands.command(aliases=['server ip', 'port', 'minecaft ip', 'IP'])
    async def ip(self, ctx):
        embed = discord.Embed(title="IP and Port instructions!!!", description='''The IP and port are given below -
        IP : **play.Night-mc.tk**
        Port : **25904**
        Java users please paste this into the server address : play.night-mc.tk
        Bedrock users please put the ip and port in the respective places. :D
        Also use the command m/ check to see the server status (whether the server is online or not).
        Hope you enjoy your stay :grin:
        Regs,
        The NightMC Team''', colour=discord.Color.blue())
        embed.set_thumbnail(url='https://media.giphy.com/media/TOkOM7ywZC6OI/giphy.gif')
        embed.set_footer(text="NightMC bot made by TME#7107",
                         icon_url="https://cdn.discordapp.com/attachments/783224139800510524/786634170779697152/Nightmc_Bot-Logo.png")
        await ctx.channel.send(embed=embed)

def setup(bot):
    bot.add_cog(CustomEmbeds(bot))