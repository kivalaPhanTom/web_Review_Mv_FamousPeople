# Generated by Django 3.0.3 on 2020-06-16 13:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('famous_people', '0004_auto_20200616_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='famous',
            name='time1',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 16, 20, 44, 16, 987808)),
        ),
        migrations.AlterField(
            model_name='propertytime',
            name='timeDetail',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 16, 20, 44, 17, 65947)),
        ),
    ]
