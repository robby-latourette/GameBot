import os

import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
bot = commands.Bot(command_prefix='!')


#Game Variables
gunChambers = 6



@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.event
async def on_message(message): 
    if message.content.startswith("!gb marco"): 
        channel = message.channel
        await channel.send("POLO!")    

    if message.content.startswith("!gb RR new"):
        channel = message.channel
        await channel.send("New Game Russian Roulette")
        gunChambers = 6
        
    #if message.content.startswith("!gb RR fire"):




bot.run(TOKEN)