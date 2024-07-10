"""
    Manejo de urls para la aplicación
"""
from django.urls import path
# se importa las vistas de la aplicación
from . import views


urlpatterns = [
        path('listar', views.listar, name='listar'),
        path('', views.listar, name='listar'),
 ]
