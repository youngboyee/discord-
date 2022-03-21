import discord
from discord.ext import commands

bot=commands.Bot(command_prefix=']')

@bot.event
async def on_ready():
    print('Zhan has landed')

bot.run('OTU1MzM3OTgyMzMwNjc5MzU3.YjgN1A.LSCa879iWGkFoQ3SLwKGHl7OE_I')
