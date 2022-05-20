""" System Module """
from django.shortcuts import get_object_or_404, render, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.http import HttpResponseRedirect
from .models import TravelReview
from .forms import TravelReviewForm, TravelCommentsForm


class TravelReviewList(ListView):
    """Class-based view to list expedition review list page """

    model = TravelReview
    template_name = 'review_list.html'
    ordering = ['-published']
    paginate_by = 8


def review_detail(request, expedition_id):
    """ A view to render the expedition detail page
    with comments and likes displayed """

    template_name = 'review_detail.html'
    expedition = get_object_or_404(TravelReview, pk=expedition_id)
    comments = expedition.comments.order_by("-created_on")
    new_comment = None
    liked = False
    if expedition.likes.filter(pk=request.user.id).exists():
        liked = True

    if request.method == 'POST':
        comment_form = TravelCommentsForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.name = request.user.username
            new_comment = comment_form.save(commit=False)
            new_comment.post = expedition
            new_comment.save()
            messages.success(request, 'Your comment has been posted!')
    else:
        comment_form = TravelCommentsForm()

    context = {
        "expedition": expedition,
        "comments": comments,
        "new_comment": new_comment,
        "comment_form": comment_form,
        "liked": liked
    }

    return render(request, template_name, context)


@login_required
def add_review(request):
    """ A view to add an expedition review to the list of reviews """

    if request.method == 'POST':
        form = TravelReviewForm(request.POST, request.FILES or None)

        if form.is_valid():
            data = form.save(commit=False)
            data.author = request.user
            data.save()
            messages.success(
                request, 'Your review has been posted successfully!')
            return redirect(reverse('review_list'))
    else:
        form = TravelReviewForm()

    return render(
        request, 'add_review.html', {'form': form, 'controller': 'Add Review'})

@login_required
def edit_review(request, expedition_id):
    """ A view to edit an expedition review """

    expedition = TravelReview.objects.get(pk=expedition_id)

    if request.method == 'POST':
        form = TravelReviewForm(request.POST, instance=expedition)

        if form.is_valid():
            form.save()
            messages.success(
                request, 'Your review has been updated successfully!')
            return redirect('review_detail', expedition_id)

        else:
            messages.error(
                request, 'Your review was not updated. Please try again.')

    else:
        form = TravelReviewForm(instance=expedition)
    return render(
        request, 'add_review.html',
        {'form': form, 'controller': 'Edit Review'})

@login_required
def delete_review(request, expedition_id):
    """ A view to delete an expedition review """

    expedition = TravelReview.objects.get(pk=expedition_id)

    if request.method == 'POST':
        expedition.delete()
        messages.success(request, 'Your review has been deleted!')
        return redirect(reverse('review_list'))

    context = {
        "expedition": expedition,
    }
    return render(request, 'delete_review.html', context)

@login_required
def post_like(request, expedition_id):
    """ A view to add/remove a like to an expedition review """

    post_id = request.POST.get('review_id')
    post = get_object_or_404(TravelReview, pk=expedition_id)
    if post.likes.filter(pk=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
        messages.info(request, 'You have liked this review!')

    return HttpResponseRedirect(reverse('review_detail', args=[post_id]))
