from django.urls import path
from .views import HomeView
from . import views

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('review_list', views.all_expeditions, name='expeditions')
]