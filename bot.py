import discord
import pymysql
import configparser
import functions
import asyncio
from discord.ext import commands

config = configparser.ConfigParser()
config.read("config.ini", encoding='utf-8')

con = pymysql.connect(
    host=config["DB"]["server"],
    user=config["DB"]["login"],
    password=config["DB"]["password"],
    database=config["DB"]["database"]
)

def get_prefix(bot, message):
    with con.cursor() as cur:
        cur.execute(f"SELECT prefix FROM simple_voice.server_{message.guild.id};")
        row = cur.fetchone()
        return row

bot: commands.Bot = commands.Bot(command_prefix = get_prefix, instintents = discord.Intents.all())

@bot.event
async def on_ready():
    print(f'Авторизован под {bot.user}')

bot.run(config["Config"]["token"])
