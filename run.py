import requests
import datetime

API = open("credentials", "r").read()
LOCATION_URL_BASE = "http://api.openweathermap.org/geo/1.0/direct?q="
""" 
full url for location is
http://api.openweathermap.org/geo/1.0/direct?q={cityname}&limit={limit}&appid={APIkey}
"""
CITY_URL_BASE = "https://api.openweathermap.org/data/2.5/weather?"

"""
full url for current weather is
https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={APIkey}
"""


def city_check():
    '''
    Checks the validity of the User's input and pulls the
    latitude and longitude from their city input to return
    '''
    city = input("Please enter your city: \n")
    location = requests.get(f"{LOCATION_URL_BASE}{city}&limit=1&appid={API}")
    location_status = location.status_code
    location_detail = location.json()[0]
    latitude = location_detail['lat']
    longitude = location_detail['lon']
    country = location_detail['country']
    if location_status == 200:
        print(f"Great! Checking weather for {city}, {country}...")
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
    print(f"Current weather:")
    if sky == 'clear sky':
        print(f"Today you have a lovely {sky}")
    else:
        print(f"Today you have some {sky}")
    print(f"The current temperature is {current_temp_c}C")
    if current_temp_c != feels_c:
        print(f"It feels like {feels_c}C")
    print(f"Humidity is {hum}%")

    return weather_data


def main():
    latitude, longitude = city_check()
    get_current_weather(latitude, longitude)
    

main()
