# Generated by Django 4.1.3 on 2022-11-18 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="TeleSettings",
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
                ("tg_token", models.CharField(max_length=200, verbose_name="Token")),
                ("tg_chat", models.CharField(max_length=200, verbose_name="Chat")),
                ("tg_text", models.TextField(verbose_name="Text")),
            ],
            options={
                "verbose_name": "Settings",
                "verbose_name_plural": "Settings",
            },
        ),
    ]
