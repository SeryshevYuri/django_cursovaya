# Generated by Django 3.1.7 on 2021-02-20 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_tovar_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='usluga',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Изображение'),
        ),
    ]
