# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-01-21 18:39
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toilet', '0002_auto_20170112_1435'),
    ]

    operations = [
        migrations.AddField(
            model_name='toiletlecture',
            name='total_time',
            field=models.DurationField(default=datetime.timedelta(0)),
        ),
    ]
