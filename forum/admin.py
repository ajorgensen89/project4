from django.contrib import admin
from .models import forumPost, forumComment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(forumPost)
class forumPostAdmin(SummernoteModelAdmin):

    summernote_field = ('content')


# Register your models here.

# admin.site.register(forumPost)
admin.site.register(forumComment)