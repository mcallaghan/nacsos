# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-03-31 08:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoping', '0067_snowballingsession_technology'),
    ]

    operations = [
        migrations.AddField(
            model_name='snowballingsession',
            name='database',
            field=models.CharField(max_length=6, null=True, verbose_name='Query database'),
        ),
    ]