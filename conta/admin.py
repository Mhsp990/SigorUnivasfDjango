from veiculos.models import Veiculo
from django.contrib import admin
from .models import Conta
# Register your models here.

class ContaAdmin(admin.ModelAdmin):
    list_display = ('Clientes','status','data_emissao','data_vencimento','Valor')
    ordering=['data_vencimento']

    def Valor(self,obj):
        return "R$  "+str(obj.OS.valor) 

    def Clientes(self, obj ):
        return obj.conta_cliente.nome


admin.site.register(Conta,ContaAdmin)