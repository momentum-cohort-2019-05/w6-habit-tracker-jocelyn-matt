# Generated by Django 2.2.3 on 2019-07-03 16:06

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0003_auto_20190702_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='habit',
            unique_together={('name', 'user')},
        ),
    ]
