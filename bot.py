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
        cur.execute(f"SELECT prefix FROM simple_voice.servers_data WHERE server_id = {message.guild.id};")
        row = str(cur.fetchone())
        return row

bot: commands.Bot = commands.Bot(command_prefix = get_prefix, intents = discord.Intents.all())

@bot.event
async def on_ready():
    print(f'Авторизован под {bot.user}')

@bot.command()
async def info(ctx):
    await ctx.send('Test!')
    embed = discord.Embed(title='Simple Voice',
                          description='Создание собственных каналов для каждого участника. Редактирование параметров канала через команды и многое другое.',
                          url='https://github.com/Shandeika/simple-voice', colour=0x8691c8)
    embed.set_thumbnail(url='https://photo.shandy-dev.ru/shandy/uploads/ab1d22e5013aef1fb490a5f1e80c977a.png')
    embed.set_image(url='https://photo.shandy-dev.ru/shandy/uploads/3ce580d24d84b65768beac66bbf12d92.png')
    embed.set_author(name='Shandy', url='https://github.com/Shandeika/',
                     icon_url='https://photo.shandy-dev.ru/shandy/uploads/9de56bb9dc3276a0b7cf678809097521.png')
    embed.set_footer(text='Copyright © 2019–2021 Shandy developer agency All Rights Reserved. © 2021')
    await ctx.send(embed=embed)    

bot.run(config["Config"]["token"])
