# Generated by Django 3.0.7 on 2020-07-09 10:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0026_auto_20200709_1700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentmv',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 9, 17, 26, 18, 171675)),
        ),
        migrations.AlterField(
            model_name='product',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 9, 17, 26, 18, 167685)),
        ),
        migrations.AlterField(
            model_name='propertylinkyoutobe',
            name='linkSource',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='propertytime',
            name='timeDetail',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 9, 17, 26, 18, 170678)),
        ),
    ]
