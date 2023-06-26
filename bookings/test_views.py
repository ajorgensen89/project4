from django.test import TestCase
from .models import Item
from django.contrib.auth.models import User


class TestUser(TestCase):
    # (self) is TestDjango
    # Use self.user for User based testing.
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@test.com',
            password='testpassword'
        )

    def test_setUp(self):
        # Example for logged in user.
        self.client.login(username='testuser', password='testpassword')

        # Check attributes from the user instance.
        self.assertEqual(self.user.username, 'testuser')
        self.assertEqual(self.user.email, 'test@test.com')

        # Delete after test.
        self.user.delete()    

    def test_get_bookings_sheet(self):
        response = self.client.get('/view')
        self.assertEqual(response.status_code, 301)

    def test_create_a_booking(self):
        response = self.client.get('/book')
        self.assertEqual(response.status_code, 301)

    def test_can_cancel_item(self):
        self.user = User.objects.create_user(
            username='john',
        )
        item = Item.objects.create(name=self.user, email='john@test.com', date='2023-01-01', time='5PM', people='2', booked='True')
        response = self.client.get(f'/cancel/{item.id}')
        self.assertRedirects(response, '/view/')
        existing_items = Item.objects.filter(id=item.id)
        self.assertEqual(len(existing_items), 0)

    def test_can_edit_item(self):
        self.user = User.objects.create_user(
            username='john',
        )
        item = Item.objects.create(name=self.user, email='john@test.com', date='2023-01-01', time='5PM', people='2', booked='True')
        response = self.client.post(f'/edit/{item.id}', {'id': '1', 'name': 1, 'email': 'john@test.com', 'date': '2023-01-01', 'time': '6PM', 'people': '2', 'booked': 'True',})
        self.assertRedirects(response, '/view/')
        updated_item = Item.objects.get(id=item.id)
        self.assertEqual(updated_item.time, '6PM')      
