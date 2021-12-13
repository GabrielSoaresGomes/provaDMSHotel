# Generated by Django 4.0 on 2021-12-13 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reserva', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='estaLivre',
            field=models.CharField(choices=[('S', 'Sim'), ('N', 'Não')], default='Sim', max_length=4, verbose_name='Está livre'),
            preserve_default=False,
        ),
    ]
