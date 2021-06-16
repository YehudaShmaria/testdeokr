# Generated by Django 3.1.5 on 2021-05-21 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vilon', '0004_auto_20210521_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curtain',
            name='type',
            field=models.CharField(choices=[('tefira', 'תפירה'), ('zebra', 'זברה')], default='tefira', max_length=30),
        ),
    ]
