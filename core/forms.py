from django import forms
from datetime import date, time
from core.models import DailyRecord, Habit

class RecordForm(forms.ModelForm):
    
    class Meta:
        model = DailyRecord
        fields = ['amount', 'date' ]

class HabitForm(forms.ModelForm):

    class Meta:
        model = Habit
        fields = ['name', 'goal', 'amount']