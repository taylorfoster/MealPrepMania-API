# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-02 04:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foody', '0004_auto_20161202_0443'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='menuItemasd',
            new_name='menuItem',
        ),
    ]