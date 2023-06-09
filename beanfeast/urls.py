"""beanfeast URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from forum import views
from bookings import views



urlpatterns = [
    # To use Admin.
    path('admin/', admin.site.urls),
    # To view bookings.
    path('view/', views.get_bookings_sheet, name = 'get_bookings_sheet'),
    # To create a booking.
    path('book/', views.create_a_booking, name = 'create_a_booking'),
    # item id links from forms / templates as a parameter.
    path('edit/<booking_id>', views.edit_booking ,name = 'edit_booking'),
    # Cancel Bookings.
    path('cancel/<booking_id>', views.cancel_booking ,name = 'cancel_booking'),
    # Use for layout in Django Admin.
    path('summernote/', include('django_summernote.urls')),
    # Path to forum.urls.
    path('', include('forum.urls'), name = 'forum_urls'),
    # To use sign in/register/logout.
    path('accounts/', include('allauth.urls')),
    # Welcome (home) page.
    path('', views.welcome, name = 'welcome'),
    
]
