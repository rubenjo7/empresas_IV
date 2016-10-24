from django.shortcuts import render, get_object_or_404
from django.template import RequestContext, loader
from django.http import HttpResponse
from empresas.models import Empresas, Valoracion
from empresas.forms import EmpresasForm


# Create your views here.
def index (request):
	"""Vista de la pagina principal de la aplicacion.
		En ella se listan las empresas que hay registradas
		Tambien da la opcion de registrar una nueva empresa
		
		:Parameters: 
             - `request`: Solicitud. 
             
	"""
	lista_ultimas_empresas = Empresas.objects.all()
	context = {'lista_ultimas_empresas': lista_ultimas_empresas}
	return render(request, 'empresas/index.html', context)

	
def datos (request, empresa_id):
	#empresa = get_object_or_404 (Empresas, pk=empresa_id)
	"""Vista de los datos de una empresa.
		
		Muestra el nombre de la empresa y el correo de contacto
		:Parameters: 
             - `request`: Solicitud.
             - `empresa_id`: Clave primaria de la empresa que va a ser procesada.  
	"""
	empresa=Empresas.objects.get(pk=empresa_id)
	return render(request, 'empresas/datos.html', {'empresa': empresa})

	
def valoraciones (request, empresa_id):
	"""Vista de las valoraciones asociadas a una empresa.
	
		Lista todas las valoraciones que una empresa ha recibido
		Muestra Correo - Puntuacion
		:Parameters: 
             - `request`: Solicitud.
             - `empresa_id`: Clave primaria de la empresa que va a ser procesada.  
	"""
	todos_valoraciones=Valoracion.objects.all().filter(empresa=empresa_id)
	context2 = {'todos_valoraciones':todos_valoraciones}
	return render(request, 'empresas/valoraciones.html', context2)
	
def puntuaciones (request, empresa_id):
	"""Vista de las puntuaciones asociadas a una empresa.
		
		Lista todas las puntuaciones que una empresa ha recibido en el proceso de valoracion
		Muestra solo las puntuaciones asociadas
		:Parameters: 
             - `request`: Solicitud.
             - `empresa_id`: Clave primaria de la empresa que va a ser procesada.  
	"""
	empresa = Empresas.objects.get(pk=empresa_id)
	puntuaciones_empresa = Valoracion.objects.filter(empresa=empresa)
	context3 = {'puntuaciones_empresa':puntuaciones_empresa}
	#puntuacion=Valoracion.objects.get(pk=empresa_id)
	return render(request, 'empresas/puntuaciones.html', context3)
	
def get_Empresa(request, empresa_id):
	emp=Empresas.objects.filter(pk=empresa_id)
	return emp
	#return render(request, 'empres', context3)
	
	


def add_empresa(request):
	"""Vista de la funcionalidad de add_empresa.
	
		Recibiendo un objeto del tipo request, analiza si se trata de datos enviados mediante un formulario.
		Comprueba que dicho formulario es valido en relacion al modelo y en caso de ser valido, alamacena en
		la base de datos la nueva empresa, devolviendo el flujo al index de la aplicacion.
		
		En caso de que el formulario no sea valido o se procese con errores, se informa de lo que esta pasando. 
		
		:Parameters: 
             - `request`: Solicitud.
		
	
	"""
    # A HTTP POST?
	if request.method == 'POST':
		form = EmpresasForm(request.POST)

        # Have we been provided with a valid form?
		if form.is_valid():
            # Save to the database.
			form.save(commit=True)

            # Now call the index() view.
            # The user will be shown the homepage.
			return index(request)
		else:
            # The supplied form contained errors - just print them to the terminal.
			print form.errors
	else:
        # If the request was not a POST, display the form to enter details.
		form = EmpresasForm()

	# Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
	return render(request, 'empresas/add_empresa.html', {'form': form})





