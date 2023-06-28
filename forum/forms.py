from .models import Comment
from django import forms 


class CommentForm(forms.ModelForm):
    """
    Creates a form for comments to be entered into.
    Rendered into view of 'Discussion Board'.
    """
    class Meta:
        model = Comment
        fields = ('body',)
    