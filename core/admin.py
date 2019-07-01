from django.contrib import admin
from core.models import Habit, Record
# Register your models here.

@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = ('name', 'goal', 'user')

@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = ('date', 'number', 'user')