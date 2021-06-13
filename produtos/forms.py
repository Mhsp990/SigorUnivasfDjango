from django import forms
from . import models

class AdicionarProduto(forms.ModelForm):
    class Meta:
        model = models.Produto
        fields = ['codigo', 'nome', 'tipo', 'qntd', 'unit','preco_compra', 'preco_venda']