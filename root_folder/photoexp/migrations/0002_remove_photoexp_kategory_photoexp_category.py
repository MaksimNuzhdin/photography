# Generated by Django 4.1.3 on 2022-11-14 15:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kategories', '0001_initial'),
        ('photoexp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photoexp',
            name='kategory',
        ),
        migrations.AddField(
            model_name='photoexp',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='kategories.kategories', verbose_name='Category'),
        ),
    ]
