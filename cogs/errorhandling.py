import discord
import discord.utils
from discord.ext import commands
from discord.utils import get

class ErrorHandling(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(title="ERROR", description='You do not have permission to execute that command',
                                  color=discord.Color.red())
            embed.set_footer(text="NightMC bot made by TME#7107",
                             icon_url="https://cdn.discordapp.com/attachments/783224139800510524/786634170779697152/Nightmc_Bot-Logo.png")
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(ErrorHandling(bot))