# Generated by Django 2.2.9 on 2020-03-04 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoping', '0317_project_no_relevance'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='no_further',
            field=models.BooleanField(default=False),
        ),
    ]
