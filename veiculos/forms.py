from django import forms
from . import models

class AdicionarVeiculo(forms.ModelForm):
    class Meta:
        model = models.Veiculo
        fields = ['placa', 'modelo', 'marca', 'cor', 'cliente']