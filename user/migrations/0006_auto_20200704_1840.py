# Generated by Django 3.0.3 on 2020-07-04 11:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20200704_1840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='time_join',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 4, 18, 40, 54, 662495)),
        ),
    ]
