import discord
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

bot = commands.Bot(intents=intents)
slash = SlashCommand(bot, sync_commands=True)

AUTHORIZED_USERS = [1234567890, 9876543210]  # Replace with the actual user IDs

@slash.slash(name="restart", description="Restarts the bot.")
async def restart_bot(ctx: SlashContext):
    if ctx.author.id in AUTHORIZED_USERS:
        await ctx.send("Restarting the bot...")
        await bot.logout()
    else:
        await ctx.send("You are not authorized to use this command.")

bot.run('YOUR_BOT_TOKEN')