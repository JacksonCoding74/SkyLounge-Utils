import discord
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

bot = commands.Bot(intents=intents)
slash = SlashCommand(bot, sync_commands=True)

staff_roles = ["Staff Member", "Moderator", "Admin"]  # Add your staff roles in the desired order

@slash.slash(name="demote", description="Demote a user from their current staff role.")
async def demote_user(ctx: SlashContext, user: discord.Member, reason: str = None):
    author = ctx.author
    guild = ctx.guild

    # Check if the user has a staff role
    has_staff_role = False
    for role_name in staff_roles:
        role = discord.utils.get(guild.roles, name=role_name)
        if role and role in user.roles:
            has_staff_role = True
            break

    if not has_staff_role:
        await ctx.send("The specified user does not have a staff role.")
        return

    # Get the highest staff role the user currently has
    highest_staff_role = None
    for role_name in staff_roles:
        role = discord.utils.get(guild.roles, name=role_name)
        if role and role in user.roles:
            highest_staff_role = role
            break

    # Get the previous staff role to be assigned
    prev_staff_role_index = staff_roles.index(highest_staff_role.name) - 1
    prev_staff_role = discord.utils.get(guild.roles, name=staff_roles[prev_staff_role_index])

    # Demote the user
    try:
        await user.remove_roles(highest_staff_role)
        if prev_staff_role:
            await user.add_roles(prev_staff_role)
        await ctx.send(f"{user.mention} has been demoted from **{highest_staff_role.name}**.")

        if reason:
            await user.send(f"You have been demoted from **{highest_staff_role.name}**. Reason: {reason}")
    except discord.Forbidden:
        await ctx.send("I don't have the necessary permissions to modify roles.")
    except discord.HTTPException:
        await ctx.send("An error occurred while demoting the user.")

bot.run('YOUR_BOT_TOKEN')