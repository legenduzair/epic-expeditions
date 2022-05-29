"""System Module"""
from django.test import TestCase


class UrlTest(TestCase):
    """URL Loading Test"""
    def test_reviewlist_url(self):
        """Test to observe if review list URL is loading correctly"""
        response = self.client.get('/review_list')
        self.assertEqual(response.status_code, 301)

    def test_reviewdetail_url(self):
        """Test to observe if add review URL is loading correctly"""
        response = self.client.get('/add_review')
        self.assertEqual(response.status_code, 301)
