from django.shortcuts import render 
from eventos.models import Certificado, Evento


def meus_certificados(request):
    certificados = Certificado.objects.filter(participante=request.user)
    return render(request, 'meus_certificados.html', {'certificados': certificados})

def meus_eventos(request):
    if request.method == "GET":
        user = request.GET.get('user')

        eventos = Evento.objects.filter(criador=request.user)
        
        print(eventos)

        if user:
            eventos = eventos.filter(nome__contains=user)

        return render(request, 'meus_eventos.html', {'meus_eventos': meus_eventos})
