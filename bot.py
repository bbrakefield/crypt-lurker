import discord
import asyncio
import json
import platform
import markovgen
from helper import is_owner

from discord.ext.commands import Bot
from discord.ext import commands

# set config variables
with open("config/config.json") as cfg:
	config = json.load(cfg)

token = config["token"]

# set the bot up
description = """
A bot created by Hemogoblin#2677 made for personal use with friends in private servers.
"""
client = Bot(description=description, command_prefix="$", pm_help = True)

@client.event
async def on_ready():
	print('Logged in as '+ client.user.name + ' ID:' + client.user.id)
	print('Currently connected to ' + str(len(client.servers)) + ' servers.')
	print('Currently connected to ' + str(len(set(client.get_all_members())))	+ ' users.')
	print('--------')
	print('To invite {}:'.format(client.user.name))
	print('https://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions=8'.format(client.user.id))
	print('--------')
	print('Created by Hemogoblin#2677')

@client.command(name="quit")
@is_owner()
async def bot_quit():
	await client.say("Shutting down now...")
	await client.logout()

@client.command()
async def ping(*args):

	await client.say(':ping_pong: pong!')
	
@client.command()
async def quote(*args):

    content = open("tenth_sublevel.txt", 'r')
    markov = markovgen.Markov(content)
    quote = markov.generate_markov()
    await client.say(quote)
    
client.run(token)

