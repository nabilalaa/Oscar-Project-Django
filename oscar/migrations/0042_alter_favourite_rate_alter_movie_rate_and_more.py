# Generated by Django 4.0.2 on 2022-03-16 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oscar', '0041_alter_favourite_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favourite',
            name='rate',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='rate',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='show',
            name='rate',
            field=models.CharField(max_length=5, null=True),
        ),
    ]
