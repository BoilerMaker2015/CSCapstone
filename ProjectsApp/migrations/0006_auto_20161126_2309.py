# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-27 04:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectsApp', '0005_auto_20161126_2208'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='bookmark',
            new_name='members',
        ),
    ]
