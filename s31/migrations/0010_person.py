# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-25 04:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('s31', '0009_auto_20171219_0825'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='full name')),
            ],
        ),
    ]
