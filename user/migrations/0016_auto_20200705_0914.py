# Generated by Django 3.0.5 on 2020-07-05 02:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0015_auto_20200705_0910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='time_join',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 5, 9, 14, 21, 376288)),
        ),
    ]
