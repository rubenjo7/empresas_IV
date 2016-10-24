from django.contrib import admin

# Register your models here.

from empresas.models import Empresas,Valoracion

#class ValoracionAdmin(admin.ModelAdmin):
#	model = Valoracion
#	extra=2
	
#class EmpresasAdmin(admin.ModelAdmin):
#	fieldsets = [
#		(None,				{'fields': ['nombre']}),
#		(None,				{'fields': ['correo']}),
#		('Fecha visita',	{'fields': ['fecha_visita'], 'classes': ['collapse']}),
		
#	]
	#inline = [linea_valoracion]
#	list_display = ('nombre','correo','fecha_visita')
#	list_filter = ['fecha_visita']
#	search_fields = ['nombre']

admin.site.register(Empresas)
admin.site.register(Valoracion)
