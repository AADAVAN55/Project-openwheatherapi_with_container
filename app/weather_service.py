import os
import requests
from dotenv import load_dotenv

load_dotenv()

async def get_weather_data(location: str):
    api_key = os.getenv("OPENWEATHER_API_KEY")
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise exception for HTTP errors
        data = response.json()
        weather_description = data["weather"][0]["description"].capitalize()
        temperature = data["main"]["temp"]
        return f"Current weather in {location}: {weather_description}, {temperature}°C."
    except requests.RequestException as e:
        return "Failed to fetch weather data."
