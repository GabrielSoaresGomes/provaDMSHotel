# Generated by Django 4.0 on 2021-12-13 23:15

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reserva', '0004_alter_hotel_maximopessoas_alter_hotel_preco'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='estabelecimento',
            field=models.CharField(choices=[('Hotel', 'Hotel'), ('Pousada', 'Pousada'), ('Casa de Temporada', 'Casa de Temporada')], max_length=20, verbose_name='Estabelecimento'),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='preco',
            field=models.DecimalField(decimal_places=2, max_digits=7, validators=[django.core.validators.MinValueValidator(0.01)], verbose_name='Preço por dia'),
        ),
    ]