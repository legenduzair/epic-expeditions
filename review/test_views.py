"""System Module"""
from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import TravelReview, TravelComments


class TestViews(TestCase):
    """Base testing class to be used for other test cases"""
    def setUp(self):
        """Setup for testing models"""
        self.username = 'john'
        self.password = '54321'
        user = User.objects.create_user(
            username=self.username,
            email='john@doe.com',
            password=self.password)
        self.client.login(username='john', password='54321')
        self.expedition = TravelReview.objects.create(
            title='Marrakesh',
            author=user,
            content='Review test',
            excerpt='Excerpt test',
            published='2022-05-24',
            ratings='1').pk
        self.comments = TravelComments.objects.create(
            post=TravelReview.objects.get(id=self.expedition),
            name=user,
            body='Comments test',
            created_on='May 24, 2022, 13:05 p.m.'
            )


class ReviewDetailViewTest(TestViews):
    """Testing class to see if Review Detail view exists"""
    def test_review_detailhtml_exists(self):
        """Test to observe if review_detail html template exists"""
        response = self.client.get(
            '/review_detail/' + str(self.expedition))
        self.assertEqual(response.status_code, 301)


class AddReviewTest(TestViews):
    """Testing class to see if Add Review form is functional"""
    def test_addreviewform_valid(self):
        """Test to observe if add review form is operating
        and that it redirects to add_review URL"""
        self.client.login(username='john', password='54321')

        payload = {
            'title': 'Marrakesh',
            'travel_image': '',
            'excerpt': 'Excerpt Test',
            'content': 'Content Test',
            'ratings': '2'
        }
    
        response = self.client.post(reverse('add_review'), data=payload)
        self.assertEqual(response.status_code, 200)


class EditReviewUrlTest(TestViews):
    """Testing class to see if Edit Review URL is functional"""
    def test_editreview_url(self):
        """Test to observe if edit review URL is working"""
        response = self.client.get(
            '/edit_review/' + str(self.expedition))
        self.assertEqual(response.status_code, 301)


class DeleteReviewUrlTest(TestViews):
    """Testing class to see if Delete Review URL is functional"""
    def test_deletereview_url(self):
        """Test to observe if delete review URL is working"""
        response = self.client.get(
            '/delete_review/' + str(self.expedition))
        self.assertEqual(response.status_code, 200)
