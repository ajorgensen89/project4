from django.test import TestCase
from .forms import CommentForm


class TestCommentForm(TestCase):
    """
    Test CommentForm model. Check field inputs are the same.
    """
    def test_field_are_in_form_metaclass(self):
        form = CommentForm()
        self.assertEqual(form.Meta.fields, ('body',))