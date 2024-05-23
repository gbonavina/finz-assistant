# Generated by Django 5.0.6 on 2024-05-20 19:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_ativo_capitalizacao_ativo_reais_ativo_variacao_24h'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ativo',
            name='quant',
            field=models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
