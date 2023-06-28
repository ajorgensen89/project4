from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Post, Comment
from .forms import CommentForm
from django.contrib import messages


class PostList(generic.ListView):
    """
    Create a view for Model - Post. Show if status = 1 (published).
    """
    model = Post
    queryset = Post.objects.filter(status = 1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 1

class PostDetail(View):
    """
    Get and Post details from comment model. 
    Checking approval status.
    Renders post, comments, likes on form.
    """


    def get(self, request, slug, *args, **kwargs):
        # Get posts with status = 1 for published.
        queryset = Post.objects.filter(status = 1)
        # Get object slug or error 404.
        post = get_object_or_404(queryset, slug = slug)
        # Get comment related to that post.
        comments = post.comments.filter(
        approved = True).order_by("-created_on")
        # Set defaut until user interaction
        liked = False
        # Change 'like' of each forum post if boolean value to True if exists.
        if post.likes.filter(id = self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm(),
            },
        )


    def post(self, request, slug, *args, **kwargs):
        # Get post with status = 1 for published.
        queryset = Post.objects.filter(status = 1)
        # Get object slug or error 404.
        post = get_object_or_404(queryset, slug = slug)
        # Get comment related to that post.
        comments = post.comments.filter(
        approved = True).order_by("-created_on")
        # Set default until user interaction.
        liked = False
        # Change 'like' of each forum post if boolean value to True if exists.
        if post.likes.filter(id = self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data = request.POST)  

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit = False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()
        # Render on requested page.    
        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": CommentForm(),
            },
        )


def delete_comment(request, comment_id):
    
    comment = get_object_or_404(Comment, id = comment_id)

    comment.delete()

    messages.error(request, "Comment deleted.")

    # Render on requested page.    

    # Redirect back to the previous page. The same 'Discussion and Leave Comment page'.
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    

class PostLike(View):
    """
    Post likes from users. Remove likes from users.
    Also for Administraion users when logged in.
    """


    def post(self, request, slug):
        # Get class Post or 404 error.
        post = get_object_or_404(Post, slug = slug)
        
        # Filter post by id and if it exists, either, remove or add the like. 
        # Display by red heart if added and grey heart outline if not.
        if post.likes.filter(id = request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        # Reverse response after action above.
        return HttpResponseRedirect(reverse('post_detail', args = [slug]))


    

