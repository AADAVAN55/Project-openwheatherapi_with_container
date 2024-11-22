from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = FastAPI()

# Model for handling location input
class LocationRequest(BaseModel):
    location: str

@app.post("/api/get_weather")
async def get_weather(request: LocationRequest):
    location = request.location
    api_key = os.getenv("OPENWEATHER_API_KEY")
    
    # Construct the OpenWeatherMap API URL
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"

    # Make a request to the OpenWeatherMap API
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an error for HTTP codes 4xx/5xx
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail="Error connecting to the weather service.")

    # Parse the response from the API
    data = response.json()
    if response.status_code != 200 or "weather" not in data or "main" not in data:
        raise HTTPException(status_code=404, detail="Could not fetch weather data. Please check the location and try again.")

    # Extract weather details
    weather_description = data["weather"][0]["description"].capitalize()
    temperature = data["main"]["temp"]
    
    # Return formatted weather data
    return {"message": f"Current weather in {location}: {weather_description}, {temperature}°C."}
