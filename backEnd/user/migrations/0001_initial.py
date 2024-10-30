# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-27 17:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=11, null=True, unique=True)),
                ('email', models.EmailField(max_length=64, null=True, unique=True)),
                ('password', models.CharField(max_length=64)),
                ('sex', models.CharField(default='Man', max_length=5)),
                ('introduction', models.CharField(max_length=128, null=True)),
                ('resident', models.CharField(max_length=16, null=True)),
            ],
            options={
                'db_table': 'user_data',
            },
        ),
        migrations.AlterUniqueTogether(
            name='user',
            unique_together=set([('phone', 'email')]),
        ),
    ]
