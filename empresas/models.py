import datetime
from django.utils import timezone
from django.db import models

# Create your models here.

class Empresas (models.Model):
	"""Modelo para representar una empresa.
		
		Esta formado con el nombre de la empresa y su correo
	
	"""
	nombre = models.CharField (max_length=200)
	correo = models.CharField (max_length=200)
	#fecha_visita = models.DateField ('Fecha visita') #'%Y-%m-%d %H:%M:%S'
	
	
	def __unicode__(self):
		return self.nombre
		
	def getEmpresa(self):
		return self
		
	def deleteEmpresa(self):
		self.delete()
	

	#def fue_visitado_recientemente(self):
		#return self.fecha_visita >= timezone.now () - datetime.timedelta (days=1)


class Valoracion(models.Model):
	"""Modelo para representar una valoracion acerca de una empresa.
	
		Esta formado por un comentario y una puntuacion
		Su clave externa es la empresa con la que esta relaccionada
	"""
	empresa = models.ForeignKey (Empresas)
	comentario = models.CharField (max_length=200)
	puntuacion = models.IntegerField (default=0)
	

	def __unicode__(self):
		return self.comentario
