import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from website import db, create_app
from website.models import City, Timestamp
from datetime import datetime
import requests
import json

API_KEY = "c97a89a1a175f935e3f864807e4643f4"
city = "Athens"

response = requests.get(f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}")

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

app = create_app()

with app.app_context():
    city_add = City(name=city)
    db.session.add(city_add)
    db.session.commit()

    for key,value in weather_data.items():
        timestamp = datetime.strptime(key, "%Y-%m-%d %H:%M:%S")

        temp_data = value[0]
        main_weath = value[1]
        wind_data = value[2]

        new_timestamp = Timestamp(
            city_id  = city_add.id,
            temp = temp_data["temp"],
            feels_like = temp_data["feels_like"],
            temp_min = temp_data["temp_min"],
            temp_max = temp_data["temp_max"],
            humidity = temp_data["humidity"],
            main_weath = main_weath[0]["main"],
            main_desc = main_weath[0]["description"],
            wind_speed = wind_data["speed"]
        )
        db.session.add(new_timestamp)

    db.session.commit()