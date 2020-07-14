# Generated by Django 3.0.7 on 2020-07-05 11:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0017_auto_20200705_0914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(blank=True, choices=[('Nam', 'Nam'), ('Nữ', 'Nữ'), ('Giới tính thứ ba', 'Giới tính thứ ba')], default='Nam', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='img',
            field=models.ImageField(blank=True, default='static/user/default_pro.jpg', null=True, upload_to='profiles_pic'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='time_join',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 7, 5, 18, 38, 7, 210722), null=True),
        ),
    ]
