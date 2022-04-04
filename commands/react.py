import discord
from discord.ext import commands
import json
import random
import datetime as dt
import pytz
from core.classes import cog_extension
import requests

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
    @commands.command()
    async def weather(self,ctx,*,city:str):
        city_name = city
        complete_url = jdata['base_url'] + "appid=" + jdata['api_key'] + "&q=" + city_name
        response = requests.get(complete_url)
        self.x = response.json()
        self.channel = ctx.message.channel
        if self.x["cod"] != "404":
            async with self.channel.typing():
                self.y = self.x["main"]
                temperature=self.y["temp"]
                self.celsiuis_temperature= str(round(temperature-273.15))
                self.pressure=self.y["pressure"]
                self.humidity=self.y["humidity"]
                self.z=self.x["weather"]
                self.weather_description = self.z[0]["description"]
                weather_description = self.z[0]["description"]
                embed = discord.Embed(title=f"Weather in {city_name}",
                                color=ctx.guild.me.top_role.color,
                                timestamp=ctx.message.created_at,)
                embed.add_field(name="Descripition", value=f"**{weather_description}**", inline=False)
                embed.add_field(name="溫度(C)", value=f"**{self.celsiuis_temperature}°C**", inline=False)
                embed.add_field(name="濕度(%)", value=f"**{self.humidity}%**", inline=False)
                embed.add_field(name="Atmospheric Pressure(hPa)", value=f"**{self.pressure}hPa**", inline=False)
                embed.set_thumbnail(url="https://i.ibb.co/CMrsxdX/weather.png")
                embed.set_footer(text=f"Requested by {ctx.author.name}")

def setup(bot):
    bot.add_cog(react(bot))
