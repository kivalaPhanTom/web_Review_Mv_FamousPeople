# Generated by Django 3.0.5 on 2020-07-04 18:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0015_auto_20200705_0148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 5, 1, 53, 13, 272793)),
        ),
        migrations.AlterField(
            model_name='propertytime',
            name='timeDetail',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 5, 1, 53, 13, 278778)),
        ),
    ]