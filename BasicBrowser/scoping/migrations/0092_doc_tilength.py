# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-05-05 08:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoping', '0091_auto_20170502_0959'),
    ]

    operations = [
        migrations.AddField(
            model_name='doc',
            name='tilength',
            field=models.IntegerField(null=True),
        ),
    ]
