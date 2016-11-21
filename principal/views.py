# Create your views here.
from principal.models import Bebida, Receta, User
from django.shortcuts import render_to_response
from django.http import HttpResponse

def lista_bebidas(request):
    bebidas = Bebida.objects.all()
    return render_to_response('lista_bebidas.html', {'lista':bebidas})

def sobre(request):
    html = '<html><body>Proyeto de ejemplo</body></html>'
    return HttpResponse(html)

def inicio(request):
    recetas = Receta.objects.all()
    return render_to_response('inicio.html', {'recetas': recetas})

def usuarios(request):
    users = User.objects.all()
    recetas = Receta.objects.all()
    return render_to_response('usuarios.html', {'usuarios': users, 'recetas': recetas})