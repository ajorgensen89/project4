from forum import views
from django.urls import path

# Class based views. To render class as a view.
urlpatterns = [
    path('', views.forumList.as_view(), name="forum.html"),
    # path('', views.check, name="check")
]