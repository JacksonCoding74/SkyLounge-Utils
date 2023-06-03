import discord
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

bot = commands.Bot(intents=intents)
slash = SlashCommand(bot, sync_commands=True)

@slash.slash(name="membercount", description="Displays the current server member count.")
async def member_count(ctx: SlashContext):
    guild = ctx.guild
    member_count = guild.member_count
    human_count = sum(not member.bot for member in guild.members)
    bot_count = member_count - human_count

    response = f"👥 Total Members: {member_count}\n👤 Humans: {human_count}\n🤖 Bots: {bot_count}"
    await ctx.send(response)

@bot.event
async def on_ready():
    print(f"Bot is ready. Logged in as {bot.user}")

bot.run('YOUR_BOT_TOKEN')