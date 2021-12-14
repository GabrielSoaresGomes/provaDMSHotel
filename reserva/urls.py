from django.urls import path, include
from .views import listarHospedagem, reservarHospedagem, hospedagensReservadas

urlpatterns = [
    path('',listarHospedagem, name="listarHospedagem"),
    path('reservar/<int:id>', reservarHospedagem, name="reservarHospedagem" ),
    path('reservados', hospedagensReservadas, name="hospedagensReservadas"),
]
