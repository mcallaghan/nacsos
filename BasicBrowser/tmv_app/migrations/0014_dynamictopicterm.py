# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-06-06 16:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tmv_app', '0013_topic_primary_dtopic'),
    ]

    operations = [
        migrations.CreateModel(
            name='DynamicTopicTerm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.FloatField()),
                ('run_id', models.IntegerField(db_index=True)),
                ('term', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tmv_app.Term')),
                ('topic', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tmv_app.DynamicTopic')),
            ],
        ),
    ]
