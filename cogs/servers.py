import discord
import random
import time
import asyncio
import datetime

from discord.ext import commands
from discord.ext.commands import Bot
from random import randint

bot = commands.Bot(commands_prefix = commands.when_mentioned_or ("m."))
version = "Mod Bot v0.1"
logs = discord.Object("401552701835444225")

class Servers():

    @bot.event
    async def on_server_join(server):
        embed = discord.Embed(title="__Joined: {}__".format(server.name), color=0x00ff00, timestamp = datetime.datetime.utcnow())
        embed.add_field(name="Server Name", value=server.name, inline=True)
        embed.add_field(name="Owned By", value=server.owner, inline=True)
        embed.add_field(name="Total Members", value="{0} members".format(server.member_count), inline=True)
        embed.add_field(name="Server Region", value=server.region, inline=True)
        await bot.send_message(logs, embed=embed)

    @bot.event
    async def on_server_remove(server):
        embed = discord.Embed(title="__Removed From: {}__".format(server.name), color=0xff0000, timestamp = datetime.datetime.utcnow())
        embed.add_field(name="Server Name", value=server.name, inline=True)
        embed.add_field(name="Owned By", value=server.owner, inline=True)
        embed.add_field(name="Total Members", value="{0} members".format(server.member_count), inline=True)
        embed.add_field(name="Server Region", value=server.region, inline=True)
        await bot.send_message(logs, embed=embed)
    
def setup(bot):
    bot.add_cog(Servers)
