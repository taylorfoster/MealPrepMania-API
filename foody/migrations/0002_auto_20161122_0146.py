# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-22 01:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foody', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='insructions',
        ),
        migrations.AddField(
            model_name='recipe',
            name='instructions',
            field=models.CharField(blank=True, default=b'Ball some meat', max_length=100),
        ),
    ]