from django.views.generic import TemplateView
from django.shortcuts import render
import urllib.parse
import urllib.request
import json
from datetime import datetime

# Create your views here.


class WeatherView(TemplateView):

    template_name = 'errors/500.html'


# def search_weather(request):
#     if request.method == 'POST':
#         city = urllib.parse.quote_plus(request.POST['city'])
#         source = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q=' +
#                                         city + '&units=metric&appid=8cc5e423f92f5911e4369f44a1e605be').read()
#         list_of_data = json.loads(source)
        
#         data = {
#             "city": city,
#             "dt": (list_of_data['dt']),
#             "temp": str(list_of_data['main']['temp']) + ' °C',
#             "humidity": str(list_of_data['main']['humidity']),
#             "wind": str(list_of_data['wind']['speed']*2),
#             "pressure": str(list_of_data['main']['pressure']),
#             "timezone": (list_of_data['timezone']),
#             "description": str(list_of_data['weather'][0]['description']),
#             "icon": str(list_of_data['weather'][0]['icon']),
#         }

#         dt = data['dt']
#         timezone = data['timezone']
#         current_time = utctime_and_timezone(dt + timezone)
#         print(current_time)

#         data = {
#             "city": city,
#             "dt": (list_of_data['dt']),
#             "temp": str(list_of_data['main']['temp']) + ' °C',
#             "humidity": str(list_of_data['main']['humidity']),
#             "wind": str(list_of_data['wind']['speed']*2),
#             "pressure": str(list_of_data['main']['pressure']),
#             "timezone": (list_of_data['timezone']),
#             "description": str(list_of_data['weather'][0]['description']),
#             "icon": str(list_of_data['weather'][0]['icon']),
#             "current_time": current_time,
#         }

#     else:
#         data = {}
    
#     return render(request, "weather.html", data)


def utctime_and_timezone(utc_with_tz):
    local_time = datetime.utcfromtimestamp(utc_with_tz)
    return local_time.time()



