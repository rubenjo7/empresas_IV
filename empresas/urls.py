from django.conf.urls import url

from empresas import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^(?P<empresa_id>\d+)/$', views.datos, name='datos'),
    url(r'^(?P<empresa_id>\d+)/valoraciones/$', views.valoraciones, name='valoraciones'),
    url(r'^(?P<empresa_id>\d+)/puntuaciones/$', views.puntuaciones, name='puntuaciones'),
    url(r'^add_empresa/$', views.add_empresa, name='add_empresa'),
]
