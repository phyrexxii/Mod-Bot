import discord
from discord.ext import commands
from discord.ext.commands import Bot
import time
import random
from random import randint
import datetime
import psutil
import asyncio
import os
import aiohttp

bot = commands.Bot(command_prefix = commands.when_mentioned_or("m."))
tu = datetime.datetime.now()
version = "Mod Bot v0.2"
logs = discord.Object("401552701835444225")
bot.remove_command("help")
errorlogs = discord.Object("414261857524908032")

startup_extensions = ["cogs.admin", "cogs.help", "cogs.botsorgapi"]
adminids = ["221381001476046849", "342853951353520128"]

for extension in startup_extensions:
    try:
        bot.load_extension(extension)
        print(f'{extension} Loaded')
    except Exception as e:
        print(f"Failed to load extention {extension}\n{type(e).__name__}: {e}")

@bot.event
async def on_ready():
    print("===================================")
    print("Logged in as: %s"%bot.user.name)
    print("ID: %s"%bot.user.id)
    print('Server count:', str(len(bot.servers)))
    print('User Count:',len(set(bot.get_all_members())))
    print("Py Lib Version: %s"%discord.__version__)
    print("===================================")
    await bot.change_presence(game=discord.Game(name = "m.help | m.botinfo"))

@bot.command(pass_context=True)
async def ping(ctx):
    """Check The Bots Response Time"""
    t1 = time.perf_counter()
    await bot.send_typing(ctx.message.channel)
    t2 = time.perf_counter()
    thedata = (":ping_pong: **Pong.**\nTime: " + str(round((t2 - t1) * 1000)) + "ms")
    color = ''.join([random.choice('0123456789ABCDEF') for x in range(6)])
    color = int(color, 16)
    data = discord.Embed(description = thedata, colour=discord.Colour(value = color))
    data.set_footer(text="Mod Bot v0.1 | Requested by: {}".format(ctx.message.author))
    await bot.say(embed = data)
    
@bot.command(pass_context = True)
async def userinfo(ctx, member: discord.Member = None):
    if member == None:
        await bot.say(":x: | Please `Mention` A `User`!!")
    else:
        user = member
        ago = (ctx.message.timestamp - user.joined_at).days
        account_ago = (ctx.message.timestamp - user.created_at).days
        colour = ''.join([random.choice('0123456789ABCDEF') for x in range(6)])
        colour = int(colour, 16)
        embed = discord.Embed(colour = discord.Colour(value = colour), timestamp = datetime.datetime.utcnow())
        embed.set_thumbnail(url=member.avatar_url)
        embed.add_field(name="Name:", value=member.name)
        embed.add_field(name="Discriminator:", value='#{}'.format(member.discriminator))
        embed.add_field(name="Nickname:", value=member.nick)
        embed.add_field(name="ID:", value=member.id)
        embed.add_field(name="Status:", value=member.status)
        embed.add_field(name="Game:", value=member.game)
        embed.add_field(name='In Voice', value=member.voice_channel)
        embed.add_field(name="Joined Server:", value="{0}, {1} days ago".format(str(user.joined_at.strftime("%A, %b %d, %Y")), ago))
        embed.add_field(name="Account Created:", value="{0}, {1} days ago".format(str(user.created_at.strftime("%A, %b %d, %Y")), account_ago))
        embed.add_field(name="Roles:", value= ', '.join([r.name for r in sorted(member.roles, key=lambda r: -r.position)]))
        embed.add_field(name='Highest Role', value=member.top_role.name)
        await bot.say(embed = embed)

@bot.command(pass_context = True)
async def gbans(ctx):
    '''Gets A List Of Users Who Are No Longer With us'''
    x = await bot.get_bans(ctx.message.server)
    x = '\n'.join([y.name for y in x])
    embed = discord.Embed(title = "List of The Forgotten", description = x, color = 0xFFFFF)
    embed.set_footer(text="Mod Bot v0.1 | Requested by: {}".format(ctx.message.author))
    return await bot.say(embed = embed)

@bot.command(pass_context=True)
async def serverinfo(ctx):
    """Shows information about the server"""
    server = ctx.message.server
    online = len([m.status for m in server.members
                    if m.status == discord.Status.online or
                    m.status == discord.Status.idle])
    total_users = len(server.members)
    text_channels = len([x for x in server.channels
                            if x.type == discord.ChannelType.text])
    voice_channels = len(server.channels) - text_channels
    passed = (ctx.message.timestamp - server.created_at).days
    created_at = ("Since {}. That's over {} days ago!"
                  "".format(server.created_at.strftime("%d %b %Y %H:%M"), passed))

    colour = ''.join([random.choice('0123456789ABCDEF') for x in range(6)])
    colour = int(colour, 16)
    embed = discord.Embed(description = created_at, colour = discord.Colour(value = colour), timestamp = datetime.datetime.utcnow())
    embed.add_field(name = "Region", value = str(server.region))
    embed.add_field(name = "Users Online", value = "{}/{}".format(online, total_users))
    embed.add_field(name = "Text Channels", value = text_channels)
    embed.add_field(name = "Voice Channels", value = voice_channels)
    embed.add_field(name = "Roles", value = len(server.roles))
    embed.add_field(name = "Owner", value = str(server.owner))
    embed.set_footer(text = "Server ID: " + server.id)
    embed.add_field(name = "AFK Timeout", value = "{} minutes".format(server.afk_timeout/60).replace(".0", ""))
    embed.add_field(name = "AFK Channel", value = str(server.afk_channel))
    embed.add_field(name = "Verification Level", value = str(server.verification_level))
    embed.set_footer(text= "{} | Requested by: {}".format(version, ctx.message.author))

    if server.icon_url:
        embed.set_author(name = server.name, url = server.icon_url)
        embed.set_thumbnail(url = server.icon_url)
    else:
        embed.set_author(name=server.name)

    await bot.say(embed = embed)

@bot.command(pass_context = True)
async def uptime(ctx):
    """Check bot uptime."""
    global tu
    colour = ''.join([random.choice('0123456789ABCDEF') for x in range(6)])
    colour = int(colour, 16)
    embed = discord.Embed(colour = discord.Colour(value = colour), timestamp = datetime.datetime.utcnow())
    embed.add_field(name = "__**My Current Uptime :**__",value = (timedelta_str(datetime.datetime.now() - tu)))
    embed.set_footer(text= "{} | Requested by: {}".format(version, ctx.message.author))
    await bot.say(embed = embed)

#Convert uptime to a string.
def timedelta_str(dt):
    days = dt.days
    hours, r = divmod(dt.seconds, 3600)
    minutes, sec = divmod(r, 60)

    if minutes == 1 and sec == 1:
        return '{0} days, {1} hours, {2} minute and {3} second.'.format(days,hours,minutes,sec)
    elif minutes > 1 and sec == 1:
        return '{0} days, {1} hours, {2} minutes and {3} second.'.format(days,hours,minutes,sec)
    elif minutes == 1 and sec > 1:
        return '{0} days, {1} hours, {2} minute and {3} seconds.'.format(days,hours,minutes,sec)
    else:
        return '{0} days, {1} hours, {2} minutes and {3} seconds.'.format(days,hours,minutes,sec)

@bot.command(pass_context = True)
async def botinfo(ctx):
    """Get Info About The Bot"""
    colour = ''.join([random.choice('0123456789ABCDEF') for x in range(6)])
    colour = int(colour, 16)
    embed = discord.Embed(colour = discord.Colour(value = colour), timestamp = datetime.datetime.utcnow())
    embed.add_field(name='Bot Info', value = "I'm made with the library Discord.py Async."
                    " I'm developed by Shutdown.py#2406. "
                    "If you need any help with me, Join my [devs' server](https://discord.gg/X4CJdEM)."
                    "Send feedback using the feedback command")
    embed.add_field(name='Total Commands', value=(len(bot.commands)))
    embed.add_field(name = 'Invite Me!', value = '[Invite](https://discordbots.org/bot/399115688792424448)')
    embed.set_footer(text= "{} | Requested by: {} at".format(version, ctx.message.author))
    await bot.say(embed = embed)

@bot.command(pass_context=True)
async def count(ctx):
    """The amout of users/servers im in"""
    users = len(set(bot.get_all_members()))
    servers = len(bot.servers)

    colour = ''.join([random.choice('0123456789ABCDEF') for x in range(6)])
    colour = int(colour, 16)
    embed = discord.Embed(colour = discord.Colour(value = colour), timestamp = datetime.datetime.utcnow())
    embed.add_field(name = "Servers im Modding: ", value = servers)
    embed.add_field(name = "Users im Serving: ",value = users)
    embed.add_field(name = "Add me: ", value = "Type m.botinfo")
    embed.set_footer(text= "{} | Requested by: {} at".format(version, ctx.message.author))
    await bot.say(embed = embed)

@bot.command(pass_context=True)
async def roleinfo(ctx, *,role: discord.Role = None):
    """Info about a role"""
    if role == None:
        await bot.say(":x: | Role not found")
    else:
        colour = ''.join([random.choice('0123456789ABCDEF') for x in range(6)])
        colour = int(colour, 16)
        embed = discord.Embed(colour = discord.Colour(value = colour), timestamp = datetime.datetime.utcnow())
        embed.add_field(name = "Role Name", value = format(role.name))
        embed.add_field(name = "Role ID", value = format(role.id))
        embed.add_field(name = "For Server", value = format(role.server))
        embed.add_field(name = "Hoist", value = format(role.hoist))
        embed.add_field(name = "Role Position", value = format(role.position))
        embed.add_field(name = "Mentionable Role", value = format(role.mentionable))
        embed.add_field(name = "Role Created At", value = format(role.created_at))
        embed.set_footer(text= "{} | Requested by: {} at".format(version, ctx.message.author))
        await bot.say(embed = embed)
        
@bot.command(hidden = True, aliases=['about'])
async def info():
        RAM = psutil.virtual_memory()
        used = RAM.used >> 20
        percent = RAM.percent
        CPU  = psutil.cpu_percent()
        embed = discord.Embed(title="Info")
        embed.add_field(name="Memory", value=f'{percent}% ({used}MB)')
        embed.add_field(name="CPU", value=f"{CPU}%")
        await bot.say(embed=embed)
        
@bot.command(pass_context=True, hidden = True)
async def ores(ctx, user: discord.User, *, response):
  if message.owner.id in adminids:
    em = discord.Embed(title="Dev team answer!", description="Your issue has been responded to", timestamp = datetime.datetime.utcnow())
    em.add_field(name = "Answered by {}:".format(ctx.message.author), value=response)
    await bot.send_message(userl, embed=em)
  else:
    return

@bot.event
async def on_server_join(server):
    embed = discord.Embed(title="__Joined: {}__".format(server.name), color=0x00ff00, timestamp = datetime.datetime.utcnow())
    embed.add_field(name="Owned By", value=server.owner, inline=True)
    embed.add_field(name="Total Members", value="{0} members".format(server.member_count), inline=True)
    embed.add_field(name="Server Region", value=server.region, inline=True)
    await bot.send_message(logs, embed=embed)

@bot.event
async def on_server_remove(server):
    embed = discord.Embed(title="__Removed From: {}__".format(server.name), color=0xff0000, timestamp = datetime.datetime.utcnow())
    embed.add_field(name="Owned By", value=server.owner, inline=True)
    embed.add_field(name="Total Members", value="{0} members".format(server.member_count), inline=True)
    embed.add_field(name="Server Region", value=server.region, inline=True)
    await bot.send_message(logs, embed=embed)
    
@bot.event
async def on_command_error(error, ctx):
    if isinstance(error, commands.CommandNotFound):
        return
    else:
        embed = discord.Embed(title=":warning: Error!", description="Command Error: `{}{}`\n`{}`: ```{}```".format(ctx.prefix, ctx.command, type(error).__name__, error), color=0xff0000)
        embed.set_footer(text=ctx.message.author, icon_url=ctx.message.author.avatar_url)
        embed.set_author(name=ctx.message.server.name, icon_url=ctx.message.server.icon_url)
        await bot.send_message(ctx.message.channel, embed= embed)
        await bot.send_message(errorlogs, embed= embed)

if not os.environ.get('TOKEN'):
        print("No Token Found")
bot.run(os.environ.get('TOKEN').strip('\"'))
