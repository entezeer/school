# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-13 05:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('s31', '0005_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shedule',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='\u043d\u043e\u043c\u0435\u0440')),
                ('day', models.CharField(max_length=50, verbose_name='day')),
                ('num', models.CharField(max_length=1, verbose_name='num')),
                ('subject', models.CharField(max_length=50, verbose_name='subject')),
                ('form', models.CharField(max_length=1, verbose_name='\u043a\u043b\u0430\u0441\u0441')),
                ('formw', models.CharField(max_length=1, verbose_name='word')),
            ],
        ),
    ]