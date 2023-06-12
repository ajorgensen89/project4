from django.contrib import admin
from .models import forumPost, forumComment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(forumPost)
class forumPostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'create_on')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'create_on')
    summernote_field = ('content')


# Register your models here.

# admin.site.register(forumPost)
# admin.site.register(forumComment)

@admin.register(forumComment)
class forumCommentAdmin(admin.ModelAdmin):
    
    list_display = ('name', 'body', 'post', 'create_on', 'approved')
    list_filter = ('approved', 'create_on')
    search_fields = ('name', 'email', 'body')

    #action to approve comments. (more than one if needed)
    actions = ['approve_comments']

    # boolean result. set to true.
    def approve_comments(self, request, queryset):
        queryset.update(approved=True)