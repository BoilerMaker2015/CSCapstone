# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-05 07:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectsApp', '0008_auto_20161204_2314'),
        ('GroupsApp', '0007_auto_20161204_2235'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='project',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='ProjectsApp.Project'),
        ),
    ]
