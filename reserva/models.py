from django.db import models

class Hotel(models.Model):

    ESTABELECIMENTO_CHOICES = (
        ("H", "Hotel"),
        ("P", "Pousada"),
        ("CT", "Casa de Temporada"),
    )

    TELEVISAO_CHOICES = (
        ('S', "Sim"),
        ("N", "Não")
    )
    estabelecimento = models.CharField("Estabelecimento", max_length=20, choices=ESTABELECIMENTO_CHOICES)
    cidade = models.CharField("Cidade", max_length=100)
    nomeEstabelecimento = models.CharField("Nome do Estabelecimento", max_length=100)
    preco = models.DecimalField("Preço", max_digits=7, decimal_places=2)
    notaAvaliacao = models.DecimalField("Nota de Avaliação", max_digits=3, decimal_places=2) # De 0 a 5 -> ex: 4.5
    qualidadeWifi = models.DecimalField("Qualidade do WIFI", max_digits=3, decimal_places=2) # De 0 a 10 -> ex: 8.9
    tvCabo = models.CharField("Tem TV a Cabo", max_length=5, choices=TELEVISAO_CHOICES)
    maximoPessoas = models.SmallIntegerField("Número máximo de pessoas")