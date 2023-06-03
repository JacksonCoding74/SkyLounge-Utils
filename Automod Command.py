import discord
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

bot = commands.Bot(intents=intents)
slash = SlashCommand(bot, sync_commands=True)

automod_enabled = False
logging_channel_id = 123456789  # Replace with the ID of your logging channel
prohibited_words = ["badword1", "badword2", "badword3"]  # Add your list of prohibited words here

@slash.slash(name="automod", description="Enable or disable automod for spamming, links, spam mentions, file uploads, and swearing.")
async def toggle_automod(ctx: SlashContext):
    global automod_enabled
    automod_enabled = not automod_enabled
    
    if automod_enabled:
        await ctx.send("Automod has been enabled.")
    else:
        await ctx.send("Automod has been disabled.")

@bot.event
async def on_message(message):
    if not automod_enabled:
        return
    
    author = message.author
    
    # Check for spamming
    if len(message.content) > 100:
        await message.delete()
        await author.send("Your message has been removed for spamming.")
    
    # Check for links
    if "http://" in message.content or "https://" in message.content:
        await message.delete()
        await author.send("Your message has been removed for containing a link.")
    
    # Check for spam mentions
    if len(message.mentions) >= 5:
        await message.delete()
        await author.send("Your message has been removed for spam mentioning.")
    
    # Check for file uploads
    for attachment in message.attachments:
        if attachment.filename.endswith((".zip", ".exe")):
            await message.delete()
            await author.send("Your message has been removed for uploading a restricted file.")
            break
    
    # Check for prohibited words
    content_lower = message.content.lower()
    if any(word in content_lower for word in prohibited_words):
        await message.delete()
        await author.send("Your message has been removed for containing prohibited content.")
        
        # Send alert to logging channel
        logging_channel = bot.get_channel(logging_channel_id)
        if logging_channel:
            embed = discord.Embed(
                title="Prohibited Message Alert",
                description=f"**User:** {author.mention} ({author.id})\n"
                            f"**Message Content:** {message.content}",
                color=discord.Color.red()
            )
            await logging_channel.send(embed=embed)
    
    await bot.process_commands(message)

bot.run('YOUR_BOT_TOKEN')