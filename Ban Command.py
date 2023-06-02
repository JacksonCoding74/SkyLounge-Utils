import discord
from discord_slash import SlashCommand, SlashContext

# Create a new Discord bot instance
bot = discord.Client(intents=discord.Intents.default())
slash = SlashCommand(bot, sync_commands=True)

@bot.event
async def on_ready():
    print(f'Bot is ready. Connected to Discord as {bot.user.name}')

@slash.slash(name="ban", description="Ban a user", options=[
    {
        "name": "user",
        "description": "The user to ban",
        "type": 6,  # User type
        "required": True
    },
    {
        "name": "reason",
        "description": "Reason for the ban",
        "type": 3,  # String type
        "required": False
    }
])
async def ban(ctx: SlashContext, user: discord.User, reason: str = None):
    # Perform ban logic here
    if reason:
        ban_message = f"{user.name} has been banned for {reason}."
    else:
        ban_message = f"{user.name} has been banned."

    await ctx.send(ban_message)

# Replace 'YOUR_DISCORD_TOKEN' with your actual Discord bot token
bot.run('YOUR_DISCORD_TOKEN')