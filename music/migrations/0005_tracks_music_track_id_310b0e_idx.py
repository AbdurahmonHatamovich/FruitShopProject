# Generated by Django 5.0.4 on 2024-05-11 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0004_alter_tracks_options'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='tracks',
            index=models.Index(fields=['id'], name='music_track_id_310b0e_idx'),
        ),
    ]