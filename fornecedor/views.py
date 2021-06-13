from django.shortcuts import render, redirect
from . import forms
from .models import Fornecedor
from django.core.paginator import Paginator
from django.urls import reverse
# Create your views here.
def listarFornecedor(request):
    template_name = 'list.html'
    context = {}
    search =  request.GET.get('search')
    if search:
        fornecedores = Fornecedor.objects.filter(nome__icontains=search)
    else:
        fornecedores = Fornecedor.objects.all().order_by('codigo')

    # alterar fornecedores de dicionario pra array
    
    context['head'] = ['nome','tel1','tel2','end','email']
    lista = [{'col':[f.nome,f.telefone1 or '----',f.telefone2 or '----',
        f.endereço,f.email], 
        'get_edit_url':f.get_edit_url, 'get_delete_url':f.get_delete_url} 
        for f in fornecedores]
        
    paginator = Paginator(lista, 9)
    pages = request.GET.get('page')
    context['list'] = paginator.get_page(pages)
    context['title'] = "Fornecedores"
    context['back'] = reverse('fornecedor:list')
    context['add'] = reverse('fornecedor:adicionar')
    context['element'] = 'fornecedor'
    return render(request,template_name,context)

def adicionarFornecedor(request):
    
    if request.method == 'POST':
        form = forms.AdicionarFornecedor(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('cliente:listarClientes')
    else:
        form = forms.AdicionarFornecedor()
    return render(request, 'fornecedor/adicionarFornecedor.html', {'form': form})

def edit_fornecedor(request, pk):
    pass
def delete_fornecedor(request, pk):
    pass