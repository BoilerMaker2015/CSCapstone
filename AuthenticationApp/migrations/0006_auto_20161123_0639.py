# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-23 11:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AuthenticationApp', '0005_auto_20161123_0633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='major',
            field=models.CharField(max_length=120, null=True),
        ),
    ]