from . import views
from django.urls import path


urlpatterns = [
    # Url to home page showing forum post.
    path('forum/', views.PostList.as_view(), name = 'post_list'),
    # Expanding on the posts details.
    path('<slug:slug>/', views.PostDetail.as_view(), name = 'post_detail'),
    # Manipulate likes.
    path('like/<slug:slug>', views.PostLike.as_view(), name = 'post_like'),
    # To delete comments.
    path('delete/<comment_id>/', views.delete_comment, name='delete_comment'),
]