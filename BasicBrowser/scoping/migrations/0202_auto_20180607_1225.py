# Generated by Django 2.0.5 on 2018-06-07 12:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scoping', '0201_remove_docstatement_tag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='docstatement',
            name='doc',
        ),
        migrations.AddField(
            model_name='docstatement',
            name='par',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='scoping.DocPar'),
        ),
    ]