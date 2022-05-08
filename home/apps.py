""" System Module """
from django.apps import AppConfig


class HomeConfig(AppConfig):
    """ Add configuration for Home app """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'home'
