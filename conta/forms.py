from django import forms
from . import models

class CriarConta(forms.ModelForm):
    class Meta:
        model = models.Conta
        fields = ['conta_cliente', 'conta_fornecedor', 'OS','status', 
        'data_vencimento', 'tipo_pagamento', 'descricao']