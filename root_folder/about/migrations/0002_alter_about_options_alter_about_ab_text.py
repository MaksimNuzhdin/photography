# Generated by Django 4.1.3 on 2022-11-19 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("about", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="about",
            options={"verbose_name": "About page", "verbose_name_plural": "About page"},
        ),
        migrations.AlterField(
            model_name="about",
            name="ab_text",
            field=models.TextField(verbose_name="text"),
        ),
    ]