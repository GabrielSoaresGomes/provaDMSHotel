from django.urls import path, include
from .views import listarHospedagem, reservarHospedagem

urlpatterns = [
    path('',listarHospedagem, name="listarHospedagem"),
    path('reservar/<int:id>', ),
    path('reservados')
]
