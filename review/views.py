from django.shortcuts import render
from django.views.generic import ListView
from .models import TravelReview

# Create your views here.

class TravelReviewList(ListView):
    model = TravelReview
    template_name = #
    ordering = ['-published']
    paginate_by = 8


