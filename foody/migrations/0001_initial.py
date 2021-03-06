# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-01 01:45
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Direction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(blank=True, default=b'Ball some meat', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='GroceryItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isPurchased', models.BooleanField(default=False)),
                ('name', models.CharField(blank=True, default=b'Meat', max_length=100)),
                ('measurement', models.CharField(blank=True, default=b'cup', max_length=100)),
                ('quantity', models.FloatField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=b'Meat', max_length=100)),
                ('measurement', models.CharField(blank=True, default=b'cup', max_length=100)),
                ('quantity', models.FloatField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
            options={
                'ordering': ('date',),
            },
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default=b'Meatballs', max_length=100)),
                ('menuItem', models.ForeignKey(db_column=b'menuItem', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='recipes', to='foody.MenuItem')),
            ],
            options={
                'ordering': ('title',),
            },
        ),
        migrations.AddField(
            model_name='ingredient',
            name='recipe',
            field=models.ForeignKey(db_column=b'recipe', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ingredients', to='foody.Recipe'),
        ),
        migrations.AddField(
            model_name='direction',
            name='recipe',
            field=models.ForeignKey(db_column=b'recipe', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='directions', to='foody.Recipe'),
        ),
    ]
