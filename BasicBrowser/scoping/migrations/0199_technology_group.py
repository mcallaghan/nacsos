# Generated by Django 2.0.5 on 2018-06-07 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoping', '0198_auto_20180529_1410'),
    ]

    operations = [
        migrations.AddField(
            model_name='technology',
            name='group',
            field=models.TextField(null=True, verbose_name='Broad Category Name'),
        ),
    ]
