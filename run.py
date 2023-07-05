import os
from dotenv import load_dotenv, dotenv_values
import requests
import time
from datetime import datetime
from termcolor import colored, cprint
import displays

"""
Load secret key API credentials
"""
load_dotenv()
API = os.getenv("API_KEY")

"""
API URLS
"""
LOCATION_URL_BASE = "http://api.openweathermap.org/geo/1.0/direct?q="
CITY_URL_BASE = "https://api.openweathermap.org/data/2.5/weather?"
FORECAST_URL_BASE = "https://api.openweathermap.org/data/3.0/onecall?"
FORECAST_EXCLUDE = "&exclude=minutely,hourly,current&appid="
HISTORY_URL_BASE = "https://api.openweathermap.org/data/3.0/onecall/timemachine?"


def welcome_message():
    cprint(displays.TITLE, "blue")
    cprint(displays.UMBRELLA, "yellow")
    cprint(f"\nWelcome to Weather Check!\n", "green")
    cprint(f"Weather Check is an app to check the current, past and forecasted weather.", "green")
    cprint(f"Past weather data can be checked up to 8 days", "green")
    cprint(f"Weather forecast data can be checked from 01/01/1979.\n", "green")


def city_check(city_select):
    '''
    Checks the validity of the User's input and pulls the
    latitude and longitude from their city input to return
    '''
    location = requests.get(
        f"{LOCATION_URL_BASE}{city_select}&limit=1&appid={API}")
    location_status = location.status_code
    location_detail = location.json()[0]
    latitude = location_detail['lat']
    longitude = location_detail['lon']
    country = location_detail['country']
    if location_status == 200:
        cprint(
            f"Great! Checking weather for {city_select},{country}.", "cyan")
    else:
        print("Error found, please try again later")
    
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
    sunrise = datetime.fromtimestamp(
        weather_data['sys']['sunrise'] + weather_data['timezone'])
    sunset = datetime.fromtimestamp(
        weather_data['sys']['sunset'] + weather_data['timezone'])
    wind_speed = weather_data['wind']['speed']
    clouds = weather_data['clouds']['all']
    cprint(f"Current weather:\n", "light_blue")
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
    print(f"Sunrise: {sunrise} (City's local time)")
    print(f"Sunset: {sunset} (City's local time)")

    return weather_data


def weather_forecast(lat, long):
    """
    Prints the weather forecast to the user.
    User can choose how many days in the future they would like to see
    the forecast for.
    """
    print("Looks like you're needing the weather forecast!")
    print(f"Please choose how many days in the future you would like to see.")
    print(f"Example: For tomorrow's forecast type 1.")
    fore_day_select = int(input("Make your selection:\n"))
    forecast_check = requests.get(
        f"{FORECAST_URL_BASE}lat={lat}&lon={long}{FORECAST_EXCLUDE}{API}")
    forecast_data = forecast_check.json()
    forecast_day = forecast_data["daily"][fore_day_select]
    forecast_date = datetime.fromtimestamp(
        forecast_day['dt'] + forecast_data["timezone_offset"])
    forecast_summary = forecast_day["summary"]
    for time, temp in forecast_day["temp"].items():
        forecast_day["temp"][time] = round(temp - 273.15)
    morning_temp_c = forecast_day["temp"]["morn"]
    day_temp_c = forecast_day["temp"]["day"]
    eve_temp_c = forecast_day["temp"]["eve"]
    night_temp_c = forecast_day["temp"]["night"]
    forecast_hum = forecast_day["humidity"]
    forecast_speed = forecast_day["wind_speed"]
    forecast_cloud = forecast_day["clouds"]
    cprint(f"\nChecking forecast for {fore_day_select} day(s) in future\n", "light_yellow")
    print(f"Date chosen: {forecast_date} (City's local time)")
    print(f"{forecast_summary}")
    print(f"Cloud cover will be {forecast_cloud}%")
    print(f"Wind speed will be {forecast_speed}m/s")
    print(f"Morning temperature: {morning_temp_c}C")
    print(f"Day temperature: {day_temp_c}C")
    print(f"Evening temperature: {eve_temp_c}C")
    print(f"Night temperature: {night_temp_c}C")
    print(f"Humidity will be {forecast_hum}%")
    if "rain" in forecast_day:
        forecast_rain = forecast_day["rain"]
        print(f"There will be {forecast_rain}mm of rain")
    else:
        print("There will be 0mm of rain")


def weather_history(lat, long):
    cprint("\nYou can check past weather from 01/01/1979!", "light_green")
    cprint("Date format must be DD/MM/YYYY\n", "light_green")
    past_date = input("What date would you like to check the weather?\n")
    past_convert = datetime.strptime(past_date, "%d/%m/%Y")
    past_time = round(datetime.timestamp(past_convert))
    date_call = requests.get(
        f"{HISTORY_URL_BASE}lat={lat}&lon={long}&dt={past_time}&appid={API}")
    past_data = date_call.json()
    past_data_list = past_data["data"][0]
    past_main = past_data_list["weather"][0]["description"]
    past_cloud = past_data_list["clouds"]
    past_speed = past_data_list["wind_speed"]
    past_temp_c = round(past_data_list["temp"] - 273.15)
    past_hum = past_data_list["humidity"]
    past_sunrise = datetime.fromtimestamp(
        past_data_list["sunrise"] + past_data['timezone_offset'])
    past_sunset = datetime.fromtimestamp(
        past_data_list["sunset"] + past_data['timezone_offset'])
    print(f"\nOn this day there were some {past_main}")
    print(f"Cloud cover was {past_cloud}%")
    print(f"Wind speed was {past_speed}m/s")
    print(f"The temperature was {past_temp_c}C")
    print(f"The humidity was {past_hum}%")
    print(f"Sunrise: {past_sunrise} (City's local time)")
    print(f"Sunset: {past_sunset} (City's local time)")


def main():
    welcome_message()
    while True:
        try:
            city = input("Please enter your city: \n")
            city_check(city)
            break
        except IndexError:
            print("Invalid City, please try again")
    latitude, longitude = city_check(city)
    while True:
        print(f"\nPlease choose an option:\n")
        print(f"1 - View current weather")
        print(f"2 - View weather forecast (up to 8 days)")
        print(f"3 - View past weather")
        print(f"4 - Restart program")
        key_press = int(input("Please enter your selection: \n"))
        if key_press == 1:
            get_current_weather(latitude, longitude)
        elif key_press == 2:
            weather_forecast(latitude, longitude)
        elif key_press == 3:
            weather_history(latitude, longitude)
        elif key_press == 4:
            print("\nOkay! Restarting...\n")
            main()
        else:
            print("Invalid selection, please try again\n")


main()
