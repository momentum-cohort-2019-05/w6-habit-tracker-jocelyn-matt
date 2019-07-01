from django.shortcuts import render
from core.models import Habit, Record
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.

def indexview(request):
    habits = Habit.objects.all()
    records = Record.objects.all()
    return render(request, 'index.html', {"habits": habits, "records": records})
