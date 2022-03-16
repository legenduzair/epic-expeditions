from django.shortcuts import get_object_or_404, render, redirect, reverse
from django.contrib import messages
from django.views.generic import ListView
from .models import TravelReview
from .forms import TravelReviewForm


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


def review_detail(request, expedition_id):
    expedition = get_object_or_404(TravelReview, pk=expedition_id)
    form = TravelReviewForm

    context = {
        "expedition": expedition,
        "form": form,
    }

    return render(request, 'review_detail.html', context)

def add_review(request):

    # expedition = get_object_or_404(TravelReview, pk=expedition_id)
    if request.method == 'POST':
        form = TravelReviewForm(request.POST or None)

        if form.is_valid():
            data = form.save(commit=False)
            data.save()
            messages.success(request, 'Your review has been posted successfully!')
            return redirect(reverse('review_list'))
    else:
        form = TravelReviewForm()
        messages.error(request, 'Your review has failed to post. Please try again.')

    return render(request, 'add_review.html', {'form': form})




