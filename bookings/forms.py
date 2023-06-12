from django import forms
from .model import Item, Comment


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'email', 'date', 'time', 'people', 'tableSize', 'booked', 'cancel']

        