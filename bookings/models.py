from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import random 
from django.db.models.fields import DateTimeField

# To create a random . Needed??
#    randomNum = random.randint(1, 10)
# Create your models here.
# table class

created_on = False
STATUSS = ((0, "Draft"), (1, "Published"))

class Item(models.Model):
    """ Class created to make a form for the user to submit details 
        to make a booking. Checking for all the information within the class.
    """
    name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField()
    date = models.DateField()
    time = models.TimeField()
    people = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(10)])
    tableSize = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    booked = models.BooleanField(null=False, blank=False, default=False)
    cancel = models.BooleanField(null=False, blank=False, default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUSS, default=0)
    approved = models.BooleanField(default=False)

# To rename the default option from django.
    def __str__(self):
        return self.name

# To create an order.
    class Meta:
        ordering = ['-created_on']
