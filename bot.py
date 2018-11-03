import discord
from discord.ext import commands
import json
import glob

with open("bot.json") as file:
	js = json.load(file)
	token = js["token"]

bot = commands.Bot(command_prefix="rg!")

# Cogs

def getCogs():
    for i in list(map(lambda p: p.replace('\\','.').replace('/','.')[:-3], glob.glob("cogs/*.py"))):
        yield i

def loadCogs():
    for i in getCogs():
        bot.load_extension(i)


def unloadCogs():
    for i in getCogs():
        bot.unload_extension(i)

# Event

@bot.event
async def on_ready():
	gamestat = discord.Activity(name="rg!help",type=discord.ActivityType.playing)
	await bot.change_presence(activity=gamestat)
	loadCogs()
	print("Bot ready")

# Invite command

@bot.command()
async def invite(ctx):
	await ctx.send("https://bit.ly/2PDuIkc")

# Website command

@bot.command()
async def website(ctx):
	await ctx.send("http://roboticgangsta.surge.sh")

# Github command

@bot.command()
async def github(ctx):
	await ctx.send("support the bot by visiting its github page: https://github.com/imakespaghetticode/robotic-gangsta")

# Reload cogs

@bot.command(hidden=True)
@commands.is_owner()
async def reload(ctx):
    unloadCogs()
    loadCogs()
    await ctx.send("Done")

bot.run(token)