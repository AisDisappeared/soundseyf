# Generated by Django 5.0.4 on 2024-04-05 19:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("music", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Composers",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(blank=True, max_length=255, null=True)),
                ("biography", models.TextField(blank=True, null=True)),
                (
                    "image",
                    models.ImageField(default="default.jpg", upload_to="Composers/"),
                ),
            ],
        ),
        migrations.AddField(
            model_name="masterpieces",
            name="composer",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="music.composers",
            ),
        ),
    ]
