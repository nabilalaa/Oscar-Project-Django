# Generated by Django 4.0.2 on 2022-02-21 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oscar', '0031_alter_favourite_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favourite',
            name='name',
            field=models.CharField(max_length=150, null=True),
        ),
    ]