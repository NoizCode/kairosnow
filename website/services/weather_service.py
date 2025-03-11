import requests
import json

API_KEY = "c97a89a1a175f935e3f864807e4643f4"

response = requests.get(f"http://api.openweathermap.org/data/2.5/forecast?q=Athens&appid={API_KEY}")

# PRETTY PRINT JSON
json_data = json.dumps(response.json(), indent=4) 
print(json_data)

weather_data = {}

for item in response.json()["list"]:
    print(item)
    if "dt_txt" in item:
        weather_data[item["dt_txt"]] = ""
