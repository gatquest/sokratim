# Generated by Django 3.2.3 on 2021-05-29 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('either', '0004_alter_favorite_short_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favorite',
            name='link_name',
            field=models.CharField(max_length=300, verbose_name='Введите ссылку'),
        ),
        migrations.AlterField(
            model_name='favorite',
            name='short_name',
            field=models.CharField(max_length=50, verbose_name='Введите название для ссылки'),
        ),
    ]
