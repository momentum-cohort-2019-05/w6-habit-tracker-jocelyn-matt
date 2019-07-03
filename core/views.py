from django.shortcuts import render, get_object_or_404, redirect
from core.models import Habit, DailyRecord
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from datetime import date
from .forms import RecordForm, HabitForm

# Create your views here.
@login_required
def indexview(request):
    habits = Habit.objects.all()
    dailyrecords = DailyRecord.objects.all()
    return render(request, 'index.html', {"habits": habits, "dailyrecords": dailyrecords})

@login_required
def HabitDetailView(request, pk):
    habits = get_object_or_404(Habit, pk=pk)
    record_date = request.POST.get('date', date.today())
    record = DailyRecord(habit = habits, date = record_date)
    if request.method == 'POST':
        form = RecordForm(data=request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect(to='index')

    else:
        form = RecordForm()
        
    return render(request, 'habit_detail.html', {"habits": habits, "record": record, "form": form})

@login_required
def CreateHabitView(request):
    habits = Habit.objects.all()

    if request.method == 'POST':
        habitform = HabitForm(data=request.POST)
        if habitform.is_valid():
            habitform.save()
            return redirect(to='index')

    else:
        habitform = HabitForm()

    return render(request, 'create_habit.html', {"habits": habits, "habitform": habitform})