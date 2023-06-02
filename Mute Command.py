import discord
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_option

# Create a new Discord bot instance
bot = discord.Client(intents=discord.Intents.default())
slash = SlashCommand(bot, sync_commands=True)

@bot.event
async def on_ready():
    print(f'Bot is ready. Connected to Discord as {bot.user.name}')

@slash.slash(name="mute", description="Mute a member", options=[
    create_option(
        name="member",
        description="The member to mute",
        option_type=6,  # User type
        required=True
    ),
    create_option(
        name="duration",
        description="Mute duration in minutes",
        option_type=4,  # Integer type
        required=False
    )
])
async def mute(ctx: SlashContext, member: discord.Member, duration: int = None):
    # Mute the member
    await member.edit(mute=True)

    if duration:
        await asyncio.sleep(duration * 60)  # Convert minutes to seconds
        await member.edit(mute=False)
        await ctx.send(f"{member.mention} has been unmuted after {duration} minutes.")
    else:
        await ctx.send(f"{member.mention} has been muted.")

# Replace 'YOUR_DISCORD_TOKEN' with your actual Discord bot token
bot.run('YOUR_DISCORD_TOKEN')