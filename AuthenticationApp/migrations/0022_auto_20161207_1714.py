# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-07 22:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AuthenticationApp', '0021_auto_20161206_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='engineer',
            name='company',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='CompaniesApp.Company'),
        ),
    ]