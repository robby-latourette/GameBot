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
async def cum(ctx, arg:int):
    if(arg > 3600):
        await ctx.send("error, too long try again")
        return
    else:
        await ctx.send("JUST RIGHT")

bot.run(TOKEN)