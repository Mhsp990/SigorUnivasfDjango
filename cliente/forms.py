from django import forms
import re
from . import models

class AdicionarCliente(forms.ModelForm):
    class Meta:
        model = models.Cliente
        fields = ['cpf', 'nome']
    
    def clean_cpf(self):
        
        cpf = self.cleaned_data.get('cpf')
        if len(cpf) < 11:
            raise forms.ValidationError("O CPF deve ser composto por 11 dígitos")

        result = re.search("[0-9]{11}", cpf)
        if result is None:
            raise forms.ValidationError("O CPF deve ser composto apenas por dígitos")
        return cpf