import os
from dotenv import load_dotenv, dotenv_values
import requests
from datetime import datetime

"""
Load secret key API credentials
"""
load_dotenv()
API = os.getenv("API_KEY")

LOCATION_URL_BASE = "http://api.openweathermap.org/geo/1.0/direct?q="
CITY_URL_BASE = "https://api.openweathermap.org/data/2.5/weather?"
FORECAST_URL_BASE = "https://api.openweathermap.org/data/3.0/onecall?"

"""
full url
https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}9&exclude=minutely,hourly,current&appid={API}
"""


def city_check(city_select):
    '''
    Checks the validity of the User's input and pulls the
    latitude and longitude from their city input to return
    '''
    location = requests.get(f"{LOCATION_URL_BASE}{city_select}&limit=1&appid={API}")
    location_status = location.status_code
    location_detail = location.json()[0]
    latitude = location_detail['lat']
    longitude = location_detail['lon']
    country = location_detail['country']
    if location_status == 200:
        print(f"Great! Checking weather for {city_select}, {country}...")
    else:
        print("Error found, please run again")
    return latitude, longitude


def get_current_weather(lat, long):
    """
    Function to get the current weather of the city chosen by the user.
    Prints details of main weather, temperature and humidity
    """
    weather = requests.get(f"{CITY_URL_BASE}lat={lat}&lon={long}&appid={API}")
    weather_data = weather.json()
    sky = weather_data['weather'][0]['description']
    current_temp_k = weather_data['main']['temp']
    current_temp_c = round(current_temp_k - 273.15)
    feels_k = weather_data['main']['feels_like']
    feels_c = round(feels_k - 273.15)
    hum = weather_data['main']['humidity']
    sunrise = datetime.fromtimestamp(weather_data['sys']['sunrise'])
    sunset = datetime.fromtimestamp(weather_data['sys']['sunset'])
    wind_speed = weather_data['wind']['speed']
    clouds = weather_data['clouds']['all']
    print(f"Current weather:")
    if sky == 'clear sky':
        print(f"Today you have a lovely {sky}")
    else:
        print(f"Today you have some {sky}")
        print(f"Cloud cover is {clouds}%")
    print(f"Wind speed is {wind_speed} m/s")
    print(f"The current temperature is {current_temp_c}C")
    if current_temp_c != feels_c:
        print(f"It feels like {feels_c}C")
    print(f"Humidity is {hum}%")
    print(f"Sunrise: {sunrise} UTC")
    print(f"Sunset: {sunset} UTC")

    return weather_data


def weather_forecast(lat, long):
    print("Looks like you're needing the weather forecast!")
    print(f"Please choose how many days in the future you would like to see.")
    print(f"Example: For tomorrow's forecast type 1.")
    fore_day_count = int(input("Make your selection:"))
    forecast_check = requests.get(f"{FORECAST_URL_BASE}lat={lat}&lon={long}&exclude=minutely,hourly,current&appid={API}")
    forecast_data = forecast_check.json()
    print(f"Checking forecast for {fore_day_count} day in future")


def main():
    print(f"Welcome to Weather Check!\n")
    city = input("Please enter your city: \n")
    city_check(city)
    latitude, longitude = city_check(city)
    print(f"Please choose an option:\n")
    print(f"1 - View current weather")
    print(f"2 - View weather forecast (up to 8 days)")
    print(f"3 - View past weather")
    print(f"4 - Exit program")
    key_press = int(input("Please enter your selection: \n"))
    if key_press == 1:
        get_current_weather(latitude, longitude)
    elif key_press == 2:
        weather_forecast(latitude, longitude)
    elif key_press == 3:
        print("Coming soon...")
    elif key_press == 4:
        close = str(input("Are you sure you want to finish? (y/n)\n"))
        if close == "y":
            exit()
        else:
            print("restarting...")
    else:
        print("Error, invalid selection")


main()
