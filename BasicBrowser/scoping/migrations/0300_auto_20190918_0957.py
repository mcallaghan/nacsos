# Generated by Django 2.2 on 2019-09-18 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoping', '0299_auto_20190909_1426'),
    ]

    operations = [
        migrations.AddField(
            model_name='ipccref',
            name='match_status',
            field=models.IntegerField(choices=[(0, 'Unchecked'), (1, 'In query'), (2, 'In WoS'), (3, 'Not in WoS')], default=0),
        ),
        migrations.AlterField(
            model_name='riskofbias',
            name='collection_biases',
            field=models.IntegerField(choices=[(0, 'Probably Yes'), (2, 'Probably No'), (1, 'Unclear')], help_text='Was the study free from motivation bias caused by the process of being observed (Hawthorne effect)?', null=True),
        ),
        migrations.AlterField(
            model_name='riskofbias',
            name='randomisation_differences',
            field=models.IntegerField(choices=[(0, 'Probably Yes'), (2, 'Probably No'), (1, 'Unclear')], help_text='Did the differences between the baseline characteristics of the control and treatment group suggest a reliable randomisation between treatment and control groups?', null=True),
        ),
    ]
