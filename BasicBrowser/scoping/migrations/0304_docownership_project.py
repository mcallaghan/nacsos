# Generated by Django 2.2 on 2019-10-07 09:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scoping', '0303_auto_20191007_0947'),
    ]

    operations = [
        migrations.AddField(
            model_name='docownership',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='scoping.Project'),
        ),
    ]
