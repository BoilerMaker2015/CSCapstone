# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-04 21:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GroupsApp', '0004_auto_20161204_1656'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='group_platforms',
            field=models.CharField(blank=True, default=None, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='group',
            name='group_skills',
            field=models.CharField(blank=True, default=None, max_length=500, null=True),
        ),
    ]
