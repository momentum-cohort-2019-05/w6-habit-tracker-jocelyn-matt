# Generated by Django 2.2.3 on 2019-07-01 20:58

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DailyRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, default=datetime.date.today, null=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
        migrations.RemoveField(
            model_name='habit',
            name='record',
        ),
        migrations.AddField(
            model_name='habit',
            name='amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
        migrations.DeleteModel(
            name='Record',
        ),
        migrations.AddField(
            model_name='dailyrecord',
            name='habit',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.Habit'),
        ),
    ]
