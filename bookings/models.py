from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import random 
from django import forms
from django.contrib.auth.models import User

# To create a random . Needed??
#    randomNum = random.randint(1, 10)
# Create your models here.
# table class

created_on = False
STATUSS = ((0, "Draft"), (1, "Published"))

class Item(models.Model):
    """
    Class created to make a form for the user to submit details 
    to make a booking.
    """
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField()
    date = models.DateField()
    time = models.TimeField()
    people = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(10)])
    tableSize = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    booked = models.BooleanField(null=False, blank=False, default=False)
    cancel = models.BooleanField(null=False, blank=False, default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUSS, default=0)
    approve = models.BooleanField(default=False)

# To rename the default option from django.
    def __str__(self):
        return str(self.name)

# To create an order.
    class Meta:
        ordering = ['-created_on']
    
    
class Reservation(models.Model):
    """
    class to ensure the booking request has be be approved before it is confirmed to the user
    """
    reservation = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="appointment")
    made_on = models.DateTimeField(auto_now_add=True)
    approve = models.BooleanField(default=False)

    class Meta:
        ordering = ['made_on']

    def __str__(self):
        return f"Reservation: {self.name}"  


# class ResetApprove(models.Model):

#     approve = models.BooleanField(default=False)
#     edit_approve = approve

#     def __str__(self):
#         return f"Reset: {self.name}"


    
