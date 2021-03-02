import discord
import asyncio
from discord.ext import commands
import praw
import sys
import platform
import os


token = ('place your bot token here')
prefixes = ['n! ','n!','>', '+', '&', '=']
intents = discord.Intents.default()  # Enable all intents except for members and presences
intents.members = True  # Subscribe to the privileged members intent.
client = commands.Bot(command_prefix=prefixes, intents=intents)


reddit = praw.Reddit(client_id="your reddit client id", client_secret="your client secret",
                     username="ur username", password="ur pass", user_agent="praw")
#we are not using the reddit api rn but will be adding uses for it in future

a = 1


async def status_task():
    while True:
        activity = discord.Activity(name="NightMC", type=discord.ActivityType.watching)
        await client.change_presence(status=discord.Status.idle, activity=activity)
        await asyncio.sleep(20)
        activity2 = discord.Activity(name="NightMC", type=discord.ActivityType.playing)
        await client.change_presence(status=discord.Status.idle, activity=activity2)
        await asyncio.sleep(20)
        activity3 = discord.Activity(name="NightMC", type=discord.ActivityType.listening)
        await client.change_presence(status=discord.Status.idle, activity=activity3)
        await asyncio.sleep(20)
        activity4 = discord.Activity(name="Under Development", type=discord.ActivityType.playing)
        await client.change_presence(status=
                                     discord.Status.idle, activity=activity4)
        await asyncio.sleep(20)
        activity5 = discord.Activity(name="Donations", type=discord.ActivityType.watching)
        await client.change_presence(status=discord.Status.idle, activity=activity5)
        await asyncio.sleep(20)

@client.event
async def on_ready():
    print("-------------------")
    print(f"Logged in as {client.user.name}")
    print(f"Discord.py API version: {discord.__version__}")
    print(f"Python version: {platform.python_version()}")
    print(f"Running on: {platform.system()} {platform.release()} ({os.name})")
    print(f"Bot by TME#7107")
    print("-------------------")
    client.load_extension('cogs.music')
    client.load_extension('cogs.mod')
    client.load_extension('cogs.ticket')
    client.load_extension('cogs.embeds')
    client.load_extension('cogs.fun')
    client.load_extension('cogs.general')
    client.loop.create_task(status_task())


@client.event
async def on_member_join(member):
    channel = client.get_channel(803745347385819157)
    if member.guild.id == 803741726829183048:
        embed = discord.Embed(title=f"Welcome to NightMC {member}", description=''':crescent_moon:   NightMC
        IP: **Play.Night-mc.tk**
        Port: **19132**
        Main Features :
        [+] Bedrock and Java **Cross Play** [1.8 - 1.16]
        [+] Lagless 
        [+] [Survival] Vanilla Experience and 4 Other Gamemodes [Anarchy, Plots, Vanilla, Herobrine, and 1 other Coming Soon...]
        [+] BedWars
        [+] SkyWars
        [+] SkyBlock
        [+] Family Friendly Community
        [+] Cool Ranks with Awesome Perks
        [+] Server Cosmetics 
        [+] Many More tons of Features on Discord
        [+] Store
        [+]Memes
        [+]Dope Music
        [+]Active Staff
        [+]Giveaways
        [+]And much more cool stuff. Join our discord below to experience all this. I am sure you won't regret it :D
        Thanks For Joining And Please dont Forget to Check our Store at DIscord Here is our Link:
        Website Link -> https://www.night-mc.tk/
        Forums Link -> https://www.night-mc.tk/forum/
        Discord Invite Link -> http://discord.night-mc.tk/
        https://discord.gg/nEPNMvBZ5t''', colour=discord.Color.blue())
        embed.set_thumbnail(url='{}'.format(member.avatar_url))
        embed.set_footer(text="NightMC bot made by TME#7107",
                         icon_url="https://cdn.discordapp.com/attachments/783224139800510524/786634170779697152/Nightmc_Bot-Logo.png")

        await member.send(embed=embed)
        embed2 = discord.Embed(title=f'Welcome to NightMC {member}', description=''':crescent_moon:   NightMC
        IP: **Play.Night-mc.tk**
        Port: **19132**''', colour=discord.Color.blue())
        embed2.set_footer(text="NightMC bot made by TME#7107",
                          icon_url="https://cdn.discordapp.com/attachments/783224139800510524/786634170779697152/Nightmc_Bot-Logo.png")
        embed2.set_thumbnail(url='{}'.format(member.avatar_url))
        rules = client.get_channel(803745354607886376)
        information = client.get_channel(803749955633807401)
        selfroles = client.get_channel(803745360949674054)
        server_ip = client.get_channel(803745947737128961)
        sos = client.get_channel(803769038035484672)
        await channel.send(embed=embed2)
        await channel.send(f'''<:bot:811912806999130142> Hello {member.mention} welcome to NightMC! 
    Please read the {rules.mention} and visit {information.mention} for all you need to know.
    Please go to {selfroles.mention} so you don’t miss out on any important updates.
    You can find all the server ips in {server_ip.mention}, and if you need help at any point please go to {sos.mention} <:bot:811912806999130142>''')
        await member.send(embed=embed)

    else:
        return

@client.event
async def on_member_leave(member):
    channel = client.get_channel(783221061360812032)
    embed = discord.Embed(title="Member Left", description="We are very sorry to see you leave {member}",
                          colour=discord.Color.blue())
    await channel.send(embed=embed)


@client.event
async def on_message(message):
    if client.user.mentioned_in(message):
        embed = discord.Embed(title="Bot mentioned",
                              description="Prefix of the bot as of now is **n! **\n\nPls use **n! help** to view a list of the commands of the bot.",
                              colour=discord.Color.blue())
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/773049508152999936/786850749916512276/gg.gif")
        embed.set_footer(text="NightMC bot made by TME#7107",
                         icon_url="https://cdn.discordapp.com/attachments/783224139800510524/786634170779697152/Nightmc_Bot-Logo.png")
        await message.channel.send(embed=embed)

    '''cmd_args = message.content.split("]")
    cmd = cmd_args[0]
    if len(cmd_args) > 1:
        title = cmd_args[1]
    if len(cmd_args) > 2:
        description = cmd_args[2]
    if message.content == "n! announce":
        embed = discord.Embed(title=title, description=description, colour=discord.Color.blue())
        embed.set_footer(text="NightMC bot made by TME#7107", icon_url="https://cdn.discordapp.com/attachments/783224139800510524/786634170779697152/Nightmc_Bot-Logo.png")
        embed.set_image(url="https://cdn.discordapp.com/attachments/783224139800510524/786946157603455006/NGsTdv4V.gif")
        channel = client.get_channel(796713193233580033)
        announce = discord.utils.get(cmd.guild.roles, id=799246006645948467)
        embed2 = discord.Embed(title="Success!!!!", description="Announcement created successfully.",
                               colour=discord.Color.blue())
        embed2.set_footer(text="NightMC bot made by TME#7107",
                          icon_url="https://cdn.discordapp.com/attachments/783224139800510524/786634170779697152/Nightmc_Bot-Logo.png")
        await channel.send(embed=embed)
        await channel.send(announce.mention)
        await message.channel.send(embed=embed2)'''

    if "noice" in message.content:
        await message.add_reaction("<:noice:800639390724522004>")

    if "pog" in message.content:
        await message.add_reaction("<:3797_pogchap_bean:801379422187552788>")

    await client.process_commands(message)

    if ":" == message.content[0] and ":" == message.content.lower()[-1]:
        emoji_name = message.content[1:-1]
        for emoji in message.guild.emojis:
            if emoji_name == emoji.name:
                await message.channel.send(str(emoji))
                await message.delete()
                break
            else:
                pass

    if "discord.gg" in message.content.lower():
        owner = [707549304382029845, 471306929575034882, 797453600136888351, 552769094693421056, 765825783687282698]
        if message.author.id in owner:
            return

        else:
            await message.channel.purge(limit=1)
            await message.channel.send(
                f'Hey {message.author.mention} :rage: \nYou are not allowed to post discord links on this server!!!!',
                delete_after=5)

    if "https://discord.gg" in message.content.lower():
        owner = [707549304382029845, 471306929575034882, 797453600136888351, 552769094693421056, 765825783687282698]
        if message.author.id in owner:
            return

        else:
            await message.channel.purge(limit=1)
            await message.channel.send(
                f'Hey {message.author.mention} :rage: \nYou are not allowed to post discord links on this server!!!!',
                delete_after=5)

    if "fuck" in message.content.lower():
        await message.channel.purge(limit=1)
        await message.channel.send(
            f'Hey {message.author.mention} :rage: \nYou are not allowed to use bad words on this server because it is a family friendly server...',
            delete_after=5)

    if "shit" in message.content.lower():
        await message.channel.purge(limit=1)
        await message.channel.send(
            f'Hey {message.author.mention} :rage: \nYou are not allowed to say bad words on this server because it is a famuly friendly server!!!!',
            delete_after=5)

    if "fucking" in message.content.lower():
        await message.channel.purge(limit=1)
        await message.channel.send(
            f'Hey {message.author.mention} :rage: \nYou are not allowed to say bad words on this server because it is a famuly friendly server!!!!',
            delete_after=5)

    if "nigga" in message.content.lower():
        await message.channel.purge(limit=1)
        await message.channel.send(
            f'Hey {message.author.mention} :rage: \nYou are not allowed to say bad words on this server',
            delete_after=5)

    if "nigger" in message.content.lower():
        await message.channel.purge(limit=1)
        await message.channel.send(
            f'Hey {message.author.mention} :rage: \nYou are not allowed to say bad words on this server',
            delete_after=5)
    if "niger" in message.content.lower():
        await message.channel.purge(limit=1)
        await message.channel.send(
            f'Hey {message.author.mention} :rage: \nYou are banned for sending the **n** word on the server!!!',
            delete_after=5)

    if "bitch" in message.content.lower():
        await message.channel.purge(limit=1)
        await message.channel.send(
            f'Hey {message.author.mention} :rage: \nYou are not allowed to say bad words on this server because it is a famuly friendly server!!!!',
            delete_after=5)

    if "whore" in message.content.lower():
        await message.channel.purge(limit=1)
        await message.channel.send(
            f'Hey {message.author.mention} :rage: \nYou are not allowed to say bad words on this server because it is a famuly friendly server!!!!',
            delete_after=5)

    if "vagina" in message.content.lower():
        await message.channel.purge(limit=1)
        await message.channel.send(
            f'Hey {message.author.mention} :rage: \nYou are not allowed to say bad words on this server',
            delete_after=5)

    if "penis" in message.content.lower():
        await message.channel.purge(limit=1)
        await message.channel.send(
            f'Hey {message.author.mention} :rage: \nYou are not allowed to say bad words on this server',
            delete_after=5)

    if "testicles" in message.content.lower():
        await message.channel.purge(limit=1)
        await message.channel.send(
            f'Hey {message.author.mention} :rage: \nYou are not allowed to say bad words on this server',
            delete_after=5)

    if "holy shit" in message.content.lower():
        await message.channel.purge(limit=1)
        await message.channel.send(
            f'Hey {message.author.mention} :rage: \nYou are not allowed to say bad words on this server because it is a famuly friendly server!!!!',
            delete_after=5)

    if "dick" in message.content.lower():
        await message.channel.purge(limit=1)
        await message.channel.send(
            f'Hey {message.author.mention} :rage: \nYou are not allowed to say bad words on this server',
            delete_after=5)

    if "pussy" in message.content.lower():
        await message.channel.purge(limit=1)
        await message.channel.send(
            f'Hey {message.author.mention} :rage: \nYou are not allowed to say bad words on this server',
            delete_after=5)

    if "gay" in message.content.lower():
        await message.channel.purge(limit=1)
        await message.channel.send(
            f'Hey {message.author.mention} :rage: \nYou are not allowed to say bad words on this server',
            delete_after=5)

    if "lesbian" in message.content.lower():
        await message.channel.purge(limit=1)
        await message.channel.send(
            f'Hey {message.author.mention} :rage: \nYou are not allowed to say bad words on this server',
            delete_after=5)

    if "shitass" in message.content.lower():
        await message.channel.purge(limit=1)
        await message.channel.send(
            f'Hey {message.author.mention} :rage: \nYou are not allowed to say bad words on this server because it is a famuly friendly server!!!!',
            delete_after=5)

    if "sex" in message.content.lower():
        await message.channel.purge(limit=1)
        await message.channel.send(
            f'Hey {message.author.mention} :rage: \nYou are not allowed to say bad words on this server',
            delete_after=5)

    if "porn" in message.content.lower():
        await message.channel.purge(limit=1)
        await message.channel.send(
            f'Hey {message.author.mention} :rage: \nYou are not allowed to say bad words on this server',
            delete_after=5)

    if "nudes" in message.content.lower():
        await message.channel.purge(limit=1)
        await message.channel.send(
            f'Hey {message.author.mention} :rage: \nYou are not allowed to say bad words on this server',
            delete_after=5)


    else:
        return


@client.event
async def on_reaction_add(reaction, user):
    ChID = '783211257112166412'
    if reaction.message.channel.id != ChID:
        return
    if reaction.emoji == "✅":
        Member = discord.utils.get(user.server.roles, name="Member")
        await client.add_roles(user, Member)



client.run(token)