# Generated by Django 4.0.2 on 2022-02-21 22:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oscar', '0032_alter_favourite_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favourite',
            name='user',
        ),
    ]
