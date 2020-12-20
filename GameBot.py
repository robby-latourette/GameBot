import os
import discord
import random
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
bot = commands.Bot(command_prefix='gb')


#Game Variables
gunChambers = 6
def getChambers(): return gunChambers
def setChambers(num): gunChambers = num

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command()
async def rr(ctx, arg):
    if arg == "marco": 
        await ctx.send("POLO!")    

    if arg == "new":
        await ctx.send("New Game: Russian Roulette")
        setChambers(6)
        
    if arg == "fire":
        prob = 1/getChambers()
        rand = random.random()
        if rand > prob:
            await ctx.send("*click*")
            setChambers(getChambers()-1)
        else:
            await ctx.send("BANG!!!! You are dead.")
            setChambers(6)




bot.run(TOKEN)