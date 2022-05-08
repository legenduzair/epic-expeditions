""" System Module """
from django.apps import AppConfig


class WeatherConfig(AppConfig):
    """ Add configuration for Weather app """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'weather'
