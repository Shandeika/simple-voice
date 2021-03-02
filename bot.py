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

bot: commands.Bot = commands.Bot(command_prefix="/")

@bot.event
async def on_ready():
    print(f'Авторизован под {bot.user}')

bot.run(config["Config"]["token"])
