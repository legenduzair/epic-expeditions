""" System Module """
from django.apps import AppConfig


class ReviewConfig(AppConfig):
    """ Add configuration to Review app """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'review'
