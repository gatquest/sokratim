# Generated by Django 3.2.3 on 2021-05-29 13:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('either', '0007_favorite_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favorite',
            name='date',
        ),
    ]
