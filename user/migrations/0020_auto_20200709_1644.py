# Generated by Django 3.0.7 on 2020-07-09 09:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0019_auto_20200705_1859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='time_join',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 7, 9, 16, 44, 0, 193288), null=True),
        ),
    ]