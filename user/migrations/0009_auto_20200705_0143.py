# Generated by Django 3.0.5 on 2020-07-04 18:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_auto_20200705_0139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='time_join',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 5, 1, 43, 41, 639711)),
        ),
    ]
