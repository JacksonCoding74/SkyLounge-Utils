import discord
from discord.ext import commands
from datetime import datetime

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def account_info(ctx, user: discord.Member = None):
    if user is None:
        user = ctx.author

    avatar_url = user.avatar_url
    username = user.name
    discriminator = user.discriminator
    user_id = user.id
    creation_time = user.created_at.strftime('%Y-%m-%d %H:%M:%S')
    is_nitro = user.premium_since is not None

    embed = discord.Embed(title=f'Account Info - {username}', color=discord.Color.blue())
    embed.set_thumbnail(url=avatar_url)
    embed.add_field(name='Username', value=username, inline=True)
    embed.add_field(name='Discriminator', value=discriminator, inline=True)
    embed.add_field(name='User ID', value=user_id, inline=True)
    embed.add_field(name='Account Age', value=creation_time, inline=False)
    embed.add_field(name='Nitro Subscriber', value=is_nitro, inline=False)

    await ctx.send(embed=embed)

bot.run('YOUR_BOT_TOKEN')