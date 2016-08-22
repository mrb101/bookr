# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-19 13:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_auto_20160819_1351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='slug',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]