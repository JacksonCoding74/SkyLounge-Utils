import discord
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

bot = commands.Bot(intents=intents)
slash = SlashCommand(bot, sync_commands=True)

@slash.slash(name="purge", description="Purges a specified number of messages from a channel.")
async def purge_messages(ctx: SlashContext, amount: int):
    if amount < 1:
        await ctx.send("Please provide a valid number of messages to purge.")
        return

    if amount > 999:
        amount = 999

    await ctx.channel.purge(limit=amount+1)
    await ctx.send(f"Successfully purged {amount} messages.")

bot.run('YOUR_BOT_TOKEN')