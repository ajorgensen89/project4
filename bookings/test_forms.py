from django.test import TestCase
from .forms import BookingForm

class TestBookingForm(TestCase):
    
    def test_item_name_is_required(self):
        form = BookingForm({'name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['name'][0], 'This field is required.') 

    def test_field_are_explicit_in_form_metaclass(self):
        form = BookingForm()
        self.assertEqual(form.Meta.fields, ['name', 'email'])     
