# Generated by Django 2.2 on 2019-04-26 13:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scoping', '0272_docproject_full_relevant'),
    ]

    operations = [
        migrations.AddField(
            model_name='studyeffect',
            name='docmetacoding',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='scoping.DocMetaCoding'),
        ),
    ]
