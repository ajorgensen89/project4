from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.test import TestCase
from .models import Post, Comment


class TestPostModel(TestCase):
    """
    Test forum/models.py.
    Test model = class Post().
    """


    def test_post_model(self):
        self.user = User.objects.create_user(
                username = 'john',
            )
        post = Post.objects.create(
            title = 'Fruity cocktail',
            slug = 'Fruity-cocktail',
            author = self.user,
            # updated_on = 
            content = 'Some cocktails come with a shot',
            featured_image = 'image',
            excerpt = 'Excerptionally fruity cocktails made here.',
            # created_on = str('2023, 6, 26, 20, 50, 33, 204371, tzinfo=Z'),
            status = 1,
            # likes = True,
        )
        
        self.assertEquals(post.title, 'Fruity cocktail')
        self.assertEquals(post.slug, 'Fruity-cocktail')
        self.assertEquals(post.author, self.user)
         # self.assertEquals(post.updated_on, )
        self.assertEquals(post.content, 'Some cocktails come with a shot',)
        self.assertEquals(post.featured_image, 'image')
        self.assertEquals(post.excerpt, 'Excerptionally fruity cocktails made here.')
         # self.assertEquals(post.created_on, )
        self.assertEquals(post.status, 1)
        # self.assertEquals(post.likes, True)

         # def test_field_in_model_metaclass(self):
         #     item = Post()
         #     self.assertEqual(item.Meta.ordering, ('-created_on'))

    
class TestCommentModel(TestCase):
    """
    Test forum/models.py.
    Model tested = class Comment().
    """


    def test_comment_model(self):
        self.user = User.objects.create_user(
                username = 'john',
            )
        self.post = Post.objects.create(
            title = 'Fruity cocktail',
            slug = 'Fruity-cocktail',
            author = self.user,
            # updated_on = 
            content = 'Some cocktails come with a shot',
            featured_image = 'image',
            excerpt ='Excerptionally fruity cocktails made here.',
            # created_on=str('2023, 6, 26, 20, 50, 33, 204371, tzinfo=Z'),
            status = 1,
            # likes = True,
        )
        comments = Comment.objects.create(
            post = self.post,
            # made_on='2023-01-01',
            name = 'john',
            body = 'Wine has body and legs.',
            approved = False,
        )

        self.assertEquals(comments.post, self.post)
        # self.assertEquals(reservations.created, '2023-01-01')
        self.assertEquals(comments.name, 'john')
        self.assertEquals(comments.body, 'Wine has body and legs.')
        self.assertEquals(comments.approved, False)

        # def test_field_in_model_metaclass(self):
        #     item = Comment()
        #     self.assertEqual(item.Meta.ordering, ('created_on'))
