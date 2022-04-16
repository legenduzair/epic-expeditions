from django.views.generic import TemplateView
from django.shortcuts import render
import urllib.request
import json

# Create your views here.


class WeatherView(TemplateView):

    template_name = 'weather.html'


def search_weather(request):
    if request.method == 'POST':
        city = request.POST['city']
        source = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q=' +
                                        city + '&units=metric&appid=8cc5e423f92f5911e4369f44a1e605be').read()
        list_of_data = json.loads(source)

        data = {
            "country_code": str(list_of_data['sys']['country']),
            "temp": str(list_of_data['main']['temp']) + ' °C',
            "pressure": str(list_of_data['main']['pressure']),
            "humidity": str(list_of_data['main']['humidity']),
            "main": str(list_of_data['weather'][0]['main']),
            "icon": str(list_of_data['weather'][0]['icon']),
        }
        print(data)
    else:
        data = {}
    
    return render(request, "weather.html", data)
