# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-30 19:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Spot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(default='No Title', max_length=250)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('image', models.URLField(max_length=500)),
            ],
        ),
    ]
