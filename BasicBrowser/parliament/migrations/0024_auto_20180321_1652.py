# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-03-21 16:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('parliament', '0023_auto_20180321_1650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partylist',
            name='region',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cities.Region'),
        ),
    ]
