# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-07 10:12
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoping', '0163_auto_20171025_0933'),
    ]

    operations = [
        migrations.AddField(
            model_name='wosarticle',
            name='cr_scopus',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), null=True, size=None, verbose_name='Cited References'),
        ),
    ]
