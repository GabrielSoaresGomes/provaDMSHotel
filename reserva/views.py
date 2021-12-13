from django.shortcuts import render, redirect
from .models import Hotel

def listarHotel(request):
    hoteis = Hotel.objects.all()
    return render(request, "index.html", {"hoteis": hoteis})
