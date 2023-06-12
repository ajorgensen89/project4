from django.test import TestCase


# To get access to Django Testing.

class TestDjango(TestCase):
    def test_working(self):
        self.assertEqual(1, 0)