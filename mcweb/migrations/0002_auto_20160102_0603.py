# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-02 06:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mcweb', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='merchant',
            name='display_name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]