import discord
import asyncio
import json
import random
import platform
import markovgen
from helper import is_owner


from discord.ext import commands
from discord import Game

# set config variables
with open("config/config.json") as cfg:
	config = json.load(cfg)

token = config["token"]
phrases = config["phrases"]

# set the bot up
description = """
A bot created by Hemogoblin#2677 made for personal use with friends in private servers.
"""
client = commands.Bot(description=description, command_prefix="$", pm_help = True)

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

@client.event
async def on_message(msg):
	await client.process_commands(msg)

@client.event
async def on_message_edit(old, new):
	await client.process_commands(new)

@client.command(name="quit")
@is_owner()
async def bot_quit():
	await client.say("Shutting down now...")
	await client.logout()

@client.command()
async def ping(*args):
	await client.say(':ping_pong: pong!')

async def random_status():
	await client.wait_until_ready()
	counter = 0
	channel = discord.Object(id='391089813740191745')
	while not client.is_closed:
		phrase = random.choice(phrases)
		game = Game(name=phrase)
		await client.change_presence(game=game)
		await asyncio.sleep(20)

@client.command()
async def quote(*args):
    content = open("tenth_sublevel.txt", 'r')
    markov = markovgen.Markov(content)
    quote = markov.generate_markov()
    await client.say(quote)

client.loop.create_task(random_status())  
client.run(token)

