# Generated by Django 3.1.5 on 2021-05-21 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vilon', '0002_auto_20210514_1451'),
    ]

    operations = [
        migrations.AddField(
            model_name='curtain',
            name='name',
            field=models.CharField(default='Vilon', max_length=10),
        ),
        migrations.AddField(
            model_name='curtain',
            name='type',
            field=models.CharField(choices=[('FRESHMAN', 'Freshman'), ('SOPHOMORE', 'Sophomore')], default='FRESHMAN', max_length=30),
        ),
        migrations.AlterField(
            model_name='curtain',
            name='img',
            field=models.ImageField(upload_to='static/images'),
        ),
    ]
