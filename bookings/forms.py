from django import forms
from .models import Item, Reservation


class BookingForm(forms.ModelForm):
    """
    Create booking form from Item model
    """
    class Meta:
        model = Item
        fields = ['name', 'email', 'date', 'time', 'people', 'tableSize', 'booked']


class ReservationForm(forms.ModelForm):
    """
    Create Form 
    """
    class Meta:
        model = Reservation
        fields = ('reservation',)
