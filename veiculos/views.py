from veiculos.forms import AdicionarVeiculo
from django.shortcuts import redirect, render
from . import forms
# Create your views here.
from .models import Veiculo
from django.http import HttpResponse
# Create your views here.

def veiculos_list(request):
    veiculos=Veiculo.objects.all().order_by('placa')
    return render(request,'veiculos/veiculos_list.html',{'veiculos':veiculos})

def adicionarVeiculos(request):
    if request.method == 'POST':
        form = forms.AdicionarVeiculo(request.POST, request.FILES)
        form.save()
    else:  
        form = forms.AdicionarVeiculo()
        redirect('veiculos:listarVeiculos')
    return render(request, 'veiculos/adicionarVeiculo.html', {'form': form})



def veiculo_detail(request, placa):
    #return HttpResponse(codigo)
    veiculo=Veiculo.objects.get(placa=placa)
    return render(request,'veiculos/veiculo_detail.html',{'veiculos':veiculo})
