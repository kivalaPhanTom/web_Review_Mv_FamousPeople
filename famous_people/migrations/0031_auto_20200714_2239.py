# Generated by Django 3.0.3 on 2020-07-14 15:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('famous_people', '0030_auto_20200714_2238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentfamous',
            name='dateFamous',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 14, 22, 39, 46, 239706)),
        ),
        migrations.AlterField(
            model_name='famous',
            name='time1',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 14, 22, 39, 46, 234688)),
        ),
        migrations.AlterField(
            model_name='propertytime',
            name='timeDetail',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 14, 22, 39, 46, 239706)),
        ),
    ]
