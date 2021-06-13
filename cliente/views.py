from django.shortcuts import render, redirect
from . import forms
from .models import Cliente
# Create your views here.
def listarClientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'cliente/clienteList.html',{'clientes':clientes})

def adicionarCliente(request):
    
    if request.method == 'POST':
        form = forms.AdicionarCliente(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('cliente:listarClientes')
    else:
        form = forms.AdicionarCliente()
    return render(request, 'cliente/adicionar_cliente.html',  {'form': form})