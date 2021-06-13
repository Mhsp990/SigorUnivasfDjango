
from django.conf.urls import url
from . import views

app_name='produtos'

urlpatterns = [
    url(r'^$',views.listagem, name="list"),#produtos_list
    url(r'^adicionar/$', views.produto_adicionar, name="adicionar"),
    url(r'^teste/$', views.produto_adicionar, name="adicionar"),
    url(r'^edit/(?P<pk>[\d]+)/$', views.edit_produto, name="edit"),
    url(r'^update/(?P<pk>[\d]+)/$', views.update_produto, name="update"),
    url(r'^delete/(?P<pk>[\d]+)/$', views.delete_produto, name="delete"),
    url(r'^(?P<codigo>[\w-]+)/$',views.produto_detail, name="detail"),
]
