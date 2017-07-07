# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-07-06 13:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scoping', '0106_citation'),
    ]

    operations = [
        migrations.CreateModel(
            name='CDO',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('citation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scoping.Citation')),
                ('doc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scoping.Doc')),
            ],
        ),
    ]
