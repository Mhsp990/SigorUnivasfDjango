from django import forms
from . import models

class CriarOrdemServico(forms.ModelForm):
    class Meta:
        model = models.OrdemDeServico
        fields = ['cliente', 'veiculos', 'valor','status','produtos', 'funcionario', 'descricao']
      