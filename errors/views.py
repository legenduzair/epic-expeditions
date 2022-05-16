""" System Module """
from django.shortcuts import render

# Create your views here.


def page_not_found_view(request, exception):
    """ Function to render 404 error page """
    return render(request, 'errors/404.html', {})


def my_custom_error_view(request, exception=None):
    """ Function to render 500 error page """
    return render(request, 'errors/500.html', {})


def my_custom_permission_denied_view(request, exception=None):
    """ Function to render 403 error page """
    return render(request, 'errors/403.html', {})


def my_custom_bad_request_view(request, exception=None):
    """ Function to render 400 error page """
    return render(request, 'errors/400.html', {})
