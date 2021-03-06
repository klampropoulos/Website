# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-28 18:15
from __future__ import unicode_literals

from django.db import migrations, models
import location_field.models.plain


class Migration(migrations.Migration):

    dependencies = [
        ('calendarium', '0003_auto_20171128_2013'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='locat',
            field=models.CharField(default='', max_length=256, verbose_name='location'),
        ),
        migrations.AlterField(
            model_name='event',
            name='location',
            field=location_field.models.plain.PlainLocationField(max_length=63),
        ),
    ]
