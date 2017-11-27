from django.shortcuts import render
from django.utils import timezone
from .models import Publicacion


# Create your views here.

def lista_publicaciones(request):
    publicaciones = Publicacion.objects.filter(fecha_publicacion__lte=timezone.now()).order_by('fecha_publicacion')
    return render(request, 'blog/lista_publicaciones.html', {'publicaciones':publicaciones})	