from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date, time

# Create your models here.

class Habit(models.Model):
    goal = models.TextField(max_length=300)
    name = models.CharField(max_length=200)
    user = models.ForeignKey(to=User, on_delete= models.CASCADE)
    amount = models.DecimalField(max_digits=6, decimal_places=2, default=0)

    def __str__(self):
        return self.name

class Meta:
        unique_together = ['name', 'record']

class DailyRecord(models.Model):
    date = models.DateField(null = True, blank = True, default=date.today)
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    habit = models.ForeignKey(to=Habit, on_delete= models.SET_NULL, null = True)

    def __str__(self):
        return self.amount


