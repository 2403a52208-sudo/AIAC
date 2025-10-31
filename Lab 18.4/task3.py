import requests
def display_specific_weather_details(city_name):
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

        if weather_data.get('cod') != 200:
            print("Error: Could not retrieve weather data. Please check the city name and try again.")
            return
        city = weather_data.get('name', 'Unknown')
        main = weather_data.get('main', {})
        weather_list = weather_data.get('weather', [])
        temperature = main.get('temp', 'N/A')
        humidity = main.get('humidity', 'N/A')
        # Get the first weather description if available
        if weather_list and isinstance(weather_list, list):
            description = weather_list[0].get('description', 'N/A').capitalize()
        else:
            description = 'N/A'
        print(f"City: {city}")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Weather: {description}")

    except requests.exceptions.RequestException:
        print("Error: Could not connect to API. Check your API key or network connection.")
if __name__ == "__main__":
    city = input("Enter city name: ")
    display_specific_weather_details(city)
