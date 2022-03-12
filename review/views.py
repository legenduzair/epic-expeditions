from django.shortcuts import render
from django.views.generic import ListView
from .models import TravelReview

# Create your views here.

class HomeView(ListView):
    model = TravelReview
    template_name = 'home.html'

# def all_expeditions(request):
#     expeditions = TravelReview.objects.all()

#     context = {
#         "expeditions": expeditions,
#     }

#     return render(request, 'review_list.html', context)

class TravelReviewList(ListView):
    model = TravelReview
    template_name = 'review_list.html'
    ordering = ['-published']
    paginate_by = 8


def review_detail(request, id):
    expedition = TravelReview.objects.get(id=id)

    context = {
        "expedition": expedition
    }

    return render(request, 'review_detail.html', context)



