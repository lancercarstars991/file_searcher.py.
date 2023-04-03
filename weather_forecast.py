import requests
from pprint import pprint

city = input("Enter a city: ")

url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=your_api_key&units=metric"

res = requests.get(url)

data = res.json()

temp = data["main"]["temp"]
desc = data["weather"][0]["description"]
humidity = data["main"]["humidity"]
wind_speed = data["wind"]["speed"]

print(f"\nTemperature: {temp}°C\nDescription: {desc}\nHumidity: {humidity}%\nWind Speed: {wind_speed} km/h")
