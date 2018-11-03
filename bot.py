import discord
from discord.ext import commands
import json

with open("bot.json") as file:
	js = json.load(file)
	token = js["token"]

bot = commands.Bot(command_prefix="rg!")

@bot.event
async def on_ready():
	print("Bot ready")


# Ping command

@bot.command()
async def ping(ctx):
    await ctx.send(str(int(bot.latency * 1000))+ "ms")

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



bot.run(token)