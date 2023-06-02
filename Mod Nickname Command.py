import discord
import random
import string
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_option

# Create a new Discord bot instance
bot = discord.Client(intents=discord.Intents.default())
slash = SlashCommand(bot, sync_commands=True)

@bot.event
async def on_ready():
    print(f'Bot is ready. Connected to Discord as {bot.user.name}')

@slash.slash(name="moderatenick", description="Set a member's nickname to a Moderated Nickname")
async def moderate_nickname(ctx: SlashContext, member: discord.Member):
    # Generate random text for the moderated nickname
    random_text = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=8))
    moderated_nickname = f"Moderated Nickname '{random_text}'"

    # Change the member's nickname
    await member.edit(nick=moderated_nickname)
    await ctx.send(f"Nickname changed for {member.mention} to `{moderated_nickname}`")

# Replace 'YOUR_DISCORD_TOKEN' with your actual Discord bot token
bot.run('YOUR_DISCORD_TOKEN')