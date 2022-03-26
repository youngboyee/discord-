import discord
from discord.ext import commands
import json

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
    channel=bot.get_channel(955340986979086408)
    await channel.send(f'{member}降落啦!')
    
@bot.event
async def on_member_remove(member):
    channel=bot.get_channel(955340986979086408)
    await channel.send(f'{member}飛走了...')
   
@bot.command()
async def ping(ctx):
    await ctx.send('{0}毫秒'.format(round(bot.latency*1000)))


bot.run('OTU1MzM3OTgyMzMwNjc5MzU3.YjgN1A.ocbuUmqhj4HRHwlFFGqq9aw2ga0')