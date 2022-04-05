import discord  #至關重要
from discord.ext import commands
import json
import os
with open('setting.json',mode='r',encoding='utf8') as jfile:
    jdata=json.load(jfile)


intents=discord.Intents.default()
intents.members=True

bot=commands.Bot(command_prefix='-',intents=intents)

@bot.event
async def on_ready():#確認機器人已經上線
    print("Yang's bot is ready!")
    

@bot.event#成員進入伺服器
async def on_member_join(member):
    channel=bot.get_channel(int(jdata['hi_channel']))#在json檔裡面指定頻道ID
    await channel.send(f'{member.mention}降落啦!')#在頻道裡面傳訊息
                                #tag那個人
@bot.event#成員離開伺服器
async def on_member_remove(member):
    channel=bot.get_channel(int(jdata['bye_channel']))
    await channel.send(f'{member.mention}飛走了...')
#以下為cog的東西
@bot.command()
async def load(ctx,extension):
    bot.load_extension(f'commands.{extension}')
    await ctx.send('load {0} done'.format(extension))
@bot.command()
async def reload(ctx,extension):
    bot.reload_extension(f'commands.{extension}')
    await ctx.send('reload {0} done'.format(extension))
@bot.command()
async def unload(ctx,extension):
    bot.unload_extension(f'commands.{extension}')
    await ctx.send('unload {0} done'.format(extension))



for Filename in os.listdir('./commands'):
    if Filename.endswith('.py'):
        bot.load_extension(f'commands.{Filename[:-3]}')

if __name__ =='__main__':
     bot.run(jdata['TOKEN'])

