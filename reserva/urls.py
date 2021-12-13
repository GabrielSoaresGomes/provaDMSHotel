from django.urls import path, include
from .views import listarHotel

urlpatterns = [
    path('',listarHotel, name="listarHotel")
]
