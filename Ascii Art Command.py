import discord
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext
import random

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

bot = commands.Bot(intents=intents)
slash = SlashCommand(bot, sync_commands=True)

ascii_art = [
    r"```\n"
    r"   |\_/|   \n"
    r"  / @ @ \  \n"
    r" ( > º < ) \n"
    r"  '>>x<<'  \n"
    r" /  O  O  \ \n"
    r" /        \ \n"
    r"```",
    r"```\n"
    r"   /\_/\\   \n"
    r"  (=^ .^=)  \n"
    r" c   \"\"  j \n"
    r"```",
    r"```\n"
    r"       __      \n"
    r"    __/o \-/\__ \n"
    r"   /_-\__\/-\_-\ \n"
    r"   \_-/__\__-_/ \n"
    r"     \========/ \n"
    r"```",
    # Add more ASCII art here
]

@slash.slash(name="randomascii", description="Generate random ASCII art.")
async def generate_random_ascii(ctx: SlashContext):
    random_art = random.choice(ascii_art)
    await ctx.send(random_art)

@bot.event
async def on_ready():
    print(f"Bot is ready. Logged in as {bot.user}")

bot.run('YOUR_BOT_TOKEN')