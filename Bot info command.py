import discord
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

bot = commands.Bot(intents=intents)
slash = SlashCommand(bot, sync_commands=True)

@slash.slash(name="botinfo", description="Show information about the bot.")
async def bot_info(ctx: SlashContext):
    bot_user = ctx.guild.get_member(bot.user.id)

    # Fetch bot account information
    bot_name = bot_user.name
    bot_discriminator = bot_user.discriminator
    bot_id = bot_user.id
    bot_created_at = bot_user.created_at.strftime("%Y-%m-%d %H:%M:%S")
    bot_avatar_url = bot_user.avatar_url

    # Create an embed to display bot information
    embed = discord.Embed(title="Bot Information", color=discord.Color.blurple())
    embed.set_thumbnail(url=bot_avatar_url)
    embed.add_field(name="Name", value=bot_name, inline=False)
    embed.add_field(name="Discriminator", value=bot_discriminator, inline=False)
    embed.add_field(name="ID", value=bot_id, inline=False)
    embed.add_field(name="Created At", value=bot_created_at, inline=False)

    await ctx.send(embed=embed)

bot.run('YOUR_BOT_TOKEN')