from django.contrib import admin
from .models import TravelReview
from django_summernote.admin import SummernoteModelAdmin

@admin.register(TravelReview)
class TravelReviewAdmin(SummernoteModelAdmin):

    summernote_fields = ('content')




