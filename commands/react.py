import discord
from discord.ext import commands
import json
import random
import datetime as dt
import pytz
from core.classes import cog_extension

with open('setting.json',mode='r',encoding='utf8') as jfile:
    jdata=json.load(jfile)

class react(cog_extension):

    @commands.command()
    async def 圖片(self,ctx):
        random_pic=random.choice(jdata['pic'])
        pic=discord.File(random_pic)
        await ctx.send(file=pic)

    @commands.command()
    async def 網路圖片(self,ctx):
        web_pic=random.choice(jdata['url_pic'])
        await ctx.send(web_pic)

    @commands.command()
    async def 查榜(self,ctx):
        TWtz = pytz.timezone('UTC')
        embed=discord.Embed(title="click here", url="https://www.cac.edu.tw/apply111/index.php", description="一階查榜", color=0x6ef2ca,
        timestamp=dt.datetime.now(tz=TWtz))
        embed.set_author(name="youngboyee", icon_url="https://truth.bahamut.com.tw/s01/202110/a50732a732a0bf9f0e8506a221220014.JPG")
        embed.add_field(name="bot", value="aaa", inline=False)
        await ctx.send(embed=embed)
    @commands.command()
    async def chat(self,ctx,*,msg):
        await ctx.send('{0}LOL'.format(msg))

    @commands.command()
    async def say(self,ctx,*,msg):
        await ctx.message.delete()
        await ctx.send("Don't say {0}!".format(msg))
    @commands.command()
    async def clean(self,ctx,num:int):
        await ctx.channel.purge(limit=num+1)

def setup(bot):
    bot.add_cog(react(bot))
