""" System Module """
from django import forms
from .models import TravelReview, TravelComments


class TravelReviewForm(forms.ModelForm):
    """ Class-based function to add expedition review form """
    excerpt = forms.CharField(widget=forms.Textarea(attrs={
        'rows': '3',
    }))

    class Meta:
        """ Defines meta characteristics of expedition review form """
        model = TravelReview
        fields = ('title', 'travel_image', 'excerpt', 'content', 'ratings')
        widgets = {'ratings': forms.HiddenInput()}


class TravelCommentsForm(forms.ModelForm):
    """ Class-based function to add expedition comments form """
    body = forms.CharField(widget=forms.Textarea(attrs={
        'rows': '4',
    }))

    class Meta:
        """ Defines meta characteristics of expedition comments form """
        model = TravelComments
        fields = ('body', )
