# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-04 21:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GroupsApp', '0003_auto_20161204_1655'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='group_platforms',
        ),
        migrations.RemoveField(
            model_name='group',
            name='group_skills',
        ),
    ]