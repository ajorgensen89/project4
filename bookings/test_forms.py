from django.test import TestCase
from .forms import BookingForm, ReservationForm


class TestBookingForm(TestCase):
    """
    Test BookingForm in bookings/forms.py.
    Model = class Item().
    Check all form objects in list. 
    Give objects 'Field Required' Status.
    Check metadata fields are being stored.
    """
    # (self) is TestDjango
    
    def test_item_name_is_required(self):
        form = BookingForm({'name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    def test_item_email_is_required(self):
        form = BookingForm({'email': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors.keys())
        self.assertEqual(form.errors['email'][0], 'This field is required.')

    def test_item_date_is_required(self):
        form = BookingForm({'date': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('date', form.errors.keys())
        self.assertEqual(form.errors['date'][0], 'This field is required.')

    def test_item_time_is_required(self):
        form = BookingForm({'time': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('time', form.errors.keys())
        self.assertEqual(form.errors['time'][0], 'This field is required.')

    def test_item_people_is_required(self):
        form = BookingForm({'people': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('people', form.errors.keys())
        self.assertEqual(form.errors['people'][0], 'This field is required.')

    def test_field_in_form_metaclass(self):
        form = BookingForm()
        self.assertEqual(form.Meta.fields, ['name', 'email', 'date', 'time', 'people', 'booked'])  


class TestReservationForm(TestCase):
    """
    Test ReservationForm in bookings/forms.py.
    Model = class Reservation().
    Check metadata fields are being stored.
    """
    def test_field_in_form_metaclass(self):
        form = ReservationForm()
        self.assertEqual(form.Meta.fields, ('reservation',))          
