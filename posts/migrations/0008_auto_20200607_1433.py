# Generated by Django 3.0.6 on 2020-06-07 14:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_auto_20200607_1418'),
    ]

    operations = [
        migrations.RenameField(
            model_name='like',
            old_name='liked_post',
            new_name='post',
        ),
    ]
