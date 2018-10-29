# Generated by Django 2.0.5 on 2018-09-04 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parliament', '0035_auto_20180731_1450'),
    ]

    operations = [
        migrations.AddField(
            model_name='search',
            name='utterance_count',
            field=models.IntegerField(default=0, verbose_name='Number of utterance objects'),
        ),
        migrations.AddField(
            model_name='utterance',
            name='search_matches',
            field=models.ManyToManyField(to='parliament.Search'),
        ),
        migrations.AlterField(
            model_name='search',
            name='par_count',
            field=models.IntegerField(default=0, verbose_name='Number of paragraph objects'),
        ),
    ]
