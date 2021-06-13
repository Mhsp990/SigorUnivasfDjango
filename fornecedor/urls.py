from django.conf.urls import url
from . import views

app_name='fornecedor'

urlpatterns = [
    url(r'^$',views.listarFornecedor, name="list"),
    url(r'^adicionar/$', views.adicionarFornecedor, name="adicionar"),
    url(r'^edit/(?P<pk>[\d]+)/$',   views.edit_fornecedor, name="edit"),
    url(r'^delete/(?P<pk>[\d]+)/$', views.delete_fornecedor, name="delete"),
]
