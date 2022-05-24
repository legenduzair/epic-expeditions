from django.test import TestCase
from django.contrib.auth.models import User
from .models import TravelReview, TravelComments


class TestModels(TestCase):
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
            published='May 24, 2022',
            ratings='1')
        self.comments = TravelComments.objects.create(
            post='Marrakesh',
            name=user,
            body='Comments test',
            created_on='May 24, 2022, 13:05 p.m.'
        )