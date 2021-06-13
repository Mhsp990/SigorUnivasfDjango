from django.contrib import admin
from .models import Funcionario
# Register your models here.

class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('nome','cargo',)
    ordering=['nome']
admin.site.register(Funcionario,FuncionarioAdmin)