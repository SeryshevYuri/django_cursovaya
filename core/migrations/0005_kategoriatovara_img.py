# Generated by Django 3.1.7 on 2021-02-20 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_usluga_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='kategoriatovara',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Изображение'),
        ),
    ]
