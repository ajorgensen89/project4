from django.test import TestCase
from .models import Post
from django.contrib.auth.models import User

class TestPostList(TestCase):
    """
    Test PostList in forum/views.py.
    Model = class post().
    """
    