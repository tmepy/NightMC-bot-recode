import discord
import discord.utils
from discord.ext import commands
from discord.utils import get

class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def suggest(self, ctx, *, suggestion: str = None):
        if suggestion == None:
            failed_embed = discord.Embed(title="Suggestion Failed", description="Please tell something to suggest",
                                         color=discord.Color.red())
            await ctx.send(embed=failed_embed)
            return

        embed = discord.Embed(title="Suggestion", description=suggestion, color=discord.Color.blue())
        embed.set_footer(text=f"Suggestion by {ctx.author.name}", icon_url=ctx.author.avatar_url)

        successful_embed = discord.Embed(title="Suggestion Successful", description='Suggestion created successfully',
                                         colour=discord.Color.green())

        channel = self.bot.get_channel(803745358207385620)

        message = await channel.send(embed=embed)

        await message.add_reaction('<a:bot_tick:805658829189677096>')
        await message.add_reaction('<a:cross_bot:805658996773879830>')

        await ctx.send(embed=successful_embed)

    @commands.command()
    async def google(self, ctx, *, search: str = None):
        if search == None:
            search = "bruh u did not search anything -_-"

        search = search.replace(" ", "%20")

        await ctx.send(f"https://www.google.com/search?&q={search}+")

    @commands.command()
    async def ping(self, ctx):
        embed = (discord.Embed(
            title="Pong!",
            description=f"The ping is **{round(self.bot.latency * 1000)} ms** or **{self.bot.latency} seconds**.",
            colour=discord.Color.blue()
        ))
        embed.set_footer(text="NightMC bot made by TME#7107",
                         icon_url="https://cdn.discordapp.com/attachments/783224139800510524/786634170779697152/Nightmc_Bot-Logo.png")
        await ctx.channel.send(embed=embed)

def setup(bot):
    bot.add_cog(General(bot))