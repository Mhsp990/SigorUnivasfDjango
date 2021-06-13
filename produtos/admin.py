from django.contrib import admin
from .models import Produto




class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('codigo','nome','qntd')
    ordering=['codigo']


admin.site.register(Produto,ProdutoAdmin)