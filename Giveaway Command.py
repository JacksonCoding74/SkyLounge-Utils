import discord
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils import manage_components
from discord_slash.model import ButtonStyle

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

bot = commands.Bot(intents=intents)
slash = SlashCommand(bot, sync_commands=True)

giveaway_data = {}  # Stores giveaway information

@slash.slash(name="creategiveaway", description="Create a giveaway with specified number of winners.")
async def create_giveaway(ctx: SlashContext, winners: int):
    giveaway_embed = discord.Embed(title="🎉 Giveaway", description="React to participate!")
    giveaway_embed.add_field(name="Number of Winners", value=str(winners))
    giveaway_embed.add_field(name="Participants", value="0")
    giveaway_embed.add_field(name="Hosted By", value=ctx.author.display_name)

    message = await ctx.send(embed=giveaway_embed, components=[manage_components.create_button(
        style=ButtonStyle.green, label="Join Giveaway", custom_id="giveaway_join")])

    giveaway_data[message.id] = {
        "winners": winners,
        "participants": set(),
        "host": ctx.author.display_name
    }

@bot.event
async def on_button_click(interaction):
    if interaction.custom_id == "giveaway_join":
        message_id = interaction.message.id
        if message_id in giveaway_data:
            giveaway = giveaway_data[message_id]
            participant = interaction.user
            giveaway["participants"].add(participant)
            participants_count = len(giveaway["participants"])
            winners_count = giveaway["winners"]
            host = giveaway["host"]

            giveaway_embed = interaction.message.embeds[0]
            giveaway_embed.set_field_at(1, name="Participants", value=str(participants_count), inline=False)

            await interaction.message.edit(embed=giveaway_embed)

            if participants_count >= winners_count:
                winners = "\n".join([participant.display_name for participant in
                                     random.sample(giveaway["participants"], winners_count)])
                result_embed = discord.Embed(title="🎉 Giveaway Results",
                                             description=f"Congratulations to the winners!\n\n{winners}")
                result_embed.add_field(name="Hosted By", value=host)
                await interaction.message.edit(content="🎉 **Giveaway Ended!**", embed=result_embed,
                                               components=[])

@bot.event
async def on_ready():
    print(f"Bot is ready. Logged in as {bot.user}")

bot.run('YOUR_BOT_TOKEN')