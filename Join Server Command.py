import discord
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

bot = commands.Bot(intents=intents)
slash = SlashCommand(bot, sync_commands=True)

@slash.slash(name="joinserver", description="Generate an invite link to join the server.")
async def join_server(ctx: SlashContext):
    invite_link = "https://discord.gg/Mf46Rnqtbu"
    await ctx.send(f"You can join the server using this invite link: {invite_link}")

bot.run('YOUR_BOT_TOKEN')