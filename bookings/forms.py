from django import forms
from .models import Item, Reservation


class BookingForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'email', 'date', 'time', 'people', 'tableSize', 'booked', 'cancel']

    # class Meta:
    #     model = DateCheck
    #     fields = ['date']


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ('reservation',)


# class ResetForm(forms.ModelForm):
#     class Meta:
#         model = ResetApprove
#         fields = ('approve',)


