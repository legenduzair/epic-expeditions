from django.urls import path
from .views import HomeView, TravelReviewList
from . import views

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('review_list/', TravelReviewList.as_view(), name='review_list')
]