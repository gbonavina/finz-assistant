# Generated by Django 5.0.6 on 2024-05-21 01:09

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='last_update',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
