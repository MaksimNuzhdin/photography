# Generated by Django 4.1.3 on 2022-11-14 18:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("photoexp", "0003_remove_photoexp_category_photoexp_category_ph"),
    ]

    operations = [
        migrations.DeleteModel(
            name="PhotoExp",
        ),
    ]