from django.views.generic import TemplateView


class HomeView(TemplateView):
    """ Class-based function to render home page """
    template_name = 'home.html'