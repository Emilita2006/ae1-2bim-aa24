from django.db import models

class Equipo(models.Model):
    nombre = models.CharField(max_length=30)
    siglas = models.CharField(max_length=30)
    seguidores = models.IntegerField()
    campeonatos = models.IntegerField()
    estadio = models.CharField(max_length=100)

    def __str__(self):
        return """Nombre: %s - Siglas: %s \n
                Seguidores: %d\n
                Campeonatos: %d\n
                Estadio: %s""" % (self.nombre,
                self.siglas,
                self.seguidores,
                self.campeonatos,
                self.estadio)
