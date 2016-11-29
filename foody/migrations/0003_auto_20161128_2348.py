# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-28 23:48
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('foody', '0002_auto_20161128_0322'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroceryItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isPurchased', models.BooleanField(default=False)),
                ('name', models.CharField(blank=True, default=b'Meat', max_length=100)),
                ('measurement', models.CharField(blank=True, default=b'cup', max_length=100)),
                ('quantity', models.CharField(blank=True, default=b'1', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('recipe', models.ForeignKey(db_column=b'recipe', on_delete=django.db.models.deletion.CASCADE, to='foody.Recipe')),
            ],
        ),
        migrations.RemoveField(
            model_name='grocerylist',
            name='ingredient',
        ),
        migrations.AlterField(
            model_name='direction',
            name='recipe',
            field=models.ForeignKey(db_column=b'recipe', on_delete=django.db.models.deletion.CASCADE, related_name='directions', to='foody.Recipe'),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='recipe',
            field=models.ForeignKey(db_column=b'recipe', on_delete=django.db.models.deletion.CASCADE, related_name='ingredients', to='foody.Recipe'),
        ),
        migrations.DeleteModel(
            name='GroceryList',
        ),
    ]