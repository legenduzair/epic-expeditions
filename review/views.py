from django.shortcuts import render
from django.views.generic import ListView
from .models import TravelReview
from .forms import TravelReviewForm
from django.shortcuts import get_object_or_404

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

def add_review(request):

    expedition = get_object_or_404(TravelReview, id=expedition_id)
    if request.method == 'POST':
        review_form = TravelReviewForm(request.POST or None)

        if review_form.is_valid():
            data = form.save(commit=False)
            data.user = request.user
            data.expedition = expedition
            data.save()
            messages.success(request, 'Your review has been posted successfully!')
            return redirect('review_detail', expedition.id)
        else:
            form = TravelReviewForm()
            messages.error(request, 'Your review has failed to post. Please try again.')

        context = {'form': form}

        return render(request, context)




