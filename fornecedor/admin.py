from django.contrib import admin
from .models import Fornecedor
# Register your models here.

class FornecedorAdmin(admin.ModelAdmin):
    list_display = ('nome','telefone1','telefone2')
    ordering=['nome']
admin.site.register(Fornecedor,FornecedorAdmin)