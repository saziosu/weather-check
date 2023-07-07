import os
from dotenv import load_dotenv, dotenv_values
import requests
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
HISTORY_URL_BASE = ("https://api.openweathermap.org/data/3.0/onecall/\
timemachine?")


def welcome_message():
    """
    Welcomes the user, gives description of the image.
    Displays ascii art to the user.
    """
    cprint(displays.TITLE, "blue")
    cprint(displays.UMBRELLA, "yellow")
    cprint(f"\nWelcome to Weather Check!\n", "green")
    cprint(
        "{} {}".format(
            "Weather Check is an app to check the current,",
            "past and forecasted weather."
        ),
        "green"
    )
    cprint(f"Past weather data can be checked up to 8 days", "green")
    cprint(f"Weather forecast data can be checked from 01/01/1979.\n", "green")


def city_check(city_select):
    """
    Runs the user's city through the OpenWeather API, returns the 
    longitude and latitude. Confirms the user's input and checks that the 
    API url returns a 200 response.
    """
    location = requests.get(
        f"{LOCATION_URL_BASE}{city_select}&limit=1&appid={API}")
    location_status = location.status_code
    # Set API data to json format
    location_detail = location.json()[0]
    latitude = location_detail["lat"]
    longitude = location_detail["lon"]
    country = location_detail["country"]
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
    # Set API data to json format
    weather_data = weather.json()
    sky = weather_data["weather"][0]["description"]
    current_temp_k = weather_data["main"]["temp"]
    # Converts the temperature in kelvins to celius
    current_temp_c = round(current_temp_k - 273.15)
    feels_k = weather_data["main"]["feels_like"]
    feels_c = round(feels_k - 273.15)
    hum = weather_data["main"]["humidity"]
    # Sunrise & Sunset times are converted to city's local time
    sunrise = str(datetime.fromtimestamp(
        weather_data["sys"]["sunrise"] + weather_data["timezone"]))[-8:]
    sunset = str(datetime.fromtimestamp(
        weather_data["sys"]["sunset"] + weather_data["timezone"]))[-8:]
    wind_speed = weather_data["wind"]["speed"]
    clouds = weather_data["clouds"]["all"]
    # Details printed to the user
    cprint(f"Current weather:\n", "light_blue")
    if sky == "clear sky":
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
    # Set API data to json format
    forecast_data = forecast_check.json()
    forecast_day = forecast_data["daily"][fore_day_select]
    forecast_date = str(datetime.fromtimestamp(
        forecast_day["dt"] + forecast_data["timezone_offset"]))[:-8]
    forecast_summary = forecast_day["summary"]
    # Convert all temps to celsius
    for time, temp in forecast_day["temp"].items():
        forecast_day["temp"][time] = round(temp - 273.15)
    morning_temp_c = forecast_day["temp"]["morn"]
    day_temp_c = forecast_day["temp"]["day"]
    eve_temp_c = forecast_day["temp"]["eve"]
    night_temp_c = forecast_day["temp"]["night"]
    forecast_hum = forecast_day["humidity"]
    forecast_speed = forecast_day["wind_speed"]
    forecast_cloud = forecast_day["clouds"]
    # Prints weather data to the user
    cprint(f"\nChecking forecast for {fore_day_select} day(s) in \
            future\n", "light_yellow")
    cprint(f"Date chosen: {forecast_date}", "blue")
    print(f"{forecast_summary}")
    print(f"Cloud cover will be {forecast_cloud}%")
    print(f"Wind speed will be {forecast_speed}m/s")
    print(f"Morning temperature: {morning_temp_c}C")
    print(f"Day temperature: {day_temp_c}C")
    print(f"Evening temperature: {eve_temp_c}C")
    print(f"Night temperature: {night_temp_c}C")
    print(f"Humidity will be {forecast_hum}%")
    # If rain is not present, the API does not report this value.
    # If statemtent to prevent errors if there is no rain
    if "rain" in forecast_day:
        forecast_rain = forecast_day["rain"]
        print(f"There will be {forecast_rain}mm of rain")
    else:
        print("There will be 0mm of rain")


def weather_history(lat, long):
    """
    Gets the past weather details for the user's selected date.
    """
    cprint("\nYou can check past weather from 01/01/1979!", "light_green")
    cprint("Date format must be DD/MM/YYYY\n", "light_green")
    past_date = input("What date would you like to check the weather?\n")
    past_convert = datetime.strptime(past_date, "%d/%m/%Y")
    past_time = round(datetime.timestamp(past_convert))
    date_call = requests.get(
        f"{HISTORY_URL_BASE}lat={lat}&lon={long}&dt={past_time}&appid={API}")
    # Set API data to json format
    past_data = date_call.json()
    past_data_list = past_data["data"][0]
    past_main = past_data_list["weather"][0]["description"]
    past_cloud = past_data_list["clouds"]
    past_speed = past_data_list["wind_speed"]
    past_temp_c = round(past_data_list["temp"] - 273.15)
    past_hum = past_data_list["humidity"]
    past_sunrise = str(datetime.fromtimestamp(
        past_data_list["sunrise"] + past_data["timezone_offset"]))[-8:]
    past_sunset = str(datetime.fromtimestamp(
        past_data_list["sunset"] + past_data["timezone_offset"]))[-8:]
    # prints past weather data to the user
    print(f"\nOn this day there were some {past_main}")
    print(f"Cloud cover was {past_cloud}%")
    print(f"Wind speed was {past_speed}m/s")
    print(f"The temperature was {past_temp_c}C")
    print(f"The humidity was {past_hum}%")
    print(f"Sunrise: {past_sunrise} (City's local time)")
    print(f"Sunset: {past_sunset} (City's local time)")


def main():
    """
    Asks the user to input the city to be used by the app
    Gives navigation to the user
    """
    while True:
        # Requests user's city input and confirms validity
        try:
            city = input("Please enter your city: \n")
            city_check(city)
            break
        except IndexError:
            cprint("Invalid City, please try again", "red")
    latitude, longitude = city_check(city) # convert return tuple into variables
    # Loop all options after each selection
    while True:
        print(f"\nPlease choose an option:\n")
        print(f"1 - View current weather")
        print(f"2 - View weather forecast (up to 8 days)")
        print(f"3 - View past weather")
        print(f"4 - Choose a new city")
        try:
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
                cprint("Invalid selection, please try again\n", "red")
        except ValueError:
            cprint("Invalid selection. Please try again.", "red")


welcome_message()
main()
