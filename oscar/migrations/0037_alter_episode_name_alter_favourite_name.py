# Generated by Django 4.0.2 on 2022-02-25 05:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('oscar', '0036_remove_show_video_alter_favourite_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='episode',
            name='name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='oscar.show'),
        ),
        migrations.AlterField(
            model_name='favourite',
            name='name',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
