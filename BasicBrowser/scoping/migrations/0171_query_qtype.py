# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-29 13:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoping', '0170_emailtokens_sent_other_tech'),
    ]

    operations = [
        migrations.AddField(
            model_name='query',
            name='qtype',
            field=models.CharField(choices=[('DE', 'Default'), ('SB', 'Snowballing Backward'), ('SF', 'Snowballing Forward'), ('MN', 'Manual Add')], default='DE', max_length=2),
        ),
    ]
