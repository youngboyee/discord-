import discord
from discord.ext import commands
import json
import random
import datetime as dt
import pytz
from core.classes import cog_extension
with open('setting.json',mode='r',encoding='utf8') as jfile:
    jdata=json.load(jfile)


class main(cog_extension):
    
    @commands.command()
    async def ping(self,ctx):
        await ctx.send('{0}毫秒'.format(round(self.bot.latency*1000)))

def setup(bot):
    bot.add_cog(main(bot))