from django import forms
from .models import Item


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'email', 'date', 'time', 'people', 'tableSize', 'booked', 'cancel']

