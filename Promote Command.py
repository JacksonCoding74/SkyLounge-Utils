import discord
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

bot = commands.Bot(intents=intents)
slash = SlashCommand(bot, sync_commands=True)

staff_roles = ["Staff Member", "Moderator", "Admin"]  # Add your staff roles in the desired order

@slash.slash(name="promote", description="Promote a user to the next staff role.")
async def promote_user(ctx: SlashContext):
    author = ctx.author
    guild = ctx.guild
    
    # Get the highest staff role the user currently has
    highest_staff_role = None
    for role_name in staff_roles:
        role = discord.utils.get(guild.roles, name=role_name)
        if role and role in author.roles:
            highest_staff_role = role
            break
    
    # Check if the user already has the highest staff role
    if highest_staff_role is None or highest_staff_role == staff_roles[-1]:
        await ctx.send("You already have the highest staff role.")
        return
    
    # Get the next staff role to be assigned
    next_staff_role_index = staff_roles.index(highest_staff_role.name) + 1
    next_staff_role = discord.utils.get(guild.roles, name=staff_roles[next_staff_role_index])
    
    # Assign the next staff role to the user
    try:
        await author.add_roles(next_staff_role)
        await author.add_roles(highest_staff_role)
        await ctx.send(f"You have been promoted to **{next_staff_role.name}** and now have **{highest_staff_role.name}**.")
    except discord.Forbidden:
        await ctx.send("I don't have the necessary permissions to assign roles.")
    except discord.HTTPException:
        await ctx.send("An error occurred while assigning roles.")

bot.run('YOUR_BOT_TOKEN')