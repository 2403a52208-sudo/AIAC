import requests
import json
import os

def get_weather_info_and_save(city_name):
    api_key = "f630cb1cc555f6d13d9fae45e0db6712"  # Use your OpenWeatherMap API key
    base_url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric'
    }
    try:
        response = requests.get(base_url, params=params, timeout=5)
        data = response.json()
        if response.status_code == 200:
            city = data.get("name")
            temp = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            weather = data["weather"][0]["description"]

            # Print formatted data to console
            print(f"City: {city}")
            print(f"Temperature: {temp}°C")
            print(f"Humidity: {humidity}%")
            print(f"Weather: {weather.capitalize()}")

            # Prepare result for saving
            result = {
                "city": city,
                "temp": temp,
                "humidity": humidity,
                "weather": weather.capitalize()
            }

            # Load or create results.json
            results_file = "results.json"
            if os.path.exists(results_file):
                try:
                    with open(results_file, "r", encoding="utf-8") as f:
                        results_list = json.load(f)
                except Exception:
                    results_list = []
            else:
                results_list = []

            # Append new result and save back to file
            results_list.append(result)
            with open(results_file, "w", encoding="utf-8") as f:
                json.dump(results_list, f, indent=4)
        else:
            print("Error: City not found. Please enter a valid city name.")
    except Exception as e:
        print("Error while fetching weather data:", e)

if __name__ == "__main__":
    user_city = input("Enter city name: ")
    get_weather_info_and_save(user_city)

