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
from django.urls import path
from bookings.views import get_bookings_sheet, create_a_booking, edit_booking

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', get_bookings_sheet, name='get_bookings_sheet'),
    path('book', create_a_booking, name='create_a_booking'),
    # item id links from forms/templates as a parameter
    path('edit/<item_id>', edit_booking ,name='edit_booking')
]
