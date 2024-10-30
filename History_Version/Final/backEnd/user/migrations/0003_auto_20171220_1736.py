# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-20 09:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20171011_2023'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='introduction',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='resident',
            field=models.CharField(max_length=16, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='sex',
            field=models.CharField(default='Man', max_length=5),
        ),
    ]