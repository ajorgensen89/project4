from django.shortcuts import render
from django.views import generic

# import model from forumPost to use in class.
from .models import forumPost


# class being used for view.
class forumList(generic.ListView):
    model = forumPost
    # Build it. For content.
    queryset = forumPost.objects.filter(status=1).order_by('-create_on')
    template_name = 'forum.html'
    paginate_by = 4
