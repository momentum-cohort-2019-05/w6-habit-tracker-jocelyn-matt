from django import forms
from datetime import date, time

class RecordForm(forms.Form):
    amount = forms.IntegerField()
    date = forms.DateField(initial=date.today)
