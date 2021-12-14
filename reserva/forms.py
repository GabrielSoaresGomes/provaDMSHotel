from django import forms
from django.forms import fields
from .models import HospedagemReservada

class ReservarHospedagemForm(forms.ModelForm):
    class Meta:
        model = HospedagemReservada
        fields = ["nomeHospedagemReservada", "dataEntrada", "dataSaida", "valorFinal"]
