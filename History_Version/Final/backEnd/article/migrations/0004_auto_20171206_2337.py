# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-06 15:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_merge_20171206_2334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='liked',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='article',
            name='views',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
