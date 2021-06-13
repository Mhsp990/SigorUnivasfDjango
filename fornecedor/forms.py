from django import forms
from . import models

class AdicionarFornecedor(forms.ModelForm):
    class Meta:
        model = models.Fornecedor
        fields = ['codigo']