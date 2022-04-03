import discord
from discord.ext import commands
import json
import asyncio
import datetime as dt
import pytz
from core.classes import cog_extension



class task(cog_extension):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        '''
        async def interval():#間隔執行
            await self.bot.wait_until_ready()
            self.channel=self.bot.get_channel(848189292467191860)
            while not self.bot.is_closed():#bot沒關就會一直執行
                await self.channel.send('I am running')
                await asyncio.sleep(5)#5秒
        self.Atask=self.bot.loop.create_task(interval())
        '''
        async def timetask():
            TWtz = pytz.timezone('UTC')
            await self.bot.wait_until_ready()
            self.channel=self.bot.get_channel(848189292467191860)
            while not self.bot.is_closed():#bot沒關就會一直執行
                now_time=dt.datetime.now(tz=TWtz)
                with open('setting.json',mode='r',encoding='utf8') as jfile:
                    jdata=json.load(jfile)
                if now_time==jdata['time']:
                    await self.channel.send("It's working")
                    await asyncio.sleep(1)#讓程式有間隔時間，以免卡住
                else:
                    pass
            self.Atask=self.bot.loop.create_task(timetask())


    @commands.command()
    async def setchannel(self,ctx,ch_id:int):
        self.channel=self.bot.get_channel(ch_id)
        await ctx.send('Set channel:{0}'.format(self.channel.mention))#tag頻道

    @commands.command()
    async def settime(self,ctx,time):
        with open('setting.json',mode='r',encoding='utf8') as jfile:
            jdata=json.load(jfile)
        jdata['time']=time#把輸入的時間傳入jdata
        with open('setting.json',mode='w',encoding='utf8') as jfile:
            json.dump(jdata,jfile,indent=4)#縮排，檔案才不會爆
def setup(bot):                                          
    bot.add_cog(task(bot))
