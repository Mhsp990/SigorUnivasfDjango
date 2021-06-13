from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .models import OrdemDeServico
from . import forms
from cliente import models as modelCliente
from veiculos import models as modelVeiculos
# Create your views here.

@login_required(login_url='login')
def listarOrdemServico(request):
    
    OSlist = OrdemDeServico.objects.all()
    return render(request, 'ordemServico/ordemServico_list.html',{'OSlist':OSlist})



@login_required(login_url='login')
def criarOrdemServico(request):
    if request.method == 'POST':
    
        #cpf_usuario = request.POST.get("cpf_usuario")
        #cliente = modelCliente.Cliente.objects.get(pk=cpf_usuario)
          
        #placa_veiculo = request.POST.get("placa_veiculo")
        #veiculos = modelVeiculos.Veiculo.objects.get(pk=placa_veiculo)

        #status = request.POST.get("status")
        #OS = OrdemDeServico(cliente=cliente, veiculos=veiculos, status=status)
        #OS.save()
        form = forms.CriarOrdemServico(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('ordemServico:listarOrdemServico')
    
    else:
        form = forms.CriarOrdemServico()
    return render(request, 'ordemServico/criarOrdemServico.html', {'form': form})


    
