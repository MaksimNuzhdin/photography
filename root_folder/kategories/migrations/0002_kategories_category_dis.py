# Generated by Django 4.1.3 on 2022-11-19 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("kategories", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="kategories",
            name="category_dis",
            field=models.TextField(default="-", null=True, verbose_name="Discription"),
        ),
    ]