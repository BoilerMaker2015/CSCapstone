# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-08 03:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CommentsApp', '0005_subcomment_creator'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subcomment',
            name='creator',
        ),
    ]
