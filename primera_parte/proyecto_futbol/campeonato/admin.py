from django.contrib import admin

# Importar las clases del modelo
from campeonato.models import Equipo

# Agregar la clase Equipo para administrar desde
# interfaz de administración
admin.site.register(Equipo)
