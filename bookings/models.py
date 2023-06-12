from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import random 


randomNum = random.randint(1, 10)
# Create your models here.
# table class
class Item(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField()
    booked = models.BooleanField(null=False, blank=False, default=False)
    date = models.DateField()
    time = models.TimeField()
    cancel = models.BooleanField(null=False, blank=False, default=False)
    people = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(10)])
    tableSize = models.PositiveIntegerField(default=randomNum, validators=[MinValueValidator(1), MaxValueValidator(10)])

class Comment(models.Model):
    comment = models.CharField(max_length=200)



