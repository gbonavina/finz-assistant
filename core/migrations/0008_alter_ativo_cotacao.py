# Generated by Django 5.0.6 on 2024-05-18 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_ativo_p_l_ativo_tipo_ativo_variacao_24m_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ativo',
            name='cotacao',
            field=models.CharField(default='', max_length=25),
        ),
    ]