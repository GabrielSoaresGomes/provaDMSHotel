from django import forms
from django.forms import fields, widgets
from .models import HospedagemReservada


class InputTypeData(forms.DateInput):     
    input_type = 'date'


class ReservarHospedagemForm(forms.ModelForm):
    class Meta:
        model = HospedagemReservada
        fields = [ "nomeHospedagemReservada","dataEntrada", "numeroDias", "valorFinal", "numeroPessoas"]
        widgets = {
            "dataEntrada": InputTypeData()
        }


