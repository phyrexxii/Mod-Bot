import discord
from discord.ext import commands
from discord.ext.commands import Bot
import time
import random
from random import randint
import asyncio
import traceback
import datetime
import sys

bot = commands.Bot(command_prefix = "m.")

class ErrorHandler:

    @bot.event
    async def on_command_error(error, ctx):
        if isinstance(error, commands.CommandNotFound):
            embed = discord.Embed(color = ctx.message.author.color, timestamp = datetime.datetime.utcnow())
            embed.set_author(name = "Error: Command Not Found!", icon_url = ctx.message.author.avatar_url)
            embed.add_field(name = "Command Used: ", value = ctx.message.content)
            embed.add_field(name = "My Commands: ", value = "Type m.help", inline = True)
            embed.set_footer(text="Mod Bot v0.1")
            await ctx.message.delete()
            await ctx.bot.send_message(ctx.message.channel, embed = embed)

        elif isinstance(error, commands.BadArguement):
            embed = discord.Embed(color = ctx.message.author.color, timestamp = datetime.datetime.utcnow())
            embed.set_author(name = "Error: Invalid Input!", icon_url = ctx.message.author.avatar_url)
            embed.add_field(name = "Command Used: ", value = ctx.message.content)
            embed.add_field(name = "My Commands: ", value = "Type m.help", inline = True)
            embed.set_footer(text="Mod Bot v0.1")
            await ctx.message.delete()
            await ctx.bot.send_message(ctx.message.channel, embed = embed)

        elif isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(color = ctx.message.author.color, timestamp = datetime.datetime.utcnow())
            embed.set_author(name = "Error: Missing Permissions!", icon_url = ctx.message.author.avatar_url)
            embed.add_field(name = "Command Used: ", value = ctx.message.content)
            embed.add_field(name = "My Commands: ", value = "Type m.help", inline = True)
            embed.add_field(name = "No Perms: ", value = "You **Can't** Use this command", inline = True)
            embed.set_footer(text="Mod Bot v0.1")
            await ctx.message.delete()
            await ctx.bot.send_message(ctx.message.channel, embed = embed)
	
	elif isinstance (error, commands.BotMissingPermissions):
            embed = discord.Embed(color = ctx.message.author.color, timestamp = datetime.datetime.utcnow())
            embed.set_author(name = "Error: I'm Missing Permissions!", icon_url = ctx.message.author.avatar_url)
            embed.add_field(name = "Command Used: ", value = ctx.message.content)
            embed.add_field(name = "My Commands: ", value = "Type m.help", inline = True)
            embed.add_field(name = "Reinite Me!", value = "[Invite](", inline = True)
            embed.set_footer(text="Mod Bot v0.1")
            await ctx.message.delete()
            await ctx.bot.send_message(ctx.message.channel, embed = embed)
            
        else:
	    #  All other Errors not returned come here... And we can just print the default TraceBack.
	    print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
	    traceback.print_exception(type(error),error,error.__traceback__, file=sys.stderr)
            
            
def setup(bot):
    bot.add_cog(ErrorHandler)

    
