from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Hotel(models.Model):

    ESTABELECIMENTO_CHOICES = (
        ("Hotel", "Hotel"),
        ("Pousada", "Pousada"),
        ("Casa de Temporada", "Casa de Temporada"),
    )

    SIM_NAO_CHOICES = (
        ('Sim', "Sim"),
        ("Não", "Não")
    )
    estabelecimento = models.CharField("Estabelecimento", max_length=20, choices=ESTABELECIMENTO_CHOICES)
    cidade = models.CharField("Cidade", max_length=100)
    nomeEstabelecimento = models.CharField("Nome do Estabelecimento", max_length=100)
    preco = models.DecimalField("Preço por dia", max_digits=7, decimal_places=2, validators=[MinValueValidator(0.01)])
    notaAvaliacao = models.DecimalField("Nota de Avaliação", max_digits=2, decimal_places=1, validators=[MinValueValidator(0), MaxValueValidator(5)]) # De 0 a 5 -> ex: 4.5
    qualidadeWifi = models.DecimalField("Qualidade do WIFI", max_digits=2, decimal_places=1, validators=[MinValueValidator(0), MaxValueValidator(10)]) # De 0 a 10 -> ex: 8.9
    tvCabo = models.CharField("Tem TV a Cabo", max_length=5, choices=SIM_NAO_CHOICES)
    maximoPessoas = models.SmallIntegerField("Número máximo de pessoas", validators=[MinValueValidator(0)])
    estaLivre = models.CharField("Está livre", max_length=4, choices=SIM_NAO_CHOICES )

    def __str__(self):
        return f'{self.nomeEstabelecimento} - {self.cidade}' #Mensagem que aparece no admin