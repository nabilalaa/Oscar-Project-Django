# Generated by Django 4.0.2 on 2022-02-14 23:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oscar', '0004_movie_platform_serial_platform'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='Platform',
            new_name='platform',
        ),
        migrations.RenameField(
            model_name='serial',
            old_name='Platform',
            new_name='platform',
        ),
    ]
