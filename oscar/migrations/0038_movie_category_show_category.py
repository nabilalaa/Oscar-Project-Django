# Generated by Django 4.0.2 on 2022-02-28 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oscar', '0037_alter_episode_name_alter_favourite_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='category',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='show',
            name='category',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
