from django.urls import path, include
from .views import listarHospedagem

urlpatterns = [
    path('',listarHospedagem, name="listarHospedagem")
]
