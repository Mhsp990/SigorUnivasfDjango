from django.contrib import admin
from .models import Cliente
# Register your models here.

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome','telefone1')
    ordering=['nome']

admin.site.register(Cliente,ClienteAdmin)