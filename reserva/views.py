from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Hospedagem, HospedagemReservada
from .forms import ReservarHospedagemForm


@login_required
def listarHospedagem(request):
    hospedagens = Hospedagem.objects.all()
    search = request.GET.get('search', '')
    if search:
        hospedagens = Hospedagem.objects.filter(nomeEstabelecimento__icontains=search, )
    return render(request, "index.html", {"hospedagens": hospedagens})


@login_required
def reservarHospedagem(request, id):
    hospedagem = Hospedagem.objects.get(id=id)
    hospedagem.estaLivre = "Não"
    formulario = ReservarHospedagemForm(request.POST or None)
    if formulario.is_valid():
        formulario.save()
        hospedagem.save()
        return redirect('hospedagensReservadas')
    return render(request, 'finalizarReserva.html', {"formulario": formulario, "hospedagem": hospedagem})


@login_required
def hospedagensReservadas(request):
    hospedagens = HospedagemReservada.objects.all()

    return render(request, "hospedagensReservadas.html", {"hospedagens": hospedagens})

