from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date, time

# Create your models here.

class Habit(models.Model):
    goal = models.TextField(max_length=300)
    name = models.CharField(max_length=200, null=True)
    user = models.ForeignKey(to=User, on_delete= models.CASCADE)
    amount = models.DecimalField(max_digits=6, decimal_places=2, default=0)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('habit-detail', args=[str(self.id)])

    class Meta:
        unique_together = ['name', 'user']

class DailyRecord(models.Model):
    date = models.DateField(null = True, blank = True, default=date.today)
    amount = models.IntegerField()
    habit = models.ForeignKey(to=Habit, on_delete= models.SET_NULL, null = True)

    # def __str__(self):
    #     return self.amount


#hey this is a test to see if the changes will save