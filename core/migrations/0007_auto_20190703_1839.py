# Generated by Django 2.2.3 on 2019-07-03 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20190703_1814'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='dailyrecord',
            constraint=models.UniqueConstraint(fields=('habit', 'date'), name='user'),
        ),
    ]
