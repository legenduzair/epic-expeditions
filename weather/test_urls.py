"""System Module"""
from django.test import TestCase


class UrlWeatherTest(TestCase):

    def test_weather_url(self):

        response = self.client.get('')
        self.assertEqual(response.status_code, 200)