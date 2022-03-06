from django.contrib import admin
from .models import TravelReview
from django_summernote.admin import SummernoteModelAdmin

@admin.register(TravelReview)
class TravelReviewAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('published', 'author')
    list_display = ('title', 'author', 'content', 'published', 'ratings')
    search_fields = ('title', 'author')
    summernote_fields = ('content')




