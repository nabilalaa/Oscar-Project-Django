# Generated by Django 4.0.2 on 2022-02-18 05:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oscar', '0019_episode_movie_durations_shows_durations'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Shows',
            new_name='Show',
        ),
    ]
