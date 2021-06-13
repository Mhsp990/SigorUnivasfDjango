from django.conf.urls import url
from . import views

app_name='conta'

urlpatterns = [
    url(r'^list/$', views.listarContas, name="listarContas"),
    url(r'^criarConta/$', views.criarConta, name="criarConta"),
]
