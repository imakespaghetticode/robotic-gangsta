import discord
from discord.ext import commands


class ownercommands:
    def __init__(self, bot):
        self.bot = bot

# Ping

    @commands.command(hidden=True)
    async def ping(self,ctx):
        await ctx.send(str(int(self.bot.latency*1000))+"ms")

# Kill

    @commands.command(hidden=True)
    @commands.is_owner()
    async def kill(self,ctx):
        await self.bot.close()

def setup(bot):
    bot.add_cog(ownercommands(bot))