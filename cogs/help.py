import discord
import time
import datetime
import random
from random import randint
from discord.ext import commands
from discord.ext.commands import Bot

bot = commands.Bot(command_prefix = commands.when_mentioned_or ("m."))
bot.remove_command("help")
version = "Mod Bot v0.2"

class help():

    @bot.group(pass_context = True)
    async def help(ctx):
      if ctx.invoked_subcommand is None:
        colour = ''.join([random.choice('0123456789ABCDEF') for x in range(6)])
        colour = int(colour, 16)
        embed = discord.Embed(title = "Mod Bot Help Menu",
                              colour = discord.Colour(value = colour),
                              timestamp = datetime.datetime.utcnow())
        embed.add_field(name = "For Help Using a Command:", value = "Type m.help <command>")
        embed.add_field(name = "General Commands:", value = "`help | ping | botinfo | uptime | count | issue | suggestion`")
        embed.add_field(name = "Utility Commands:", value = "`lockdown | unlock | clear | gbans | serverinfo | roleinfo`")
        embed.add_field(name = "Moderation Commands:", value = "`mute | erunmute | addrole | remrole | dm | warn | ban | kick`")
        embed.set_footer(text="{} | Requested by: {}".format(version, ctx.message.author))
        await ctx.bot.say(embed = embed)

    @help.command(pass_context = True)
    async def ping(ctx):
        colour = ''.join([random.choice('0123456789ABCDEF') for x in range(6)])
        colour = int(colour, 16)
        embed = discord.Embed(colour = discord.Colour(value = colour), timestamp = datetime.datetime.utcnow())
        embed.add_field(name = "Help: ping", value = "Usage: m.ping")
        embed.add_field(name = "Notes:", value = "None", inline = True)
        embed.add_field(name = "Description:", value = "```Check the bots response time```")
        await ctx.bot.say(embed = embed)

    @help.command(pass_context = True)
    async def botinfo(ctx):
        colour = ''.join([random.choice('0123456789ABCDEF') for x in range(6)])
        colour = int(colour, 16)
        embed = discord.Embed(colour = discord.Colour(value = colour), timestamp = datetime.datetime.utcnow())
        embed.add_field(name = "Help: botinfo", value = "Usage: m.botinfo")
        embed.add_field(name = "Notes:", value = "None", inline = True)
        embed.add_field(name = "Description:", value = "```Get Information about the bot```")
        await ctx.bot.say(embed = embed)

    @help.command(pass_context = True)
    async def uptime(ctx):
        colour = ''.join([random.choice('0123456789ABCDEF') for x in range(6)])
        colour = int(colour, 16)
        embed = discord.Embed(colour = discord.Colour(value = colour), timestamp = datetime.datetime.utcnow())
        embed.add_field(name = "Help: uptime", value = "Usage: m.uptime")
        embed.add_field(name = "Notes:", value = "None", inline = True)
        embed.add_field(name = "Description:", value = "```How long the bots been online```")
        await ctx.bot.say(embed = embed)

    @help.command(pass_context = True)
    async def lockdown(ctx):
        colour = ''.join([random.choice('0123456789ABCDEF') for x in range(6)])
        colour = int(colour, 16)
        embed = discord.Embed(colour = discord.Colour(value = colour), timestamp = datetime.datetime.utcnow())
        embed.add_field(name = "Help: lockdown", value = "Usage: m.lockdown")
        embed.add_field(name = "Notes:", value = "None", inline = True)
        embed.add_field(name = "Description:", value = "```Locks down a channel. Admins Only can chat!```")
        await ctx.bot.say(embed = embed)

    @help.command(pass_context = True)
    async def unlock(ctx):
        colour = ''.join([random.choice('0123456789ABCDEF') for x in range(6)])
        colour = int(colour, 16)
        embed = discord.Embed(colour = discord.Colour(value = colour), timestamp = datetime.datetime.utcnow())
        embed.add_field(name = "Help: unlock", value = "Usage: m.unlock")
        embed.add_field(name = "Notes:", value = "None", inline = True)
        embed.add_field(name = "Description:", value = "```Unlocks the channel so everyone can chat!```")
        await ctx.bot.say(embed = embed)

    @help.command(pass_context = True)
    async def clear(ctx):
        colour = ''.join([random.choice('0123456789ABCDEF') for x in range(6)])
        colour = int(colour, 16)
        embed = discord.Embed(colour = discord.Colour(value = colour), timestamp = datetime.datetime.utcnow())
        embed.add_field(name = "Help: clear", value = "Usage: m.clear <2-100>")
        embed.add_field(name = "Notes:", value = "None", inline = True)
        embed.add_field(name = "Description:", value = "```Clears the chat From 2 - 100 Messages```")
        await ctx.bot.say(embed = embed)

    @help.command(pass_context = True)
    async def gbans(ctx):
        colour = ''.join([random.choice('0123456789ABCDEF') for x in range(6)])
        colour = int(colour, 16)
        embed = discord.Embed(colour = discord.Colour(value = colour), timestamp = datetime.datetime.utcnow())
        embed.add_field(name = "Help: gbans", value = "Usage: m.gbans")
        embed.add_field(name = "Notes:", value = "None", inline = True)
        embed.add_field(name = "Description:", value = "```Gets a list of users banned from the server```")
        await ctx.bot.say(embed = embed)

    @help.command(pass_context = True)
    async def serverinfo(ctx):
        colour = ''.join([random.choice('0123456789ABCDEF') for x in range(6)])
        colour = int(colour, 16)
        embed = discord.Embed(colour = discord.Colour(value = colour), timestamp = datetime.datetime.utcnow())
        embed.add_field(name = "Help: serverinfo", value = "Usage: m.serverinfo")
        embed.add_field(name = "Notes:", value = "Detailed Info Soon!", inline = True)
        embed.add_field(name = "Description:", value = "```Shows detailed info about the server```")
        await ctx.bot.say(embed = embed)

    @help.command(pass_context = True)
    async def roleinfo(ctx):
        colour = ''.join([random.choice('0123456789ABCDEF') for x in range(6)])
        colour = int(colour, 16)
        embed = discord.Embed(colour = discord.Colour(value = colour), timestamp = datetime.datetime.utcnow())
        embed.add_field(name = "Help: roleinfo", value = "Usage: m.roleinfo <rolename>")
        embed.add_field(name = "Notes:", value = "Role has to be mentionable to use this", inline = True)
        embed.add_field(name = "Description:", value = "```Gets info about a role```")
        await ctx.bot.say(embed = embed)

    @help.command(pass_context = True)
    async def mute(ctx):
        colour = ''.join([random.choice('0123456789ABCDEF') for x in range(6)])
        colour = int(colour, 16)
        embed = discord.Embed(colour = discord.Colour(value = colour), timestamp = datetime.datetime.utcnow())
        embed.add_field(name = "Help: mute", value = "Usage: m.mute <user> <duration> <reason>")
        embed.add_field(name = "Notes:", value = "30s = 30 seconds, 5m = 5 minutes, etc.", inline = True)
        embed.add_field(name = "Description:", value = "```Mutes a user for a time and duration. This command auto-unmutes after time is up```")
        await ctx.bot.say(embed = embed)

    @help.command(pass_context = True)
    async def erunmute(ctx):
        colour = ''.join([random.choice('0123456789ABCDEF') for x in range(6)])
        colour = int(colour, 16)
        embed = discord.Embed(colour = discord.Colour(value = colour), timestamp = datetime.datetime.utcnow())
        embed.add_field(name = "Help: erunmute", value = "Usage: m.erunmute <user> <reason>")
        embed.add_field(name = "Notes:", value = "None", inline = True)
        embed.add_field(name = "Description:", value = "```Unmuted a user earlier than the muted duration```")
        await ctx.bot.say(embed = embed)

    @help.command(pass_context = True)
    async def addrole(ctx):
        colour = ''.join([random.choice('0123456789ABCDEF') for x in range(6)])
        colour = int(colour, 16)
        embed = discord.Embed(colour = discord.Colour(value = colour), timestamp = datetime.datetime.utcnow())
        embed.add_field(name = "Help: addrole", value = "Usage: m.addrole <rolename> <user>")
        embed.add_field(name = "Notes:", value = "Role does not have to be mentionable", inline = True)
        embed.add_field(name = "Description:", value = "```Adds a role to the specified user```")
        await ctx.bot.say(embed = embed)

    @help.command(pass_context = True)
    async def remrole(ctx):
        colour = ''.join([random.choice('0123456789ABCDEF') for x in range(6)])
        colour = int(colour, 16)
        embed = discord.Embed(colour = discord.Colour(value = colour), timestamp = datetime.datetime.utcnow())
        embed.add_field(name = "Help: remrole", value = "Usage: m.remrole <rolename> <user>")
        embed.add_field(name = "Notes:", value = "Role does not have to be mentionable", inline = True)
        embed.add_field(name = "Description:", value = "```Removes a role for a user```")
        await ctx.bot.say(embed = embed)

    @help.command(pass_context = True)
    async def dm(ctx):
        colour = ''.join([random.choice('0123456789ABCDEF') for x in range(6)])
        colour = int(colour, 16)
        embed = discord.Embed(colour = discord.Colour(value = colour), timestamp = datetime.datetime.utcnow())
        embed.add_field(name = "Help: dm", value = "Usage: m.dm <user> <message>")
        embed.add_field(name = "Notes:", value = "None", inline = True)
        embed.add_field(name = "Description:", value = "```Dms a user a message```")
        await ctx.bot.say(embed = embed)

    @help.command(pass_context = True)
    async def warn(ctx):
        colour = ''.join([random.choice('0123456789ABCDEF') for x in range(6)])
        colour = int(colour, 16)
        embed = discord.Embed(colour = discord.Colour(value = colour), timestamp = datetime.datetime.utcnow())
        embed.add_field(name = "Help: warn", value = "Usage: m.warn <user> <reason>")
        embed.add_field(name = "Notes:", value = "None", inline = True)
        embed.add_field(name = "Description:", value = "```Warns a user with a reason```")
        await ctx.bot.say(embed = embed)

    @help.command(pass_context = True)
    async def ban(ctx):
        colour = ''.join([random.choice('0123456789ABCDEF') for x in range(6)])
        colour = int(colour, 16)
        embed = discord.Embed(colour = discord.Colour(value = colour), timestamp = datetime.datetime.utcnow())
        embed.add_field(name = "Help: ban", value = "Usage: m.ban <member> <reason>")
        embed.add_field(name = "Notes:", value = "None", inline = True)
        embed.add_field(name = "Description:", value = "```Bans a user with a reason```")
        await ctx.bot.say(embed = embed)

    @help.command(pass_context = True)
    async def kick(ctx):
        colour = ''.join([random.choice('0123456789ABCDEF') for x in range(6)])
        colour = int(colour, 16)
        embed = discord.Embed(colour = discord.Colour(value = colour), timestamp = datetime.datetime.utcnow())
        embed.add_field(name = "Help: kick", value = "Usage: m.kick <user> <reason>")
        embed.add_field(name = "Notes:", value = "None", inline = True)
        embed.add_field(name = "Description:", value = "```Kicks a user from the server with a reason```")
        await ctx.bot.say(embed = embed)

    @help.command(pass_context = True)
    async def issue(ctx):
        colour = ''.join([random.choice('0123456789ABCDEF') for x in range(6)])
        colour = int(colour, 16)
        embed = discord.Embed(colour = discord.Colour(value = colour), timestamp = datetime.datetime.utcnow())
        embed.add_field(name = "Help: issue | bug", value = "Usage: m.issue | bug <message>")
        embed.add_field(name = "Notes:", value = "You could use either issue or bug as the command", inline = True)
        embed.add_field(name = "Description:", value = "```Tells me an issue(s) you have with the bot```")
        await ctx.bot.say(embed = embed)

    @help.command(pass_context = True)
    async def suggestion(ctx):
        colour = ''.join([random.choice('0123456789ABCDEF') for x in range(6)])
        colour = int(colour, 16)
        embed = discord.Embed(colour = discord.Colour(value = colour), timestamp = datetime.datetime.utcnow())
        embed.add_field(name = "Help: suggestion | suggest", value = "Usage: m.suggestion | suggest <message>")
        embed.add_field(name = "Notes:", value = "You could use either issue or bug as the command", inline = True)
        embed.add_field(name = "Description:", value = "```Tells me a sugestion about the bot. You can tell me anything, and chances are i might add it to the bot!```")
        await ctx.bot.say(embed = embed)

    @help.command(pass_context = True)
    async def count(ctx):
        colour = ''.join([random.choice('0123456789ABCDEF') for x in range(6)])
        colour = int(colour, 16)
        embed = discord.Embed(colour = discord.Colour(value = colour), timestamp = datetime.datetime.utcnow())
        embed.add_field(name = "Help: count", value = "Usage: m.count")
        embed.add_field(name = "Notes:", value = "None", inline = True)
        embed.add_field(name = "Description:", value = "```Gives You my server/member count```")
        await ctx.bot.say(embed = embed)

def setup(bot):
    bot.add_cog(help)
