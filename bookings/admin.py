from django.contrib import admin
from .models import Item

# Register your models here.
@admin.register(Item)
class simple(admin.ModelAdmin):
    list_filter = ('status', 'created_on', 'approved')

    actions = ['approved_bookings']

    def approved_bookings(self, request, queryset):
        queryset.update(approved=True)

admin.site.register(DateCheck)





# admin.site.register(Item)


# admin.site.register(Comment)
