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
async def chat(ctx,msg):
    await ctx.send('{0}LOL'.format(msg))

@bot.command()
async def say(ctx,*,msg):
    #await ctx.message.delete()
    await ctx.send("Don't say {0}!".format(msg))
@bot.command()
async def clean(ctx,num:int):
    await ctx.channel.purge(limit=num+1)

bot.run(jdata['TOKEN'])
