# Generated by Django 4.0 on 2021-12-14 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reserva', '0015_hospedagemreservada_numeropessoas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospedagemreservada',
            name='dataEntrada',
            field=models.DateField(verbose_name='Insira a data de entrada no formato ( DD/MM/AAAA ) '),
        ),
    ]
