# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-05 01:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AuthenticationApp', '0015_auto_20161204_2017'),
    ]

    operations = [
        migrations.RenameField(
            model_name='skill',
            old_name='skill',
            new_name='student',
        ),
    ]