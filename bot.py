import discord
from discord.ext import commands
import json
import os
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
async def load(ctx,extension):
    bot.load_extension(f'commands.{extension}')
    await ctx.send('loaded {0} done'.format(extension))
@bot.command()
async def reload(ctx,extension):
    bot.reload_extension(f'commands.{extension}')
    await ctx.send('reloaded {0} done'.format(extension))
@bot.command()
async def unload(ctx,extension):
    bot.unload_extension(f'commands.{extension}')
    await ctx.send('unloaded {0} done'.format(extension))



for Filename in os.listdir('./commands'):
    if Filename.endswith('.py'):
        bot.load_extension(f'commands.{Filename[:-3]}')

if __name__ =='__main__':
     bot.run(jdata['TOKEN'])

