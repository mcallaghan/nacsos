# Generated by Django 2.2 on 2019-09-30 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoping', '0301_query_estimated_docs'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='rating_first',
            field=models.BooleanField(default=False),
        ),
    ]
