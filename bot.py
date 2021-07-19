import discord
from discord.ext import commands
import os
import random
import time
from discord.ext.commands.converter import CategoryChannelConverter
import requests as request
import requests
import shutil
from random import choice
import datetime
import time
import discord.utils
from prsaw import RandomStuff
import aiohttp
import urllib.parse

from requests.sessions import merge_setting
# simple bot stuff
client = commands.Bot(command_prefix = "c-")
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.do_not_disturb)
    print("Bot is ready!")
client.remove_command('help')

# join msg
@client.event
async def on_guild_join(guild):
    for channel in guild.text_channels:
        if channel.permissions_for(guild.me).send_messages:
            embed = discord.Embed(colour=discord.Colour(16553790))
            embed.set_thumbnail(url="https://media.discordapp.net/attachments/597238107368194048/847688002019917834/Untitled_8.png?width=474&height=415")
            embed.add_field(name="Hey im Cryto!", value="My prefix is c-", inline=False)
            embed.add_field(name="What can I do?", value="I have fun commands to enhance your servers experience.", inline=False)
            await channel.send(embed=embed)
        break

# purge messages
@client.command()
@commands.has_permissions(administrator=True)
async def purge(ctx, amount : int):
    await ctx.channel.purge(limit=amount)
    await ctx.reply('Finished purging messages!')

# say whatever you want
@client.command()
async def say(ctx, *, value):
    message = ctx.message
    await ctx.send(f"{value}")
    await message.delete()


# no help for u
@client.command()
async def help(ctx):
    await ctx.reply("no")

# wikihow fun
@client.command()
async def how(ctx):
	# Text
	url_stp = "https://hargrimm-wikihow-v1.p.rapidapi.com/steps"

	querystring_stp = {"count":"1"}

	headers_stp = {
		'x-rapidapi-key': "eaf4158a20mshc3efd011f75e721p1b838cjsn92d8c4821791",
		'x-rapidapi-host': "hargrimm-wikihow-v1.p.rapidapi.com"
		}

	rs = request.request("GET", url_stp, headers=headers_stp, params=querystring_stp)
	bs = rs.json()["1"]

	# Image
	url_img = "https://hargrimm-wikihow-v1.p.rapidapi.com/images"

	querystring_img = {"count":"1"}
	
	headers_img = {
		'x-rapidapi-key': "eaf4158a20mshc3efd011f75e721p1b838cjsn92d8c4821791",
		'x-rapidapi-host': "hargrimm-wikihow-v1.p.rapidapi.com"
		}

	r = request.request("GET", url_img, headers=headers_img, params=querystring_img)
	b = r.json()["1"]

	if r.status_code == 200:
		try:
			embed = discord.Embed(title=bs, color=discord.Colour(16553790))
			embed.set_image(url=b)
			await ctx.send(embed=embed)
		except:
			await ctx.send("Something went wrong, please go scream at the devs <@597205813055979522>!")


# suicide help
@client.command()
async def suicide(ctx):
    embed = discord.Embed(title="Suicide prevention.", colour=discord.Colour(0xf67aff))
    embed.set_thumbnail(url="https://media4.giphy.com/media/3ohs4Bj2OPOGcKn9Ic/giphy.gif")
    embed.set_footer(text="Please know that you arent alone, people can help you.")
    embed.add_field(name="__USA Suicide Prevention Hotline.__", value="1-800-273-8255", inline=False)
    embed.add_field(name="__If you arent from the USA__", value="https://www.opencounseling.com/suicide-hotlines", inline=False)
    await ctx.send(embed=embed)

# get bot ping
@client.command()
async def ping(ctx):
    await ctx.reply(f'{round(client.latency * 1000)}ms ping!')

# 8 ball
@client.command()
async def m8b(ctx, question):
    responses = ['As I see it, yes.',
             'Yes.',
             'Positive',
             'From my point of view, yes',
             'Convinced.',
             'Most Likley.',
             'Chances High',
             'No.',
             'Negative.',
             'Not Convinced.',
             'Perhaps.',
             'Not Sure',
             'Maybe',
             'I cannot predict now.',
             'Im to lazy to predict.',
             'I am tired. *proceeds with sleeping*']
    response = random.choice(responses)
    embed=discord.Embed(title="The magic 8 ball has spoken!", colour=discord.Colour(16553790), description= f'{response}')
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/597238107368194048/847688002019917834/Untitled_8.png?width=773&height=676")
    await ctx.reply(embed=embed, mention_author=False)

# Coinflip
determine_flip = [1, 0]

@client.command()
async def cf(ctx):
    if random.choice(determine_flip) == 1:
        embed = discord.Embed(title="Coinflip", description=f"{ctx.author.mention} Flipped a coin, it landed on **Heads**!", colour=discord.Colour(16553790))
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/597238107368194048/847944298086793286/Untitled_11.png?width=731&height=676")
        await ctx.send(embed=embed)

    else:
        embed = discord.Embed(title="Coinflip", description=f"{ctx.author.mention} Flipped a coin, it landed on **Tails**!", colour=discord.Colour(16553790))
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/597238107368194048/847944316861153280/Untitled_10.png?width=731&height=676")
        await ctx.send(embed=embed)

# Ban
@commands.has_permissions(ban_members=True)
@client.command()
async def ban(ctx, user: discord.Member, *, reason="No reason provided"):
        await user.ban(reason=reason)
        ban = discord.Embed(title=f" {user.name} has been banned!", description=f"Reason: {reason}\nBy: {ctx.author.mention}", colour=discord.Colour(16553790), timestamp = datetime.datetime.utcnow())
        ban.set_thumbnail(url="https://media.discordapp.net/attachments/597238107368194048/847946172958244874/Untitled_12.png?width=731&height=676")
        await ctx.message.delete()
        await ctx.channel.send(embed=ban)
        await user.send(embed=ban)

# Kick
@commands.has_permissions(kick_members=True)
@client.command()
async def kick(ctx, user: discord.Member, *, reason="No reason provided"):
        await user.kick(reason=reason)
        kick = discord.Embed(title=f" {user.name} has been kicked!", description=f"Reason: {reason}\nBy: {ctx.author.mention}", colour=discord.Colour(16553790), timestamp = datetime.datetime.utcnow())
        kick.set_thumbnail(url="https://media.discordapp.net/attachments/597238107368194048/847946172958244874/Untitled_12.png?width=731&height=676")
        await ctx.message.delete()
        await ctx.channel.send(embed=kick)
        await user.send(embed=kick)

################################################################################################################
############################################ <!> COMMANDS LIST <!> #############################################
################################################################################################################



@client.command()
# commands list
async def cmds(ctx):
	embed=discord.Embed(title="Commands List", colour=discord.Colour(16553790))
	embed.set_thumbnail(url="https://media.discordapp.net/attachments/597238107368194048/847688002019917834/Untitled_8.png?width=639&height=559")
	embed.add_field(name="c-cmds", value="Command to show this message.", inline=True)
	embed.add_field(name="c-ping", value="Get the bots ping.", inline=True)
	embed.add_field(name="c-suicide", value="Suicide prevention methods.", inline=True)
	embed.add_field(name="c-cf", value="Flip a coin.", inline=True)
	embed.add_field(name="c-m8b", value="Ask the magic 8 ball a question.", inline=True)
	embed.add_field(name="c-how", value="Generate a random wikihow.", inline=True)
	embed.add_field(name="c-say", value="Make the bot say something.", inline=True)
	embed.add_field(name="c-purge | admin only", value="Removes a specified amount of messages.", inline=True)
	embed.add_field(name="c-ban | admin only", value="Bans the specified user.", inline=True)
	embed.add_field(name="c-kick | admin only", value="kicks the specified user.", inline=True)
	embed.set_footer(text="Developed by Fire#4567", icon_url="https://media.discordapp.net/attachments/597238107368194048/847946172958244874/Untitled_12.png?width=604&height=559")
	await ctx.send(embed=embed)


################################################################################################################
############################################ <!> ERROR MESSAGES <!> ############################################
################################################################################################################

@client.event
async def on_command_error(ctx, error):
			embed = discord.Embed(title="Command Error.", colour=discord.Colour(16553790), description= f"{str(error)}")
			embed.set_thumbnail(url = "https://media.discordapp.net/attachments/597238107368194048/847687991983734824/Untitled_4.png?width=432&height=400")
			await ctx.reply(embed=embed)



client.run('')