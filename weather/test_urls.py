"""System Module"""
from django.test import TestCase


class UrlWeatherTest(TestCase):
    """URL Loading Test"""
    def test_weather_url(self):
        """Test to observe if weather page URL is loading correctly"""
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
