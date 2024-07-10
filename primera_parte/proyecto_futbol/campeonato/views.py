from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext

# importar las clases de models.py
from campeonato.models import *

# Create your views here.

def listar(request):
    """
        Listar los registros del modelo Equipo,
        obtenidos de la base de datos.
    """
    # a través del ORM de django se obtiene
    # los registros de la entidad; el listado obtenido
    # se lo almacena en una variable llamada
    # equipos
    equipos = Equipo.objects.all()
    # se obtiene el número de elementos de la lista
    numero_equipos = len(equipos)
    # en la variable tipo diccionario llamada informacion_template
    # se agregará la información que estará disponible
    # en el template
    informacion_template = {'equipos': equipos, 'numero_equipos': numero_equipos}
    return render(request, 'listar_equipo.html', informacion_template)
