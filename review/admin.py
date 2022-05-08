""" System Module """
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import TravelReview, TravelComments


@admin.register(TravelReview)
class TravelReviewAdmin(SummernoteModelAdmin):
    """ Creates admin panel for displaying travel reviews """
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('published', 'author')
    list_display = ('title', 'author', 'content', 'published', 'ratings')
    search_fields = ('title', 'author')
    summernote_fields = ('content')


@admin.register(TravelComments)
class TravelCommentsAdmin(admin.ModelAdmin):
    """ Creates admin panel for displaying travel comments """
    list_filter = ('created_on',)
    list_display = ('post', 'name', 'body', 'created_on',)
    search_fields = ('name', 'body')
