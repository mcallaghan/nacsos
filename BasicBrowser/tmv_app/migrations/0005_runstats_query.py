# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-05-19 14:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scoping', '0099_auto_20170512_1404'),
        ('tmv_app', '0004_auto_20170516_0929'),
    ]

    operations = [
        migrations.AddField(
            model_name='runstats',
            name='query',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='scoping.Query'),
        ),
    ]