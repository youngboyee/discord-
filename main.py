import discord
from discord.ext import commands


intents=discord.Intents.default()
intents.members=True

bot=commands.Bot(command_prefix='!',intents=intents)

@bot.event
async def on_ready():
    print('Zhan has landed')



@bot.event
async def on_member_join(member):
    channel=bot.get_channel(955340986979086408)
    await channel.send(f'{member}降落啦!')
@bot.event
async def on_member_remove(member):
    channel=bot.get_channel(955340986979086408)
    await channel.send(f'{member}飛走了...')


bot.run('')
