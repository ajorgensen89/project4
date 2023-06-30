from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


STATUS = ((0, "Draft"), (1, "Published"))


class Post(models.Model):
    """
    Create model for different input to create a 'Forum Post'. 
    Used for Events or News posts.
    Image can be rendered with each new post. 
    It can be created and not posted straight way.
    """
    title = models.CharField(max_length = 200, unique = True)
    slug = models.SlugField(max_length = 200, blank=True,  null=True, unique=True)
    author = models.ForeignKey(
    User, on_delete = models.CASCADE, related_name = 'forum_posts')
    updated_on = models.DateTimeField(auto_now = True)
    content = models.TextField()
    featured_image = CloudinaryField('image', default = 'placeholder')
    excerpt = models.TextField(blank = True)
    created_on = models.DateTimeField(auto_now_add = True)
    status = models.IntegerField(choices = STATUS, default = 0)
    likes = models.ManyToManyField(
    User, related_name = 'forum_likes', blank = True)


    class Meta:
        ordering = ['-created_on']


    def __str__(self):
        return self.title


    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):
    """
    Model created to show comments on the above 'Forum Posts'. 
    Users or administraion can have a discussion and post comments.
    To be approved if coming from a 'user'.
    Newest comments will be listed at the top.
    """
    post = models.ForeignKey(
    Post, on_delete = models.CASCADE, related_name = 'comments')
    name = models.CharField(max_length = 80)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add = True)
    approved = models.BooleanField(default = False)


    class Meta:
        ordering = ['created_on']


    def __str__(self):
        return f"Comment {self.body} by {self.name}"    
