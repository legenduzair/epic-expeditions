from django.shortcuts import render

# Create your views here.


def page_not_found_view(request, exception):

    return render(request, 'errors/404.html', {})


def my_custom_error_view(request, exception=None):

    return render(request, 'errors/500.html', {})


def my_custom_permission_denied_view(request, exception=None):

    return render(request, 'errors/403.html', {})


def my_custom_bad_request_view(request, exception=None):

    return render(request, 'errors/400.html', {})