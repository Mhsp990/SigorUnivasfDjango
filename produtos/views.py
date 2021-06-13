from django.shortcuts import render, redirect
from .models import Produto
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from . import forms
from django.urls import reverse
from .utils import intcomma
# Create your views here.

@login_required(login_url='login')
def listagem(request):
    template_name = 'list.html'
    context = {}
    search =  request.GET.get('search')
    if search:
        produtos = Produto.objects.filter(nome__icontains=search)
    else:
        produtos = Produto.objects.all().order_by('codigo')

    # alterar produtos de dicionario pra array
    context['head'] = ['Cod','Nome','Tipo','Preço de compra (R$)','Preço de venda (R$)','Estoque']
    lista = [{'col':[p.codigo, p.nome, p.tipo, intcomma(p.preco_compra), 
            intcomma(p.preco_venda), p.qntd], 
        'get_edit_url':p.get_edit_url, 'get_delete_url':p.get_delete_url} 
        for p in produtos]
        
    paginator = Paginator(lista, 9)
    pages = request.GET.get('page')
    context['list'] = paginator.get_page(pages)
    context['title'] = "Produtos"
    context['back'] = reverse('produtos:list')
    context['add'] = reverse('produtos:adicionar')
    context['element'] = 'produto'
    return render(request,template_name,context)

@login_required(login_url='login')
def produtos_list(request):

    
    search =  request.GET.get('search')
    if search:
        produtos = Produto.objects.filter(nome__icontains=search)
    else:
        produtos = Produto.objects.all().order_by('codigo')

    paginator = Paginator(produtos, 9)
    pages = request.GET.get('page')
    produtos = paginator.get_page(pages)
    return render(request,'produtos/produtos_list.html',{'produtos':produtos})

@login_required(login_url='login')
def produto_detail(request, codigo):
    #return HttpResponse(codigo)
    produto=Produto.objects.get(codigo=codigo)
    return render(request,'produtos/produto_detail.html',{'produto':produto})

@login_required(login_url='login')
def produto_adicionar(request):
    if request.method == 'POST':
        form = forms.AdicionarProduto(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False) #Impede que dado seja gravado no banco
            #instance.author = request.user
            instance.save()
            return redirect('produtos:list')
    else:
        form = forms.AdicionarProduto()
    return render(request, 'produtos/produto_adicionar.html', {'form': form})
  

@login_required(login_url='login')  
def teste(request):
    data = Produto.objects.all().order_by('codigo')
    render(request, 'produtos/produto_adicionar.html', {data:data})


@login_required(login_url='login')  
def edit_produto(request, pk):
    #produtos = Produto.objects.get(pk=pk)
    #produtos = 0
    #form = forms.AdicionarProduto(instance=produtos)
    #return render(request, 'produtos/produto_adicionar.html', {'form': form})
    data = {}
    data['produto'] = Produto.objects.get(pk=pk)
    data['form'] = forms.AdicionarProduto(instance=data['produto'])
    
    return render(request, 'produtos/produto_adicionar.html', data)


@login_required(login_url='login')
def update_produto(request, pk):
    data = {}
    data['produto'] = Produto.objects.get(pk=pk)
    form = forms.AdicionarProduto(request.POST or None, instance=data['produto'])
    if form.is_valid(): 
        form.save()
    return redirect('produtos:list')


@login_required(login_url='login')
def delete_produto(request, pk):
    produto = Produto.objects.get(pk=pk)
    produto.delete()
    return redirect('produtos:list')