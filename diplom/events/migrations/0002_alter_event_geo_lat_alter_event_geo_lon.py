# Generated by Django 4.2.1 on 2023-06-07 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='geo_lat',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='geo_lon',
            field=models.FloatField(blank=True),
        ),
    ]
