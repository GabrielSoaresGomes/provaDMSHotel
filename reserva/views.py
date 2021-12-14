from django.shortcuts import render, redirect
from .models import Hospedagem

def listarHospedagem(request):
    hospedagens = Hospedagem.objects.all()
    return render(request, "index.html", {"hospedagens": hospedagens})

def reservarHospedagem(request, id):
    ""