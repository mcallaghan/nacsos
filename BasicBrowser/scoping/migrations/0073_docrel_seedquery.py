# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-04-07 08:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scoping', '0072_auto_20170406_1713'),
    ]

    operations = [
        migrations.AddField(
            model_name='docrel',
            name='seedquery',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='scoping.Query'),
        ),
    ]
