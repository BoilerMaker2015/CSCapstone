# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-08 03:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AuthenticationApp', '0022_auto_20161208_0141'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='engineer',
            name='company',
        ),
        migrations.AddField(
            model_name='engineer',
            name='company',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
