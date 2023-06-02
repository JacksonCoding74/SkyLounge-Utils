import discord
from discord_slash import SlashCommand, SlashContext

# Create a new Discord bot instance
bot = discord.Client(intents=discord.Intents.default())
slash = SlashCommand(bot, sync_commands=True)

@bot.event
async def on_ready():
    print(f'Bot is ready. Connected to Discord as {bot.user.name}')

@slash.slash(name="slowmode", description="Set the slow mode in a channel", options=[
    {
        "name": "channel",
        "description": "The channel to set the slow mode",
        "type": 7,  # Channel type
        "required": True
    },
    {
        "name": "duration",
        "description": "The slow mode duration in seconds",
        "type": 4,  # Integer type
        "required": True
    }
])
async def slowmode(ctx: SlashContext, channel: discord.TextChannel, duration: int):
    # Set the slow mode in the channel
    await channel.edit(slowmode_delay=duration)
    await ctx.send(f"Slow mode has been set to {duration} seconds in {channel.mention}.")

# Replace 'YOUR_DISCORD_TOKEN' with your actual Discord bot token
bot.run('YOUR_DISCORD_TOKEN')