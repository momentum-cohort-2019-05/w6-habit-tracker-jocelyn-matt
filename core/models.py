from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date, time

# Create your models here.
class Record(models.Model):
    date = models.DateField(null = True, blank = True, default=date.today)
    number = models.DecimalField(max_digits=6, decimal_places=2)
    user = models.ForeignKey(to=User, on_delete= models.CASCADE)
    # habit = models.ForeignKey(to=Habit, on_delete= models.SET_NULL, null = True)


    def __str__(self):
        return self.number

class Habit(models.Model):
    goal = models.TextField(max_length=300)
    name = models.CharField(max_length=200)
    user = models.ForeignKey(to=User, on_delete= models.CASCADE)
    record = models.ForeignKey(to=Record, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

class Meta:
        unique_together = ['user', 'record']

