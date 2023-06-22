import requests
import datetime

API_CRED = open("credentials", "r").read()
LOCATION_URL = "http://api.openweathermap.org/geo/1.0/direct?q="
""" 
full url for location is http://api.openweathermap.org/geo/1.0/direct?q={city name}&limit={limit}&appid={API key}
"""
CITY_URL = "https://api.openweathermap.org/data/2.5/weather?"

"""
full url for current weather is https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}
"""

