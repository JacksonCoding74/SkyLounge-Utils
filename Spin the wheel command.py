import random
import discord
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

bot = commands.Bot(intents=intents)
slash = SlashCommand(bot, sync_commands=True)

@slash.slash(name="spinthewheel", description="Spin the wheel and randomly select an item.",
             options=[
                 {
                     "name": "item1",
                     "description": "Item 1",
                     "type": 3,
                     "required": True
                 },
                 {
                     "name": "item2",
                     "description": "Item 2",
                     "type": 3,
                     "required": False
                 },
                 {
                     "name": "item3",
                     "description": "Item 3",
                     "type": 3,
                     "required": False
                 },
                 {
                     "name": "item4",
                     "description": "Item 4",
                     "type": 3,
                     "required": False
                 },
                 {
                     "name": "item5",
                     "description": "Item 5",
                     "type": 3,
                     "required": False
                 }
             ])
async def spin_the_wheel(ctx: SlashContext, item1: str, item2: str = None, item3: str = None,
                         item4: str = None, item5: str = None):
    items = [item1]
    if item2:
        items.append(item2)
    if item3:
        items.append(item3)
    if item4:
        items.append(item4)
    if item5:
        items.append(item5)

    if len(items) < 2:
        await ctx.send("Please provide at least two items.")
        return

    selected_item = random.choice(items)
    await ctx.send(f"🎉 The wheel spins and lands on: **{selected_item}**!")

@bot.event
async def on_ready():
    print(f"Bot is ready. Logged in as {bot.user}")

bot.run('YOUR_BOT_TOKEN')