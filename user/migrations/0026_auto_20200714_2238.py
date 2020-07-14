# Generated by Django 3.0.3 on 2020-07-14 15:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0025_auto_20200714_2227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='img',
            field=models.ImageField(blank=True, default='media/profiles_pic/avatar.png', null=True, upload_to='profiles_pic'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='time_join',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 7, 14, 22, 38, 2, 549768), null=True),
        ),
    ]
