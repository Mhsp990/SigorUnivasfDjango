"""mainOficina URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.site.site_header="Administrador SiGOR"
admin.site.index_title="Bem vindo ao SiGOR"
admin.site.site_title="SiGOR"


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^produtos/', include('produtos.urls')),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^OS/', include('ordemServico.urls')),
    url(r'^fornecedor/', include('fornecedor.urls')),
    url(r'^conta/', include('conta.urls')),
    url(r'^cliente/', include('cliente.urls')),
    url(r'^about/$',views.about),
    url(r'^$',views.homepage, name="home"),
    url(r'^home/',views.sistema, name="sistema"),
    url(r'^veiculos/', include('veiculos.urls')),
]

urlpatterns += staticfiles_urlpatterns()