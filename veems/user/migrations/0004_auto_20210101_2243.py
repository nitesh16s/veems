# Generated by Django 3.1.4 on 2021-01-01 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20201231_2153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(
                blank=True, max_length=150, null=True, verbose_name='username'
            ),
        ),
    ]