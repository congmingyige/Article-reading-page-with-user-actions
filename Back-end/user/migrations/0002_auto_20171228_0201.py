# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-27 18:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='introduction',
        ),
        migrations.RemoveField(
            model_name='user',
            name='resident',
        ),
        migrations.RemoveField(
            model_name='user',
            name='sex',
        ),
    ]
