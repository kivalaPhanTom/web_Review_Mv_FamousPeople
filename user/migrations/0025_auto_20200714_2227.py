# Generated by Django 3.0.3 on 2020-07-14 15:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0024_auto_20200709_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='profiles_pic'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='time_join',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 7, 14, 22, 27, 46, 528866), null=True),
        ),
    ]
