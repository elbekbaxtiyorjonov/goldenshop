# Generated by Django 5.0 on 2023-12-11 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hodimlar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=255)),
                ('familya', models.CharField(max_length=255)),
                ('nomer', models.CharField(max_length=255)),
                ('email', models.EmailField(blank=True, max_length=255)),
                ('murojat', models.CharField(max_length=255)),
            ],
        ),
    ]
