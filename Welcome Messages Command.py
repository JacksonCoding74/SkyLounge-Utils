import discord
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

bot = commands.Bot(intents=intents)
slash = SlashCommand(bot, sync_commands=True)

welcome_messages_enabled = False
welcome_channel_id = None

@slash.slash(name="setwelcome", description="Enable or disable welcome messages in a channel.")
async def set_welcome(ctx: SlashContext, channel: discord.TextChannel, enabled: bool):
    global welcome_messages_enabled
    global welcome_channel_id

    welcome_messages_enabled = enabled
    welcome_channel_id = channel.id

    if enabled:
        await ctx.send(f"📩 Welcome messages enabled in {channel.mention}!")
    else:
        await ctx.send("🚫 Welcome messages disabled.")

@bot.event
async def on_member_join(member):
    global welcome_messages_enabled
    global welcome_channel_id

    if welcome_messages_enabled and welcome_channel_id:
        channel = bot.get_channel(welcome_channel_id)
        await channel.send(f"👋 Welcome, {member.mention}!")

@bot.event
async def on_ready():
    print(f"Bot is ready. Logged in as {bot.user}")

bot.run('YOUR_BOT_TOKEN')