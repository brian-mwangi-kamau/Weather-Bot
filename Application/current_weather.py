import requests
import os
from datetime import datetime 
from dotenv import load_dotenv
load_dotenv()
import pytz

BASE_URL = 'https://api.openweathermap.org/data/2.5/weather?'
API_KEY = os.environ['API_KEY']

city = input("Enter your city's name: ")

url = BASE_URL + 'appid=' + API_KEY + '&q=' + city

response = requests.get(url).json()

def kelvin_to_celcius(kelvin):
    celcius = kelvin - 273.15
    return celcius


temp_kelvin = response['main']['temp']
temp_celcius = kelvin_to_celcius(temp_kelvin)
wind_speed = response['wind']['speed']
description = response['weather'][0]['description']
timestamp = response['dt']

real_time_utc = datetime.utcfromtimestamp(timestamp)

nairobi_timezone = pytz.timezone("Africa/Nairobi")
real_time_nairobi = real_time_utc.replace(tzinfo=pytz.UTC).astimezone(nairobi_timezone)
# print(response)

hour = real_time_nairobi.hour
minute = real_time_nairobi.minute
second = real_time_nairobi.second

if hour < 12:
    if minute < 10:
        print(f"{hour}:0{minute} a.m, {city}")
    else:
        print(f"{hour}:{minute} a.m, {city}")
else:
    if minute < 10:
        print(f"{hour}:0{minute} p.m, {city}")
    else:
        print(f"{hour}:{minute} p.m, {city}")


print(f"The temperature in {city} is {temp_celcius:.2f}°C")
print(f"The wind is moving at {wind_speed}m/s")
print(f"There is some {description}")

# if description == 'light rain':
#     print("Carry your umbrellas fellas!")
# else:
#     print("What a day!")
