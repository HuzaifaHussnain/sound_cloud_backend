# Generated by Django 3.1 on 2020-08-12 07:25

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('song', '0003_song_media_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='likes',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]