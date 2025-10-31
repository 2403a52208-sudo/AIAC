import requests

def get_weather_info(city_name):
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
            print(f"City: {city}")
            print(f"Temperature: {temp}°C")
            print(f"Humidity: {humidity}%")
            print(f"Weather: {weather.capitalize()}")
        else:
            print("Error: City not found. Please enter a valid city name.")
    except Exception as e:
        print("Error while fetching weather data:", e)

if __name__ == "__main__":
    user_city = input("Enter city name: ")
    get_weather_info(user_city)
