# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-01 16:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0002_auto_20171011_2023'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('text', models.TextField(null=True)),
                ('views', models.PositiveIntegerField(default=0)),
                ('liked', models.PositiveIntegerField(default=0)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.User')),
            ],
            options={
                'db_table': 'article_data',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.User')),
            ],
            options={
                'db_table': 'comment_data',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='comments',
            field=models.ManyToManyField(to='article.Comment'),
        ),
        migrations.AlterUniqueTogether(
            name='comment',
            unique_together=set([('author', 'content')]),
        ),
        migrations.AlterUniqueTogether(
            name='article',
            unique_together=set([('author', 'time')]),
        ),
    ]
