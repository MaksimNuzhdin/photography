# Generated by Django 4.1.3 on 2022-11-19 18:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("kategories", "0002_kategories_category_dis"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="kategories",
            options={"verbose_name": "Categories", "verbose_name_plural": "Categories"},
        ),
    ]
