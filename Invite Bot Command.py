import discord
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

bot = commands.Bot(intents=intents)
slash = SlashCommand(bot, sync_commands=True)

@slash.slash(name="invite", description="Invite the bot to your server.")
async def invite_bot(ctx: SlashContext):
    response = "I cannot be invited as I am a private bot only for use in the SkyLounge server!"
    await ctx.send(response)

bot.run('YOUR_BOT_TOKEN')