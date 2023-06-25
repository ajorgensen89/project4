from django.test import TestCase
from .models import Item

# Create your tests here.
class TestViews(TestCase):
    # (self) is TestDjango
    def test_get_bookings_sheet(self):
        response = self.client.get('/view')
        self.assertEqual(response.status_code, 301)

    def test_create_a_booking(self):
        response = self.client.get('/book')
        self.assertEqual(response.status_code, 301)

    # def test_get_edit_item_page(self):
    #     item = Item.objects.create()
    #     response = self.client.get(f'/edit/{item.id}')
    #     self.assertEqual(response.status_code, 301)    