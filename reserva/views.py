from django.shortcuts import render, redirect
from .models import Hotel

def listarHospedagem(request):
    hospedagens = Hotel.objects.all()
    return render(request, "index.html", {"hospedagens": hospedagens})

def reservarHospedagem(request, id):
    ""