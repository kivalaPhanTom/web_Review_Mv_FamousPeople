# Generated by Django 3.0.5 on 2020-07-05 02:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('famous_people', '0020_auto_20200705_0914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='famous',
            name='time1',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 5, 9, 14, 40, 260780)),
        ),
        migrations.AlterField(
            model_name='propertytime',
            name='timeDetail',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 5, 9, 14, 40, 264770)),
        ),
    ]