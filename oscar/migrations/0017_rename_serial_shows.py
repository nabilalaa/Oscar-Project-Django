# Generated by Django 4.0.2 on 2022-02-18 05:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oscar', '0016_serial_choice'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Serial',
            new_name='Shows',
        ),
    ]