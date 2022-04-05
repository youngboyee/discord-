import discord
from discord.ext import commands
import json
import random
import datetime as dt
import pytz
from core.classes import cog_extension
import requests
import twstock as tws

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
    async def 笑話(self,ctx):
        random_ch_joke=random.choice(jdata['ch_joke'])
        await ctx.send(random_ch_joke)
        await ctx.send('\n.\n.\n{0}拜託說好笑喔'.format(ctx.author.mention))

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
    @commands.command()
    async def weather(self,ctx,*,city:str):
        city_name=city
        complete_url = jdata['base_url'] + "appid=" + jdata['api_key'] + "&q=" + city_name
        response = requests.get(complete_url)
        x = response.json()
        
        if x["cod"] != "404":
            async with ctx.message.channel.typing():
                y = x["main"]
                temperature=y["temp"]
                celsiuis_temperature= str(round(temperature-273.15))
                pressure=y["pressure"]
                humidity=y["humidity"]
                z=x["weather"]
                weather_description = z[0]["description"]
                weather_description = z[0]["description"]
                embed = discord.Embed(title=f"Weather in {city_name}",
                                color=ctx.guild.me.top_role.color,
                                timestamp=ctx.message.created_at,)
                embed.add_field(name="概況", value=f"**{weather_description}**", inline=False)
                embed.add_field(name="溫度(C)", value=f"**{celsiuis_temperature}°C**", inline=False)
                embed.add_field(name="濕度(%)", value=f"**{humidity}%**", inline=False)
                embed.add_field(name="氣壓(hPa)", value=f"**{pressure}hPa**", inline=False)
                embed.set_thumbnail(url="https://i.ibb.co/CMrsxdX/weather.png")
                embed.set_footer(text=f"Requested by {ctx.author.name}")
                await ctx.send(embed=embed)
        else:
            await ctx.send("City not found.")
    @commands.command()
    async def stock(self,ctx,sid:str):
        data = tws.realtime.get(sid)
        channel = ctx.message.channel
        if data["success"] != False:
            async with channel.typing():
                rt = data["realtime"]
                ltp = rt["latest_trade_price"]
                h = rt["high"]
                l = rt["low"]
                op = rt["open"]
                info=data['info']
                time = info["time"]
                embed = discord.Embed(title=f"Stock prize at {time}",
                                color=ctx.guild.me.top_role.color,
                                timestamp=ctx.message.created_at,)
                embed.add_field(name="Latest Trade Price", value=f"**{ltp}**", inline=False)
                embed.add_field(name="開盤價", value=f"**{op}**", inline=False)
                embed.add_field(name="高點", value=f"**{h}**", inline=False)
                embed.add_field(name="低點", value=f"**{l}**", inline=False)
                await channel.send(embed=embed)
        else:
            await channel.send("Stock not found.")
def setup(bot):
    bot.add_cog(react(bot))
