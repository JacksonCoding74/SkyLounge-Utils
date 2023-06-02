import discord
from discord_slash import SlashCommand, SlashContext

# Create a new Discord bot instance
bot = discord.Client(intents=discord.Intents.default())
slash = SlashCommand(bot, sync_commands=True)

@bot.event
async def on_ready():
    print(f'Bot is ready. Connected to Discord as {bot.user.name}')

@slash.slash(name="kick", description="Kick a member", options=[
    {
        "name": "member",
        "description": "The member to kick",
        "type": 6,  # User type
        "required": True
    },
    {
        "name": "reason",
        "description": "Reason for the kick",
        "type": 3,  # String type
        "required": False
    }
])
async def kick(ctx: SlashContext, member: discord.Member, reason: str = None):
    # Perform kick logic here
    if reason:
        kick_message = f"{member.name} has been kicked for {reason}."
    else:
        kick_message = f"{member.name} has been kicked."

    await member.kick(reason=reason)
    await ctx.send(kick_message)

# Replace 'YOUR_DISCORD_TOKEN' with your actual Discord bot token
bot.run('YOUR_DISCORD_TOKEN')