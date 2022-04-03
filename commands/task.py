import discord
from discord.ext import commands
import json
import asyncio
import random
import datetime as dt
import pytz
from core.classes import cog_extension

with open('setting.json',mode='r',encoding='utf8') as jfile:
    jdata=json.load(jfile)

class task(cog_extension):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        async def interval():#間格執行
            await self.bot.wait_until_ready()
            self.channel=self.bot.get_channel(848189292467191860)
            while not self.bot.is_closed():#bot沒關就會一直執行
                await self.channel.send('I am running')
                await asyncio.sleep(5)#5秒
        self.Atask=self.bot.loop.create_task(interval())
@commands.command()
async def setchannel(self,ctx,ch_id:int):
    self.channel=self.bot.get_channel(ch_id)
    await ctx.send('Set channel:{0}'.format(self.channel.mention))
def setup(bot):                                          #tag他
    bot.add_cog(task(bot))
