# Generated by Django 3.0.3 on 2020-07-14 15:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('famous_people', '0029_auto_20200714_2227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentfamous',
            name='dateFamous',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 14, 22, 38, 2, 539013)),
        ),
        migrations.AlterField(
            model_name='famous',
            name='time1',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 14, 22, 38, 2, 535013)),
        ),
        migrations.AlterField(
            model_name='propertytime',
            name='timeDetail',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 14, 22, 38, 2, 538012)),
        ),
    ]
