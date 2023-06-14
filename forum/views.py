from django.shortcuts import render
# from django.views import generic
from django.views.generic import ListView

# import model from forumPost to use in class.
from .models import forumPost


# class being used for view.
class forumList(ListView):
    model = forumPost
    # Build it. For content.
    queryset = forumPost.objects.filter(status=1).order_by('-create_on')
    template_name = 'index.html'
    paginate_by = 4


