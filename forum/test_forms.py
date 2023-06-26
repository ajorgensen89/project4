from django.test import TestCase
from .forms import CommentForm


class TestCommentForm(TestCase):
    """
    Test CommentForm in forum/forms.py.
    Model = class Comment().
    Check metadata fields are being stored.
    """
    def test_field_are_in_form_metaclass(self):
        form = CommentForm()
        self.assertEqual(form.Meta.fields, ('body',))