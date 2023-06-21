from django import forms
from .models import Item


class BookingForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'email', 'date', 'time', 'people', 'tableSize', 'booked', 'cancel']

    # class Meta:
    #     model = DateCheck
    #     fields = ['date']    

