""" System Module """
import urllib.parse
import urllib.request
import json
from datetime import datetime
import math
from django.shortcuts import render


def search_weather(request):
    """ A view to use openweathermap API to
    search for current weather of any city in the world """

    if request.method == 'POST':
        city = (request.POST['city'])
        api_main = 'https://api.openweathermap.org/data/2.5/weather?q='
        api_units = '&units=metric&appid=8cc5e423f92f5911e4369f44a1e605be'
        url = api_main + city + api_units
        replace_url = url.replace(" ", "%20")
        source = urllib.request.urlopen(replace_url).read()
        list_of_data = json.loads(source)

        data = {
            "city": city,
            "dt": (list_of_data['dt']),
            "country_code": str(list_of_data['sys']['country']),
            "temp": (list_of_data['main']['temp']),
            "humidity": str(list_of_data['main']['humidity']),
            "wind": str(list_of_data['wind']['speed']*2),
            "pressure": str(list_of_data['main']['pressure']),
            "timezone": (list_of_data['timezone']),
            "description": str(list_of_data['weather'][0]['description']),
            "icon": str(list_of_data['weather'][0]['icon']),
        }

        temp = data['temp']
        rounded_temp = math.floor(temp)
        full_temp = str(rounded_temp) + ' °C'
        dt = data['dt']
        timezone = data['timezone']
        current_time = utctime_and_timezone(dt + timezone)
        print(current_time)

        data = {
            "city": city,
            "dt": (list_of_data['dt']),
            "country": str(list_of_data['sys']['country']),
            "temp": full_temp,
            "humidity": str(list_of_data['main']['humidity']),
            "wind": str(list_of_data['wind']['speed']*2),
            "pressure": str(list_of_data['main']['pressure']),
            "timezone": (list_of_data['timezone']),
            "description": str(list_of_data['weather'][0]['description']),
            "icon": str(list_of_data['weather'][0]['icon']),
            "current_time": current_time,
        }

    else:
        data = {}

    return render(request, "weather.html", data)


def utctime_and_timezone(utc_with_tz):
    """A view to convert timezone and dt UTC values to current time"""
    local_time = datetime.utcfromtimestamp(utc_with_tz)
    return local_time.time()
