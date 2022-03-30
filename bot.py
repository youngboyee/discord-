import discord
from discord.ext import commands
import json
import random
import datetime as dt
import pytz

with open('setting.json',mode='r',encoding='utf8') as jfile:
    jdata=json.load(jfile)


intents=discord.Intents.default()
intents.members=True

bot=commands.Bot(command_prefix='-',intents=intents)

@bot.event
async def on_ready():
    print('Zhan has landed')
    channel=bot.get_channel(955340986979086408)
    await channel.send('Zhan降落啦!')
    

@bot.event
async def on_member_join(member):
    channel=bot.get_channel(int(jdata['hi_channel']))
    await channel.send(f'{member}降落啦!')
    
@bot.event
async def on_member_remove(member):
    channel=bot.get_channel(int(jdata['bye_channel']))
    await channel.send(f'{member}飛走了...')
 
@bot.command()
async def ping(ctx):
    await ctx.send('{0}毫秒'.format(round(bot.latency*1000)))

@bot.command()
async def 圖片(ctx):
    random_pic=random.choice(jdata['pic'])
    pic=discord.File(random_pic)
    await ctx.send(file=pic)

@bot.command()
async def 網路圖片(ctx):
    web_pic=random.choice(jdata['url_pic'])
    await ctx.send(web_pic)

@bot.command()
async def chat(ctx,msg):
    await ctx.send('{0}LOL'.format(msg))

@bot.command()
async def 查榜(ctx):
    TWtz = pytz.timezone('UTC')
    embed=discord.Embed(title="click here", url="https://www.cac.edu.tw/apply111/index.php", description="一階查榜", color=0x6ef2ca,
    timestamp=dt.datetime.now(tz=TWtz))
    embed.set_author(name="youngboyee", icon_url="https://truth.bahamut.com.tw/s01/202110/a50732a732a0bf9f0e8506a221220014.JPG")
    embed.add_field(name="bot", value="aaa", inline=False)
    await ctx.send(embed=embed)
    

bot.run(jdata['TOKEN'])
