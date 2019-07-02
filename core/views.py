from django.shortcuts import render, get_object_or_404
from core.models import Habit, DailyRecord
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.

def indexview(request):
    habits = Habit.objects.all()
    dailyrecords = DailyRecord.objects.all()
    return render(request, 'index.html', {"habits": habits, "dailyrecords": dailyrecords})

def HabitDetailView(request, pk):
    habits = get_object_or_404(Habit, pk=pk)
    dailyrecords = DailyRecord.objects.all()
    return render(request, 'habit_detail.html', {"habits": habits, "dailyrecords": dailyrecords})
