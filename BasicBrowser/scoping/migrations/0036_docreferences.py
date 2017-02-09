# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-02-07 13:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scoping', '0035_merge_20170207_1009'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocReferences',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('refdoi', models.CharField(max_length=150, null=True, verbose_name='DOI')),
                ('doc', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='scoping.Doc')),
            ],
        ),
    ]