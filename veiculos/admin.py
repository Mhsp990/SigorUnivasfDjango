from django.contrib import admin
from .models import Veiculo
# Register your models here.
class VeiculoAdmin(admin.ModelAdmin):
    list_display = ('modelo','marca','placa')
    ordering=['placa']

admin.site.register(Veiculo,VeiculoAdmin)
