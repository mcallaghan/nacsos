# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-19 13:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tmv_app', '0063_auto_20171212_1324'),
    ]

    operations = [
        migrations.AddField(
            model_name='timedtopic',
            name='year_share',
            field=models.FloatField(null=True),
        ),
    ]