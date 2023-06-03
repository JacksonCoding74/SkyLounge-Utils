import discord
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

bot = commands.Bot(intents=intents)
slash = SlashCommand(bot, sync_commands=True)

@slash.slash(name="profilepic", description="Retrieve user's profile picture.")
async def get_profile_picture(ctx: SlashContext, user: discord.User = None):
    if user is None:
        user = ctx.author

    # Get the URL of the user's profile picture
    profile_pic_url = user.avatar_url

    # Create an embed with the profile picture
    embed = discord.Embed(title=f"{user.name}'s Profile Picture", color=discord.Color.blurple())
    embed.set_image(url=profile_pic_url)

    await ctx.send(embed=embed)

@get_profile_picture.error
async def profile_picture_error(ctx: SlashContext, error):
    if isinstance(error, commands.errors.UserNotFound):
        await ctx.send("User not found.")

@bot.event
async def on_ready():
    print(f"Bot is ready. Logged in as {bot.user}")

bot.run('YOUR_BOT_TOKEN')