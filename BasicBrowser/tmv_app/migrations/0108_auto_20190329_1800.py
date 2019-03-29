# Generated by Django 2.1.2 on 2019-03-29 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tmv_app', '0107_runstats_rng_seed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='runstats',
            name='rng_seed',
            field=models.IntegerField(help_text='seed for random number generator for stochastic estimation of topic model (blei dtm)', null=True),
        ),
    ]
