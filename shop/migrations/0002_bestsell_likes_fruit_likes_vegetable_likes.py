# Generated by Django 5.0.4 on 2024-05-12 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bestsell',
            name='likes',
            field=models.PositiveBigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='fruit',
            name='likes',
            field=models.PositiveBigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='vegetable',
            name='likes',
            field=models.PositiveBigIntegerField(default=0),
        ),
    ]
