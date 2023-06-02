import discord
from discord_slash import SlashCommand, SlashContext
import psutil
import datetime

# Create a new Discord bot instance
bot = discord.Client(intents=discord.Intents.default())
slash = SlashCommand(bot, sync_commands=True)

@bot.event
async def on_ready():
    print(f'Bot is ready. Connected to Discord as {bot.user.name}')

@slash.slash(name="stats", description="Display system statistics")
async def stats(ctx: SlashContext):
    cpu_load = get_cpu_load()
    ram_usage = get_ram_usage()
    storage_usage = get_storage_usage()
    network_usage = get_network_usage()
    uptime = get_uptime()

    stats_message = (
        f"CPU Load: {cpu_load}%\n"
        f"RAM Usage: {ram_usage}%\n"
        f"Storage Usage: {storage_usage}%\n"
        f"Network Usage: {network_usage}\n"
        f"Uptime: {uptime}"
    )

    await ctx.send(stats_message)

def get_cpu_load():
    return psutil.cpu_percent(interval=1)

def get_ram_usage():
    return psutil.virtual_memory().percent

def get_storage_usage():
    return psutil.disk_usage('/').percent

def get_network_usage():
    network = psutil.net_io_counters()
    return f"Sent: {convert_bytes(network.bytes_sent)} | Received: {convert_bytes(network.bytes_recv)}"

def get_uptime():
    uptime = datetime.datetime.now() - datetime.datetime.fromtimestamp(psutil.boot_time())
    return str(uptime)

def convert_bytes(bytes):
    if bytes < 1024:
        return f"{bytes} B"
    elif bytes < 1024**2:
        return f"{bytes/1024:.2f} KB"
    elif bytes < 1024**3:
        return f"{bytes/1024**2:.2f} MB"
    else:
        return f"{bytes/1024**3:.2f} GB"

# Replace 'YOUR_DISCORD_TOKEN' with your actual Discord bot token
bot.run('MTExNDI2NTg0MjUzNjkzOTY3MQ.GwP2_L._NgVIoAvvJBJaIuJTPrj8fGwJrPFW9inNovybM')
