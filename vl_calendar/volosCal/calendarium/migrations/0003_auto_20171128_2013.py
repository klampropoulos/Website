# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-28 18:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calendarium', '0002_event_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='location',
            field=models.CharField(default='Volos', max_length=256, verbose_name='location'),
        ),
    ]
