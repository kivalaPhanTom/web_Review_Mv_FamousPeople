# Generated by Django 3.0.7 on 2020-07-09 10:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('famous_people', '0024_auto_20200709_1644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentfamous',
            name='dateFamous',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 9, 17, 0, 0, 807228)),
        ),
        migrations.AlterField(
            model_name='famous',
            name='time1',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 9, 17, 0, 0, 804236)),
        ),
        migrations.AlterField(
            model_name='propertytime',
            name='timeDetail',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 9, 17, 0, 0, 807228)),
        ),
    ]
