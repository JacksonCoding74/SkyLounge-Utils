import discord
from discord.ext import commands, tasks
from discord_slash import SlashCommand, SlashContext
import requests
import asyncio

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

bot = commands.Bot(intents=intents)
slash = SlashCommand(bot, sync_commands=True)

@tasks.loop(hours=24)
async def post_random_fact(channel_id):
    channel = bot.get_channel(channel_id)
    fact = fetch_random_fact()
    await channel.send(f"📚 **Random Fact**: {fact}")

def fetch_random_fact():
    response = requests.get("https://uselessfacts.jsph.pl/random.json?language=en")
    data = response.json()
    return data["text"]

@slash.slash(name="setupfact", description="Set up the random fact posting in a channel.")
async def setup_fact(ctx: SlashContext, channel: discord.TextChannel):
    # Start the task to post random facts every day
    post_random_fact.start(channel.id)
    await ctx.send(f"📚 Random facts will now be posted in {channel.mention} every day!")

@bot.event
async def on_ready():
    print(f"Bot is ready. Logged in as {bot.user}")

bot.run('YOUR_BOT_TOKEN')