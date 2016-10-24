from django import forms
from empresas.models import Empresas, Valoracion
from datetime import date, datetime

class EmpresasForm(forms.ModelForm):
	nombre = forms.CharField(max_length=128, help_text="Inserte nombre empresa.")
	correo = forms.CharField(max_length=128, help_text="Inserte correo empresa.")
	#fecha_visita=forms.DateTimeField(initial=datetime.datetime.fecha_visita)
	#fecha_visita=forms.DateField(initial=date.today)
	#fecha_visita = forms.DateTimeField(initial='2015-10-20 10:58:49')

    # An inline class to provide additional information on the form.
	class Meta:
        # Provide an association between the ModelForm and a model
		model = Empresas
		fields = ('nombre',)
		
		
		#exclude = ('fecha_visita',)

		


class ValoracionForm(forms.ModelForm):
	comentario = forms.CharField(max_length=128, help_text="Comentario de la valoracion")
	puntuacion= forms.IntegerField(widget=forms.HiddenInput(), initial=0)

	class Meta:
        # Provide an association between the ModelForm and a model
		model = Valoracion

        # What fields do we want to include in our form?
        # This way we don't need every field in the model present.
        # Some fields may allow NULL values, so we may not want to include them...
        # Here, we are hiding the foreign key.
        # we can either exclude the category field from the form,
		exclude = ('empresa',)
        #or specify the fields to include (i.e. not include the category field)
        #fields = ('title', 'url', 'views')
