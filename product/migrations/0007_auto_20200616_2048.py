# Generated by Django 3.0.3 on 2020-06-16 13:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_auto_20200616_2044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 16, 20, 48, 13, 797888)),
        ),
        migrations.AlterField(
            model_name='propertytime',
            name='timeDetail',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 16, 20, 48, 13, 797888)),
        ),
    ]
