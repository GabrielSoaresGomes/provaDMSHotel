# Generated by Django 4.0 on 2021-12-13 20:19

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reserva', '0002_hotel_estalivre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='notaAvaliacao',
            field=models.DecimalField(decimal_places=2, max_digits=3, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)], verbose_name='Nota de Avaliação'),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='qualidadeWifi',
            field=models.DecimalField(decimal_places=2, max_digits=3, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)], verbose_name='Qualidade do WIFI'),
        ),
    ]