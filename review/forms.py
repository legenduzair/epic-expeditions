from django import forms
from .models import TravelReview, TravelComments 

class TravelReviewForm(forms.ModelForm):

    class Meta:

        model = TravelReview
        fields = ('title', 'travel_image', 'excerpt', 'content', 'ratings')


class TravelCommentsForm(forms.ModelForm):

    class Meta:
        model = TravelComments
        fields = ('post', 'body',)