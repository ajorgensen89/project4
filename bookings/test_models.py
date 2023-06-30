from django.test import TestCase
from .models import Item, Reservation
from django.contrib.auth.models import User
from datetime import datetime


class TestBookingModel(TestCase):
    """
    Test for bookings / models.py.
    Test model = class Item().
    """


    def test_item_model(self):
        self.user = User.objects.create_user(
                username = 'john',
            )
        test = Item.objects.create(
            name = self.user,
            email = 'test@test.com',
            date = '2023-01-01',
            time = '5PM',
            people = '2',
            booked = True,
            # created_on=str('2023, 6, 26, 20, 50, 33, 204371, tzinfo=Z'),
            status = 1,
            approve = True,
        )

        # created_on_strp = datetime.strptime(test.created_on, '%Y, %m, %d, %H, %M, %S, %f, tzinfo=%Z')
        # assert created_on_strp == datetime.datetime('2023, 6, 26, 20, 50, 33, 204371, tzinfo=Z')


        self.assertEquals(test.name, self.user)
        self.assertEquals(test.email, 'test@test.com')
        self.assertEquals(test.date, '2023-01-01')
        self.assertEquals(test.time, '5PM')
        self.assertEquals(test.people, '2')
        self.assertEquals(test.booked, True)
        # self.assertEquals(created_on_strp, '2023, 6, 26, 20, 50, 33, 204371, tzinfo=<UTC>'),
        self.assertEquals(test.status, 1)
        self.assertEquals(test.approve, True)

    # def test_field_in_model_metaclass(self):
    #     item = Item()
    #     self.assertEqual(item.Meta.ordering, ('-created_on'))

class TestBookingModelReservation(TestCase):
    """
    Test for bookings/models.py.
    Test model = class Reservation().
    """
    def test_reservation_model(self):
        self.user = User.objects.create_user(
                username = 'john',
            )
        self.test = Item.objects.create(
            name = self.user,
            email = 'test@test.com',
            date = '2023-01-01',
            time = '5PM',
            people = '2',
            booked = True,
            # created_on = str('2023, 6, 26, 20, 50, 33, 204371, tzinfo=Z'),
            status = 1,
            approve = True,
        )
        reservations = Reservation.objects.create(
            reservation = self.test,
            # made_on = '2023-01-01',
            approve = True,
        )

        self.assertEquals(reservations.reservation, self.test)
        # self.assertEquals(reservations.made_on, '2023-01-01')
        self.assertEquals(reservations.approve, True)

    # def test_field_in_model_metaclass(self):
    #     res = Reservation()
    #     self.assertEqual(res.Meta.ordering, ('made_on'))      

class TestWelcomeModel(TestCase):

    def test_welcome_model(self):
        welcome = WelcomeModel.objects.create(
            message = 'Welcome page rendered'
        )

        self.assertEqual(welcome.message, 'Welcome page rendered')
