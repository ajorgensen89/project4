from django.contrib import admin
from .models import Item, Comment
# from .admin import bookingModel
# Register your models here.

admin.site.register(Item)
#list_filter = ('status', 'create_on')

admin.site.register(Comment)
# @admin.register(Item)
#class bookingModelClass(bookingModel):

    # list_display = ('title', 'slug', 'status', 'create_on')
    # search_fields = ['title', 'content']
    #list_filter = ('status', 'create_on')


# Register your models here.


#@admin.register(Comment)
#class forumCommentAdmin(admin.ModelAdmin):
    
    #list_display = ('name', 'body', 'post', 'create_on', 'approved')
    #list_filter = ('approved', 'create_on')
    #search_fields = ('name', 'email', 'body')

    #action to approve comments. (more than one if needed)
    #actions = ['approve_comments']

    # boolean result. set to true.
    #def approve_comments(self, request, queryset):
        #queryset.update(approved=True)