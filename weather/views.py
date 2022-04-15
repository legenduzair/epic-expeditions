from django.views.generic import TemplateView

# Create your views here.


class WeatherView(TemplateView):

    template_name = 'weather.html'
