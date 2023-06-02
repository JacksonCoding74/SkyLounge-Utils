import discord
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_option

# Create a new Discord bot instance
bot = discord.Client(intents=discord.Intents.default())
slash = SlashCommand(bot, sync_commands=True)

@bot.event
async def on_ready():
    print(f'Bot is ready. Connected to Discord as {bot.user.name}')

@slash.slash(name="changenick", description="Change a member's nickname", options=[
    create_option(
        name="member",
        description="The member to change the nickname",
        option_type=6,  # User type
        required=True
    ),
    create_option(
        name="nickname",
        description="The new nickname",
        option_type=3,  # String type
        required=True
    )
])
async def change_nickname(ctx: SlashContext, member: discord.Member, nickname: str):
    # Change the member's nickname
    await member.edit(nick=nickname)
    await ctx.send(f"Nickname changed for {member.mention} to `{nickname}`")

# Replace 'YOUR_DISCORD_TOKEN' with your actual Discord bot token
bot.run('YOUR_DISCORD_TOKEN')