# Generated by Django 5.0.4 on 2024-05-11 17:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_tracks_listened'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tracks',
            options={'ordering': ('id',)},
        ),
    ]