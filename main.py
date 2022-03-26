import discord
from discord.ext import commands
import json

with open('setting.json',mode='r',encoding='utf8') as jfile:
    jdata=json.load(jfile)


intents=discord.Intents.default()
intents.members=True

bot=commands.Bot(command_prefix='!',intents=intents)

@bot.event
async def on_ready():
    print('Zhan has landed')
    channel=bot.get_channel(848189292467191860)
    await channel.send('Zhan降落啦!')
    

@bot.event
async def on_member_join(member):
    channel=bot.get_channel(int(jdata['Welcome_channel']))
    await channel.send(f'{member}降落啦!')
    
@bot.event
async def on_member_remove(member):
    channel=bot.get_channel(int(jdata['Bye_channel']))
    await channel.send(f'{member}飛走了...')
   
@bot.command()
async def ping(ctx):
    await ctx.send('{0}毫秒'.format(round(bot.latency*1000)))


bot.run(jdata['TOKEN'])
