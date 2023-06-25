from django.test import TestCase
from .models import Item

# Create your tests here.
class TestViews(TestCase):
    # (self) is TestDjango
    def test_get_bookings_sheet(self):
        response = self.client.get('/view')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bookings/bookings_sheet.html')

    def test_create_a_booking(self):
        response = self.client.get('/book')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bookings/book_table.html')

    def test_edit_booking(self):
        item = Item.objects.create(name='Edit')
        response = self.client.get(f'/edit/{item.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bookings/edit_bookings.html')

    def test_can_book_item(self):
        response = self.client.post('/book', {'name': 'Add Item'})
        self.assertRedirects(response, '/')

    def test_can_cancel_booking(self):
        item = Item.objects.create(name='cancel')
        response = self.client.get(f'/cancel/{item.id}')
        self.assertRedirects(response, '/')
        existing_items = Item.objects.filter(id=item.id)
        self.assertEqual(len(existing_items), 0)