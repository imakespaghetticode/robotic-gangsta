import discord
from discord.ext import commands
import json

with open("bot.json") as file:
	js = json.load(file)
	token = js["token"]

bot = commands.Bot(command_prefix="rg!")

@bot.command()
async def ping(ctx):
    await ctx.send(str(int(bot.latency * 1000))+ "ms")

@bot.command()
async def invite(ctx):
	await ctx.send("https://bit.ly/2PDuIkc")



bot.run(token)