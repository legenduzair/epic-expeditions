from django.test import TestCase
from .forms import TravelReviewForm, TravelCommentsForm


class CreateTravelReviewTest(TestCase):
    """Travel Review Creation Test"""
    def test_createreview_valid(self):
        """Test to observe if travel review form is valid"""
        form = TravelReviewForm(data={
            "title": "titletest",
            "travel_image": "travelimagetest",
            "excerpt": "excerpt",
            "content": "contenttest",
            "ratings": 1
        })
        self.assertTrue(form.is_valid())

    def test_createreview_invalid(self):
        """Test to observe if travel review form is invalid"""
        form = TravelReviewForm(data={
            "content": ""
        })
        self.assertFalse(form.is_valid())


class CreateTravelCommentsTest(TestCase):
    """Travel Comments Creation Test"""
    def test_createcomments_valid(self):
        """Test to observe if travel comments form is valid"""
        form = TravelCommentsForm(data={
            "body": "commentstest"
        })
        self.assertTrue(form.is_valid())

    def test_createcomments_invalid(self):
        """Test to observe if travel comments form is invalid"""
        form = TravelCommentsForm(data={
            "body": ""
        })
        self.assertFalse(form.is_valid())
