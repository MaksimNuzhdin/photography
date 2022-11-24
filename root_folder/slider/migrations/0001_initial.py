# Generated by Django 4.1.3 on 2022-11-10 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slider_img', models.ImageField(max_length=200, upload_to='sliderimg/', verbose_name='img')),
                ('slider_title', models.CharField(max_length=200, verbose_name='Название')),
                ('ыдшвук_css', models.CharField(default='-', max_length=200, null=True, verbose_name='CSS class')),
            ],
            options={
                'verbose_name': 'Название',
                'verbose_name_plural': 'Название',
            },
        ),
    ]