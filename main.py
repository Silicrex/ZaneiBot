import discord
from discord.ext import commands
import logging
from datetime import datetime
from dotenv import load_dotenv
import os
from pathlib import Path

# Make sure .env exists and load environment variables
if not Path('.env').is_file():
    with open('.env', 'w') as file:
        file.write('# Tokens\nDISCORD_TOKEN=')
    print('Generated .env file, stopping')
    quit()
load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

Path('logs/').mkdir(exist_ok=True)  # Make sure the Logs folder exists
log_handler = logging.FileHandler(filename=f'logs/{datetime.now().strftime("%Y-%B")}.log', encoding='utf-8', mode='a')

bot = commands.Bot(command_prefix='$', intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} on discord.py version {discord.__version__}!')


DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
bot.run(DISCORD_TOKEN, log_handler=log_handler)
