import discord
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

bot = commands.Bot(command_prefix='!', intents=intents)
slash = SlashCommand(bot, sync_commands=True)

@slash.slash(name="remove_timeout", description="Removes the timeout from a user.")
async def remove_timeout(ctx: SlashContext, user: discord.Member):
    if user.guild_permissions.mute:
        await user.edit(mute=False)
        await ctx.send(f"Successfully removed timeout from {user.mention}.")
    else:
        await ctx.send("This user is not in timeout.")

bot.run('YOUR_BOT_TOKEN')