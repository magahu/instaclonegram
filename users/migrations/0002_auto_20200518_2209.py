# Generated by Django 2.2.12 on 2020-05-18 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='biography',
            field=models.TextField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='profile',
            name='website',
            field=models.URLField(blank=True, max_length=70),
        ),
    ]
