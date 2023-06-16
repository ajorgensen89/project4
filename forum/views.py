from django.shortcuts import render
# from django.views import generic
from django.views.generic import ListView

# Import model from forumPost to use in class.
from .models import forumPost
from django.shortcuts import render


# Class being used for view with model name forumPost.
class forumList(ListView):
    model = forumPost
    # Build in. For content.
    queryset = forumPost.objects.filter(status=1).order_by('-create_on')
    template_name = 'forum/forum.html'
    paginate_by = 4



def check(request):
    this = forumPost.objects.all()
    contents = {
        'this': this
    }    
    return render(request, 'forum/forum.html', contents)


