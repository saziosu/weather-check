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
    if location_status == 200:
        print(f"Great! Checking weather for {city}...")
    else:
        print("Error found, please run again")
    return latitude, longitude


main()