from django.contrib import admin
from core.models import Habit, DailyRecord
# Register your models here.

@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = ('name', 'goal', 'user', 'amount')

@admin.register(DailyRecord)
class DailyRecordAdmin(admin.ModelAdmin):
    list_display = ('date', 'amount', 'habit')