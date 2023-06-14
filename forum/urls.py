from . import views
from django.urls import path

# Class based views. To render class as a view.
urlpatterns = [
    path('forum/', views.forumList.as_view(), name="forumhome"),
]