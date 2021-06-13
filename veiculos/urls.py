
from django.conf.urls import url
from . import views

app_name='veiculos'

urlpatterns = [
    url(r'^list/$',views.veiculos_list, name="listarVeiculos"),
    url(r'^adicionarVeiculo/$',views.adicionarVeiculos, name="adicionarVeiculo"),
    url(r'^(?P<placa>[\w-]+)/$',views.veiculo_detail, name="detailv"),
]
