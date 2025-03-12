import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

import requests
import json

API_KEY = "c97a89a1a175f935e3f864807e4643f4"

response = requests.get(f"http://api.openweathermap.org/data/2.5/forecast?q=Athens&appid={API_KEY}")

# PRETTY PRINT JSON
json_data = json.dumps(response.json(), indent=4) 
#print(json_data)

weather_data = {}
data = [] # Temporarily store "main" and "weather" data

for item in response.json()["list"]:
    data.extend([item["main"], item["weather"], item["wind"]])
    weather_data[item["dt_txt"]] = data
    data = []

for key in weather_data:
    print("\n")
    print(key,":", weather_data[key])