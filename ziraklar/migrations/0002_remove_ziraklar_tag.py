# Generated by Django 5.0 on 2023-12-11 22:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ziraklar', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ziraklar',
            name='tag',
        ),
    ]
