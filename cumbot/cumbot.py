import os

import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
bot = commands.Bot(command_prefix='$POG')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command()
async def cum(ctx, arg):
    if isinstance(arg, int):
        await ctx.send(arg + "is not an integer, try again")
    else:
        await ctx.send(arg + "is an integer CONGRATS")

bot.run(TOKEN)