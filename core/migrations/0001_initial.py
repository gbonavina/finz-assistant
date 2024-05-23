# Generated by Django 5.0.6 on 2024-05-17 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ativo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(default='', max_length=10)),
                ('quant', models.IntegerField(default=0)),
                ('price', models.FloatField(default=0)),
            ],
        ),
    ]
