# Generated by Django 2.2 on 2019-06-14 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoping', '0290_remove_intervention_medium2'),
    ]

    operations = [
        migrations.AddField(
            model_name='docmetacoding',
            name='excluded',
            field=models.BooleanField(default=False),
        ),
    ]
