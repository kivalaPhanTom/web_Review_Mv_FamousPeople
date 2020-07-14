# Generated by Django 3.0.7 on 2020-06-15 02:49

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Famous',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('famous_title', models.CharField(default='', max_length=255)),
                ('time1', models.DateTimeField(default=datetime.datetime(2020, 6, 15, 9, 49, 35, 584970))),
                ('famous_img', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='PropertyTitle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TitleName_detail', models.CharField(default='', max_length=255)),
                ('name_title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='famous_people.Famous')),
            ],
        ),
        migrations.CreateModel(
            name='PropertyTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timeDetail', models.DateTimeField(default=datetime.datetime(2020, 6, 15, 9, 49, 35, 632843))),
                ('time1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='famous_people.Famous')),
            ],
        ),
        migrations.CreateModel(
            name='PropertyImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_img_detail', models.ImageField(upload_to='images/')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='famous_people.Famous')),
            ],
        ),
        migrations.CreateModel(
            name='PropertyContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_detail', models.TextField(blank=True, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='famous_people.Famous')),
            ],
        ),
    ]