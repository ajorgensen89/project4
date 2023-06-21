from django.contrib import admin
from .models import Item

# Register your models here.
@admin.register(Item)
class simple(admin.ModelAdmin):
    list_filter = ('status', 'created_on', 'approve')

    actions = ['approve_bookings']

    def approve_bookings(self, request, queryset):
        queryset.update(approve=True)

    #def edit_approve_booking(self, request, queryset):
        #queryset.update(approve=False)    



# admin.site.register(DateCheck)
