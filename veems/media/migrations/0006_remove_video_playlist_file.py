# Generated by Django 3.1.4 on 2020-12-20 21:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0005_upload_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='playlist_file',
        ),
    ]