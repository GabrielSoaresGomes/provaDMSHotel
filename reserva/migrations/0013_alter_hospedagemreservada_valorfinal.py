# Generated by Django 4.0 on 2021-12-14 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reserva', '0012_alter_hospedagemreservada_dataentrada_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospedagemreservada',
            name='valorFinal',
            field=models.DecimalField(decimal_places=2, max_digits=9, null=True, verbose_name='Valor final'),
        ),
    ]