# Generated by Django 5.0.4 on 2024-04-23 10:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("music", "0009_palo"),
    ]

    operations = [
        migrations.AddField(
            model_name="palo",
            name="song_detail",
            field=models.TextField(blank=True, null=True),
        ),
    ]
