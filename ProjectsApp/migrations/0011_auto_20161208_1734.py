# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-08 17:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectsApp', '0010_auto_20161208_0335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='creator',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='AuthenticationApp.Engineer'),
        ),
    ]