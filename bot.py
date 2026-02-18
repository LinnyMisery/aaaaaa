import discord
from discord.ext import commands
import random
import os

# --- BOT SETUP ---
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# --- CARDS FOLDER ---
CARD_FOLDER = "./cards"  # make sure your images are in the 'cards' folder

# --- EVENTS ---
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

# --- RANDOM CARD DRAW ---
@bot.command()
async def kcard(ctx):
    if not os.listdir(CARD_FOLDER):
        await ctx.send("No cards found! Upload some images to /cards folder.")
        return
    card = random.choice(os.listdir(CARD_FOLDER))
    await ctx.send(file=discord.File(os.path.join(CARD_FOLDER, card)))

# --- SPECIFIC CARD BY NAME ---
@bot.command()
async def kcardname(ctx, name: str):
    card_path = os.path.join(CARD_FOLDER, f"{name.lower()}.png")
    if os.path.exists(card_path):
        await ctx.send(file=discord.File(card_path))
    else:
        await ctx.send("Sorry, that card doesn’t exist!")

# --- TOKEN ---
# The bot reads the token from Railway’s Environment Variables
bot.run(os.environ["TOKEN"])
