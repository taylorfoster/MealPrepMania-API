# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-04 20:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foody', '0006_auto_20161204_1954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='direction',
            name='text',
            field=models.CharField(blank=True, default=b'Ball some meat', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='measurement',
            field=models.CharField(blank=True, default=b'cup', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='name',
            field=models.CharField(blank=True, default=b'Meat', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='title',
            field=models.CharField(blank=True, default=b'Recipe Title', max_length=100, null=True),
        ),
    ]
