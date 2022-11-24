# Generated by Django 4.1.3 on 2022-11-19 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("crm", "0004_statuscrm_commentcrm_order_status"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="statuscrm",
            options={"verbose_name": "Status", "verbose_name_plural": "Statuses"},
        ),
        migrations.AlterField(
            model_name="order",
            name="order_message",
            field=models.TextField(
                default="New", max_length=1000, null=True, verbose_name="message"
            ),
        ),
        migrations.AlterField(
            model_name="statuscrm",
            name="Status_name",
            field=models.CharField(max_length=200, verbose_name="Status name"),
        ),
    ]