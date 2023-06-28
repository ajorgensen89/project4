from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django import forms
from django.contrib.auth.models import User

# To create a random . Needed??
#    randomNum = random.randint(1, 10)
# Create your models here.
# table class

created_on = False
STATUSS = ((0, "Draft"), (1, "Published"))
TIME_SLOTS = [
    ('5PM', '5PM'),
    ('6PM', '6PM'),
    ('7PM', '7PM'),
    ('8PM', '8PM'),
    ('9PM', '9PM'),
    ('10PM', '10PM'),
    ('11PM', '11PM'),
]
TABLES = [
    ('A', 'A'),
    ('B', 'B'),
    ('C', 'C'),
]

class Item(models.Model):
    """
    Class created to make a form for the user to submit details 
    to make a booking.
    """
    name = models.ForeignKey(User, on_delete = models.CASCADE)
    email = models.EmailField()
    date = models.DateField()
    time = models.CharField(
    max_length = 8, choices = TIME_SLOTS, default = '5PM')
    people = models.PositiveIntegerField(default = 1, validators = [
    MinValueValidator(1), MaxValueValidator(10)])
    booked = models.BooleanField(
    'HAPPY TO SEND FOR APPROVAL? TICK BOX.', 
    null = False, blank = False, default = False)
    created_on = models.DateTimeField(auto_now_add = True)
    status = models.IntegerField(choices = STATUSS, default = 0)
    approve = models.BooleanField(default = False)

# To rename the default option from django.


    def __str__(self):
        
        return str(self.name)
        #self.name.username

# To create an order.
    class Meta:
        ordering = ['-created_on']  
 
 
class Reservation(models.Model):
    """
    class to ensure the booking request has be be 
    approved before it is confirmed to the user
    """
    reservation = models.ForeignKey(
    Item, on_delete = models.CASCADE, related_name = "appointment")
    made_on = models.DateTimeField(auto_now_add = True)
    approve = models.BooleanField(default = False)

    class Meta:
        ordering = ['made_on']


    def __str__(self):
        return f"Reservation: {self.reservation}"


class WelcomeModel(models.Model):
    """
    """
    message = 'message to the welcome page'

    def __str__(self):
        return f" Welcome {self.message}"