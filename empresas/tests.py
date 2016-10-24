from django.test import TestCase

# Create your tests here.

from empresas.models import Empresas
from empresas.views import *


class EmpresasMethodTests(TestCase):

	def test_crea_empresa(self):
		emp = Empresas(nombre='etest',correo='ctest')
		emp.save()
		self.assertEqual(emp.nombre, 'etest')
		self.assertEqual(emp.correo, 'ctest')
		
	def test_devuelve_empresa(self):
		emp2 = Empresas(nombre="empresa_prueba",correo="correo_prueba")
		emp2.save()
		emp3=Empresas(nombre=" ",correo=" ")
		emp3=emp2.getEmpresa()
		self.assertEquals(emp3.nombre, emp2.nombre)
		
	
