# Generated by Django 2.0.5 on 2018-05-23 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoping', '0189_auto_20180518_1005'),
    ]

    operations = [
        migrations.AddField(
            model_name='docpar',
            name='tag',
            field=models.ManyToManyField(to='scoping.Tag'),
        ),
    ]
