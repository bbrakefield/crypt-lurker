import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
import platform
import pylast
import markovgen

FM_API_KEY = "1af81fce0edaa08f4405e1d0e67fb5cd"
FM_API_SECRET = "ecfadcd0eceb3427fb757f4d42926fad"
username = "lupine_lvthn"
password_hash = pylast.md5("LUmmTI-2012")
client = Bot(description="Bot created by Hemogoblin#2677", command_prefix="$", pm_help = True)
network = pylast.LastFMNetwork(api_key=FM_API_KEY, api_secret=FM_API_SECRET, username=username, password_hash=password_hash)

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


@client.command()
async def ping(*args):

	await client.say(':ping_pong: pong!')
	
@client.command()
async def quote(*args):

    content = open("tenth_sublevel.txt", 'r')
    markov = markovgen.Markov(content)
    quote = markov.generate_markov()
    await client.say(quote)

@client.command()
async def movepins(*args):
	async for pin in client.pins_from(client.get_channel(391083579171536897)):
		print(pin.content)

@client.command()
async def bandinfo(band: str):
	artist = pylast.Artist(band, network)
	await client.say(artist.get_bio_content())

@client.command(pass_context=True)
async def test(ctx):

	counter = 0
	tmp = await client.say('Calculating messages...')
	async for log in client.logs_from(ctx.message.channel, limit=100):
		if log.author == ctx.message.author:
			counter += 1

	await client.edit_message(tmp, 'You have {} messages.'.format(counter))


    # print(message.author.nick + ': ' + message.content)
    # async for log in client.logs_from(client.get_channel('371774040865505282'), limit=1000):
    # if log.author == message.author:
    #     print(log.content)

    
client.run('MzI4NTEzMzI1MDk0OTI4Mzg0.DRWDWg.8jbuYl18Y0lu_yroR4DKP8seA60')

