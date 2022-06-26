import discord
import sqlite3
from decouple import config
from discord.ext import commands

TOKEN = config('TOKEN')
bot = commands.Bot(command_prefix='/', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("test bot is ready")

    global base, cur 
    base = sqlite3.connect('test-bot.db')
    cur = base.cursor()
    if base:
        print('DB connected succesfully')


bot.run(TOKEN)