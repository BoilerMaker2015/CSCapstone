# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-05 01:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AuthenticationApp', '0012_student_platforms'),
    ]

    operations = [
        migrations.CreateModel(
            name='Platform',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('platform', models.CharField(max_length=1000)),
                ('user', models.ManyToManyField(to='AuthenticationApp.Student')),
            ],
        ),
    ]
