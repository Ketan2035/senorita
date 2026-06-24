import requests
from config import OPENWEATHER_API_KEY
def get_weather(city):

    api_key = OPENWEATHER_API_KEY

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

    data = requests.get(url).json()

    if "main" in data:
        temp = data["main"]["temp"] - 273.15
        return f"{city} temperature is {temp:.1f} degree Celsius"

    return "Weather data not found"