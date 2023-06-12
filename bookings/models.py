from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import random 
from django.db.models.fields import DateTimeField


randomNum = random.randint(1, 10)
# Create your models here.
# table class

created_on = False
class Item(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField()
    date = models.DateField()
    time = models.TimeField()
    people = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(10)])
    tableSize = models.PositiveIntegerField(default=randomNum, validators=[MinValueValidator(1), MaxValueValidator(10)])
    booked = models.BooleanField(null=False, blank=False, default=False)
    cancel = models.BooleanField(null=False, blank=False, default=False)
    created_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_on']    


class Comment(models.Model):
    comment = models.CharField(max_length=200)



