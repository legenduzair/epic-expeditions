from django.shortcuts import render
from django.views.generic import ListView
from .models import TravelReview

# Create your views here.

class HomeView(ListView):
    model = TravelReview
    template_name = 'home.html'

# class TravelReviewList(ListView):
#     model = TravelReview
#     template_name = #
#     ordering = ['-published']
#     paginate_by = 8


