# Generated by Django 3.0.3 on 2020-06-16 13:44

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(blank=True, upload_to='profiles_pic')),
                ('sex', models.CharField(blank=True, choices=[('Nam', 'Nam'), ('Nữ', 'Nữ'), ('Không xác định', 'Không xác định')], max_length=20)),
                ('birthday', models.DateField()),
                ('time_join', models.DateTimeField(default=datetime.datetime(2020, 6, 16, 20, 44, 17, 81569))),
                ('ctv', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]