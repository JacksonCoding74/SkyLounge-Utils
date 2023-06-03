import discord
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

bot = commands.Bot(intents=intents)
slash = SlashCommand(bot, sync_commands=True)

@slash.slash(name="role", description="Give or remove a role from users.")
async def manage_role(ctx: SlashContext, action: str, role: discord.Role, members: commands.Greedy[discord.Member]):
    if action.lower() == "give":
        for member in members:
            await member.add_roles(role)
        await ctx.send(f"Successfully given the {role.name} role to {len(members)} members.")
    elif action.lower() == "remove":
        for member in members:
            await member.remove_roles(role)
        await ctx.send(f"Successfully removed the {role.name} role from {len(members)} members.")
    else:
        await ctx.send("Invalid action. Please specify 'give' or 'remove'.")

bot.run('YOUR_BOT_TOKEN')