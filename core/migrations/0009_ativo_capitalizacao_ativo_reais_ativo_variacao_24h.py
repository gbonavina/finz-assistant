# Generated by Django 5.0.6 on 2024-05-20 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_alter_ativo_cotacao'),
    ]

    operations = [
        migrations.AddField(
            model_name='ativo',
            name='capitalizacao',
            field=models.CharField(default='', max_length=25),
        ),
        migrations.AddField(
            model_name='ativo',
            name='reais',
            field=models.CharField(default='', max_length=25),
        ),
        migrations.AddField(
            model_name='ativo',
            name='variacao_24h',
            field=models.CharField(default='', max_length=25),
        ),
    ]
