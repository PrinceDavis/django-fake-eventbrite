# Generated by Django 2.0 on 2019-11-09 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fake_eb', '0002_auto_20191109_0352'),
    ]

    operations = [
        migrations.AddField(
            model_name='fakeeventbriteevent',
            name='duration_specfier',
            field=models.TextField(default=''),
        ),
    ]
