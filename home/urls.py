from django.urls import path
from .views import HomeView

urlpatterns = [
    path('weather/', HomeView.as_view(), name='home'),
]