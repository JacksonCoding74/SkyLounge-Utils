import discord
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext
import requests

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

bot = commands.Bot(intents=intents)
slash = SlashCommand(bot, sync_commands=True)

@slash.slash(name="randommeme", description="Find and send a random meme.")
async def send_random_meme(ctx: SlashContext):
    # Make a request to get a random meme from an API
    response = requests.get("needs a endpoint")

    if response.status_code == 200:
        meme_data = response.json()
        meme_url = meme_data["url"]

        # Create an embed with the meme
        embed = discord.Embed(title="Random Meme", color=discord.Color.blurple())
        embed.set_image(url=meme_url)

        await ctx.send(embed=embed)
    else:
        await ctx.send("Failed to fetch a random meme.")

@bot.event
async def on_ready():
    print(f"Bot is ready. Logged in as {bot.user}")

bot.run('YOUR_BOT_TOKEN')