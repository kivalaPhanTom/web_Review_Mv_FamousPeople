# Generated by Django 3.0.5 on 2020-07-04 18:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0012_auto_20200705_0009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 5, 1, 39, 57, 113318)),
        ),
        migrations.AlterField(
            model_name='propertytime',
            name='timeDetail',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 5, 1, 39, 57, 117308)),
        ),
    ]
