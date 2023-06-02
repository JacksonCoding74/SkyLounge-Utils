import discord
from discord_slash import SlashCommand, SlashContext

# Create a new Discord bot instance
bot = discord.Client(intents=discord.Intents.default())
slash = SlashCommand(bot, sync_commands=True)

@bot.event
async def on_ready():
    print(f'Bot is ready. Connected to Discord as {bot.user.name}')

@slash.slash(name="eval", description="Evaluate Python code", options=[
    {
        "name": "code",
        "description": "The code to evaluate",
        "type": 3,  # String type
        "required": True
    }
])
async def evaluate_code(ctx: SlashContext, code: str):
    # Check if the user has permission to execute eval command
    if ctx.author.id != YOUR_USER_ID:
        await ctx.send("You don't have permission to execute this command.")
        return

    try:
        # Execute the provided code
        result = eval(code)

        # Send the result as a message
        await ctx.send(f"**Result:**\n```{result}```")
    except Exception as e:
        # Send an error message if code execution fails
        await ctx.send(f"**Error:**\n```{type(e).__name__}: {e}```")

# Replace 'YOUR_DISCORD_TOKEN' with your actual Discord bot token
bot.run('YOUR_DISCORD_TOKEN')