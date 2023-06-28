from django.test import TestCase
from .models import Post
from django.contrib.auth.models import User

class TestPostList(TestCase):
    """
    Test PostList in forum/views.py.
    Model = class Post().
    """
    def test_post_list(self):
        self.post = Post.objects.create(
            title = 'Fruity cocktail',
            slug = 'Fruity-cocktail',
            author = self.user,
            # updated_on = datetime.now(),
            content = 'Some cocktails come with a shot',
            featured_image = 'image',
            excerpt = 'Excerptionally fruity cocktails made here.',
            # created_on = str('2023, 6, 26, 20, 50, 33, 204371, tzinfo=Z'),
            status = 1,
            # likes = True,
        )
        lists = PostList.objects.create(
            model = self.post,
            # queryset = Post.objects.filter(status = 1).order_by('-created_on'),
            template_name = 'index.html',
            paginate_by = 1,

        )

        self.assertEqual(lists.model, self.post)
        # self.assertEqual(lists.model, )
        self.assertEqual(lists.template_name, 'index.html')
        self.assertEqual(lists.paginate_by, 1)


# class TestPostDetail(TestCase):
#     """
#     Test PostDetail in forum/views.py.
#     Model = class Post().
#     """
#     def test_get(self):


    