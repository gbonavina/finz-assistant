# Generated by Django 5.0.6 on 2024-05-17 22:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_ativo_usuario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ativo',
            name='usuario',
        ),
    ]
