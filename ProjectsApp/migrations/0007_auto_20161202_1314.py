# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-02 18:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectsApp', '0006_auto_20161126_2309'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='members',
            new_name='bookmarkMembers',
        ),
    ]
