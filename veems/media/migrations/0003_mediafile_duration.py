# Generated by Django 3.1.3 on 2020-12-05 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0002_mediafilethumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='mediafile',
            name='duration',
            field=models.IntegerField(null=True),
        ),
    ]