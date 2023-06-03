import discord
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext
import requests

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

bot = commands.Bot(intents=intents)
slash = SlashCommand(bot, sync_commands=True)

@slash.slash(name="weather", description="Get current weather information for a location.")
async def weather(ctx: SlashContext, location: str):
    api_key = "9588b4704e8c71a376dcfcc14b5eed5d"  # Replace with your OpenWeatherMap API key
    api_url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"

    response = requests.get(api_url)
    data = response.json()

    if response.status_code == 200:
        city = data['name']
        country = data['sys']['country']
        weather_desc = data['weather'][0]['description']
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']

        weather_info = f"🌍 Location: {city}, {country}\n" \
                       f"☁️ Weather: {weather_desc}\n" \
                       f"🌡️ Temperature: {temp}°C\n" \
                       f"💧 Humidity: {humidity}%\n" \
                       f"🌬️ Wind Speed: {wind_speed} m/s"

        await ctx.send(weather_info)
    else:
        await ctx.send("Failed to fetch weather information.")

@bot.event
async def on_ready():
    print(f"Bot is ready. Logged in as {bot.user}")

bot.run('YOUR_BOT_TOKEN')
