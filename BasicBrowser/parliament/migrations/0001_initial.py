# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-01-18 15:45
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cities', '0010_adjust_unique_attributes'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        migrations.swappable_dependency(settings.CITIES_COUNTRY_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Constituency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('has_coal', models.BooleanField()),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.CITIES_COUNTRY_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(null=True)),
                ('parl_period', models.IntegerField(null=True)),
                ('doc_type', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Interjection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Paragraph',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Parl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(choices=[('N', 'National'), ('R', 'Regional')], max_length=1)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.CITIES_COUNTRY_MODEL)),
                ('region', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cities.Region')),
            ],
        ),
        migrations.CreateModel(
            name='ParlSession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('n', models.IntegerField()),
                ('years', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), size=None)),
                ('total_seats', models.IntegerField()),
                ('parliament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parliament.Parl')),
            ],
        ),
        migrations.CreateModel(
            name='Party',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.TextField()),
                ('first_name', models.TextField()),
                ('dob', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('years', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), size=None)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('parlsession', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parliament.ParlSession')),
                ('party', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parliament.Party')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parliament.Person')),
            ],
        ),
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('text', models.TextField()),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Query Creator')),
            ],
        ),
        migrations.CreateModel(
            name='SeatResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_votes_cast', models.FloatField()),
                ('votes_received', models.FloatField()),
                ('incumbent', models.BooleanField()),
                ('majority', models.FloatField()),
                ('constituency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parliament.Constituency')),
                ('parlsession', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parliament.ParlSession')),
                ('party', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parliament.Party')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parliament.Person')),
            ],
        ),
        migrations.CreateModel(
            name='SeatSum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seats', models.IntegerField()),
                ('government', models.BooleanField()),
                ('majority', models.BooleanField()),
                ('parlsession', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parliament.ParlSession')),
                ('party', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parliament.Party')),
            ],
        ),
        migrations.CreateModel(
            name='Utterance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parliament.Document')),
                ('speaker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parliament.Person')),
            ],
        ),
        migrations.AddField(
            model_name='paragraph',
            name='utterance',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parliament.Utterance'),
        ),
        migrations.AddField(
            model_name='interjection',
            name='paragraph',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parliament.Paragraph'),
        ),
        migrations.AddField(
            model_name='interjection',
            name='parties',
            field=models.ManyToManyField(to='parliament.Party'),
        ),
        migrations.AddField(
            model_name='interjection',
            name='persons',
            field=models.ManyToManyField(to='parliament.Person'),
        ),
        migrations.AddField(
            model_name='document',
            name='parlsession',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parliament.ParlSession'),
        ),
        migrations.AddField(
            model_name='document',
            name='search_matches',
            field=models.ManyToManyField(to='parliament.Search'),
        ),
        migrations.AddField(
            model_name='constituency',
            name='parliament',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parliament.Parl'),
        ),
        migrations.AddField(
            model_name='constituency',
            name='region',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cities.Region'),
        ),
    ]
