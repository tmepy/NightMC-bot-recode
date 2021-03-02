import discord
import discord.utils
from discord.ext import commands
from discord.utils import get

class Mod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='ban')
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member = None, *, reason=None):
        if member == None or member == ctx.message.author:
            embed = discord.Embed(title='BAN WARNING',
                                  description=f'Hey {ctx.author.mention},\nYou cannot **ban** urself!!!!',
                                  colour=discord.Color.red())
            embed.set_footer(text="NightMC bot made by TME#7107",
                             icon_url="https://cdn.discordapp.com/attachments/783224139800510524/786634170779697152/Nightmc_Bot-Logo.png")
            await ctx.channel.send(embed=embed)
            return

        if reason == None:
            reason = "For not follwing the rules of the server!!!!"
        embed_user = discord.Embed(title="BAN",
                                   description=f'Hey {member.mention}, \nYou have been banned on **NightMC** becasuse of\n\n{reason}',
                                   colour=discord.Color.blue())
        embed_user.set_footer(text="NightMC bot made by TME#7107",
                              icon_url="https://cdn.discordapp.com/attachments/783224139800510524/786634170779697152/Nightmc_Bot-Logo.png")
        await member.send(embed=embed_user)
        embed = discord.Embed(title="BAN Successful",
                              description=f'Hey {ctx.author.mention},\n{member.mention} has been successfully banned from the server',
                              colour=discord.Color.blue())
        embed.set_footer(text="NightMC bot made by TME#7107",
                         icon_url="https://cdn.discordapp.com/attachments/783224139800510524/786634170779697152/Nightmc_Bot-Logo.png")
        await member.guild.ban(member, reason=reason)
        await ctx.channel.send(embed=embed)

    @commands.command(name='lock')
    @commands.has_permissions(manage_channels=True)
    async def lock(self, ctx, channel: discord.TextChannel = None):
        member = discord.utils.get(ctx.guild.roles, id=803743837008298044)
        overwrite = ctx.channel.overwrites_for(member)
        overwrite.send_messages = False
        await ctx.channel.set_permissions(member, overwrite=overwrite)
        await ctx.send('Channel locked.')

    @commands.command(name = 'unlock')
    @commands.has_permissions(manage_channels=True)
    async def unlock(self, ctx, channel: discord.TextChannel = None):
        member = discord.utils.get(ctx.guild.roles, id=803743837008298044)
        overwrite = ctx.channel.overwrites_for(member)
        overwrite.send_messages = True
        await ctx.channel.set_permissions(member, overwrite=overwrite)
        await ctx.send('Channel unlocked.')

    @commands.command(aliases=['delete', 'del', 'purge'])
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount=5):
        await ctx.channel.purge(limit=amount + 1)
        await ctx.channel.send(f'{amount} messages deleted by {ctx.message.author}', delete_after=2)

    @commands.command(name='announce')
    @commands.has_permissions(administrator=True)
    async def announce(self, ctx, *, message: str = None):
        if message == None:
            embed = discord.Embed(title='ERROR!!!', description='Please provide something to announce :blush:',
                                  color=discord.Color.red())
            await ctx.send(embed=embed)
            return
        message_args = message.split("  ")
        embed = discord.Embed(title=message_args[0], description=message_args[1], colour=discord.Color.blue())
        embed.set_footer(text="NightMC bot made by TME#7107",
                         icon_url="https://cdn.discordapp.com/attachments/783224139800510524/786634170779697152/Nightmc_Bot-Logo.png")
        embed.set_image(url="https://cdn.discordapp.com/attachments/783224139800510524/786946157603455006/NGsTdv4V.gif")
        channel = self.bot.get_channel(803745352742207488)
        announce = discord.utils.get(ctx.guild.roles, id=803745336397004830)
        embed2 = discord.Embed(title="Success!!!!", description="Announcement created successfully.",
                               colour=discord.Color.blue())
        embed2.set_footer(text="NightMC bot made by TME#7107",
                          icon_url="https://cdn.discordapp.com/attachments/783224139800510524/786634170779697152/Nightmc_Bot-Logo.png")
        await channel.send(embed=embed)
        await channel.send(announce.mention)
        await ctx.channel.send(embed=embed2)

    @commands.command(name='say')
    @commands.has_permissions(administrator=True)
    async def say(self, ctx, *, message: str = None):
        if message == None:
            embed = discord.Embed(title='ERROR!!!', description='Please provide something to say :blush:',
                                  color=discord.Color.red())
            await ctx.send(embed=embed)
            return
        message_args = message.split("  ")
        if message_args[1] == None:
            message_args[1] = ' '
        embed = discord.Embed(title=message_args[0], description=message_args[1], colour=discord.Color.blue())
        embed.set_footer(text="NightMC bot made by TME#7107",
                         icon_url="https://cdn.discordapp.com/attachments/783224139800510524/786634170779697152/Nightmc_Bot-Logo.png")
        embed2 = discord.Embed(title="Success!!!!", description="Announcement created successfully.",
                               colour=discord.Color.blue())
        embed2.set_footer(text="NightMC bot made by TME#7107",
                          icon_url="https://cdn.discordapp.com/attachments/783224139800510524/786634170779697152/Nightmc_Bot-Logo.png")
        await ctx.channel.send(embed=embed)




def setup(bot):
    bot.add_cog(Mod(bot))