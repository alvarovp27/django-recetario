#encoding:utf-8
# Create your views here.
from principal.models import Bebida, Receta, User, Comentario
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.core.mail import EmailMessage
from principal.forms import ContactoForm, RecetaForm, ComentarioForm

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
    comentarios = Comentario.objects.filter(receta=dato)
    return render_to_response('receta.html', {'receta': dato, 'comentarios': comentarios})

def contacto(request):
    if request.method == 'POST':
        formulario = ContactoForm(request.POST)
        if formulario.is_valid():
            titulo = 'Mensaje desde el recetario de Maestros del Web'
            contenido = formulario.cleaned_data['mensaje'] + '\n'
            contenido += 'Comunicarse a: '+formulario.cleaned_data['correo']
            correo = EmailMessage(titulo, contenido, to=['avalenciaparra@gmail.com'])
            correo.send()
            return HttpResponseRedirect('/')
    else:
        formulario = ContactoForm()
    return render_to_response('contactoform.html', {'formulario': formulario}, context_instance=RequestContext(request))

def nueva_receta(request):
    if request.method == 'POST':
        formulario = RecetaForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/recetas')
    else:
        formulario = RecetaForm()
    return render_to_response('recetaform.html', {'formulario': formulario}, context_instance=RequestContext(request))

def nuevo_comentario(request):
    if request.method == 'POST':
        formulario = ComentarioForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/recetas')
    else:
        formulario = ComentarioForm()
    return render_to_response('comentarioform.html', {'formulario': formulario}, context_instance=RequestContext(request))