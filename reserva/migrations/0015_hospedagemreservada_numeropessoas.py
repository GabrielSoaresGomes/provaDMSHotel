# Generated by Django 4.0 on 2021-12-14 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reserva', '0014_alter_hospedagemreservada_valorfinal'),
    ]

    operations = [
        migrations.AddField(
            model_name='hospedagemreservada',
            name='numeroPessoas',
            field=models.SmallIntegerField(default=0, verbose_name='Número de pessoas'),
            preserve_default=False,
        ),
    ]
