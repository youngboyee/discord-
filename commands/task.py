import discord
from discord.ext import commands
import json
import random
import datetime as dt
import pytz
from core.classes import cog_extension

with open('setting.json',mode='r',encoding='utf8') as jfile:
    jdata=json.load(jfile)

class task(cog_extension):
    def __init__(self):
        super().def__init__()
def setup(bot):
    bot.add_cog(task(bot))
