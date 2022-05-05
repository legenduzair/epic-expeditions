from django.shortcuts import render
import urllib.parse
import urllib.request
import json
from datetime import datetime

# Create your views here.


def search_weather(request):
    if request.method == 'POST':
        city = (request.POST['city'])
        url = 'https://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=metric&appid=8cc5e423f92f5911e4369f44a1e605be'
        replace_url = url.replace(" ", "%20")
        source = urllib.request.urlopen(replace_url).read()
        list_of_data = json.loads(source)
        
        data = {
            "city": city,
            "dt": (list_of_data['dt']),
            "temp": str(list_of_data['main']['temp']) + ' °C',
            "humidity": str(list_of_data['main']['humidity']),
            "wind": str(list_of_data['wind']['speed']*2),
            "pressure": str(list_of_data['main']['pressure']),
            "timezone": (list_of_data['timezone']),
            "description": str(list_of_data['weather'][0]['description']),
            "icon": str(list_of_data['weather'][0]['icon']),
        }

        dt = data['dt']
        timezone = data['timezone']
        current_time = utctime_and_timezone(dt + timezone)
        print(current_time)

        data = {
            "city": city,
            "dt": (list_of_data['dt']),
            "temp": str(list_of_data['main']['temp']) + ' °C',
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
    local_time = datetime.utcfromtimestamp(utc_with_tz)
    return local_time.time()



