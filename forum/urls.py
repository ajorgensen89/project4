from . import views
from django.urls import path

# Class based views. To render class as a view.
#urlpatterns = [
    #path('', views.forumList.as_view(), name="forum.html"),
    # path('', views.check, name="check")
#]


urlpatterns = [
    path('forum/', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
]