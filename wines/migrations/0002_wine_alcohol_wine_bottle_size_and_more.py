# Generated by Django 5.0.7 on 2024-11-15 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("wines", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="wine",
            name="Alcohol",
            field=models.CharField(default="Unknown", max_length=50),
        ),
        migrations.AddField(
            model_name="wine",
            name="Bottle_size",
            field=models.CharField(default="750ml", max_length=50),
        ),
        migrations.AddField(
            model_name="wine",
            name="serving_temperature",
            field=models.CharField(default="unknown", max_length=50),
        ),
    ]
