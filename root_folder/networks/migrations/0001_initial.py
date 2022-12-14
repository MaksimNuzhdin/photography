# Generated by Django 4.1.3 on 2022-11-19 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Networks",
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
                (
                    "nw_name",
                    models.CharField(max_length=200, verbose_name="Social network"),
                ),
                (
                    "nw_img",
                    models.ImageField(upload_to="", verbose_name="Social network link"),
                ),
                ("nw_link", models.CharField(max_length=500, verbose_name="Link")),
            ],
            options={
                "verbose_name": "Social network",
                "verbose_name_plural": "Social network",
            },
        ),
    ]
