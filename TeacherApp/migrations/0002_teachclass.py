# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-02 04:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TeacherApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeachClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=120, null=True)),
            ],
        ),
    ]
