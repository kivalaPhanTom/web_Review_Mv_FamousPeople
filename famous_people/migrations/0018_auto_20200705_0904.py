# Generated by Django 3.0.5 on 2020-07-05 02:04

import datetime
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('famous_people', '0017_auto_20200705_0221'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Like',
            new_name='Famous_Like',
        ),
        migrations.AlterField(
            model_name='famous',
            name='time1',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 5, 9, 4, 0, 366993)),
        ),
        migrations.AlterField(
            model_name='propertytime',
            name='timeDetail',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 5, 9, 4, 0, 366993)),
        ),
    ]