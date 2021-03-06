# Generated by Django 2.0.5 on 2018-09-13 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='favorites_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='status',
            name='retweets_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='status',
            name='source',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='status',
            name='text',
            field=models.TextField(null=True),
        ),
    ]
