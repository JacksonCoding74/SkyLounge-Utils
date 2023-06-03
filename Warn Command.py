import discord
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

bot = commands.Bot(intents=intents)
slash = SlashCommand(bot, sync_commands=True)

@slash.slash(name="warn", description="Issues a warning to a user.")
async def warn_user(ctx: SlashContext, user: discord.Member, reason: str):
    warning_message = f"You have been warned in {ctx.guild.name} for the following reason:\n\n{reason}"
    
    try:
        await user.send(warning_message)
        await ctx.send(f"Successfully warned {user.mention} and sent a DM with the reason.")
    except discord.Forbidden:
        await ctx.send(f"Could not send a DM to {user.mention}.")

bot.run('YOUR_BOT_TOKEN')