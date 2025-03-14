import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from sqlalchemy.orm import joinedload
from website import db, create_app
from website.models import City, Timestamp
from datetime import datetime
import requests
import json

API_KEY = "c97a89a1a175f935e3f864807e4643f4"
cities = ["Agrinio", "Athens", "Patra", "Kalamata", "Tripoli", "Thessaloniki", "Karpenisi", "Chalkis", "Volos"]
k = 273.15 # Kelvin to celsius conversion

for current_city in cities:
    response = requests.get(f"http://api.openweathermap.org/data/2.5/forecast?q={current_city}&appid={API_KEY}")

    ### PRETTY PRINT JSON ###
    #json_data = json.dumps(response.json(), indent=4) 
    #print(json_data)

    weather_data = {}
    data = [] # Temporarily store "main" and "weather" data

    for item in response.json()["list"]:    
        data.extend([item["main"], item["weather"], item["wind"]])
        weather_data[item["dt_txt"]] = data
        data = []

    ### Print data for debugging ###
    #for key in weather_data:
    #    print("\n")
    #    print(key,":", weather_data[key])

    app = create_app()

    with app.app_context():
        city_add = City(name=current_city)
        db.session.add(city_add)
        db.session.commit()

        for key,value in weather_data.items():

            time_date = datetime.strptime(key, "%Y-%m-%d %H:%M:%S")
            timestamp = time_date.strftime("%d-%m-%Y %H:%M:%S")

            temp_data = value[0]
            main_weath = value[1]
            wind_data = value[2]

            new_timestamp = Timestamp(
                city_id  = city_add.id,
                time = timestamp,
                temp = round(temp_data["temp"] - k),
                feels_like = round(temp_data["feels_like"] - k),
                temp_min = round(temp_data["temp_min"] - k),
                temp_max = round(temp_data["temp_max"] - k),
                humidity = temp_data["humidity"],
                main_weath = main_weath[0]["main"],
                main_desc = main_weath[0]["description"].capitalize(),
                wind_speed = wind_data["speed"],
                icon = str(f" https://openweathermap.org/img/wn/{main_weath[0]["icon"]}@2x.png")
            )
            db.session.add(new_timestamp)

        db.session.commit()
        print(f"Fetched data for {current_city} succesfully.\nCommited to the database.")