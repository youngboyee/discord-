import discord
from discord.ext import commands
import json
import asyncio
import datetime 
from core.classes import cog_extension

timesetter=[]

class task(cog_extension):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        
        #async def interval():#間隔執行
            #await self.bot.wait_until_ready()
            #self.channel=self.bot.get_channel(848189292467191860)
            #while not self.bot.is_closed():#bot沒關就會一直執行
               #await self.channel.send("It's working")
               #await asyncio.sleep(1)#讓程式有間隔時間，以免卡住
               #self.Atask=self.bot.loop.create_task(interval())
        self.counter=0
        async def timetask():#指定時間執行
            
            await self.bot.wait_until_ready()
            self.channel=self.bot.get_channel(960024341087682570)#指定頻道
            while not self.bot.is_closed():#bot沒關就會一直執行
                now_time=datetime.datetime.now().strftime('%H%M')
                with open('setting.json',mode='r',encoding='utf8') as jfile:
                    jdata=json.load(jfile)
                if now_time==jdata["time"] and self.counter<3:
                    await self.channel.send("{0}你不是要{1}嗎?".format(timesetter[0].mention,jdata["schedule"]))
                    await asyncio.sleep(1)#讓程式有間隔時間，以免卡住
                    self.counter+=1
                    
                else:
                    await asyncio.sleep(1)
                    pass
            self.counter=0
            timesetter.clear()
        
        self.Atask=self.bot.loop.create_task(timetask())


    @commands.command()
    async def setchannel(self,ctx,ch_id:int):
        self.channel=self.bot.get_channel(ch_id)
        await ctx.send('Set channel:{0}'.format(self.channel.mention))#tag頻道

    @commands.command()#設定時間
    async def settime(self,ctx,time):
        with open('setting.json',mode='r',encoding='utf8') as jfile:
            jdata=json.load(jfile)
        jdata['time']=time#把輸入的時間傳入jdata
        with open('setting.json',mode='w',encoding='utf8') as jfile:
            json.dump(jdata,jfile,indent=4)#縮排，檔案才不會爆
        timesetter.append(ctx.author)

    @commands.command()#設定要做的事
    async def schedule(self,ctx,time):
        with open('setting.json',mode='r',encoding='utf8') as jfile:
            jdata=json.load(jfile)
        jdata['schedule']=time#把輸入的事傳入jdata
        with open('setting.json',mode='w',encoding='utf8') as jfile:
            json.dump(jdata,jfile,indent=4)#縮排，檔案才不會爆
        

def setup(bot):                                          
    bot.add_cog(task(bot))
