import requests

def get_user_input():
    city = input("Enter the name of the city: ")
    if city.lower() == 'exit':
        return None
    elif not city:
        print("City name cannot be empty. Please enter a valid city name.")
        return None
    return city

def get_temperature_in_unit(kelvin_temp, unit='Celsius'):
    if unit == 'Celsius':
        return round(kelvin_temp - 273.15, 2)
    elif unit == 'Fahrenheit':
        return round((kelvin_temp - 273.15) * 9/5 + 32, 2)
    elif unit == 'Kelvin':
        return round(kelvin_temp, 2)
    else:
        print(f"Unsupported temperature unit: {unit}. Using Celsius by default.")
        return round(kelvin_temp - 273.15, 2)

def display_weather_info(city, weather, temperature, unit='Celsius'):
    print(f"\nWeather information for {city}:")
    print(f"Weather: {weather.capitalize()}")
    print(f"Temperature: {temperature} {unit}")
    print("-" * 30)

def main():
    API_KEY = '1de6412cc72e9f00191c9ebdadd8575d'
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

    while True:
        city = get_user_input()
        if not city:
            break

        unit = input("Enter temperature unit (Celsius/Fahrenheit/Kelvin): ").capitalize()

        request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
        response = requests.get(request_url)

        if response.status_code == 200:
            data = response.json()
            weather = data['weather'][0]['description']
            temperature = get_temperature_in_unit(data["main"]["temp"], unit)
            display_weather_info(city, weather, temperature, unit)
        elif response.status_code == 404:
            print("City not found. Please check the city name and try again.")
        else:
            print(f"An error occurred. Status Code: {response.status_code}")

if __name__ == "__main__":
    main()





