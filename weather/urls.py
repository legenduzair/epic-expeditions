from django.urls import path
from .views import WeatherView
# from . import views

urlpatterns = [
    # path('', views.search_weather, name='weather'),
    path('', WeatherView.as_view(), name='weather'),
]