# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-28 03:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('foody', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='direction',
            name='recipe',
            field=models.ForeignKey(db_column=b'recipe', on_delete=django.db.models.deletion.CASCADE, to='foody.Recipe'),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='recipe',
            field=models.ForeignKey(db_column=b'recipe', on_delete=django.db.models.deletion.CASCADE, to='foody.Recipe'),
        ),
    ]
