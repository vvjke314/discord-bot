from re import X
import discord
import sqlite3, string, json
from decouple import config
from discord.ext import commands

TOKEN = config('TOKEN')
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("test bot is ready")

    global base, cur 
    base = sqlite3.connect('db/test-bot.db')
    cur = base.cursor()
    if base:
        print('DB connected succesfully')

@bot.command()
async def test(ctx):
    await ctx.send('Ты хуйлан')

@bot.command()
async def info(ctx):
    author = ctx.message.author
    await ctx.send(f'{author} конченный еблан')

@bot.event
async def on_message(message):
    if {i.lower().translate(str.maketrans('','', string.punctuation)) for i in message.content.split(' ')}\
    .intersection(set(json.load(open('cenz.json')))) != set():
        await message.channel.send(f'{message.author.mention} Пизда тебе ебланчик')
        await message.delete()

bot.run(TOKEN)