from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin
from bookings.models import WelcomeModel


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """
    Display Forum Post model in Administraion.
    """
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on')
    summernote_fields = ('content')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Display Forum Comments from users in administraion. 
    To be approved before viewed on the website.
    """
    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')

    #action to approved comments.
    actions = ['approved_comments']


    # boolean result. set to true.


    def approved_comments(self, request, queryset):
        queryset.update(approved = True)
