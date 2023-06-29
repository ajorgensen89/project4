# from django.test import TestCase
# from .models import Post
# from django.contrib.auth.models import User
# from .views import PostList, PostDetail
# from django.http import HttpRequest

# class TestPostDetail(TestCase):
#     """
#     Test PostList in forum/views.py.
#     Model = class Post().
#     """
#     def test_post_detail(self):
#         post = PostDetail(
#             data = {
#                 "title": "Fruity cocktail",
#                 "slug": "fruity-cocktail",
#                 "author": "john",
#                 'updated_on': '2023-01-01',
#                 'content': 'Some cocktails come with a shot',
#                 'featured_image': 'image',
#                 'excerpt': 'Excerptionally fruity cocktails made here.',
#                 'created_on':'2023-01-01',
#                 'status': '1',
#                 'likes': 'True',
#             }
#         )
#         self.assertEqual("title", post.data)
#         self.assertEqual("slug", post.data)
#         self.assertEqual("author", post.data)
#         self.assertIn('updated_on', post.fields)
#         self.assertIn('content', post.fields)
#         self.assertIn('featured_image', post.fields)
#         self.assertIn('excerpt', post.fields)
#         self.assertIn('created_on', post.fields)
#         self.assertIn('status', post.fields)
#         self.assertIn('likes', post.fields)

#         request = HttpRequest()

#         request.POST = {
#             "title": "Fruity cocktail",
#             "slug": "fruity-cocktail",
#             "author": "john",
#             'updated_on': '2023-01-01',
#             'content': 'Some cocktails come with a shot',
#             'featured_image': 'image',
#             'excerpt': 'Excerptionally fruity cocktails made here.',
#             'created_on':'2023-01-01',
#             'status': '1',
#             'likes': 'True',
#         }

#         test_post = PostDetail(request.POST)
#         self.assertTrue(test_post.is_valid())




    # def test_post_list(self):
    #     response = self.client.get(reverse('home'))
    #     self.assertTemplateUsed(response, 'index.html')
    #     self.assertEqual(response.status_code, 200) 
    #     self.assertEqual(len(response.context['post_list']), 6)
    #     self.assertContains(response, 'Fruity cocktail')
        


# class TestPostDetail(TestCase):
#     """
#     Test PostDetail in forum/views.py.
#     Model = class Post().
#     """
#     def test_get(self):


    