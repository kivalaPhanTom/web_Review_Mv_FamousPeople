# Generated by Django 3.0.7 on 2020-06-15 02:46

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name_MV', models.CharField(default='', max_length=255)),
                ('content_intro', models.TextField(blank=True, null=True)),
                ('time', models.DateTimeField(default=datetime.datetime(2020, 6, 15, 9, 46, 51, 78617))),
                ('product_img_intro', models.ImageField(upload_to='images/')),
                ('Check_Attribute_top', models.CharField(choices=[('NOTTOP', 'Not Top'), ('TOP', 'TOP')], default='NOTTOP', max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='PropertyTitle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TitleName_detail', models.CharField(default='', max_length=255)),
                ('name_title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Product')),
            ],
        ),
        migrations.CreateModel(
            name='PropertyTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timeDetail', models.DateTimeField(default=datetime.datetime(2020, 6, 15, 9, 46, 51, 127520))),
                ('time', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Product')),
            ],
        ),
        migrations.CreateModel(
            name='PropertySinger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SingerName_detail', models.CharField(default='', max_length=255)),
                ('name_singer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Product')),
            ],
        ),
        migrations.CreateModel(
            name='PropertyImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_img_detail', models.ImageField(upload_to='images/')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Product')),
            ],
        ),
        migrations.CreateModel(
            name='PropertyContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_detail', models.TextField(blank=True, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Product')),
            ],
        ),
    ]
