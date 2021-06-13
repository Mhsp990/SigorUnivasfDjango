from veiculos.models import Veiculo
from django.contrib import admin
from .models import OrdemDeServico
# Register your models here.

class OsAdmin(admin.ModelAdmin):
    list_display = ('numeroOS','veiculos','data_created','status','valor')
    ordering=['numeroOS']
admin.site.register(OrdemDeServico,OsAdmin)
