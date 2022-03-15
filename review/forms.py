from django import forms
from .models import TravelReview

class TravelReviewForm(forms.ModelForm):

    class Meta:

        model = TravelReview
        fields = ('title', 'travel_image', 'excerpt', 'content', 'ratings')