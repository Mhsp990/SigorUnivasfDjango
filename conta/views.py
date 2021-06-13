from django.shortcuts import render, redirect
from .models import Conta
from . import forms

# Create your views here.
def listarContas(request):
    contas = Conta.objects.all()
    return render(request, 'conta/contaList.html', {'contas':contas})


def criarConta(request):
    if request.method == 'POST':
        form = forms.CriarConta(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('conta:listarContas')
    else:
        form = forms.CriarConta()
    return render(request, 'conta/criarConta.html', {'form':form})
