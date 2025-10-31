import requests
import json

def display_weather_details_with_error_handling(city_name):
    api_key = "f630cb1cc555f6d13d9fae45e0db6712"  # Replace with your actual OpenWeatherMap API key
    base_url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric'
    }
    try:
        response = requests.get(base_url, params=params, timeout=10)
        response.raise_for_status()
        weather_data = response.json()
        # OpenWeatherMap returns code 401 for invalid API key, and code 404 for city not found
        if weather_data.get('cod') != 200:
            print("Error: Could not connect to API. Check your API key or network connection.")
        else:
            print(json.dumps(weather_data, indent=4))
    except requests.exceptions.RequestException:
        print("Error: Could not connect to API. Check your API key or network connection.")

if __name__ == "__main__":
    city = input("Enter city name: ")
    display_weather_details_with_error_handling(city)
