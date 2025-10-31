import requests
import json

def display_weather_details(city_name):
    api_key = "f630cb1cc555f6d13d9fae45e0db6712"  # Replace with your OpenWeatherMap API key
    base_url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric'
    }
    response = requests.get(base_url, params=params)
    weather_data = response.json()
    print(json.dumps(weather_data, indent=4))

if __name__ == "__main__":
    city = input("Enter city name: ")
    display_weather_details(city)
