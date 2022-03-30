import discord
from discord.ext import commands
import json
import random


with open('setting.json',mode='r',encoding='utf8') as jfile:
    jdata=json.load(jfile)


intents=discord.Intents.default()
intents.members=True

bot=commands.Bot(command_prefix='!',intents=intents)

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
async def ping(self,ctx):
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
    

bot.run(jdata['TOKEN'])
