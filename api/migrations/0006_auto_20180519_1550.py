# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-19 15:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20180519_1549'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='price',
            name='id',
        ),
        migrations.AlterField(
            model_name='price',
            name='booking',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='api.Booking'),
        ),
    ]
