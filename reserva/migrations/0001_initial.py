# Generated by Django 4.0 on 2021-12-13 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estabelecimento', models.CharField(choices=[('H', 'Hotel'), ('P', 'Pousada'), ('CT', 'Casa de Temporada')], max_length=20, verbose_name='Estabelecimento')),
                ('cidade', models.CharField(max_length=100, verbose_name='Cidade')),
                ('nomeEstabelecimento', models.CharField(max_length=100, verbose_name='Nome do Estabelecimento')),
                ('preco', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Preço')),
                ('notaAvaliacao', models.DecimalField(decimal_places=2, max_digits=3, verbose_name='Nota de Avaliação')),
                ('qualidadeWifi', models.DecimalField(decimal_places=2, max_digits=3, verbose_name='Qualidade do WIFI')),
                ('tvCabo', models.CharField(choices=[('S', 'Sim'), ('N', 'Não')], max_length=5, verbose_name='Tem TV a Cabo')),
                ('maximoPessoas', models.SmallIntegerField(verbose_name='Número máximo de pessoas')),
            ],
        ),
    ]
