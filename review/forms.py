from django import forms
from .models import TravelReview, TravelComments 

class TravelReviewForm(forms.ModelForm):
    excerpt = forms.CharField(widget=forms.Textarea(attrs={
        'rows': '3',
    }))

    class Meta:

        model = TravelReview
        fields = ('title', 'travel_image', 'excerpt', 'content', 'ratings')
        widgets = {'ratings': forms.HiddenInput()}


class TravelCommentsForm(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea(attrs={
        'rows': '4',
    }))

    class Meta:
        model = TravelComments
        fields = ('body', )