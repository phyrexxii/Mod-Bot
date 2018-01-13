import discord
from discord.ext import commands
from discord.ext.commands import Bot
import random
from random import randint
import time
import asyncio
import time
import datetime

bot = commands.Bot(commands_prefix = "m.")

version = "Mod Bot v0.1"

class Admin():

    @bot.command(pass_context = True)
    async def lockdown(ctx):
        """Locks down the channel (Only Admins May Speak)"""
        user_roles = [r.name.lower() for r in ctx.message.author.roles]
        if "admin" in user_roles:
            try:
                overwrites_everyone = ctx.message.channel.overwrites_for(ctx.message.server.default_role)
                if overwrites_everyone.send_messages == False:
                    await ctx.bot.say("Channel is already locked down. Use `m.unlock` to unlock.")
                    return
                overwrites_everyone.send_messages = False
                await ctx.bot.edit_channel_permissions(ctx.message.channel, ctx.message.server.default_role, overwrites_everyone)
                await ctx.bot.say("Channel Is Locked :lock:. Only Admins May Speak. Do Not Talk about It In Other Channels!")
#                await ctx.bot.delete_message(ctx.message)

            except discord.errors.Forbidden:
                await ctx.bot.say("I'm Missing `Permissions`. **Please Reivite Me** [Here](https://goo.gl/j2JrMt)")
        else:
            msg = ':eyes: | {} Tried to use `lockdown` | ID: {}'.format(ctx.message.author, ctx.message.author.id)
            await ctx.bot.send_message(discord.utils.get(ctx.message.server.channels, name="logs"), msg)
            await ctx.bot.say(":x: | Admin Only! | Action has been logged! :page_facing_up:")

    @bot.command(pass_context = True)
    async def unlock(ctx):
        """Unlocks the channel (Admins Only)"""
        user_roles = [r.name.lower() for r in ctx.message.author.roles]

        if "admin" in user_roles:
            try:
                overwrites_everyone = ctx.message.channel.overwrites_for(ctx.message.server.default_role)
                overwrites_staff = ctx.message.channel.overwrites_for(discord.utils.get(ctx.message.server.roles, name="Admin"))
                if overwrites_everyone.send_messages == None:
                    await ctx.bot.say("Channel is already unlocked.")
                    return
                overwrites_everyone.send_messages = None
                overwrites_staff.send_messages = True
                await ctx.bot.edit_channel_permissions(ctx.message.channel, ctx.message.server.default_role, overwrites_everyone)
                await ctx.bot.edit_channel_permissions(ctx.message.channel, discord.utils.get(ctx.message.server.roles, name="Admin"), overwrites_staff)
                await ctx.bot.say("Channel unlocked. :unlock:")
#                await ctx.bot.delete_message(ctx.message)
            except discord.errors.Forbidden:
                await ctx.bot.say("I'm Missing `Permissions`. **Please Reivite Me** [Here](https://goo.gl/j2JrMt)")
        else:
            msg = ':eyes: | {} Tried to use `unlock` | ID: {}'.format(ctx.message.author, ctx.message.author.id)
            await ctx.bot.send_message(discord.utils.get(ctx.message.server.channels, name="logs"), msg)
            await ctx.bot.say(":x: | Admin Only! | Action has been logged! :page_facing_up:")

    @bot.command(pass_context = True)
    async def kick(ctx, member : discord.Member = None, *, reason = ""):
        '''Kick a user from the server with a reason'''
        user_roles = [r.name.lower() for r in ctx.message.author.roles]

        if "admin" in user_roles:
            if member == None:
                await ctx.bot.say(":x: | Specify a user to `Kick`")

            if reason == "":
                await ctx.bot.say(":x: | You need a `Reason`")
            else:
                embed = discord.Embed(description = "{} was kicked.".format(member.name), color = 0xF00000)
                embed.add_field(name = "Reason: ", value = reason)
                embed.add_field(name="Moderator:", value=ctx.message.author, inline = True)
                embed.set_footer(text = "{} | Kicked by: {}".format(version, ctx.message.author))
                await ctx.bot.kick(member)
                await ctx.bot.say(embed = embed)
#                await ctx.bot.delete_message(ctx.message)
                await ctx.bot.send_message(discord.utils.get(ctx.message.server.channels, name="logs"), embed = embed)

        else:
            msg = ':eyes: | {} Tried to use `kick` | ID: {}'.format(ctx.message.author, ctx.message.author.id)
            await ctx.bot.send_message(discord.utils.get(ctx.message.server.channels, name="logs"), msg)
            await ctx.bot.say(":x: | Admin Only! | Action has been logged! :page_facing_up:")

    @bot.command(pass_context=True)
    async def clear(ctx, number):
        '''Clears The Chat 2-100'''
        user_roles = [r.name.lower() for r in ctx.message.author.roles]

        if "admin" in user_roles:
            mgs = []
            number = int(number)
            async for x in ctx.bot.logs_from(ctx.message.channel, limit = number):
                mgs.append(x)
            await ctx.bot.delete_messages(mgs)
        else:
            msg = ':eyes: | {} Tried to use `clear` | ID: {}'.format(ctx.message.author, ctx.message.author.id)
            await ctx.bot.send_message(discord.utils.get(ctx.message.server.channels, name="logs"), msg)
            await ctx.bot.say(":x: | Admin Only! | Action has been logged! :page_facing_up:")

    @bot.command(pass_context = True)
    async def mute(ctx, member: discord.Member = None, duration = None, *,reason = ""):
        """Mutes a user with a duration and auto unmute! (Admin Only)"""
        user_roles = [r.name.lower() for r in ctx.message.author.roles]

        if "admin" in user_roles:
            if member == None:
                await ctx.bot.say(":x: | Specify a `User` to `Mute`")
            if duration == None:
                await ctx.bot.say(":x: | Missing a `Duration` for the `Mute`")
            if reason == "":
                await ctx.bot.say(":x: | Missing a `Reason` to `Mute`")

            unit = duration[-1]
            if unit == 's':
                time = int(duration[:-1])
                longunit = 'seconds'
            elif unit == 'm':
                time = int(duration[:-1]) * 60
                longunit = 'minutes'
            elif unit == 'h':
                time = int(duration[:-1]) * 60 * 60
                longunit = 'hours'
            else:
                await ctx.bot.say('Invalid Unit! Use `s`, `m`, or `h`.')
                return
            progress = await ctx.bot.say(":timer: | User will be `Muted` shortly")

            try:
                for channel in [c for c in ctx.message.server.channels if c.type == discord.ChannelType.text]:
                    await ctx.bot.edit_channel_permissions(channel, member, overwrite=discord.PermissionOverwrite(send_messages = False))
                for channel in [c for c in ctx.message.server.channels if c.type == discord.ChannelType.voice]:
                    await ctx.bot.edit_channel_permissions(channel, member, overwrite=discord.PermissionOverwrite(speak = False))
            except:
                pass

            color = ''.join([random.choice('0123456789ABCDEF') for x in range(6)])
            color = int(color, 16)
            embed = discord.Embed(description = "__**User Mute**__", colour=discord.Colour(value=color), timestamp = datetime.datetime.utcnow())
            embed.add_field(name = "Muted", value = member)
            embed.add_field(name = "Duration: ", value = duration, inline = True)
            embed.add_field(name = "Reason: ", value = reason, inline = True)
            embed.set_footer(text = version)
            await ctx.bot.delete_message(progress)
            await ctx.bot.say(embed = embed)
#            await ctx.bot.delete_message(ctx.message)
            await ctx.bot.send_message(discord.utils.get(ctx.message.server.channels, name="logs"), embed = embed)
            await asyncio.sleep(time)

            try:
                for channel in [c for c in ctx.message.server.channels if c.type == discord.ChannelType.text]:
                    await ctx.bot.edit_channel_permissions(channel, member, overwrite=discord.PermissionOverwrite(send_messages = True))
                for channel in [c for c in ctx.message.server.channels if c.type == discord.ChannelType.voice]:
                    await ctx.bot.edit_channel_permissions(channel, member, overwrite=discord.PermissionOverwrite(speak = True))
            except:
                pass

            color = ''.join([random.choice('0123456789ABCDEF') for x in range(6)])
            color = int(color, 16)
            embed = discord.Embed(description = "__**Times Up! | Unmute**__", colour=discord.Colour(value=color), timestamp = datetime.datetime.utcnow())
            embed.add_field(name = "User: ", value = member)
            embed.set_footer(text = "{} | Muted by: {}".format(version, ctx.message.author))
            await ctx.bot.say(embed = embed)
            await ctx.bot.send_message(discord.utils.get(ctx.message.server.channels, name="logs"), embed = embed)
    
        else:
            msg = ':eyes: | {} Tried to use `mute` | ID: {}'.format(ctx.message.author, ctx.message.author.id)
            await ctx.bot.send_message(discord.utils.get(ctx.message.server.channels, name="logs"), msg)
            await ctx.bot.say(":x: | Admin Only! | Action has been logged! :page_facing_up:")
        

    @bot.command(pass_context = True)
    async def erunmute(ctx, member: discord.Member = None, *, reason = ""):
        """This unmutes a user earlier than the muted duration (Admin Only)"""
        user_roles = [r.name.lower() for r in ctx.message.author.roles]

        if "admin" in user_roles:
            if member == None:
                await ctx.bot.say("{} Specify a `User` to `Unmute`".format(ctx.message.author.mention))
            if reason == "":
                await ctx.bot.say("{} Missing a `Reason` to `Unmute`".format(ctx.message.author.mention))

            progress = await ctx.bot.say(":timer: | User will be `Unmuted` shortly")

            try:
                for channel in [c for c in ctx.message.server.channels if c.type == discord.ChannelType.text]:
                    await ctx.bot.edit_channel_permissions(channel, member, overwrite=discord.PermissionOverwrite(send_messages = True))
                for channel in [c for c in ctx.message.server.channels if c.type == discord.ChannelType.voice]:
                    await ctx.bot.edit_channel_permissions(channel, member, overwrite=discord.PermissionOverwrite(speak = True))
            except:
                pass

            color = ''.join([random.choice('0123456789ABCDEF') for x in range(6)])
            color = int(color, 16)
            embed = discord.Embed(description = "__**Early Unmute**__", colour=discord.Colour(value=color), timestamp = datetime.datetime.utcnow())
            embed.add_field(name = "Member: ", value = member)
            embed.add_field(name = "Reason For Early Unmute: ", value = reason)
            embed.set_footer(text = "{} | Unmuted by: {}".format(version, ctx.message.author))
            await ctx.bot.delete_message(progress)
            await ctx.bot.say(embed = embed)
#            await ctx.bot.delete_message(ctx.message)
            await ctx.bot.send_message(discord.utils.get(ctx.message.server.channels, name="logs"), embed = embed)
        else:
            msg = ':eyes: | {} Tried to use `erunmute` | ID: {}'.format(ctx.message.author, ctx.message.author.id)
            await ctx.bot.send_message(discord.utils.get(ctx.message.server.channels, name="logs"), msg)
            await ctx.bot.say(":x: | Admin Only! | Action has been logged! :page_facing_up:")

    @bot.command(pass_context = True)
    async def dm(ctx, user : discord.Member = None, *, message : str = None):
        '''Dm a User (Admin Only)'''
        user_roles = [r.name.lower() for r in ctx.message.author.roles]

        if "admin" in user_roles:
            if user is None:
                return await ctx.bot.say(":x: | Please specify a **Member** to **__DM__**")
            if message is None:
                return await ctx.bot.say(":x: | You must have a **Message**")
            else:
                color = ''.join([random.choice('0123456789ABCDEF') for x in range(6)])
                color = int(color, 16)
                embed=discord.Embed(title="Moderator Message", description="Do not reply we will not recieve the message", colour=discord.Colour(value=color), timestamp = datetime.datetime.utcnow())
                embed.add_field(name="Message:", value = message, inline = False)
                embed.set_footer(text = version)
                await ctx.message.delete()
                await ctx.bot.send_message(user, embed=embed)
#                await ctx.bot.delete_message(ctx.message)
                await ctx.bot.say(":white_check_mark: | User Has Been Msg'd")
        else:
            msg = ':eyes: | {} Tried to use `dm` | ID: {}'.format(ctx.message.author, ctx.message.author.id)
            await ctx.bot.send_message(discord.utils.get(ctx.message.server.channels, name="logs"), msg)
            await ctx.bot.say(":x: | Admin Only! | Action has been logged! :page_facing_up:")

    @bot.command(pass_context = True)
    async def warn(ctx, member: discord.Member = None, *, reason = ""):
        '''Warn a user with a reason (Admin Only)'''
        user_roles = [r.name.lower() for r in ctx.message.author.roles]

        if "admin" in user_roles:
            if member == None:
                await ctx.bot.say(":x: | Please specify a `Member` to `Warn`")
            if reason == "":
                await ctx.bot.say(":x: | You must `Provide` a `Reason`")

            else:
                color = ''.join([random.choice('0123456789ABCDEF') for x in range(6)])
                color = int(color, 16)
                embed = discord.Embed(title = "__**Warning**__", colour=discord.Colour(value=color), timestamp = datetime.datetime.utcnow())
                embed.add_field(name = "User: ", value = member, inline = True)
                embed.add_field(name="UserID: ", value = member.id, inline = True)
                embed.add_field(name="Reason: ", value = reason, inline = True)
                embed.add_field(name="Moderator:", value=ctx.message.author, inline=False)
                embed.set_footer(text= "{} | Warned by: {}".format(version, ctx.message.author))
                await ctx.bot.say(embed = embed)
                await ctx.bot.send_message(discord.utils.get(ctx.message.server.channels, name="logs"), embed = embed)
#                await ctx.bot.delete_message(ctx.message)
        else:
            msg = ':eyes: | {} Tried to use `warn` | ID: {}'.format(ctx.message.author, ctx.message.author.id)
            await ctx.bot.send_message(discord.utils.get(ctx.message.server.channels, name="logs"), msg)
            await ctx.bot.say(":x: | Admin Only! | Action has been logged! :page_facing_up:")

    @bot.command(pass_context = True)
    async def addrole(ctx, rolename, user: discord.Member = None):
        """Gives a user a role (Admin Only)"""
        user_roles = [r.name.lower() for r in ctx.message.author.roles]

        if "admin" in user_roles:
            author = ctx.message.author
            channel = ctx.message.channel
            server = ctx.message.server
            role = discord.utils.find(lambda r: r.name.lower() == rolename.lower(), ctx.message.server.roles)

            if user is None:
                await ctx.bot.say(":x: | Role not found!")

            if not channel.permissions_for(server.me).manage_roles:
                await ctx.bot.say("I dont have `manage_roles`.")
            else:
                await ctx.bot.add_roles(user, role)
                await ctx.bot.say("Added role {} to {}".format(role.name, user.name))

        else:
            msg = ':eyes: | {} Tried to use `addrole` | ID: {}'.format(ctx.message.author, ctx.message.author.id)
            await ctx.bot.send_message(discord.utils.get(ctx.message.server.channels, name="logs"), msg)
            await ctx.bot.say(":x: | Admin Only! | Action has been logged! :page_facing_up:")

    @bot.command(pass_context = True)
    async def remrole(ctx, rolename, user: discord.Member = None):
        """Removes the role from the user (Admin Only)"""
        user_roles = [r.name.lower() for r in ctx.message.author.roles]

        if "admin" in user_roles:
            author = ctx.message.author
            channel = ctx.message.channel
            server = ctx.message.server
            role = discord.utils.find(lambda r: r.name.lower() == rolename.lower(), ctx.message.server.roles)

            if user is None:
                await ctx.bot.say(":x: | Role not found!")

            if not channel.permissions_for(server.me).manage_roles:
                await ctx.bot.say("I dont have `manage_roles`.")
            else:
                await ctx.bot.remove_roles(user, role)
                await ctx.bot.say("Removed role {} from {}".format(role.name, user.name))

        else:
            msg = ':eyes: | {} Tried to use `remrole` | ID: {}'.format(ctx.message.author, ctx.message.author.id)
            await ctx.bot.send_message(discord.utils.get(ctx.message.server.channels, name="logs"), msg)
            await ctx.bot.say(":x: | Admin Only! | Action has been logged! :page_facing_up:")

    @bot.command(pass_context = True)
    async def ban(ctx, user: discord.Member = None, *,reason = ""):
        user_roles = [r.name.lower() for r in ctx.message.author.roles]

        if "admin" in user_roles:
            if user == None:
                await ctx.bot.say(":x: | Specify a `User` to `Ban`")
            if reason == "":
                await ctx.bot.say(":x: | Missing a `Reason` to `Ban`")
            else:
                color = ''.join([random.choice('0123456789ABCDEF') for x in range(6)])
                color = int(color, 16)
                embed = discord.Embed(title = "__**User Ban**__", colour=discord.Colour(value=color), timestamp = datetime.datetime.utcnow())
                embed.add_field(name = "User: ", value = reason)
                embed.add_field(name="Moderator:", value=ctx.message.author, inline = True)
                embed.set_footer(text= "{} | Banned by: {}".format(version, ctx.message.author))
                await ctx.bot.say(embed = embed)
                await ctx.bot.send_message(discord.utils.get(ctx.message.server.channels, name="logs"), embed = embed)
                await ctx.bot.ban(user)

        else:
            msg = ':eyes: | {} Tried to use `ban` | ID: {}'.format(ctx.message.author, ctx.message.author.id)
            await ctx.bot.send_message(discord.utils.get(ctx.message.server.channels, name="logs"), msg)
            await ctx.bot.say(":x: | Admin Only! | Action has been logged! :page_facing_up:")
            
    @bot.command(pass_context = True, hidden = True)
    async def setup(ctx):
        user_roles = [r.name.lower() for r in ctx.message.author.roles]

        if "admin" in user_roles:
            server = ctx.message.server

            everyone = discord.PermissionOverwrite(read_messages = False, send_messages = False, read_message_history = False, add_reactions = True)
            mine = discord.PermissionOverwrite(read_messages = True)
        
            progress = await ctx.bot.say("Setting Myself Up! Please Be Patient :timer:")
            await asyncio.sleep(1)
            await ctx.bot.create_channel(server, 'logs', (server.default_role, everyone), (server.me, mine),type = discord.ChannelType.text)
            progress2 = await ctx.bot.say("Successfully Create Channel Named `logs`")
            await asyncio.sleep(2)
            await ctx.bot.delete_message(progress)
            await ctx.bot.delete_message(progress2)
            await ctx.bot.say("Setup Complete! Type `m.help` To View My Commands!")

        else:
            msg = ':eyes: | {} Tried to use `setup` | ID: {}'.format(ctx.message.author, ctx.message.author.id)
            await ctx.bot.send_message(discord.utils.get(ctx.message.server.channels, name="logs"), msg)
            await ctx.bot.say(":x: | Admin Only! | Action has been logged! :page_facing_up:")

def setup(bot):
    bot.add_cog(Admin)
    
