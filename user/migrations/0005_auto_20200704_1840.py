# Generated by Django 3.0.3 on 2020-07-04 11:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20200704_1643'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='birthday',
        ),
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(blank=True, choices=[('Nam', 'Nam'), ('Nữ', 'Nữ'), ('Giới tính thứ ba', 'Giới tính thứ ba')], max_length=20),
        ),
        migrations.AlterField(
            model_name='profile',
            name='time_join',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 4, 18, 40, 49, 921021)),
        ),
    ]
