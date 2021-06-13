from django.conf.urls import url
from . import views

app_name='cliente'

urlpatterns = [
    url(r'^list/$', views.listarClientes, name="listarClientes"),
    url(r'^adicionarCliente/$', views.adicionarCliente, name="adicionarCliente"),
]
