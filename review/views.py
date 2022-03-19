from django.shortcuts import get_object_or_404, render, redirect, reverse
from django.contrib import messages
from django.views.generic import ListView
from .models import TravelReview
from .forms import TravelReviewForm, TravelCommentsForm


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
    template_name = 'review_detail.html'
    expedition = get_object_or_404(TravelReview, pk=expedition_id)
    # form = TravelReviewForm()
    comments = expedition.comments.filter(active=True)
    new_comment = None

    if request.method == 'POST':
        comment_form = TravelCommentsForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.expedition = expedition
            new_comment.save()
    else:
        comment_form = TravelCommentsForm()

    context = {
        "expedition": expedition,
        # "form": form,
        "comments": comments,
        "new_comment": new_comment,
        "comment_form": comment_form,
    }

    return render(request, template_name, context)


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

    return render(request, 'add_review.html', {'form': form, 'controller':'Add Review'})


def edit_review(request, expedition_id):
    expedition = TravelReview.objects.get(pk=expedition_id)

    if request.method == 'POST':
        form = TravelReviewForm(request.POST, instance=expedition)

        if form.is_valid():
            form.save()
            messages.info(request, 'Your review has been updated!')
            return redirect('review_detail', expedition_id)

        else:
            messages.error(request, 'Your review was not updated. Please try again.')
        
    else:
        form = TravelReviewForm(instance=expedition)
    return render(request, 'add_review.html', {'form': form, 'controller':'Edit Review'})


def delete_review(request, expedition_id):
    expedition = TravelReview.objects.get(pk=expedition_id)

    expedition.delete()
    return redirect(reverse('review_list'))