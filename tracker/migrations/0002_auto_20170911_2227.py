# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-11 20:27
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carmodel',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2017, 9, 11, 22, 27, 54, 909251)),
        ),
        migrations.AlterField(
            model_name='carmodel',
            name='link',
            field=models.URLField(max_length=2000),
        ),
    ]
