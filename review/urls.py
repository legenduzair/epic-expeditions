from django.urls import path
from .views import TravelReviewList
from . import views

urlpatterns = [
    path('review_list/', TravelReviewList.as_view(), name='review_list'),
    path('review_detail/<expedition_id>/', views.review_detail, name='review_detail'),
    path('review_like/<expedition_id>/', views.TravelPostLike, name='review_like'),
    path('add_review/', views.add_review, name='add_review'),
    path('edit_review/<expedition_id>/', views.edit_review, name='edit_review'),
    path('delete_review/<expedition_id>', views.delete_review, name='delete_review'),
]