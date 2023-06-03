import discord
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

bot = commands.Bot(intents=intents)
slash = SlashCommand(bot, sync_commands=True)

@slash.slash(name="serverinfo", description="Show information about the server.")
async def server_info(ctx: SlashContext):
    guild = ctx.guild

    # Fetch various server information
    server_name = guild.name
    server_owner = guild.owner
    member_count = guild.member_count
    server_region = guild.region
    creation_date = guild.created_at.strftime("%Y-%m-%d %H:%M:%S")

    # Create an embed to display server information
    embed = discord.Embed(title="Server Information", color=discord.Color.blurple())
    embed.add_field(name="Name", value=server_name, inline=False)
    embed.add_field(name="Owner", value=server_owner.mention, inline=False)
    embed.add_field(name="Member Count", value=member_count, inline=False)
    embed.add_field(name="Region", value=server_region, inline=False)
    embed.add_field(name="Creation Date", value=creation_date, inline=False)

    await ctx.send(embed=embed)

bot.run('YOUR_BOT_TOKEN')