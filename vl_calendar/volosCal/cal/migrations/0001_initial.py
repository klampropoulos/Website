# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-02 20:33
from __future__ import unicode_literals

import colorfield.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EventCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Name')),
                ('color', colorfield.fields.ColorField(default='#FF0000', max_length=18, verbose_name='Color')),
            ],
        ),
    ]
