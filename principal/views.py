#encoding:utf-8
# Create your views here.
from principal.models import Bebida, Receta, User
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext

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

def lista_recetas(request):
    recetas = Receta.objects.all()
    #context_instance -> we've to use this parameter for accessing to the image
    #return render_to_response('recetas.html', {'recetas': recetas}, context_instance=RequestContext(request))
    #RequestContext did not work because it did not give me the right uri to obtain the path of "carga" folder
    #so i had to do a work around
    return render_to_response('recetas.html', {'recetas': recetas})

def detalle_receta(request, id_receta):
    dato = get_object_or_404(Receta, pk=id_receta)
    return render_to_response('receta.html', {'receta': dato})