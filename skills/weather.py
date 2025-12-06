import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("WEATHER_API")
DEFAULT_CITY = os.getenv("DEFAULT_CITY", "Hyderabad")
def get_weather(text=None):
    city = extract_city(text) if text else DEFAULT_CITY

    if not API_KEY:
        return f"No API key, can't fetch weather for {city}"

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    try:
        r = requests.get(url).json()
        if r.get("cod") != 200:
            return f"City '{city}' not found."

        temp = r["main"]["temp"]
        desc = r["weather"][0]["description"].capitalize()
        return f"Temperature in {city.title()}: {temp}°C, {desc}"

    except requests.exceptions.RequestException as e:
        return f"Weather fetch error: {e}"


def extract_city(text):
    text_lower = text.lower()
    phrases = [
        "what is the weather in",
        "what's the weather in",
        "is the weather in",
        "weather in",
        "what is weather in"
    ]
    for phrase in phrases:
        if phrase in text_lower:
            return text_lower.replace(phrase, "").strip().title()
    return text.split()[-1].title()  # fallback
  