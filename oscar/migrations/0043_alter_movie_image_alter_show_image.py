# Generated by Django 4.0.2 on 2023-04-20 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oscar', '0042_alter_favourite_rate_alter_movie_rate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='image',
            field=models.ImageField(null=True, upload_to='Movies'),
        ),
        migrations.AlterField(
            model_name='show',
            name='image',
            field=models.ImageField(null=True, upload_to='Series'),
        ),
    ]
