"""System Module"""
from django.test import TestCase


class TestErrors(TestCase):
    """Test for testing the 404 page"""
    def test_page_not_found(self):
        """Test for observing if the URL below exists"""
        response = self.client.get('/review_detail/0/')
        self.assertEqual(response.status_code, 404)
