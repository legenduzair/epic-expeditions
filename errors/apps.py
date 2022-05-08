""" System Module """
from django.apps import AppConfig


class ErrorsConfig(AppConfig):
    """ Add configuration for Errors app """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'errors'
